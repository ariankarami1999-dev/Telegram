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
<img src="https://cdn4.telesco.pe/file/pAOfAhPescjWXlVXVusE6LBGN2pif_OUhruW9FKiLYXjNTaVKpID9h37MRICjH2KPklEiNUpKMgFc38Zf9A9X8i48RNToYqCxQECocyMNtsDUWI0s_nhu_4_YTwZWnULe0AXi3AR_aJDc8Q6ts-5LZrpFjRVLBPa7eDZd1uqMzcbBTNaBFKsgIx7A2JeajF8Nxzl5qTKp_Hw2CzoTYW4d9_OPyC1oa62umhGx5ksOtTBVW2U4BbY9IK8y9OCL1eMpnYTwOQeAvQSJdZ8z-syYn5lcw1BKWEeOUxpSXMwK0yQ_ayxYp1zIghsNv0BkuRsQtw1TUJ3hsu7SWLYz7aAcw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.23M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 05:55:40</div>
<hr>

<div class="tg-post" id="msg-656496">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
دو پایگاه هوایی و تاسیسات مهم باقی‌مانده در ناوگان پنجم نیروی دریایی آمریکا هدف قرار گرفتند
🔹
روابط عمومی سپاه پاسداران انقلاب اسلامی از هدف قرار گرفتن دو پایگاه هوایی آمریکا در کویت به نام‌های علی‌السالم و تاسیسات مهم باقی مانده در ناوگان پنجم نیروی دریایی آمریکا در بحرین در پاسخ به تجاوز ارتش کودک‌کش آمریکا خبر داد.
متن بیانیه سپاه به این شرح است:
بسم الله القاصم الجبارین
فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ
ساعت ۱:۳۰ بامداد امروز چهار فروند نفتکش متخلف با تحریک و هدایت ارتش متجاوز آمریکا بدون هماهنگی و بدون توجه به اخطارهای مکرر نیروی دریایی سپاه، قصد خروج غیر قانونی از تنگه هرمز را داشتند که پس از اخطار، یکی از نفتکش ها مورد هدف واقع شده و متوقف شد و دیگر شناورها متخلف به عقب برگشتند.
به دنبال این واقعه ساعت ۲:۳۰ بامداد، پهپادهای آمریکایی یک دکل مخابراتی در قشم و یک دکل را در سیریک مورد اصابت دو پرتابه قرار دادند. در پاسخ به تجاوز ارتش کودک کش آمریکا بلافاصله دو پایگاه هوایی آمریکا در کویت به نامهای علی‌السالم و تاسیسات مهم باقی مانده در ناوگان پنجم نیروی دریایی آمریکا در بحرین هدف آتش موشک های بالستیک نیروی هوافضای سپاه واقع شدند.
به دشمن متجاوز و کودک‌کش اخطار می کنیم در صورت تکرار این شرارت ها به پاسخ محدود اکتفا نخواهد شد. مسئول عواقب بسته شدن کامل تنگه هرمز به روی خروج نفت و گاز شما خواهید بود.
و ما النصر الا من عند الله العزیز الحکیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 713 · <a href="https://t.me/akhbarefori/656496" target="_blank">📅 05:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656491">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQrt6vSCeImYiJRSJuUQTMn1TsIqdrL4jYpG8bYIsQXkT7fmY7b1XA9_Mr7tcnzlRykeoX1T1-2aeQVLXKffsAarFUyA8ghaedy9hd2RAh14k8n9Hx2MgEU6PH8Z_dqNZJeBweEUTS5wkIKvAkvJZVy_t9E7uDp3uMPnvw9WtWRP47-hLqrXuWs57bC_UxDXen4gSQEpmze0s8wsPMAbIrtOMfj87JmO6sdi-7kqczS82hc3-_kaSMMp_lwdms5DBICD-lnFU_up64A85eRtEFUCOu9mUMB0_xVLO5E9zOs7xvkXZFHWNimSSxpbVFc3gNJZ-zW6CigP0oAc-arURg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/656491" target="_blank">📅 00:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656489">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mh6eGA-DShhbwgIz9uJkb93GEWAHKqX-uQEDJLxBYrTuMraD8t1ZFVOzp0deraL735ZnZGhNfOsrxLN3MLRnO0kXhkka78pQbTp3eUy0auKyDHHdvQPFvU983xH5XdCN60TLVdlLD7-kdZBSUeg7trcrIx_dk44KPjiT3Z9K0CHEdCojxCMMZY4mEJcTuFUnYMYyVIF-jisB4j2v3rzXrVtnjlxOxx6Tpmj97WVDsWgReGz0KRll-iIo9AkM6_-Y-foAZRGp6n1js9H2-8arKPQgwN2Xl0_3aKOAhfiKgU6M6xV-JVilMW0Bb0vZlDOcgiO53v3sftkBWpicla06NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش سنتکام به شلیک اخطار ارتش به سمت ناوشکن‌های متجاوز آمریکا  ادعای ستاد فرماندهی مرکزی ارتش تروریستی آمریکا:
🔹
شلیک‌های اخطار از سوی ایران برای هشدار به کشتی‌های آمریکایی در دریای عمان و عقب راندن آنها نادرست است.
🔹
لازم به ذکر است پس از شلیک های اخطارِ…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/656489" target="_blank">📅 23:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656488">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0LUvut5j_E6LfyM0Xj-Amkphn24VthyGtHvvHrnWmHSKI-Ljyl4noPPZp9InMgHiDywAKSKVMyT_cf6ZyYIoIoAaQxCviCtkgQ_g2qYCB2Yks6skKuNqfxJWl-aeRQCuMMMg-kvqfXmoJN_nOjxsL4YbegFWMWnPGSF4s-AWV3rn_OAlgo58uSd57HppY5mrc4Zxarfp3hn9ZazTYL1sWDEnsK50d4vWZb1M7HH_5GN82ScAVRAfdLkCnMUqt-6isAPI97W5ROUi4kTDqckgoTyJjSxlewWcWEaBrb_CGuP5JnZk4mTr9o_1-QsfEjPqXwBIgkkgbneAQEIbEg0sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سگ زرد: در حال بررسی ارسال سلاح به تایوان هستیم
رئیس‌جمهور آمریکا:
🔹
در حال بررسی امکان ارسال بسته تسلیحاتی  ۱۴ میلیارد دلاری به تایوان هستیم.
🔹
هنوز درباره ارسال کردن یا نکردن این بسته تسلیحاتی به تایوان تصمیم نگرفته‌ایم.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/656488" target="_blank">📅 23:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656487">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hd3_iDBNONAkZDbx4pVU5YKPqK88P3IDevmeUbQNMHi6KNuKmMDCGaNjgLTaCK7NK4kflnEOL9ealk81rUzHqmSuJNpm6nnsmw0C6aJqAZxxl-3cwXcw5-IA6foxQig-t_LG5e0mMsCMZwa8x0PopZ5YRUYoy5WPNCSdoDqZ2oX4IF4-A5x3uX8_UjZS-xgz9YhkkB8MT46cHfY3EGnt0_fuLYJ3QG-wEVnTP5vw5j2KdT3bFmCkzxrj5Km8zW1xes4WRIjih-so6T9v3a-qOkcojzaDf_0P0zAwIhJFWKPTbH45lFUgDe0gW4hxK1YtS_EDna-i2nWDTweWCtNdhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری تماشایی از قله دالانپر ارومیه
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/656487" target="_blank">📅 23:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656486">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a55273f8b.mp4?token=atPgiaEHnWhP0WA825jAQEWZRWSLxyXqwDNBTElIHxv9fTtZJDgE3Mna3MLdkcyU4XEkNU69sa5t_QdRGaIwg0qzDR9sDabUg-U6zPvI3f-x6HFeO-KiDPVDNXZ2ftgERvtKQUiLnTAojVx1o75LLA1IeqHIUmEQhoqLEz1cI0iK2M0Idf3zUIe0XJo6xkWDp0gq0lN3Dr02G_kPCH7gDwst5GsILWjRvnxFv5Ass5alqSkhWmrV3GRbFXMs37ZuaML6z4lNFLkBjo8VOtPtBDAFN3GePpjCp4iotclNsrvalWL2updIqFZXU39SutfKXzILT1R6VU_6RRsknT59toWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a55273f8b.mp4?token=atPgiaEHnWhP0WA825jAQEWZRWSLxyXqwDNBTElIHxv9fTtZJDgE3Mna3MLdkcyU4XEkNU69sa5t_QdRGaIwg0qzDR9sDabUg-U6zPvI3f-x6HFeO-KiDPVDNXZ2ftgERvtKQUiLnTAojVx1o75LLA1IeqHIUmEQhoqLEz1cI0iK2M0Idf3zUIe0XJo6xkWDp0gq0lN3Dr02G_kPCH7gDwst5GsILWjRvnxFv5Ass5alqSkhWmrV3GRbFXMs37ZuaML6z4lNFLkBjo8VOtPtBDAFN3GePpjCp4iotclNsrvalWL2updIqFZXU39SutfKXzILT1R6VU_6RRsknT59toWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تهدید یک نماینده مجلس به ترور مقامات اسرائیلی
متفکر آزاد، عضو هیئت رئیسه مجلس در شبکه افق:
🔹
اسرائیل بداند که مسیر ترور یک طرفه نیست/ همین امروز در خیابان‌های اسرائیل اتفاقی افتاده است که معادلات را عوض کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/656486" target="_blank">📅 23:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656485">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔹
خبرهای داغ امروز را در وبسایت خبرفوری کلیک کنید
🔹
🔹
گزارش لحظه به لحظه از اخبار جنگ و مذاکره ایران و آمریکا | از شلیک موشک هشدار ایرانی تا توقیف نفتکش از سوی آمریکا
👇
khabarfoori.com/fa/tiny/news-3220568
🔹
ترامپ: به‌زودی جنگ نهم راه خواهد افتاد!
👇
khabarfoori.com/fa/tiny/news-3220567
🔹
رئیس جدید موساد کیست؟ | همه‌چیز درباره مردی که می‌خواهد نظام سیاسی ایران را تغییر دهد
👇
khabarfoori.com/fa/tiny/news-3220645
🔹
ماجرای آرم «ساواک» روی سینه طرفداران سلطنت؛ چماق به دستان وارد می شوند | رضا پهلوی «موسولینی» می‌شود
👇
khabarfoori.com/fa/tiny/news-3220679
🔹
پیش‌بینی یک نماینده مجلس: آمریکا بعد از جام جهانی سنگین‌تر حمله کرده و ایران را تبدیل به غزه دوم خواهند کرد!
👇
khabarfoori.com/fa/tiny/news-3220707
🔹
ویدئوهای جذاب ما را در آپارات خبرفوری تماشا کنید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/656485" target="_blank">📅 23:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656484">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
صدای انفجار در کردستان عراق
🔹
خبرنگار المیادین گزارش داد صدای انفجار در حومه سلیمانیه در کردستان عراق شنیده شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/656484" target="_blank">📅 23:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656483">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95c285d770.mp4?token=DOIm7tOSWfMipblBwz6uLqx3KkluGNlo0DVVYL3vNMT3RHZxTl14VT3oCG59Ss6FneAxz5huoSJ_ZJRvl4pWD02ddO9OxPFGzegb3VaA0Hv0sHIiUBz89IkuKYZQhkZY6toIOLNLqq8iZpeZ-s3TOZLT9hZ97ssX_68CjtLOtpv1rKhcFI7UXfeorDE87HsTx1STvBHitdfKsUgO6glNHfHl1FxE4PduQjbWk7mWgIqC2e9NwFEd_Rx1cDadXostg6NCpgTrYwOjnDIp2AG2m0FCR_je4_SqwXIda1zaEYyDsBV0EWehzulAxjSO0hDMcFGw4Ta_mRMsM_9ahJkL-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95c285d770.mp4?token=DOIm7tOSWfMipblBwz6uLqx3KkluGNlo0DVVYL3vNMT3RHZxTl14VT3oCG59Ss6FneAxz5huoSJ_ZJRvl4pWD02ddO9OxPFGzegb3VaA0Hv0sHIiUBz89IkuKYZQhkZY6toIOLNLqq8iZpeZ-s3TOZLT9hZ97ssX_68CjtLOtpv1rKhcFI7UXfeorDE87HsTx1STvBHitdfKsUgO6glNHfHl1FxE4PduQjbWk7mWgIqC2e9NwFEd_Rx1cDadXostg6NCpgTrYwOjnDIp2AG2m0FCR_je4_SqwXIda1zaEYyDsBV0EWehzulAxjSO0hDMcFGw4Ta_mRMsM_9ahJkL-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو پربازدید در شبکه‌های اجتماعی از
تینیجرهای تهرانی در یک دورهمی که جهت حمایت از ملی‌پوشان فوتبال
دور هم جمع شدند
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/656483" target="_blank">📅 23:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656482">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">شب شب ولادته تو دلها قیامته</div>
  <div class="tg-doc-extra">مهدی رسولی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/656482" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨
شب شب ولادته
تو دلها قیامته
برای عاشقا راه سعادته
🎙
#مهدی_رسولی
#ولادت_امام_موسی_کاظم
(ع)
مرجع رسمی مداحی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/656482" target="_blank">📅 23:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656481">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/008d1f0eff.mp4?token=QaFBXdSMM-NwhAKvLnZeMMSr87FIgR5jwPY2_7EiNUeU4y3y7BWP8c2MzHRlCTJV2DzUW_DBdBXYCdFC5wcMTyR3mfZWJxiimBRktpysR6SYRpPs7lvflmn_HsWhrLZCc_AXECyDN31U2rrf48fe4oLmqYtawUm-_TmHloRhthycOONPgx4pQ6hT-so3zTtIc13rvklqXx_GSvz3HvK4LvRhE2fHsfFwCug_inNETonatPqFY5fYbd69nSnonkCSsivIMqJDmVbXu3_kj9_DAr1Y5Ok_MkU7sm9PsOyVq8b6C3MMottyN8CuFuf-jucgADU93OcqJ5yaWX8nqOBnoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/008d1f0eff.mp4?token=QaFBXdSMM-NwhAKvLnZeMMSr87FIgR5jwPY2_7EiNUeU4y3y7BWP8c2MzHRlCTJV2DzUW_DBdBXYCdFC5wcMTyR3mfZWJxiimBRktpysR6SYRpPs7lvflmn_HsWhrLZCc_AXECyDN31U2rrf48fe4oLmqYtawUm-_TmHloRhthycOONPgx4pQ6hT-so3zTtIc13rvklqXx_GSvz3HvK4LvRhE2fHsfFwCug_inNETonatPqFY5fYbd69nSnonkCSsivIMqJDmVbXu3_kj9_DAr1Y5Ok_MkU7sm9PsOyVq8b6C3MMottyN8CuFuf-jucgADU93OcqJ5yaWX8nqOBnoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجلیل از شیخ نعیم قاسم، دبیرکل مجاهد حزب‌الله با ابتکار مردمی در جشن ده کیلومتری غدیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/656481" target="_blank">📅 23:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656479">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dd4Z75JcMoYyvWRHnJ3vhP3IV_H__jcJr9DlBkr7qPzW4z_BruFHY-7ggOCgwKaF51Nkn2gG9cN24ymBF12BZOKDnoAf0cai4PYu8B_DZCMkBksVOQIThzF-l3LD5hiM5v12E0MUAhDUnB0xqLmD3HF912XovknoEPq3gEEJ5p3pKM6r1LMEW0_mJH6b-afBxGkdFK2E3FCoeYRzbTtZsme6BROW6LsROsznWHFjCQo8J1bRhG7DhXtZyDY4HI2-qMxVnIcjy9aFs_mjqSi-JDvp-RLCcAqb2MYTMWT8jrRrzoDsyoqKccvDec9Ff0k5feLciA4HmOho17O2QkbmWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JvRFSZyljwkHqOfADT1FhMp5IjAd3PxnZLpRFlgGHnvio9cLCbo8U8Lio2qtUaCqLxCSW6Pdm7HFWwe4tStbu1TyaWbZ_hdCDhzqEzzaf3T17mTxUWMpR6vWNun_nFOVuwjt3qoHIDayhbZdTon1s7LLVTSm1IH8MiKvY8S1Tt5V3siQjXhUQ3DBcpFtH8GJCosogB9PQMswyojT97tLPiNqOuH3q78QKRjUDyhfDtkgltr_PU20qW_80jQU2O6Phenj4gCRVe6_Ba2MVLFno6K0R1m_fD4KKu9zSKE8gZtQWLrM9Dzph9DVYT2bmfIJIhH0SNWLzqZLuRbztYX3WA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
وضعیت خونین بازار ارزهای دیجیتال
🔹
بیت‌کوین برای اولین بار در دو سال گذشته به زیر ۶۰,۰۰۰ دلار سقوط کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/656479" target="_blank">📅 23:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656478">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guX1BPCHAYObJR0eT9iADxcg2kV-D90oMyJq3guuekRLoI3ltTsajWT3nwR5zl5RnSkeykSxC8TFnG6dObCWes8jxwQFiFNdL3hcIxahnoLXHgCEIwoRL4O554EgQYxrYa-KUpEege8jLxfDCfSWZljauK5yB_OCURUR62jSBSdrXHSnWck6IoDQDABEDK8HaLuSg24TQgEDJ9moWOxyANt832bZZnx5cGd5JCUutNk3g9DbR0WAUeBOGoi4oXQ-kiYSe4wnJUKebRwBtLpxCnrlovhFhPSH_1Vg-CJinoGEq7qSpjy5zPRdefY1FMhNUORMrO1SryEQwv6wq8Sxvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای آرم «ساواک» روی سینه طرفداران سلطنت/ چماق به دستان وارد می شوند/ رضا پهلوی «موسولینی» می شود
🔹
آنچه مورد توجه رسانه های اروپایی قرار گرفته میل طرفداران سلطنت و پهلوی به «اقتدارگرایی» است؛ میلی فزاینده که روز به روز بیشتر می شود و مخالفان استفاده از خشونت و خشم را می بلعد. اما استفاده از عبارت «اقتدارگرایی» فقط بخشی از هویت برساخته توسط پهلوی چی ها و طرفداران سلطنت را نشان می دهد. به نظر می رسد طرفداران سلطنت و پهلوی تبدیل به نوعی جنبش «فاشیستی» شده اند.
بیشتر بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3220679</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/656478" target="_blank">📅 23:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656477">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4756779ec.mp4?token=Nk7rQR4r799K89qDT9hwYsLmQ2mnjEj2sXThfpPSG9DS4SDGUeoydFEXnNs9Ce8KDwEYaMsPrBo4iIMlyJpvbm9y_TtYIcqTk9K-B7ojKsumEXBv236b69ijMKTBTgkuAbEG78AiBFFnPe_UMDOPPT8PX39YOq9cT-zPeCh0yIjiZ8ZRN5-hTiTE8BwG7NvSSgSavRV0t1bd1VcV9gi42_z30Eh0xcqQCmr1WvqVMb_Gi3wdlP19IRVUckdsRccly9SKICYo4AgKp4GE0qgTSe0FyPsVBk9mcTMCjHSTkxZOcwoTXn3u2hHLeNjUGyrSyajqT7mnA1B0Xf_Bl-UjxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4756779ec.mp4?token=Nk7rQR4r799K89qDT9hwYsLmQ2mnjEj2sXThfpPSG9DS4SDGUeoydFEXnNs9Ce8KDwEYaMsPrBo4iIMlyJpvbm9y_TtYIcqTk9K-B7ojKsumEXBv236b69ijMKTBTgkuAbEG78AiBFFnPe_UMDOPPT8PX39YOq9cT-zPeCh0yIjiZ8ZRN5-hTiTE8BwG7NvSSgSavRV0t1bd1VcV9gi42_z30Eh0xcqQCmr1WvqVMb_Gi3wdlP19IRVUckdsRccly9SKICYo4AgKp4GE0qgTSe0FyPsVBk9mcTMCjHSTkxZOcwoTXn3u2hHLeNjUGyrSyajqT7mnA1B0Xf_Bl-UjxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نخست‌وزیر پاکستان: همواره در کنار آمریکا بوده‌ایم؛ برای همیشه از «ترامپ» به عنوان «مرد صلح» یاد خواهیم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/656477" target="_blank">📅 23:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656476">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
مردم در یک هفته ۱۸ همت نقدینگی وارد بورس کردند!
🔹
در هفته‌ گذشته بورس ایران با موجی سنگین از ورود پول حقیقی روبه‌رو شد. سهامداران خرد حدود ۱۸ همت نقدینگی جدید به بازار تزریق کردند و موتور رشد سهام را روشن کردند.
🔹
در همین فضا، شاخص کل با رشد ۷ درصدی تا سطح ۴ میلیون و ۳۵۹ هزار واحد پیش رفت. اما ستاره اصلی بازار، شاخص هم‌وزن بود؛ این نماگر با رشد خیره‌کننده ۸.۲۷ درصدی از سقف تاریخی عبور کرد و در ارتفاع ۱ میلیون و ۱۶۲ هزار واحد ایستاد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/656476" target="_blank">📅 23:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656475">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
تریتا پارسی: به بازیکنان جام جهانی ایران ویزای ورود به ایالات متحده اعطا شده است، اما آنها شب را در ایالات متحده نخواهند ماند
🔹
آنها در مکزیک مستقر خواهند شد و سپس برای هر بازی به آنجا پرواز خواهند کرد.
🔹
این بدان معناست که آنها باید در همان روز بازی از طریق…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/656475" target="_blank">📅 23:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656472">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f1d4b315b.mp4?token=s0zboiiywwv8DEvErTjV62yzBQPfVPgWgZGzQGxbdmhEg3B22d1MSMCozG_lnv8ZyQS6tOsGk_q3ApgMllXhTYLY_4i6BESFHLt8-5PpWkEpBvofbzOFNCUU3NOXfwndvsGs1As0Hj53ERAybQOGqJjs-6g57dB74B832o6we0ASs3R-GLiGtFXf1-r8LjZlwwFEAOjOja7wy1zHjti7nD8IEsPPspRUvZynOfWDo-9WV167GhZLDpothH_y900Na37_-D7Vw_uAcuRPmQnXGravX3AmzJ7XAy4DH1xg8zTBwmnmsox4UYS3hfIWZlWB8fDtoLHfHB6i5zQIIsL7sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f1d4b315b.mp4?token=s0zboiiywwv8DEvErTjV62yzBQPfVPgWgZGzQGxbdmhEg3B22d1MSMCozG_lnv8ZyQS6tOsGk_q3ApgMllXhTYLY_4i6BESFHLt8-5PpWkEpBvofbzOFNCUU3NOXfwndvsGs1As0Hj53ERAybQOGqJjs-6g57dB74B832o6we0ASs3R-GLiGtFXf1-r8LjZlwwFEAOjOja7wy1zHjti7nD8IEsPPspRUvZynOfWDo-9WV167GhZLDpothH_y900Na37_-D7Vw_uAcuRPmQnXGravX3AmzJ7XAy4DH1xg8zTBwmnmsox4UYS3hfIWZlWB8fDtoLHfHB6i5zQIIsL7sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امام رضا علیه‌السلام:
کسی که قبر پدرم را در بغداد زیارت کند مانند کسی است که قبر رسول خدا (ص) و امیرالمؤمنین (ع) را زیارت کرده است.
💐
ولادت باب الحوائج
#امام_کاظم
(ع) مبارک باد
@Heyate_gharar</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/656472" target="_blank">📅 23:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656471">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
حمله به کشتی ترکیه‌ای در دریای سیاه
🔹
المیادین گزارش داد که یک کشتی ماهیگیری ترکیه‌ای هنگام تردد در دریای سیاه هدف قرار گرفت.
🔹
در این حمله یک نفر کشته و ۴ نفر دیگر زخمی شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/656471" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656463">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sgxs55ClOTNU_aB0TC1tsKiWqqGD3Hvuo9zI2_3xXvH8t9wpZysIprcJbFAKE6RMsd-VB0VRCdO4UpIKpQk7ybOZ0UqHV5kSBOv9RRZParNCdSmzo1bDDbA2RZNUpqw4soZh6EYLwSJa2vsn2CQcNeP3MjZz8J3YOcdMER4U3DZbQHXpx7sOlqTCLTppSDtWCh6zYBeymD2U2bZv52RWcuton6FL7IvLbaBTYZ0lIJXgMCBatH6OTs3N8Xq9sq4yojleN0GBVY0RnhEnxK0bhVJXQ3LledAvlyxJIUNOEk_0Ojw3wyqjxMwN_UmDUbKhPdZOCZne7jKB4QKQJnvKUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GMyrsXx51om2QQ2ZeVF0YVr_xcKGmI9XMz-aRXKO_7GiKP5UmdXdRJpHW6epkTkIgNv6EiXIhQdlwXWgMNc-q3bd4Eua_g_qPe9eLKfCj_Yg4b-_jExNbsOKEe_pPwkQqSASOgnx1BHwQM6PNcpNtV8LIKkpl98vL5PXvTBqZ60nIx-Sx2eItYXMrsggOyBY4jFR1ajtFnXPVfbBUkTKxMMO92gQDVJK9pdqrDiGO7Q42S0t_Hwa2eFgHnBETKNXfKLpIcbondJqRUnFQB_gdZPMI4NWqwtqsyPdwgZYf2iDCSARrD9K9mc5SapvgSG-cFTC301p1HwVm1hIfUsKQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tlQTqOoucxEWPdSLoW7XZ2pY_WSBaQeQiLmn_QOXxpJhBjMdcTsY-jwlJmJDiPtkkwwsL6AIO1sfqC2jXp0VTbc2MryjZtWk-ODzoGdQXDF-jcxlO5yKCqtREbbOkMyxWfdpRzBSQfb9Ri56EGAilCQNPUTrBWWODx41mS9B6L7xgbXHMBjb4C_aCueVXDwWcUuNszGtONzcCgPa355nPMNs-tbUg8wk7kKjjaGMRI7oSIVZQaMUMLqaZD26j2_CYuWc_bINI0OaX6hPMZh6gVsBE1QmPYlwzsHX6QNM2eJ9FezFxCFowvLbC9hhBZ-IozijBpz9-3v0Szh1xp41cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PyZ-aCAl7GcxUl0doO5uXMu16fM_fUy8ae9Qi1vhpyF94zpKFlsLg7tLlYsjJhos6MYjTmOOvlLYN13spQUBgzYguT0T24H7NyvlJaeCXPvAsxqNAa3ykANl3XeOO2tYrwRK-OAFLRJ5K4Cks8Drk4NdgAPBSnTLuQNf9Eceh3f9h3VuS_36tcPrsib9agbtF6RiYsjwEMv88w2DS-6qSoRN97v0_O_xLbsvJgVVV71KcrFBNIfiGsYf9pE3QxSKkKLjCZf0GK_UIB7g3Swsg4R8ZS2eHwfa4PaSb2maBUbSf2SoPY2bShS0RgG0pgnMOjP3SXrhoRn4I93yNy1_fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XNlkLj-hEpM-6D7GIN6C0-uUjP54lagjpzjdpEugwE_Fl4mTF31fAwZqE5AnWepJ2WDKfaMJgU9AjWvUee-q3OHdP8GDjDG0X-o_KbKVRyr0r3MCZUNLg42O4MO-Sfobnm5eQI0LYaiffNCRbGyD3xe58D6Crs5I0MMsMw3oleXnzpdsNz1XVmME__9d0kgt8vkiwPgxJILzqy8-QA8NcZAw7DW-ob3xTzpJVnAZqr9pHSQ14DywPO6YY8eLcmSJaW1j2O7miH5Lu2jpxgvXNGY-0VRGhDXQfjiWsTFkV9N2wQ392NMA4ns2t5Lre3nuPO5sSxm42WPF71iskYUatQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HoSiSNLxZoEBBPEDW4q7lt6_dyA4DEnemBq5XRSjyymR6qlCz7V2CRd_8X36J1_XrhPD54cn0rODWspTrD-kVMIgaxxxvX5zqqOGGVzi9nmWE7FTIgL4QtGg_MgfZPKJtcDUPL8_wn2h2Q9Ms7dURL2J-REVeR6whEQSVjCFSc4FgOqeAoONJopGN5gHIUzCbt5grDv5YdDYQHBIiDCzRVkZLKAuhl5n_TIbRI5d6Dn-lFhOGDJCgn7YJNtylEwyzil0CsuGzmO2_lEKA2PgiBR7n8aTlU8vSwDdOgjehrhJWPpbq-syMK_q-XJEcNC4hcnLhidNuDRJtr2_-WrhZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PcKlppptluE05JFpEt_F7QEMNaApIgnJabsol6PbeVqwa9xvg1kSmfYQfG5mR2SbxdbFs6jhyP8lcR5Z4lADcHFgxBffDw8ZtiYC7SMbshSoE2dMmNo1L9KvlqjueKSHiuicEfzUCVfm-5pmoo_Iw0Jd8R0XcAS1SaXHAVtdHdrEE2YN9YryAbnVeX3FEgIWIh4ahInOtg_dnK7FCLtnGBEUC4l52WEXP_wCiIHsOyfW8avEO5Yb-AGVuw0ER8Ddm4A8ULjAt6x4JmHNkwccDOIwstmthS-Yzww4k9FTv_rce0IDPw1XdgLgxptFrsvjziZ_MFDmiKoMU_IWV4MGrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CibMFIZEXJJ9FKklipHfqoe7P8otCZQi3adlpajPuk9h7PPLwFUnU_ZrrKX9fL2lQ2ICHfbViYMHjJ1yt_mEa1kZaCE9wFdb3LZ-wp72vPjf_i3wOJ8eT_l_DQUqSv-OE-e3CjuS5LCea9jvbZBu2Tpy7n8yxTqahevwldDQFVvYZRLTYGGSIdm5-ITVvvun8T6iNdAfaf1xjqZTMwUPs-G9XyDf-6CBHIMQDMGgbYmgSRBkemgyhEZvPoSw-Wv29fqQEWmvz1yeEZ2fdLmXdF5PQuN3S3A_9JjXywRogj3StCfvdgiq-BZ_bajz16adstaZbLa7LwV2dT7jVaArhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۸ عادت کوچک روزانه که به شما وقار و ابهت می‌بخشند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/656463" target="_blank">📅 22:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656460">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f1d4b315b.mp4?token=vbZz8fNoaFenJKjr8Hlby7ceQLoWrhAigSu5oolioz9j47QnK6teF7Xl6x0t-KILw9bctZbg0psvRc6azDaNCT6k2WPVDQdCGL7E9KZOGgBx7piI1Uj9Oh4gzl-2vVuUH-WK5khhuRjeBvG3GibZnHvSHBRMqTcf_z1PrBTUQFVxF7Y2d7Dp2QwhYuKg_qzwHULY9DvBVao6PPF6dzhRmKFLLy056HiCF5yoTwBDFVDxeBEqWdRMhqni3jwjnYzqXJEJrPZRyOoSxywacHJU2tEpJCIpuequShV5NeWT75EVaFc14QZbYccGRztxwZXCtDxmXSQ97j1CCra53LsE0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f1d4b315b.mp4?token=vbZz8fNoaFenJKjr8Hlby7ceQLoWrhAigSu5oolioz9j47QnK6teF7Xl6x0t-KILw9bctZbg0psvRc6azDaNCT6k2WPVDQdCGL7E9KZOGgBx7piI1Uj9Oh4gzl-2vVuUH-WK5khhuRjeBvG3GibZnHvSHBRMqTcf_z1PrBTUQFVxF7Y2d7Dp2QwhYuKg_qzwHULY9DvBVao6PPF6dzhRmKFLLy056HiCF5yoTwBDFVDxeBEqWdRMhqni3jwjnYzqXJEJrPZRyOoSxywacHJU2tEpJCIpuequShV5NeWT75EVaFc14QZbYccGRztxwZXCtDxmXSQ97j1CCra53LsE0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امام رضا علیه‌السلام:
کسی که قبر پدرم را در بغداد زیارت کند مانند کسی است که قبر رسول خدا (ص) و امیرالمؤمنین (ع) را زیارت کرده است.
💐
ولادت باب الحوائج
#امام_کاظم
(ع) مبارک باد
@Heyate_gharar</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/656460" target="_blank">📅 22:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656459">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfwnrVAdGW-8NbERmRcaRq1spy90NQYLdZSjw-QLMFvD5MEvLKKfLv97NZySiD_v_s8LNNoghVHPeb_-MaGQwFQKEZujxbS4tlmqbLknq7gz4zvcSUjhu7QiO0R6TQt71ZJGBAtDC9NtF5N8QZUMPd4xyTRGyYmLA5ypGipPEL0_ZMe96f1WQIoPQIG8KIoAPbiHulIA5yWPSR8Ery0teb-9GfNleJZcRGUxPZK_qpDI2i3QRJVwCA61Hsx9cdAagyjXDAfILRabrbMa_yAIni4SiEaZyLBAwf3wdWHRTPIytnt8SvKJq2iEEiaGqGY1i44vVQT6pqiaJ19rkggDuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: روادید ورود به آمریکا برای بازیکنان تیم ملی فوتبال ایران صادر شد #ورزشی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/656459" target="_blank">📅 22:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656458">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
بخشش جریمه بیمه نامه شخص ثالث از فردا به مدت ۱۵ روز
بیمه مرکزی:
🔹
همه دارندگان وسایل نقلیه موتوری زمینی و ریلی بدون بیمه‌نامه شخص ثالث، می‌توانند از فردا شنبه ۱۶ خرداد تا پایان ۳۰ خرداد نسبت به خرید بیمه‌نامه شخص ثالث اقدام کنند و از بخشودگی ۱۰۰ درصدی جریمه حق بیمه بهره‌مند شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/656458" target="_blank">📅 22:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656457">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ترامپ درباره پوتین و زلنسکی: بگذارید خودشان حل کنند؛ من کسی هستم که آن‌ها را به این موقعیت رساندم #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/656457" target="_blank">📅 22:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656456">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1MeyV0FAgBKlDBAuWRy19ulFQkgci8amBVPRRJjAEiEZnfeSW4blGeQMDv0kujSii6GLBnBvCbjzDyPP4oFkmoibtyEeuuNi75LXL9mymF1exZcChxgAJFpjHLxvAMyup0S2Y1joxctDuKxda0lV5rQydcy4gW4ox33wZp2kATCr5-AT6BCDcr6M3bER8uQ1NDBHJGdHdL70mauMZs4-8qpnOfuoFS94DTik1-ZTtnXhq-WCnuVVX14Ibg8Um2F96yo8Iy4s88OIu9wnUtVRDb-Z8hKKZTOHmkvYqEzuiiZPQVU7W_G26PDbyTnfPc-mku6qpuJg2nl8e3o6vAe8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس آمریکا امروز یک تریلیون دلار از ارزش خود را از دست داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/656456" target="_blank">📅 22:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656455">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
ادعای اکسیوس: تیم کارشناسان آمریکایی مأمور طراحی جزئیات فنی توافق هسته‌ای احتمالی با ایران هستند  اکسیوس:
🔹
در صورت ورود مذاکرات با ایران به مرحله دوم، تیمی از کارشناسان هسته‌ای آمریکا باید طرح‌هایی برای دفع مواد هسته‌ای ایران، محدودتر کردن برنامه غنی‌سازی…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/656455" target="_blank">📅 22:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656454">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03b8820397.mp4?token=Bpv8_YoO7gHgjqcS6QjexojF2ziVCNXLZSkAlsxSEhEFxt_TX8hxrOZeICmwvorHsyTSwMCPGSpZiu8t708ST-gpkAXpWRu_K-0uoBfWfDLUleSj0AwMSP9d4FsB9peInV-Ek5gVji7xMyB60Qh7rHS2SVCOvqXQu2475csx3BqlqqpbKQuG-xgdqOceFBlLE-Ms0pPW6NEgEHsY0-LKypyQYmFMuj7MTMVOx7lrMWjjjpOmiRMvL9kQARl3Uz7uwglDaDyrfM_LL_cLVU_HAbi_CS6YgOnX9BMj02rT9YxwcsuSKTbyu5u3o5VakvjE0PfT0YAwgGJsmVxxhRX6gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03b8820397.mp4?token=Bpv8_YoO7gHgjqcS6QjexojF2ziVCNXLZSkAlsxSEhEFxt_TX8hxrOZeICmwvorHsyTSwMCPGSpZiu8t708ST-gpkAXpWRu_K-0uoBfWfDLUleSj0AwMSP9d4FsB9peInV-Ek5gVji7xMyB60Qh7rHS2SVCOvqXQu2475csx3BqlqqpbKQuG-xgdqOceFBlLE-Ms0pPW6NEgEHsY0-LKypyQYmFMuj7MTMVOx7lrMWjjjpOmiRMvL9kQARl3Uz7uwglDaDyrfM_LL_cLVU_HAbi_CS6YgOnX9BMj02rT9YxwcsuSKTbyu5u3o5VakvjE0PfT0YAwgGJsmVxxhRX6gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمع مردم تهران به یاد حزب الله قهرمان لبنان در مهمانی کیلومتری غدیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/656454" target="_blank">📅 22:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656445">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/spzGTZq-6xzr_Gbs_5CHbPAcVzuoK3VGxK3tIDWg8VAAxMcDaDKBG8CbTlsUh3o2ST0LsxjU3fCCOPapYoFwb5yV9O5fbgOr26-UawzKKpanKdy5lNNMDgI-Z1AHRb_Sne8w5i1RJi611BUQ6raT79dHjTFMHitJ7jaqyP3Lch5_6muN-OrN7KYVnfg1wn7etXLqGsXIdioZac96ex6B9HHHViRjAsFaqNsonP_yx8gt5pOOkdo7ASghxZ7wGARGe1gwubGdPRoozorbmkGmVVW936hb61hGyoijb8VN1ymKISdcdsHS7g2uq5R9foAf9uQu3H3CDw_JA0Jb2gfJFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YFnos-w8s54sQ4dnmh68LZz_O8QkftCiET9t8KnuxFxMwXOKT041tvL_MGoPbVT4_2ApPDPnLXoyU8yYrP649tCCZHMIQsaAUGDq4edIaj2eWXVb9ltoYZlTj0GAJ9kTVuEiXPWYqulZiM5Dx87y7j06yKHyUfh_kNX8MmoBtkPqZOtsCvNwWeko6gqdkp1aGgpmR3uY3qBgwIds4f0mpRD_B6AqO26LUEA6aOCoQudaEEzx28bxNZsnrkH4j_2YrrjL2CsJ-_hiBlUbC7XOs9Lc9loHUvp-m5K9e3cARQFIqAC29MXwFX0V9alPrImR-t8_c2sxCdpk_q4fZPi3eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mc3GVJsiS9GPyweBpSNHsUMmTK_yq7upOzKGKWtOc9xyQw0eR9Mel4np-e7J79HPlo1woUklmK1nU3BXua5H2PCrDCxHVIxP5ZhJ0JIQ_LzS8hjBwPVbyulUCZ0wRGhsV6xsjcgOp6uMqCqchXBzb8YG8S3aSmPUD0gkMNi9FjhfLsEi3ttoAL-cBAmmX3zMlHAy7G1vHHLD-63p-oQvvyZNwVNeWGbNllL9J9rb_kVyVjbA6fXSiiX4LuQZzKoP_xmKit4xfQzpV18pvOKM7Vsz8-b0G2F1uRQdL55RWpfML20TM6e8jnYChVb57RrEHMSavnLrA3ZgLQBK80BQQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BaA9iLZZecVRPnmxxNeggvob2JRB4an1ojkpJVKYC_DB_o-VidBPvd8mxejRVEpYMrW8O2uTyoQxXDfZlrCmWeY8gkx-tD1hQM9j4tDqskh_tiHTMItOebFh7l2KXQ0iN0C1RDIYbWG8PBy4ywhSIWfmPWjx96wZ3D_PyOnHf9SRDnFCzLP00TFDn92tFbND9Np8hGjKwyDTkl43e6KiuN40APOKhZFHcXbezPp_SKpw99wgltHXHzo6dsb98L6lcTyqA-TxGydmAuxFgDgg6B-7vnt0b7aKufhQb0xtLkchNn_d-FToQjpv6UKBM38pHOt_4AOjcWs_WfFnWujxyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UDLwiY6VBawBhvqNCIGHf7fSr7DN69S0yhCMmR2d3M6bNIyHPqZm4t1gG7ZAuZBsmF_dBJ-lfTOMl2YiI4AyRc1_u7hEBreOMyfJtJv3h0D4Iau7p8zbTy_sT0yZlOgdhiB8u6l-aaH4ta-XBGWHGgT17j2iHgVNvbGF5qYbTlRf_bVsMe61Ya5s84qgbfWGwjPPha20aQN60YyYMDxdjJQPU8zrGPKZE5kprgJiumuMJ1_49HjdmwGGhFTflhRbzq1I5TSC56YrHii9P5RdBkweW1jQ2u72rD_QGsJkQlvWm1LIbfudpQPj9yn9YziJYJ0nQIbWe9Wlu8lNdz7wPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tgKSipq5xMAqtAQzeXkrNevWZj6BlFhg5JkYKH1CzylGOzkYYdjnHSCGKgVHmyYECHG7q1rFR0YkLMFkeQ0ZRHrSXwWJHcwfTF-bldwg5x3QLJ0XXN_mVB8kl2LQI56fnKJ8sh8LTjvLmDuIvTZSisolel33U6Oe8t3JgBFTEHQXg8VQNu4cUMLIKffYK2UCQWXJ3MttxOeUxtJiEJ-X6CmaZB3_4XwydpKUl_G2Rl1xXYXRXb-adlx9H3pMdXD22ngj7TQ7JCTs1EbzLdwgF1FWjefLONYtkxivq-GgCJaCJuMFL1sf235pSwmGKU9dlJFqEFdWk2EURHGfSTtv_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G2WX-yNo30u_idzJEembuqF_KOaBvNMwpLLJWi-hqjx8JZeRMXvDpGOn1YqIayxPoEhpQutR7Al_M-F6ap6-ET1CnYfSA1YDxX0JgxJQCbMR8rZkjj8OyFUfVNifr_T0AbZr_q1ZMF6mccxQMHBgEdTvlg5kgZyyj9bJHwHDC14grc_h3R1iaWyBCnVgFBNRMEonBORaDMb9EruA6NBwIW6ckb_R0KhXh7v7iFkgldXtmZMN2gZQpDiOt0JTvuf8qfNCcapiFYLbiY_51LFLdu4TNm1MU3_WjHI6JZ8jaUkGD9YIb3DsE9oZL3ov84SJZGZRUcKdQG9v3ojIe3pGEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B-B9DLtrjoxNOylO0uC2L-g86YsW-dmz8_NwG7j-TMFXIMMHEyFO7J50xgHTqN65QzdC7tx-AxrWgpCHIsVxqlFGSNMU8bCP4NXbJbRHlOItUigCwVOwbV7d6rZA6TwZ4TFvrgCeNv98SACTDIHlA7FFlWqNOH11BWTCED5dLL7CJNivVQ2LSf4pRD-uPvPUUltypjNU6cxxSjf4Ppgk9A8loCQc-eXXNeuPH0XbRhEC031XtZAO1t5j6aGEfsh2eZlyYZ1kUdLrQpBWlw4zFjtAuK5iiqW7cIgp9cpwfK2R50NjTrxYijaNLJZf_9Xy9QBL8utNGkOOSLI7nxDL2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXLbFGXQAnGTfFYO-UwLcaX03UzZQFNnn_Q71RV5cKtLZFXsZsZMSpPNEX7Yln0nAdTsCweqnOb3Scv5IZdHUDF2D60J3l0nHNwzNrKap9FtUPDNgyMXqVqaHdN56O2-RgML3-vI2dhDcM7ouZK9NMs9O_ZKpiUKikXtQ68TszqOSM-1Fxcsv6sTFze5SOB9qmoMfjz4uZ_udBPHnT82zBakxgOCXakXFA8ClQnsdajMyAx190DLvZgvE-2gCFxFZvSCOeKgyV-cGJWk34F_Gwux80HCizEwopJXygD2O-StrX9NVZLtdtmnSV-quo9DBl-MqQRtZX0PyKJXFMKYvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت قدم‌های خیر
💫
در مسیر
#همدلی
و حمایت از خانواده‌های ایرانی،
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با ذبح ۳ رأس گوسفند و توزیع گوشت قربانی میان خانواده‌های حائز صلاحیت، تلاش می‌کند سهمی هرچند کوچک در این مسیر خیر داشته باشد.
این خدمت، با حضور و اعتماد شما مردم ادامه پیدا کرده است
🤍
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/656445" target="_blank">📅 22:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656444">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgyGmyDjmBTvLKgecdmTnJhwpoq2RsUfLjj_I911UMOejCleu2a8KcVQhAM-aRBF7K1wdcluXmQQA6S7zgnMeVR0EspwfV_UPnS8eGq8ltGxjLwLu9STqjp_3HVNAWc1vADXe4oIH8eGhePumz8Nqx-i67CxAlODVp7NYQhciy8Ro0go59LuUtcThotEW75E1Ms21z40fB_QUwwiCH2d5kw9euR2G8GngklA4Rhy_ec13fPpJxXKwZPnqubkjPguMAjZugIoXIYimfwA5qN7Vc5BDtJq_RtAQTONSpRen471aLLXMVxLN5juN7GHQCqfM4-JKATmahuhWlvwpQpK3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صاحب ایده تغییر نظام در ایران! | صعود یک نظامی به رأس موساد در بحبوحه بحران اعتماد اطلاعاتی | مرد ناشناخته‌ای که رئیس موساد شد؛ رومان گوفمن کیست؟
🔹
صعود سریع رومان گوفمن از دستیار نتانیاهو به رئیس موساد، یک گسست از سنت در جامعه اطلاعاتی اسرائیل محسوب می‌شود؛ آن هم در شرایطی که این سازمان پیش‌تر با انتقادات شدیدی دربارهٔ شکست‌های امنیتی گذشته روبرو بوده و خود این انتصاب نیز با مخالفت‌های داخلی همراه شده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3220645</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/656444" target="_blank">📅 22:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656443">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ادعای اکسیوس: اختلافات جزئی بر سر یادداشت تفاهم میان ایران و آمریکا  اکسیوس به نقل از مقامات آمریکایی و منابع منطقه‌ای درگیر در میانجی‌گری:
🔹
واشینگتن و تهران همچنان بر سر چندین جزئیات مربوط به یادداشت تفاهم (MOU) اختلاف دارند.
🔹
با این حال، این منابع می‌گویند…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/656443" target="_blank">📅 22:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656442">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ادعای اکسیوس: سفر ویتکاف و کوشنر به اوک‌ریج برای بررسی گزینه‌های فنی مذاکرات هسته‌ای با ایران    اکسیوس:
🔹
استیو ویتکاف و جرد کوشنر برای رایزنی با گروهی از کارشناسان فنیِ احتمالیِ مذاکرات هسته‌ای با ایران به آزمایشگاه ملی اوک‌ریج در تنسی سفر کرده‌اند.  …</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/656442" target="_blank">📅 22:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656441">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBenelli Motor Iran</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFIKnRPEpyjZ9xQWZqAiMyOkJhNHD9YZNJxdJs8tiqQKtt24yhpsmTmAoENshQzAiEMNGyJaXgMZA_FcbDmvAaG_ipyVV9XwIo5ckHCT_xEc7EOqeC2XBXPyRtqBak2rDcEcoDU-u47wlfGjpwkZNpNaEls2r9NcFL-VA8s9SfDn2g6iEbVsXrQW-2b5u7fEAXNgaRWqz8OoJ9P4Gm_H8v-Tfg2CmlxYS5N92OIQWpHVGF6JYzToITm224_RSke2qn-y5ThiD92fwo84adq-8G8Z5VD0nbdIF8bJe360k1eIEJvkiLeiuoXwR7W8XBl60HqpUVrTQTbMQAENRmoJIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موتورسیکلت موربیدلی N249R
✨
249 سی‌سی
💪
تندرو و قدرتمند
✅
37 ماه گارانتی از نیکران‌موتور
جهت مشاهده قیمت نقد و اقساط و مشخصات فنی روی لینک زیر کلیک نمائید
👇
https://l.nikrun.com/0re
🏍️</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/656441" target="_blank">📅 22:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656440">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ادعای اکسیوس: سفر ویتکاف و کوشنر به اوک‌ریج برای بررسی گزینه‌های فنی مذاکرات هسته‌ای با ایران
اکسیوس:
🔹
استیو ویتکاف و جرد کوشنر برای رایزنی با گروهی از کارشناسان فنیِ احتمالیِ مذاکرات هسته‌ای با ایران به آزمایشگاه ملی اوک‌ریج در تنسی سفر کرده‌اند.
🔹
کاخ سفید در پی دستیابی به یک یادداشت تفاهم (MOU) با ایران برای پایان جنگ و آغاز مذاکرات هسته‌ای تفصیلی است و قصد دارد از پیش تیمی از متخصصان را برای این روند آماده کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/656440" target="_blank">📅 22:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656439">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgx5Q-1t4rwEfik7XeXGnVQy-Dvw34sogXohhPNEHcwS3DO068BF8nP-ZOwppZgdR7pvtXiVQaZiFFlkPUdoRCbKoH9BR3CXGMa8Rs9gjo9cVzTpCyln0K2xPsF7hRA3dZihYhthQ2M2jwxImoRZtNJY0pYzj06ElM-FwMMOqnJ6yM9WXhRS-1tMUeNHRk0AMqaYPMP-tvPnRTNM2_NAce5bUd_Tx9FvsYbOnicvfLJ9E6lQwMUth2GRlaR_XqfhTaVXqhT-esF7gHZP7kBnsZs5VYbs5ygf1qLg0nWSWnh8ZSxIpV70CbIoih_ngTkR-tk4-YyDJmEo_aFjw-4rdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر منتخب خبرگزاری فرانسه از غزه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/656439" target="_blank">📅 21:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656438">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ادعای
سخنگوی دولت عراق: سپتامبر ۲۰۲۶ پایان ائتلاف بین‌المللی در عراق خواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/656438" target="_blank">📅 21:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656437">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33bc160535.mp4?token=GJovYEXsgRxeU9agcB2NiczijBW7miYFPDmOcaO7wx0z9Ywqx-h5l2M3z2hl2YwscG1QFWYjqt1BlZITHzobhVCX8ESDiWAtP-_JU_We0t3aM0Iss5oBMghYvOBXBAPvLhyVZOUDjscqRU55DXropPRxAeO2vLbjWw0L_K-LthstYDBbaZ-slw5tjZkMb3Sgm5d5lE118iTd-i8MkTl6GqmTeSSd3TAnsJtDmWoCpOP3n2IEL05f1cMKyLxwg1i65d2A3Geh3DeASpYbiw2itdKMcx5WMdp1GnzbzSUPHYugsG4cQfXYPRpCnEdl62rIo9IRJruZZWkKKC-uAvhIEx4DmvjMvk-nOS-w4J2XAhPLhqAPndAObtDWBXuI4Ws0znpTKHzS0SpcZQno375PX2on0yq8mdiqc8p2QwVMGZdENWy6uYPlSEkJrkpr2zPZ8QYXc4fEBIzkOm2W17frtnI3bs9bbWUV3gDSnH19JVyBdOOnQqOF4orRlxA18QjqOxcOiHq4oSQsuhzH3C1BkcBBSwimCD-EqkPcHOF0bGoTKbekajOiLkgG6nQeoRQ0whJ1gRKd8XifIlvn9X09LixAhH7JOb4p3ecn-eK_GnyGJD6Ov3OsOV9CjWNia-wWQsFD92nJ33wZAfEJ1Nv056eGFkNi2oXTjoZTh1rKX-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33bc160535.mp4?token=GJovYEXsgRxeU9agcB2NiczijBW7miYFPDmOcaO7wx0z9Ywqx-h5l2M3z2hl2YwscG1QFWYjqt1BlZITHzobhVCX8ESDiWAtP-_JU_We0t3aM0Iss5oBMghYvOBXBAPvLhyVZOUDjscqRU55DXropPRxAeO2vLbjWw0L_K-LthstYDBbaZ-slw5tjZkMb3Sgm5d5lE118iTd-i8MkTl6GqmTeSSd3TAnsJtDmWoCpOP3n2IEL05f1cMKyLxwg1i65d2A3Geh3DeASpYbiw2itdKMcx5WMdp1GnzbzSUPHYugsG4cQfXYPRpCnEdl62rIo9IRJruZZWkKKC-uAvhIEx4DmvjMvk-nOS-w4J2XAhPLhqAPndAObtDWBXuI4Ws0znpTKHzS0SpcZQno375PX2on0yq8mdiqc8p2QwVMGZdENWy6uYPlSEkJrkpr2zPZ8QYXc4fEBIzkOm2W17frtnI3bs9bbWUV3gDSnH19JVyBdOOnQqOF4orRlxA18QjqOxcOiHq4oSQsuhzH3C1BkcBBSwimCD-EqkPcHOF0bGoTKbekajOiLkgG6nQeoRQ0whJ1gRKd8XifIlvn9X09LixAhH7JOb4p3ecn-eK_GnyGJD6Ov3OsOV9CjWNia-wWQsFD92nJ33wZAfEJ1Nv056eGFkNi2oXTjoZTh1rKX-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احیا و حقیقت | قسمت دوم: ترکش
🔹
هواپیماها رفته بودند، اما میلیاردها ترکش هنوز در آسمان و بر زمین می‌چرخیدند...
🔹
درست در همان لحظه‌ای که کارکنان در حال تعویض شیفت بودند و محوطه از همیشه شلوغ‌تر بود.
🔹
همه‌چیز می‌گفت باید ده‌ها نفر آسیب می‌دیدند.
مسیر ترکش‌ها، تعداد افراد حاضر و منطق حادثه، همگی همین را فریاد می‌زدند.
🔹
اما آن روز، اتفاق دیگری رقم خورد؛
هیچ ترکشی به هیچ‌کس اصابت نکرد.
🔹
این فقط روایت یک حمله نیست؛
روایت لحظه‌ای است که در دل آتش و اضطراب، رخدادی شکل گرفت که بسیاری آن را فراتر از یک اتفاق معمولی می‌دانند.
🔹
روایت محمد جامعی از حمله ناجوانمردانه دشمنان آمریکایی‌صهیونیستی به زیرساخت‌های غیرنظامی ایران اسلامی در شرکت فولاد خوزستان
#از_نو_تو_را_آباد_خواهم_کرد
!
@khouzestan_steel_co</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/656437" target="_blank">📅 21:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656436">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
مجله نیروی هوایی آمریکا: حمله موشکی ایران پایگاه العدید را از کار انداخت
مجله نیروی هوایی و فضایی آمریکا:
🔹
در هفته‌های آغازین جنگ ۲۰۲۶ میان آمریکا و ایران، موشک‌های ایرانی خسارت شدیدی به مرکز عملیات هوایی ترکیبی (CAOC) در پایگاه هوایی العدید قطر وارد کرده و این تأسیسات را از کار انداخته‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/656436" target="_blank">📅 21:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656435">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrbUPodwI1QADRoLn9dwtAKEeWE0wAQlOOsEaG47UXptjKpDrto9NVXt7uE1GCYzU_xL2A2-kYtxuF6Wptzo4zvLcRwjD4tGZhulirFvU0weQsdZIPolRRT2z5yfonuS6kzRUyVxYStFrWnYjOI1Zxs3Sa6R71YSZxu333GyYwsuyPXmzTQAPxkgF_5i1WYTQh9spIa2bGBgiqoE4S3XlRi_LbiKI0cigvemKbLbe1KsTC4mJG3yB2VF0GIS6sKKTuImBeO7ow98LcnaSRD9eALdn8Y2_4fxXSFsNgj7jXSz49z-07Pb94hpXBjm09tuhbWnXLd8LUpFKEMCMSrHdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زلزله در ترافیک اینترنت؛ بات‌ها از انسان‌ها جلو زدند!
🔹
بر اساس داده‌های جدید شرکت کلادفلر، برای اولین‌بار در تاریخ وب، ترافیک تولید شده توسط بات‌ها و ایجنت‌های هوش مصنوعی از کاربران انسانی پیشی گرفته است.  سهم بات‌ها به عدد شگفت‌انگیز ۵۷.۴ درصد رسیده است.
🔹
مدیرعامل کلادفلر این اتفاق را «غافلگیرکننده و بسیار زودتر از پیش‌بینی‌ها» توصیف کرده و گفته بود انتظار داشت این نقطه عطف حوالی سال ۲۰۲۷ رخ دهد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/656435" target="_blank">📅 21:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656434">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: ما در رابطه با ایران موفقیت‌های بزرگی کسب کرده‌ایم؛ آنها در موقعیتی نیستند که سلاح هسته‌ای داشته باشند #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/656434" target="_blank">📅 21:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656433">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7056189cc.mp4?token=Oxb-6nQHGdgrtoIPeLriJiRBI0hnpC2qIoLvKs5RuwJHk-WADxjKwslUV-mE3tT1vs9u3p44vbyhnoIgM1vZM0xN0QYBzIRKvcSKcn--gv8cT42znRuqEC7ro9QMEopxpBdd5A2Iw1a3fODOGai53v-qgy7foiZCK8q_0Lv3aAb_JUbhRfsbp7neEajnNIc_avjv0QhL8ygS8pOnydBg4UiUDn61JzNo-qMZUR5_KFDOsx115Bsd6z4LDLv05GKM-55VCLOR53dFzXKiuL_lXGWuHhRExTOKmezszPm0hwJz81CCSjeEVxSSMKQcosd5MkuOUr8DNPXdHl5o0vxYLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7056189cc.mp4?token=Oxb-6nQHGdgrtoIPeLriJiRBI0hnpC2qIoLvKs5RuwJHk-WADxjKwslUV-mE3tT1vs9u3p44vbyhnoIgM1vZM0xN0QYBzIRKvcSKcn--gv8cT42znRuqEC7ro9QMEopxpBdd5A2Iw1a3fODOGai53v-qgy7foiZCK8q_0Lv3aAb_JUbhRfsbp7neEajnNIc_avjv0QhL8ygS8pOnydBg4UiUDn61JzNo-qMZUR5_KFDOsx115Bsd6z4LDLv05GKM-55VCLOR53dFzXKiuL_lXGWuHhRExTOKmezszPm0hwJz81CCSjeEVxSSMKQcosd5MkuOUr8DNPXdHl5o0vxYLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: ما در رابطه با ایران موفقیت‌های بزرگی کسب کرده‌ایم؛ آنها در موقعیتی نیستند که سلاح هسته‌ای داشته باشند
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/656433" target="_blank">📅 21:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656432">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80c2eddcb6.mp4?token=KtMNHvRXG59Km-SxulwNFvkTrU0DTLhxdhG-2y7f9T-fp2MQt2gZFY6gLGhn-A8uXUm9SMcg2lw0mKxF83bictelVz14ucW2cnqlKPrGzFYEe0zjcBh_lakdJW7D60TSiGrmFPPKQv0t9yh5n3uJSzXFw4fG3UgUDQlfoZwemRxm-e6jIxgGeMItqbFICcT1WOEot12wTKm_v0kX-W4x_e3x_C7Qj97fw4SB36z6IoisejCQjB8XrGCWHY0oxFFc-vZeDO0MURlsbKI3SSciaFSy5e7DNnxRtc4gAQAiYbCC1yhmvTptUHYV4St2dIEt_zrn-6sx2RqUPMAh10IaLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80c2eddcb6.mp4?token=KtMNHvRXG59Km-SxulwNFvkTrU0DTLhxdhG-2y7f9T-fp2MQt2gZFY6gLGhn-A8uXUm9SMcg2lw0mKxF83bictelVz14ucW2cnqlKPrGzFYEe0zjcBh_lakdJW7D60TSiGrmFPPKQv0t9yh5n3uJSzXFw4fG3UgUDQlfoZwemRxm-e6jIxgGeMItqbFICcT1WOEot12wTKm_v0kX-W4x_e3x_C7Qj97fw4SB36z6IoisejCQjB8XrGCWHY0oxFFc-vZeDO0MURlsbKI3SSciaFSy5e7DNnxRtc4gAQAiYbCC1yhmvTptUHYV4St2dIEt_zrn-6sx2RqUPMAh10IaLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حقوق خنثی‌‌کننده بمب چقدره؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/656432" target="_blank">📅 21:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656431">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
ادعای نتانیاهو: توافق آتش‌بس با لبنان هنوز تکمیل نشده است
🔹
بنیامین نتانیاهو، نخست وزیر اسرائیل در نشست کابینه امنیتی این رژیم مدعی شد توافق آتش بس با لبنان هنوز نهایی نشده است.
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/656431" target="_blank">📅 21:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656430">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAi7pQLZ6RMcvWctCPCRb__VfI5gVjVAYpn5Nr1stF8osy9aKqvQWTPWvjDy-rSxfUE-iCzz0--zDlb0r82ZWdepH5ECTNWl3u8iA7YZ9aq4sCIt6tGCGOe0VGmGHwI9J47CwrEbq2pAuaqy1YsXXdBCDRuFNch4sEVAhk11UnCd3URWa6zUGm85yAuJ3-JPdMRjdow7tfwzf8FWLX2j2u2MBuQ2Z3oTiSgBmp5Y-yIPiSpDDk74_cy_UYTCjvtdFUHoD1m1ddDqZ6mRa5Mfm2hPrTPrBibgGikuicpxNjzhM7TPDJKrCOSxNzBY7O21LzWPzb2SqnU199kl0uI1lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طرح جدید فیفا برای مراسم پیش از بازی‌های جام جهانی
🔹
فیفا قصد دارد آیین پیش از شروع بازی‌های جام جهانی را با حضور تمام بازیکنان ترکیب اصلی و نیمکت دو تیم در اطراف دایره میانی زمین و همراه با پرچم‌های بزرگ دو کشور هنگام پخش سرود ملی برگزار کند.
🔹
به گفته رسانه فیفا، هدف از این تغییر، مشارکت همه بازیکنان فهرست تیم در این لحظه نمادین است.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/656430" target="_blank">📅 21:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656429">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db8e4d50f1.mp4?token=kvOgVE0eUibEAsWGl6-Y7V7CZPtHGtQoeCu7eQGqPm2DUCqJQem_KDPvVAtK7IjrBolgJSYV-QQlOBLU4_mamOoWTwg5GF2OcQwk870whR9hhmbfKQaNS3XkOwel7B-6gtT-ts0QLmTvVs_Vc0Nso6zry2x1_4kiat7poPMOv37n_P_QiQt7ZJQI-m6bJkCeTY1WaOlTMZiW9dgIhSyc7qPcM3h9tATl_blmzgezMT1GS5b7CKIPnAKHDSSo9MHBAhXfL4kL2g9qdCRLErknSUt-AQeGGU0xu7IrgFYL-gzvTIExFOHWd4ITM-OLt0SdwwUBWXBbjYNqH6oLZkQJ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db8e4d50f1.mp4?token=kvOgVE0eUibEAsWGl6-Y7V7CZPtHGtQoeCu7eQGqPm2DUCqJQem_KDPvVAtK7IjrBolgJSYV-QQlOBLU4_mamOoWTwg5GF2OcQwk870whR9hhmbfKQaNS3XkOwel7B-6gtT-ts0QLmTvVs_Vc0Nso6zry2x1_4kiat7poPMOv37n_P_QiQt7ZJQI-m6bJkCeTY1WaOlTMZiW9dgIhSyc7qPcM3h9tATl_blmzgezMT1GS5b7CKIPnAKHDSSo9MHBAhXfL4kL2g9qdCRLErknSUt-AQeGGU0xu7IrgFYL-gzvTIExFOHWd4ITM-OLt0SdwwUBWXBbjYNqH6oLZkQJ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای عمل نکردن بمب سنگرشکن در دفتر فرمانده فراجا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/656429" target="_blank">📅 21:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656425">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KinLqGhPO0FqFPp10k1ZPYMQZyhFOaiZ0yL_KydYSHnVokfHdcImXFeo0N7TWLFBxB95IsbR8tDG9y7EEldo3O3iTDW8pTBjQkOIayKeUHB3E3OFCGavky74ejkMl290Uew2rLmDFjNMfgs11dQzjgPSawee1-H8kbeI8ROmj_fZSxy8g0FDNQbwNYx487U1eTUL2QjWzFFL_YtvD6it7CCPReKFH_wfROAsA3VRerqG1TxqyhqSGEfgQjwPBxljTwUfhKpCP8_5KWQQmaQHc1LRnx2BkhPAvKsjLjuwy17yCBV-3Na45DnZ1jHI_PAhpcf6kOJKSl9Cb39RGjGtzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p8ewTxYZ6N0XT01kbRwg2K_uUbzi3J3RWnVKhQiJMH6AR_VulMgj9urSzj06b8cmApPy3fUZ1kK7R2ItogBHbb5vvExZP3Bhu3QQwGdPRSozr3RFL-_hyeBLXH-FeERd91v0bwHQ605FmK-mH8o3M3vh8YhZIdwwChKkLNfiW13Q5N2EfdoC8-iYWGF-pRTRDV1i8w4-9kNPTST5QmXmAePVzOeBt9KCZSM26pTR3XSZ_8-hPG1yqb58Pg11O_nigpTutiOq4jslVNvZ8OPGRoLMmLrxMJBR7nPWV9S1Lkmu4b66KB75gyuHlRPNdu1g2s-LpSdDr9cPwEvXjOxdwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DaPhqvmOmD-KKSeneIWVag2YygWEGJkc9bX4be8qk_QSXg6oS7bGWuDgNZZlnPzBb0e4rDFRIdlsdDen3XMK-yuD4X7IlN-EXMxVCdohx6e5Mn0_J517D6D99o2sNlzUFs9plsCc66hc5JoVOZa8o0SynhEP07y6fBWBe7zPY-UZk0wqqBaMFtzbYEOKZrBsYWxlOq1c__Ugt3bhfpId2N5QcISOxs3z3ilkVX2UdMQ4EOwqRbKoOALOFPcc44sc3v8D4o6REN0ZpFOj7FokKLFSLIaA_bIVNo0t7Pf4_AeFHmJ2jog8pFa9qFzESm6EFw0bWesVutwnPXp6R9cIWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hJtk5Z36mRlhBJ3e-maJ65LE0mFxuNHLnpxcF9cT18n-ZhRsz-qCIVLryp6nhKAx99Uokdzcsy7YqmA4HYeGJAJvFXNbjHVJrZIZ-ZUa1NCP00Kv650lZOWNOqotVEWy-sAXAQ4PpdTppBmkVLm3pDqttoba0bOftlAjEGTUjm2orcG1RoWtwJBeBD2PoAdKzZaFAuqxndYrIT80J0HP0Zz8_UWaRsX6WcGw81o_V6cCIdz-gF7U3rn7Enb-R77Nh6HP4hx5dYgRlC4e7C3fmXSzgs5zVMP1fBw1XugGUnmMtFiL7HnZpJE_xVyLHJBeMUDRzoO_oMy0uCSgjyzjZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ترامپ: توان نظامی ایران‌را نابود کردیم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/656425" target="_blank">📅 20:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656424">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
رویترز: روادید ورود به آمریکا برای بازیکنان تیم ملی فوتبال ایران صادر شد
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/656424" target="_blank">📅 20:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656420">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/md17XJqoTnH6jrQ8hHNwbOenqCYX22NgzbF3QTg1YplKWk5FbeIn4jnG_x707oEH8J6SXqKIWqZ4RY1j2sl7ZMtWt63Yy3OyKnpsMVAzc4ejFczLTcTTcBZLp6f-NuS4v0j45R1RwT6op8OMGQNCsZ54rXlQJfxP5sIf7BdHP8iqVpNC-jF3DmwJBcrf0y3BQhDHZ7B7RhJX7oQ5c4rUXk6YpoCYKvL24LKIgS0sF_wZsnsZnlxGxZbtxANJRVnebMIHaHPLYTHDqL53QMec4UC03glBkdoQ_0v1sxNVOyzdUwDTRJMLbYmq6halETYJdbxkPU_bOJXqZ8TkTXL0Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egc831speW09vMAZwFpqhHhAexxwfzjodAY8uC5vs84rYSQX9kAlfaPTKhCfq9hBpPK9xLOTb-1mECbj8EOte3pxCEhBC2yQw825sc-4ioCqEKIBvQMYuazI_W2Ml4opYhmrn8cLgE7TiM2Zf7-5UrXHXkXmifwMW8NBCY4xU-RjUV9GefUpnmAsM2wX6zWvpZeD7BIGpDomRtTTYWz_gRhCSA-xPaGFOxAn78O0fibdTIvdpGI7lKLNSofwjKxY0OTjfF2B_H8WNaTJtTvEh49-DApCtnsFLTXX-cXbgJfPkRyRF7VQfH-kUtLF0h1Lc-Ss26cecg-ssy6Gk6KrOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qox5sAg6WmzegxiJ-DeWi_GS07vbGYAgDdIqUOYkyVYmN2pJ-j-354U-sd1aGIHQqubZ5TUiK8dMAP-CVzrfEsr9qFiZqS-xSs3Iy3AO4ewq8QulT9EI5rzS1mzdOImcd0BvEUuCNL6E0skxd0QbC_WM-dWAvcvoGk_AWn_mxjeKG6eIOQJLR0_9dgo2DySCOw4JaEZP5TbyBrPingMV4xsIEQkLagLDQ_rUfgjpAMxbdyYgB5b7hiRMCrBuEsuT0n5qfkX8AbpufDJcC4BDjwKUyqa5GxsSMIbwDIT2Dn6DQNVfTZZEht79GGgOJ2N-IHs_SEnv0nhCJLLN4iuKXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C0opNdEwCmbQ7OdYrZ2v8wKJJf_f636_Xksuy0-Skzg5P4WxFC-OToGGgwD2o6tgUW0ekVgHBzAXjrDw3hWTtjDBzFXo-eI--iywvE9o176UQQEVxEwpaQgZQaVsMqX9Nj0i2pf9R6zTBZLg3lAslWXnj7GAIu_N7_BmjvtYTQQoEbVuYn_cQSnkiq9c1vqMFsaTNwAlT5ECI_au5tFNkQ1tsi7FjN4ZwIv8MZVetue0i6xers9A7ouKwYzwXXJ3ijOqIZzj94e6HfUqsjwD5eQJQ4U5bMDKpZZaFfq9Od8yEB-KveDrEpsWHs5nSorvjy3oJS0XnHNqLHgytFGl4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
افزایش چشمگیر قیمت لوازم برقی ضروری در بازار
🔹
در تصاویر منتشرشده، قیمت چند مورد از لوازم برقی خانگی از جمله یخچال، ماشین لباسشویی، ماشین ظرفشویی و مایکروویو مشاهده می‌شود که قیمت زیاد آنها قابل تأمل است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/656420" target="_blank">📅 20:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656418">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JHuxyBRcuGR9hW-_egXgiVfFvIAtJKosH6Anbkm4kyQN7ghKXssNoVitiptvMRM9B9dHWsq2vbyoUAKgICFCZZ9eSK29MVOpJZdvs-k9EN3M99_QJM-A8xlwCjhxb_69bAOpN1-cGbZ81jKBmuVeShER6sp0LEm-bMT2h0hW3U8a5FkrENp5AcDeGPKJ-wFYRZ3l5SUbJxFdViH3IeDGT3euRgI9KoyUsBZYSwCuGj8mnTrtDHaFcbG7SvaCEmhadDqgfivIz7f-CBfaZpDJaq6h1KGCUKEqi1Wp2eK0wQ8oG9hVXfMaDFYlc8oeVHregDR_kVK_q39z6YPCY2lGCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CRinVyckgHk-C8OLzOTWCy7ADp7cWd8Rs1TsttMkPiloA3U-NMwEJcsrZJUeBzS7uezxqn3-TVcp-zvD4ngUdSvgK-QbcTyqOYbvtesa78EKmR1zFBd9tVowjvuoZVu2d3sLj0f5_TYt8U66A3ElDNrN6ADmm6tTAUG9LlMXml7bJgFlRrjN3HBZ4oEqM1v6YQ023X21CXDcEm9m103J3Hyik-fefDfBlPLEiW_1QKSg3BOtZFIoTSnqJ6hBvF014JPcMSYnqs6IQ95LHjgPQeWUEBtuzvB9gdLNR0Js4RzXAzzkDYe_6B7TCWVDV_uqhY_9uuRg4jFCBhDS2S0pfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فقط به عشق علی...
🔹
در پی برگزاری پویش «به عشق علی(ع)»، مخاطبان خبرفوری عکس‌هایی از کارهای نیک و خیرخواهانه خود در عید غدیر خم را با ما به اشتراک گذاشتند؛ تصاویری از ارادت به حضرت علی (ع) در عمل.
#فقط_به_عشق_علی
#LiveLikeAli
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/656418" target="_blank">📅 20:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656417">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
توقیف محموله سنگین سلاح و نارنجک دستی
فرمانده مرزبانی فراجا:
🔹
مرزبانان ۳۴ قبضه سلاح کلت و mp5 و ۱۶ قبضه سلاح شکاری به همراه ۷ قبضه نارنجک دستی و مقادیر قابل توجهی مهمات مربوطه را کشف کردند.
🔹
مرزبانان علاوه بر انهدام باندهای قاچاق سلاح، تعداد ۷ قاچاقچی را دستگیر و پس از تشکیل پرونده تحویل مراجع قضایی دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/656417" target="_blank">📅 20:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656416">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
پوتین: مسکو معتقد نیست ایران به‌دنبال سلاح هسته‌ای است
🔹
رئیس‌جمهور روسیه با حمایت از توقف اقدامات نظامی علیه ایران گفت مسکو نشانه‌ای از تحریک از سوی تهران نمی‌بیند و معتقد نیست ایران به‌دنبال سلاح هسته‌ای است.
🔹
پوتین همچنین از آمادگی روسیه برای دریافت…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/656416" target="_blank">📅 20:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656415">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
محسن رضایی به سی‌ان‌ان: آیت الله خامنه‌ای با ترامپ دیدار نخواهد کرد؛ آقای ترامپ مذاکرات را به بن‌بست کشانده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/656415" target="_blank">📅 20:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656414">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
طلب ملاقات با خداوند از فرشتگان و روبرو شدن با واقعی‌ترین غم
🔹
00:12:00 نحوه جالب جدا شدن روح از جسم
🔹
00:22:00 کنترل متفاوت نگاهم روی اطرافیان
🔹
00:24:50  علت موارد شخصی که به هر شخص مرتبط است
🔹
00:30:50 تأثیر آرزوهای ناخودآگاه بر زندگی
🔹
00:39:00 طلب صحبت مستقیم با خود خداوند
🔹
00:43:40 سنگین‌ترین غمی که تاکنون تجربه نکرده‌ایم
🔹
00:56:50 عدم داشتن اعتقاد به برزخ و دنیای پس از مرگ
🔹
قسمت هفتم، (باور)، فصل چهارم
🔹
#تجربه‌گر
: حمید علیزاده
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/656414" target="_blank">📅 20:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656413">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
پوتین: مسکو معتقد نیست ایران به‌دنبال سلاح هسته‌ای است
🔹
رئیس‌جمهور روسیه با حمایت از توقف اقدامات نظامی علیه ایران گفت مسکو نشانه‌ای از تحریک از سوی تهران نمی‌بیند و معتقد نیست ایران به‌دنبال سلاح هسته‌ای است.
🔹
پوتین همچنین از آمادگی روسیه برای دریافت اورانیوم غنی‌شده ایران و ادامه رایزنی با آمریکا، ایران و اسرائیل برای کاهش تنش‌ها خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/656413" target="_blank">📅 20:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656412">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e3968f346.mp4?token=C3Oen8UJXCO48Gh9rtXw174isNKfgI9FD61s-QyHZ3XNmGs1lJ1ljZU167hwtlp5YntXOyPvL2oMrLaAKrK8dfL0TEIq0Uw--cJp09DFrqIWHwZ47eif1jzZUNxWJalhjjnN3C3PttfHIJ1gRPZJ18isrQMA0WNTD1phqLRAC7s-DsiSIqt9_97SEOECIKWozSmQC173bg-J5jDuUzitu570je37S6Ll3GeekbjOSz_aZaHPkXgN5ustiCF06mRUNeDf1DTRJEVYq750uWmR8CdyVenyfPkkhAsL6ptCCy1WbVpmqFdM0SL_I4JuJdQfNlcQCapyWoxYv7ZPMiofuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e3968f346.mp4?token=C3Oen8UJXCO48Gh9rtXw174isNKfgI9FD61s-QyHZ3XNmGs1lJ1ljZU167hwtlp5YntXOyPvL2oMrLaAKrK8dfL0TEIq0Uw--cJp09DFrqIWHwZ47eif1jzZUNxWJalhjjnN3C3PttfHIJ1gRPZJ18isrQMA0WNTD1phqLRAC7s-DsiSIqt9_97SEOECIKWozSmQC173bg-J5jDuUzitu570je37S6Ll3GeekbjOSz_aZaHPkXgN5ustiCF06mRUNeDf1DTRJEVYq750uWmR8CdyVenyfPkkhAsL6ptCCy1WbVpmqFdM0SL_I4JuJdQfNlcQCapyWoxYv7ZPMiofuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی به سی‌ان‌ان: آیت الله خامنه‌ای با ترامپ دیدار نخواهد کرد؛ آقای ترامپ مذاکرات را به بن‌بست کشانده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/656412" target="_blank">📅 20:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656411">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
رویترز مدعی تهیه پیش‌نویس قطعنامه‌ علیه ایران در آژانس از سوی آمریکا شد
رویترز:
🔹
ایالات متحده در آستانه نشست هفته آینده شورای حکام آژانس بین‌المللی انرژی اتمی، در حال آماده‌سازی پیش‌نویس قطعنامه‌ای برای محکوم کردن ایران است.
🔹
این در حالی است که تهران و واشنگتن در حال گفت‌وگو درباره تمدید آتش‌بس هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/656411" target="_blank">📅 19:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656409">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfp91cffGQI07pyKCBr0r0xyhQWpwQr86DvuQ34S6-XiFO4_uhl7hHuA1rVXH1WEc4Y8S5rXK2oV87nsKp2oMTVWjHUUkfJ2ZUs8PRjNaBCd0DsGpLCCl9-3PVZkdORNJI2XcQ7Omh_aJRn8yDewCEFLuZEO4fZdCxmlzRQiaGVek8udy3aESQWyv485dx2mzIp9zNSekJaS6O-H--GY38d_lBNmlOfwh0oDmCBhps14612gAnnYIM4kCg_GIorhL0tCAb0YiGy7skJWXCRsrD5GEEJHLkLM0lstlycI4phI0S5bPOW0Bl93spDigeLggRiUE37Kss_Je6o2-de9iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPNWy1Y5igEGd6W0j3r3xkqQOR4ytgTaR1LyLJDG-So1ywE_s1Etq3AKfcsEQMbjE0MLU6xwnlJ1_IHIyTupESSqGmPHtP_YaKrnzBbgC8NbuM5raShGe7G9bLtzxxZyYo9iwEtWFxGxF7sP8BTF31dUGhhivnP3nA0TEM2S8r-UNnEy-plDO6zPKjoUZNINNBfqXOTm6m4HQAyAp3ceF0BLic9FQVp9_AxcKBNOEqAtBzAIGImDs8k8CqQcRrhYHTmuxvRWj3xqEcUJ-na4fxHVX-gnrXK0I-cQgvGS6FMGFpEEKnpkbfAcIN6u0dVB0_3595talkH6ZqsgXzXIBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فقط به عشق علی...
🔹
به مناسبت عید سعید غدیر خم، مخاطبان خبرفوری تصاویر اقدامات خیرخواهانه و نیکوکارانه خود را درپی پویش به عشق علی برای ما ارسال کردند؛ روایت‌هایی از مهربانی که به نام امیرالمؤمنین علی (ع) رقم خورد.
#فقط_به_عشق_علی
#LiveLikeAli
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/656409" target="_blank">📅 19:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656408">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
تحریم‌های جدید آمریکا علیه ایران
🔹
وزارت خزانه‌داری آمریکا از اعمال تحریم‌های جدید علیه ایران خبر داد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/656408" target="_blank">📅 19:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656407">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdPhc3MZyiDtCbI81NevtE6q8_GJLoi1HpC6EUw9bYXjMHKD3GZOcien_3cm0IMdaTdA0SvDq9HcufDDH7d5j-4mc5jFo955ZiW6AelHl4oW1khCyjsqmp4QRIUmZg8qWlyillacw0svUsV-tnUI5pYz2KFzgurXvHmf_XlZVvY-cJXzpu6I4kmLsvzHKsAz4x3Rxn8eVLd1bfPjaQzOrl9swe1UpZnvPEiaAOGvqbQeBOLmBaq0fQ-7dxF51vaHx0G4vOy4No0m016LCgHsO_qFqdLdtwObW95Ce9pwMJgCKGx6kBx4tGR23qGn4fYDIYpBaKB8KwFOB0DDAs7Ctg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان در شبکه اجتماعی ایکس: سرو می‌ماند ولی طوفان به پایان می‌رسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/656407" target="_blank">📅 19:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656406">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
زمین‌لرزهٔ ۴.۸ ریشتری در عمق ۸ کیلومتری زمین، حوالی منطقهٔ بالاده در مرز استان‌های فارس و بوشهر را لرزاند
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/656406" target="_blank">📅 19:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656404">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CF9St5mkCLR3SJ-yxe8qBbic_4WRfHpQiwX1umdhtTdCIW0ozb_c8EvTvbyVr9IBzTC7bob8Fu3Cf37T-KiTwREWjiywRm5Hul7kZ76iyMc3uwCCtFl8KKfK0njjG9NaHE5V_PZlNGKLfiK5P90vz3Durc35O8uMXi0CxThU5q3z6iaxPNedrPERdB-jwbnDMsocb7_QxvEaSGDr37nQt_LGsTW1nKHS92I5OCGzto5eBVwpsFhaEvSJQeaWi7Dume1DasLeuvmzTbwBu1Q2Bi1lIRn_xfgOKWKiAkDsOxhNbom9bSsst6YARRXpZ9NeU3iZaNqQUhmva183XRNrUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از سنگ مزار شهید علی لاریجانی در حرم مطهر حضرت معصومه (ع)
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/656404" target="_blank">📅 19:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656403">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VApl3DRaChtSoMInRSipQEz20r4hwn1isKyZciZKN5Yr17jYGyss5WlSbbboTHm3xE1Z9KMIbM7DKbP2EzRd4ufo5ShqKUfn4cZh7m7lMHdcAf5wpStuaypOaPwAzj9w8milUWIDZd3OFSAsW643fNDCtgxzOQA1G2ULC8ZKIScb4fCE9P2yQT8wdfOFtA67YwvG3Zm4vue2avBELxZe7IpISB5_0ZjH4ZmiiN3vrqIdha3wgwa2VpCS1I973IeoCfn6VQAAV-q3F7Z7sNrHGHtST3Tn7Jmk23ALttQoLt3gsPCTXUwwF4hRvGn3s0dRYIMuq8Rn1D9efJDuUD0oGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بگو مگوی توییتری رئیس کمیسیون امنیت ملی و مشاور ترامپ
🔹
روز گذشته مشاور ترامپ در پاسخ به ابراهیم عزیزی تصاویر موشک خیبرشکن را هوش مصنوعی خواند.
🔹
ابراهیم عزیزی در پاسخ به مشاور ترامپ  در توییتر به او یادآور شد: فرار ۹۰۰۰ آمریکایی و تخریب پایگاه‌های آمریکا در منطقه هوش مصنوعی است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/656403" target="_blank">📅 19:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656399">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MKAzhUQ7mSN5DrbNwao-X1nFcKqbAXAI0yugkJaH7xnJtI-7gZtGo3eCpEPvJRiFUane5HpKGK-lt5fQrYQm16XYIwXm5OwExwItNSjm9HvcffGXopR0LUP-GZxSo_P90nN-0MyOVqycsQy-8NK8H1tf11Iyr2ct23m0q0zUBMs_Giy3h_Y5T6ahQbL3iH5oBjOIk37pF7DwzlPMss4WtZ9ePt-A60PtHrm72YL-D1utnBmHC17fE6fPiTYUH2djfjziPx-mJ-GbTYoXwGPcJFzNjdAKzgrYfMPMLJ4_L5Irc4gCHT8y-ohrkHQaihZqNRtsrKO7gM99fJ4Eqyp0lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BuDNNd_knoeKElO5NHbfO3KWSTFrisGTmVKf7ZVauXa0rtHN9gULWQXmV_7oTDaEI4C7m2Jhi_fRqLD7kh4UCQg2UZbD4RtoWvDbVhWoMT4CYD52c1lquARgQ3wPVUUgDKidj2IpTi2dOoWitDSCiTiDDuogFxeIAiF-9dCFYoEoImtJElsQnOgydM_aM8FO4zi01hPAuBE-8o2ahd3_E6JwxaCrc296W2SHw-XCc2wqICX70L4Xt66AVZsDAKRRURV_-MGLYg92VsFqU10tb6hMb6Vtie8nY6JVT1yQM0NAiqnRK4e-ynlS_2I3kZ5A1F7hxo6nk_0TeqOLVevEaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kUqgHcWAXbSZnp5rV8Q4RoKRx-5L79zeGa_l_MbN01keLY4-DZOvXOSnBFkQxa56WZ_BWbmzfxUNVKiiqVo8Va3gITvPlfzY7TozfQ0DNqQT5Dy3fJK_jbzYZiAqNhjOLk_YdhF1fTZqNTvD4WTLcV3kXoY6c_Aw-TKHGnlgjdsf4B9vk-EjFLfvtgKk1CX-T_Q7-vyw_kKmB6sx6f3K8aJamg6r2ugivyCU7ZVFjRw9ti7QaG2GW0K6TmH0B-W2vESMtCZC6kdcJmEbqSP1mG04phdQC7gdA0VZ2mMHQNv6q2w--2b6jzLF2_OPkOLDNUvvvPlNjVzDCstMF0DQOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KU7B8_wt-taYYCNGI52TIgYMvhVtyMu2YQVoBJ4JXPPXICfMIeaIZRnp_GUPfJJfwhxSN4v7jwMDxpYui1Q87IseY10yCDmn4ZM2iUxxo5ihGBOICDF-OefSL2a7ZgEoICVIdLvSS_NU0ZBt7clUDFogDKcfq6Red12xG5MT-NNoCVD-XwVBiJacwNTI6kCYuBEetAXiHi8sNwEUWri7nt75tGTj1KLDsYaNboH6tC5jwYivaFUfqOpE42245ssTfjgvzhpZf2fIQ5IrOPO2JkZAqUrKOIS80Yg0HL_7PAphiWnjy9K6pbnkczdYCeGBWkmcFSSATzVTu0Zauw_9uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تمرکز اپل روی عینک هوشمند؛ جانشین ویژن پرو در کار نیست
🔹
گزارش‌ها می‌گویند اپل توسعه جانشین هدست Vision Pro را متوقف کرده و تمرکز خود را روی دو مدل عینک هوشمند گذاشته است.
🔹
همزمان تصاویری از نسخه مشکی این هدست نیز منتشر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/656399" target="_blank">📅 19:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656398">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EO-tLKuVkhnq_QXdxDDo_2n3eQyspAAw-BkJmNzGBd6elTRNwML-ipXEMJjP3PFEoQvsWDDelx9c567ItJdWxf_UYSnvakpBGFVrnJureOAJaAraPY2bWklUqTe9SllQJXDTjPrKyrjTq0fltMVoKw3o7rGwupo8sCsS3_gZ4N4n-sa6Or0RipJCMHVa5mv1r5jTDzqviOfkcFd4IJZWWJlXk1JwY6B0ZnD9JuS0auEzya0k3ysxFD3quSAGi3ZWUPNt7L7UjavmQo-OeNi00Fg_vxtZHdIT0aT2x1vaswUIHS8AzeHlw8fXHAHcQpwkpwvF_tn0ldu1Ed15vhTo1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/656398" target="_blank">📅 19:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656397">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
پوتین: دلیلی برای دیدار با زلنسکی نمی‌بینم
رئیس‌جمهور روسیه:
🔹
نمی‌دانم که چرا اوکراین نمی‌خواهد ببیند که دولت ترامپ ضامن مذاکرات صلح باشد.
🔹
زلنسکی خواستار دیدار شده، ‌ولی من دلیلی برای آن نمی‌بینم، در حالی که ما به توافق صلح دائمی نیاز داریم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/656397" target="_blank">📅 19:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656395">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2UfU4R7tn7R4GOfZg6Y6JyM6tsZ3hHR4of4qmZ276BWMAr6DSTw3f7LZ4MMYb50YTWBmOM9PBO6_Kck2AEJoQx8VNJiNobvNqcaoq2uNCjiqde5F3n2ZrFFBMbZAyYwi_y_mIcJautcqxTYrghknSP-ViJnS4JQiPdLTlTGznWZnnEA_Biudodf5ev_KO8soeW-BlRzOcL1xmj6cPCnDWiMgWRHUnXfVxaTG4IFUC9lnVKWJWDrstcmQpDekKmBfegc_cumpgaptOfEoOO9z83gS8ExcOaD9j-2m49PSMupTxY_XCBL477ofyCY3N-4z1h2inkDLJ8LOfWFaC1lsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ریزش رمز ارزها ادامه دارد
🔹
برای اولین بار در ماه‌های گذشته ارزش بیت‌کوین  به ۶۰ هزار دلار رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/656395" target="_blank">📅 18:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656394">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mkd9nh7leO7iuM3tfj-IMOrKgNfdMigDKWDrkQ08CoBypUmzCVKSPtWe3MWPDPBB-cR_QEElE-rQVe-6Kw-Q1k_vL5Rhb18vGIUkO9jbV3yViUCLEJYX1sLxRpkotMDBb5mIemqqdYdYnr-b0HfDBcbd0ur0oMgUocEurMfRNyH97gP_ZnSfJYVpqs6HyRKq47UsZOzvp6Qkf6bXlXq7dGFgGSmgvEWCBHgUEIcmKLrTYYiIvjtzPJHK3f_nXFyPLtsqKkKDDqiXvzX3UezGQNOO5vgpbs96ba4ApjE4jrcUIlh1KH4K3HuhAFeGYvx9PIw9U8LxJah6Ct67oFYoBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/656394" target="_blank">📅 18:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656392">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
تخریب کلیسا ثبت‌ ملی انجیلی شهر مشهد
🔹
تاریخ ساخت این کلیسا به دوره پهلوی اول می‌رسد و ثبت ملی بود.
🔹
هنوز خبر رسمی از علت تخریب منتشر نشده است.  #اخبار_مشهد در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/656392" target="_blank">📅 18:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656391">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
تحریم‌های جدید آمریکا علیه ایران
🔹
وزارت خزانه‌داری آمریکا از اعمال تحریم‌های جدید علیه ایران خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/656391" target="_blank">📅 18:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656389">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/so0u0iyO5_rKycSPCXHCNeNXz0-lyQQ-AYYS10391lYz1c6WWER7a7B5n6I14nXhx4BUKd4bJ37JCvpRmxqmvuU-h5SvAagkXvqY6Bfpy9htYyC41-fqm1IrOrQCA5DhgnfDttHJqnR4YzogyT5_cZfjLTY8kxlXbl39koT9Khmu65M-G9Jx-UBHWu7kzZ0pUTlaIES6v6jgtHKZMAQtE_MgToiGEa3UtXiR1TfRJed7FI9smFuMGwIptA3LDrvJ2OOrUeIyPhMEzoW9ixZuq9zJQduIzZTHENj7q-gTBQ3hnTNouUDQITApRIdCGupo9640IxSkjLRgSnGDdGJ8pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c4kOJ8VzIL1fMoDAbJtdK6MXfHXfRufUJUKoaSRfHPTRxnvJAAIIEuHDTUk_mLNiCNU4aT9zJbaoGKzo7RBVB9wqti06NHMWhUyfFphujSRoRdIGNoELAETrfBk3mzE0Suvix5uC1kn1hsfZZ4lWaj50o0jHv2pKECfDP1yl5UrBNM6RfMqtsrss82PXN0he_D2FvPWFozdyuBxTA12HGj1fl6k74QVE2c_JTxzmz4rGfrwoI1lq1fss4sLRCkjHHBELiofdfbHOW5ziMucdoRsaKSSvtzgVVN4Imc2VTJZ56u2JbK2gquGGZ3Au7XJfrzR2K8VGisHNWcJHz0YyFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آماده‌سازی شهر ونکوور برای رقابت‌های جام جهانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/656389" target="_blank">📅 18:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656388">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnCY-sHtmiO69ndhQR1rvsRBs1Y6FgAoXbnDBh6sbWuJ8F-jNVYVm_cnH-iMOHfK57C0Bx97mZQP9lr_avC-vsVG0jrq1H8Hb5r8zfJW-60tmHKbh4vKTgw497O_UzPel9RGEOEP-D_w9mS9PrFsc81D7G6FI7xpe_qhZ2G1J2yihHNtbuT7RUUVAr-GJALPG6m5_tZsGbLOuKQiKBf7hbSvh0Rcp6NMsKC53QkDngxmFyMcPVhIvmaHtU54ATCGorqXWcLGXMgwSnUuLILyJxXhxCVPxYu5xzwHYxdiRpTuQW7L01tH2TjRyIU9A-9Wr_cJ6NJ2SQ7zsfn3Ta5Z2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«زینب دشتی»مجری تلویزیون کویت، به دلیل حمایت از ایران به ۳ سال حبس محکوم شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/656388" target="_blank">📅 18:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656387">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUHgodLuzYvH-gqNFdiTCZ2zDII-8BsEaKKUuN3F2ErAbRntaddgzm3bRUJhB4alcyrpVwywafxyxnGbZgHCV0DmspulP-MoxZGHZjKwHqazIJT59jH5k5ayjJqfAY7WI1tALNb900SHtWdDMz8eLI1hA3z9O4pj1TGKVN94clwxldDsF7x4Iexjhlq3b4ADIsn6Y4YxJgFCY-fuG6o_mHECH9RJjRWhDbYZDkReR-Hg4PI-WkZQPRIwlXZ3_1zWhWHyVZJl0kibM5VXmgCrVtnTjV077grNvmv0gwDW68kNnkyln0VpLQXJHORbP3luw4wDRKgvNMLUwFvbcebbbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبر و بیانیه‌ای که از دیدار عراقچی و ویتکاف به نقل از کاخ سفید درحال پخش شدن است قدیمی بوده و برای سال گذشته و برای تاریخ ۱۳ آوریل ۲۰۲۵ است
/جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/656387" target="_blank">📅 18:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656386">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ادعای سنتکام: تغییر مسیر ۱۲۹ کشتی تجاری همزمان با محاصره دریایی ایران
فرماندهی مرکزی آمریکا:
🔹
از زمان آغاز محاصره دریایی ایران، مسیر ۱۲۹ کشتی تجاری تغییر کرده و ۶ کشتی از کار افتاده‌اند.
🔹
کشتی تهاجمی آبی-خاکی «تریپولی» برای حمایت از این عملیات در حال عبور از دریای عرب است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/656386" target="_blank">📅 18:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656385">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2107dd4795.mp4?token=XqFfUScjYNIPUC10BJTmqF6kmQnUtQ_hXSMss0zRPK_00MAJK0xoqS89I5Y0h_mU90qUM_uwmqToy8C6P3uejVK2NWgpu27UaLrnrjw96to3-mjNqdW-j1NK62pxaD5-QhhqGIsN-WaMXSP6GQhAlIbGC_cdJMQodJmuOstShA1eKAw-SaUVE8YBIHfJjb0KnCPL3ZfJZd6ws5JWw33yITjKLl0XgM__SJX7qSjEuvbxfInReJqCgI9anKS2CfgzqxGZBJQ_8ExNjWQ06kxpxOlTSU3n1-8ZyIqw3iU5RpH0nHG1E9BO5ehTojdPEz4LgBrqV2WPcTMeFa0o6wTV3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2107dd4795.mp4?token=XqFfUScjYNIPUC10BJTmqF6kmQnUtQ_hXSMss0zRPK_00MAJK0xoqS89I5Y0h_mU90qUM_uwmqToy8C6P3uejVK2NWgpu27UaLrnrjw96to3-mjNqdW-j1NK62pxaD5-QhhqGIsN-WaMXSP6GQhAlIbGC_cdJMQodJmuOstShA1eKAw-SaUVE8YBIHfJjb0KnCPL3ZfJZd6ws5JWw33yITjKLl0XgM__SJX7qSjEuvbxfInReJqCgI9anKS2CfgzqxGZBJQ_8ExNjWQ06kxpxOlTSU3n1-8ZyIqw3iU5RpH0nHG1E9BO5ehTojdPEz4LgBrqV2WPcTMeFa0o6wTV3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به نظرتون با چه سلاحی میشه تو جنگ پیروز شد؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/656385" target="_blank">📅 18:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656383">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">شلیک اخطار موشکی - پهپادی نداجا به سمت ناوشکن‌های متجاوز و مزاحم آمریکایی   روابط عمومی ارتش:
🔹
پس از شلیک اخطار موشک‌های «قدیر» و پهپادهای تهاجمی نیروی دریایی ارتش به سمت ناوشکن‌های آمریکایی DDG-103 و DDG-87، این شناورها دریای عمان را ترک کرده و به سمت اقیانوس…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/656383" target="_blank">📅 17:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656382">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtqjsIwDPV4Da95HItyHmDn34IfyNRKOJ4__3Lsf5NdNC36M6vGra8Xjwm2HvB8gxNFAlH_bLHhkdVRJh7K7JU4NWV-jXJFGdwZKAhhn9wD7boEVvb6ANnHwxB5nGdVw8RRmuvgY-zbVKT-CkB0yBVAnJyCwyIhejp9q2dcty-cAycT5EgLoghqNBccpS0bQQnoEeptpQMb51xvnoiUBHKDR1c0qQ8e_gaIQvbMpynYe1VC3VqKOrYz7wXEOJgjBpvR6IrKQ4Awo9GYLrzDNjSsDqSrAgFUBZfKCeM-nELZZUcRXySNtJEq8kRlViF7Mx5V9ItQDJfOxdCMgpB1QUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگشت ایران به جمع ۲۰ تیم برتر جهان؛ آرژانتین صدرنشین جدید رنکینگ فیفا!
🔹
تیم ملی ایران پس از پیروزی مقابل مالی، با یک پله صعود در رنکینگ فیفا به رتبه بیستم جهان رسید.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/656382" target="_blank">📅 17:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656379">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac4c63bd03.mp4?token=Pxkzhc0itjezMiWzEsVsycv_xbHpigwnOQXoBhQ7bJZi49GUY4_oO8wDZZM-7JgtglktwpocEMZ664hPd0rPJbOkgsU5MyFe0B7638aEXWEE3HnC7LEPD3xuu0699v1fvekb8oem9zNOIS4ZNZ5cwgTgXm6xmn3Dv3QeadOaHYbyRb8_fjywaZvhF8k9oUtaKPowK_x-borC1u_LcT0JFrmQOltET4uS_Tetc6K5ORwEpkWBQ00Sthr1g4Iv9BiIvTtaLtwa9Fz82_5m-iaE-Tqwru4EVvQ9BAjiUR7yKtZrZ6YCBOfyKVx4tb4gpss5CoxEUTujKhqxMNGi-yzg-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac4c63bd03.mp4?token=Pxkzhc0itjezMiWzEsVsycv_xbHpigwnOQXoBhQ7bJZi49GUY4_oO8wDZZM-7JgtglktwpocEMZ664hPd0rPJbOkgsU5MyFe0B7638aEXWEE3HnC7LEPD3xuu0699v1fvekb8oem9zNOIS4ZNZ5cwgTgXm6xmn3Dv3QeadOaHYbyRb8_fjywaZvhF8k9oUtaKPowK_x-borC1u_LcT0JFrmQOltET4uS_Tetc6K5ORwEpkWBQ00Sthr1g4Iv9BiIvTtaLtwa9Fz82_5m-iaE-Tqwru4EVvQ9BAjiUR7yKtZrZ6YCBOfyKVx4tb4gpss5CoxEUTujKhqxMNGi-yzg-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شارژر چینی که بعد از کامل شدن شارژ، خودش از پریز خارج می‌شود
🔹
یک شرکت چینی به نام
Kuwajia
شارژری طراحی کرده که پس از رسیدن شارژ دستگاه به درصد تعیین‌شده (مثلاً ۱۰۰٪)، به‌طور خودکار دوشاخه خود را از پریز بیرون می‌کشد و شارژ را قطع می‌کند؛ محصولی که به‌تازگی در فضای مجازی وایرال شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/656379" target="_blank">📅 17:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656378">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1fa8b999.mp4?token=RbI4o2wS0HnDhc5dUKwmJFmc7tqZixvItxtHcco1gH-QQv2DO1OKXPi6PAsKjy9mKmzJNUGak_i0phsVUckNze91qfYm54nVhk19BHSoCpWU9wKQIipARUs2f4uFQxod7NwujD2uB74_g9K4UxCS3G0WFlDoS8fl2S6NPbEKTFYHL7gHLkATZn7rz_BJDykxBCBSTDkhY-we4A11yoVuqTCosurE3IAUqyjMgCpPMQXMZeqWXSTIgkN27L1NsSLkzLWpxPYRQEVzJlPGSDsUF78wFpDmyUZjCt_7Q7G5rl3-drZUNGj0Gs-8_Z1i6GS-ldjFR48WgzCPQLQlrxIDHYO0sofW-eqgBm6sxHcTTCQV6eqlJNbSZ8eL-ba_GO4p3aaXeAPDAHWpz6baCTs2l9QAw8HDYmCqFKuaXLAjbXa9-pIKJ0Fs7F1XZO-N0HTmF09nKcwGSIlm9YTIun3nPHAp6g_CqE79moVYW6gl2A1wUisMlHg_j_wMAk0xhOWq3b8bl7mv1rxQnryZUkXSaRh6ee9QN-9VldajDn9irejH1Woo8bNL-3E5F4jP4JwvfhhHi1GAZMMBBY7rtc_Z2NpS11lCweabBZ_ChxijYsnrNwHZUUXHK8d_7b9d3JJF4prZfrDO56tq5ossMX45lDRmzsmLGStLdNHjKjVPDDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1fa8b999.mp4?token=RbI4o2wS0HnDhc5dUKwmJFmc7tqZixvItxtHcco1gH-QQv2DO1OKXPi6PAsKjy9mKmzJNUGak_i0phsVUckNze91qfYm54nVhk19BHSoCpWU9wKQIipARUs2f4uFQxod7NwujD2uB74_g9K4UxCS3G0WFlDoS8fl2S6NPbEKTFYHL7gHLkATZn7rz_BJDykxBCBSTDkhY-we4A11yoVuqTCosurE3IAUqyjMgCpPMQXMZeqWXSTIgkN27L1NsSLkzLWpxPYRQEVzJlPGSDsUF78wFpDmyUZjCt_7Q7G5rl3-drZUNGj0Gs-8_Z1i6GS-ldjFR48WgzCPQLQlrxIDHYO0sofW-eqgBm6sxHcTTCQV6eqlJNbSZ8eL-ba_GO4p3aaXeAPDAHWpz6baCTs2l9QAw8HDYmCqFKuaXLAjbXa9-pIKJ0Fs7F1XZO-N0HTmF09nKcwGSIlm9YTIun3nPHAp6g_CqE79moVYW6gl2A1wUisMlHg_j_wMAk0xhOWq3b8bl7mv1rxQnryZUkXSaRh6ee9QN-9VldajDn9irejH1Woo8bNL-3E5F4jP4JwvfhhHi1GAZMMBBY7rtc_Z2NpS11lCweabBZ_ChxijYsnrNwHZUUXHK8d_7b9d3JJF4prZfrDO56tq5ossMX45lDRmzsmLGStLdNHjKjVPDDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیعت مادران شهدای کودک میناب با آقا سید مجتبی خامنه ای
📍
میدان انقلاب اسلامی
مهمونی کیلومتری غدیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/656378" target="_blank">📅 17:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656377">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">همدردی مادر شهید کودک میناب با مردم و رزمندگان لبنان
📍
میدان انقلاب اسلامی
مهمونی کیلومتری غدیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/656377" target="_blank">📅 17:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656376">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">«چالش بیعت» در مراسم مهمونی کیلومتری غدیر
در روز ولایت امیرالمومنین علیه السلام مردم تهران با خلف صالح رهبر شهید انقلاب بیعت کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/656376" target="_blank">📅 17:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656375">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3103085dcb.mp4?token=BdVhQ6nFT9huCBf1aiN7o6Nh_SjNuIDWd9lHrDsn1zHEXxVzu0RU7ujpO6jkOvN_t0CetmyaCsPkNxUfkjnihhOU7LDNR2Fzw6MALlT-MFPIxa1Qaop5WXcSZzvWEOaRVmZteRE3oi0UtLKNHqcFixCzBchn9bAVXUKV5TtvxF2KYiqLxp3M0fHh0l5UQ25lh9paTzCiy9tV8ECAbf6A4T7YBMND5z9fnDPtYPVkm0CS6_sEq19HQp-BL4pwwVaHErOwvq48IDeea6RdN38Hq2UHcofiB9-Z_MX-Z_V_o0Hvz7LK33P7sfxMly0SEG2sXEWEMCOntECkRd4DoPnPjHaL7aFIIO6BeGVVBhrr4UVMJiR4GhFxNxCeWSEOs8xoK3RDoONdIcK9ZaoOpXg_UzhnTC5WwqTLUin4b3ViIv9rVNZqvHkuc-02QjT7rUhXu6Oj5fWhQRONRo3QnO8Ek6GDs8V_xQFBE9tX4YbocHs1L87LGMOXOnQ72rR979fRYA65uBUgzENyOu6mbSYQ0_nuzJM6ONI3ERDlZL-V_M2NoRLuucoj3mbRKMvW2n3RMEX_OGAnqLrCSO3GmvXYgLgBR0m41z_dmo9Lxun3QrT1_K5IZ_Sw2C1rmg-QQiOoJx_QWs4cUMGHgQZxP_K0GUU6M-lmm99CXJCIgti5i4c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3103085dcb.mp4?token=BdVhQ6nFT9huCBf1aiN7o6Nh_SjNuIDWd9lHrDsn1zHEXxVzu0RU7ujpO6jkOvN_t0CetmyaCsPkNxUfkjnihhOU7LDNR2Fzw6MALlT-MFPIxa1Qaop5WXcSZzvWEOaRVmZteRE3oi0UtLKNHqcFixCzBchn9bAVXUKV5TtvxF2KYiqLxp3M0fHh0l5UQ25lh9paTzCiy9tV8ECAbf6A4T7YBMND5z9fnDPtYPVkm0CS6_sEq19HQp-BL4pwwVaHErOwvq48IDeea6RdN38Hq2UHcofiB9-Z_MX-Z_V_o0Hvz7LK33P7sfxMly0SEG2sXEWEMCOntECkRd4DoPnPjHaL7aFIIO6BeGVVBhrr4UVMJiR4GhFxNxCeWSEOs8xoK3RDoONdIcK9ZaoOpXg_UzhnTC5WwqTLUin4b3ViIv9rVNZqvHkuc-02QjT7rUhXu6Oj5fWhQRONRo3QnO8Ek6GDs8V_xQFBE9tX4YbocHs1L87LGMOXOnQ72rR979fRYA65uBUgzENyOu6mbSYQ0_nuzJM6ONI3ERDlZL-V_M2NoRLuucoj3mbRKMvW2n3RMEX_OGAnqLrCSO3GmvXYgLgBR0m41z_dmo9Lxun3QrT1_K5IZ_Sw2C1rmg-QQiOoJx_QWs4cUMGHgQZxP_K0GUU6M-lmm99CXJCIgti5i4c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت دستور رهبر شهید انقلاب به امیرموسوی در روز اول جنگ ۱۲ روزه برای در نظر گرفتن تجمع مردمی عید غدیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/656375" target="_blank">📅 17:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656374">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">در مهمونی کیلومتری غدیر تهران چه گذشت؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/656374" target="_blank">📅 17:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656373">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc5d3e0763.mp4?token=pHb5uN5R77zqnuvhInfhfuqe9MffFQTT9leR1dVmCFSEhuzB4XRBvZIHIf-FXSTvWCideZTMh5thNYQyb4YB10bdcK8_XtkZKI0VLOza-spThgXFBkFGodv9yYq-YilopyhQrtv6dGZ0lFNMdj3TWGY9zz-ufG4NnetI_Nt7fb5KW6h4RWM5dJOJgpOtaXWeL7OLhO-ipeouounMNE1QFjVBXsyHsB-D7jpILjQk-QhrlaBtkeEFScZHps3Fu5eawBv2Y34rf9VvVAWyJxl634th7VXfnjwMIHhNe2HqxX5SpiM2lbxB9vYojEEEnLuDVdcpJT_J6DSi8_1vpt6wSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc5d3e0763.mp4?token=pHb5uN5R77zqnuvhInfhfuqe9MffFQTT9leR1dVmCFSEhuzB4XRBvZIHIf-FXSTvWCideZTMh5thNYQyb4YB10bdcK8_XtkZKI0VLOza-spThgXFBkFGodv9yYq-YilopyhQrtv6dGZ0lFNMdj3TWGY9zz-ufG4NnetI_Nt7fb5KW6h4RWM5dJOJgpOtaXWeL7OLhO-ipeouounMNE1QFjVBXsyHsB-D7jpILjQk-QhrlaBtkeEFScZHps3Fu5eawBv2Y34rf9VvVAWyJxl634th7VXfnjwMIHhNe2HqxX5SpiM2lbxB9vYojEEEnLuDVdcpJT_J6DSi8_1vpt6wSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرد گمشده نپالی پس از مراسم تشییع جنازه‌اش، زنده پیدا شد
🔹
یک راهنمای کوهستانی نپالی که گمان می‌رفت در کوه اورست جان باخته باشد، یک هفته پس از مفقود شدن و پس از آغاز مراسم تشییع جنازه‌اش، در حالی که سینه خیز به سمت کمپ اصلی می‌رفت، زنده پیدا شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/656373" target="_blank">📅 17:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656372">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMQGZfF5ddKm8nDgVr8x_k-pO3HobCw9TgzcYnaK4bqGuKb8kTp_1dztP8_3eTMEMOB9-eKIOVzaQBpDJwi3AS4GLzngLZjNP08u3M2ntGhZ2Rv-yDc6FimLxBwcEWA9jb1-U4TXVRHCxkLvrGowvWGwuIaNdH0p-X25uOxtZcqHusaAGj0XnHDMAVvpAeKc9lcnj2vjCeZUl0OXTeyTxs9YPTUyX9YXnPcxpI-a1gCwEeKUTSPzWJyb7qKVmJ-kwkbcWgVR0X2EfUwnzDTgkzZUtCbVXYOYRqX40UT1JqCxRCTwiSKkWFADNLjRWPeh26dVuateW5dQqO0GYemN5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازداشت مدیر یک شرکت ایرانی حوزه فناوری در آمریکا
🔹
وزارت دادگستری آمریکا خبر داد که مدیرعامل شرکت ایران تک به اتهام تأمین تجهیزات آمریکایی برای تأسیسات هسته‌ای و نظامی ایران دستگیر شد.
🔹
جمشید قمی، ۶۳ ساله، اهل ساحل نیوپرت، به توطئه برای نقض قانون اختیارات…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/656372" target="_blank">📅 17:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656371">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
تکذیب وخامت حال میرحسین موسوی
یکی از نزدیکان خانواده میرحسین موسوی:
🔹
او به‌دلیل سرماخوردگی و با توجه به سابقه آنژیوپلاستی قلب، برای مراقبت بیشتر در بیمارستان بستری شده است.
🔹
به گفته وی، حال موسوی خوب است و خبر وخامت وضعیت او صحت ندارد./ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/656371" target="_blank">📅 17:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656370">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ادعای گروسی: ازسرگیری بازرسی‌ها پیش‌شرط هر توافق است  مدیرکل آژانس بین‌المللی انرژی اتمی به الجزیره:
🔹
بیش از هشت ماه است راستی‌آزمایی موجودی اورانیوم ایران انجام نشده و بازگشت به بازرسی از سایت‌ها شرطی غیرقابل چشم‌پوشی برای هر توافقی است.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/656370" target="_blank">📅 17:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656369">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/656369" target="_blank">📅 17:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656367">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65ef51f223.mp4?token=HbfF2rKs8uPgYcIDUBWbdefzqGozXgtKzPImyjp2YFkgZdS44I6GOgDuneEDH1tBXSWHejol0tQaL8Ub5GJM_ijEr6pECCRqBZxfiaj5VSaJNXle8_D6SOgOvVfa6_UYjlAukmaCtDeFiZ8qJqibOBeYKLh6hNLsQeHZp4YcQg6Q9Dor0EBhoUjoQnP0pgsu4KqvYH7QXTjx2YwYMaeGoVAF9Mq_XclRN9t6p2AO5anjinW2DTmFnpfLFyAZvRX7EzP6zXhqDjZRhv-7Uzh-ytH-UHao-Ni3fQrTBgQkiqpq8ugOLjL8UJiZsZ4YjWi_UxeLQW7WALU0WtphGuv-cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65ef51f223.mp4?token=HbfF2rKs8uPgYcIDUBWbdefzqGozXgtKzPImyjp2YFkgZdS44I6GOgDuneEDH1tBXSWHejol0tQaL8Ub5GJM_ijEr6pECCRqBZxfiaj5VSaJNXle8_D6SOgOvVfa6_UYjlAukmaCtDeFiZ8qJqibOBeYKLh6hNLsQeHZp4YcQg6Q9Dor0EBhoUjoQnP0pgsu4KqvYH7QXTjx2YwYMaeGoVAF9Mq_XclRN9t6p2AO5anjinW2DTmFnpfLFyAZvRX7EzP6zXhqDjZRhv-7Uzh-ytH-UHao-Ni3fQrTBgQkiqpq8ugOLjL8UJiZsZ4YjWi_UxeLQW7WALU0WtphGuv-cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
من به عشق حضرت علی(ع)...
🔹
در روز عید غدیر خم، از مردم خواستیم جمله «من به عشق علی(ع)...» را کامل کنند. آنچه شنیدیم، جلوه‌هایی از مهرورزی، خدمت به مردم، یاری نیازمندان و عمل به سیره نورانی امیرالمؤمنین(ع) بود.
#فقط_به_عشق_علی
#LiveLikeAli
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/656367" target="_blank">📅 17:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656366">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84be7c8b93.mp4?token=gh3CoqptQEf5pxi6LyLM838CrYveXf1EBaYBoF_P-gR3SFngDqHdMxgYp4RQ8GQYSvvVt9Lp6tZvL2QRKC-fvjFUdZD0Ls7SB4H4Da-97KlGNneKf4-6-LhmasOLgU4K_6EBKjpYgT3z7GbKMYg1jGzsEi7NVa5BPMufRJjohzMVzzOrouTTbMlNRcG3AgsZwM9s5SKBDfPEq_AixQpUXR_G8JwOTnN8qo7gBEsiCzNtypAkRoAfrnzWIFt-1hzZ8uA5gVoEigqLwrgjIyTXSZhML4bRRuU1IfxfV2KyG6ZHSI-v2324E4b_5Zofo4R6AX8Y5KIxdRVk-sFFfpyO3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84be7c8b93.mp4?token=gh3CoqptQEf5pxi6LyLM838CrYveXf1EBaYBoF_P-gR3SFngDqHdMxgYp4RQ8GQYSvvVt9Lp6tZvL2QRKC-fvjFUdZD0Ls7SB4H4Da-97KlGNneKf4-6-LhmasOLgU4K_6EBKjpYgT3z7GbKMYg1jGzsEi7NVa5BPMufRJjohzMVzzOrouTTbMlNRcG3AgsZwM9s5SKBDfPEq_AixQpUXR_G8JwOTnN8qo7gBEsiCzNtypAkRoAfrnzWIFt-1hzZ8uA5gVoEigqLwrgjIyTXSZhML4bRRuU1IfxfV2KyG6ZHSI-v2324E4b_5Zofo4R6AX8Y5KIxdRVk-sFFfpyO3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آلبانی علیه داماد ترامپ؛ معترضین البانیایی: پروژه لوکس کوشنر را متوقف کنید
🔹
در ادامه اعتراضات مردمی در آلبانی علیه «جارد کوشنر» داماد ترامپ که در حال ساخت استراحتگاه مجلل در خاک این کشور اروپایی است، مردم دست به تظاهرات زدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/656366" target="_blank">📅 17:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656365">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
ادعای گروسی: ازسرگیری بازرسی‌ها پیش‌شرط هر توافق است
مدیرکل آژانس بین‌المللی انرژی اتمی به الجزیره:
🔹
بیش از هشت ماه است راستی‌آزمایی موجودی اورانیوم ایران انجام نشده و بازگشت به بازرسی از سایت‌ها شرطی غیرقابل چشم‌پوشی برای هر توافقی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/656365" target="_blank">📅 17:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656364">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d40dbeba5.mp4?token=VG7z6Hs7OvZtjBdVZyxhUbYjttpwQRMQaXrTcgupwZRsYaoafDsXo2yJnVS_V7Bsyc8qnbOoeroJyWfU5jv1uGWkWPqNi9CZSqB-oApEDU9nSHosWCHlNagoergRR35Iw3iZ7CicSiHZD7XGyt-S-K_WtNDSC2J-Y7T30yNum0J0KxpsIZFWARmxgW9-Ar02ZCR3qjHfPcFiNQXHe5qB8qpGvhpsXEHx72fHwAWzT2aXv60Sm6HbsacsUXNTh3ImS5jR5Pdl6rxdD-fN_4ddf7UQDU79wRYqeue47ABUPznr-yOmB_rHiHhv8ZOQr46qOCuz9J69xtQoEfS0vSHdmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d40dbeba5.mp4?token=VG7z6Hs7OvZtjBdVZyxhUbYjttpwQRMQaXrTcgupwZRsYaoafDsXo2yJnVS_V7Bsyc8qnbOoeroJyWfU5jv1uGWkWPqNi9CZSqB-oApEDU9nSHosWCHlNagoergRR35Iw3iZ7CicSiHZD7XGyt-S-K_WtNDSC2J-Y7T30yNum0J0KxpsIZFWARmxgW9-Ar02ZCR3qjHfPcFiNQXHe5qB8qpGvhpsXEHx72fHwAWzT2aXv60Sm6HbsacsUXNTh3ImS5jR5Pdl6rxdD-fN_4ddf7UQDU79wRYqeue47ABUPznr-yOmB_rHiHhv8ZOQr46qOCuz9J69xtQoEfS0vSHdmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نصب کتیبه‌های ولادت امام موسی‌ الکاظم(ع) در حرم رضوی
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/656364" target="_blank">📅 16:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656363">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42cc35c7d4.mp4?token=lb4WhuV4vVEllZXuqYFZD3UsrIdmoo6WKU7DW-kvEfky_2p-tMXdAsQ9uWQFRcjIA147zsTPPEzsPHUF9UX6SwJx2HPh-PHDUUXbe2sOPRdlIiAq3lC2L1UkF_3O2q3Z3s1PPmLNWVDIPR23F4NQ86fkVPsuE5kn4EcP_LZ217Zz4Pau4VegkHdbXPqwJMPo5jx01oJVPCynfT1PvuwzY0eaoPts9QlCBrqZPBsc_7nuV75fC0QsYzWY_wptKwd23BoVbGz1QvuLZDZDS1dNKdhM0DZt1nAsxOQMza6kJ8DbC2KxkDtVhJ2KMj96YxLTtrBhjlw73WR7oHKb_JRpiykk0-ZVxmN657oqnScfnxqoQ99WAh9nDR4wsB_oBYz6KzbSVYdTO_YeDDPM86lsMq4hnMVXsY-_0NVnVaDDpadhQM9CaDpwPX_JZHft1H4Dcnl6nlrhTyQ0ji33BRIW5GQuXc5SFXtMQ7yM8ysEiNRTcPRVZj_f-B6scrBcq15a_YTbjkfdtO1x4-e0N3i45QF9u4yjcT9QWBX2QByMx7W1CSl5KSiNm6WAH9AIvXhsCAY1lVe20gW0rt-G8m3TwXbHwM4odMeOhryd9Kon2Cne9D25YPftEHxPYqHSyt-3-5J5zExwHjtg3XWCfxJS26PdwFqsbSBLSV1Rc00ctoc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42cc35c7d4.mp4?token=lb4WhuV4vVEllZXuqYFZD3UsrIdmoo6WKU7DW-kvEfky_2p-tMXdAsQ9uWQFRcjIA147zsTPPEzsPHUF9UX6SwJx2HPh-PHDUUXbe2sOPRdlIiAq3lC2L1UkF_3O2q3Z3s1PPmLNWVDIPR23F4NQ86fkVPsuE5kn4EcP_LZ217Zz4Pau4VegkHdbXPqwJMPo5jx01oJVPCynfT1PvuwzY0eaoPts9QlCBrqZPBsc_7nuV75fC0QsYzWY_wptKwd23BoVbGz1QvuLZDZDS1dNKdhM0DZt1nAsxOQMza6kJ8DbC2KxkDtVhJ2KMj96YxLTtrBhjlw73WR7oHKb_JRpiykk0-ZVxmN657oqnScfnxqoQ99WAh9nDR4wsB_oBYz6KzbSVYdTO_YeDDPM86lsMq4hnMVXsY-_0NVnVaDDpadhQM9CaDpwPX_JZHft1H4Dcnl6nlrhTyQ0ji33BRIW5GQuXc5SFXtMQ7yM8ysEiNRTcPRVZj_f-B6scrBcq15a_YTbjkfdtO1x4-e0N3i45QF9u4yjcT9QWBX2QByMx7W1CSl5KSiNm6WAH9AIvXhsCAY1lVe20gW0rt-G8m3TwXbHwM4odMeOhryd9Kon2Cne9D25YPftEHxPYqHSyt-3-5J5zExwHjtg3XWCfxJS26PdwFqsbSBLSV1Rc00ctoc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آمریکا مدعی توقیف ابرنفتکش مرتبط با ایران در اقیانوس هند شد
سنتکام:
🔹
نیروهای آمریکایی در یک عملیات شبانه، کشتی بدون پرچم و تحریم‌شده «داوینا» را در اقیانوس هند توقیف کرده‌اند.
🔹
به‌گفته مقام‌های آمریکایی، این کشتی در اکتبر ۲۰۲۴ به دلیل ارتباطات نفتی با ایران تحریم شده بود؛ «داوینا» یک ابرنفتکش با ظرفیت حمل حدود دو میلیون بشکه نفت‌خام است.
🔹
گزارش‌ها حاکی است این کشتی آخرین بار روز جمعه در سواحل جنوبی سریلانکا مشاهده شده بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/656363" target="_blank">📅 16:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656362">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8363494d27.mp4?token=vR2L17_tcr-0nSvoS8v54_zafRPB37wtECQihbY1N3nOZSpHYtdSgk-AOBUJGICL-QiyfSjGWVJZXmL4jZD1yQ3lV6hO-Hzl_U3ur0tsDQZnvZ831cLlSn_agv0GgwR2qatrMBudIjGMJKg1VCVqrdXLldzhXaqGXaPq89PpJVRx3OPrMoE4dED-OeoGRuL9lqIsUUeU7u6TOxTjt74LWDYfTnqSGlE3txGHRUyevd5zsmv042ic6pRzenNS_Awhv9aE6qqvovujMyozWI-NaDqxn5z7tz2c1T1BzW7wnoTIaFIiQ_QPfIvURqWY2SG_z4qL_wvqpUaVTaB1SP3PIDs460y7PSlzOiAyIomgTGiu5eFlh7F3ghKfndlG_K3jK6bGWDF8n6APwLIH1us-jrYjQk8djTUNI6SPZ8bII30dnbbLxGRftwu96ZSfCgONgQDpHLBvH48DxlS-a7_iz02pZHlAu4qaAh2HCnFG_4oNfrJRlSj2TfTC4HfsBRYjK6jtpaWOeXaKaZzA3VcV8gktz9RPs0je-i04OH6mWwUuHpZfrDgYz5K6ncdX-L52c2JuaQC19ZzcVACO7dXmnhUNMXbOGTZKxpjoQ-bSP-v238XnKrJu41sbOIMk7re7LuwzvK7X3M45G_39KrFST1K--jeoAQAFRgaX2BGfNlM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8363494d27.mp4?token=vR2L17_tcr-0nSvoS8v54_zafRPB37wtECQihbY1N3nOZSpHYtdSgk-AOBUJGICL-QiyfSjGWVJZXmL4jZD1yQ3lV6hO-Hzl_U3ur0tsDQZnvZ831cLlSn_agv0GgwR2qatrMBudIjGMJKg1VCVqrdXLldzhXaqGXaPq89PpJVRx3OPrMoE4dED-OeoGRuL9lqIsUUeU7u6TOxTjt74LWDYfTnqSGlE3txGHRUyevd5zsmv042ic6pRzenNS_Awhv9aE6qqvovujMyozWI-NaDqxn5z7tz2c1T1BzW7wnoTIaFIiQ_QPfIvURqWY2SG_z4qL_wvqpUaVTaB1SP3PIDs460y7PSlzOiAyIomgTGiu5eFlh7F3ghKfndlG_K3jK6bGWDF8n6APwLIH1us-jrYjQk8djTUNI6SPZ8bII30dnbbLxGRftwu96ZSfCgONgQDpHLBvH48DxlS-a7_iz02pZHlAu4qaAh2HCnFG_4oNfrJRlSj2TfTC4HfsBRYjK6jtpaWOeXaKaZzA3VcV8gktz9RPs0je-i04OH6mWwUuHpZfrDgYz5K6ncdX-L52c2JuaQC19ZzcVACO7dXmnhUNMXbOGTZKxpjoQ-bSP-v238XnKrJu41sbOIMk7re7LuwzvK7X3M45G_39KrFST1K--jeoAQAFRgaX2BGfNlM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظاتی کمتر دیده شده از حضور سال ۱۳۹۶ رهبر شهید انقلاب در منطقه زلزله‌زده سرپل ذهاب
🔹
همراهی حضرت آیت‌الله سیدمجتبی خامنه‌ای با رهبر شهید انقلاب در بازدید از وضعیت مردم زلزله‌زده کرمانشاه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/656362" target="_blank">📅 16:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656356">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TI8u5FBmIMbHyADbiYyRQ4h5RvPG8FJ2XtlvdTPf6CSllfv-BPd55tKj36BoK-f_hGlIoRt1tXceM5-8sKIpoAvkoO3EF7Xr874ULrG-LtT1QVV8hAYRhsNWryxzDz8txplkqu-K_vEwlWT8WRdq_MRIgzpu3ZSWGXeZB4iaPcDQMjgoGP7eTipgwtOgQvOORv_sjRrehNQpB1ohGvnSVf5bAsTh4LSInAM2OTnFSAtlBjGjRIfF6zJhTCAuHXocE0NAonZXiLRnAQPgU0ROGI6sP28-ro_0JZZSU1COZDonRXQvun6ptTBY8LtRzd4Q7egESAc_nGokNAzB5x7EQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شانس ۱۱ درصدی ایران برای صعود از گروه G جام‌جهانی
🔹
براساس پیش‌بینی‌های پلی‌مارکت شانس ایران برای صعود از گروه، ۱۱ درصد عنوان شده است. بلژیک در گروه ایران با ۶۷ درصد بیشترین بخت را برای صعود از گروه دارد.
🔹
مصر ۸ درصد بیشتر از ایران شانس دارد و نیوزلند با ۳ درصد کمترین شانس صعود را دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/656356" target="_blank">📅 16:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656355">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfRIVlefqVlQ7BffHfJSNIBTb4rPY92HBZ9VLcJPtrXduUXB6djLmfSHzlC4mkDmQN02t8xwNqACz7oTPGo3Ivm6UjjBIIUlmWrBeKI295Kid-JQ-TiMlSVqd_V1qXn9W5H3vqGmNhwhlHh4HwP8Oru51S0y4sPq0ePCn3rdFcAFFdOlA7hsjW1KxVwrexKvEDvLiJwg5-hs_5mq3zTsv5bSV8Z3X5XBX_1vIwPxqlTqSf7cN6_4tPkWrkBDJFHtY_F4IA7yxyXudfYC3KiM2v8Bgzmlfjhe6GlhltxDcQOXfwwHjwICzgL2tgphfYLOQxnDEBsIzrrG8vgnKmFuuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
«تنها مذاکره‌کننده»
🔹
جلدِ ویژهٔ «الأخبار»، روزنامهٔ نزدیک به جریان مقاومت لبنان، در واکنش به تحولات این روزها و عطشِ دولتِ این کشور برای مذاکره مستقیم با سران رژیم اسرائیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/656355" target="_blank">📅 16:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656354">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2Qnsd5I4NE0IyGIC2LxA88ErgOCUJE8eaIGYv0mAu-pRSfq8LUuPI_t4ib7J_5WtfJjBgADuQzs72-iI0ci7hDe0Fxfke0_mkfcvcoqviMcJVNkhMiom0B4CkYBlbo5pmAjFiphaUl2lGG9gUuN1PCH85ThEiOxNFjy0SQonCVnAbfmXobiIPZdy2OKwUlmR63YS64pMFfdxxW8PUUIph_Gf6dbmDXNkvvNm_yD8HCjwgJtYKf5NeDxodD1yJGqCGVwP0krzDI1Ljfmr-SdXSSy_0UsApbCi4jSpnt-KkkZJKUUMnf0XRvSzRJS3h0U8d73t7zdNsnYJA9zwDZL_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاپ لئو برای نخستین‌بار یک زن غیرروحانی را به مقام ارشد واتیکان منصوب کرد
🔹
ماریا مونتسرات آلوارادو، که هم‌اکنون ریاست رسانه کاتولیک مستقر در ایالات متحده با نام «اخبار ای‌دبلیوتی‌ان» را بر عهده دارد، هدایت بخش قدرتمند ارتباطات واتیکان را بر عهده خواهد گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/656354" target="_blank">📅 16:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656351">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fec0af58a4.mp4?token=pmuJsN7HBQM0i7ZxqH9ubd83OG7l4yyRjcH_K-L5_GeOa_5jVhV3hTr-1646u7PmPNlGHukzwkGjNOZsiaWpm7RySvPPT_7zvqCeaSahoCjgaR1VYyyEcyvUOWCfvRJzg8i1czkOEOVb88QpM1PawH60CWYxGCrKKWqBhWwQM-eaKVTxfTd30xo8jacOoMVsrCK56GeJUzn4NKSf1PzAKiXq5Mv7wnCrEEyrKpvWHSvum52RlWEVSfnsLfiKvEc29ybDhY9n_tLUJkZWCwQQd7jWO6Fa18RmrFcpAG0ct3C6I6ZjmWxFWNO89pyWLFehANDyetp9E8Lw6lHB5ZvcmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fec0af58a4.mp4?token=pmuJsN7HBQM0i7ZxqH9ubd83OG7l4yyRjcH_K-L5_GeOa_5jVhV3hTr-1646u7PmPNlGHukzwkGjNOZsiaWpm7RySvPPT_7zvqCeaSahoCjgaR1VYyyEcyvUOWCfvRJzg8i1czkOEOVb88QpM1PawH60CWYxGCrKKWqBhWwQM-eaKVTxfTd30xo8jacOoMVsrCK56GeJUzn4NKSf1PzAKiXq5Mv7wnCrEEyrKpvWHSvum52RlWEVSfnsLfiKvEc29ybDhY9n_tLUJkZWCwQQd7jWO6Fa18RmrFcpAG0ct3C6I6ZjmWxFWNO89pyWLFehANDyetp9E8Lw6lHB5ZvcmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بمباران مناطق جنوبی لبنان توسط جنگنده‌های اسرائیلی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/656351" target="_blank">📅 16:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656349">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
تیزر قسمت هفتم از فصل چهارم
🔹
در این قسمت روایت تجربه نزدیک به مرگ آقای حمید علیزاده را که در تصادف شدید روح از بدن جدا شده و از فرشتگان طلب ملاقات با خداوند را می‌کند و با واقعی‌ترین غم روبه‌رو می شود را با هم نظاره می‌کنیم
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: حمید علیزاده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/656349" target="_blank">📅 16:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656348">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
کلاس‌های دانشگاه شریف از روز شنبه ۲۳ خرداد حضوری شد
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/656348" target="_blank">📅 15:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656347">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97ce25261d.mp4?token=K2kEeAtbT6pVnaqJEOBPSDm56rKP8SZ6jNg-CXGXjxQjpZajYtI-Lt-hJ-12B6YOl2ezGuHECU7Ex8598Qw2Isvz1-3IWVOD6NB2xyw7Yvwc-Uxm3zZcEcDqZ3HywYhWjVRtbqCuRb_ky5aNdzvXlmzflx80W-pz-aGwxN4GnN9gpwShL6ixRxkxNG31OpBl6N0PpcaMshzzJwx7_33S4dAI-Lvl9n2kCOHBwIr_KMhex3J7DaonhspyZZdcuB-M9yp8XJX15pXudmd5LonsYQrF0uKPv9fXh3zYiA-jt7uDpnh6WKwy7lnvev8WC91gNQmy9_cwlbLj9HQYltKRUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97ce25261d.mp4?token=K2kEeAtbT6pVnaqJEOBPSDm56rKP8SZ6jNg-CXGXjxQjpZajYtI-Lt-hJ-12B6YOl2ezGuHECU7Ex8598Qw2Isvz1-3IWVOD6NB2xyw7Yvwc-Uxm3zZcEcDqZ3HywYhWjVRtbqCuRb_ky5aNdzvXlmzflx80W-pz-aGwxN4GnN9gpwShL6ixRxkxNG31OpBl6N0PpcaMshzzJwx7_33S4dAI-Lvl9n2kCOHBwIr_KMhex3J7DaonhspyZZdcuB-M9yp8XJX15pXudmd5LonsYQrF0uKPv9fXh3zYiA-jt7uDpnh6WKwy7lnvev8WC91gNQmy9_cwlbLj9HQYltKRUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصفهان نصف جهان
😍
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/656347" target="_blank">📅 15:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656346">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/craFPWjX2g3ojJ5Hp8zaysB6YC7p6prHsgozQYIUMDsUULDoUZ_8YSSmI-cxX2WNrRjOAvyAepvj0eii1J1L4wuTdvbFP8K37Z0GOrogAtEOYykT4cC0MZqASzBFrIRLxSIRD3nZb7m9vOHF6XqmrxpbYc751GQcgGTmGmhK3z6xz__JxRojUWohtRT1Or_QXpk6qESkt-JtltipRNma3A6O1DnmOTLy2u80c7YDicbD0iO8bJjeQfwPVzBUqhWtLR8bz-1h-5hsYOpy_SgfSp6AtRORKE2cIuF92mlRHA5KdlejnGL3BZaI6Nz3HlZvt-H7pOm_qPDZBobXCo1zAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از هر ۱۰ آمریکایی ۷ نفر می‌خواهند جنگ با ایران سریع تمام شود
هیل:
🔹
در نظرسنجی اکونومیست/یوگاو، ۶۸ درصد از پاسخ‌دهندگان گفتند که معتقدند که آمریکا «باید برای پایان دادن به جنگ با ایران هر چه سریع‌تر به توافق برسد»، در حالی که ۱۱ درصد با این نظر مخالف بودند. ۲۱ درصد هم در مورد رسیدن به توافق مطمئن نبودند./  خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/656346" target="_blank">📅 15:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656343">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNWMu--i7EdkfMZmh15pDzCwWqnI__yTlkaRW4NSoum3uVTJE8YBxPa0ep1m90uTveHmVX9cjRyhfdw5P3Hh8ezwDuW3Gguoy4fMHI37W0fF1_pZxGjOnckxuCucs8L1LqPHGYDpep8vLLB0DqEjhIPleZwEiTrZ8J8RmFdDAf2oQYXBH6kuM9C32bW7yDXKhMKTSZobbn1DMi4Frr_aL3ZJu2r-ISGu0U4lkety2RyFwGtwaEq9C6b7TT6OYO6CRtim_s2IYHXi9cLpNvQzp2fCEnzHHrBYekIWMJw7RJV203K5Oet1cFwBxKLc7SR5BxWhopTRa5OQBXb3JneHAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قابلیت جدید گوگل برای چهره‌های معروف و رسانه‌ها: ساخت پروفایل اختصاصی در موتور جستجو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/656343" target="_blank">📅 15:24 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
