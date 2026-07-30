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
<img src="https://cdn4.telesco.pe/file/n9iJPeezaSCVqPqH72PRo_RSHDKX6w9IhrFcY2Pr2yLf3GmMYpBjtIcUTtUYnfUJOGVPs7Lw8F4Zk8Utn-vXKLmgZr84bTP1CgsTeYK9IztmZI0a_ffAJyIUOpP-5tIhbzSj6gMsYWAtT8JX9F-5mqyvDU02mbtIx1ehzrQ94mPho09S24qWjZKS-3vg-CYeAcI3qzm3F2c7UnWR_JaWYuq-P3UCalT9X7V2u9WYe2C7GaR86f_yCFHP9RDyCJ4v4monxygSP5CC5XZ7SahfQYadFXxTZU1JWT1ut74_N5JhbIPqvGW2X_FuRN81m47YD3SV4Y34vrEWmbKYkxd2VA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 224K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 10:58:31</div>
<hr>

<div class="tg-post" id="msg-81529">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یک منبع آمریکایی به شبکه "i24NEWS" گفت:
حمله شب گذشته گسترده بود و تأثیر قابل توجهی داشت. این حمله تقریباً دو برابر قوی‌تر و گسترده‌تر از عملیات‌های قبلی بود.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/funhiphop/81529" target="_blank">📅 10:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81528">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/funhiphop/81528" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81527">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/funhiphop/81527" target="_blank">📅 10:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81526">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/funhiphop/81526" target="_blank">📅 10:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81525">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kW0wuwx5wpxEj0qfFSrWPY--QIoL21plRkJs2TygsHFF2-btPN2dPlFPmIsbCO4QcdDhcOKqpcJGZcXhufTIrnF3VF9V75uNWeKQQKztADEPn5eaviv3anx86FIpzWmwcquvsQq4qJy1rI4YwUJA-1XU1n8-L2u8-TO208GFKs2k3GaT08sj1flILFN1kHDx_DSf-VObq5z8IeKasrvEtA7kzQrlALN3F-rjwH0WQy8hsbKu2xGl1nVBm_oAMLgUCiqxeC_DXafzYLFOSRaNCuRKZT0A-CuF0WIErBvkt9RixZ88I-ZGMT-RirIjDalpY1RqZ8wkTVvcssLdKglPAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کیرم تو این اکسپلورم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/funhiphop/81525" target="_blank">📅 08:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81524">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اینکه شب گذشته آمریکا مسکونی زده احتمال داره یه پیامی باشه برای ایران واسه جنگ های بعدی که احتمال داره رخ بده، که امیدوارم کصشر باشه و این برداشت صحت نداشته باشه. (اگرم انقدر اورانگوتانید که فکر میکنید آمریکا کصدسته و مختصات اشتباه به بمب و موشک داده و صرفا اسرائیل نقطه زنه نظر ندید کلا)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/funhiphop/81524" target="_blank">📅 08:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81523">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b757b219d.mp4?token=G360l9NnA7kOt7mjmSCdMQS4fh9Py5TukuhVCHfkyhs3kF4VfuZzH1ssnJn20gE-xCT3ZUVvYm6bCXHOLlDdfMWpoQk0SQ7GW6V_Otg6_GVih__V_hNW3Ks1Aiy9iJ4gRFcOL-71pt1viVjYO3qtg53HCttzGvG1kitpxX2WJYLoGsH7rLojHLm5KBoPG5O37JdOWXcJxxkoQDeuMkf--865QrGq_n9mJB2kwol_e7vq5dOPT2CKd1wsEg836m86cnlBH3Iq66n7DFah-4DheM7BGIN5xKiQD2kqaX5rSPGfOPkVo2OESbw5M8jMjmaBTGRbUP7TYrXmKeSxIZNiNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b757b219d.mp4?token=G360l9NnA7kOt7mjmSCdMQS4fh9Py5TukuhVCHfkyhs3kF4VfuZzH1ssnJn20gE-xCT3ZUVvYm6bCXHOLlDdfMWpoQk0SQ7GW6V_Otg6_GVih__V_hNW3Ks1Aiy9iJ4gRFcOL-71pt1viVjYO3qtg53HCttzGvG1kitpxX2WJYLoGsH7rLojHLm5KBoPG5O37JdOWXcJxxkoQDeuMkf--865QrGq_n9mJB2kwol_e7vq5dOPT2CKd1wsEg836m86cnlBH3Iq66n7DFah-4DheM7BGIN5xKiQD2kqaX5rSPGfOPkVo2OESbw5M8jMjmaBTGRbUP7TYrXmKeSxIZNiNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متاسفانه شب گذشته هم:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/funhiphop/81523" target="_blank">📅 06:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81522">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">نتانیاهو:
نمیدونم دیپلماسی چقدر ممکنه اتفاق بیفته، اما نسبت به شیوه رفتار ایران بدبین هستم.
اونا همیشه دروغ میگن، همیشه تقلب میکنن و همیشه برای خریدن زمان بازی میکنن.
آیا ممکنه این رفتار با اعمال فشار کافی، از جمله فشار دیپلماتیک و اقتصادی، تغییر کنه؟ باید این رو امتحان کرد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/funhiphop/81522" target="_blank">📅 06:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81521">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تسنیم:
برق برخی نقاط اهواز قطع شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/81521" target="_blank">📅 05:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81519">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">انفجار های پی در پی قشم و بوشهر و بندرعباس
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/81519" target="_blank">📅 03:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81518">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بوشهر آبادان کیش
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/81518" target="_blank">📅 03:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81516">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a76739cd9.mp4?token=DpwqODK1NbVAx-IgvX7hQyESAS2GjMoT1uhqdyCCGcbL0BbzeCo6FF9b3SJDhMFhmIV7pVtycJM40dGyvOfBWo0Ap6n7zqFWxRBtxka-Qc9P2-5LWCrxQmITDEhkBmC9iHb3Hn3tiT3jglKu71YAmQdnSSRp6Aw-jk09LaVtQxP23rNa3CV9Ch3RwC9ko4OFI0H4fabi1zitSnoJRY0QPWhR1fqIXGICtBSzgxPehwzNls_ERMqsJrmtkS1qpMW1fCZW7vAHNx4Gih8nVy3vPhIc5BEwDG9va01cw9Gdc5QIfHYPhPKOPl4nJqRiVzst-U5tfFEXltpF0bFa_J4m-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a76739cd9.mp4?token=DpwqODK1NbVAx-IgvX7hQyESAS2GjMoT1uhqdyCCGcbL0BbzeCo6FF9b3SJDhMFhmIV7pVtycJM40dGyvOfBWo0Ap6n7zqFWxRBtxka-Qc9P2-5LWCrxQmITDEhkBmC9iHb3Hn3tiT3jglKu71YAmQdnSSRp6Aw-jk09LaVtQxP23rNa3CV9Ch3RwC9ko4OFI0H4fabi1zitSnoJRY0QPWhR1fqIXGICtBSzgxPehwzNls_ERMqsJrmtkS1qpMW1fCZW7vAHNx4Gih8nVy3vPhIc5BEwDG9va01cw9Gdc5QIfHYPhPKOPl4nJqRiVzst-U5tfFEXltpF0bFa_J4m-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان مراسم اکبر عبدی، عادل فردوسی‌پور در کنار عباس صالحی وزیر فرهنگ و ارشاد جمهوری اسلامی نشسته بود میخواست دستشو ببوسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81516" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81515">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/81515" target="_blank">📅 02:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81514">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/81514" target="_blank">📅 02:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81513">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بابا کصخل بمب افکن نیست که رادار خاموش کنه، سوخت رسانه</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81513" target="_blank">📅 02:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81512">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بخواد بزنه ردیاب سوخت رسانا رو روشن میزاره که مهدی ادمین فان هیپ هاپ بفهمه؟</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81512" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81511">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حاج زدن حاج
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81511" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81510">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81510" target="_blank">📅 02:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81509">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کصخل سوخت رسانا بلند نشدن که باهم بندازن، بالاخره میزنه دیگه</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/81509" target="_blank">📅 02:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81508">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/81508" target="_blank">📅 02:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81507">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81507" target="_blank">📅 02:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81506">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فعلا چیزی جز صدای پدافند شنیده نشده به فیک نیوزا توجه نکنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81506" target="_blank">📅 01:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81505">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پست آدرویت تو چنلش: این روزا انقدر اتفاقای بد و عجیب میوفته تو ایران آدم نمید‌ونه از کدوم ناراحت باشه
🤧
🤐
🫤
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81505" target="_blank">📅 01:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81504">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81504" target="_blank">📅 00:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81503">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تنها اپی که سپاه و نیروهای نیابتیش میتونن آزادانه توش کار کنن تلگرامه</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81503" target="_blank">📅 00:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81502">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ این جواب سخت ما چیشد خوابمون میاد</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81502" target="_blank">📅 22:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81501">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNqPcpeb1nzfPHY8bMe0FDFCPDr3AaSfvAuf7Nqt86-3BHPefiCx2V54jUSGzu2Xownfo5RORTObsQDG_Jy1kkWk7UbMu1qXVvvx0_PqsfSWblQXD_UtF_kMkzwcL8mghVr6NF5QAOU70mFjCpifk2Fg3cAJBLLmVt_XIM8Ezyk84MnF8yF_KWcee7vVgKejanVSM4GQXf1KMZi953bU3KyASZxazEno3hlUrEmTbHdBUy6cBkC3yvOtxAW1e59p0EMp7zLScX2ESUSexqtKBpnr-jLPLr17eZLECtHfHi-HjTi5v83W3KCdT9Y5DKdPnPJ1a1RrbFtxpgX_oTCidA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برا دزد شدنم ۲۵۰ میلیون سرمایه اولیه نیازه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81501" target="_blank">📅 22:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81500">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oA0LdfWtcOWofz9t6dl2wvbiKpAdWBtqC1V6E1NnWMvJlxOUdaQk9onYdr1iFYgE_YuWNj8OYmsOFKYmJXEThYh8Hrlvzd74ksn4SdIungyGRTokSg9yWP67jGuLoumgxMdZHkQhsdLigViwEBYeDEx71H2bSTzQ_ftdhwx0sJvwTQn1aOec-odivSB4u1408f-eh3DdiyN5eVx2O9sftX_bRh3bCD5JRYoTb_PiQ6iNHJqaKUhtuZgSYrW_fLeYp0iVF2gALA1YQuVvwB-LmzhrI9PeLbxFO0bONhsKwvQeZ4HonXBnp2RK0vIc93jz_0DE4icAPcHDvaqsL7A7Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
با نایت موویز، دیگه سینما همیشه تو جیبته!
😍
دیگه نیازی نیست اشتراک بخری برای تماشا و دانلود فیلم و سریال!
🤖
تازه نایت موویز یه دستیار هوشمند هم داره که بهت فیلم و سریال معرفی میکنه :)
💵
با خرید اشتراک خداحافظی کن و به نایت موویز سلام کن
👇
❤️
🍿
@NightMoviezBot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81500" target="_blank">📅 22:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81499">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نتانیاهو امروز با رضا پهلوی دیدار داشته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81499" target="_blank">📅 21:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81497">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nW0xd9nO0r9iLXlUi8GP0RRtGCEBYN9cBRnJWvJz8dgVbCaFTuOd3vnia76scnCx8SEJ_54r6masZxg9MG0vaXk45F7cwMR5CxRzX55w1d9OVEN2d4aV1YFcih0KfItRndyVxRn1_TdYGupE_S--dh6pAJnfzVZl9f68GjQaGu6BH1I1LascjESzpq6lOSsyZwv3z478kfyX14D7j20KBLjXAXZwADIxuLh4-sGKSm-otRpC9ub1CC5DAhDK3f-LDACzqOWTEkuWggjt6Sm0I0tmVx1BCcqT0L3QiotI_ar3fo74AJbDVYl0_rxjfFqheLCY0olj4SfxX-jMnBRm_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام چه بامزس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81497" target="_blank">📅 20:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81495">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5U1AWsJV8O0UnSGSfpL-cW4MyEYWvQ0zUlEvXU8XUn6XMO5rGXuLIq5-SY94T6mcDEtS1Vxgm4gMzGO9uAyRImBJjxtD0kOse4nnWG07W3KwN1OucSuqlW1xt2PwsqoLnSiqVBLiIO1Pv5pZJyqyTpSSsBwKI4iXYwBnYNUS7c0FSGeUdEaWEYv4v_qrpIaOcOAWwJs2t84vZVMz6jEagbsDKZB9kNFO70ifklHOxztXu1jCMFficMc4XJXov05R9ZoQwnUx_ChpftwMXHWdfvKo8zFXUK9B368kn0IOJae15c3-XGIbBO2VVnuC2H_cuZySKsdS847lncREfDX4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی بچه اش رو دوماه زودتر بدنیا اورده با عمل که فقط تاریخ تولدش روز رند بخوره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81495" target="_blank">📅 20:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81494">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3Loqm4APOojIJnZASYZV6yKJlbZs84qgdX_KpEzEEFjYiLDuJAc9CERTGmbOJABTRePFFnnyVGkGko88I9cGcbxfv-sBkjHcDXF4rE3jlalPY5oKCFARZB8BCAEXdW-kjGCmhDcENMWO27_sSppqD63y6kIAQLUqrAPUUkIIeEmzLFQ1D_aHQ1gO_jtI_ki2Cc5MsaAdgIJahBNEsQZW2reut27uPQXNP5V44yxt8Kw5uMYI2UNqq_WeDmzw_PDzN_4gJNV9a5829X89i6e-qVJu2D-RKJh5T7-eZKSJwxPbgjwfPOOS0ItYaEq-Tiakk5s7aOz516vlKWFMkeeWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوتیسم پسر کوکوریا عود کرده، بخاطر همین دیکه موی بلند جواب نیست و باید ببافه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81494" target="_blank">📅 20:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81493">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پرایم هیچ بازیکنی اندازه رافینیا ۲۰۲۴ بهم نچسبید</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81493" target="_blank">📅 20:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81491">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">از وقتی تلاش نکردم برا باز کردن پیچ خوردگیا هندزفری سیمی کیر رفت تو زندگیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81491" target="_blank">📅 20:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81490">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پول ایرپاد نداره؟</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81490" target="_blank">📅 20:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81488">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IQ6-mPoDPewPVkqd9F9vzbFG_gkVEusrt2KV_HfJ-ryWGMAE3qjCugkc2pKD5gTqd8zSGexLhC5dAqTmTfD3qcPiNGEQCuX8Q-9Ep5I3C-1O5BNUuqhDhx9HouCH3ishWfi_TxqYxoMcROvZy9V6C5kmXf103Ll3XxMqliMGxSKyjNCcYD7bo52yCQ5mCVoQFAF9EbKcn3By8OHMAy6wT4kkrDxliFYOZfae944XR9546JZLSuEYaIRDhdnSMoPDMZdE5K9BnyRkEaYFIjgC16l1l-R9MYut9FwDGC33miEnniamxbGG1BGfvY2T0M-oKyuj7CQVFuCZd3mRMmrcew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SxS_dT6odrAuJRoQbGchPZgJKtVj4x7ZMSmVDtjUiKsbkRQg_pdPjlwa4dY-B7L8nttPV7TQajPUO3SrfzFY6Md8tjQjsCxIBvE1jPmlXGgxGeeiiV5SLpD7KOe9ML5YVNgctW-esUW4JD6WG6ae3GHve6u2aZHHd30GqU2FaSPIrwVw8ubQAf-J3tDWSsr4JdRJnAkJ3smpq0_RGrvyOFTicgnWCT0sGvJAvSstORo_--O58K6cKyEqD0w6VmgFAeFxSujEoMWn0Qahb7uxBc25ynFMHzPHwxzyvKSe5V6Vu5xAhv3zeYQAnL16vXLW-kLyK3m3PwdZrEwWfDpAiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رافینیا شبیه زن جنده ها شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81488" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81486">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/awAj1AkdhJROYp_c2-KC-whHXQAqah_-LIui5Y3eO6KeicrMyxtY2BQoBjvmxqmvlCwZhIB73Pbihx28-esbrKeIFsFDyOMqg9HWWp5XpA-XntPKPvvfNB_ppfL2a75ol150wi8XWatfYT1Wp0_nC1uF4WbeS-ApK25GW8bMUEthwsHFK7OUr3pA9zFwgMmweWjPRquBZhEKBp5thHIDGTGKnqNa7hsTBh9yKoM3xfYj7FvlzFctzSsHDE-QUSokoLdX_ZrRiFkWnn10gxhE9fJmUjaSyOs_vX4bicnMTwIWxVTbdVi2YxFVwl7HRj1LNGsCP_wLLhavolkB85Huyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n26owryElAWEv137zE2igws0h2xvqBlN5aYwVyKj45s6QPkzS3cBY2CB-m8cmRmncFzkLCHRkjle7Gyao3pNYphVxvqh37TdaP9xFcKFlL1XpAIlCAjVkrg3fnKXmHTB4O9rzZfPPrGcYRSBjiXlMprotV-duQDkeKuTo5qo0p95Jxam75PJiaiohCcBudZJP9TXzRYxRumSX8xoW_ueEDayjfSoITDbMqKSW1LNj3cREvegJSQoWMtd9Ai2UK3DrTvb_iC3ai36sB1lxMr7ExsshYvpFGLY4Kv51NPRyMR_sC4123OKsvbD4Wqeg9Yvs0BDc7_zM2HzQfEyTpz2sg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هرکاری میکنم نمیتونم با قیافه جدید وینیسیوس کنار بیام.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81486" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81485">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnZ14VSz4wZuUDQUhun3sR-141FYZZDiV2-tsTGXOEcy4_EcKkFV5ENWFeLh-7IQcunWafbIj1ZBLxSrSdGlUut1ltxqcImDqpfMczBL0-AMafrHHOo9jizVWoJ6GZPUgKwNzFfavj_tCS0JSN1TGocn_z8ZR5G8OlwKGtJD1Ite05ORC5Y2UYzqJc2lgDXO2ncyqLUu78PBVJZsK-x5rbkBwZP2FZV0R3-Rx3fDgITDHa2AoJn2G-v9PoUPpIog4zYUnCFHZa9-Ms-MUijDwqhIXTwVKwEwaA35Iw_GgopGvS_Inm3a4SdjKc-Z44xe03L9SczC9DX7MBhgNmVZBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی بگم والا.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81485" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81484">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixCpPs9tUIT-yO5zQLzHOs5t-HS8uxkaIYxeqFRtIjZZxX1zlQCmDctTqffry0Dw-TmdxkH3jJZMW3FVWQiA4wB15sxSUAAtruwqoH3rXyqCPxt3D3pxCrqQ-ESxsJ5uas52rw--j83y6scJg7uTJ_dPWC2UVKPRzNZaoTFW2VIMBR5rlnVmCxJ-AsBws6xxjbqNpUlVr0IrfaIfIX8lRBehe8Xk-1SPdWbu3RmfmWYgPcpoTnA_EGB3wrXJ3q1aNtsO5LB9A83J4Y1CM2welKjj_kwjbeEFzgTcrPW8qTWAkkzba8CsIzuwjXw210rfV0QgYCwLtjuI9qTlGoYL_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اتلتیکو مادرید
🇪🇸
-
🇪🇸
ختافه
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
چهارشنبه ساعت ۱۹:۰۰
🏟
ورزشگاه سرو دل اسپینو
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اتلتیکو مادرید در ۶ بازی اخیر خود مساوی نکرده است.
✅
ختافه در ۴ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر اتلتیکو مادرید ۳ گل در هر بازی بوده است.
🧠
تحلیل خوب، آغاز خوش‌شانسی است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r7
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81484" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81483">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNcjxp0kpsHPiXasCclFnz8gqZyhxze3ct0jVBqhfppxaCXu2dTD6HqFNBD0dqwjxklp_ltviM_UkUEykmU7XfkZz9rSS7mJ0QW8ma4qd3Fm5y2KoDHAr4rNtBtIPwCu5GzUHa7ycGa66DNN21Ccz0dGzsw11LeOLSc0Xumt-EZd7iR_km3upbt-av9LjynMbFVTPWGw_W-4QwlPRUiIShu7WcjfCF_k2W8sXGtu9HnXKbZBMyjtkXhFKEyO0PVArWZw5SRwHN1uk3o4ytiZPPgLKHCBByqVCLXqSS766nQaiJQT-HlPblkJEHrzRN94YZ6z7J38iBQmNj_PvrZ2XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس جدید صابر‌ ابر و دوست پسرش.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81483" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81482">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSke61ZsLbo-PVjV_a7YjGN1TFnP-dCD36xIaKafIRWxlNnUJK5lgtDJVqzaPuFpm90UklAtOE4Af0V2IJTYGkTMIhfR0c-ksH4qsLTYPSQ2JOsUxMN3j2rpzFiLXoPazC5gc8CsAsOLdg3oq8enNi1SdbOjxg8vd-yP79ypyRJzTnchLItP4l--HbqZrLJIwrHRaetYoCO8BlOX6RxxV8tjP_Kan7T3oTudtPmtICSish7dpIs_O_HI2VL6eLzqntxL1q9TUT7WSsyvTYsYL4KMxhMFwF1aQV7_Pg0Ty2flgRZEBsQcJb4MszwmOF4KGa53kSpmd_XuvuilRaultA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفایل پاول تو تلگرام:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81482" target="_blank">📅 18:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81481">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jojmvhttiFgqrOLWC8KOpj08GFZtrWHN-8K0JTm5Y_BiuH6HEEluALbn8JU_ovHJ69SBRp3KWKp76ef9wcRfM2pYe4c8vFWJq412DXizt-mNcPBUoAi3IRn6Yyy6qxv-w9uWrAjfkwEdy1byLWXBRNpNHlA1wicJ0_JWSqNhI0SHEaCx9XoQq6BxjSuBbcGxSJpR0hHwJNW00PIpRbnMDHIUOjPoU2HzTkUTz47w1d_qRPEWAnR_pMsji101IaOF5p20gaajEoQzZzH57FvfGeZZ6znbxQ5vwgXk1g5wvhyLFfDcmkPDWosl5WADyLFutleoXzTKDe6qS3XvFn7Ohw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش دورف:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81481" target="_blank">📅 17:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81480">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81480" target="_blank">📅 17:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81479">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3Xwk40MTgLfEzD059NwXld2OmhlgjUTQhOGD34riOyMcN2aWzAJbJnqkK-ek7jYq_AWWHAjEKjrhaWesgzU52T7J6WyQ_9rnag4UdvqxEIcRE-1mmeGv4Ve7XYdsKCQDNfZSFsp_R96Ae4LSZpxuj4OOuxqbAiF6ikH-Qvqhn6jzYlY8iIGSYegqjAZ3kQF9gg370BfZv7h4NeayrJKnvJ8wpuir4W4fjUgW3DdTVJPOxD58p_cteKzZKQxDzDQHxuBFdMS4hZcOrfwOHUfC0q82afiw9yenBZ3Lq1cD_vLKzbGTe2KsxT2erna6hFDfwnXd-U01vg5CrahJJCKVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81479" target="_blank">📅 17:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81478">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjiosP2WRMp59ldpLdCMJJU9udVvRbsZNNUg4nwtCS7U57iy_0OALYY0Z-Os03E84C7YtfnFHYaB_8ZmT8gfjxy1ioMSXxgb6J1u34RsITH0buYnB-2I758beDatuNjmuZq6es86uYQYAT-OlEe0DsxzMbmjvO0dG_7FMTldtL7z83YjdL2jRSjehMBrpKD63cl_FO7JFyJqy-90LlLi3yGRk143P0-1WCQFexwAPPrcmQhngThCQ1mmIO8qjz4KLdr7HcvRlXdAO9KnJwHv8MvzmnUiXDsFNyBnFudDMU0wqSQOYe-KaIdHSrDufzR87e4V9-80Rjuvp8U_7GXvTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81478" target="_blank">📅 16:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81477">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ: ضربه سختی به ایران خواهیم زد‌‌.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81477" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81476">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">منابع نزدیک به سپاه میگن در نتیجه حملات دیشب عربستان و آمریکا در عراق، تا این لحظه دست کم ۵نیروی ارشد حفاظت اطلاعات سپاه کشته شدند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81476" target="_blank">📅 15:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81475">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81475" target="_blank">📅 15:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81474">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81474" target="_blank">📅 15:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81472">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XX0Rc3WsYfv3qWo4xxGlgIyUdLowrjBJ6ucRctFbbQLBynTA_lBMLQp3bvMWznFX2rgNgNXg3AA3_DnxESZmjme0HnnK0_QdwoJ4DpCsZfggytwlO4Q2Z3OBo5xKN7xHpudE9KLgwGyk3W5Ryfroyso45imWUnMwSbvpragqcyKF2VcmEMDbKYK9WBGCUy2H2mHSldT1SMybHKnkmoQBjR6lCtntKvfFFClJ8HShLCdZqaexP7QYSsXho2TgsstorVQHJmGz7Hyk6H0OcQq2MljqW5k2T9zQFv9KCJCmshprUAJ6VlnfXgaseS0L234JLilhwv3zMcOyjuNjE7uaoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس نمیدونه چرا این پست انقدر ری اکشن "
🤣
" میگیره.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81472" target="_blank">📅 14:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81470">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nvJgj3IBGVjo88fX1afMSiLp0fU8yi-tSZEM1bY1KtnnDNI274fYkUz5z7UNteijMy3IFeeJ0Skp_3_yg3xg837l28sdBxQhBmM2GCZYAJghohXdpUXuQWWH6WorNy1jCqqaK405LO1h8aazgRAf8OEMlkLSUNl1_EnuhUMP27VPKrIDFNOo90fWIrtDRAzRD-xxF2ybaB1ETe6Cg3NeX2k7eWMH00T7mVooDetm92CDpsxtm25FHxi7xBPsnLUzcS-phdzhPwlRIl9RxVOFf2HrzcN8JfLkfu_fW_uiCiUbeQpOTKVeIaXeIvfbjkKllmgcMcZvBPmU2gq-OtSxfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLKQqx8C7eQe790u_Bf1g4AJ16E4GYpbWs5XaGfHcUTZsC56Yb6R8UGYfdktduV53yOORk4OXLvOULrdiuqvDeH6lm1l8xnZGoVv3XqImBD4GbgoHQNpUwbPid0wIYj9bYTNmSv7xHXxdV9QC4jaD3694QUqgFuf_-eTN_ucGThPvSusrXTYHu7fnzuAcQklPqoZUjXLgBOIBNM87MInHzSFi96ryiERR9wQXwrJURdnHfPKIDheovfDQxJa6ZbqnHBDtB6cAOQL7XxvBrotD9SasVgHM-Vcm0onRf7KGHuEj7H1ByiizovN3dheJeaM5Z9FXGv3bQFf4F57Jwl5cw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پینترست چرا تبدیل به کرج شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81470" target="_blank">📅 14:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81465">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اگه این با سپاه همکاری میکرد که الان همه تو صف اعدام بودیم</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81465" target="_blank">📅 13:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81464">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81464" target="_blank">📅 13:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81463">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دلار 193
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81463" target="_blank">📅 13:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81462">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPHkbTSgWJxJhjjxGFukarE2ZvpZeF9OB8vIjsTk4leCxFyHVKoB8CoKY1-ZaqRTLCLUrccGT8jT7Nr6BCDYCQ3xSg8_wBbdi9rqbaMDfnW0nKZ7cZcZRzZzfxkmjCGfkBjCOMHmwgFLvuS1bKR9Z39Mc_I4C6XUDKsqu49d_YGdrAIJFpam8iV9c8MDJ60dkNP5532h4QIi2rRZQAQYcuGqj9UlchbQCQ_7Nr0ES_emR1p_icCZKsgRSbOohSfHUD6ZtTyYLB6KMoXqlCrRw4PrlCQGMNkeZNBVHaT_ouC_ARrL4z_pangEe36cWxGBv3qDrAJATfurAfxfwuGfqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پیشرو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81462" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81461">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkV5ihIGOtoCJQRBSPivlPWM7CdackJTc9mJmDXVb7UIXYvqtpdOj-XZk3h_ExsL9nOuecw41H3KOXXvvhaTVrYX4BAPaRqbiazxXKD8uGsnO6epebvj4WKP51cJTpk3D1iWey6BYRQ1XZr311LWTzZs44cNHg6WPwBUmu3r6QJj6iObFfgeySo7Qa1DKZsJjTfD6E2OJO-AADM0PWFYuam_iqA8H9CGRot_jLf4aEqrxC-xp722xc6rlUkQXQRKi-FBBTlls_0xNQy7OexjRi4w1DNCjqoMN7GvIXKUVNTbNrnkMR5ft-7Y2S4maw1gG6fTb9R73_A7TyPIfK_6pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اتلتیکو مادرید
🇪🇸
-
🇪🇸
ختافه
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
چهارشنبه ساعت ۱۹:۰۰
🏟
ورزشگاه سرو دل اسپینو
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اتلتیکو مادرید در ۶ بازی اخیر خود مساوی نکرده است.
✅
ختافه در ۴ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر اتلتیکو مادرید ۳ گل در هر بازی بوده است.
🧠
تحلیل خوب، آغاز خوش‌شانسی است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r7
💻
@BetForward</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81461" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81460">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">از الان تا ۶ سال آینده هر اتفاقی بیوفته ربطش میدیم به جلد مجله اکونومیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81460" target="_blank">📅 12:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81458">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هدف یدونه پایگاه آمریکا تو اردن بود فقط
💔
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/funhiphop/81458" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81457">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تروخدا اسرائیل باشه تروخدا این یهودا خیلی راحت نابود می‌‌شن بوم بوم تلاویو اسرائیلی‌ها مجبور می‌شن از دریا فرار کنن تروخدا پدافنداشون ته کشیده ۸۵۸۷۴۳۹۹۴۴ نفر ازشون مفقود می‌شه کلا اندازه یه استان ایرانن ۹ میلیون جمعیت دارن کلا تروخدا تروخدا اسرائیلو بزن سردار
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/funhiphop/81457" target="_blank">📅 01:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81456">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ببینیم از لپ لپ اسم کدوم کشور درمیاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/funhiphop/81456" target="_blank">📅 01:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81454">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJ3mHqdEtsI4cRFh-OHHFa5TzQvm6-CMUpIFuwtrB72soqlajHBYdNiuPpAn0Kg2I4l5sekP0awUq6Prfg82lgJvP_juo31RtHN3jsx36ilM2Lh2GVaEgksimVXi82eMMzjeEaOv5zPv8cvjt5oCCwBeUAM8-qrcUmR_k45cnX2ACs_MhbT1e2i37O_WpDkHAymdvdeFdrYMt1tSS-VLwF1Se5ZS8tCL0BpozcF-ONdVwo8L-rlf0eecvOvV4mD_dXvMA_qBvDC0aKpLLlaK3oSeXO8dCpDNVSJAWW1ZxJH1cr0m6X9N7syuQEf0iy1qqavt6V4k985VN7aKwi0p4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/funhiphop/81454" target="_blank">📅 00:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81453">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyzY_GN13oGA6fwwllBYgBQIVojkpJY10XsGoFFM2tjgaW8r8mSnT6H_8iVXT6mNw_-Qg-862flA40dnO0uNdcYbxFkQP2UlAoqPbL8MHY02bvwR7yjl63QKfuymm5qJSURuVBeuFq50Y2Sz8v4y0Xx7U3kO1-T0b-RP8peqkQi8hrVWi9kWGgXRywSsP0b2-2UghOhzDSujoR519J0KiqwacHfK6cd2VNis367E1OML1xTKe0IYTL7kB8rWasRImeAPqD4RDZQ_QmuskgHw0JnKMp7u9-HMaRDvtoxc5DfC2SIQHeJ5Q9Cd4bwlwMVSKfxzbHi-_5lmWLUolKCmUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم" تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/81453" target="_blank">📅 00:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81452">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrS9pwvPfWN59t-HKbKWptNBsZu0nBucMdwX1BBB7iWvcXzLepp2YHbzS5h-Sbj2k3OjV1cUitKi0BcAGWnkQUkna83rPC901zn_PtpxazBIYGi6MXKuP2Jq1iZJHsFrwPxG-vsVdaQe5DXo2KVnk2zBfNqfduCRLbCHDIjacoQcwtsR-T3No00LxRYRd3QeBTJ6ubSIMG87twuD3cvTW2yUsm-ibsEmNwtAKfGLp7zdQ8gwi3PQnrsV4981cCnWiVVqqo_lBHyuO2W1XuaxH0XJLxhr5wQZdqF1d_b9tGW7zw707BBGhCFPRGJ6K7usMktrr7nCeqSvPuv5RO1sbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم"
تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/funhiphop/81452" target="_blank">📅 00:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81451">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">#رسمی
داریوش ترک کردهههه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81451" target="_blank">📅 00:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81450">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6Z3v5ZSPG_FhnobkgF78eOF5_i_satohpVZCCgA4BcaGPEWTuG1oGErcO5xUrZJ7iNKF98tdxMYltcmD5J5F8s0ldR3wP4CfWhly5nLq_jJGXPBVxtBt09SWA7_MHOujPmS1ZD1cA4zf25UtA0FSBlOF2Xr052GXdAP8waVrYin8bcbeTdbHzbIyQie2c3Ny6lNoPpBv2vC6tpWcP9tSLHTBKo6RwanbUsItXsPQVc5rbE5Po84mqNitj3GZnGkjNnjtuRx73aaRPbifE7-O5jhv26TZ4hH7DI_NUzqy4Dn7FA7XjC3xAnE9KIU1Ckd-Aek-JZ1yxGGpCX0YILk5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور شاهزاده رضا پهلوی در مراسم یادبود لیندزی گراهام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81450" target="_blank">📅 00:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81449">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یعنی جدی عملکرد ترامپ رو تو اوردن نفت از ۱۲۰ دلار به ۷۵ دلار تو دوماه ببینی و باز از گرونی نفت بعنوان یه موفقیت حرف بزنی نیازمند خیلی کصخل بودنه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81449" target="_blank">📅 23:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81448">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jARsW1CYH3iVIPBdVSpuW8pjLdmevOjKv-_o3jzRorfcIF-km6SnQ4hggKKhilZ8UpfoDCc99Jw0MxDscifQkzJ4O3aYbu7hVdAKVJzZrk1QEX4y_Q_wrZ-go9qIjJPgrD-W8AZRsOsknhwCFvGJQYYRkhydCSbPjCWK1aNChCFKuaJNFtED3PVgbA_ACmraKBz1hjzp6ZyjVgTriKi7nuwBNTgiUT07UW7sxUNcG_-t63ZvUy8dnkBAFlWd16TY0vQcmFRf9TaqKIQtGeoS-kywe6TKSzk7iFAqvinLf6IFyjZGJanvWr3E8lAeSO1J7j7J-91IDd0t-I3Ss51p6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا سکته کرده، اما اعلام کرده که حالش خوبه.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81448" target="_blank">📅 23:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81447">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">قالیباف: دنبال بهتر کردن
زندگی
مردم هستیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81447" target="_blank">📅 22:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81446">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gR2qHbEHO340_Al2Dn2W4eRMyl3G0oqQEZSGc4pvxsKnbnNxDUr5APphJtuiadJ9y-kxwRalck8Jg7KdPizGtq3k0wDGPadt-S_fDlShC05KLT4g4qwEn0mOw8YeolC3UFFAUil4b33NYcxKqC9AD8enboK3va3ELRPhqr9kjLZBavk4GrEMByPh0l6FcSECWutILpR9tZHxS0hwOS_cYV2vqfOaNaFGYopjDJo_BdRKCJJRbqBUZ-WAqAVBMForUdro-4qwGwq6oGXE5f2nKf8BumyS_edJXlisrhAu1-rxTyYIK3n5lGHdgfBLiiUvDef_ydmd15GnB2fBseY0GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعفری دوباره منیجر حصین شده، هم پرایم حصین هم شایع با جعفری بود، با هر کدوم قطع همکاری کرد بگا رفتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81446" target="_blank">📅 22:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81445">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromApexNet Shop | اپکس نت شاپ</strong></div>
<div class="tg-text">🏳
سرور مولتی لوکیشن ویتوری موجود شد
💎
🟣
لیست قیمت سرور ها
⬇️
🟡
سرور 10g - کاربر نامحدود 90 روزه - 45000 تومان
🟡
سرور 20g - کاربر نامحدود 90 روزه - 95000 تومان
🟡
سرور 30g - کاربر نامحدود 90 روزه - 135000 تومان
🟡
سرور 50g - کاربر نامحدود 90 روزه - 225000 تومان
🟡
سرور 80g - کاربر نامحدود 90 روزه - 360000 تومان
🟡
سرور 100g - کاربر نامحدود 90 روزه - 430000 تومان
🟣
همچنین سرور تست موجوده حتما قبل خرید از ربات سرور تست دریافت‌ کنید و بعد اگر راضی بودید خرید کنید
✅
🟣
برای خرید از ربات زیر استفاده کنید
⬇️
🤖
@ApexNetShop_bot
🟣
برای ارتباط با پشتیبانی و مشاوره با آیدی زیر در ارتباط باشید
✅
👨‍💻
@mehdi_splus</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81445" target="_blank">📅 22:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81443">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DYNx5lDqJpl6fa60COrdkHYMhn-HAqy9iW3_PjFApP8PI2wes4qVKneTAlcB_3hWp0InF8f-wttMk5J9GPQYPAudzKVdSesYEYbxMcrG76LZq85zx7NAZnC-prVmTB9vHvBOqBvfYT6W2gNPaQGEb5y1zAcQNdQhGydtXCsGPVrbNacm84JcVsIiwyGI3ARI5tRlvbjchjyWnSYCaNVX_1V7L5KgaM9lhirdPfRFF4cGJiLAB-5Ve5RAm8ly_MF5Dy_cjbkSplq7UGcsbb60ikFTbQ9qCj2JvLDDwnNId88XR3o6XbxtJDls0n-YQ9ymL_PF5uhwMaNbiwxxWiFUdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pnSVeHxBtNWQKUFnw1OAAfUpa2y4AuuVIKsf0Mrlak3eebjPM0EKtfZivn6xq2T3DdDd4JZYdg8GlxzSNB6uHWRuH1zmNtCOpEnqZA7DR0iQ6lwLUkPvCnyUdLVup35fmKlLcsO7TufKViLZ2vZITptnoJr7e0d2-DgmyXF9N-Hx9YGqzcD_emIOf1-qLGlo8VkZy5Rmcw6FWbMkubMZvutN_U0duRHyW162XaFuJT5ys-bvYg7THHnPRC4M-zoGbjx8pZtbS-y6xxdvi8j6WJOu5qOo3xPQz2etGrQ8kHAvbGXLDqmKmL7akDC11YhOBWVYW-3xbmF_Jv368c_oTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استوری های نوید و بامداد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81443" target="_blank">📅 22:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81442">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5beb4b7c70.mp4?token=hn1_Gzg8wRKbURVMlRIR_vA0f3rYyBOTx-i6S6FKfoESs6XAAkJpv_K-YMpktB28g74dH2lKvYG4jK2mvx0c5BTat9XHgHOOSRgUxKdA5v4mvplbDxzaKzLxuH8LrmDme2Fn2xdaQP8dFybQDyoh3j8cnDB8OuU9YSTblcsSvJnLcVlrZu7tXJ3yg_DWgW-wwQ5WHbPB9PV9WwC_pdef71H5EgTmZQzA6C1aUdnkvh19iuPyE6xxxzq86zv1xC_aTU4mszAj53iVCIpmQ1zw_3DLuMgjZEww1c7Wtycp6t1_YkFdpUK0YEXKvBLgxEjXY-hXz4Tsyb3ADaYKOtFasQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5beb4b7c70.mp4?token=hn1_Gzg8wRKbURVMlRIR_vA0f3rYyBOTx-i6S6FKfoESs6XAAkJpv_K-YMpktB28g74dH2lKvYG4jK2mvx0c5BTat9XHgHOOSRgUxKdA5v4mvplbDxzaKzLxuH8LrmDme2Fn2xdaQP8dFybQDyoh3j8cnDB8OuU9YSTblcsSvJnLcVlrZu7tXJ3yg_DWgW-wwQ5WHbPB9PV9WwC_pdef71H5EgTmZQzA6C1aUdnkvh19iuPyE6xxxzq86zv1xC_aTU4mszAj53iVCIpmQ1zw_3DLuMgjZEww1c7Wtycp6t1_YkFdpUK0YEXKvBLgxEjXY-hXz4Tsyb3ADaYKOtFasQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهوی جنایتکار کودک‌کش تروریست صهیون:
آقا جلسه‌ی خیلی خفنی با ترامپ داشتیم، وقتی می‌گم خیلی خفن یعنی خیلی خفن دیگه، ما تقریبا سر همه برنامه‌ها و اهدافمون به اشتراک رسیدیم، از جمله همینکه ترامپ مارو پاره کرده که ایران سلاح هسته‌ای نخواهد داشت و یه سری چیزای دیگه که من گفتم و جاش نیست اینجا بگم زشته جلو جمع.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81442" target="_blank">📅 21:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81440">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SIJ9ZvJTIBeA_ghYBD9polOwmf2tc7JHb0DqpNH-EQc-Ec3e-gVb_2PDBDmDU_zHHwoChVLdoLWpKXyBj54ILZmR5zb1VbuRfM7jMyK-wyk2EjTZW1p4sxMn5ALuXlmiUpeC2hPrADxy78RLIg2awtEa1jn_VWXGC-S0NZVfAn4ldYA5IocscVDdDo9K2Oz5rmyPkfCEbtFYhlZrc4_60SidyEdDzvHVHg2aXRzfwFI6SOHsnINI5vcWYI8oChANndk9No8QkmRVWDy5ugu7vi1V8g6SVbgxcNsJRWNICFQOkzwokoiayACXUgrvNqm1mUYDfdZnRJKZQx-HsHquoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rZ1A_z2Wl9CHFURtCC2dtYn7l-sOZrgzW46sOiRJq4oY5k80TtAaPyRVp9tRBSvP8nNERtSvmJqiknTVeOS7Qwh28mZzODh2Ha0WvFrSFCEyPY15fuarI4zcWpaeKJgN-0-mrrQde4V2BhTEWOOePqk_MjtfLJ4gnnbgYfodnBAKdnJwQj02XPdWqmYNPQxFlxSE2ADuEDrzvC5g-RYYT7TH9cuEFtQiw5H9iNwSN7-tc4RtLIrH5hJb-eN6SUwHjJQ75iOdU9xtG-J7zQmx6oHCNsJnPalFybrd0RCgJYiSCaxbifw-4jmdhE_biJnKyM6h7PF_ezQmMO7_bU2ejA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کوکوریا قیافه دلافوئنته رو تتو کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81440" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81439">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOaV8L5IfBqLRvkwS42msecQx_hiuk3t4Np1T1U1HzxyYipJRNGTWrLZEy9MOCbU4Ap6Dpu_mpBfo5YenwLhvVfKP7Ev5E7SI8P0nXTNDKzrDHi7JwNj02EJMsZtlboLFsIYz2Q_eHAYfSZNd7MzRxzzy5oq3sWaqt0VDXuP6wBdR1xXhTh7Mvm6q2JdARvTyUYZDR4Jo7G9AtrWwBAQ7p1DNMzC3SP-XZtyfQ4gPQEu1scXpkU5fP4jCPYDS-xWDNT67z9fX60xCAJQuaDakNKyDscZVziJFkBmiwTXMgB0qpUvM36aLo2kRr6Iq6F0Yl6_peIdnkBUgl2M33VREw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماممممممممم
😂
🤣
🤣
با هوش مصنوعی فیلم سوپر زن رونالدو رو  درست  کردن  اصلا ببینید پشماتون‌میریزه
🔞
یجوری داره میده انگار  ۲۰ ساله توی پورن هاب داره کار میکنه دهن سرویس
😂
😂
ویدئوش رو اپلود کردیم بات برید ببینید بدردتون میخوره اخر شبی
تماشای  ویدئو کامل
https://t.me/CONFINGMeliShkn_bot?start=3126b54d70f9</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81439" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81438">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بعد از اتفاقات دیشب شماره مادر سام صابری رو گیر اوردن براش فیلم سر بریدن فرستادن گفتن سر سام رو داریم میبریم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81438" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81437">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">شاهزاده قراره با بی‌بی نتانیاهو در مراسم ختم سناتور لیندسی گراهام دیدار داشته باشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81437" target="_blank">📅 20:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81436">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUdRbCAAL2IPgU2WkVkAQKbTAdo7hBKBd3cbcFCKZostOtcoUMSARjHBwM43qAhIvK1Xr2rKVc6MegMxTm0GGJRCjfOjUt22IOkc6rKpCpAyKLC-lSPE_2ZmMjRzzQOwNfo3BkRUJP9J6rFSIlHfWPDwHkWWbHg4LN9iE_2tLPfbh1k0GhCOXfqET0Bh7zsoGD3NDeEdLpW9nj0inczFwhtl28gMwk3bf27Uyc5qDK4W9HCPQG1lM-LJMU33H3rnQnEjkAsvphLC70B6ocA3dtRzkph4xRAlkidDFgRWegw-0vLAubEoZaPsmi0Grz2nG6yqUjpGZocZpH-6zRrZIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه گذشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81436" target="_blank">📅 20:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81435">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Numb 1 - Madoro</div>
  <div class="tg-doc-extra">numb</div>
</div>
<a href="https://t.me/funhiphop/81435" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81435" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81434">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeNGzNWUCTbWPhDM3QTD1d2fu8-LEH8GRd81oPzVpex7b2Ei98kzo-IogN-Y4cuu72pxpfEJBiSxB5TYyzHsaWV2WkHER5CHEa9arz2Bv6Ax5QMGqhpbsnZDAnml7W-yuc8rbyaoPKOW1vHS-vToKiDxcR7FkEb5ATaUGpD8x7g2QYqKHEBOg2psY_TCtbYlmhRSgaTFt9fbUmbKddx_U1VuGmblyZw7xch8X-BgDAY8iznk0-o7YExLF9SfK_QGanuqIIyg8DpT5W5AMiXGFZZh4226wp5wCPiyVKV2KTSoU_d_Kv0bABNekJGrxi_qtbiZjKbOEzX2MjVQOoMH8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهنگ جدید numb به نام مادورو منتشر شد
📺
Telegram</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81434" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81433">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">این که ترامپ دوساعت قبل جلسه با نتانیاهو میاد میرینه به نتانیاهو یعنی یه کاسه ای زیر نیم کاسس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81433" target="_blank">📅 20:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81432">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E88U8kyBDUcs4Pguo4hOB-sJ5kL9Zmow5msO2-0pTsg70SAPlUNuOVxqVTJZWovnq1YDz70T2qlYCtOTfG8mH6Wr8PACvnCwg0lKAFawZtUY_5F6zJdMj2gL0SkmC0GjhL2pIZ1TDIREsj1eUsbfq2zSFIVOcNFoGyEgQ2n5ltWnMgqDAtMaIkdNTgcyCPHbofsMrTSDaxjUuBqhtdNEsFAI7ASIN7EIFw8-opCIz0j1gPuZtqHGPVVRQ42-SPDIZQtOfrk-3C-GC3PHyPqdxqhsO6bs4fgjXssxygY6_dnYfy-3ihd6orAC44s-44Xwu1CeauvBhvdIJfUbAVoW5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یارو تو فصل یک عشق ابدی رفته صداسیما
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81432" target="_blank">📅 20:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81431">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aayrN0e26gnPnNwkEPn61qoFTSZpycD2UFwMJaq2isRRqNZlpxDax0yU7HoKGqsi98WWitbUBBawG-dX9ALrPk6gwDpjSWVgpnTwSdqRmWX_7jFCDIxDMpQGzGZHrsZvSRjBzFzOnjHna5KaQ1sF1u-4D8lxouKpKUeKy-WYy4yYj3NZ-mw5STlNk2axDMc5WxRjpM30oyN9Gh3FQcKfObIruOZo38DnDwby1qHhPsOoFqM2J6DTuxGtEfDnNEozRBBpoRRcXkkAKgReMkt1uIF3o4PeulunmAfbfI5zaHk_uWP1CVJvM8fxpAAb6VIy3cz6mp02Wdz2D6z-aIOaBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو و دو تا از طرفداراش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81431" target="_blank">📅 19:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81430">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz-ameDH4YCaWBN7CsUfuHrONMp4pwIXfP9F37CI0O65C7ZveFxYss4xcZrV6DPKx2je3qmyXQ4Dyc1-MLNt9NK72fR08gWwHsTl7RHGlpJ9pTs6CCSurFlRgPQbd02tRrSTJU6swc16xEtEkdIBHmgG5XodjlGnyX5OBcBvfNKjqPZvh7aHBpPvOfY9OXdcfKWg8yX8KqZNTwQ2eAwWt8GAdOy1ZY5AvXdub9omjyoQiczbnunRRP5frpdMrv6j9VuMoAFC9xI9K5RtRJyKAe3yaq8UoEWeb7GJk4mXrBCFGQ454HriTXwQ1prqt3SC57aWPKDk3H28Ie9VVBDTfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ فصل جدید لیگ جزیره
🔥
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81430" target="_blank">📅 19:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81429">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUVoYMahsj_geLUiG7ApSmvQqY4A5mofBlVQkOGF5WFt-ZcTj5AuQgw9iKZf7IFgpxwOkXdFHD-EPcSUNY8etV45n-SGglReWyjX4ujnHSvk94HDIESv6ybd60y1nd5De0MHSxBD0XOZgHOBBJPRgyh0SVmNVG5G50yyj171RbLFzjd5RG3ZEFBoPDBwP49yFxbh5R8dZsaBiSZPjit0Jkc1baucrh0BwZGbYHEMxy-ADUb7EfFK3gPPXyq6_F6ExE3Zef1OaHJIr5cppBS7wERK6XBnx_RgywfFA1Cd5zzH-VWS9sy0wvQa18uafrsOyaKfjKZFvUK-hDgOxV9VmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچی بگم از طنز ماجرا کم میشه
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81429" target="_blank">📅 18:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81428">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GehZMFd5zeU0hjkCrI3ke_MOobrR2e-noYdZnwEfvvWPv6XGGXr99wQ4iVYx4ROiVtJGkAaYchij_4RFBBd6N-3l7nSmzOVn6VsiY_sU92QTrCXApbUoXV_XQduUelb-AB-DF8TjhtKfC3lIS7UT-9Q1VfdfXAZS2a6LuHvstugG3kBd6tsDT1q-gZvLUn5yvk2JJ3WfqbwU1-5_FBe1T_aAS4oHk3Bc3jbykztyrLcfvdTBFGo6uZHcuUkpLQtzMPPl5aFA528-1Uv0CHkua9JD5eFfb-Wxds-Wj-p45Omuu4vZLl5JiXYvdL7SWVLSlzAiuuGlb0xzgpe-KHO8Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رئال مادرید
🇪🇸
-
🇪🇸
لگانس
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
سه‌شنبه ساعت ۱۹:۳۰
🏟
کمپ تمرینی رئال مادرید
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
رئال مادرید ۳ بازی اخیر خود را برده است.
✅
لگانس در ۳ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر رئال مادرید ۳ گل در هر بازی بوده است.
🧠
برد، همیشه عدد نیست، گاهی آرامش است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r6
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81428" target="_blank">📅 18:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81427">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81427" target="_blank">📅 17:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81426">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">به گفته ایران اینترنشنال,
قائم حسینی ، امیرحسین ملکی
و
علی دشتی
از معترضان پرونده‌ی میدان علیخانی اصفهان، به زودی قراره اعدام بشند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81426" target="_blank">📅 17:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81425">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81425" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81424">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkeD8gYXpa3_MK9HufoGNjVYikmkMroSTR93dbyVcj8b_3NTGhY34LoUw7Jxccii8KEWqcdPCe5N2H2wt4RM9NiCODTO5dSSMoCxs76WGFPJ6sBeYcY6nyvGf8PFd8Qhm8p_S6gvon4rYsESKeU-PWhQeC00O91-N8VJYCKuFUkMwceHGyyThkpUf3Bq8O8b1ssV-TxDEEAv5hmOiwG7M7XkH4uhuVV3djwrVjhHWUTQY2kW1jNNzeyxXRE2owJBLSYfbAQOi-L4PoTUiDpq-C7T0g5gz5pTstwbeyP8VbWGV48FgL4CqNEe9ZNV5KitrTyh1Og5LsC4l2vHtV6GyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو خود سایت کارزار، کارزار را انداختن برا بسته شدن کارزار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/81424" target="_blank">📅 15:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81423">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اینطوری که روز به روز اطلاعات جدید تری نسبت به زیرساختایی که از ایران زدن و زیرساختایی که از عربا خورده میاد، فکر کنم آمریکا رو فقط در جبهه کری خونی با AI شکست دادیم که اونم ترامپ اشتراک طلایی گرفته داره همونم ازمون میگیره</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81423" target="_blank">📅 14:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81422">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سخنگوی دولت: در طول جنگ ۴۰ روزه ۲۳۰ میلیون متر مکعب از ظرفیت تولید گاز خود را از دست دادیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81422" target="_blank">📅 13:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81421">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">از سر شب تا صبح ۱۰ ها موشک میخوره تو خاک کشور
اما به اندازه ۵ دقیقه اذان صبح کشته نمیده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/81421" target="_blank">📅 13:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81419">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XBcW_k2trip8oLkJB0CX4ClHH22VZCGtpVvRgPUmgYBPvTTgQj31FGzkQpikIOOpgx5XnlTdl2dOOpd6lwTfzqzJkOYGSoydz5kcbgUVoWEQctW90F9lsuny2rcyiLXsIVsFJvb_hVHr6UAU3-MUg-7GuusfZRrEqs1R5DtBkCt30PhPryMlAXPUcRMIhnBHG6n9GTyprtwV3dRkHM7JZcokXTGa3CXx43QRDGuKjnmdeUYef_mc_o-nmTA1gDTja9D-tNvUR4742dDktFWP7CVJTT8jy9N3q-lptuvMYDFR3Lal0n_MGJSo35zHWMh1qSKsbPQDBIarFq8apY76Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kRnDiFiMIQQ0jgnIGdAw_AcoAkvCqzY4n0oeQP4KsaovpfasjjtkQ56P7xwuCudktraaa2yWPXpIgTGnyb3TQKKA-j8SZz3USSdAv7BN_BXeXlwB5N64H86hyOTWwCtfAGTVcELszfRodixHSp90he-d26OweRDvhctLh1KJVvsicUDnv7alA_3_9XjB4pB4wDUASrthGmmo3ejLkGMLSNLO1z3LX9eBIfOK2fFnSjgfhird2ZXYMC4yNM6G8pjIgHWxuK5tyJ8vK7ZBbu5c8JotQQv2foKJwbMKB2LU-cl_AWFJrQ60ESpSBlwdAPKNrb08aFiZFujgHOIc76H6Og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی دیگه از پیش بینی های اکونومیست درست از اب دراومد.
زلنسکی با دوربین کنار یک کشتی ایرانی که داره کالا حمل میکنه، و یک پهپاد هم بالاسرشه
چند روز قبل اوکراین با پهپاد یک کشتی ایرانی حمله کرد.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81419" target="_blank">📅 13:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81417">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bf2mMEW9VoceLDkw220aF80_jdSkWgjmP2mDPv6t26HbJDZEX5J7n5NxP8ykY2YfDo1F_pepRLhXyvRiTal_I8xIdXqCZdxuW3l0ieuc0QPhgzXTDQ4wLWpttPE7Goop0TxbpMOgWyb8EywCajWxDO-Ow_IBq3f4dYE4bj5ClzvcBVvF8oJDcaEcV3djsR6ol5RIrI1nHc3aMIEc43UG_zjauO0TumI_HDMuiuZmS6611SSDhYBzFND79v_95WcjlB8VmMYGQHWcisJhz6mqbLFSp8-fgs65EQO4O-f3XQrRdYu-rCkoxomJJlSWKGJ7FHKf902OJlTU7gumQamnHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f171036de.mp4?token=Ow9tdrf0qd34xgPl0slgdtBRJCiUyFr48byY04DrUe0Y4g8WNJiZJU70ZrtZDEi6IY88g4Cz_s8n79xv1RdLdQ37znwhEdzvbi82jwvTZ_H9EdNiKQpEySaIQbAmWZPS9FsKmFhMGwF5iwi16S2F5T98keJnvrKS9ZjP4Pluy1K9hLD3GPz32TRhp6lFJY0nb0GxbkHFaOb13lqi6ArJqhqEMdmb_eHveqYKCnUXeqBAOWD2wgssKM8BhmOlMWcukhFwR_wW2jRM6UT9SolG5Ap7mpQgfTFeomQdcHC0ZFRyJsTohFx4ScniTyBJxeB8lDZFSNkm4gDP84CqYJPWKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f171036de.mp4?token=Ow9tdrf0qd34xgPl0slgdtBRJCiUyFr48byY04DrUe0Y4g8WNJiZJU70ZrtZDEi6IY88g4Cz_s8n79xv1RdLdQ37znwhEdzvbi82jwvTZ_H9EdNiKQpEySaIQbAmWZPS9FsKmFhMGwF5iwi16S2F5T98keJnvrKS9ZjP4Pluy1K9hLD3GPz32TRhp6lFJY0nb0GxbkHFaOb13lqi6ArJqhqEMdmb_eHveqYKCnUXeqBAOWD2wgssKM8BhmOlMWcukhFwR_wW2jRM6UT9SolG5Ap7mpQgfTFeomQdcHC0ZFRyJsTohFx4ScniTyBJxeB8lDZFSNkm4gDP84CqYJPWKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طقه پوبون رو زدن
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81417" target="_blank">📅 13:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81416">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TviC-ODqiukEL7IWF_JfEkoNx5gZYqFEndpWftlVf_9vYkgH9RZq2CyOWYaF0eYGM-TgBJbwMZ_DWbvf5QUkMD5rWU9CvYvXOuszGIm-9_cJJYMfAxo_cs2hWwExMydS5dY0zL61JG5C0VSj3Su9ciN_5SqVy79cVtsglqlEsZQrYPhNFzVhVQ0JPudog4_16OjkvrPXraWOjcXjATcTbRRhp60Q8IqeG29vZUVgZeNcLuiHRt0MMfwT7OPANP6OQhTbQpAw1dEI2LrvrDRH_wUbKmwvESVOT_mc_rz4j5dCSPWZaG1nAmGQVbjsf23j0wc204vgY4HKZVmTFc9QOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رئال مادرید
🇪🇸
-
🇪🇸
لگانس
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
سه‌شنبه ساعت ۱۹:۳۰
🏟
کمپ تمرینی رئال مادرید
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
رئال مادرید ۳ بازی اخیر خود را برده است.
✅
لگانس در ۳ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر رئال مادرید ۳ گل در هر بازی بوده است.
🧠
برد، همیشه عدد نیست، گاهی آرامش است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r6
💻
@BetForward</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81416" target="_blank">📅 13:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81414">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce9ff43bec.mp4?token=PFygynSTKl60e91So-IwGyVcUpN-qXhhF2kJkjiMioLb43vcO_hwGrEINVfKXRjCRtfKcysFPInGoGuaUc0Thk_Ss5DrN88agDjkBGspx5zy9wettxD0XklU5c7h9EzzvEL35WsWSjFyM4EGaw7jUZyWUTB9ghxa8qw_4RXy_DPBT9heZYQ3odimvLBcIOf9B6x6WZ1r033UytvOWVmZGNOkx66LmLgORb6pcI-l5lfKzPTgwU7NlmpMk8oR4wba8UjS7OMljKGN41f8vXmCj1Ocdt7DUZTs7RcZReyu-0fkdKwhTsKgElbrINv17NnDzt9SiOCK6KYg1Qf1vsVbGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce9ff43bec.mp4?token=PFygynSTKl60e91So-IwGyVcUpN-qXhhF2kJkjiMioLb43vcO_hwGrEINVfKXRjCRtfKcysFPInGoGuaUc0Thk_Ss5DrN88agDjkBGspx5zy9wettxD0XklU5c7h9EzzvEL35WsWSjFyM4EGaw7jUZyWUTB9ghxa8qw_4RXy_DPBT9heZYQ3odimvLBcIOf9B6x6WZ1r033UytvOWVmZGNOkx66LmLgORb6pcI-l5lfKzPTgwU7NlmpMk8oR4wba8UjS7OMljKGN41f8vXmCj1Ocdt7DUZTs7RcZReyu-0fkdKwhTsKgElbrINv17NnDzt9SiOCK6KYg1Qf1vsVbGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی گرامی کار قبلیت چی بوده؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81414" target="_blank">📅 11:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81413">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مگه نمیگفتن هر زمستونی یه بهاری داره هر شبی یه روزی، خارتو گاییدم چرا تموم نمیشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81413" target="_blank">📅 10:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81412">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXe6fZm_Vte1zSoO7oj3iaK86bpXRZyBdaNMP4r7Bw6K9RMN8BTXnZXv0l8ClZHF-2Qww41dBoRUOY2njsc63DftpmEiAutAgDbqNyk3QE6VS-Kyde7bHjJwCsJ1Pbxw8_xy-btz9fhapjvEojJmhWFf5l7FHQbsg1zTBpGurdwiVG8DGgq0e1ZzSxhela8_7XGAHKH3gWkzja6W1nNW3prEAVWqI0L4GaMEcBYRDTZU_N3CYAJa2HrS-iEKrJqNaUPEkTMuB1dZrZbro2w99xqobOTjccfjebsiu_mqk5UmoyCtfQuc12xSQh_rgpRBmQYM_rPMktZmbq6ArRI5VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81412" target="_blank">📅 10:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81411">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تروخدا فرزاد قدیمی رو قاطی زیرزمینیا نکنید، فرزاد اونقدرا هم کیری نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/81411" target="_blank">📅 08:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81410">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خبرگزاری فارس:  هر سه نفر اعدام شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/funhiphop/81410" target="_blank">📅 05:29 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
