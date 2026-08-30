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
<img src="https://cdn4.telesco.pe/file/QH-zbGjjcljjsEvscO7RIcOD2BEuiev61JdkBIC55Rju-gozCDcJSxmzyxJ1k6PEKJYN50WcW-T0PVFpyZgByBfjQFTDFUdJyfDV97SMHVloOVx_xrYbLuzM6SgisUMQlUq-bKtEQJ5qlPLV3M4ciGO2ofTSdxqVzbWcNXuSdNAza36UIwC1dpFEb4IEzqN6AYmp6afnsli3w64G72UcNzXQQxgYUCe-hmoHBfKRuNR4NCDtDG09aSnqE_clHIBPO2ocoW8iTbwZfEewD1XIeqfJIdP6nKm8BJajOqSa5p7RjGz4pXt2gxzova-k3MtVAexrlnztXlFd3onkPXVumQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 439K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 17:38:01</div>
<hr>

<div class="tg-post" id="msg-21715">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oy1pkXLSDPzePhnWMLlMnCaZWjZKPlW663t4Jz4VvTKDfF3f-TrT49xgtApAydVdOw7OlWFbVzExTreLpSH2ST6M5o-k1XHs-IxqZuKKf7UqnDnXVqc7HIj-5lnCp4-RIv9JM9TNO_VqHgRDwPCpgq3Gc34tqsNGt2-1oSZU1nz3MFIBnI5-aq7rJ7KhME1fuFaElYpnLd1ywYJLVu_o56cz8KoshxiZ04AXRnMjLwMpOOod1uB3P40fDgwqF5Pkwvi12N28g_9mUc2mmpFwjxHyQQwsCy11tY6PmcYbW_V9uQyDJYapdgey5VyDMIxATOD2Wuhcw3FEGPFYyDvZ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i91FBSu0a9UCFvzjcMUyTtURnsppXnSaEoqGuiJFggMZ4xQsnj6Qf4TwWq5QxkXttDMfzLZ-cZ7skIX2Xoooo6XsCg-QAmi8wvLKDxrzx530P9C8KypOOzjB0jh_puFHHrAcZ_0W-SHHovypbF25kMWI0ClnddjjqS7DNWqm5sdEJEi_BjejZEzRsxO_h7g8_R8oyUEkf2sLsKRcTG1j6fRbe-TdU1WnwplXADfjB_acGXt-pz6WSLDzBko2xI04nt4wQvqkO7jgOf18Mi225bw1Phx0025Wpa9mkYNNnkDtcLYSRabWvWZacHPNI2LQS0fS11mPD97aKRJWgPtODw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیکلاس مادورو از زندان:
«این عکس‌ها را به‌عنوان هدیه‌ای کوچک برای همه نوه‌هایم، چه پسر و چه دختر، و برای همه مردم شریف و بزرگواری که ما را دوست دارند، می‌فرستم.می‌خواهم بدانید که ما استوار ایستاده‌ایم؛ با قلب‌هایی سرشار از عشق شما. عشقی که به ما می‌رسد و به دعا، کنش و تلاش همیشگی، همبستگی و حمایت واقعی تبدیل می‌شود.»
@WarRoom</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/withyashar/21715" target="_blank">📅 17:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21714">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ناو هواپیمابر «آبراهام لینکلن» آمریکا، بامداد یکشنبه ۳۰ اوت، پس از بیش از ۲۵۰ روز حضور بی‌وقفه در دریا و پایان مأموریت طولانی خود در خاورمیانه، از آب‌های نزدیک سنگاپور عبور کرد و در مسیر بازگشت به آمریکا قرار گرفت. خبرنگاران در جزیره باتام اندونزی، این ناو را کمی پس از ساعت یک بامداد به وقت محلی در حال عبور از تنگه سنگاپور مشاهده کردند. این ناو در جریان مأموریت خود در خاورمیانه از عملیات نظامی آمریکا پشتیبانی کرده و یکی از طولانی‌ترین دوره‌های استقرار ناوهای هواپیمابر آمریکایی در سال‌های اخیر را پشت سر گذاشته است. آبراهام لینکلن قرار است پیش از بازگشت به پایگاه خود در آمریکا، برای استراحت و بازیابی خدمه در تایلند توقف کند
@WarRoom</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/withyashar/21714" target="_blank">📅 15:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21713">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یونیوز: ایران در صورت گسترش جنگ، شمال اسرائیل را هدف قرار می‌دهد
تهران هشدار داده در صورت گسترش عملیات اسرائیل در لبنان، فرودگاه‌ها و پادگان‌های شمال اسرائیل هدف حملات موشکی قرار خواهند گرفت و حمایت ایران از مقاومت ادامه خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/withyashar/21713" target="_blank">📅 15:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21712">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaffcfacf3.mp4?token=Egi7ufwvGgfty7RqrAeMnYonR9XPaBQ0r3y7EwKgcki9CKDSFthRfC_DLswsgsZrDbR_uWt1gHL55Iu7CcvMFLmm35BPT03I3ut9WxA7yvIFCVTwQGBs5kUz5KhY7bDLkNNxUmWHhP9y01mBVnzg9sk9D-F_L2GPIU7Ta7rGF-LVb0Sx4cCAAHUyf2rQdisI5Yupkra9XHipX_olxNOnvDlm9CsohZwktJ6LeI-8eums13UD6nc_w2a9mZt1n6Mxx6SFLL65A8ZAYFiWiJM6c0TOhpNl8INCkEUglpkxlonq6AiJtEsqovkSTmjm6LJ4N4AHMSj2QP4pkiHKv0c3EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaffcfacf3.mp4?token=Egi7ufwvGgfty7RqrAeMnYonR9XPaBQ0r3y7EwKgcki9CKDSFthRfC_DLswsgsZrDbR_uWt1gHL55Iu7CcvMFLmm35BPT03I3ut9WxA7yvIFCVTwQGBs5kUz5KhY7bDLkNNxUmWHhP9y01mBVnzg9sk9D-F_L2GPIU7Ta7rGF-LVb0Sx4cCAAHUyf2rQdisI5Yupkra9XHipX_olxNOnvDlm9CsohZwktJ6LeI-8eums13UD6nc_w2a9mZt1n6Mxx6SFLL65A8ZAYFiWiJM6c0TOhpNl8INCkEUglpkxlonq6AiJtEsqovkSTmjm6LJ4N4AHMSj2QP4pkiHKv0c3EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@WarRoom
👺</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/21712" target="_blank">📅 15:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21711">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">الجزیره: آمریکا فعلاً از تحریم چین بابت خرید نفت ایران اجتناب می‌کند به گفته یک مقام سابق امنیت ملی آمریکا، تحریم چین همچنان به‌عنوان گزینه ذخیره ترامپ باقی مانده و تواشنگتن امیدوار است مجبور به استفاده از آن نشود
@WarRoom</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/withyashar/21711" target="_blank">📅 14:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21710">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پرونده جدید : مأموران ایرانی، کودکان زیرسن قانونی 15 و 17 ساله را در شمال اسرائیل، از طریق اینترنت اغفال ، جذب کرده و با پرداخت مبالغی به صورت جداگانه، آن‌ها را برای عکس‌برداری از مکان‌های استراتژیک و نقاشی کردن نوشته‌های گرافیتی استخدام کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/withyashar/21710" target="_blank">📅 14:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21709">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وزیر انرژی اسرائیل : اسرائیل دوباره به ایران حمله خواهد کرد حتی اگر آمریکا توافقی امضا کند
@WarRoom</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/21709" target="_blank">📅 13:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21708">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏آزاده اخلاقی، همسر محسن نامجو می‌گوید نامجو ۶ روز پیش «به بهانه پرینت چند کاغذ در سر کوچه» با یک صندل از خانه خارج شد و ناگهان با چمدانی که از همسرش ربود، از ایران سر درآورد. اخلاقی همچنین افشا کرد که نامجو حتی پاسپورت جمهوری اسلامی را نداشته و با واسطه‌گری…</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/21708" target="_blank">📅 13:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21707">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رویترز : بانک مصر در حال بررسی پیشنهاد وزارت خزانه‌داری آمریکا برای قطع ارتباط شعب امارات از بانکداری واسطه‌ای دلاری به دلیل تراکنش‌های ادعایی مرتبط با ایران است. بانک مرکزی امارات بازرسی ویژه و فوری از این شعب آغاز کرده است. بانک مصر اعلام کرد عملیات در امارات عادی است و اقدام آمریکا هنوز پیشنهادی بوده و تنها به شعبه امارات محدود می‌شود، نه عملیات در مصر یا سایر نقاط.
@WarRoom</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/21707" target="_blank">📅 13:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21706">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLqU4UF2jyxCHm9b_CUbD_ADoBfZQMfsEGsUQ7WbjsrMEPZMsWZAI9oaDT-VhnMgVxGKwd59UQxtzQpD7k6nnwKzJxoZ9Vl1dsM_UtlHgGM821nnGsLw4_p9sZewv6Zzh668tuKuu10dyIDTZ5dNt3rSpfWAOM8KImUlq8BxnQsJ61srQXVI7lBu4lSQ8irDNsYTERvJJQuGL-dT96GU0i5JVYhuH3AwT5TH3DodKjF2zlFIEgvZL7IdOkzBU98_xDa69JSvI7MoVY0tBkSO-Q7PW7BtoIdmMgcKaqi1DeM1TCpfgg9b_V5FGwSsBF5bzby4gL7JsoCBrnOmK_yqpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراق، انتقال محموله‌های نفتی خود را از طریق عملیات انتقال از یک کشتی به کشتی دیگر (ship to ship) در خارج از تنگه هرمز، آغاز کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/21706" target="_blank">📅 13:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21705">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آکسیوس به نقل از گزارش سنتکام میگه جمهوری اسلامی یه مشت آشغال ریخته بود (۲۰۰ شئ شکل مین) تو تنگه میگفتن مین‌گذاری کردیم ولی کلا ۱۱ تا مین انداختن تو آب، که ازون ۱۱ تا ۵ تاش درست انجام شده بوده
.
@WarRoom</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/21705" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21704">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqQL4LIn9lW4qb_F84B6RFSbdqr1199qk7iMX8DLhz2vKTRVrkvH2GYi37_fpRCJsV1SiZF-u_dWAs4wYoSI9eTmI7dbdv-JfhMa_k5hHq-hM5BO1npbicUPzqk0UjG7Pel_kA-AzVmkz3BglHQR9ru8J8vFuOR40DFCn-zkgmh57igtaOuxbVrMFsgwgykdyzmSQQsDDQutnsio-lMz-q67Arn1TCC5XuGAbUqAbibTKSa1U8IO9ttiRfvFTZF5aQBs6fxtLc3wit0jtjLWkuH03to-pYGgzcGIbTzNJoSK5shr2k-0HPqIjt9g2NC6-28bW3jCxFysTTbxOfpcFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۲ فروند جنگنده F-16C/D گارد ملی هوایی اوهایو
از بال ۱۸۰ شکاری و اسکادران ۱۱۲ شکاری در مسیر خاورمیانه هستند. این جنگنده‌ها با کال‌ساین‌های
TABOR11 تا TABOR16 و TABOR21 تا TABOR25 و TABOR17
ابتدا به پایگاه لاژس در آزور پرتغال می‌روند و سپس راهی خاورمیانه می‌شوند. در این عملیات، هواپیمای سوخت‌رسان
GOLD10 (AE066E / 62-3569)
پس از سوخت‌رسانی به جنگنده‌های TABOR11 تا TABOR16 و
GOLD12 (AE44FF / 23-46116)
در حال بازگشت به پایگاه گارد ملی هوایی بنگور است. همچنین
GOLD22 (AE0479 / 58-0061)
برای ادامه سوخت‌رسانی به جنگنده‌ها در حال حرکت است و
GOLD25 (AE5FAC / 19-46065)
نیز در این مأموریت حضور دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/21704" target="_blank">📅 09:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21703">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بر اساس گزارش نشریه "اکسیوس" به نقل از منابع: مدیر سازمان اطلاعات مرکزی آمریکا (سیا) پیشنهادی را به مسکو ارائه کرده است مبنی بر برگزاری یک اجلاس که در آن ترامپ، پوتین و زلنسکی حضور داشته باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21703" target="_blank">📅 03:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21702">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">@WarRoom
جعبه شیرنی ۲</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21702" target="_blank">📅 02:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21701">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشایان</strong></div>
<div class="tg-text">سلام یاشار جان. این یه پیام دلیه که برات می‌نویسم زیاد ربطی به ماجراهای روزمره نداره. خوشحالم که پیدات کردم اینارو بهت بگم چون بنظرم خیلی بیشتر ازینا حقته بدونی. من ۳۰ سالمه. ۸ سالم بود که تو دبستان شهید باهنر تجریش با رفیقام قفل وبسایتت بودیم. تو زمانی که آخوند نمی‌ذاشت بچه های ایران نفس بکشن یاشار رپفا یه تنه آرتیستای جدید و سبک جدید حمایت می‌کرد و میاورد بالا و من چون اینترنت خونمون دایل آپ بود می‌رفتم پاساژ البرز تجریش، یه مغازه بود مسعود موزیک که سی دی پستای جدید وبسایتتو برامون میزد و اون زمان رپ برای ما انگار تمام آزادی و چیزی بود که نداشتیم. و امروز برام اصن عجیبه که حتی پزشو نمیدی و زیاد به روی خودت نمیاری که اگه تو نبودی اصن چیزی به نام رپ فارس با اون دوره تاریخیش که هیچوقت دیگه اونطوری نشد به وجود نمیومد. الان شاید نسل جدید باورشون نشه اما ما یادمون نمیره تو کی بودی و چیکار کردی. تو فری استایل همه رپرا یه پسر عینکی لاغر بود که کم کم همه فهمیدن این یاشار رپفاعه. خوشحالم که الان از طریق این کانال از حالت باخبرم. به امید یه روز که تو ایرانمون، توی یه ایونت که کتاب خاطراتت از رشد موسیقی زیرزمینی ایرانو نوشتی و برا علاقه مندا امضا می‌کنی بیام و کتابتو بخرم و امضاتم بگیرم. عشقی داداش.</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21701" target="_blank">📅 02:14 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21700">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">@WarRoom
جعبه شیرنی</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/21700" target="_blank">📅 02:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21699">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromalireza</strong></div>
<div class="tg-text">سلام یاشار جان عشقی
امروز دو تا مشتری اومدن (من صندوق دار یه مغازه شیرین عسلم تو پایین شهر) دو تا مشتری اومدن زرتشتی بودن و اصالتا یزدی واقعا خیلی آدمای با شخصیت و خوش رو خوشتیپ خوش صحبت با فرهنگ بالا با اصالت و واقعا زیبا بودن اصا انرژی مثبت فراوان اصلا خیلی حالم خوب شد و انرژی گرفتم
ولی در روز چند رأس عرزشی میان مغازه واقعا آدمای کثیف بی شخصیت بی ذات پرو و طلبکار بد رو کثافت و کثیف بد تیپ بد چهره شبیه خوک میمونن و شپشو ان آدم حالش بهم میخوره و واقعا اعصاب خورد کنه وجود شون حروم زاده های بی مغز قاتل
واقعا بی صبرانه منتظر روزیم که از دست این شیعه ها و عرزشیا خلاص شیم و مردم با اصالت مونو ببینیم و کلی کیف کنیم</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21699" target="_blank">📅 02:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21698">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اتاق جنگ با یاشار :
P-8 Poseidon
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21698" target="_blank">📅 01:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21697">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اتاق جنگ با یاشار : تنگه دعوا شده
@WarRoom</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/21697" target="_blank">📅 01:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21696">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تنگه دعوا شد
🚨
🚨
🚨
چندین کزارش از شنیده شدن صدای انفجار از تنگه هرمز
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21696" target="_blank">📅 01:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21695">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21695" target="_blank">📅 01:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21694">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">@WarRoom
hamshahri javan</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21694" target="_blank">📅 00:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21693">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21693" target="_blank">📅 00:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21692">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏آزاده اخلاقی، همسر محسن نامجو می‌گوید نامجو ۶ روز پیش «به بهانه پرینت چند کاغذ در سر کوچه» با یک صندل از خانه خارج شد و ناگهان با چمدانی که از همسرش ربود، از ایران سر درآورد. اخلاقی همچنین افشا کرد که نامجو حتی پاسپورت جمهوری اسلامی را نداشته و با واسطه‌گری بهمن بابازاده، خبرنگار امنیتی که ۶ ماه با نامجو در تماس بود، مجوز حکومتی برای بازگشت به ایران را دریافت کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21692" target="_blank">📅 00:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21691">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtMY5cny8CCXcnLfgtuLESDy8FOL_Fw4ENDRDMWCBauzavYOD6WMpnyoaQSE0XSUPVga95mefnUSaLr7iRvlHZaRuJvbZbfQUdCqDAQaeEvgRpkeufmBNO0FyVVdHBWZHIqz2HU7im9zBwnMscetRdQb5OyrJ-No1PTR76TKDW2YrOngiPfEKgLHYllueChYeBB6El7DZ5_AS-lb1ZxsInjXS7wT77yHGY_Oe78fKW0dq39spJfgaSSZbxecqB548A-TlvZKQsLaS8u1mqolC8Snj37bL8obQtzQAUmL2KShb-DHtCH3YLsTm4Xm04NHS8zDN3Z08zCXTlkzMeEZsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کارگاهی محدوده بزرگراه آزادگان انفجار رخ داد ؛ یک کارگر جان باخت ,در این حادثه یک کارگر 21 ساله جان خود را از دست داد و یک مرد 30 ساله نیز مصدوم شد.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21691" target="_blank">📅 00:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21690">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECtPW86SAuklnmZbk_pQFoYWoA9kbefb5tCrbP-eu34qZDUCN4wt47fBSQ1YLGPn3RmYVofUOz8rmqVFr4YtyXrRnK-GQCuYm6L7-WD-0qhnudhw5B0SCp0LMds0YlTJpwc9Z4I9G2tNHp21iswNt1Ar5ShqQJgHZJjRYV3Dh88mIq88H0eP0AHk_QE9xuu8zBcoPA6hOG6hljZeSDyEjrZaBQFWXaoBOY6ypYth0xiunncH6WaqpwYBkF6A1ja5W8GvegpqmZthuSxB8Gl1IfKzyfyAe6uTe0B_vFvVxLX0nrKQw2krGvG2-Z_9A_CSuCzeWnnNGS_pTfv3dIJfKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل
: فرمانده یگان نخبه و یک
تک‌تیرانداز حماس در غزه کشته شدند
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21690" target="_blank">📅 23:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21689">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پدافند جنوب غرب تهران فعال شد
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21689" target="_blank">📅 22:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21688">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کاظم دست کج غریب‌آبادی:
تلاش قطر و پاکستان این بود که بررسی کنند آیا امکان بازگشت به اجرای تعهدات تفاهم اسلام‌آباد وجود دارد یا خیر.
ایران آمادگی خود را از طریق تفاهم با عمان درباره تنگه هرمز مشخص کرده، اما اجرای تعهدات بر عهده آمریکا است.اما آمریکا تعهدات خود را متوقف کرده
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21688" target="_blank">📅 22:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21687">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">باراک راوید خبرنگار آکسیوس: ابتکار بستن تنگه هرمز از سوی فرمانده نیروی دریایی سپاه مطرح شد
دو مقام اسرائیلی به باراک راوید گفتند با اینکه طرح بستن تنگه هرمز توسط سیاست مداران ایرانی درحال بررسی بود، تنگسیری بدون گرفتن اجازه کل تنگه هرمز را مین گذاری کرده بود
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21687" target="_blank">📅 21:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21686">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بانک مرکزی امارات متحده عربی با تأکید بر لزوم رعایت قوانین توسط تمامی شعب «بانک مصر»، از آغاز تفتيش و بازرسی فوری این بانک در رابطه با مبارزه با پول‌شویی خبر داد و اعلام کرد که اقدامات احتمالی بعدی را بررسی می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21686" target="_blank">📅 21:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21685">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مارک لوین : قطر یک رژیم سلطنتی و اسلام‌گرای شیطانی و نامشروع است
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21685" target="_blank">📅 20:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21684">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9a3d293ea.mp4?token=dnv-P0vdBF-9hDSZPuTJRt7y_Vv3cpXPUDzETclUmKSzrLdKSANMzA8o1QXW-tSJjsKo9KRs0eqmZrnPDNhWHvd1LKO7NB9axriX_fghB_YsvPFgVa7_xrHBuMRIsQvPWChLH08Sh-xL0MK2MiaJLxDjpIakvZiyCIHfFprVlqWAUUMiwvAiTq21VHSOKfTN0Q9l3469A5aB8sdJzXFDzMwPRCyfG4jYTbot-4Jv0DKhP3jeKNYZMQH14cwwmZW1N9r1nSqSAMs7WrZhAvGxgKbg4mWCIlINF5qIbHXjZhOKAfsE2Dp8v6rWOui_qfsylErkQxFMzkpH4XgUahPr5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9a3d293ea.mp4?token=dnv-P0vdBF-9hDSZPuTJRt7y_Vv3cpXPUDzETclUmKSzrLdKSANMzA8o1QXW-tSJjsKo9KRs0eqmZrnPDNhWHvd1LKO7NB9axriX_fghB_YsvPFgVa7_xrHBuMRIsQvPWChLH08Sh-xL0MK2MiaJLxDjpIakvZiyCIHfFprVlqWAUUMiwvAiTq21VHSOKfTN0Q9l3469A5aB8sdJzXFDzMwPRCyfG4jYTbot-4Jv0DKhP3jeKNYZMQH14cwwmZW1N9r1nSqSAMs7WrZhAvGxgKbg4mWCIlINF5qIbHXjZhOKAfsE2Dp8v6rWOui_qfsylErkQxFMzkpH4XgUahPr5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در تروث : دریاچه آمریکا توسط اردک‌های دونالد محافظت می‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21684" target="_blank">📅 18:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21683">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ‌ در تروث : «سی‌ان‌ان (CNN، شبکه خبری آمریکایی) در یک مارپیچ مرگ قرار دارد و MS NOW (شبکه خبری آمریکایی که به‌تازگی نامش از MSNBC تغییر کرده و ترامپ با کنایه آن را “MSDNC” می‌نامد) هم همین وضعیت را دارد؛ واقعاً تقریباً هیچ‌کس هیچ‌کدام از این دو شبکه را تماشا نمی‌کند! بهترین فرد در سی‌ان‌ان، هری انتن (Harry Enten، تحلیلگر و نظرسنج سیاسی CNN) است، چون حاضر شد نشان دهد که دونالد جی. ترامپ (رئیس‌جمهور آمریکا) شش برابر محبوب‌تر از آبراهام لینکلن (رئیس‌جمهور شانزدهم آمریکا)، جرج واشنگتن (نخستین رئیس‌جمهور آمریکا) یا هر رئیس‌جمهور دیگری است. او اعتبار دارد؛ اخراجش نکنید! سی‌ان‌ان را می‌توان با مدیریت و مجریان جدید دوباره احیا کرد، اما MS NOW را نمی‌توان! چون یک برند بزرگ را هرگز نمی‌توان واقعاً نابود کرد!»
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21683" target="_blank">📅 18:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21682">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مرکز اطلاع‌رسانی فراجا : الف.ل، از سرکردگان شبکه تراستی که طی سال‌های گذشته مبادرت به دریافت ارز حاصل از صادرات کرده بود، توسط کارآگاهان پلیس امنیت اقتصادی فراجا شناسایی و دستگیر شد. بدهی این فرد به شبکه بانکی کشور، ۳۰۰ میلیون یورو معادل بیش از ۷۰ هزار میلیارد تومان است. این فرد تاکنون از اجرای تعهدات خود امتناع کرده و متواری بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21682" target="_blank">📅 17:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21681">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPhs3x6EoCo2KZrJKED2yYJIPOr9DVxdyHXJbYbEE6ZEEusM-onMjzMjKEqern5r6eArM_q1IkLK90doobXDeQRvNu3fWMTZ8m1W4ehadDD4A7Nke0NKIMy40jCmEgSZ87RJR0-ONLJrqkEtS4uI7m0XeMZX5yzd14bGfWA-jOZHlD1WO02KLJpifQEf5_wxHe_vxxOKUD_tEnDTXI0q6vvMYxiBmtcXrg63cJzfe1MkxzfNFXTc70n-3tcTjpl3AwFkA7YW045W02LIoFS99X3W8jn7jemgt0wGMsClQAKq7VF8E8m4p6jmiLmtb4YTupU9MA565Ns2fxd2ZB17Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت کارکنان ناو لاوان به کشور پس از 7 ماه
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21681" target="_blank">📅 16:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21680">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خبرنگار وال استریت ژورنال:
هیچ چیز به اندازه احتمال ادامه حمل و نقل دریایی هدایت‌شده توسط آمریکا از طریق تنگه هرمز، به اهرم فشار رژیم آسیب نمی‌رساند. اگر این امر ادامه یابد، اوضاع را تغییر خواهد داد. اگر چنین شود، اوضاع بسیار بد خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21680" target="_blank">📅 16:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21679">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCZKPXa6AGpagQRvQ10N1DI70Mo6SWPobSErBBNyiSPVYoAuuTmSmqRP5r4KhzLQ81TKXGhVt7jjiM7GSiVMgozAsxhWg1CmS30p2l7WWCHc5yuhteN7cVSrGFcKaEO3c7EChhW1cOwlTLN2WqJvJBFsz2JoGD8WE76I8rVCSe_DiH8MyClj0Cpdho76_ILn__vtb7blRR7i3aRnMTw_1RJCgV1BXMClOrSu8DzdTxUUm5Qc2jd_TXt6mTvJGHiUfl2jurLmB1-iJRoxujskD3satR2ZFQoZ67vSMlBN3NidEl0y0Ui5Wvx8PCYsdkOyqUnR5Y7Pb0o-jIasIM2e9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر ماهواره‌ای از بقایای ناوچه‌های جماران، نقدی، بایندر و چند شناور دیگر
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21679" target="_blank">📅 15:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21678">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اتاق جنگ با یاشار : شکاف و درگیری در  بدنه حاکمیت
؛ تنها ساعاتی پس از آنکه مجتبی خامنه‌ای در پیام خود به مناسبت هفته دولت تأکید کرد بیان ضعف‌ها و کاستی‌های کشور در شرایط جنگ می‌تواند به دشمن روحیه بدهد و به انسجام جامعه آسیب بزند، مسعود پزشکیان در گفت‌وگوی تلویزیونی تصویری کاملاً متفاوت از وضعیت اقتصادی ارائه کرد و گفت: «پول و درآمد نداریم» و دولت با کمبود منابع مالی و ارزی روبه‌روست و مشکلات کشور بیشتر شده است.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21678" target="_blank">📅 15:06 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21677">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">رویترز: جنگ و تشدید تحریم‌های آمریکا فشار سنگینی بر اقتصاد ایران وارد کرده است.
مقام‌های ایرانی برای نخستین‌بار در این گزارش به ابعاد قابل‌توجه فشار اقتصادی اذعان کرده‌اند؛ مسعود پزشکیان می‌گوید تجارت خارجی ایران به دلیل تحریم‌ها و محاصره دریایی آمریکا حدود
۳۵ درصد کاهش یافته
و تورم سالانه نیز به
۶۶ درصد
رسیده است. مجتبی خامنه‌ای هم از دولت خواسته برای مقابله با تورم، بیکاری، افزایش قیمت‌ها و مشکلات بازار اقدام جدی انجام دهد
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21677" target="_blank">📅 14:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21676">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Afp72_ymQmuquRpUw_1xOPevUhjUatfTFVRufVPwqYxpMMWlRZ401Hn54Ti1fI2Qt-ig7V8S3WkF9oALcAlpxQ2F6WkJ3fS_SYNqneSIOk35-6cAqEAS2d2JUN5qLMJrvjjUXSfQN2nRg9RYkIOVr1n6Fpqcz9DuyZIgzf4FeH8R2X9xXazy8CSjf2Ap0vumjpPejZxC_ZKkFmoAzWDqV4hp7kY3UuL8sRF6NZUuIRS7YmBtQPNsfsFSn4jGhuhGeUnfe5EImjPW5Gt1eoJU9leRjV9BUnce7rhvQVOseV-HBI92mQ0SKYRBesLs_dNoHDYHmdWWNwB-aSUkjRBjrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب، یک تانکر نفتی به نام "ELLIE" تلاش کرد تا از تنگه هرمز عبور کند و از مسیر جنوبی استفاده کرد که توسط ایالات متحده پشتیبانی می‌شد، اما این تلاش ناموفق بود و تانکر به عقب بازگردانده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21676" target="_blank">📅 13:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21675">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خبرگزاری هاآرتص در تحلیل‌ خود درباره وضعیت ایران، با اشاره به تضعیف موقعیت جمهوری اسلامی، افزایش فشارهای داخلی و خارجی و نگرانی‌های فزاینده در میان مقام‌های حکومت، ارزیابی کرده است که احتمال به خطر افتادن بقای جمهوری اسلامی نسبت به گذشته جدی‌تر شده است
@WarRo</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21675" target="_blank">📅 13:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21674">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مؤسسه نیروی دریایی آمریکا USNI : گزارش داده است که ناو هواپیمابر تئودور روزولت CVN71 و ناوگروه رزمی آن در هفته‌های آینده از سن‌دیگو حرکت کرده و برای استقراری بیش از هفت‌ماهه در خاورمیانه آماده می‌شوند. فرمانده ناو نیز خدمه را برای مأموریتی حدود هشت‌ماهه آماده…</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21674" target="_blank">📅 13:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21673">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نرخ دلار ۲۰۷،۰۰۰ تومان(سقف تاریخی)
دلار کف بازار ۲۱۰ هزار تومان(سقف تاریخی)
تتر ۲۰۴،۰۰۰ تومان
بیتکوین ۷۷،۶۳۷ $
انس جهانی طلا ۴،۴۵۳ $(آخرین قیمت)
نفت برنت  ۸۸،۱۰$(آخرین قیمت)
@WarRoom
۱ ظهر تهران</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21673" target="_blank">📅 13:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21672">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">الجزیره : ترامپ ترامپ می‌خواهد سایه جنگ ایران را از انتخابات کنگره دور کند به افکار عمومی داخل آمریکا و بازارهای جهانی اطمینان دهد که منابع انرژی دوباره با قیمت‌های قابل‌قبول در دسترس خواهند بود و ایران دیگر این سلاح مهم، یعنی تنگه هرمز، را در اختیار ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21672" target="_blank">📅 12:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21671">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">استیون میلر، مشاور کاخ سفید:
تنگه هرمز برای ایالات متحده باز و برای ایران بسته است!
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21671" target="_blank">📅 12:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21670">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">فرمانده مرزبانی فراجا از کشف ۳۸ قبضه سلاح جنگی با اشراف اطلاعاتی مرزبانان در غرب کشور در مرزهای استان کردستان خبر داد.در این عملیات، ۳۸ قبضه سلاح جنگی شامل ۲۰ قبضه کلاش و ۱۸ قبضه کلت به همراه ۳۹ عدد خشاب و یک هزار و ۳۵۰ عدد فشنگ جنگی و یک دستگاه بیسیم کشف و ضبط شد.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21670" target="_blank">📅 11:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21669">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ در‌تروث مدعی شده آمریکا با ونزوئلا به یک توافق تاریخی نفتی دست یافته که بر اساس آن، بخش خصوصی با حمایت دولت آمریکا کنترل اکثریت بیش از ۶۵ میلیارد بشکه ذخایر اثبات‌شده نفت ونزوئلا را به دست می‌گیرد؛ به گفته او، این قرارداد بدون هزینه برای مالیات‌دهندگان…</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21669" target="_blank">📅 11:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21668">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ در‌تروث مدعی شده آمریکا با ونزوئلا به یک
توافق تاریخی نفتی
دست یافته که بر اساس آن، بخش خصوصی با حمایت دولت آمریکا
کنترل اکثریت بیش از ۶۵ میلیارد بشکه ذخایر اثبات‌شده نفت ونزوئلا
را به دست می‌گیرد؛ به گفته او، این قرارداد بدون هزینه برای مالیات‌دهندگان آمریکایی، ذخایر نفت آمریکا را بیش از دو برابر کرده و در آینده باعث افزایش عرضه نفت و کاهش قیمت بنزین در آمریکا خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21668" target="_blank">📅 11:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21667">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وال‌استریت ژورنال به نقل از منابع آگاه گزارش داد دولت
ترامپ
به میانجی‌های مذاکرات ایران اعلام کرده است که
هیچ علاقه‌ای به بازگشت به چارچوب تفاهم اولیه‌ای که در ژوئن با ایران شکل گرفته بود ندارد
.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21667" target="_blank">📅 10:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21666">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وال‌استریت ژورنال به نقل از مقام‌های آمریکایی گزارش داد واشنگتن با سرعت در حال انتقال مقادیر زیادی مهمات، موشک‌های رهگیر و تجهیزات نظامی به خاورمیانه است تا توان نیروهای آمریکایی و متحدانش برای مقابله با تهدیدهای احتمالی ایران تقویت شود. این انتقال شامل سامانه‌های دفاع هوایی و موشکی، از جمله رهگیرهای پاتریوت و تاد، از نقاط مختلف جهان به منطقه است. مقام‌های آمریکایی می‌گویند این اقدامات بخشی از تلاش واشنگتن برای تقویت حضور نظامی و حفظ آمادگی دفاعی در برابر هرگونه اقدام احتمالی ایران است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21666" target="_blank">📅 10:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21665">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نیروی دریایی سپاه انقلاب اسلامی: رویکرد ما در مورد تنگه هرمز تا زمانی که اقدامات آمریکا متوقف شود و این کشور به تعهدات خود عمل کند، ادامه خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21665" target="_blank">📅 02:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21664">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1WM7wIBpRIIJYIiwNR70IV92d4R9aJLpleYn-6gJEPfTXwBqjYYF5lt5MKN2jrZhsbKZtZ4gVINdj5vdIgaXPRoFb5r3fUVYS0IJH7-RtEB5DxfoKtrcJ0pQ7xJJJ0nnTFmzotGQ8KglDpLhUN-jLvNq-QhIuclJDlwVGTLJhTT_DsII7nEXkTWGwqg6wXx8QqRA-8KxFhqCsp1Fat3GJR2iCrBLflxf6np3iLmzRwcDWIsmuCk554UZtQO_SE6HJrkAOKGymdm0f564TGjK78p76zRcWfujbATJc01BigDSdXS4-FhTWuqZFUAHOdEeSVypXCT7W_SR3uxv43itw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای جدید نشان می‌دهند که یک عملیات لایروبی مخفی برای ایجاد یک مسیر دریایی جدید در سمت عمان از تنگه هرمز در حال انجام است.
این مسیر دریایی حدوداً 1600 فوت عرض و عمق طبیعی آن تقریباً 93 فوت است، که نیازمند لایروبی محدود برای عبور تانکرهای نفتی بزرگ است.
آمریکایی‌ها می‌گویند که کشتی‌هایی که از این مسیر عبور می‌کنند، به دلیل جزیره مسندم و انحنای زمین، خارج از دید ایران باقی می‌مانند!
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21664" target="_blank">📅 00:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21663">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اتاق جنگ با یاشار :  امشب مارگاریتا زدم
😁
ببینیم چی‌میشه … بیداریم
⚔️</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21663" target="_blank">📅 23:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21662">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18d571649.mp4?token=BId2FEoLP6eA8yME3ViP5eYaX-h3ACPmT7RPt4C67hvmGmyaIWqPBIaoKHbVBCBSY8BJNrgLy_zBRrCpmUjdAXfHwOFWWIImnBI50aei9iExqsMzV0RvzyQWxGgbhTxbb7KqkBVLTyBzeQFXgCmM_b57yLo661yvs-QqpL_4_-PNBZ9sGiJujm2kW3CLM__Hcp7hCxqZ_6D_BbxWvkPcUcsZGkxJX5Sdpjn3H9eoxg_TVRXmOHKRanryCI6VNQglCQnL_FXb-JBpeBMSYLZPFqghvBk4C_xP2lKKHMd13AzPSyoddr-ZNVoFRArTTpgYZOhwSUvgZTwqsbG60HWbhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18d571649.mp4?token=BId2FEoLP6eA8yME3ViP5eYaX-h3ACPmT7RPt4C67hvmGmyaIWqPBIaoKHbVBCBSY8BJNrgLy_zBRrCpmUjdAXfHwOFWWIImnBI50aei9iExqsMzV0RvzyQWxGgbhTxbb7KqkBVLTyBzeQFXgCmM_b57yLo661yvs-QqpL_4_-PNBZ9sGiJujm2kW3CLM__Hcp7hCxqZ_6D_BbxWvkPcUcsZGkxJX5Sdpjn3H9eoxg_TVRXmOHKRanryCI6VNQglCQnL_FXb-JBpeBMSYLZPFqghvBk4C_xP2lKKHMd13AzPSyoddr-ZNVoFRArTTpgYZOhwSUvgZTwqsbG60HWbhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: اونایی که میگن تحریم تاثیر نداره عقلندارن
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21662" target="_blank">📅 23:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21661">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BV2q0fY_YkJt1o_5hzQXMJOfuJVh9Otc9cMLgDdTfAZPmpVTleqPjxctoJhzGoOA3EQN554uBTUTyWrNZVTSoEgkZqoYPIL1QyV3CNv-oR0AaniBvCHh93suCZWYSTuo5VjvjEQB8NJBBPWs2N3my7oY_SeCu54IVUHVmowsw8bcTCBdlwo3PSH53HAkclf7CTyFjaLXCOgzmGsGLU4If94L-0SG1ANwcuulvl2_25t2A0GiZDaqjtdxozUy1Fd9xsqgTZ7XRVMWgJqnheSVGct1HasiFvjJ-hzkoGiiAeSy3eFusI2jWy8aGePmeyq7GebDogtO04wCTQHWeKojxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : مخفیگاه دقیق: سه تا موشک/پهپاد ساعت نزدیکای ۲۲ از نزدیک مدرسه پرتاب شد یه تونل دارن فقط چند صد متر با خونه ها و مدرسه فاصله داره یه جاده اسفالت فرعی هست رد میشه  صد یا دویست متر بیشتر با محل پرتاب اینا فاصله نداره..سیریک-بمانی @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21661" target="_blank">📅 23:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21660">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دیدبان اتاق جنگ : مخفیگاه دقیق:
سه تا موشک/پهپاد ساعت نزدیکای ۲۲ از نزدیک مدرسه پرتاب شد یه تونل دارن فقط چند صد متر با خونه ها و مدرسه فاصله داره یه جاده اسفالت فرعی هست رد میشه  صد یا دویست متر بیشتر با محل پرتاب اینا فاصله نداره..سیریک-بمانی
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21660" target="_blank">📅 22:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21659">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مسعود پزشکیان هم اکنون اعلام کرد نرخ سوم بنزین، از ۵ هزار تومان به ۱۰ هزار تومان افزایش پیدا می‌کند.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21659" target="_blank">📅 22:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21658">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دیدبان اتاق جنگ : سه تا پهباد بودن یکی افتاد نزدیک ساحل
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21658" target="_blank">📅 22:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21657">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjYHcWtXyzYBk7xrapO_ADMsasY3AcvcvWUuZJJr5uXuunV12LoedeHc34RlOJ1ViZpqKeLjBqrsVV50FM45BijgeLo0ZwHlN9C1fCKIYcKakjUon3SQKe8YJsuUUh2iNRnLdc8gT7IB0c7j-WUiWjpYu7wmZaJip1VEADLhAor6d3jHEGIgwRZa10XhWvFf_BzBsVDR5s3iHAwe3wFff1bkYxInG4BzNvmuY5Wl8vk47evdmZvAOfIxU_YLxJVNk2UUXZTT9wIrwrIOggE17FXbPwzCZ3-J22zJwFQkTqrs4DpparKd53rQj0FoK2XC5jkeRWerfURakxToOEnKXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی در تنگه هرمز در آتش میسوزد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21657" target="_blank">📅 22:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21656">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گزارش ۳ پرتاب از سیریک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21656" target="_blank">📅 22:10 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21655">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گزارش ۳ پرتاب از سیریک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21655" target="_blank">📅 22:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21654">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مستند و مصاحبه جنجالی کامل تلویزیون إسرائيل با یک نیروی ایرانی ویژه در موساد با نام مستعار آرش در داخل ایران ( در این مستند صحنه ها بازسازی شده اند ) که در طول جنگ۱۲ روزه نقش مهمی را در انهدام سایت های پدافندی جمهوری‌اسلامی ایفا کرده بود. با زیر نویس فارسی…</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21654" target="_blank">📅 21:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21653">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کرملین
: پوتین ۱۰ شهریور با پزشکیان دیدار می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21653" target="_blank">📅 21:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21652">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">موشتبی ای آی : گاهی اوقات، بیان صادقانه نقاط ضعف ما، کمک بزرگی به دشمن است.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21652" target="_blank">📅 21:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21651">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52453c0c98.mp4?token=QoVMY85hPCQSUFiX85kuBMg_pZOwLY1j8KSVvY12mkOa6CbchqsHoSq_cnyIv0cSXF3SEcjOk8vnDucXww7G7ATMsUqCPohbes-MiQxVoTWn_wsvfK8QuEcoS7OsTZTNYb220sjB0uFvxwytGO0Z-zIFh-iYavqiT5jytkSyJLES40hMXZCO35dsVEDN1vjJhBooe47ax-YPeYdgvU1RibKuR9ep2sg4TAgE-JFuhnx4i4jk4VR-f3N39SX2sz7Kgk1I6fTmgriOoPxzWj_pDjxeyjDhXtsosXzW-Kn9CRGRih26dgAkiM_wRPq3z9o1z3mVoSkzPOOniGNjgb8wgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52453c0c98.mp4?token=QoVMY85hPCQSUFiX85kuBMg_pZOwLY1j8KSVvY12mkOa6CbchqsHoSq_cnyIv0cSXF3SEcjOk8vnDucXww7G7ATMsUqCPohbes-MiQxVoTWn_wsvfK8QuEcoS7OsTZTNYb220sjB0uFvxwytGO0Z-zIFh-iYavqiT5jytkSyJLES40hMXZCO35dsVEDN1vjJhBooe47ax-YPeYdgvU1RibKuR9ep2sg4TAgE-JFuhnx4i4jk4VR-f3N39SX2sz7Kgk1I6fTmgriOoPxzWj_pDjxeyjDhXtsosXzW-Kn9CRGRih26dgAkiM_wRPq3z9o1z3mVoSkzPOOniGNjgb8wgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
:
می‌بینید که چقدر خوب می‌جنگیم. ما بسیار خوب می‌جنگیم. به ونزوئلا نگاه کنید. فقط ۴۸ دقیقه!
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21651" target="_blank">📅 20:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21650">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f934b07069.mp4?token=KT00FqBifObUDT_3iBN2FG1ao-sqUfHkGlPTKAuF_XTl2Jahno5FhpzSXyCHlmpUY6qdi54MOqq4tgcpczKVI9cLWaHz8lPEa-UKjon5KQe1B4EiOQv8jlBv9d8lLsHhKSoGFG48a_U1lH2BspTtPanXsHkjL-mcKj3MQSPEBKXZOzDMBDrL4B2w4mkWVhpHEtC63tddh7AvlWWXls8fW4aO6uf129ZkifTbkmPGF7ncfM6tjUeMR-ib79x817rKfjMFTPKhPWbz3QcWXWWtveWp4B9n2TotE_gbIP566YASbiRL5fKe4DWCXmntogVUzOmy2cVBm6Ht6vyI7JDsvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f934b07069.mp4?token=KT00FqBifObUDT_3iBN2FG1ao-sqUfHkGlPTKAuF_XTl2Jahno5FhpzSXyCHlmpUY6qdi54MOqq4tgcpczKVI9cLWaHz8lPEa-UKjon5KQe1B4EiOQv8jlBv9d8lLsHhKSoGFG48a_U1lH2BspTtPanXsHkjL-mcKj3MQSPEBKXZOzDMBDrL4B2w4mkWVhpHEtC63tddh7AvlWWXls8fW4aO6uf129ZkifTbkmPGF7ncfM6tjUeMR-ib79x817rKfjMFTPKhPWbz3QcWXWWtveWp4B9n2TotE_gbIP566YASbiRL5fKe4DWCXmntogVUzOmy2cVBm6Ht6vyI7JDsvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«رویای آمریکایی دوباره بازگشته است؛ فکر می‌کنم این بار قوی‌تر از هر زمان دیگری بازگشته است. در حال حاضر شرایط برای ما بسیار خوب پیش می‌رود.»
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21650" target="_blank">📅 20:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21649">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2130ad167.mp4?token=q-u4gA8NJKnqJfxrGTPw4pHikOxphuPHWT35lLIuSDteAxcoIFTGaEYGqOBL8VTbhefL8EVjekPp0weoNcAzEz_dp11nq4shJuT1qvTWUrJTDnE8OB_rIg37fDfyJGWdzl1WexALTXEDZCiZ_rXhM6QJwHSwZky1P4inj1vgxWA-xDkVEOdTRE4ZJggFzIUfl0ifBSEnuE35QOgdi5IzcQig2awDMhqauc5Q-qb_vpvso1jea5ffoRvGKAyoBqvP25hOreqGddsWolkrgKIHeHwUzVZwh5pxy82GpRLcfoMS_99_VI4rdmYu5JeIwwcro5i36_FK-UXIQZk9R9ny0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2130ad167.mp4?token=q-u4gA8NJKnqJfxrGTPw4pHikOxphuPHWT35lLIuSDteAxcoIFTGaEYGqOBL8VTbhefL8EVjekPp0weoNcAzEz_dp11nq4shJuT1qvTWUrJTDnE8OB_rIg37fDfyJGWdzl1WexALTXEDZCiZ_rXhM6QJwHSwZky1P4inj1vgxWA-xDkVEOdTRE4ZJggFzIUfl0ifBSEnuE35QOgdi5IzcQig2awDMhqauc5Q-qb_vpvso1jea5ffoRvGKAyoBqvP25hOreqGddsWolkrgKIHeHwUzVZwh5pxy82GpRLcfoMS_99_VI4rdmYu5JeIwwcro5i36_FK-UXIQZk9R9ny0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی های
ترامپ:
«راستش من دوست ندارم با آن افرادی که پشت سرم هستند(ناسا) صحبت کنم؛ چون بیش از حد خوب به نظر می‌رسند!»
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21649" target="_blank">📅 20:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21648">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا: وزارت خزانه‌داری وعده داده بود تمام شریان‌های اقتصادی باقی‌مانده برای تهران را قطع کند و به تهدید رژیم ایران پایان دهد. او تأکید کرد حامیان ایران نمی‌توانند همچنان به دلار آمریکا و نظام مالی جهانی دسترسی داشته باشند. بسنت…</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21648" target="_blank">📅 20:28 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21647">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وال‌استریت ژورنال: پروژه عظیم «نئوم» عربستان متوقف شد
وال‌استریت ژورنال گزارش داده است که پروژه چندصد میلیارد دلاری «نئوم» عربستان، به‌دلیل هزینه‌های بسیار سنگین، مشکلات تأمین مالی و بازنگری ریاض در اولویت‌های سرمایه‌گذاری، عملاً به حالت توقف رسیده است.
بر اساس این گزارش، بخش‌های مختلف این طرح جاه‌طلبانه نیز در ماه‌های اخیر با کاهش مقیاس، تأخیر یا لغو روبه‌رو شده‌اند؛ اتفاقی که ضربه‌ای جدی به یکی از نمادهای اصلی «چشم‌انداز ۲۰۳۰» محمد بن سلمان محسوب می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21647" target="_blank">📅 18:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21646">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT-Dj9FLpRmqyqBSwUH7dBJtABkgo6YMfMIYobZUp-fmqXFUJ3U1FwsejNeMYzW6RGeNJnqMAPQIv3iiMzrpCgQ3JOZgz0fGmvnJ-WZmAC-aqOgVaEVoC2nwGoYwncDPpnFKobSk8wIVUIxz4eUaHyPPZFslsiysBt6wHmH-IWiIFC0OgPg1y0d8UgVB9jsHg5mufboT65mgJ3DTdeOoG0z9uPIhTbZbXapQoq2Rkn_d_h2eDXlSmJLlMh9JKVSDzPC9fV4sZMf0jMCO4nGQe5YIpaMGjwN_76g82Rm4oi2LkckA-GldywLaG_BHCNVGeIoV_d6yQqNP9A-zdn54-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
وزارت خزانه‌داری وعده داده بود تمام شریان‌های اقتصادی باقی‌مانده برای تهران را قطع کند و به تهدید رژیم ایران پایان دهد. او تأکید کرد حامیان ایران نمی‌توانند همچنان به دلار آمریکا و نظام مالی جهانی دسترسی داشته باشند. بسنت گفت
بانک مصر امارات
این هشدار را نادیده گرفته و آمریکا امروز نخستین گام را برای پاسخگو کردن این بانک به‌دلیل آنچه «حمایت مستمر و فاحش» از رژیم ایران خوانده، برداشته است.
وزارت خزانه‌داری آمریکا:
در چارچوب «عملیات طرد اقتصادی» (Operation Economic Outcast)، شبکه اجرای قوانین جرایم مالی آمریکا (FinCEN) پیشنهاد کرده است
دسترسی بانک مصر امارات به خدمات بانکداری کارگزاری مؤسسات مالی آمریکا لغو شود
؛ اقدامی که عملاً دسترسی این بانک به بخشی از نظام مالی آمریکا را هدف قرار می‌دهد. همچنین
دفتر کنترل دارایی‌های خارجی آمریکا (OFAC)، رضا محمد تأییدی، مدیر بانک ملی دبی، و یک شرکت پوششی مستقر در هنگ‌کنگ
را تحریم کرده و مدعی شده این شرکت در پول‌شویی وجوه برای یک صرافی تحریم‌شده ایرانی نقش داشته است. خزانه‌داری آمریکا این اقدامات را بخشی از تلاش برای
قطع آخرین شریان‌های مالی مورد استفاده حکومت ایران
عنوان کرده است.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21646" target="_blank">📅 18:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21645">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گزارش ویژه فاکس نیوز : ترامپ ‌به فاکس نیوز می‌گوید ایران با افزایش فشار اقتصادی، صف‌های طولانی بنزین و تورم فزاینده‌ای که کشور را تحت تأثیر قرار داده، «برای توافق التماس می‌کند».
وزیر امور خارجه ایران می‌گوید دیپلماسی هنوز امکان‌پذیر است، اما استدلال می‌کند که فشار ایالات متحده مؤثر نخواهد بود و از واشنگتن می‌خواهد که اعتماد را بازسازی کند و به حقوق ایران احترام بگذارد.
در همین حال، مقامات نظامی ایالات متحده می‌گویند که خطوط کشتیرانی بین‌المللی پس از عملیات مین‌روبی در تنگه هرمز باز هستند، زیرا رهبر عالی ایران همچنان از دید عموم پنهان است.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21645" target="_blank">📅 17:54 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21643">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2gzLZFmIz8jsTb6Y8wgLh65bRluSL4GSEN_xw7XM1aAXS264O44BoVM2I3urLVgVpgk13OYpAWpS4C8FTF_yryr5W1_xTLSReQtaRUvNhkZde-xgVJasBHDkHwf4fikjWl6OY9dF1py1rPRqkEDxw-MdgNV9qWSAn8KfXG8WRc6w6k9JtgUQDTDVGUvWoypQiZBv81UkpjhDFpWnFnEpwxLIKS2xmPzFS4zbMfeo7dy5lwcKwzV5mFoqcJk1_er22A5jRYKGXq-C2qPd9llTwNkz6iFB4aZgt03R-fk8Zym9QmXP8zWsf_CRlIIDAtBSmufyWR4T2i9uh-dppfEig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دید بان اتاق جنگ : هم اکنون ستون دود از سمت شرکت کاله آمل پیشتر کارخانه کاله آمل در ۱۵ دی ۱۴۰۴ (۵ ژانویه ۲۰۲۶) دچار آتش‌سوزی گسترده شده بود
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21643" target="_blank">📅 17:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21642">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دبیرکل سازمان بین‌المللی دریانوردی:
حدود ۶ هزار دریانورد در ۴۰۰ کشتی همچنان در تنگه هرمز گرفتار هستند
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21642" target="_blank">📅 16:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21641">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eChCbiif2z7uHPWbh4ZSbMkj9l2kS5r6uxS3lXMe9SWYgbl1ArJ6V1MO7wRZ0a6LVDror9OUxgmuE27IPta67DB6Oh_IcUQjcNrRUcUVepECQbjJA7VoT11te619jF5PHwsR1GcRH-8jqUnwtGZJo4y5kKN0ewtPjqgvwi4mfsUQSmvfXLxe4k0oGGceUlgA4vLQQbhWiWXw8514GtWKc94h29xsrq21dV9llCVTr0GO8g3QHwOyd-4-9t-z4zbiV3tyYV0nqLxqLad8xE8posKiRnem4keoH0YfywAjNDXlkVwtiHXR_vzdIG5uy_YfKmolJahhLtZZxvD4I85kTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : دیگه از اون آدم مهربون خبری نیست.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21641" target="_blank">📅 16:02 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21640">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مستند و مصاحبه جنجالی کامل تلویزیون إسرائيل با یک نیروی ایرانی ویژه در موساد با نام مستعار آرش در داخل ایران ( در این مستند صحنه ها بازسازی شده اند ) که در طول جنگ۱۲ روزه نقش مهمی را در انهدام سایت های پدافندی جمهوری‌اسلامی ایفا کرده بود.
با زیر نویس فارسی
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21640" target="_blank">📅 15:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21639">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovbNmufn9_w3gANwI4i2Y9ZbapBfap8lz8C3A4LORdNrNMoSAsPh16ygFZRiJ-Wp0lIKY0hhP_CVoE0gKi5E3Ub8EobeYd-8ABJD9VIy8CBoepEEa8kwrjHsC8O08j5hyjpRUCMAN9FhGk4_DiqQ_LbRdW4S2JokBN8Cxevu1fPqX4_8PO1XSEvVgPg4opP6CRukwOJczro3KgtiY3O9BSOM1pGHJDglfXEZwMmLvViMyJQsweqjRz97AcCvcn6PMYREMlaPrGBTPZ0l6E-zmnDoFt7LB5T2VmYfoigXrMXVakOOm3p1Xwb6IrRlAFMRMbVVMPg701lEqYhAFnsFyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دید بان اتاق جنگ : من با یه صدای لرزیدن شیشه اتاقم بیدار شدم دوباره خوابیدم  ، بعد نیم ساعت رفتم دم پنجره یهو چشمم به این افتاد @WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21639" target="_blank">📅 15:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21638">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50b72f483d.mp4?token=blhZflKFpnJ0gvpzei7kDq1mrATMQLfci-d0MdYSJ-OIS1YDEKIImJ5MK9o22lbc3I7yuwLbQr5J-SNf6uqAUwB97TLrYJjK0F6AMoDESPOSBadEPef-8-4jc5_AFofSWGcBLUmBVtEFcKp9K7keKB45nlHclvLW84SzNtpZFi3YVAqiM5VmTiaN0MIFjxpAFnhjvEhkkEoLPO0OuEqTAddIiTj1LUMUMvcQu8tQHN3GOLVEYGJU1zkwP81S3Jk7H7ccYS0JP7HJYWgNax4pxMrjlC5yHS-fTZc382HSWlDEvZGH8SP4LUFwNW4FCK2-qr5XowWnDULw5ft8DYtxVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50b72f483d.mp4?token=blhZflKFpnJ0gvpzei7kDq1mrATMQLfci-d0MdYSJ-OIS1YDEKIImJ5MK9o22lbc3I7yuwLbQr5J-SNf6uqAUwB97TLrYJjK0F6AMoDESPOSBadEPef-8-4jc5_AFofSWGcBLUmBVtEFcKp9K7keKB45nlHclvLW84SzNtpZFi3YVAqiM5VmTiaN0MIFjxpAFnhjvEhkkEoLPO0OuEqTAddIiTj1LUMUMvcQu8tQHN3GOLVEYGJU1zkwP81S3Jk7H7ccYS0JP7HJYWgNax4pxMrjlC5yHS-fTZc382HSWlDEvZGH8SP4LUFwNW4FCK2-qr5XowWnDULw5ft8DYtxVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : اگر ایران سلاح‌های هسته‌ای در اختیار داشته باشد، این پایان اسرائیل و پایان مردم یهود خواهد بود. و مهم نیست که چراغ قرمز باشد، چراغ سبز باشد یا چراغ آبی؛ من به رنگ چراغ اهمیتی نمی‌دهم. این برای من مهم نیست. ما باید این کار را انجام دهیم، زیرا در غیر این صورت نابود خواهیم شد. ما دیگر اینجا نخواهیم بود
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21638" target="_blank">📅 15:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21637">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1175422b47.mp4?token=FuIcG65gpheu7G5JIShNe2HP4F8npap4uoJR4kzHyrxqC6XyOdHoRa4hDsG-6ZjxqBeTCCEyzQltQMlr_Jt0_VMJXxKlXHld01ygt6Him8RgZwLxSbRjel-c5yfrWr6yrDyqvF4LYLcqz1gZK_kMcwSCWhL27rAl_eO-gMgHX6o5ZXMXfTEHM-9BGDZQrBXtnJ9CnOBCbvX0Lg0LCHyMuBz1cL4HvhHUBvWoA4IITn7MXEF7ZG62nLdeLK8_CVLJh_fyjowF6tiCaah9tbnZzjpIMAYY8S17G3WJyfGQZKl4eEu4HYZPxjxQZfiz0cXauKOLyKmXlihapRkvaeZJCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1175422b47.mp4?token=FuIcG65gpheu7G5JIShNe2HP4F8npap4uoJR4kzHyrxqC6XyOdHoRa4hDsG-6ZjxqBeTCCEyzQltQMlr_Jt0_VMJXxKlXHld01ygt6Him8RgZwLxSbRjel-c5yfrWr6yrDyqvF4LYLcqz1gZK_kMcwSCWhL27rAl_eO-gMgHX6o5ZXMXfTEHM-9BGDZQrBXtnJ9CnOBCbvX0Lg0LCHyMuBz1cL4HvhHUBvWoA4IITn7MXEF7ZG62nLdeLK8_CVLJh_fyjowF6tiCaah9tbnZzjpIMAYY8S17G3WJyfGQZKl4eEu4HYZPxjxQZfiz0cXauKOLyKmXlihapRkvaeZJCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویری که ادعا می‌شود برای بندر کنگ و لنگه امروز صبح هست.
@WarRoom</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/21637" target="_blank">📅 15:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21636">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca2bad7297.mp4?token=NLH4C1I994sfxg8ekBm3u7jWnV1zOmOkkTOzle6LaB33DK-4Tr8ChD3tgbVAOy8GC91BpUFpZNzf3y9Tb7ficTbvx-iChqwJhCrY2CHgRCCX2whILi3G56LxunGhJR7J8oKc_mMsNzjeVt8iRpcUaKVv1edQlwzS-TQPe0GRaPbx8KSJ7N7rKoufHLQ4o6QgYqAaabfQZ7ZasvdRJp-c_rWkIfgKOCWF-CpnaiwayqtjQG_qmrPe9o2P9gvgC40WFnSXmaQ2ySCFNVbEdf1c2-EDcM7IG23Zg9GGPuQZ0SNRojUcObe4oa8KnCUjPoPbnrkTgJ94SCkaOYZCF7QPHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca2bad7297.mp4?token=NLH4C1I994sfxg8ekBm3u7jWnV1zOmOkkTOzle6LaB33DK-4Tr8ChD3tgbVAOy8GC91BpUFpZNzf3y9Tb7ficTbvx-iChqwJhCrY2CHgRCCX2whILi3G56LxunGhJR7J8oKc_mMsNzjeVt8iRpcUaKVv1edQlwzS-TQPe0GRaPbx8KSJ7N7rKoufHLQ4o6QgYqAaabfQZ7ZasvdRJp-c_rWkIfgKOCWF-CpnaiwayqtjQG_qmrPe9o2P9gvgC40WFnSXmaQ2ySCFNVbEdf1c2-EDcM7IG23Zg9GGPuQZ0SNRojUcObe4oa8KnCUjPoPbnrkTgJ94SCkaOYZCF7QPHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دید بان اتاق جنگ : من با یه صدای لرزیدن شیشه اتاقم بیدار شدم دوباره خوابیدم  ، بعد نیم ساعت رفتم دم پنجره یهو چشمم به این افتاد
@WarRoom</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/21636" target="_blank">📅 14:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21635">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">آکسیوس گزارش داد روزانه حدود
۲۰ تا ۳۰ نفتکش
از مسیر تحت حفاظت آمریکا در تنگه هرمز عبور می‌کنند و حدود
۹ تا ۱۰ میلیون بشکه نفت
جابه‌جا می‌شود؛ نزدیک به نیمی از صادرات پیش از جنگ. امارات، بحرین و کویت به این مسیر پیوسته‌اند و عربستان و قطر نیز ممکن است به آن ملحق شوند. آمریکا قصد دارد با
افزایش عرض کانال اصلی کشتیرانی تا اواسط سپتامبر
، امکان عبور حداقل
۵۰ کشتی در هر شب
را فراهم کند و در نهایت
۶۰ تا ۷۰ درصد صادرات نفت پیش از جنگ
را احیا کند. آکسیوس همچنین گزارش داد حدود ۲ درصد کشتی‌های عبوری ماه گذشته مورد اصابت قرار گرفته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/21635" target="_blank">📅 14:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21634">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ed644e27.mp4?token=K86J5SekNsqlFjMtsFNEYiJxLl9MnBdHj5b8UQ6BN3yPb19R2-Wg-X4PK3TqkXCG2dAZr5eUa49Rz0ASs0zxWGaPZaREu37reak87C_vI7a9aEV5lt0iHzv4D69Ol8CWk88X-m_jgm3oTOWzpQeDm7miL7j6ZoEhz7rmZAfz8fJhushAg-6z3ouEx8uLRFlHJXfzNmAKNI7ZOC1Y5AgP0Tfa9bvo82tX-WEy8Ch4aW0De9CXoqA5Mjc8ENERqes2X9U8-aEAUQw2G5s2_jW-ckU7soCpOSKkS_Xbaj240RPiGJMpxz0tH7zfOElSlHiFGHPewwm_xy7DLqwntFfT5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ed644e27.mp4?token=K86J5SekNsqlFjMtsFNEYiJxLl9MnBdHj5b8UQ6BN3yPb19R2-Wg-X4PK3TqkXCG2dAZr5eUa49Rz0ASs0zxWGaPZaREu37reak87C_vI7a9aEV5lt0iHzv4D69Ol8CWk88X-m_jgm3oTOWzpQeDm7miL7j6ZoEhz7rmZAfz8fJhushAg-6z3ouEx8uLRFlHJXfzNmAKNI7ZOC1Y5AgP0Tfa9bvo82tX-WEy8Ch4aW0De9CXoqA5Mjc8ENERqes2X9U8-aEAUQw2G5s2_jW-ckU7soCpOSKkS_Xbaj240RPiGJMpxz0tH7zfOElSlHiFGHPewwm_xy7DLqwntFfT5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صف پمپ بنزین پشت زندان رجایی کرج , ساعت ۲ ظهر امروز جمعه
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21634" target="_blank">📅 14:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21633">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نیویورک پست: پسر ترامپ، زندگی منزوی را سپری می‌کند، در حالی که با تهدیدات از سوی ایران و تلاش‌های برای ترور پدرش روبرو است. او به شدت تحت تأثیر ترور چارلی کرک، فعال محافظه‌کار نزدیک به او، قرار گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21633" target="_blank">📅 14:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21632">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پروفسور جان مرشایمر، استاد علوم سیاسی دانشگاه شیکاگو : وقتی فشار اقتصادی یک کشور را تا مرز فروپاشی می‌برد، معمولاً آن کشور تسلیم نمی‌شود، بلکه برای بقا واکنش نشان می‌دهد و دست به حمله می‌زند. مرشایمر با اشاره به حمله ژاپن به پرل هاربر در سال ۱۹۴۱ گفت فشار اقتصادی شدید آمریکا علیه ژاپن و قطع دسترسی این کشور به نفت، در نهایت به واکنش نظامی ژاپن منجر شد.
او درباره ایران نیز گفت اگر تهران احساس کند بقایش در خطر است، به آمریکا و متحدانش پاسخ می دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21632" target="_blank">📅 13:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21631">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آکسیوس گزارش داد آمریکا در نبرد بر سر تنگه هرمز به‌تدریج دست بالا را پیدا کرده است. بر اساس این گزارش، نیروهای آمریکایی با هدایت و حفاظت از کشتی‌های تجاری، عبور نفتکش‌ها از مسیر جنوبی تنگه را دوباره برقرار کرده‌اند و مقام‌های آمریکایی می‌گویند کنترل عملی این مسیر اکنون در اختیار آنهاست. اگرچه حجم تردد و صادرات نفت هنوز به سطح پیش از جنگ نرسیده، اما نفوذ ایران بر رفت‌وآمد دریایی در هرمز نسبت به ماه‌های گذشته کاهش یافته است.
@WarRoom</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/21631" target="_blank">📅 13:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21630">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وزارت امور خارجه رژیم :
تمام کشورها موظف هستند از اعمال تحریم‌های یک‌جانبه توسط ایالات متحده خودداری کنند، و تحریم‌های اقتصادی ایالات متحده علیه ایران غیرقانونی و فاقد هرگونه مبنا هستند.
@WarRoom
یاشار : بابا شما که قوی هستین چرا ترسیدین ، تحریم هم که برکته
🥴</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/21630" target="_blank">📅 13:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21629">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ در مصاحبه با شبکه 12 اسرائیل: این موضوع «تنگه» هنوز باز است.
واکنش ایران بسیار ملایم بوده است. آنها نمی‌خواهند ما دوباره به آنها حمله کنیم، این تمام ماجراست. بقیه چیزها مهم نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21629" target="_blank">📅 13:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21628">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بلومبرگ : قطر در ادامه اختلالات ناشی از بحران تنگه هرمز، وضعیت «قوه قاهره»(حفاظت حقوقی و قراردادی در شرایط اضطراری) برای تحویل گاز طبیعی مایع (LNG) به مشتریان آسیایی و اروپایی را تمدید کرده است. این تصمیم به‌دلیل ادامه محدودیت‌ها و ناامنی در تردد کشتی‌ها از تنگه هرمز اتخاذ شده و بازگشت صادرات گاز قطر به سطح عادی را به تأخیر می‌اندازد. قطر پیش از جنگ یکی از بزرگ‌ترین صادرکنندگان LNG جهان بود و اختلال در صادرات آن، فشار بیشتری بر بازار جهانی گاز، به‌ویژه در آستانه فصل زمستان، وارد کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21628" target="_blank">📅 12:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21627">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گزارش‌ها از سوریه: نیروهای ارتش اسرائیل (IDF) با آتش سنگین به منطقه تپه بت‌ال‌ورده، نزدیک به شهر بیت‌جان در مناطق روستایی غربی دمشق، شلیک کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/21627" target="_blank">📅 12:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21626">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نرخ دلار ۲۰۱،۵۰۰ تومان
دلار کف بازار  ۲۰۰-۲۰۵ هزار تومان
تتر ۲۰۰،۰۰۰ تومان
بیتکوین ۷۹،۷۸۰ $
انس جهانی طلا ۴،۶۰۹ $
نفت برنت  ۸۸،۰۸$
@WarRoom
۱۲ ظهر تهران</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/21626" target="_blank">📅 12:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21625">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">فری استایل یاس به همراه من (یاشار رپفا)
۲۰ سال پیش و زمانه همچنان بی رحم است…
@WarRoom
@RapFA
✅</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/21625" target="_blank">📅 11:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21624">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2BNcrqJtQjbHv8pkusIl2qW9A9JLRR0iUywJSkZzkgqZKQld3NFJ3yFMsAdNIzagGYb0SzHNj0lzQpghyeufRwsP1O14GsRRxmoug5r8jGwamfX4O0lx5WwFSlSaU3HxoSaK-V8pOKhHiv8BHCyw2UcaKG0hgszzizomeroIRkvESGRiGhQ_O3ObE5X4NNQ4ofxkfp37L7LOSml9-wQKfRCnRq0yLWnk83YkcL9LqV9XnUIzYBeyErBNSOJ2MPoOsMHweMY-5qEp5Eddpt5A9jCcYyG65om85Gzo7juESlbAfWoaUFzbATKUD3FmgqHKOazpVjEN5-IngHiXhYZpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی از دیدبان اتاق جنگ : کاری با دست خط ندارم سطح سواد عرزشی جماعت که برای ۹۰ میلیون نسخه میپیچن (اسرائیل)
@WarRoom</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/21624" target="_blank">📅 11:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21623">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آغاز واریز سود سهام عدالت:
سبد ۴۵۲ هزار تومانی: ۴۴۳ هزار تومان(۲.۲۰$)
سبد ۵۳۲ هزار تومانی: ۵۲۱ هزار تومان(۲.۵۹$)
سبد یک میلیون تومانی: ۹۸۱ هزار تومان(۴.۸۷$)
@WarRoom</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/21623" target="_blank">📅 11:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21622">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKrucGbDkgILD7kV0s7_2TSgYk-VNIh45AV-iDdG7Dil_ULZX-i03mxo0yB2iWnuaDy3Rm9kLqlUXou1Ra47g2j-Ojz-tE4abxsJ0PT8rDG_3M1ZkvaFJ-0g1bjWOhyPj4dEbyckhc8Ey2OCw2BL_p2gt2giOYazEorL7CIAzJgtf_SpN0cXgP0GYgm5BPLUHmkEsg9Br276EYMIeSu5B5dKjC7v5aJoAWD5jekeReeIqFvzTFGuTJj7O9IvYayVBHFgEylhlxJValWyBGCUjixm7CFKrKxT_rnMaaYw_0jVVgsQvOa5IBqVcDXKZtjovWHDWS-XWt2ub26kc15vkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث دوباره:  تنگه هرمز در حال حاضر قلمرو جدید آمریکاست
@WarRoom</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/21622" target="_blank">📅 11:07 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21621">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWN53qJZbcBMgfGFT2nSG8QG9gowb1aC6Ts3iAay99ltSALaknU2_v0Sj7wSGk5j_FnBh1yvmXYO4b0bI-9Wpdqq5Lw3KlSub6ykTjyeQn2CZB7qa1bgk6152u-WE73SGuzejaiqhUU_syUJpCpmgD3Vob5jkfy8YJofHcJq-TiHPYkRP-3uHX9XGZ9pq10ElUlEz1pckNIh-xDdmGtxWhoZ1AD5PL-IaqJwo1ykxitRmkUDxOcZkdpS9AaxSx8_9ZJNuqnQ6f0v8k7z-PR_GoA2NdFRfZvOGSMFr2RIkW9NXI0hhoG1KySdooM_2JUVBflursWkLAFN8sJKNcVIOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هارالد پنجم، پادشاه نروژ و مسن‌ترین پادشاهِ در حال سلطنت اروپا، در ۸۹سالگی در بیمارستان دانشگاهی اسلو درگذشت. کاخ سلطنتی اعلام کرد او صبح امروز جمعه ۲۸ اوت، ساعت ۶:۳۵ به وقت محلی، درگذشت. هارالد از ۱۹۹۱ پادشاه نروژ بود و بیش از ۳۵ سال بر این کشور سلطنت کرد. او به‌دلیل کم‌خونی همولیتیک تحت درمان بود و پس از ابتلا به یک عفونت باکتریایی در خون، وضعیتش به‌شدت وخیم شد. پسرش، ولیعهد هاکون ۵۳ ساله، اکنون پادشاه جدید نروژ شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/21621" target="_blank">📅 10:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21620">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دریاسالار برد کوپر، فرمانده ستاد فرماندهی مرکزی آمریکا (سنتکام)، مدعی شد نیروهای آمریکایی از زمان آغاز محاصره بنادر ایران، عبور حدود
۱٬۵۰۰ کشتی تجاری
و انتقال
۷۵۰ میلیون بشکه نفت خام
از تنگه هرمز را تسهیل کرده‌اند، در حالی که به گفته او، ایران اجازه صادرات حتی یک بشکه نفت خام را نداشته است.
کوپر همچنین مدعی شد هیچ کشتی ایرانی بدون اجازه سنتکام وارد یا از بنادر ایران خارج نشده و تنها در موارد بشردوستانه اجازه تردد داده شده است. به گفته او، تاکنون حدود
۷۵ کشتی تغییر مسیر داده شده
و
۳ کشتی
از زمان آغاز محاصره بنادر ایران از کار انداخته شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/21620" target="_blank">📅 10:49 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21619">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
«محاصره و عملیات “
طرد اقتصادی
” اقتصاد ایران در حال فروپاشی l را درهم خواهد شکست. آمریکا طی ۱۴ روز گذشته با مدیریت خود
۱۳۰ میلیون بشکه نفت
را هدایت و منتقل کرده است.
ایران: صفر.
@WarRoom</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/21619" target="_blank">📅 10:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21618">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVSegeEBHrB-kyvJ9FfyIbYTljfKPXdKPtevYuq_dSv8i40R96TNClA-FKEITTymv7xnoMIOcUY1oXyn8kYXAYnqmJ3IekmkpLJfMrwLy7nEd5p8Y8HMCPiCGdkIULTi_kJTFNN_A7yT1877AU9-MKwLGNtm-fhvxNOjfHnJ5at9UmTUIWfwG-IQzxp7r10lK-ikWlULpdbFsBsJIK7Dh7j9ddc46Wlf5O-D9CpGAu9AR0Ir4ZN-4Ztp0Bq4gQ5XFp8Mno9l8GvCsbgeEQKid41lBdenqfYR_zes3FMeuJLbNBwUJlOaLIZn1NOnRIosC2GuL6j0KXsVBwwY_rMcNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ با انتقاد شدید از گزارش جاناتان هانت، خبرنگار فاکس‌نیوز، آن را «بسیار نادرست» خواند و گفت: «من نمی‌خواهم با ایران دیدار کنم؛ آنها هستند که می‌خواهند و برای توافق التماس می‌کنند.» به نظر می‌رسد این یک سوءتفاهم باشد چون هانت در گزارش خود گفته بود مذاکرات مستقیم میان آمریکا و ایران فعلاً در جریان نیست و دولت ترامپ به‌جای مذاکره، در حال تشدید فشار اقتصادی و تحریم‌هاست؛ هم‌زمان کشورهای عربی، از جمله قطر، برای گرفتن امتیاز از تهران تلاش می‌کنند. ترامپ در ادامه از برت بایر، مجری فاکس‌نیوز، خواست «زیردستان بی‌کفایت خود را سر و سامان دهد». بایر نیز در واکنش گفت هانت «خبرنگاری عالی» است و تأکید کرد فاکس‌نیوز اصلاً نگفته ترامپ خواهان دیدار با ایران است، بلکه برعکس، در گزارش به صراحت گفته شده بود ترامپ نمی‌خواهد دیداری انجام شود و مذاکراتی در جریان نیس
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21618" target="_blank">📅 10:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21617">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سازمان عملیات دریایی بریتانیا بامداد پنجشنبه گفت که یک نفتکش در آب‌های نزدیک منطقه «الخصاب» در شمال عمان، مورد اصابت یک پرتابه نامشخص قرار گرفته که باعث آتش‌سوزی در آن شد. @WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21617" target="_blank">📅 09:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21616">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbPlEQb6i7exJvPxn0e3EbPO8s81l-hDAzfOvh0dms0OHZfPUyKw69dBsC_G69M95iSENLgDuo15iorIutl8MzTXnXbpl3cc1nt2fQM92-C6Ffj-Cq_NpwborG7sv2fg0LEoqd3kUvNmoeemvYsVaFDlu4l6JIE6oV9et-iSlZk69Aj6mYQ27YdrXbxs6Z5cQP_8T5VNu7rh7Ovz9OWt0IinQo-0TXqXbsSNpOyr2-cFFLzLZjhsYa8XDu-ciV6qMSOXUV5u_IbFWQ6rLWZa1jD77PcC-40dn6LGJfUYQhG8gPbrXZhybYbete5jRN83HCss78Jt8DUBpDG8r33APA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ایران کشوری رو به فروپاشی است
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21616" target="_blank">📅 09:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21615">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJVe8QZnR7d7LjvVfcjjTf75wnV8xHJJKAWFwcRzA8LKDA4py3vhZyKKY9j-lE18YzF5EwtFoC4hTquVJoP1unnSMaSjSizTRmpOzbCODuMW9ZXFHYKadS6n1qLwUKsQ2gXgsQe1rBbNBiavr-UXMxIysmQMnmUSRQJCpJyR7qvE3UoONIar2L9uVSoguCZ30-5RpWSkB-Dy0UgToeja1jPzO8GgQkBkbIuVMjmlk-BPvgf_qzZGp3pOfNR64qXDvBpM8DGgfxjmogJcjizIAcesUiQnDHDLPvBYHSgXUOyCrzkapyttGVM3Rea4yzdlZKdhKTX8ukT55p97Y6Hvsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶ سوخترسان آمریکایی و ۲ پهپاد در خلیج فارس در حال مأموریت هستند ، بعد از مدتها این حجم مشاهده میشه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21615" target="_blank">📅 00:14 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
