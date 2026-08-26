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
<img src="https://cdn4.telesco.pe/file/HbiJPHgh8EgU2Zts0MgY4Am5A4q2lA3Bo66oN18MP6dvk6RjduTNDr4x1JVFL6jbjjY92M5zZAzlPDhzZdjCKN4mxButPQ97NweqytTZiIH6C2Vkv-WYROn_yRjkup8zVODlJfnRtfupnD2jRxExyweSO7DqxfHxphjd5t3Crn2mlrg7hUc8a1UuEy4WgiyO0DAn6SrBtujUiBlP1zRRCdHr9Eq377-2YEpqITXeSWhhR5S-LNUbNnjglzsZ3c8TMqijdVPw-M39Rsszel7u48d1WhJdiA6q4Iv79LktDSwrvILR0F2R9khLTrR-UAEaqSmhYBg5YS0Dpdc3Yd-j5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 976K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 23:53:56</div>
<hr>

<div class="tg-post" id="msg-143979">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
فایننشال تایمز: اگر فشار های اقتصادی تاثیری بر مواضع ایران نداشته باشد، آمریکا حمله نظامی گسترده خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/alonews/143979" target="_blank">📅 23:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143978">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">💢
این تحلیلگره از تو کارگزاری پشت پرده طلا رو دراورده
منم پی‌وی تلگرامشو پیدا کردم بهش پیام بدید
براش بنویسید«
طلا
»
دو تا نقطه ورود میده همینارو بگیرید …
سیگنال هاش رانتی هستند عموماً
👇
@mahanmazandarani_pv</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/alonews/143978" target="_blank">📅 23:48 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143977">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fW5JRc8-VMtffQl0mTWrgHVmbEqVSOTCr-wbqA-C4KxiU5sP9vK23YtjyWIAcsZk_bsJ3WWV6AQEgszo6gX1u7GMmsmbKJHFfnDzKnPv_VN8VfbgzR5DBA14CapI4B5a9jk_DGrZgIsMY2hWXbKWcHd_J_IHaL4zh2aiY7clCP0lNEHI_IjHgyvDpgsMn2wSEJeyfJfuSZ6xN5pMoo_wdnj8n62YpunLPx7l3BCS3M_dYrQORFnuXgl62SSd5VwbuWStqWDrxC2GsI08dT6V6bcoXhz81enlmUZhURZwMrlmWbfbamUAHhQjOpYNXfBJxxd0Fy5hamWYOt3iMvRAdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سیسی ، رئیس جمهور مصر : نیروهای مسلح مصر برای مقابله با هر تهدید خارجی آماده هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/alonews/143977" target="_blank">📅 23:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143976">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
صداوسیما: صف‌های طولانی بنزین بخاطر شایعات کمبود بنزین و افزایش قیمت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/143976" target="_blank">📅 23:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143975">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
رئیس سازمان انرژی اتمی: ایران در جمع کشورهای دارنده سامانه گداخت هسته‌ای است و اکنون از مرحله اثبات فناوری عبور کرده و وارد مرحله ساخت سامانه و قابلیت‌‌سازی شده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/143975" target="_blank">📅 23:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143974">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
بلومبرگ: متحدان آمریکا به‌طور خصوصی هشدار می‌دهند که احتمالاً هنوز مین‌های ایرانی در تنگه هرمز وجود دارد؛ موضوعی که ادعای دونالد ترامپ، رئیس‌جمهور آمریکا، مبنی بر اینکه نیروی دریایی آمریکا آبراه را به‌طور کامل پاکسازی کرده است، زیر سؤال می‌برد
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/143974" target="_blank">📅 23:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143973">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
پمپ بنزین‌های تهران وحشتناک شلوغه
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/143973" target="_blank">📅 23:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143972">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmrbQr9uvKUWhmQShFKYflkAMXADx9159OHTXzn9ckSp93RkLLFy0kiGaQikvGEfOqQE0mma4o-NBWgvjOt00uVG796BlVNX_zia_-KlsQXk0O3uP-RdaVr6okEbpu6yc25cpmUFWqU7jCLGxnsIcwa5SDti4CqOGW3xIhjacy_VvNV_FYJKY1z3Q49FLODL5HKJdWWz8r4vtK5-mmkIjWyesWJLdKKeoAcrDlY2nbeSVZjhkI3BFGrli6Cpt3Pdhk7mQSf6VXCKzR85au16Dbe-FBBYC_zZSpnkWmULNwZhD-7LX1s0EqJrctUqxuhWobCW2lU5X5fGQFb5D6Jtjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زهرا پزشکیان، دختر رئیس جمهور، در پیامی به همسر رئیس جمهور آذربایجان، تولد او را تبریک گفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/143972" target="_blank">📅 23:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143971">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFhsjBafuUGQYlahD62GmOw32UPnC6-VI9KnUBk8Vxriv4UqfhJ34RHXMl_XnfCazWsdHRBpS7aoAzk_6mn4A72YA0pxWZ-tKlbfDBWKuoOJPQvAN65qkXS1000J-hZe7EnUpZaKidpJctdevjojVVFeAejcG5hZld5wZZtDbxPUvA9l-1SMmyvShlj_79ug7uHl87QMKNWN2n7b7txhaHnLdBOby4IuUkyAVyjbeT8h9bBW3z2NApI4EIvpFPmO35CeeF0SxFRoxjyOqAs59alnXbX0LlRe7t0cASnx1cyqjj0-Z8ZwuXfKfQVg0RfFB7EVG8xGHwoxp9Gox9CEvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه ایران:
آمریکا، ناو هواپیمابر «یواس‌اس آبراهام لینکلن» را برای نمایش قدرت به منطقه اعزام کرد؛ اما پس از ماه‌ها جنگ و بیش از ۲۰۰ روز بدون توقف در هیچ بندر، اکنون این ناو برای استراحت و تفریح خدمه، راهی تایلند شده است.
🔴
ماموریت: نمایش قدرت.
🔴
ماموریت فعلی: نمایش تعطیلات.
🔴
«من خسته‌ام، رئیس.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/143971" target="_blank">📅 23:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143970">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m8gWztXX-uLNI8tTWX16vYIXioA6lGgRghK8VS5qolVAQv4IJlJ_U6nHd80rVozB4h3LYDryfqu3FJPpZtoGXUmEJOXUtw2aGDWbxWZmpaYkCleE0h7EiG5UxdG90RKpiXoLLv5RYwjN4vCETGQTZTTbt-ejCz2Z9Yr9TV43EN1njvC-THzC1yPJmeiU9YIBrbQMz7CgOx37weL8Lcdxl5HizgrVt1UYJbffmssI_WkvPFsgUwtFgq-HTxyGVdxGha-5hGG9PcZn9fh6ba_JzeDdAweG9FEiyA9zbPM6npbXmjNlOx5fgGIEyoqv-mwbcB3MsPGDQJTx0frYyng_2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید علی کریمی خطاب به شاهزاده رضا پهلوی و تشبیه وی به قورباغه
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/143970" target="_blank">📅 23:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143969">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
قائم‌پناه: توزیع بنزین در کشور عادلانه نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/143969" target="_blank">📅 22:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143968">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 250 میلیون
‼️
🔴
دلار به زودی 210 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/143968" target="_blank">📅 22:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143966">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WHKT5ULV6Wa_ejiGNnSqpnXqCaRyPwUK7LNG-WblaiVYx_wy0b7K9u1IKn4fcyNC9VZ-WNm-RTHMQjVAAgavyavhy-0IP_vVcPuDe-tkYNcp3q9ldfM4jaaqheJWnQ7YT_vuTz8QG4qPUNqJbZQG5p_VwtTqpykyNr2ZKjcWcbQjwAUdl3u5WdLrD68CRLUqZoSpJtx-dx94k-7Y2kmvcL4izfS-JNqrezft1IfQ4fXAQibfap54y32p_1c5zIqQN7Rvzw-4uHbHCak6W86zQQK7MXBrA6q72A--JNN2yhofIiHcSl551-jQfZ5sM3ZX4riJgHpRWW3bWlT1zg3PZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oe0BT7nhbt5YT_Vilvnc6C31xCj6LJZV9KXAOGpN7KnkUsK8SettznqY6_1p33OYsmYF7pkYfsU2gusQVc9F1Shs0ftcelemtCYqV-VS0nfKE7m1mDvtb9MhGbVQlGAYUdSz_AGWMX3Hck8feoeKu3dlp01nUjAXKDLnEZP4JfvAux-iA3IHWzjO32SWuIJQYaaTJ0F_g4Lbpa-MCGrReTDz-8uPb2WEFzb-zzvYLRNMzRyKVTySMzLFbVuttFPIf20P1YAmyIl8WUS5dd5N7kvRLpq9U3G3baJzBZQ1SrraDxmtyHvEFksLhjK9ACwjW4NSDxTRaM0ROPDR05JCLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ناو هواپیمابر USS Abraham Lincoln قراره در شرق تایلند پهلو بگیرد تا خدمه ناو استراحت کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/143966" target="_blank">📅 22:51 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143965">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
جان رتکلیف، مدیر سازمان CIA پس از بازگشت از روسیه به کاخ سفید رفت و با مقامات دیدار کرد
🔴
در این جلسه، پیتر هگست، وزیر جنگ، و دن کین، رئیس ستاد مشترک نیروهای مسلح، نیز حضور داشتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/143965" target="_blank">📅 22:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143964">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
به گزارش بلومبرگ، احتمال دارد پوتین اوکراین را با سلاح «هسته‌ای» مورد حمله قرار دهد: به گفته این خبرگزاری، تعداد فزاینده‌ای از مقامات روسی به این نتیجه رسیده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/143964" target="_blank">📅 22:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143963">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: نخست‌وزیر و وزیر خارجه قطر در دیدار با مقام‌های کشورمان در روز پنج‌شنبه، درباره ادامه تلاش‌ها و ابتکارات میانجی‌گرایانه قطر و دیگر تحولات منطقه بحث و تبادل نظر خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/143963" target="_blank">📅 22:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143962">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: خواهان پایان دادن به برنامه هسته‌ای ایران از طریق مذاکرات و بازرسی‌های آژانس بین‌المللی انرژی اتمی هستیم
🔴
هدف ما این است که ایران از طریق مذاکرات، بازرسی‌ها یا استفاده از زور، تسلیحات هسته‌ای نداشته باشد.
🔴
ما نمی‌توانیم به ایران اجازه دهیم تا ابد امنیت عرضه انرژی جهان را تهدید کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/143962" target="_blank">📅 22:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143961">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
گزارش‌هایی از حملات هوایی اسرائیل به منطقه سِروبین در جنوب لبنان منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/143961" target="_blank">📅 22:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143960">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزارت خارجه قطر: وزیر خارجه فردا در تهران با شماری از مسئولان ایرانی دیدار خواهد کرد.
🔴
وزیر خارجه در تهران درباره کاهش تنش و فراهم کردن شرایط برای گفت‌وگو رایزنی خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/143960" target="_blank">📅 21:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143959">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzjOIy8U5HBmoxS0JVF6We61w0eqSFvTWNuO4Zc_x8xf8wDLxCfPRaU_wZib8Df1tU8G91KnMdeSARRlGROSzxN-3DkHri7NqpEfCErJNZn2oVMKW-zCcTJJ4kXpHDerDS0qDtSbN7KqsELd51a4eIzFpF4xo07aNo2DpR73sJGq9T3xG-zfG7XyPXtqhzg5W1--Ju9R_6Ui9-jDRo2O52p0BYO4lPj2kW0KHHkoBt0Vte5TJCEfBubT_W4mGqYtB400XtUmR0g4tAGYV3FK04ve2RO1eNk64bTtP2V51OYmMU-J9hMSuCKtzdpR31g4PSP9TUrsE6e18EJp5F1BgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش تورم مرداد به ۸۴.۴ درصد
‏
🔴
بانک مرکزی: شاخص تورم نقطه به نقطه در مرداد ۱۴۰۵ به ۸۴.۴ درصد رسید.
‏
🔴
این شاخص در ماه گذشته ۸۳.۹ درصد، و در مرداد سال گذشته ۴۱ درصد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/143959" target="_blank">📅 21:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143958">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZTl_ogeXRMYYevyApIw-7zIOY6FRB4SEPQ4MeoKggGZHK3bP4qLrdCmVx5n4U-vKnuTzs-9_yKkE9yB6oKjppvSEUuXMo39AotErWQBMS-oS6qgceN6cBFcL6AZpmFPkiiV8Bg5A3Y3yatk4LGqi_ClmZJY42t6tZv1ZYvDU4qZlNJKjorP5mK0pPLJ6NotZTPzTe2wLZpEhy9hw05aUkIxb0b0M1aLqGNWSovbkrhJHNhzQd7PcjjaqBopNv64z3_uA0Bo2cxhV6H4KK23VaJwPIIxghd3TNV60MVO3Xz4E97NSeG4mnU0kn3EtX2ns-_T5k5zLY0fHMRaL8VrGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: رابطهٔ راهبردی ایران و چین به اجازه هیچکس نیازی ندارد
🔴
از موضع اصولی چین علیه تحریم‌ های غیرقانونی آمریکا استقبال می‌کنیم
🔴
نماینده ویژه ایران در امور چین: ما از موضع اصولی چین در ردّ تحریم‌های غیرقانونی علیه ایران استقبال می‌کنیم.
🔴
شراکت راهبردی جامع ایران و چین بر پایهٔ احترام متقابل، همکاری برد-برد، و چشم‌اندازی مشترک برای جهانی چندقطبی استوار است. رابطهٔ این دو کشور نیازی به اجازهٔ هیچ‌کس ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/143958" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143957">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
سیلاب در نپال حدود ۸۰۰ مفقود و بیش از ۱۰۰ کشته برجای گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/143957" target="_blank">📅 21:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143956">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlq3vI9DWHPNV6LCaYvQtAnxKCgWm-smU6GMWUb3FgIJZrANGDDk-U13kyn-SAdebCBKOdlkLIfhARfJRidHuDG9FcdsRHp1-GQbmAL8VITmumDPq2T8Z3ars0DabIYMpx4bkbROMpPAAJC2oblbUv_vE5BhHm3H-kxcMwNWgrJVNYV04-xMV3A8NdGe0XzZt0WjjI5KYwuUBmcW0_F2JR5Vfq4aITwAuR-6iTK_TB3XS1-GHRVGUaE9nN2FsBxRkIH-RoJBPo8NkjOVRbBLX3c8GxM23rW59kdGfIbF9ITVgBNadM5x6dHKjTXWng24jhgnLNNHhfYJbw7AxM85bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار سفیر پاکستان در تهران با ظریف
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/143956" target="_blank">📅 21:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143955">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
عراقچی: ما از شورای امنیت می‌خواهیم که از استفاده واشنگتن از اقدامات اجباری و تحریم‌ها برای مجبور کردن کشورها به تغییر منافع اقتصادی‌شان، خودداری کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/143955" target="_blank">📅 21:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143954">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
بانک مرکزی: تورم مرداد ماه نسبت به تیرماه فقط یک دهم درصد افزایش داشته و به ۳‌.۷ درصد رسیده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/143954" target="_blank">📅 21:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143953">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
خبر بزرگ پزشکی؛ آمریکا درمان جدیدی برای یکی از مرگبارترین سرطان‌ها تأیید کرد!
🔴
سازمان غذا و داروی آمریکا (FDA) یک درمان جدید برای سرطان پیشرفته لوزالمعده را تایید کرد؛ بیماری‌ای که سال‌ها یکی از سخت‌ترین سرطان‌ها برای درمان بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/143953" target="_blank">📅 21:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143952">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDPL-VWMex7huVS2hPHddm5PxTJOwgBtRplpj8hBceHV65sVlzv3JOkBp-IQKi1kfTJ-B0kLMGqyzySUJ18BVx_K_LnnhtgK4vTNp1wwBs7AgGZXIuUMYKjbBe7hS3oqltRnuEpmMb1PQoSSqv55Elfmi3T-9WvmyCxiUBIjhMXQfCJ9Dv55ssMMJ_FGWp7XO7TaOG2QKbxFU8F93Rw9YfqQT245UpYBfnjch6jYxVeuKVjEDM7IMPaaHZ_bZvKFqLmGCBmm9IHNDgatv9f3Eanhu_NTPTqLBHdgl_gOcmtsYR-9OhLHddVlUObg2AgCP_gudAGQYlBEQENubUYFJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه 14 اسرائیل:
مجتبی خامنه‌ای یا مرده یا مرگ مغزی شده و از اول ماه دیگه هیچ خبری ازش نیست؛
چند ماهه که اصلاً دیده نشده، حتی تو مراسم یادبود پدرش هم نبوده و فقط چند نفر محدود ادعا می‌کنن دیدنش.
الان عملاً سپاه و بقیه دارن کشور رو می‌چرخونن و یه خلأ قدرت خطرناک ایجاد شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143952" target="_blank">📅 21:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143951">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
کارشناس صدا و سیما: در حالی که ما به علت محاصره نمی‌توانیم نفت صادر کنیم، کشورهای منطقه روزانه ۷ میلیون بشکه نفت از خلیج فارس صادر می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143951" target="_blank">📅 20:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143950">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c4082c1b5.mp4?token=l0r64hTozxZIxRC-QDot3cn5hI56VP27-vAG5QitZtbs-mvkJ5yeqga_7r1n0JQ3Ly7U8ABRpHHZdaDQ57N2lGr6QMjL899RwK6Z-95OnsE1VVNCFop6mxJHucLdXzo3OppPt30miCK6xZLySqwA-DTWoD9Ou-DGhwclocAB9mJfwFIJOOWzrA3ea-pCdw-72jxHOCMTEx7EvhT135xVQeiIToKatXCQi8zODeBBVCjnI4dCfmev6_5aEg3l61fbooDXrByVTocX7Enz-UWrhV3no-1KAWurzI4qWrxlZPjsJuyzfOgCBcRuo3XSSWGzvmJnWBehhO-hBl3fH-qjdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c4082c1b5.mp4?token=l0r64hTozxZIxRC-QDot3cn5hI56VP27-vAG5QitZtbs-mvkJ5yeqga_7r1n0JQ3Ly7U8ABRpHHZdaDQ57N2lGr6QMjL899RwK6Z-95OnsE1VVNCFop6mxJHucLdXzo3OppPt30miCK6xZLySqwA-DTWoD9Ou-DGhwclocAB9mJfwFIJOOWzrA3ea-pCdw-72jxHOCMTEx7EvhT135xVQeiIToKatXCQi8zODeBBVCjnI4dCfmev6_5aEg3l61fbooDXrByVTocX7Enz-UWrhV3no-1KAWurzI4qWrxlZPjsJuyzfOgCBcRuo3XSSWGzvmJnWBehhO-hBl3fH-qjdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عارف: آمریکا به امضای رئیس‌جمهورش احترام بگذارد؛ راهبرد ما جنگ نیست، اما خوب دفاع می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/alonews/143950" target="_blank">📅 20:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143949">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
گزارش فایننشال‌تایمز در مورد کارزار تازه واشنگتن برای تشدید فشار مالی و تجاری علیه ایران: پکن که تا ۹۰ درصد نفت صادراتی ایران را خریداری می‌کند، روز سه‌شنبه به آمریکا هشدار داد درصورتی‌که شرکت‌های چینی به دلیل تجارت با ایران هدف تحریم‌های ثانویه قرار گیرند، دست به اقدام متقابل خواهد زد.
🔴
این تهدید برای واشنگتن اهمیت زیادی دارد؛ زیرا هرگونه افزایش چشمگیر تحریم‌های آمریکا علیه شرکت‌های چینی می‌تواند مذاکرات حساس تجاری میان واشنگتن و پکن را تحت تأثیر قرار دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/143949" target="_blank">📅 20:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143948">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
سی‌ان‌ان: قیمت نفت برای سومین روز متوالی با افزایش امیدها به توافق ایران و عمان برای ایجاد مسیر جدید در تنگه هرمز کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/143948" target="_blank">📅 20:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143947">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfO1-ZEgJXC-22LODIpKhhbjZlWiuKdFLMNNk2tMQqmIfWU3X48gVZo7LRrBa4K-sL1FqauKasNYygPIA_ev5lQ_cD3eAOhfJG-PHNzgReM_EXmP_5tVRGvwR2EtzhbTcwFDRtfL__2sncAM13ei1Pvis_8GKe-s84W7_eEwSS7H8u9GTCTnwfb2jjDsq_VzygbK9Klhho1a8aCeLdkrQNa3ktaibvwJuApUcZkQSgDG4Q2d3iwrUboD2PhB1kjrBK2ZXLhp-vDGrfYKsoVU3DejVWQxo5bXDAh-1Ewo0SZvviqgSut8dayG6lFYit3__mur_tbuPyn9xuY4N9Sa7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش نبویان به بیانیه مشترک ایران و عمان درباره تنگه هرمر: عراقچی از دستور صریح رهبر مبنی بر انحصار ایران در مدیریت تنگه هرمز تخلف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/143947" target="_blank">📅 20:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143946">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/442a0c2db8.mp4?token=r-K17hu9xh_uKKLds2rvsWksUziR43km9DvudYWn_qT7kzR7_29jCV7kbtRy-GpNcoT-0hQoUD2OvqV0DNKg17wDnQZxeNlNpRLgKls_EWZB0fm75NQHBirw2R5ixtt780n-VDL_XV9VUbdcCKzy_KtbWczHKY1sTHHW07nPXO2U94YH7DA_-H3KmUcPMgBHsIxjXOThJGskQDdp8UIxArNw_WQZgJInxm9AcYrMbc-WSBD3gxZgb_go9jeTyimS-NfHqvGEWIQZ-EqHwsz_XoeOZgZMddqmAoX-oI581-Xj3FPmZ7DeWmG2j0hL39K-JTaKsPzE0A0sYvCD9HNDeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/442a0c2db8.mp4?token=r-K17hu9xh_uKKLds2rvsWksUziR43km9DvudYWn_qT7kzR7_29jCV7kbtRy-GpNcoT-0hQoUD2OvqV0DNKg17wDnQZxeNlNpRLgKls_EWZB0fm75NQHBirw2R5ixtt780n-VDL_XV9VUbdcCKzy_KtbWczHKY1sTHHW07nPXO2U94YH7DA_-H3KmUcPMgBHsIxjXOThJGskQDdp8UIxArNw_WQZgJInxm9AcYrMbc-WSBD3gxZgb_go9jeTyimS-NfHqvGEWIQZ-EqHwsz_XoeOZgZMddqmAoX-oI581-Xj3FPmZ7DeWmG2j0hL39K-JTaKsPzE0A0sYvCD9HNDeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
سیل در نپال یک پل را از جا کند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143946" target="_blank">📅 20:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143945">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
آمریکا: مذاکرات لبنان و اسرائیل از سر گرفته خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143945" target="_blank">📅 20:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143944">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
بحران بنزین شروع شد
‼️
‼️
خودتونو آماده کنید برای طوفان!
تحلیل ترسناک این پسره رو حتما ببینید
👇
https://t.me/+6PPyWURHtW5jN2M0
https://t.me/+6PPyWURHtW5jN2M0</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143944" target="_blank">📅 20:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143943">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/va_wFzVnPIV5MHEWrO_Irdcaz_uCZs4hyckqxs6c0josXg6L5AMySxiPfXibgZ79sWePSfcGxWK37zLH5o-Y3FYYtuULgD2fJvcSk8aYp-Ai8ul2HgtqEKnef0dReN5Oma98z9J8UAj4BKs-EqQohUxXZj7socieK_4ktkT5Gbgy59A4t65H0Qd9USdwwJph4jYA_aOIVT7pWNRqUCqb7wHaTbytidbuRgd6QY5utndXdf7kWSS2AJrYxrdV6vHwYWCeLiNJUICY1sY-9UeClgsKON2xH_junEe14Zipo0sD7SDScqhjySPdRbTt9svhMbNeaBrbAJXPpjwSxPpeDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ در تروث سوشال:
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/143943" target="_blank">📅 19:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143942">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c7c7f3f23.mp4?token=iTyCpJYSvnWScYwCkSHqOix3l36bCPirdP9PH3KwngaW6U3K13gPn-9v_UNF23jQAZEoCBAHV7kbb5ngAm7JqyUgk42Usfr43Cc2PjFyPUlpYqR7TkyqDwL1C-K1na_Sez6bagPJm7bn7m4jA1yKY1-st-t52O2BmbFXXTqtZPeS42J0pdXkFx5_SeQ6xJxgvaFVfuxzBPX-BBu1sSi692956P-tFTZ9wLW5q89_yAZo-S_S-2vKtwsIg8r7djqOuYUREarcKWzanilhmLxJjNID0Bd5j3YE0IiTBA8fXn2sr0hMsgqiD5MIHfAmVYnU_rUx4Sg9uf1IC-K0yiAn7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c7c7f3f23.mp4?token=iTyCpJYSvnWScYwCkSHqOix3l36bCPirdP9PH3KwngaW6U3K13gPn-9v_UNF23jQAZEoCBAHV7kbb5ngAm7JqyUgk42Usfr43Cc2PjFyPUlpYqR7TkyqDwL1C-K1na_Sez6bagPJm7bn7m4jA1yKY1-st-t52O2BmbFXXTqtZPeS42J0pdXkFx5_SeQ6xJxgvaFVfuxzBPX-BBu1sSi692956P-tFTZ9wLW5q89_yAZo-S_S-2vKtwsIg8r7djqOuYUREarcKWzanilhmLxJjNID0Bd5j3YE0IiTBA8fXn2sr0hMsgqiD5MIHfAmVYnU_rUx4Sg9uf1IC-K0yiAn7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیروز کسایی که سال ۱۴۰۴ برای ثبت‌ نام یه ساله لاماری شرکت کرده بودن و هنوز ماشینشون رو تحویل نگرفتن جلوی شرکت مربوطه جمع شدن و خواستن در رو از جا بکنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143942" target="_blank">📅 19:50 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143941">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/592c74d9a4.mp4?token=TZLnYdu1sfGp3F7IR9OO39PYZtpMCtmM3PQAUC9QoK6dQhbe544ZF_O-PT157VZBRwstLG2RyEIUHyYm-cfU_grQAXa6sv3OZ_iw8YAIc3vl2S-eX6Z6OCIRQdno9yBciulG3MoTHMDyNuHhH55nsgcWCWuTHcEezyS5Nsp2DFlOQCgDZnWIHgV7j79nXbGjLMAZsQp1ToqNYANb6WLbJ0_ZEys8eZHZTV8ksnpOm72fEhMYVop8Gecx0ei5yWw-uVH9O2gjWVKfrLBOxL3YQ4r5FhqKKDDtv8AbuJNk9lESqLbzstXZ_Vrxq8MKCP7f44Wq9aIvWSzCn3pf5A3SPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/592c74d9a4.mp4?token=TZLnYdu1sfGp3F7IR9OO39PYZtpMCtmM3PQAUC9QoK6dQhbe544ZF_O-PT157VZBRwstLG2RyEIUHyYm-cfU_grQAXa6sv3OZ_iw8YAIc3vl2S-eX6Z6OCIRQdno9yBciulG3MoTHMDyNuHhH55nsgcWCWuTHcEezyS5Nsp2DFlOQCgDZnWIHgV7j79nXbGjLMAZsQp1ToqNYANb6WLbJ0_ZEys8eZHZTV8ksnpOm72fEhMYVop8Gecx0ei5yWw-uVH9O2gjWVKfrLBOxL3YQ4r5FhqKKDDtv8AbuJNk9lESqLbzstXZ_Vrxq8MKCP7f44Wq9aIvWSzCn3pf5A3SPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک ایست بازرسی عادی در یمن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/143941" target="_blank">📅 19:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143940">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
رئیس سازمان انرژی اتمی: تا تدوین پروتکل بازرسی از سایت‌هایی که مورد حمله قرار گرفته‌اند، آژانس نمی‌تواند از سایت‌های هسته‌ای بازرسی کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143940" target="_blank">📅 19:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143939">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhVFz0yuKMehF3op5h9GwfVmMMCECLk-VXqLUSVv8yJA1pRMgluPvbOTkNUFW6Fs6b2hXO8spe3XAU_CFIO6HejCyp4iVBUHNfbQbD6U5JLSc0ki0WxPPv-nEhwhAzht_tI4SOAHwpkolMClw1riYc87cycQ1PtuYTmj2DUbtkKsyljD4EmX8mfw8pKsb3AkmG0Psaj6I1CsE1rKs6LDpB7EOGdOgpW16gnQV5oQmna4MAif9wPGj_lQ52gxt19uivuLbQS3WU11DjqLaDx5yjyYUoWJTJQvoTYy7jFSWqMVPA_T8GMpV8DaDts4xQTSdquQ57Lv44iC7OFLJge3rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بدلیل گرونی سنگ قبر یه عده دزد شبونه از قطعه ۲۱۷ بهشت زهرا کلی سنگ دزدیدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/143939" target="_blank">📅 19:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143938">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
سی‌ان‌ان: پاکسازی مین‌های تنگه هرمز کار ساده‌ای نیست
🔴
همکاری ایران حیاتی است
🔴
صرفاً اعلام بازگشایی نمی‌تواند خطر مین‌های دریایی را از بین ببرد یا اعتماد بازار را در میان صنایع کشتیرانی و بیمه احیا کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143938" target="_blank">📅 19:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143937">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
یک منبع دیپلماتیک به شبکه المیادین:
نخست‌وزیر و وزیر خارجه قطر به زودی به تهران سفر خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143937" target="_blank">📅 19:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143936">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
یک نفتکش هندی به نام HAANA لحظاتی پیش قصد داشت از مسیر جنوبی تنگه هرمز، موسوم به کریدور عمان، عبور کند.
🔴
این نفتکش پس از دریافت هشدار، از ادامه مسیر منصرف شد
🔴
همچنین گفته شده در ۲۴ ساعت گذشته هیچ ترددی در مسیر جنوبی تنگه هرمز مشاهده نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143936" target="_blank">📅 19:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143935">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ: سفر رئیس سازمان اطلاعات مرکزی آمریکا (CIA) به روسیه ربطی به تحریم‌های ایران یا احتمال حمله مسکو به انگلستان ندارد
🔴
دونالد ترامپ، رئیس‌جمهور آمریکا، گفت سفر جان رتکلیف، رئیس سازمان اطلاعات مرکزی آمریکا (CIA)، به روسیه «به‌نوعی یک سفر نیمه‌روتین» بوده و گمانه‌زنی‌ها درباره دلیل این سفر را رد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143935" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143934">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d12996542f.mp4?token=Js8IvWZiWq27KK53nGt_IcoNxG0a_LeoKRyIFyyIKRRuSzjU_XZ2r8VL5Ldppwe5jP-tIKWRQudN9BchQQicgH543lmuivLYz9PaXbivjgis8hjpRAnmGfbtZ5DPWiSZ7RWg63cQcPSLMD7xyYQ4unvL_tPn8MYUlOtw0phTUZqH60EHAdZQfonvbb7c_USy0ekmU-tjwuZ00aCkgUCU4CFHEveiWI8echLAcwghLRdojjP5qq-I2lUKu8qecdZvrdPzakfh3MpHDQhLGPjR8g01KwuH_PI7ZQZ0hfmZXEnyFiA5mTFnq5kwFicR9A0VLNsK1n54_n0WnmKz3rr7Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d12996542f.mp4?token=Js8IvWZiWq27KK53nGt_IcoNxG0a_LeoKRyIFyyIKRRuSzjU_XZ2r8VL5Ldppwe5jP-tIKWRQudN9BchQQicgH543lmuivLYz9PaXbivjgis8hjpRAnmGfbtZ5DPWiSZ7RWg63cQcPSLMD7xyYQ4unvL_tPn8MYUlOtw0phTUZqH60EHAdZQfonvbb7c_USy0ekmU-tjwuZ00aCkgUCU4CFHEveiWI8echLAcwghLRdojjP5qq-I2lUKu8qecdZvrdPzakfh3MpHDQhLGPjR8g01KwuH_PI7ZQZ0hfmZXEnyFiA5mTFnq5kwFicR9A0VLNsK1n54_n0WnmKz3rr7Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگست: گزینه حمله نظامی در هیچ نقطه‌ای از تنگه هرمز منتفی نیست
🔴
ما به هیچ‌وجه استفاده از حملات نظامی در هیچ نقطه‌ای از تنگه هرمز را منتفی نمی‌دانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/143934" target="_blank">📅 19:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143933">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ:
شب گذشته 22 قایق نظامی تندروی ایران را در تنگه هرمز هدف قرار دادیم و نابود شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/143933" target="_blank">📅 18:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143932">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Egopf7fjGjdS8NVWhMlUHVrqf99rf1FvJvnmbnK0BY0vrVtufKyL5JRdTbFJWGeyNb4BlWCvOXHur34hcu73ZJsMPvBA8PjPg3zeB_HcmVww3Lw9FD7wztqg8gkT6jLSezJNoqvBKlEyfIPQKxQmKp1u92KNw9KLGDbUCpkl7EtWhrH8TrRDcVFIXhzreQx9QV4CXR-OXy-JUMFHy982N4kXD4YsaV3flC1FudAskm_rEmNEhRuP4zOkt1hrw7gSJekANyCkHbs-8pGGRpJOGdIdR9kXuloOZepp9iTdi76jaCYQinLDdoQD9QV67n1xMfZwB146vLluh93w9bdyBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی:
اینترنت رو قطع کنید، یه دیقش هم ضرره
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143932" target="_blank">📅 18:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143931">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏
👈
خبرنگار کاخ سفید:
گزارش هایی وجود دارد مبنی بر اینکه روسیه در حال آماده شدن برای حمله محدود به انگلیس است، سفر ناگهانی و غیر عادی رئیس سازمان سیا به مسکو نیز به همین دلیل بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143931" target="_blank">📅 18:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143930">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f48fa42be5.mp4?token=SvLRHIDhne_657VaWsaH_hNtKXPQLQsqrsFnHSOXoBEuy9WMgVSVg0Q0So9jbNcoNR-2GhhzQZX6xeqM94-WvYDRe5nQaVZwnpjfznI33fx2ZzxGlCno6OOvMC_FTywORqi9K4SWwOK42oZSni5QIrqWt8XoCiXOx7HyvysCBtuem5xhxn0Htr8D5uiNq1j3qbfos3BBeSphN7OdYzZmAAt1okuN4ZlqgJAIpI6mVIp86ngK6PX_u9xEhL1HBK-8il1aU1N-xfGcKgmRK14EtpGp27KTh6cPw-Sv2eV4S_7JoEn-K1yAEHFJv9_296jWdpRBtd4YAqNL1RspAJD7VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f48fa42be5.mp4?token=SvLRHIDhne_657VaWsaH_hNtKXPQLQsqrsFnHSOXoBEuy9WMgVSVg0Q0So9jbNcoNR-2GhhzQZX6xeqM94-WvYDRe5nQaVZwnpjfznI33fx2ZzxGlCno6OOvMC_FTywORqi9K4SWwOK42oZSni5QIrqWt8XoCiXOx7HyvysCBtuem5xhxn0Htr8D5uiNq1j3qbfos3BBeSphN7OdYzZmAAt1okuN4ZlqgJAIpI6mVIp86ngK6PX_u9xEhL1HBK-8il1aU1N-xfGcKgmRK14EtpGp27KTh6cPw-Sv2eV4S_7JoEn-K1yAEHFJv9_296jWdpRBtd4YAqNL1RspAJD7VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از مسئولان‌نظام هنگام مال مردم خوری
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143930" target="_blank">📅 18:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143929">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMGruYeTxfjtw8CEnsa5Vxov2GcdQOK4wUC6triEzqLOkGHoKBq7TTk_rayrTmyp1ukEr7Xl0QwUstbvxHl9NGWbEij7ovinML6raQtvqe_OkDWd-6H793YedY1x3toX9Xnbi7aF--nJ8ZaN6G0xUJmTLj_TKPwcYl6KV1gWGOP4inJyNOew8f_Bq2TSAEbYlKlHRPzbIbJV9-TISKI1SzgXiEk03KeTerj71kTuiQzeN0Ib_ph9E0euAtJuADbcqOmKOBNciCg611Ywi-pIq18lqvcTtelCw9kQiPIxoacFIE_GhsOBnalBhio-KpRzKRFlaIQEBhnL1kQBtn-mAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چادی هوپان: یه عده خائن از ویزا نشدن من خوشحال شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143929" target="_blank">📅 18:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143928">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cd6b5d203.mp4?token=Ao671VICvy7nsKaX3RxTVQFpX_fMeYW3VYFYjzh6x5jaSfA1QdOn3-hX0KR0KIsfOb6znRAKIPdg9y1KYSKMtexX24s1G_92DaQvjpWQjafHeestvokpjx5YOloP_eQBNw92MXj2XbfMNV0D5_uFNdKIhS-oDuFX_pB-oqeUuBw5SbYg7N-o7FM7k07BBXH9TwtbtqJQkeGU8aCjEdenLD35VVW8iHfEBIQTf31d1lQkAuaLAEB_dLIzW5NhljnuaUooD3B7WNSn9FnrisAQQe_sbXbWmmfmsjv1wYeWp9ZzkHftuGb-NwgGslw0IADeui5s4eWPGvOVwltqPljQyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cd6b5d203.mp4?token=Ao671VICvy7nsKaX3RxTVQFpX_fMeYW3VYFYjzh6x5jaSfA1QdOn3-hX0KR0KIsfOb6znRAKIPdg9y1KYSKMtexX24s1G_92DaQvjpWQjafHeestvokpjx5YOloP_eQBNw92MXj2XbfMNV0D5_uFNdKIhS-oDuFX_pB-oqeUuBw5SbYg7N-o7FM7k07BBXH9TwtbtqJQkeGU8aCjEdenLD35VVW8iHfEBIQTf31d1lQkAuaLAEB_dLIzW5NhljnuaUooD3B7WNSn9FnrisAQQe_sbXbWmmfmsjv1wYeWp9ZzkHftuGb-NwgGslw0IADeui5s4eWPGvOVwltqPljQyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیالوگ ماندگار مرحوم داود رشیدی که حال و روز الان ماست
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/143928" target="_blank">📅 18:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143927">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وزیر ارتباطات: پرونده فیلترینگ باید در کشور بسته شود
🔴
استفاده از فیلترشکن‌ها خسارت بزرگی زده است
🔴
افرادی هستند که اصرار دارند در بر همان پاشنه بچرخد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/143927" target="_blank">📅 17:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143926">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qor9VOqNNt0-sbqqm-6u6TPVNX7zIoDKBCMacvAGZ1PW1KzBrpSer5k1Ib4-VtkzCYogMaQHyCUBh-Esv1XyYvT3LWB5VhyWMMcG_8K6YK2Xfuhg0KzLkU1yMMwUhQH06dgxLV_JIJcjIuu-utdfGJwrGyjdI4FzPI0e873VHLLeJlfc2WKh56m5ZypdYz04yvymYaaAVq3Dtv9D7ZRqLtBhPNIEJCqLzv3eaTljfh204Nwiy795zZMkTKnp3sI9yJXqC3iwSMxKKk3U9f0yVrl_IMhR-GfiSW8X2ENIcJlQGRJY-UPVtCO0YQUBMBxKpZRqJSNTPPQFd3tlyYADZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ به الجزیره گفت که حکومت ایران "با مردم خود بسیار بد رفتار می کند، آنها بسیاری از معترضان را می کشند."‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/143926" target="_blank">📅 17:50 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143925">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrI9Np-4CHv7T4BCznkzhyPi3g0UhbkJ1IrBWn7jO9p1z8NiCwqnZOxuhF6PN-7saA7uYr2WeV7YkusZD7rCG0s4hVt8OhQhtepQwVi08EaXt1P-qrKt-DF3aho6xojUy4_kjk-Zv3XtuW0DAjmqkPx943VaqAMszoqnKL-ZABWVoTuNXgVMpFfPUFsRdVa--7l89YYcQ8pJz_o3SMgqlQ0Tvzx3RrnGpTspq9qgtGvuNhvmWlYYtxAoeSjmBxHmUTbGPsPv_MP-V8vdupghUz-zB8IgNL1nsuE-BWoodhKQOBiXu9KE2A6YvVQ-K1lfEi7_4Ycar7I-B86Wrnb8jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: رهبر ایران زنده است ولی دست و پا و بدن به شدت آسیب دیده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/143925" target="_blank">📅 17:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143924">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترامپ: رویارویی آمریکا با ایران تابع هیچ جدول زمانی نیست و تا هر زمان که لازم باشد ادامه خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/143924" target="_blank">📅 17:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143923">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
دلار و طلا ریخت
‼️
بیا اینجا ببین کی باید بفروشی و بخری
👇
https://t.me/+6PPyWURHtW5jN2M0
https://t.me/+6PPyWURHtW5jN2M0</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143923" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143922">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de06f44cb7.mp4?token=up08NF56CoUsTdUdECgZCKqOhvyN0S_mK_E4CoIBRmQfb_imwh3tn-V4PkBNVh8LSxqlbjjhTxsW119ijso418OdE5yMLqohbzICBu3UlFp5PqIq96egMhd0HYvgzhcx1lD0NMkg58HN-yUWshq2gqWZKoNGP0MZoauDuzpaeNssHnXh6zTvdmDoSAUVTgYyu5apCOFtO4MXbfSewaGpk1RRBx6uiCLdxzAJa4ZAw0PfToKV4xqYVvEFDrKTbEp4eKWz0CZ4zdqRVoHO3L9DqatZJrLdRSQFDafPnoE9bZms2foFaC_qTucGl6NJidmUDwNTTUSEW1sYTqzNPGDgCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de06f44cb7.mp4?token=up08NF56CoUsTdUdECgZCKqOhvyN0S_mK_E4CoIBRmQfb_imwh3tn-V4PkBNVh8LSxqlbjjhTxsW119ijso418OdE5yMLqohbzICBu3UlFp5PqIq96egMhd0HYvgzhcx1lD0NMkg58HN-yUWshq2gqWZKoNGP0MZoauDuzpaeNssHnXh6zTvdmDoSAUVTgYyu5apCOFtO4MXbfSewaGpk1RRBx6uiCLdxzAJa4ZAw0PfToKV4xqYVvEFDrKTbEp4eKWz0CZ4zdqRVoHO3L9DqatZJrLdRSQFDafPnoE9bZms2foFaC_qTucGl6NJidmUDwNTTUSEW1sYTqzNPGDgCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اگر دونالد ترامپ رئیس‌جمهور نبود، اکنون اسرائیل وجود نداشت.
🔴
این یک تضمین است. اسرائیلی وجود نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/143922" target="_blank">📅 17:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143921">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b63c7b29f.mp4?token=WhrKBBwZDIDvf4C3zQxyVFVR9xZDysJHcBlznNXKm11eUCSmUrez_HfoluN_FvOEY5CeO1cYiWrwdYxgxfy9VDSoXze1YGRcq8u6EThaX8QQS35Cwyb6Srefx31NhenpVp_cIKoXU77HzXvRH1wc5Njx4F2Iso8lrqdw8hFVV_sNYn5SgW5WhIIw5OfYodxv9-p8XN33I5YQ3KIDdOrv4OkHbHIQFXVgtWfihDENWuOeSezynK1HA8E318vLYoTIZocQKUb8r9bm1vVfNqVdvHTEaaFP57rTdmRfmtARkrTRSTONprmlHwrCaxNP_73DDKDSecTvYm7Ip2DzHRvkIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b63c7b29f.mp4?token=WhrKBBwZDIDvf4C3zQxyVFVR9xZDysJHcBlznNXKm11eUCSmUrez_HfoluN_FvOEY5CeO1cYiWrwdYxgxfy9VDSoXze1YGRcq8u6EThaX8QQS35Cwyb6Srefx31NhenpVp_cIKoXU77HzXvRH1wc5Njx4F2Iso8lrqdw8hFVV_sNYn5SgW5WhIIw5OfYodxv9-p8XN33I5YQ3KIDdOrv4OkHbHIQFXVgtWfihDENWuOeSezynK1HA8E318vLYoTIZocQKUb8r9bm1vVfNqVdvHTEaaFP57rTdmRfmtARkrTRSTONprmlHwrCaxNP_73DDKDSecTvYm7Ip2DzHRvkIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
وقتی به لندن می‌روید، وقتی به پاریس می‌روید، تقریباً انگار قانون شریعه (احکام  اسلامی) یک سبک زندگی دوم است.
🔴
این مسخره است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143921" target="_blank">📅 17:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143920">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61179d1b62.mp4?token=jSDvCjeGHKHA_eCF_ZahdIpmbOXxZ2nD02F_-vfR9fiEw_xNnE9N9ul5t0sxkI2xLPUVcrJwheqddpZfoPP61O1jpKVe1nxrEpevXd4fGHZEyWuNtrWDJtXRTmhiy2LkM4QpijDqg1JVKx4bdy_inH3tJutAWJywAZaUk4JUhFNybhJpeSJWdWJd05o40fAB2FOkWe8VWkfBl4BxCzGdgpKcqjFG7MYB4oyBThSF3q-Q2wq-xTyDTtZyorg1h_VHnK1X8uL2ggr29CMVtR-oTT0eGtUyZdkV-nnSvReHL5rETKHXSHnIm4qkULHY3lDL4TFJPnsLkETvFUZ7HszVDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61179d1b62.mp4?token=jSDvCjeGHKHA_eCF_ZahdIpmbOXxZ2nD02F_-vfR9fiEw_xNnE9N9ul5t0sxkI2xLPUVcrJwheqddpZfoPP61O1jpKVe1nxrEpevXd4fGHZEyWuNtrWDJtXRTmhiy2LkM4QpijDqg1JVKx4bdy_inH3tJutAWJywAZaUk4JUhFNybhJpeSJWdWJd05o40fAB2FOkWe8VWkfBl4BxCzGdgpKcqjFG7MYB4oyBThSF3q-Q2wq-xTyDTtZyorg1h_VHnK1X8uL2ggr29CMVtR-oTT0eGtUyZdkV-nnSvReHL5rETKHXSHnIm4qkULHY3lDL4TFJPnsLkETvFUZ7HszVDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره تورم در ایران
:
فکر می‌کنم تورم ۳۰۰ درصدی دارند. شنیدم ۹۰ درصد است. فکر می‌کنم تورم ۳۰۰ درصد است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/143920" target="_blank">📅 17:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143919">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07afc966eb.mp4?token=VWXTtouvHKRpPifmXcik3WCvJn3IHNc_X4XesuaSDPaWxClCxH1TZWvMpqRqnaTrtlRzZODT3ijxVFKfn3PNyQ_6FdUQliN9gM4JPvZjYjfjHSiXD44ewU1K8g2rJicy80fzKtDijtfsd72lTLKdjZPzIQRF8eoq_zN6K-NUgoGGABrbLawhPjVZdZi2UhMoNIG_3g5UJjyj3pZsb-SNg3z6yDL1_t-m3ij4g3pa-WpZrMg7cSC8getRqMrpesQsbJxvCpBccuwlwgRqSPyDH3SrKPOB3FLysbkg0tioPIqkQD4Rs43AxDlnOG3g-YGUGWl-1DEEjcN7Ow78MZeWgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07afc966eb.mp4?token=VWXTtouvHKRpPifmXcik3WCvJn3IHNc_X4XesuaSDPaWxClCxH1TZWvMpqRqnaTrtlRzZODT3ijxVFKfn3PNyQ_6FdUQliN9gM4JPvZjYjfjHSiXD44ewU1K8g2rJicy80fzKtDijtfsd72lTLKdjZPzIQRF8eoq_zN6K-NUgoGGABrbLawhPjVZdZi2UhMoNIG_3g5UJjyj3pZsb-SNg3z6yDL1_t-m3ij4g3pa-WpZrMg7cSC8getRqMrpesQsbJxvCpBccuwlwgRqSPyDH3SrKPOB3FLysbkg0tioPIqkQD4Rs43AxDlnOG3g-YGUGWl-1DEEjcN7Ow78MZeWgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: وقتی افرادی حاضرند شما را بکشند، اعتراض کردن در ایران بسیار دشوار است. به همین دلیل آن‌ها اعتراض نمی‌کنند.
🔴
و شانس وجود دارد زیرا آن‌ها بسیار تضعیف شده‌اند... بسیاری از سربازانشان حقوق دریافت نمی‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/143919" target="_blank">📅 17:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143918">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e724bf7fc2.mp4?token=KwWznANESmrxQJ1qnDOZ2rhMYJly4oWlSyO4F8StHfkTF4J-b8_-hkam1G_SdEPbWNSqh4iKA-VTQKTK0m3x3x9jle_Os6957NUw-orgJQVW7xZENtkMscig_5DtdDuml9-e4gvuI-LuI3aO2KmDIVuFxNNipUHsO-LS9kFKG8dIOkRCAa-l4z0CmWjIk1knvWweA9bQBO7F5MTh0j_cxelq9cwrRLwhnvu4LRYgoWqZ5o5sfO0qoio7N8d4sblzHkEm4cL47p2CG2KP_3eyDTnPBRZwdtl6zEinsoTiWyjahNtII78cssg8QaHdIcMWRUAleYOTCX9Dm1CfFR8tpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e724bf7fc2.mp4?token=KwWznANESmrxQJ1qnDOZ2rhMYJly4oWlSyO4F8StHfkTF4J-b8_-hkam1G_SdEPbWNSqh4iKA-VTQKTK0m3x3x9jle_Os6957NUw-orgJQVW7xZENtkMscig_5DtdDuml9-e4gvuI-LuI3aO2KmDIVuFxNNipUHsO-LS9kFKG8dIOkRCAa-l4z0CmWjIk1knvWweA9bQBO7F5MTh0j_cxelq9cwrRLwhnvu4LRYgoWqZ5o5sfO0qoio7N8d4sblzHkEm4cL47p2CG2KP_3eyDTnPBRZwdtl6zEinsoTiWyjahNtII78cssg8QaHdIcMWRUAleYOTCX9Dm1CfFR8tpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کانادا
:
آن‌ها هیچ چیزی ندارند که ما به آن نیاز داشته باشیم. ما می‌توانیم بدون آن‌ها ادامه دهیم.
🔴
چند مورد وجود دارد که می‌تواند کمی آزاردهنده باشد، اما می‌توانیم آن‌ها را از جای دیگر تهیه کنیم.
🔴
حرفه است که به کانادا درس دهیم که دیگر نمی‌توانند این کار را انجام دهند.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143918" target="_blank">📅 17:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143917">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ترامپ: من باور ندارم که رهبر فعلی ایران فوت کرده باشد
🔴
اگر هم مرده باشد، دارند نمایش خیلی خوبی اجرا می‌کنند؛ چون مدام صحبت از این است که باید برای گرفتن تأیید نهایی‌اش با او گفتگو کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/143917" target="_blank">📅 17:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143916">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ به الجزیره: ما در حال دستیابی به یک پیروزی بسیار بزرگ هستیم و ایرانی‌ها از تورم عظیم رنج می‌برند و اقتصادشان در حال فروپاشی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/143916" target="_blank">📅 17:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143915">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فوری/ترامپ درباره ایران: بگذارید این را به شما بگوییم، من متوجه شدم گروه سوم (سران کنونی ایران) هم خوب نیستند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143915" target="_blank">📅 17:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143914">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوری/ترامپ درباره ایران: بگذارید این را به شما بگوییم، من متوجه شدم گروه سوم (سران کنونی ایران) هم خوب نیستند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/143914" target="_blank">📅 17:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143913">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ترامپ: ما مین‌ها را از آنجا خارج کردیم. اما تنگه هرمز، به کار خود ادامه می‌دهد، یک تنگه فعال است.
🔴
بله، گاهی اوقات ممکن است یک پهپاد یا موشک شلیک شود، اما این یک تنگه کاملاً فعال است.
🔴
مقدار زیادی نفت از آنجا صادر می‌شود.
🔴
دیشب ۲۰ قایق ایرانی را منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/143913" target="_blank">📅 16:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143912">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3f8d4b27a.mp4?token=ScMPIImqAc3dqiLkQiLAzkQ8XypAox821pF8ZmViPCSf6vBa4BEIbDgHsMA6STsUOsrnce2e25bOZnftKWF-nkkfVT0CuzuMtcaZGdffzDZWTDSET7UdsDK7NN5Dt4WrC2KbdWgw4YCk0UyI7iRSFtwWQEHeuimpz5Ucx3Rl5yTbi553hvFi2WyRdUvo5YPOMNPEVYsOnrCXWEBepR3lMTymHxL4H5CjNye1DWm9v4vsXxe7_iREXC_saURwy-4zr1NhUfzbnVAcV6sOZZ7ODktc9cQ9JSfShNiZglOu17PRVeDU9A5mhfhDlgdgJQgPkjDwJw9Nl80a2DZ_qgbw9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3f8d4b27a.mp4?token=ScMPIImqAc3dqiLkQiLAzkQ8XypAox821pF8ZmViPCSf6vBa4BEIbDgHsMA6STsUOsrnce2e25bOZnftKWF-nkkfVT0CuzuMtcaZGdffzDZWTDSET7UdsDK7NN5Dt4WrC2KbdWgw4YCk0UyI7iRSFtwWQEHeuimpz5Ucx3Rl5yTbi553hvFi2WyRdUvo5YPOMNPEVYsOnrCXWEBepR3lMTymHxL4H5CjNye1DWm9v4vsXxe7_iREXC_saURwy-4zr1NhUfzbnVAcV6sOZZ7ODktc9cQ9JSfShNiZglOu17PRVeDU9A5mhfhDlgdgJQgPkjDwJw9Nl80a2DZ_qgbw9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من قطعاً قانون شریعت (احکام اسلامی) را ممنوع خواهم کرد.
🔴
ما یک سیستم عالی داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/143912" target="_blank">📅 16:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143911">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f2bb31062.mp4?token=B0JHHn03A_m3wMJJ-q0EdgKonqV7jofO48wiejLgu4304sxBW7nvgBhgwgiTxEZPGA59UbTPvnplIWFAZyr-tTnvWzYsu1xIIOHgxIksUZQmlhJaiupLxuBUj3sW8Sj5m39VE1AUzvPkyTUmWddzRo094trO5KHnsUvd7RSfTMEs6P0rRQ26dS2qm-vHIF-Sha-EWqJ4t8h0fjgk3slwbY6ceQYNZIX-ELDY9B2ZU2OzsnMSkzkYOxh6w_MyTBkkwOf3r0LXT02E4GRZ7Am8OjBP-UPnOwRbcJVi41valA_xwtfZIQPfG9pui5cdDNJ4t9hl5deCOAzkjrRGm6ITug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f2bb31062.mp4?token=B0JHHn03A_m3wMJJ-q0EdgKonqV7jofO48wiejLgu4304sxBW7nvgBhgwgiTxEZPGA59UbTPvnplIWFAZyr-tTnvWzYsu1xIIOHgxIksUZQmlhJaiupLxuBUj3sW8Sj5m39VE1AUzvPkyTUmWddzRo094trO5KHnsUvd7RSfTMEs6P0rRQ26dS2qm-vHIF-Sha-EWqJ4t8h0fjgk3slwbY6ceQYNZIX-ELDY9B2ZU2OzsnMSkzkYOxh6w_MyTBkkwOf3r0LXT02E4GRZ7Am8OjBP-UPnOwRbcJVi41valA_xwtfZIQPfG9pui5cdDNJ4t9hl5deCOAzkjrRGm6ITug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
ما به زودی پیروزی بزرگی در ایران خواهیم داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143911" target="_blank">📅 16:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143910">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acb401a2e6.mp4?token=R0JG1tU3Q1a9o-Q-h_H8bfkxljgHYHn2dIW5iV5wSUmndMsSvTpYwcnHWRdlK-Jpa65DdU99m4LqONnviIvYJVVJ80mJM9PVhr0BhoJQkHY7bDwcI4WQRx03FXf6bWNQD3gLotYxCeWz7ltpxJzO0GlMgijzEXiRmTZMZ8vogh6doD1Eay9m4bXP_mBm8rSLPXc7hto79bBLXW3NqoSihHy4TSs_Iq6czkgXwYhYcDlKWfJhNToJMhUWM7p8pAirOs2l6vxOjNLul4VU_O_MtWOLaQ7JjIAmZaKcek0jvqGx2EcnIvFM4QKMC79vrilqDwwplBtt0m_umsP7QDJUSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acb401a2e6.mp4?token=R0JG1tU3Q1a9o-Q-h_H8bfkxljgHYHn2dIW5iV5wSUmndMsSvTpYwcnHWRdlK-Jpa65DdU99m4LqONnviIvYJVVJ80mJM9PVhr0BhoJQkHY7bDwcI4WQRx03FXf6bWNQD3gLotYxCeWz7ltpxJzO0GlMgijzEXiRmTZMZ8vogh6doD1Eay9m4bXP_mBm8rSLPXc7hto79bBLXW3NqoSihHy4TSs_Iq6czkgXwYhYcDlKWfJhNToJMhUWM7p8pAirOs2l6vxOjNLul4VU_O_MtWOLaQ7JjIAmZaKcek0jvqGx2EcnIvFM4QKMC79vrilqDwwplBtt0m_umsP7QDJUSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
ما از همان ابتدا واقعاً و به‌طور کامل بر ایران مسلط شده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143910" target="_blank">📅 16:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143909">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
رایزنی وزرای خارجه عربستان، ترکیه و قطر درباره کاهش تنش در منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143909" target="_blank">📅 16:50 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143908">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bab00cbf2d.mp4?token=FBLeVKYhyHIIE-M0ZbTCScCmX_Isp9R6pRiCexxZd-gP6XSgDKLUK_dNgZJo3c1-EmYd3rOI1pQhXp3AZwjCAInGK4gwiEy_8EfXezz82kbcCn5K72j5dn_q1kqyuCmlPvD0dzxzowN3rWu3o-R1xIPvLP25Gv7Xjn-BGMvLcadQ7PDGA8nTjiPmiBYg5jaL9szHuNUqu1r4XVdY2X-fo3-PX_9LbwZRfA348k5JhMHd585K1qGulrkNcUbKajlRW77mRZaV1agI0VhYB4gSOH0lpxup6hFbd3rSjwmYmrwGwI2_er-IRQJiE3CSUWk5QZLueAHaokNEbiz81E7iAHEfr3xDgFhaUrQCqgPx8KSM2LgBf0ETwnvn7Aecrd7BcPcBjZflcqoasniA5xNeewGEYokE50rBjP4nzii10OwXp7FW48PyJw94UrQe7gMgkkXTkFRr6CWRP_0xK9wnRM8x_s2ThH518usUw1e2PWkQryc5sgHnRXHbMhgBY2ZlpQTR0ovov9xZ9lwwkXvsYyPLNqbi7VMaO1m5TSuMeYXpcN0_1uksgvwH5HQxkwq8zQFXobEsRt7hsGwnJNxR1kGHbChCIXF0wb77U_io_z0q3Yz2DqBV6klRnPHziewKsu0ESAVvV2HB2HRGn5nJnsJPhN_crT3J7xcancjBTjM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bab00cbf2d.mp4?token=FBLeVKYhyHIIE-M0ZbTCScCmX_Isp9R6pRiCexxZd-gP6XSgDKLUK_dNgZJo3c1-EmYd3rOI1pQhXp3AZwjCAInGK4gwiEy_8EfXezz82kbcCn5K72j5dn_q1kqyuCmlPvD0dzxzowN3rWu3o-R1xIPvLP25Gv7Xjn-BGMvLcadQ7PDGA8nTjiPmiBYg5jaL9szHuNUqu1r4XVdY2X-fo3-PX_9LbwZRfA348k5JhMHd585K1qGulrkNcUbKajlRW77mRZaV1agI0VhYB4gSOH0lpxup6hFbd3rSjwmYmrwGwI2_er-IRQJiE3CSUWk5QZLueAHaokNEbiz81E7iAHEfr3xDgFhaUrQCqgPx8KSM2LgBf0ETwnvn7Aecrd7BcPcBjZflcqoasniA5xNeewGEYokE50rBjP4nzii10OwXp7FW48PyJw94UrQe7gMgkkXTkFRr6CWRP_0xK9wnRM8x_s2ThH518usUw1e2PWkQryc5sgHnRXHbMhgBY2ZlpQTR0ovov9xZ9lwwkXvsYyPLNqbi7VMaO1m5TSuMeYXpcN0_1uksgvwH5HQxkwq8zQFXobEsRt7hsGwnJNxR1kGHbChCIXF0wb77U_io_z0q3Yz2DqBV6klRnPHziewKsu0ESAVvV2HB2HRGn5nJnsJPhN_crT3J7xcancjBTjM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مرتس صدراعظم آلمان: ما باید از این جوّ غم و ناامیدی خارج شویم.
🔴
ما باید از رنجش گسترده‌ای که برای مدت طولانی کشورمان را فلج کرده است، رها شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/143908" target="_blank">📅 16:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143907">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ به الجزیره: برای مذاکره با ایران «عجله‌ای ندارم»
🔴
ترامپ در گفتگو با الجزیره مدعی شد که هم اقدامات اقتصادی و هم نظامی در مواجه با ایران «موثر» هستند.
🔴
او در پاسخ به سوال خبرنگار الجزیره، افزود که «من هیچ برنامه زمانی ندارم، عجله‌ای ندارم»
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143907" target="_blank">📅 16:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143906">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
یک منبع ارشد ایرانی: توافق با عمان در مورد تنگه هرمز هنوز نهایی نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/143906" target="_blank">📅 16:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143905">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2cbeca874.mp4?token=H69cSwawonRatsxWpKb0X_2RLx62frXfiKNDq8u91j09lU2cEb8iNPGjDAAB3ZsM3SrItokZXeforOfqIW9FvIJpPzJJGunXU-2ncspXNwR9vrkGUPIhZc8gJtjqtCiOpEv7J-ILPy1455L3gvQzSh1QanbNphbx-v9ieocE0O1lVG3HbSHQ2xCT2-aM2I23vX93jqvnYtsEUpkG3TFRFadvaRC7fG66XFfRu3AaSpCeVr-gmva7EnjTjUGAuHtiVHEVT8AtCXBkOwoGVzj485KtMjkJoqVfEpBM1x9GYIfRVeJvIxmNfZcDMoBZf57WloSRTLO_PsjemGCqIsMCJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2cbeca874.mp4?token=H69cSwawonRatsxWpKb0X_2RLx62frXfiKNDq8u91j09lU2cEb8iNPGjDAAB3ZsM3SrItokZXeforOfqIW9FvIJpPzJJGunXU-2ncspXNwR9vrkGUPIhZc8gJtjqtCiOpEv7J-ILPy1455L3gvQzSh1QanbNphbx-v9ieocE0O1lVG3HbSHQ2xCT2-aM2I23vX93jqvnYtsEUpkG3TFRFadvaRC7fG66XFfRu3AaSpCeVr-gmva7EnjTjUGAuHtiVHEVT8AtCXBkOwoGVzj485KtMjkJoqVfEpBM1x9GYIfRVeJvIxmNfZcDMoBZf57WloSRTLO_PsjemGCqIsMCJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به‌دنبال وقوع سیلاب‌های گسترده در نپال، نزدیک به 300 گردشگر خارجی مفقود شده‌اند.
🔴
این سیلاب‌ها تاکنون دست‌کم 17 کشته و حدود 400 زخمی برجا گذاشته‌اند.
🔴
گزارش‌ها حاکی است مناطق مرزی نپال و چین نیز تحت تأثیر این سیلاب‌ها قرار گرفته‌اند و عملیات امداد و جست‌وجو برای یافتن مفقودشدگان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/143905" target="_blank">📅 16:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143904">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fae40c1a74.mp4?token=dMw8Q_rw4l2nbVAnr7OJvgNPnTCnbIEqHBmxbyde5Meu9c0ELv5bJoUF6RGae5dHBtNVJKB_BIVCdmFW5oaCfZ59gDQx-nyIeJ7pJuovaIx-sEN02jVipEXCm8aoetnlo_u-G9XtdHB-falKQ-pWJn-3MavBSokdw9gS-bLQjRXjZPt4ZRq428kwsk2YVo3FvCKuwBV73YMaUPwFmx_IH6vOH2d8EsRZaH66IjOI2fIe2N71Gp4gFHP8ysMxDkigH8wDX-wcsXQqtnBLx24lymhIFre_i7PdoS5DugqNtr3Gs1axcwHHX594RLWu1SCLmScOWXPu5XrVtaK4LENfwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fae40c1a74.mp4?token=dMw8Q_rw4l2nbVAnr7OJvgNPnTCnbIEqHBmxbyde5Meu9c0ELv5bJoUF6RGae5dHBtNVJKB_BIVCdmFW5oaCfZ59gDQx-nyIeJ7pJuovaIx-sEN02jVipEXCm8aoetnlo_u-G9XtdHB-falKQ-pWJn-3MavBSokdw9gS-bLQjRXjZPt4ZRq428kwsk2YVo3FvCKuwBV73YMaUPwFmx_IH6vOH2d8EsRZaH66IjOI2fIe2N71Gp4gFHP8ysMxDkigH8wDX-wcsXQqtnBLx24lymhIFre_i7PdoS5DugqNtr3Gs1axcwHHX594RLWu1SCLmScOWXPu5XrVtaK4LENfwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار دیشب تجمعات شبانه: دلار شده ۲۰۰ تومن همتی یه کاری کن نگن که بی غیرتی
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/143904" target="_blank">📅 16:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143903">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXmvfpz553C-t-y2bk7LBfv-8GzhBt2vMJtpDE9OBqb_YJ-OZHQfuDU-luukhIUke4esGTxm0nrCbfQeSiRD0kY4Kv1rVU8jA6oqXpxQOUr954ZbNFDtQqDtjT3O4HNQ2i90Vh4RdgClN7B9kqXp9kCpCRnfZDWFXFx0fZ_PtJ2Gclp7A2Qja4vKiQhiO7wrfCRojgGzXA2Y0TmPStG_zR_3RNrqi5MUTIt16Ge6xoYT3B7yD_3b76dZKonWJJ1oMCk2_8ti3rBbnZU_b-TTIJqarsBQALGTFKPB2pWnpKChemHVSxAPS3Zure-MZ-989iyU6bfpUi8dZdVXFPUhrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایالات متحده، تعداد هواپیماهای تانکر سوخت‌رسان خود را در پایگاه هوایی العديد در قطر به بیش از ۹ فروند افزایش داده است
🔴
در حال حاضر، بیش از ۱۵ فروند هواپیمای تانکر سوخت‌رسان در امارات و قطر، و حدود ۲۰ فروند در عربستان سعودی مستقر هستند تا از عبور نفت‌کش‌ها از تنگه هرمز پشتیبانی کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/143903" target="_blank">📅 16:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143902">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سفیر ایران در روسیه: برخی تلاش می‌کنند مناسبات تهران و مسکو را به روابط ایران و غرب نسبت دهند که رویکردی نادرست است
🔴
پزشکیان و پوتین برای ششمین بار، در حاشیه اجلاس آتی سران سازمان همکاری شانگهای دیدار می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/143902" target="_blank">📅 15:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143901">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وزارت خارجه سریلانکا:
13 نفتکش تحت تحریم متعلق به ایران را که در نزدیکی سواحل جنوبی سریلانکا هستند را زیر نظر گرفتیم و آماده توقیف آنها هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/143901" target="_blank">📅 15:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143900">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWnOw0FzIB8L4ZBh7FSHQ6fkfP2gbswErzSJ_wYgqH87XQjnLzzRTcW0MWzYSPbm-xcyJ7Y46SfyzM0Vo_rbxTe3j8wZPCfwv46JJeJmSjj75ag9jWlL3pr9AT3dw9Ajz8RnMX5r-AhWRmg0jJS7fbWWJB9OW6OkoyqNji3a5aRpUEHWmRsEeUM5RLEpow2T4x9MZRU1xGFptL9bzvMM19npT6WqvGNG4CsDQ4UAn92PnoeWOrYbuZeJRUBECGRlpys8UGlJm7asqRSxpZmzVVvXOBIBgIZ1WH8HkVJ1vLI7a4DUGGIgkdM7cej1ZZMnb9P8KomwfkfDlOYadMYl5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:رئیس مجلس نمایندگان، مایک جانسون، عالی است. او کارها را انجام می‌دهد!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/143900" target="_blank">📅 15:50 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143899">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
شیخ محمد بن عبدالرحمن آل ثانی، نخست‌وزیر و وزیر خارجه قطر، قرار است به‌زودی به تهران سفر کند.
🔴
بر اساس گزارش‌های منتشرشده، این سفر احتمالا فردا پنجشنبه و در چارچوب تلاش‌های میانجیگرانه قطر میان ایران و آمریکا انجام خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143899" target="_blank">📅 15:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143898">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
وزیر نیرو: در جریان جنگ اخیر، در مجموع ۴۲۰۰ مگاوات از ظرفیت نیروگاهی کشور را از دست دادیم که بازسازی و جبران این ظرفیت در دستور کار قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143898" target="_blank">📅 15:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143897">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سخنگوی سپاه: تنگه هرمز در اختیار ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143897" target="_blank">📅 15:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143896">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
شبکه ام‌اس‌ناو: از مجموع سه ناوشکن همراه گروه ناو هواپیمابر آبراهام لینکلن، فقط یک ناو همراه لینکلن بازگشته؛ دو ناوشکن دیگر تاکنون هیچ دستوری مبنی بر بازگشت دریافت نکرده‌اند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143896" target="_blank">📅 15:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143895">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-ymcjd9fD5EajsLokabjIoIkv_czCMR-m5wtum37HNBTOMYOT4VQ_X1wsw1p7RR-fOgtJAwJJ-W6i2qxp8TJmSrBht2--WElhPFTqPDNIy77Y-f4XcBrDwYqUXvHqpL6CUn0zMQRcf4ZJm2odCqlsP2Ev2lHbsI0rco_cek8M1frOOT9pA6W1f6UL7UMtJFHcqff1PmybyiI4P9bGSOTER9eHbfCfyslFAUpDBcaRDiQrg7r8C4U7VA-Ysvsuh5moBQWpL-xBsH0vYXO-3v8PC8ZF6Ccy6TDV3hv6Jrf_9YeoKnrvAcxi952Eyxg62Jj6xFXij2CHRQwg4H7PKKrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
راک‌استار انتشار تصاویر لو‌رفته GTA 6 را «دلخراش» توصیف کرد؛ تاریخ عرضه ۱۹ نوامبر
🔴
به اعلام راک‌استار گیمز، انتشار تصاویر گیم‌پلی GTA 6 پیش از موعد «دلخراش» بوده و این شرکت بابت اینکه بازی به شکلی خارج از برنامه در معرض دید قرار گرفته، عذرخواهی کرده است.
🔴
راک‌استار تأیید کرد توسعه بازی «تقریباً به پایان رسیده» و فردا نمایش مفصل‌تری از GTA 6 منتشر خواهد شد.
🔴
تاریخ انتشار بازی نیز ۱۹ نوامبر اعلام شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/143895" target="_blank">📅 15:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143894">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
نشریه "ترایبون"، پاکستان اعلام کرده است که ایران در جریان درگیری نظامی با هند در ماه مه سال ۲۰۲۵، "حمایت قوی" از این کشور به عمل آورده است!
🔴
این ادعا توسط ایشاق دار، معاون نخست‌وزیر و وزیر امور خارجه پاکستان، در پاسخ کتبی به مجلس ملی در مورد وضعیت روابط پاکستان و ایران مطرح شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/143894" target="_blank">📅 15:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143893">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYrOIpsCqmzymIt-CR96oPh99k5xiZrAKfXfs7v9yyZAHaB0n4fSlWDkZQhaDgarJhVEQjQ4SNPIiwC9Tnr66tE9HlqNk3_deDc0KExQC41PH_qJKF1Gq2YFDCa5HpLRtblPvowDWdDMqA8wA3kNDRWr60aqlMIK6-3G_IXRXOMFHr26I21wVnMGkVNxyFacsadsh2alyDHhXuTXUcy9giYYXXKRdo0ykvP8Zn-EAlpH781zh-2ONWbjlV8Z1gRLcQeXkH6gooMd5WZX2c2qfIL0ktcX1qyHHADAlR6EWgVqsgKblK6JwYp7MPOXsIevuT52aNOy7c7-ntIiYmJIfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، شبکه اجتماعی Truth Social:
رئیس مجلس نمایندگان، مایک جانسون، فوق‌العاده است. او کارها را به خوبی انجام می‌دهد!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143893" target="_blank">📅 15:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143892">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
پزشکیان: جنگ همیشه راه‌حل عبور از مشکلات نیست
🔴
گره‌ای که می‌توان با دست باز کرد را نباید با دندان باز کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/143892" target="_blank">📅 14:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143891">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
گفتگوی وزرای خارجه قطر و عربستان درباره تحولات منطقه‌ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143891" target="_blank">📅 14:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143890">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
تانکر ترکرز: در خلیج عمان دست‌کم ۱۵ مجموعه عملیات انتقال کشتی‌به‌کشتی (STS) در حال انجام است.
🔴
ما ۲۵ میلیون بشکه نفت خام را شمارش کرده‌ایم؛ به‌علاوه مقداری محصولات پالایش‌شده نفتی.
🔴
این نفت تقریباً از تمام کشورهای منطقه، به‌جز ایران، منشأ گرفته است.
🔴
اکنون پنج مجموعه دیگر نیز پیدا کرده‌ایم و یکی از آن‌ها مشخصاً مربوط به گاز مایع نفتی (LPG) ایران بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/143890" target="_blank">📅 14:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143889">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
امید دانا:
اختلاف «علی کریمی» و «رضا پهلوی» از اونجایی شروع شد که علی کریمی گفته بود به ازای هر اعـدامی؛ ما هم یه قرآن میسوزونیم که رضا پهلوی خیلی به اسلام اعتقاد داره و با اینکار مخالفت کرد.
هرکسی که اسلام ستیز باشه رضا پهلوی بایکوتش میکنه و بهش فشار میاره. چون میگه ما با اسلام نمیجنگیم.
🔴
رضا پهلوی خودش تا سال ۲۰۰۹ اصلا دنبال تغییر جمهوری اسلامی نبود و دنبال این بود از طریق رفسنجانی و خاتمی توی حکومت اصلاحات به وجود بیاره. مدارکش هم موجوده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/143889" target="_blank">📅 14:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143887">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L157JAKXZgAE8LHNxpUmzyBRdYVEqtZdLiomC-C1GSQ6B8jWsnKsv7g2WniuttIBDSb48hz0gGOwkogSsK8ZzKkwmoaZB6DTf82ssYygmOPN-7YM6tI2TOyIyP-CncxqIltu6z7zN6X2foPWhdrUQQS4nzIufJqa4Z8ohn4k4LSWdloDYHQd0SErb5Ks_t90M92v6c0Ay2zmAbhayYvOpL7WsWeOTn6AgwSWcIyr__-mEAWF-zDpiPJ3JzuxMAJ-IELBm0DB-JiD4kzFVUhCTa5qO6fOOnf2AZZZZL8YRL8t4H6zkRhXe502vfxWu3oJxqeGF2cdqO0GSbfypCxdMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640fdccd62.mp4?token=eA6FY_j--bqubf_WKVyqQ-n5K4tUqNgRR7rKyIje3z02REpjZi7eWTnERI1S2aWHTLAbby5G8FoYYwRBYkJQN6AK21ru1FZCMlkFNEGK-bTlu_5rQE7mBZHkCNvDJ0lLh8iz9-AZBVlNA7xZSPecjPfN4bMQADGyzARClvCH-qdQAhksJ3EWr8j8MetOrF6Pe6GJ8JLc6X49bXNwoEO0WuNQV3v2USufDRwuq9hFBSIRufoCHGE8A5cOuscfwtday0FNoGOg4-V_3DtuSvf4JOFd6Yyl18h2LFARJIuMV6F8JnDn0i61QR2_vgr0laG7wJtNZXNgB0GtOJHDqnrA5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640fdccd62.mp4?token=eA6FY_j--bqubf_WKVyqQ-n5K4tUqNgRR7rKyIje3z02REpjZi7eWTnERI1S2aWHTLAbby5G8FoYYwRBYkJQN6AK21ru1FZCMlkFNEGK-bTlu_5rQE7mBZHkCNvDJ0lLh8iz9-AZBVlNA7xZSPecjPfN4bMQADGyzARClvCH-qdQAhksJ3EWr8j8MetOrF6Pe6GJ8JLc6X49bXNwoEO0WuNQV3v2USufDRwuq9hFBSIRufoCHGE8A5cOuscfwtday0FNoGOg4-V_3DtuSvf4JOFd6Yyl18h2LFARJIuMV6F8JnDn0i61QR2_vgr0laG7wJtNZXNgB0GtOJHDqnrA5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیشب ایرج مصداقی، عضو دفتر رضا پهلوی گفت که
امید نادان (دانا) به پیچِ 14 میلیونیِ علی کریمی دسترسی داره چون کسایی که علیه امید نادان (دانا) حرف میزنن رو بلاک کرده.
🔴
حالا علی کریمی استوری گذاشته که
ایرج مدل 57، مشاور آقای رضا پهلوی؛ اگر ثابت نکنی که پیج من دست هر کسی غیر از خود من باشه، خیلی بی ناموس و پیشرفی!
24 ساعت به اقای رضا پهلوی زمان میدم که در این مورد اظهار نظر کنه، در غیر اینصورت هر اتفاقی بیفته، گردن خودش و مشاوراشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/143887" target="_blank">📅 14:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143886">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHv_O1QFY-fAd1j1TYT23F7JZQ7OhScpnL2gHMfl9r4WIusETs6L5STK0UFrZGZxPd9njHuL4pJci05je2O5H_6Ilsh6qNA162s22n6o2-JuqtkfBqwl-Dhy4Fx39cNo1g4Df0dX7ERt0lTmk8YEsRZF1nnz0mkrwQ2fRqJKqvAeYg_cb4RXtqQ2Q3S6UrytS7VRyASIMAJtr3NTlHQVmLkQNrX9z-zeVbIC5qXJJ9GPmauctIzc1EfmU44SYvf-0FYaOiPMkwLDDIYedL_SIgEVVc8hROIca74xRc_dHXItnjX8ujx2oeBp5kAL9cMeB2JEdHuy_YLYKsJMQkv58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره: به نظر می‌رسد که واشنگتن ممکن است در متقاعد کردن کشورهای همسایه برای پیوستن به تحریم‌ها علیه تهران با مشکل مواجه شود.
‏
🔴
برخی گزارش‌ها حاکی از آن است که با ۱۶ کشور هم‌مرز با ایران تماس گرفته است - ۸ کشور از این میان، دشواری قطع روابط اقتصادی خود با ایران را به دلیل منافع در هم تنیده تأیید کرده‌اند - در حالی که ۸ کشور دیگر پاسخ داده‌اند که در حال بررسی این احتمال هستند، که می‌تواند به عنوان یک امتناع مودبانه تعبیر شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/143886" target="_blank">📅 14:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143885">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
به گفته برخی منابع: به نظر می‌رسد که واشنگتن در متقاعد کردن کشورهای همسایه برای مشارکت در تحریم‌های اعمال‌شده علیه تهران، با مشکلاتی روبرو است. برخی اطلاعات نشان می‌دهد که این کشور با 16 کشور همسایه ایران در تماس بوده است:
🔴
8 کشور تأکید کرده‌اند که به دلیل وابستگی‌های اقتصادی متقابل، قطع روابط اقتصادی با ایران برای آن‌ها دشوار است.
🔴
8 کشور دیگر نیز اعلام کرده‌اند که در حال بررسی امکان این موضوع هستند، که این می‌تواند به عنوان یک رد غیرمستقیم دیپلماتیک تلقی شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/143885" target="_blank">📅 14:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143884">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHC2N7YDoB5icDYjgHRBTJeqpjcF5a0nG9RWz6za9rDq6OgD5S2F0yq8ifvYZA1mOXwDQrhKyXviRqIG7z1z5YoH5C_Rqkkjf-0PbAx244m_bvRkxTYyF3y6w1ABW7IpAK5znsV50VFwGvuagK0XtWy6W2O5VGNPaXhR9XO6ITtcq6I9ozfykhhWdFEj7k9AWA_yRho8CMnzVcv_LyOErZgnVkT8MKUsOERt9-ZL_g0XyZMFIPXZRbsxv0fjnGxZ4SgIqZjkNHOrZ42OIskb_A8lAwCcVMa-0xEcxi4oDj02PVJbb3jjJuAg0RnqBoRPD6xVBNlaAwQdJp8dTLmcwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلتفرم خرید آنلاین طلا میلی‌گلد، حدود ۳۰۰ کیلوگرم کسری طلا داره، یعنی طلاها رو فروخته ولی نگه نداشته. اگر توی این پلتفرم سرمایه‌گذاری کردین حتماً سرمایتون رو از اینجا خارج کنید.
#میلی
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143884" target="_blank">📅 14:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143883">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739904d208.mp4?token=qyq0UD7N-xMOSK-H7ISJpHuO_iUPdP3NQ-iX8GPorlvSAubhP5JayBK8fhziuDofcb1BK128FR24UtVqH2mQokA2dNlrRFA8E2SxkhPzLXTgj9v9VIoU3gK_QX16RsQOCzVzbvJ7C0cDWcH5E-4TM0BZZjbK9UydwbPwQUJnVn1oN1QHt7SDeD4lcJHO30-vUMSELOzmnp7viucx9kW1VC3m0TJ1DXiXsAO0nHt9uJwJtMDoGu6YICXFk5-VZi0Ohw7ZyW9f4v_Q5rH9c4ImAej-d0WD5rnDHHEHfe3WPMLgxLNGYYPkZf_Mpk8dcbg9mhJ--zCj6jJ8FpZFGp3qRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739904d208.mp4?token=qyq0UD7N-xMOSK-H7ISJpHuO_iUPdP3NQ-iX8GPorlvSAubhP5JayBK8fhziuDofcb1BK128FR24UtVqH2mQokA2dNlrRFA8E2SxkhPzLXTgj9v9VIoU3gK_QX16RsQOCzVzbvJ7C0cDWcH5E-4TM0BZZjbK9UydwbPwQUJnVn1oN1QHt7SDeD4lcJHO30-vUMSELOzmnp7viucx9kW1VC3m0TJ1DXiXsAO0nHt9uJwJtMDoGu6YICXFk5-VZi0Ohw7ZyW9f4v_Q5rH9c4ImAej-d0WD5rnDHHEHfe3WPMLgxLNGYYPkZf_Mpk8dcbg9mhJ--zCj6jJ8FpZFGp3qRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به نظر میاد اگه حجاب داشته باشید دیگه رقص توی خیابون مشکلی نداره
🔴
البته هرشب شاهد رقص پرچم و میله هستیم و اونم مشکلی نداره
✅
@AloNews
|</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/143883" target="_blank">📅 14:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143882">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XP0TYmwB9oiKIpDS5asKoETmMc6DrRaPIc39x1Wjpc1R4WAz7oAAnFYGSbFzSbhxqm2wNPb4Gh8PxejqeYSVI60ZQhxL2BaG4fdAcbxp8Wb5zAoAhDGPetF0vi5AmmMzdCsUa1JQ8jlC7VWr82bSIVpiyap0U9NJIql5Z76p5yCG6gvOTIroBfTSAsDxtwbjiImJgURqq6p6MPo8jtKm1U6-8WQogZZFPjFHCwmmNd_b7gGsexUO1uaMBsh-2RiWzKnLQEdThBvJ4Z1VrI7gEJKHKkvUfwJZaQyJSnIT8RUzGUV2Ku6bZiqN5zP7acPbeZEuKQWuVbJw6B0OrSgTlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
قالیباف: مذاکره با قاتلان رهبر برام افتخار نیست و برعکس برام خیلی سخت و امتحانی سنگینه
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/143882" target="_blank">📅 14:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143881">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 250 میلیون
‼️
🔴
دلار به زودی 210 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/143881" target="_blank">📅 14:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143880">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
رویترز:تحقیقات آمریکایی در مورد نفوذ به داده‌های مرتبط با ایران در یک شرکت که از ابزارهای آن برای تاسیسات آب استفاده می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/143880" target="_blank">📅 13:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143879">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b12f4aaba6.mp4?token=vz9cRlwRxF0lCYB_zA4MgYhKIS1tUcIDbsnKkzWlch9jYtl7uF0_7T2xwoGpk1SXgfyvHh36QE-RJYZyTnnfMBvYnlkkpOB-C16zh322zbvFQ1auOZ3HdjwZCZFtbhQpTnY9uK6lmhYnYMsH3HiE2esAP6w_vdSH5F_wpN1kGOHZHDYxlXRmyiQ9TnhLfOnKcXznEi7j6rcXy4Vxx1Ypf8tJyArlkj9osAqnp-LxnYJzky-Vk5UMO7JNk8kJLfVXRRw0A1FoObAsnWjlZzy4YspYp8uAgrbA--RKwLFyr3iIKrQMHGRJ9YwgnoiUvHNIGx3Uzkoz5iHYfVP6tFhg1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b12f4aaba6.mp4?token=vz9cRlwRxF0lCYB_zA4MgYhKIS1tUcIDbsnKkzWlch9jYtl7uF0_7T2xwoGpk1SXgfyvHh36QE-RJYZyTnnfMBvYnlkkpOB-C16zh322zbvFQ1auOZ3HdjwZCZFtbhQpTnY9uK6lmhYnYMsH3HiE2esAP6w_vdSH5F_wpN1kGOHZHDYxlXRmyiQ9TnhLfOnKcXznEi7j6rcXy4Vxx1Ypf8tJyArlkj9osAqnp-LxnYJzky-Vk5UMO7JNk8kJLfVXRRw0A1FoObAsnWjlZzy4YspYp8uAgrbA--RKwLFyr3iIKrQMHGRJ9YwgnoiUvHNIGx3Uzkoz5iHYfVP6tFhg1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یکی از حامیان حکومت: ارزش دلار هر روز داره بالاتر میره و پول ما بی ارزش میشه، اما این به نفع ماست!
🔴
اون فرد خارجی بیشتر محصولات مارو میخره، در نتیجه تولید بیشتر، بیکاری کمتر و تورم مهار میشه.
#کریه_المنظر
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143879" target="_blank">📅 13:50 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143878">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8a6f01648.mp4?token=g1xkRFe69V2UjlTXW1aWBdVqGkSY9-NsWxNqbedKJENF_i_gLyw1on57Q8GrDFZfM0evG_77vRaY4_zK9SSNiqCAIrPG3Kqx1EoqUEUp0FZHkjcIk9u3s2isz56j4UztqS4BcI6bjxSh3S7XmuGiwpINK1qmfwworruKJsz9irLzljCRbuewMArJNYjrGkmsWv3ve1WZoDaFZV5oa95H72kz9rN_3LxB88Tx-mtdptwiZTgl_g2Pp1LwfdwT0TEqblZfaXhDFN99rzZ3yI39Z6EzdDdmc7ydePnONBRSdIpDWHZgOXGtnEhPKEqAoQomt4RlrfwBYVhXu8eUgepKug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8a6f01648.mp4?token=g1xkRFe69V2UjlTXW1aWBdVqGkSY9-NsWxNqbedKJENF_i_gLyw1on57Q8GrDFZfM0evG_77vRaY4_zK9SSNiqCAIrPG3Kqx1EoqUEUp0FZHkjcIk9u3s2isz56j4UztqS4BcI6bjxSh3S7XmuGiwpINK1qmfwworruKJsz9irLzljCRbuewMArJNYjrGkmsWv3ve1WZoDaFZV5oa95H72kz9rN_3LxB88Tx-mtdptwiZTgl_g2Pp1LwfdwT0TEqblZfaXhDFN99rzZ3yI39Z6EzdDdmc7ydePnONBRSdIpDWHZgOXGtnEhPKEqAoQomt4RlrfwBYVhXu8eUgepKug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فریاد «مرگ بر آمریکا و مرگ بر اسرائیل» در نشست علنی امروز مجلس!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/143878" target="_blank">📅 13:46 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
