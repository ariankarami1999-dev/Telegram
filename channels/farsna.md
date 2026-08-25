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
<img src="https://cdn4.telesco.pe/file/n_f7BTl6uWhr2O8BBWoCIqkt-IHiqMJfOlZzQw0hA_SnLhzZQTQ5O6SdmZwghuLe0a3bpf6ejfgZm7Mo_bztLTqKLTAGagGEwtnfTW2GJba57meAilGt3bu_gmTeiFpIRu5W8mXxHUeGf6Zwd0dWYTOWMLWJ5KlCnSif-xiWuGKUVJ3f0cfXiePBA_IqsHjmdmgRpYBtvHHevK_UdpCnaigbfW2oJunKA0D7C_9d52IWqM3AOf84c5Dh_MtWZn2QJhYeRUYwHkUqcqlH2IR18fbdO5R5Ah1xBUWC9STKlJ1l_Hm3KPGPG3xq_I9V28QYQfjc3QazJzrF6QooF956lQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 07:36:06</div>
<hr>

<div class="tg-post" id="msg-458109">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzeliqmS2IJEUHoYP84lsBsSKXQhHZTr4qfAMhknEC4G1dBbmKwx9-17ajbWb6d4T31HfuHkIvl7eUBJXXlAswYMxv9TxVFcBAX__BrTDnIGR8e8wtqeduOS-in_K4puOSxFF2kLCi_Ad9PD4tD2r8agtlagxs8TUK7EAA-Zagor53SHDysxQ3yLZpYsnuggR8ubyGFGjpLWM31tMu1Ac9WiCDJo4PPmwzL8EzmU7oaOJo_kS_aT9J7m6gDv_fYfdMa-gXXaJ89aoIbvDBV0k0Qu7lTx_jbPQH6XZEUZSP7A0jmdFP-PyqiCXCALNQzO5_96U-O7UmDzkgJiAOLGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روشن را دیدید، تلویزیون را خاموش کنید
🔹
«آقا پخش می‌کنیما». «بکنید». این دیالوگی است که بین حسن روشن، فوتبالیست پیشین تیم ملی و استقلال و مجری یک برنامۀ یوتیوبی ردوبدل شد. درست بعد از آن که روشن تصویر کارلوس کی‌روش، سرمربی پیشین تیم ملی را دید و فحشی جنسی و کش‌دار داد. او لحظاتی بعد همین را برای ریکاردو ساپینتو، سرمربی استقلال نیز تکرار کرد.
🔹
روشن تنها بازیکن ایرانی است که در تمام تورنمنت‌های مهم فوتبالی برای ایران گلزنی کرده. جام جهانی (۱۹۷۸)، المپیک (۱۹۷۶)، جام ملت‌ها (۱۹۷۶) و بازی‌های آسیایی (۱۹۷۴). او به همراه ایران قهرمانی جام ملت‌ها را هم تجربه کرده و در استقلال هم به قهرمانی رسیده.
🔹
بااین‌حال چیزی که این روزها از روشن در اذهان دنبال‌کنندگان فوتبال مانده، اظهارنظرهای تند، عجیب و غریب و حالا توهین‌آمیزش است. او در این سال‌ها مخالف حضور بازیکنان و مربیان خارجی در ایران بوده. مخالفتی که البته فارغ از درست یا غلط بودنش ایرادی به آن وارد نیست اما روشن حالا پا را فراتر گذاشته و رو به الفاظ رکیک آورده است.
🔹
او با چنین سابقه‌ درخشانی در زمین چمن، بیرون از مستطیل سبز دارد تیشه به میراث خودش می‌زند. وی البته تنها کسی نیست که در این راه قدم می‌زند؛ پیش‌تر خداداد عزیزی، قلیچ و فنونی‌زاده نیز با دُزهای متفاوت با اظهارنظرهای غیرعادی در فضای مجازی خبرساز شده بودند. سؤالی که پیش می‌آید این است که چرا پیشکسوتان به‌جای ارتقای دانش فنی و حضور در پست‌های مدیریتی یا مشاوره‌ای، به کارشناسان حاشیه‌ساز و پرخاشگر تبدیل شده‌اند؟
🔹
سال‌ها ارکان فوتبال از لزوم فرهنگ‌سازی روی سکوهای ورزشگاه‌ها گفته‌اند. اما چه توقعی از نوجوان پرحرارت استادیوم می‌توان داشت وقتی پیشکسوتش چنین ناسزا می‌گوید؟
🔹
برنامه‌های یوتیوبی ثابت کرده‌اند که برای هنجارشکنی، بیشتر از یک تحلیل فنی ارزش قائل‌اند. برای همین است که پس از حرف‌های روشن گل از گل مجری می‌شکفد. او می‌داند همین تکه پربازدیدترین بخش برنامه‌اش خواهد بود.
🔹
حالا دیگر وقتی روشن روی صفحۀ تلویزیون یا برنامۀ اینترنتی ظاهر می‌شود، تنها توصیه‌ای که می‌شود کرد این است که کنترل را بردارید و خاموشش کنید. چون جایی که یک پیشکسوت گل‌زن، به یک فحاش تمام‌عیار تبدیل می‌شود، دیگر ارزش تماشا ندارد.
@Sportfars</div>
<div class="tg-footer">👁️ 191 · <a href="https://t.me/farsna/458109" target="_blank">📅 07:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458108">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMIsdrsBc5tPqtSiHNZexVK8rIle_Bu7J3Cf3VEMI-0VGwyuRIg1DvjCAFB0svh38DZIW4nVphuZZEKoORNkpZpTfCxfaOhKLtT5WAXrH_vZoM9ZtaqoDrQQuP_HUAPOfB9N6D71AU-rZG8pWlzQwaqAhbPm3QgIltN0g1TF5_IKw8jr9YBg3UYhZS58L9nILJvEf9CFNBd8JMmAnjj9-Ynd3PKtnTPrQsvzU19ZTPbOZkz58Z8F_6AJwCNIZ6XnEUPE8ZXwMdL9gr2hFecFdfVt92-qdejKBzjVsJBYFz0upGNXfUmGgrIul-dyQPuHJNpbE_IDB3xyaBLtEyAN_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقاب اصفهانی امروز به شورای شهر می‌رود
🔹
سخنگوی شورای شهر تهران: در جلسۀ سه‌شنبه، معاون رئیس‌جمهور و رئیس سازمان بهینه‌سازی و مدیریت راهبری انرژی به ارائۀ گزارش درخصوص برنامه‌ها و اقدامات انجام شده در حوزۀ مدیریت مصرف بهینۀ سوخت در شهر تهران خواهد پرداخت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/farsna/458108" target="_blank">📅 07:28 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458107">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">طرح مقابله با نفوذ بیگانگان، در دستور کار صحن علنی امروز مجلس
🔹
سخنگوی هیئت رئیسۀ مجلس: ادامۀ رسیدگی به گزارش کمیسیون امنیت ملی مبنی بر مقابله با نفوذ سرویس‌های اطلاعاتی و دولت‌ها یا نهادهای بیگانه در دستور کار جلسۀ سه‌شنبه صحن علنی مجلس قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/farsna/458107" target="_blank">📅 07:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458106">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">آمریکا روادید ۲۰۰ هزار نفر را لغو می‌کند
🔹
طبق اعلامیۀ وزارت خارجۀ آمریکا، واشنگتن قصد دارد ۲۰۰ هزار روادید تجاری و گردشگری که خواستار پناهندگی در این کشور شده‌اند را لغو کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/farsna/458106" target="_blank">📅 06:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458105">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca58c6482a.mp4?token=JJksclH5zLAlOu4Y--gjAuRIMbRAvfG4Oq1Yb29K6kBvcQDqXxRjEYg139BxbogyCAkdEECUgeQSdeOWQ6KF6V6DK7t1pomV6VD3ygW4d_8NyIq6bkbNNtFDftPh6kViawwoek9yLe4T77BRRklnEZCLn6feVlsmh_DaOYEss652hNE9cx1Eqg_erxC58mL9AL00nNeAMikiAGLorGImyPBO9v36qeg86CceGtfjlOm-j6AtuJhj3WmLWjNnIamPDVjKCDJchR03JH6X0BMoCzOsH1DBFwjaKvjQH1LRA771WJzRfZdZ6UyeuAloAxxG9VvfCzXumpcLg36UYRCsaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca58c6482a.mp4?token=JJksclH5zLAlOu4Y--gjAuRIMbRAvfG4Oq1Yb29K6kBvcQDqXxRjEYg139BxbogyCAkdEECUgeQSdeOWQ6KF6V6DK7t1pomV6VD3ygW4d_8NyIq6bkbNNtFDftPh6kViawwoek9yLe4T77BRRklnEZCLn6feVlsmh_DaOYEss652hNE9cx1Eqg_erxC58mL9AL00nNeAMikiAGLorGImyPBO9v36qeg86CceGtfjlOm-j6AtuJhj3WmLWjNnIamPDVjKCDJchR03JH6X0BMoCzOsH1DBFwjaKvjQH1LRA771WJzRfZdZ6UyeuAloAxxG9VvfCzXumpcLg36UYRCsaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملۀ مجدد اوکراین به یک پالایشگاه نفت در روسیه
🔹
هواپیماهای بدون سرنشین اوکراینی  پالایشگاه نفت شهر «آفیپسکی» در فاصلۀ حدود ۳۰۰ کیلومتری خاک روسیه را هدف قرار دادند.
🔹
این پالایشگاه در حملات قبلی اوکراین نیز هدف قرار گرفته بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/farsna/458105" target="_blank">📅 06:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458104">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iyloew-D0oIGxV8QWTaiswdMPXvD698WqqmVxtffqoqlGkW8dKuCMYV98dD8FT8uITA0eBfhLiy4C6vqYBcJnwrqcOH9nYNUFveKySdPWMSChlcMsm4T8Vz1dqPbswfuBWSUtroex_4cf9qq32t2qMxDOFsKXdUU1OHR7JRLOHhygu2tlac5wgubtmPeiprfGflL5Ohm_ujVQnXXW7ezY-nklnM6Ur3lcy3G-wcSFRUWW0wm2uCGhpHZfgjxLMaOf8UyfFgREzK7AfpvH9ALpbpUK7fxF9qAJIe1fICTLdzDevLV4BnRQsxFtgp-BkSY-d29hi0tY3OUidyc1HvLvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌رسانی با سرعت کبوتر
🔹
بعد از سال‌ها رقابت برای سریع‌تر شدن اینترنت و پیام‌رسان‌ها، حالا اپلیکیشن‌هایی ظهور کرده‌اند که دقیقاً خلاف این مسیر حرکت می‌کنند؛ پیام‌ها را عمداً با تأخیر به مقصد می‌رسانند.
🔹
در یکی از این اپ‌ها، پیام با یک کبوتر مجازی ارسال می‌شود و سرعت رسیدنش به فاصله واقعی میان فرستنده و گیرنده بستگی دارد. یعنی هرچه مقصد دورتر باشد، باید بیشتر منتظر بمانید.
🔹
اپلیکیشن دیگری هم از حیوانات مختلف برای ارسال پیام استفاده می‌کند؛ حتی حلزون! هدف، تبدیل انتظار از یک مشکل به بخشی از تجربه پیام‌رسانی است.
🔹
پشت این ایده عجیب، یک هدف جدی‌تر قرار دارد: کاهش فشار ارتباطات فوری، اعلان‌های دائمی و انتظار برای پاسخ سریع. این جریان بخشی از موج «پیام‌رسانی کُند» است؛ جایی که گاهی کندتر بودن، خودش یک قابلیت محسوب می‌شود.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/458104" target="_blank">📅 05:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458103">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86fa6d752a.mp4?token=YXKJamWPmqrCHPQMZ6HBtMGnm0TS-ZzjiFRnV_aF0NNzM2V5Y4G_yu5e99XT5Qoqf1n4syMaMLH5a4y7aTYr6cGWhqBv-lZbpZA6CirISiwAWae6w8vkD_dl_Y4UKc1qwJ1GWLRNgUxbJW89lLWeCF6Ex-Ihq1K7Kl7li6a_BBMo8tmw1xDc55Ekt67Q1pqWKI7ayaomNSXCRZQxXPYMJCYt_T98oEWQHCH7ensKvbom-5Gyr0Q0JUqk5ghyVWGKBTi93XkxqY7pNOqMtuZreVw7gq13rXc3lTD4k9G1C7CyTWlhXx4X8PlnN6t-UTMONmziF0a5LUZ2JC7-6Sqvxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86fa6d752a.mp4?token=YXKJamWPmqrCHPQMZ6HBtMGnm0TS-ZzjiFRnV_aF0NNzM2V5Y4G_yu5e99XT5Qoqf1n4syMaMLH5a4y7aTYr6cGWhqBv-lZbpZA6CirISiwAWae6w8vkD_dl_Y4UKc1qwJ1GWLRNgUxbJW89lLWeCF6Ex-Ihq1K7Kl7li6a_BBMo8tmw1xDc55Ekt67Q1pqWKI7ayaomNSXCRZQxXPYMJCYt_T98oEWQHCH7ensKvbom-5Gyr0Q0JUqk5ghyVWGKBTi93XkxqY7pNOqMtuZreVw7gq13rXc3lTD4k9G1C7CyTWlhXx4X8PlnN6t-UTMONmziF0a5LUZ2JC7-6Sqvxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیرالمومنین(ع): کمک کردن به نیازمند را به فردا نینداز
#اندرز_مولا
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/458103" target="_blank">📅 04:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458100">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qCPUqEyGooJ4ZxZULgOrdzRnUidbpO_VvxpG5DX8GdOJPbY_Rx-249Fu3HEpUwHI7gKbKR18CIX0OOWs3piFv9rxol-3lbs48hAMLz0qIKCiECVjhpiZZhuHUyeKQDkAqEZnxiFUyudGNyxFGu-aXOOYxJeVAG4Qq3p_yJjWRV1hi03aUalY3ZWWTHJOkiRsqJyTEpuYJk3yMKPdxOi6JwK0Zj6WxHcTJ_tqLpE8U9lLqUiHNae0i5v8Sy5GfqOvnUB2xuo3RScAP1JgnCvBydqPinisgZ8ghfribAJgTWqOkKgmWtFP1h107IpCvhEDmGLtlzVbKnUXu0l3m5N3ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g7oVcx6ynl0DDe7nZC0zid-9yb7iNIJuf47LkgGfEH6xEebEQJcKyA86Y-vPaHQywNV1ie1fKwDJZFq9KYmb41wa7q4oPSjECWUEvY7B1JXd2auZB-uoip3r5lssGOsAWZ2un-7wENF4yKZEeWT6J8zLGod5w1X0-WZ8LtGe46MjdyxXlxj5vJSFRWlALf2gMpu71v-i4zBVJwy12WLVF7EN8JwNudkDtSEnsZxepfRTaCvQMmNDFh5ByVOQZmrC4LlonHuIAfnSnvIyHmwUZ0bJWfA03XyfaM07cKPgdOvJcPy9cG11-qMXxCWrHryfj4zVo5pCWjzct9ruwFoddA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qg2MCQjIdxypLFLV1FFatD4jjDpFt6Dm9_cL4yqsltGM66BeqBBnVa1cSiyDbd1jXZw_GGgd4aT4dMx_2iJTeh8Or9vq7AkYgVBzNRbBHgnXGCMP1sAqPQPziCa6QSkmdfTIjVArYhCv4NOm7lItXNozGt7QvWlXhjeOqoIbKStH6PefEZLEk00s78iC1OCiBSsRj1DbffiyCPiU-B-YjtJy8gsiS738frP0MQ1c0CEVnl1FZmdXXapik7YLou9Y6MO4D3hNdkm4Tft7Xs7LkWgptunCjcVpa6ufeMDkV3dpzHOzfMRfGqngocIjydggi7Wkv8-DM5UDYgjBwrdKKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شب‌های پل خواجو
عکس: امین علیجانلو
@Farsna</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/458100" target="_blank">📅 03:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458099">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حملات صهیونیست‌ها به جنوب و مرکز نوار غزه
🔹
المیادین: خودروهای نظامی اسرائیل در شرق شهر خان یونس در جنوب نوار غزه آتش گشوده‌اند.
🔹
صهیونیست‌ها به‌سمت چادرهای آوارگان در شرق شهر حمد، واقع در شمال غربی خان یونس، تیراندازی کردند.
🔹
اردوگاه‌های «النصیرات» و «البریج» در مرکز نوار غزه نیز هدف آتش خودروهای زرهی اشغالگران قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/458099" target="_blank">📅 03:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458097">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jcvb-k-ozV9AyO0bS5-c8PxE_L3KNUWCgDysPW6JQH5wknRD6AP345I0Vcsu27j1ZU5DH3ULYXB7NSB48Pe_jOzZUaq3eg3I_pXuDRHUB2BrGam7CQ1o8LFtL0igyriJru2zZtNNzrxZHCsVhz3RZRQMoKHuHtpGWTM1H1Zf4EbbRVlVWeavaRb6nDQsdHM5AGPhjRbofpjoKitYTtAevrFsDWajhCoP4mAlcv02bMek8srb33gwZFFvx2DPjf3k8fsbsMUKdeZjgPFxxVYkrQxXbYtcrD9KLIgESAsY6j9aJUxLW0-P2Fe6r3mWsr2gvKm9-TbCTX_qQaVNpBETVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کلوچه‌ از بطری پلاستیکی ساخته می‌شود
🔹
پژوهشگران با کمک مخمرهای مهندسی‌شده، پلاستیک «پی‌ئی‌تی» را به ترکیباتی تبدیل کرده‌اند که می‌توان از آن‌ها برای تولید موادغذایی استفاده کرد.
🔹
این مواد در آزمایشگاه با ترکیباتی مثل فیبر و نشاسته ترکیب و با چاپگر سه‌بعدی به شکل کلوچه درآمده‌اند.
🔹
هدف فعلاً تولید غذای روزمره نیست؛ پژوهشگران به کاربرد این فناوری در محیط‌های کم‌منبع مثل مأموریت‌های طولانی فضایی، زیردریایی‌ها و مناطق بحران‌زده فکر می‌کنند.
🔹
البته هزینۀ فعلی تولید بالاست و این فناوری هنوز در مرحلۀ آزمایشی قرار دارد؛ اما ایدۀ اصلی عجیب است: تبدیل زبالۀ پلاستیکی به بخشی از زنجیرۀ تولید غذا!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/458097" target="_blank">📅 02:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458096">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B68u9o__k7hxoORU_HcMt2YmDlh3DJd5XgIMmTP_3QT_RRId6wVhfGKLupEeKbqmLOo630SHYNueHnVSS880LUGoImjFMm_xPhxChuenly7V1fKhO6j2uDAl7K9rD2KlWRqKPSMUFKlUWXBRFh7hbmKqkO4jcoe13KQcmHh3Tcv8-Yp5_pfCFPM4aDK98ofP84E7Xp_ZY2NY13VVUB1180pe7MvCJDoJjgA1O0QNxQ39hnjhmKsMBJeKXcsYQ_4yJlCF0LOaM2OW43Im8OvaIKVb8U91u9X_dpu6Lg6hmIkx5bdROQOmhlM2Rd3HdZt0zSrbPCm8GSkSg44HV1i14A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هدف قرارگرفتن یک نفتکش در تنگۀ هرمز
🔹
سازمان عملیات دریایی انگلیس: یک نفتکش در آب‌های ۱۷ کیلومتری منطقۀ «الشیشه» در شمال عمان، مورد اصابت یک پرتابۀ نامشخص قرار گرفته و موتورخانۀ آن از کار افتاده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/458096" target="_blank">📅 01:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458095">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آمریکا تحریم‌هایی را علیه ایران اعمال کرد
🔹
وزارت خارجۀ آمریکا اعلام کرد که تحریم‌هایی علیه «مقامات نظامی و شبکه‌های ایرانی دخیل در تهیۀ سلاح و حملات سایبری» وضع شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/458095" target="_blank">📅 01:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458094">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ادامۀ حملات رژیم صهیونیستی به جنوب لبنان
🔹
توپخانۀ اشغالگران، ارتفاعات علی‌الطاهر را برای چندمین بار در روزهای اخیر گلوله‌باران کرد.
🔹
همچنین شهرک المنصوری، حومۀ شهرک‌های میفدون و صربین، و منطقۀ دوحه كفررمان نیز هدف حملات توپخانه‌ای اسرائیل قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/458094" target="_blank">📅 01:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458093">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b225fc7a.mp4?token=RWy_nLyOdqUeL1hz4KVTjvKM__50SFQVyFUoZeoawaNivqrVi6Q1TujjwsdAwTH60WN_Lpels0pkDpor1ls4eBIbeh1RAtbyOCdyv3pAWP_Tj67plzHbpnlQTPGgR5eW6kKMFXYortb51cfHp2BU5nqYDS-ULROVd4Dr4ildPo9ybeUQdJmvomKzr0okwI2hsp6zEWTJAZ1izxLDC1tNKCfIx20t1yK2N2CSMaBC8Z06NTN6t-fa0RxzP0qeLvGfLY9wJfsUK0ZfgIrnCsZ-BMlnPHa30Ikw4y-TlnUj_ZkJ8OIcj97FbrdrYwZAl_UIV-xxz3hnJZxhV-IyfxHJP5DLNA2G_L3UWI4zrYA9LywIq3TWU7Op-A7GDAQ6X0mkJuAquJu-7Prcwp8JplJpOjLLUonlqJEBgpKxVvNLlAR8aBbpdb3Wou3mBSaNvCrUq1_UZf2K8nIKVhTf5cXnuW6-5PipLpUh2CAfCdxHpqSeGxi2WQ-vEC8cpjjBHnI9wUjhv1scajtov_r3sYm9_xl6S_zcJ9eUPNZQZHG1KnxfcWANupbgLwqRc76M4ffZ3i43pW3zbctaekqyes-UJZYoBDfknBlXZg9E-rz5c42ubnTQ9BPiFgZD1CC9jcUCzbx24wU80j7GSogvpxjpaCZkE3d9kW5miMtqKKiMg-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b225fc7a.mp4?token=RWy_nLyOdqUeL1hz4KVTjvKM__50SFQVyFUoZeoawaNivqrVi6Q1TujjwsdAwTH60WN_Lpels0pkDpor1ls4eBIbeh1RAtbyOCdyv3pAWP_Tj67plzHbpnlQTPGgR5eW6kKMFXYortb51cfHp2BU5nqYDS-ULROVd4Dr4ildPo9ybeUQdJmvomKzr0okwI2hsp6zEWTJAZ1izxLDC1tNKCfIx20t1yK2N2CSMaBC8Z06NTN6t-fa0RxzP0qeLvGfLY9wJfsUK0ZfgIrnCsZ-BMlnPHa30Ikw4y-TlnUj_ZkJ8OIcj97FbrdrYwZAl_UIV-xxz3hnJZxhV-IyfxHJP5DLNA2G_L3UWI4zrYA9LywIq3TWU7Op-A7GDAQ6X0mkJuAquJu-7Prcwp8JplJpOjLLUonlqJEBgpKxVvNLlAR8aBbpdb3Wou3mBSaNvCrUq1_UZf2K8nIKVhTf5cXnuW6-5PipLpUh2CAfCdxHpqSeGxi2WQ-vEC8cpjjBHnI9wUjhv1scajtov_r3sYm9_xl6S_zcJ9eUPNZQZHG1KnxfcWANupbgLwqRc76M4ffZ3i43pW3zbctaekqyes-UJZYoBDfknBlXZg9E-rz5c42ubnTQ9BPiFgZD1CC9jcUCzbx24wU80j7GSogvpxjpaCZkE3d9kW5miMtqKKiMg-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سربازی بیرانوند باز هم به تعویق افتاد؟
🎙
سخنگوی فدراسیون فوتبال: نامه‌ای روز گذشته به سازمان لیگ رسید که در آن قید شده بیرانوند تا ۳۱ شهریور معافیت دارد اما کارت بازی او چنین بحثی را تفکیک می‌کند. آخرین کارتی که برای بیرانوند صادر شده تا این زمان را پوشش می‌دهد.
🎙
بااین‌وجود یک اما هم وجود دارد. اگر استعلام دیگری از مقامات ذی‌صلاح به سازمان لیگ بیاید، آن کارت به‌روزرسانی می‌شود و وی می‌تواند تا زمان جام ملت‌های عربستان و نیم‌فصل در باشگاهش بماند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/458093" target="_blank">📅 01:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458092">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcxSWKQHXGNtNbcbPNMsEEq8O2-aANsxuJnaXtrJgoBa35S5BS0oaEP9lE0g27fe0BtYPK6CF613B8bsbsFuw-LTrHCQIHjjOLoGF-eo1ydxenvcQa1jFOmLHFh4kgJnpfry_EdwFELVNAyi04edwTMR7bynZLWrhAQ9XhwKj8WlcuDL590j7zh-W3sD1XyK_CCN0d5zhitfRUrzLN4HiznktNsoWs4SS3e7_wSVEfLj5DO5Wst9YLEzSjXqjhOmbyMVXQ95wu0z-Zsd6VIrGsT6pPx0haIWPE50rCMDCMIETrAXBBh-2gzSL5EdinXAlD0E_SQJp_4DXYu1hs9c_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
زاکانی: تغییر چندبارۀ رویکرد جنگی آمریکا بهترین اعتراف عملی به شکست پروژه‌های قبلی در جنگ با ملت ایران است
🔹
در زمین نظامی شکست خوردید. در زمین محاصره به اهداف‌تان نرسیدید. در زمین اقتصاد هم بدتر از گذشته شکست خواهید خورد!
🔹
دست و پا نزنید. خروج از این باتلاق امروز کم‌هزینه‌تر از فرداست!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/458092" target="_blank">📅 01:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458091">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9287a378d3.mp4?token=v0Z7daxlVR3wC6y0CK1ik6rhN-zS1jX3blwM7Um8TbR8CH5gG6B5roU9p6E6NjZK-Qldv9Jk1xjzevb-GqAELvIf_XZ514sffWHz8-DjgIdSFGbtwsv0bwczdQpctbOUL01mABEqyQzl9ONkVvCZ3k5KkLT0HchkCoCyxRMgWwlBj2vlTwmAlP2Hk13JPWo0D-7_yRqE0rEUy_z00mta0x-Mgh4wt5Z_SsRRjr-GE9XG_l6uYdsJV7LSu-DVX_ftriVrKetjIlyNWzCALvn5VqZib3nLziefM7af5U-miqvLDgi9AwNmrA8YF390qKxITJYqNT30gbnsbpfc_o4RzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9287a378d3.mp4?token=v0Z7daxlVR3wC6y0CK1ik6rhN-zS1jX3blwM7Um8TbR8CH5gG6B5roU9p6E6NjZK-Qldv9Jk1xjzevb-GqAELvIf_XZ514sffWHz8-DjgIdSFGbtwsv0bwczdQpctbOUL01mABEqyQzl9ONkVvCZ3k5KkLT0HchkCoCyxRMgWwlBj2vlTwmAlP2Hk13JPWo0D-7_yRqE0rEUy_z00mta0x-Mgh4wt5Z_SsRRjr-GE9XG_l6uYdsJV7LSu-DVX_ftriVrKetjIlyNWzCALvn5VqZib3nLziefM7af5U-miqvLDgi9AwNmrA8YF390qKxITJYqNT30gbnsbpfc_o4RzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین مرگ‌بر آمریکا در رواق دارالذکر حرم رضوی، و مزار رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/458091" target="_blank">📅 00:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458090">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOnMkmdPqM2rJQI2piBviTYXL8VtfrVHQiZWMqGotaOFTA56wdMl9lNfeg_nTPvLlXdXI9AbFhlJYcSXq7FPVG3Cs6bUbJjbnKGcPNDhMUq6X5xamzSlaGx-12yEG1IYcCwWUTsXINihuWChTmlus89yPd5U7EELHqzbNHchTG53ESsZK6ySfJ_AYRcb5BSu0jE36Ow2D-E1VWImeV-QfIhUymcE64COVNjslnxer-eqqJktOhLSCsZQR6ru7Nzkyf93FOh4kIyySDBZZ7rQWGCc5puN95mz-2HxQRsWSysae-a5AkGRdHbBuduLTzimTLWGLWc491qX6gk3i382Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور: مشکل ما مصوبه نیست؛ مسئله اصلی اجرای مصوبات است
🔹
قائم‌پناه در سفر استانی به قم: مشکل ما در بسیاری از موارد قانون و مصوبه نیست، بلکه اجرای مصوبات است. مدیران باید برای تحقق وعده‌های دولت تا حصول نتیجۀ نهایی پیگیری کنند.
🔹
مردم باید ببینند وعده‌هایی که در سفرهای استانی داده شده، در حال تحقق است و پروژه‌ها از مرحلۀ مصوبه عبور کرده و وارد مرحلۀ اجرا شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/458090" target="_blank">📅 00:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458085">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J4PNe2uBCHTzl9P4gEVC18c4o7sBfVXib7e4XLr3zzHRpjKGUQXN43MSoB9xr1mlQXFxBadov6XLQZUzXUkE9yKF_3jXKAeVrBEoYEF5X660UIkgO-nrPNrl7UslIzYWgOvzuwr_4kNodpLu5GhOpA-qn0CMcIB7zBXLeCd8cE_kg54t9Yt_LC6WMf-Win6pNnLfmaS8XqdC4Lg6Xw0UL78Z72OAm4wHwbz14PudqPlkCylD28lTblrSXhAbLGa3x90r8FWNUtynyEGh2Kny4TdgUhLVVbu3gZ2g9_u_bRvnRXdsm3ADNIbX8WYLdtS5vhoyOCMD-CNxa2W_rccB1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kSzeGLlO-KFXYjw_aCDi6zjCG3PWmOOlu9vW_8nZAmvFEwoCRQiS_MMosOy0JJezdfk02Cq-0KVFYktfKWIzUHEbP24bGyn19Oidh8mqsY6YYid0j8m8_7AHEJyB5xHmfrdzAh_s-wtFlfgBtji5lSP7_oUJJHNaX7xt04HtunBWK1AUGb_2swAoj-UOfD7mNpCm1Kphr8VCmFTD_eYeVf32A_43HD9pPoDYFDu3EI4aq7au3bhOd1RFDU0IIMVX3J4_BNMXKeOflXC8dIeDJrA1X2z0oTX2H8Qcba_Ioe_VLy3tJVyFNU7ECGtxwPYpun3OnHMauVyFtpsDYzDV5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/voItS6PHqpwPRf0nPU0Xtd-XOHbo18Nj_x9vRYsL4jsZjppYQMN0JVQwYJ_87oaMRJxiVDL7Dx1N3uhCXyhLbzfl8znnD2tH52tMum9bYd7cYfPRKuYQ84UC3U5AF4-DLi0CejUT9Y16dFzmLh1QHi5PK6z1DiKjgDYXog0yNmibmhiK3WJBWQmspDWwvNtWOkEssmi3KmaWYe4hD_-0grt35cy_SKuQ_V_dDTx_s-vt3JBVWvvQ44fsVqFuOIE7CHCylfAz46oDwbpAghDmdT2NnFz0YQk0_zEp9viyk73M5wEjjac0U1I_VFERw-2SmnGGFz-EkVaR06qrjR2i3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SKgtGAu8487HRLbOguF_UaPBN24KV-qbUpw6WnOL_YHuqhJg6CUyWeWcjWYXguBDpsK7cxl1PTrTL6lUSEHByWVnta45DEIVg7cCA4qAS89NuCXBAVQqwR5RjusZyT4gWqiY3mEeizCRKV_hhgjyHbOXRU5JFfSanOnek4R-NMkwQL5CVkjgRm3c8FeS7wGgXcKeCCzukkLHmoVB0IdZT0G2drKaYdsour8uf1Q2xK1u_0NWKmzp-bdK1LPpOa1cr0r7c3c3l98C4HR6jmiQmiYDLMKHJhU-59nSKbsA390pKXabfTfsZJtuTxtwgSHt12Xti4JCSGuuh0Gegem9Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ag78l1oBzv0Qey5zeQswjsPOE2N1O1JeMPZ4jcEHuoT95YgIWCBzg515v6wP_234m28s4G3jdmaOQyyfg8vTbRLCcyP8KqGkPoOZ0v-ypmva0LowkFBJU9aK3KYAKSPBRXKh4DJ6hY1dvxq_cS7wSAlwMH3JfU4ao5r48Ttp8WleIjT_XX5ZTGA5EB8uAmtGNbGPWcKnJjNO0lCgpydbzK_EvMhaMUDjrKz4z5Bm7RRYGd-Q_zTWISrw4dgO62uALfiSEsmqISRo6OMU9jL7s6oD5hHU7xtNtzM6WPFn-6FxJj4U28c9RejVXeHyAAjCFYWvhkUIQdqBVbhI56cOog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۳ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/458085" target="_blank">📅 00:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458075">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Et1_4ca4MLCcklpjky7xZjo7RkqfNSOZ-vXVefZ3XVhuX_a8Hv4Hh0_4Cq-eeyrAGgs2hE1XQ3YbbcxVrKIHlLXXgFQPDnYpyXJFjhQOVht2r6iCjwtUq0KGiAToBPQoC3t8Lb23LoDsFDZ2V79_I4ZvQz7oAXEHvuQOo6xcT0Xl76C_fpsjGSUz0lCaUNxV28oL4W_Yvf9N87HAOZ6P04bI9dlKJrrA5EgxWbizrvZuu_nMwaDsFAnDsS8JIJJhL-2L3r1_KkI6HWFicN2CbIMXmUShNvfrRNQL89KJM6MgZOL8FJOlbGeZFEnBOtSElv9SUGfn6OzDCg2HdFo0_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNyFpxzFEICJZ-ybEhWq1NQw4dWTB0E0lGKs-X74GLqXNNVD1D6NU1dzVeyGlR1SN4_BKjOO9GKTp6zk6AffAYgt78ovxsMMjwcgQIO65ophiVW4HLg_yn57jxcj8mz9Ra4lXC5-OjG-7FaSerLG8nj8vRiGNQ3UWT6EoUqTPf_ZcN9_8iKxmmTbXisFet0BePS4B1Ng7ZUmVj519QUpayfzjvA2O4NwvI5EpMaBopMx1ap-M6sRyuaRogMhiMvN_KgEvyiYjTDIhDyAUqrk6JL7zabJjw4AkOZSJsa94wsGXu_NG3MxghVS3RPul6zIBbs7LpHrfe0wEAXLeUvx8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k5-rem8VT58TVPwHeQBA7rdi1yvQDKC0OkzsWOIi_Yfg2t3zNrzavwlLr8vA4F5RUHyAzr7U6kgcCRfd7g82dvRCkHAXpcB7ZWSv1AeNWOhdVTW59HLWX5-GGTPQufxeGdsHDZHJuj1xvudlvVdMK6LlEOpQ4BA1fBVyfUazFqdjFl__LwN3G77OmzGbz7nTJ4Qjwco-F_kesG4fWzl1vORdRdl0UCfTVkiSzv3rfJ1c53BjO6zTfW4AldtEaMXTYk2kYtZJcVOwUGfty-Zy9WSrHnPyvH91P4Up6RWP-Cu9L10rrR9dkqv75G2qBi64NYOIPrDctMvIwyhl36TSyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I-EpRdEgjzN-0E9if0-2seHElSnmU3MwspbDfOZokCh_jeO2oFp2DxolHMCiiitIezYZDAX-unpA256n9nz8SNJMJGSf_Im9TxM73eFuIW391Hh5Wc6qrk8bN3APOPWJFtoDGJ9VoF7yagF0H6RXggdecmSbL65Ujz5IvAwIgK2KaumgcNFKPilajPbbZ9JpChb5IAZDFYlVkumbiEtpNds-nko9FepjULHsru0u6TAGgWP8FfHqUwLnGoPo9VfeH2qc2BcmTcFPHykYI24TCHFoU8CKwPHS-zOK5Zdb8uqLClM7SnR5gixWnVi1xkr8WEjX3uncbOQR31BK_o9ZSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cgNxvf2ZU2Srgg7m4PlFqvigJofWT9aItLIxagzLNFeAetAMdr2haln1hZaYpaz45i13k4S61aQR3b_JevGIy9fLvrArQxpqAJ0EQu8TsLAg_aYLD4wu2OdE0JIc0TNM_Eb27EvB21NmDHkXLOjC3WycCyWnS1Hi8G1897baqzLpwh0uz2tl4KQK60SRVPDDyLYhY-2q0B6Z86aNGMAQzwtDWBpCdKEmv-fQafte-rKibQsmumsmfiDfGcsbk2bn-z0BeK-VFUocaI0dodYpLBkUeA12pxWLlVAilr_XV9fhacqBdAYUncEyzqcjPJ6RfRTcMeLhLFDT-8nt5b-amw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BMAaARXVQdzCKl72ByciSst-Q5xDXSk8d6OGMNMQ1AAV9uZinA1Aa-q1WgYsHv6lwhdc1y4jwOsMwTKOKvUU3O9_F65_6-vubMmSSmZPma6hOldVUx_ftIpWak__IOYLa71ah4mAKTn2dHax1Cp62kv-4_L7dPOWESvKdPfolWsot3f4zUHA7stoYdrXsApJMYlBjzTyMmyCboZimH8dOQGLIXu5WVSSC6g5gj2Z8ivS--YNTwl9neDQlJqVhkw-Le3ECUDWEGzDUd3fljHZow4eLvCeIeEpLd_Bt2f9iYetdVqAm5oHfvlzO9mSnKmbrGozpNwkDQKsDg8_opZRCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Co9L9BkfZF6ZxE0zgQ_t2RN_voZJSmysro3kQ3_M6kTUiMuDpjmdotxCzVtmypiFlczT_iioRdRHD_yzPwjST14oIManLbkDVmTDKRN28pB_c3ItJwSemKZXQWw6g4Ddw-WUdCrpMy4yF7tEkzaauCgNYyGN5nkeZRznQwpof_kHV587iXM-t7Nbs7YOMVlOD6AL-H1GPFyUsXo5vk71V3Y4C7vUtJa4Al34Pf0JoXoQOHuafh9kwAmLv4sVuwUdiGNJ1-YY8Tmq6eCRM11Bzaah9wKKXGudkl04TON3Oa8xgwfooWwpckIpnBaV3nqqHojtbKXrvBT4r2nOoCUkUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mTqus2hLuwXPQLS-eZS81gAotpMdNx13HmJPOwSSaCbh5E_grWmwKM6uaGKbp3O3EBS5YsBkfiBOBbY6JlTDjj7s19yFNCH_SwBpMb4bAhk3BF4qDmFpnIt33JZ4Qfu5OoTsxxv8n15cVOWAvhmXmcwb7QdYJ9BGQnNBV0QkyOiRz-d6IZEMVOiyymkeXY3WH6ieOXX2adg_KCUX8DmzTAtfwg_CYO9oiaVDKQ1YO1qaN2_cU3Hr1D4qRCu471xWZTAWc77c4tRK7IyabPgRhEpfpX9MHf_qJX8zdUHAeFNh6WwGT9ZnUbZ3mH1Z7G6piiZ_YDWHRJQY80_OmtGk-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZhBnOQgAwvL85fQoXT6nrpIREpmfICnGYZbgPsUm3hrh--ed5NRc_FcAipRhPpHItyoQF-WIFL2Nnyb3miRouAw04fEmzHA1V3si5myqaWQweE0d7h2kzO-gF5Jy2f6IIEJQK-VWG7WJuGhyV2iqhamXN3KsE8zKQv8aSSR7yGK99eTHmEfgosCDCuXxHlJ0BGWxqnJOUeh0x03m9yThhG4mFk-4iZ5BqBijsOnzwi_F7RuqLjYQW4dPvKmc-i9DpJ6EoKxnFpwjd3CAR4UR3JOa_KQfd7o3KF2IRoZYH__BjcgLoxAwEvMBSHVAhAdQcuGoLDbWqzOE5aD0NG6HNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pE8RiDBoEzt2V94u8wFYPXqMCuKS9Io-4tDkZW4QNgtt69yyIf9e3fN4FF_BUfJB52eqbKX3OsfkKjGRaQg0QCMEwJ0RYam7yTT9q33uZFqLUYGBqlMIj_rThmuo4E8dhD9JslYI0spsksaM_Pd7OASxmXuCevAcnI6xxbTP0LYvmf2j5HVOZqb6cZvbxjPcHpsRgJCPvzmgtcK5ON3cg1kOniv6h6o0aObEEpDQF-Izy0Zrw00RmUqIkDc7M-ErXEnYLK5hklbXaNxiTVUgg3_YX7Qc-q-aFh-wVJpldQy6uB_uPj0Gx9Hb29PkZ0UB-8I3mXsz-kmMHBcGI1Bplg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/458075" target="_blank">📅 00:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458059">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b9f37d892.mp4?token=r0ygulF8TJgNvROsI4PmDIB5Mi_rLcnpQZJPshwDKlxkQMqu3oqs7-nbL9IqmqzKwgOEng_fVa4hiVUyBQxtdbKZdvnwqWZo8Lv83tmdBTtn98UXwCzUKCEnjJqEch4OV3ekv6mdJZnMNecdJ_6HeW4c12zset4TLdW7S-pWHNhWYOGVYfydRMppZMbSdff3848rCRSHrf2pHoKiOClRRfpiOMGXil20EFG__Xgt9h_mpWmse7eVywVTW8AVZGrLq-D3cSIurRl7GuH-LrEdXSFZcJUQxy-THhV1ukJe7s5hd2mkV1n5obRId9N6p4sh3pmWYxFfzcGZQ7zgmvfl-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b9f37d892.mp4?token=r0ygulF8TJgNvROsI4PmDIB5Mi_rLcnpQZJPshwDKlxkQMqu3oqs7-nbL9IqmqzKwgOEng_fVa4hiVUyBQxtdbKZdvnwqWZo8Lv83tmdBTtn98UXwCzUKCEnjJqEch4OV3ekv6mdJZnMNecdJ_6HeW4c12zset4TLdW7S-pWHNhWYOGVYfydRMppZMbSdff3848rCRSHrf2pHoKiOClRRfpiOMGXil20EFG__Xgt9h_mpWmse7eVywVTW8AVZGrLq-D3cSIurRl7GuH-LrEdXSFZcJUQxy-THhV1ukJe7s5hd2mkV1n5obRId9N6p4sh3pmWYxFfzcGZQ7zgmvfl-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دختری از تولد شیرین تا شهادت در کنار پدر  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/458059" target="_blank">📅 00:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458058">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0Ra2QYjf5cs7ZoWmID0Jy5QrtokBJ-fItFhVYk5Q5UnajP4tfG5IZGgrdSkuRmO-wgruYSAjtlfS68IE2ZC87rjREBfxTEEmQ4TWYvqIESEtRkiKReia4Wg_33yC7KoqkjcX-sSXVvbca77KnK_9KFq7tod33nlZtBJPnx_gD93bHHIhYiOcEaGVeAWLzE3TRB3E1O2b5WPjUZjJsiu7tTY0_nih8v5c0e-AUushNZbIKLbQEtd5Xb_uYsEFSQgf2wa0tIndAqHjvzOx4_EJ_B2sVhJOIu9L_X21GBOYUNvHSn2XHNfohIyq-iAjs_bL10s7LDyga7yHY7OKM9xeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقيف محمولۀ داروی قاچاق در بندرخمير
🔹
پلیس شهرستان خمیر: در جریان اجرای طرح مقابله با قاچاق کالا و ارز، مأموران انتظامی از یک خودروی سواری هزار قلم داروی غیرمجاز و فاقد مجوز به ارزش ۲ میلیارد ریال کشف کردند.
🔹
در اين رابطه يک نفر دستگير و با تشکیل پروندۀ قضایی جهت سير مراحل قانونی به مراجع قضایی معرفی شدند.
@Frasna
-
Link</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/458058" target="_blank">📅 00:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458057">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiX1oqupt7supy0DD1xF6_a4jZmDCMR0B0D7zTbwulwfUU8atxkTaSqCS2AKYsLFuHUTuRBOuwFDWE1U7NYXbjo179LiYdv7hFcYFQo9ekxEqXbPO53Bj-ECyNhnUe2Hcgqzi6vD7I7tR3vibeRjQIPY7JwDIPbqYjI9kEqtSb9cv_pEd6g6WFOMpl2u4tCeHLD2LCRGfTVmM0mn57PAcAKp0WjTqD-ObvYvr3oL57W6NVGmDyeVta5kU0BMbOBOkb9ts1f_OnJ3ilwJDFGY0LDurrtB6-zfzd_wnvgrSeoQGm4GNe0eonkXfUS7dttvqHrv3XZm7eDI8fmnWYReHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای شنیده‌شدن؛ خانم‌ها از این اشتباه دوری کنند
🔹
گاهی درد و خستگی واقعی است، اما نوع بیان آن باعث می‌شود به‌جای شنیده‌شدن، فقط احساس گناه ایجاد شود. مظلوم‌نمایی یکی از همین خطاهاست که فرد را در جایگاه قربانی قرار می‌دهد.
🔹
گاهی زن واقعاً خسته و دلخور است، اما به‌جای بیان مستقیم نیازش، جملاتی مثل «همیشه من باید بسوزم و بسازم» یا «هیچ‌کس قدر مرا نمی‌داند» را تکرار می‌کند.
🔹
این شیوه ممکن است در کوتاه‌مدت توجه ایجاد کند، اما در بلندمدت همسر را خسته و دفاعی می‌کند.
🔹
راه بهتر، بیان مستقیم و محترمانه نیازهاست. به‌جای اینکه بگوییم «من بدبختم که هیچ‌کس مرا نمی‌فهمد»، بگوییم: «من این روزها واقعاً تحت فشارم و به همراهی بیشتری از طرف تو نیاز دارم.»
🔹
پیش از گلایه از خودتان بپرسید: «می‌خواهم همسرم دلش برایم بسوزد یا واقعاً بفهمد چه نیازی دارم؟» این دو، نتیجه متفاوتی دارند.
🔹
جملاتی مثل «همیشه من»، «هیچ‌کس مرا» و «من بدبختم که» را به این شکل بیان کنید: «من اکنون احساس ... دارم و به ... نیاز دارم.» قرار نیست دردتان را کوچک کنید؛ قرار است آن را روشن، محترمانه و اثرگذار بیان کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/458057" target="_blank">📅 23:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458056">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcb52a1b4f.mp4?token=Zj4iUESzKW-nrZoFQ35vqabcv4LrsGWrSFzEfBorIIPfR0OmcUj5C_Dwf_giNAF_4h2JP2BrcqjJoCFRv2zR1oTx8OFjUEEVdBeRiFCHUwd1dKK9eX6rZIPBPTGXpcmbn2gLUm0hvCE7J7to3MWMw3dHVJqBoMSjWwdNei201MhSikVlpkekSpUUTwA7-AaeXKbOlDWqCZN1PUCvz63m3d6MvNlGVTB6bM67n4mhYTBV68q7bJEPAw8a22KovP3tr5mzfw1qj78KqACXbFQy48OtqFZMd8fOLvQmSaZYPYoOyZ6biMnGIkQQLNI_TNp8GdPv1g4KJnEzDF0SDdWLdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcb52a1b4f.mp4?token=Zj4iUESzKW-nrZoFQ35vqabcv4LrsGWrSFzEfBorIIPfR0OmcUj5C_Dwf_giNAF_4h2JP2BrcqjJoCFRv2zR1oTx8OFjUEEVdBeRiFCHUwd1dKK9eX6rZIPBPTGXpcmbn2gLUm0hvCE7J7to3MWMw3dHVJqBoMSjWwdNei201MhSikVlpkekSpUUTwA7-AaeXKbOlDWqCZN1PUCvz63m3d6MvNlGVTB6bM67n4mhYTBV68q7bJEPAw8a22KovP3tr5mzfw1qj78KqACXbFQy48OtqFZMd8fOLvQmSaZYPYoOyZ6biMnGIkQQLNI_TNp8GdPv1g4KJnEzDF0SDdWLdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید انقلاب: آمریکا از دوران دفاع مقدس هشت‌ساله در آرزوی تسلیم ایران است
@Farsna</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/458056" target="_blank">📅 23:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458055">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🎥
گناباد در شبی که با عشق و ایثار روشن شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/458055" target="_blank">📅 23:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458054">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7090408440.mp4?token=r68AVXZOAfvpmTMIplUOGkpb6-W5GZMKywx0wRGCEWwVxBWkvyVxEKfrzBoghLY1JFRdOrPdJcNrcM6MPRMdoKcgHQUeVmTg6Fa6ZM_wLGvi2uSAWp0Oag0Qn3AHfpmtG2FjwYrjQZuZ3V6yqXWKOSINVV0zTEp_P1sONwFh5rxB2DRBsJlX_dKLsQEfeAaP9Q1L4YDqexd52IfazxDnuzXmINfpMrojsOK6mc5v7dCLHpTR-TuF--E9FO43jXLl2Phdhs5l_ziQ3rPAiot5pptKkgGMcDcw8kQZJm9K9VOkrPTPBzH-24stzqwIpwZmJmtSAMcIELZjuCk4jATIJg6Z2ss82r_OFX1lkLVMTV8qisofmrzjw05KUxFBdVn74fzQHUesXqvkO8xlJjP2T_z52Aupzh9DDpmSFq7jssg1BqgTDuzA0ONZ0GmbYzHom1FOZp--ZSrEB8yRJPql-OJ7SdfgrKRMOWMiw8NCtHR0rIbxOR7JFy7plpnqPp5vpwAahWiY-uqglJ-W1TlPIsK83iuktyukSXG7qFz4UGXXddLU0z4iRNfgvVTkyGulh82w0CIlBLtbRCLzehQ7sYYRnVutyogRDctahJ71N_zZBFLOvQ4m07wAu03n_911l1560iPGZZ_ZPyTvckC08C5X_FJsuwz9qXVpK6JuSLU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7090408440.mp4?token=r68AVXZOAfvpmTMIplUOGkpb6-W5GZMKywx0wRGCEWwVxBWkvyVxEKfrzBoghLY1JFRdOrPdJcNrcM6MPRMdoKcgHQUeVmTg6Fa6ZM_wLGvi2uSAWp0Oag0Qn3AHfpmtG2FjwYrjQZuZ3V6yqXWKOSINVV0zTEp_P1sONwFh5rxB2DRBsJlX_dKLsQEfeAaP9Q1L4YDqexd52IfazxDnuzXmINfpMrojsOK6mc5v7dCLHpTR-TuF--E9FO43jXLl2Phdhs5l_ziQ3rPAiot5pptKkgGMcDcw8kQZJm9K9VOkrPTPBzH-24stzqwIpwZmJmtSAMcIELZjuCk4jATIJg6Z2ss82r_OFX1lkLVMTV8qisofmrzjw05KUxFBdVn74fzQHUesXqvkO8xlJjP2T_z52Aupzh9DDpmSFq7jssg1BqgTDuzA0ONZ0GmbYzHom1FOZp--ZSrEB8yRJPql-OJ7SdfgrKRMOWMiw8NCtHR0rIbxOR7JFy7plpnqPp5vpwAahWiY-uqglJ-W1TlPIsK83iuktyukSXG7qFz4UGXXddLU0z4iRNfgvVTkyGulh82w0CIlBLtbRCLzehQ7sYYRnVutyogRDctahJ71N_zZBFLOvQ4m07wAu03n_911l1560iPGZZ_ZPyTvckC08C5X_FJsuwz9qXVpK6JuSLU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماهنگ قایم موشک
🎙
باصدای: سعید باقری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/458054" target="_blank">📅 23:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458053">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90c246713.mp4?token=mcjPPEUL6rlhhdMCM3RyBnmL5S347GmCzp_Gq0WNEVSH_8Pt2qvx18tayKAgPU9vjRm6G7GPTgEsULn90jHbnueHWXZWiYGzrXtQ1Bh4kZ1dhoQZYl5YW1uePB0ksG5nCW9vABiUEYV8yVwVLYDrcHT6w54GomTzM4J2vtBJ0uj-6I_2AxE_95ABbuUAM_ux1vzDluGcLq46hWR2cI5g3Ky4ZKTXs5qhHWreFI8ClyD96gDjpQ11PKQK8__V2y8MKVxmDi4Lzip9gTYQBrXnUTuYpr-vj9mXjsyBrTA0Kx0zPn4pBWKCgQbGiILR2aXtK2SQtGzUwuyioZMgKoFoOb0scsKNhyvvppJekFN0rBTYZa-No41WZeyUfwNX63i0z6iAt2FiB5eW2xNyVqqmfauJ-tC8PKqedvRKH_aFD4CVL9Gh4rz8hvtsiD2zjkuM7GpKq-LJ2hIL7TVMcecndFO4ohx-zfdX5qabM3dREakW30V05TNeCGrAizl93sBNJf7O-8X1cXWTwVTldFXAxWsWmLX4wMmDfyYYh0SvH09t3-vznSITTbONZiUd30uR2caEP7UldaIDUi9G4KblS_pMW7XX1DmD6JhtwQDZz70ULiydkaU3MkURnSxpTOpa21aJPPD8p15YrbUC0-nZ6LBR7CQGQkf03j8XO93cDmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90c246713.mp4?token=mcjPPEUL6rlhhdMCM3RyBnmL5S347GmCzp_Gq0WNEVSH_8Pt2qvx18tayKAgPU9vjRm6G7GPTgEsULn90jHbnueHWXZWiYGzrXtQ1Bh4kZ1dhoQZYl5YW1uePB0ksG5nCW9vABiUEYV8yVwVLYDrcHT6w54GomTzM4J2vtBJ0uj-6I_2AxE_95ABbuUAM_ux1vzDluGcLq46hWR2cI5g3Ky4ZKTXs5qhHWreFI8ClyD96gDjpQ11PKQK8__V2y8MKVxmDi4Lzip9gTYQBrXnUTuYpr-vj9mXjsyBrTA0Kx0zPn4pBWKCgQbGiILR2aXtK2SQtGzUwuyioZMgKoFoOb0scsKNhyvvppJekFN0rBTYZa-No41WZeyUfwNX63i0z6iAt2FiB5eW2xNyVqqmfauJ-tC8PKqedvRKH_aFD4CVL9Gh4rz8hvtsiD2zjkuM7GpKq-LJ2hIL7TVMcecndFO4ohx-zfdX5qabM3dREakW30V05TNeCGrAizl93sBNJf7O-8X1cXWTwVTldFXAxWsWmLX4wMmDfyYYh0SvH09t3-vznSITTbONZiUd30uR2caEP7UldaIDUi9G4KblS_pMW7XX1DmD6JhtwQDZz70ULiydkaU3MkURnSxpTOpa21aJPPD8p15YrbUC0-nZ6LBR7CQGQkf03j8XO93cDmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«انتظارات مردم از مجلس انقلابی»؛ صدایی که در شب ۱۷۷ شنیده شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/458053" target="_blank">📅 23:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458052">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0811e8964d.mp4?token=OikkUuNPNjjnIfXEbFKQZfywzwHLHksybzRS_oYUhdycUEr9KkiE0R32u3r25zuCj_xiquuLYVUjrvC3SD4uWkN9O4xo-IelH_Jzn7BDmYqe0aqjr3BbNQSW17XvucP2qSwq9Y1jDsFeS5MgQsxwwUJozXtQad6VImVHSaJzTYgfZs-TzJ2EBg9Su4ecSGJxBblIPLny3mLERASQR7pY2imozb6a1BTZTMKMc3KbrBiqUfpWaURPJZKjBefoB0p8yEtY4mUJBmeBQepydWj1Rux1SK8CYgm1VsjsJT_IBdzsa_flTVZzGLjmwYtRthzKdruLki34wcr8UBRL73_AA36RIm3bcvO3M_GIo-QG_oxb470Hfr9PvY6ZzrTtcYkBPcf6r6lWKLmsSDueWoNE-LI0X3UHdzmsgS2SQmZseXateqIZ34qgu1CtlKm_BQACND-ID5iBN_8Zc2wns2FY8fHBK7TA6WlJLyyM8QCtFw9gbk8I8mWAwyD__z-VDoT5cPDS8c7rnsEVqzMxZnpRcbAQ6Xk6iESPgXs5iKr0rfTUnyyIgzuJpLQhs4hzxD_N2LktcsAljnwnkNDZGsbwvTLuc1de4v-1IIwBp06fx2hKtRE2HXJKsCqa0OQnhun6NQ_BS8kZQY4y1nrUDD8l9gr1LbSaBJb63dEKI_VM3FY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0811e8964d.mp4?token=OikkUuNPNjjnIfXEbFKQZfywzwHLHksybzRS_oYUhdycUEr9KkiE0R32u3r25zuCj_xiquuLYVUjrvC3SD4uWkN9O4xo-IelH_Jzn7BDmYqe0aqjr3BbNQSW17XvucP2qSwq9Y1jDsFeS5MgQsxwwUJozXtQad6VImVHSaJzTYgfZs-TzJ2EBg9Su4ecSGJxBblIPLny3mLERASQR7pY2imozb6a1BTZTMKMc3KbrBiqUfpWaURPJZKjBefoB0p8yEtY4mUJBmeBQepydWj1Rux1SK8CYgm1VsjsJT_IBdzsa_flTVZzGLjmwYtRthzKdruLki34wcr8UBRL73_AA36RIm3bcvO3M_GIo-QG_oxb470Hfr9PvY6ZzrTtcYkBPcf6r6lWKLmsSDueWoNE-LI0X3UHdzmsgS2SQmZseXateqIZ34qgu1CtlKm_BQACND-ID5iBN_8Zc2wns2FY8fHBK7TA6WlJLyyM8QCtFw9gbk8I8mWAwyD__z-VDoT5cPDS8c7rnsEVqzMxZnpRcbAQ6Xk6iESPgXs5iKr0rfTUnyyIgzuJpLQhs4hzxD_N2LktcsAljnwnkNDZGsbwvTLuc1de4v-1IIwBp06fx2hKtRE2HXJKsCqa0OQnhun6NQ_BS8kZQY4y1nrUDD8l9gr1LbSaBJb63dEKI_VM3FY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: برنامه‌هایی برای عملیات آفندی اقتصادی علیه دشمن داریم
🔹
دشمن می‌خواهد در اقتصاد علیه ما آفند کند و ما هم باید آفند کنیم.
🔹
امروز هرکسی حتی یک سنت از اوراق قرضۀ آمریکا خریداری می‌کند در خون کودکان شهید ما شریک است. @Farsna</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/458052" target="_blank">📅 23:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458051">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_6U14lj2fQFluTulCN0oRlpR29hR3v-XnK50WBqlsZ5momzcLUOGhtQD4apCweRo5onTmIHIZTdB8LZm8mtZ_j2qYiRXAikH6XgZNw1fxIZy9F5y1baDBlFocjDb0_8-b44cCBnWS1pL_p3krwCyn5zPJZSUVYT1PURhMNCthAXeez_pmwHWso7upmczX49a3mcp_Zn-rE9EXEUkX9YAkrUeacqoExKovjYi5AbJemMGOzp83uectJVqcepbHlHLcxogwNbu0oA6soV9UcxcwIi7I9dbC7FibFi-ey4FNdc5sYmKIcrxx2yYUN1JWOd7loVaCPWivlmCG0OGd4_mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فناوری موشکی این ناوچه را به سپر دریایی تبدیل می‌کند
🔹
اینترستینگ‌انجینیرینگ: چین یک فروند ناوچهٔ جدید از خانوادهٔ «۰۵۴A» را وارد خدمت نیروی دریایی خود کرده است.
🔹
شناوری حدود ۳۹۰۰ تا ۴۰۰۰ تنی که برای انجام مجموعه‌ای از مأموریت‌های رزمی، از دفاع هوایی و نبرد ضدکشتی گرفته تا مقابله با زیردریایی‌ها، طراحی شده است.
🔹
ورود این ناوچه، بخشی از روند مستمر توسعه و افزایش تعداد شناورهای عملیاتی نیروی دریایی چین محسوب می‌شود.
🔹
کلاس ۰۵۴A که در ردهٔ ناوچه‌های موشک‌انداز قرار می‌گیرد، یکی از پرتعدادترین خانواده‌های شناورهای رزمی چین است.
🔹
یکی از مهم‌ترین ویژگی‌های ۰۵۴A، سامانهٔ پرتاب عمودی موشک آن است؛ این ناوچه به ۳۲ سلول پرتاب عمودی برای موشک‌های پدافند هوایی مجهز شده و از موشک‌های میان‌برد «اچ‌کیو-۱۶» استفاده می‌کند.
🔹
این ترکیب به ناوچه اجازه می‌دهد در برابر تهدیدهای هوایی از خود و سایر شناورهای همراه دفاع کند و بخشی از چتر دفاعی یک گروه دریایی را تشکیل دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/458051" target="_blank">📅 23:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458048">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28636dee93.mp4?token=QVSv1dlhdTlm-k2oK0k75fFUpl-PD4N6Rrp6gaGjoCH5sH0TQ7-8T9TFKqWZUuG7rlpdsV_sBOE3BYDrexxdaczMffl4yYM5bvGTUoPPUe--tFgXDkTCTpKta63MZS3k0Iz8DpeFFdf-UxwtLy8_fGMiLmOXcJCpyIB6ZMn28UtWZ4fo6MzmVF5SBbm0fPv0Rx6hhmygmlanBJhKLtlipqFpz1N2yFOuU4VDA_AgOlaGP6qNm_v6iwzxMjN4bOkYQD-HENd9PWzb2Tt_r8F5hAagFZDJqbA3n5G8DO_KXmnbngegOlPiTlFgIFS121JhcBqJYJd7dcCjnapZ4Hb80w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28636dee93.mp4?token=QVSv1dlhdTlm-k2oK0k75fFUpl-PD4N6Rrp6gaGjoCH5sH0TQ7-8T9TFKqWZUuG7rlpdsV_sBOE3BYDrexxdaczMffl4yYM5bvGTUoPPUe--tFgXDkTCTpKta63MZS3k0Iz8DpeFFdf-UxwtLy8_fGMiLmOXcJCpyIB6ZMn28UtWZ4fo6MzmVF5SBbm0fPv0Rx6hhmygmlanBJhKLtlipqFpz1N2yFOuU4VDA_AgOlaGP6qNm_v6iwzxMjN4bOkYQD-HENd9PWzb2Tt_r8F5hAagFZDJqbA3n5G8DO_KXmnbngegOlPiTlFgIFS121JhcBqJYJd7dcCjnapZ4Hb80w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: با کمک مردم در جنگ اقتصادی هم مثل جنگ نظامی دشمن را شکست می‌دهیم
🔹
مردم همان‌گونه که در حوزۀ صرفه‌جویی پای‌کارآمدند در حوزۀ سرمایه‌گذاری برای بازسازی اقتصاد هم خواهند آمد. @Farsna</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/458048" target="_blank">📅 23:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458047">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ab451d35.mp4?token=A-pHrEByRiOcHGEf2LL_sNpKUBxwz6Hy4kK4OP5rnBSbxEGrNhxH8hf7j0GA7dImxRyF7RTQflBV2bqtpVIVnxjZq46NNm_Z4dOfM1ggdMdsd-xxY6tAJLMUb7jXMtPLppC0YUo0EDrF-80oCBsH8SHNzJfWgiLLAgiZf9_x9DzEOU6NbxKKJ89o_C9Oa-GNxbbbr-7YcjJUFcdgY9GhTuJo-qKVvs1ZTXzv0yIw9-mfJwigXM-gJ9evLToZNTPTElaM-C3qizopu7KJXdzFlk3vO76bRsT0zE5OHiPZjrNDtN9V1buZV_jnUnkyouFrbd7I5Goyc-jGwqj9gDutAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ab451d35.mp4?token=A-pHrEByRiOcHGEf2LL_sNpKUBxwz6Hy4kK4OP5rnBSbxEGrNhxH8hf7j0GA7dImxRyF7RTQflBV2bqtpVIVnxjZq46NNm_Z4dOfM1ggdMdsd-xxY6tAJLMUb7jXMtPLppC0YUo0EDrF-80oCBsH8SHNzJfWgiLLAgiZf9_x9DzEOU6NbxKKJ89o_C9Oa-GNxbbbr-7YcjJUFcdgY9GhTuJo-qKVvs1ZTXzv0yIw9-mfJwigXM-gJ9evLToZNTPTElaM-C3qizopu7KJXdzFlk3vO76bRsT0zE5OHiPZjrNDtN9V1buZV_jnUnkyouFrbd7I5Goyc-jGwqj9gDutAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: مردم صرفه‌جویی بزرگی را رقم زده‌اند
🔹
اتفاق بزرگی در حوزۀ صرفه‌جویی رخ داده که آمارهای آن به‌زودی منتشر می‌شود؛ باید در این زمینه واقعا قدردان مردم باشیم. @Farsna</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/458047" target="_blank">📅 23:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458046">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18bd0dbed.mp4?token=Sx2QjNRnit1yPXKr5791wb4XY4twQ3k0uGWEyMgRpH9q5w1P5FU3SvWCxzBCXOGOc3vFFHuH5VmPcTfxlOjm-EZQDl3q5CckFhEeYAGzBw09AUPb2wctXu7SsrqXU4P2Wcc9ceWEG7ts4D5mq1MaCbRSg6n-YeMi-p64sPNzM0m8Xehi3QaDNbWvGEZbWHNsroAykHITbKzj6-XyPxLvRGY_7nW9j1soUJ0D195XhBEgVm28GpJblwnAjdPPQo7YiiFUSvMm7h9uObL4DxaIA1C3yehR8oPJ6b4G7SDjO211CqmKRsdAYUJDoDZVnnB7jshdPYw4WlVJAfJ_-u9KuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18bd0dbed.mp4?token=Sx2QjNRnit1yPXKr5791wb4XY4twQ3k0uGWEyMgRpH9q5w1P5FU3SvWCxzBCXOGOc3vFFHuH5VmPcTfxlOjm-EZQDl3q5CckFhEeYAGzBw09AUPb2wctXu7SsrqXU4P2Wcc9ceWEG7ts4D5mq1MaCbRSg6n-YeMi-p64sPNzM0m8Xehi3QaDNbWvGEZbWHNsroAykHITbKzj6-XyPxLvRGY_7nW9j1soUJ0D195XhBEgVm28GpJblwnAjdPPQo7YiiFUSvMm7h9uObL4DxaIA1C3yehR8oPJ6b4G7SDjO211CqmKRsdAYUJDoDZVnnB7jshdPYw4WlVJAfJ_-u9KuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: مردم می‌توانند با استفاده از اوراق گواهی نفت سود ارزی از نفت آتی کسب کنند  @Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/458046" target="_blank">📅 23:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458045">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
به خاطر خدا فکری به حال معیشت و مستمری ناچیز معلولان شدید و خیلی شدید که فاقد شغل و درآمد هستند و توان کار کردن ندارند بکنید. قانون مادۀ ۲۷ معلولان مبنی بر پرداخت مستمری به میزان حداقل دستمزد، سال‌هاست که کامل و درست اجرا نشده. معلولان شدید و خیلی شدید چطور با مستمری ۲ میلیون تومانی در این گرانی و تورم زندگی کنند؟
🔸
رئیس‌جمهور پیگیر حقوق اساتید شده‌اند. ما چه جوری می‌توانیم با ایشان ارتباط بگیریم که کارمندهای قرارداد خرید خدمت اداره کل راه و شهرسازی یک ماه حقوق نگرفته‌اند و معاون توسعه هم تهدید به اخراج کرده است؟ چطور می‌شود پیگیری کرد؟
🔹
چرا هیچ‌کس درباره آنتن‌دهی اپراتورها، مخصوصاً ایرانسل چیزی نمی‌گوید؟ تازگی‌ها می‌بینی یک روز کامل آنتن ایرانسل می‌رود؛ علاوه بر اینترنت، مردم کار و زندگی دارند و منتظر تماس واجب هستند.
🔸
درختان صد و ۲۰۰ ساله در منطقه متروپل بندر انزلی (معروف به باغ زیری) به خاطر تغییر کاربری و بی‌توجهی به منابع طبیعی در حال قطع‌شدن هستند و کسی هم پیگیر آن نیست.
🔹
از صبح تا الان در خیابان کارگر هستم برای تأیید پزشکی اسناد رسمی تأمین اجتماعی. گفتند سیستم قطع است. نزدیک ۳۰۰ نفر کارشان راه نیفتاده. من خودم دارویی دارم که دیگر آزاد به من نمی‌دهند و الان تأیید هم نمی‌شود. امروز باید دارو بگیرم. می‌شود فارس پیگیری کند تا این قطعی سیستم در مراکز دولتی، مخصوصاً کارهای حساس دارو، درست شود؟
🔸
فرزند اوتیسم شدید ۱۸ ساله دارم که در منزل نگهداری می‌کنم. از بهزیستی نه حق پرستاری و نه هزینه لوازم بهداشتی هیچ‌کدام را دریافت نمی‌کنیم. الان که وزارت کار می‌خواهد تعرفه مراکز و حق پرستاری را افزایش دهند، لااقل فکری هم به حال کسانی بکنند که هیچ حق پرستاری نمی‌گیرند و چند سال در نوبت هستند و با هزینه دارو و پوشاک، بچه‌ها را در خانه نگهداری می‌کنند.
🔹
دانشگاه جندی شاپور اهواز هر ماه به بهانه‌های مختلف حقوق نیروهای شرکتی رو با تاخیر پرداخت می‌کنه تا به امروز هم حقوق نگرفتیم.
🔸
سایپا مرداد ۱۴۰۴ فراخوان اسقاط خودرو فرسوده داد و طبق تعهدی که در قرارداد نوشته شده، باید یک ماه بعد ماشین را تحویل می‌داد. الان ۸ ماه گذشته و ما را با خانواده و هزار مشکل دیگر بدون ماشین نگه داشته‌اند. هیچ‌کس هم پاسخگو نیست. خواهشاً شما که خبرنگار هستید پیگیری کنید.
🔹
خبری در خصوص عدم پرداخت حقوق پرسنل شهرداری کوت عبدالله استان خوزستان کار کنید. ما فقط حقوق اردیبهشت را دریافت کرده‌ایم. مگر نیروهای شهرداری انسان نیستند؟ با این شرایط گرانی، جنگ و گرما، پرسنل شهرداری خط مقدم خدمتگزاری هستند. همه ما انقلابی و بچه همین کشوریم؛ چه فرقی با سایر دستگاه‌ها داریم؟ ما سال‌هاست در این مشکل فرو رفته‌ایم و هیچ پاسخی دریافت نکرده‌ایم.
🔸
۲ سال قبل قرار بود سایپا معوقات ما را بدهد، اما هر بار که زنگ می‌زنیم جواب درستی نمی‌دهند. آخرین مرحله که زنگ زدم گفتند بروید شکایت کنید.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/458045" target="_blank">📅 23:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458044">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07642de9.mp4?token=UkXbTgRmjgcdnGBMtZyFqCO26xbJHzwWmVyEenbPvQ6F8dI4IRQsM0BB-hRkLAdc_uiZDjzwbiKNq9VlKYn9TRsF7Vxvxi8j26glWyIrVCJvGIb4MLfN52jj4vmAR6mr507gbL46sTburbgZ-e762wL0m0AfNHU6w4Hk3BOu6KqtisgPHOEiNqbxBz9j0Pk_AdDhT9ZRF2FNnhqhuB3jqsPMoG1rGwkNvqc2-B2ijLSTTwuEz5yDHYQypRttew_8niSM_oR-52F51FRgl7bztX2k1BcIIpzg5L9L4WxcCd0FwrxA3XEPUppsa1uRAEM23sSQC-TxFfqBkGehC4v-EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07642de9.mp4?token=UkXbTgRmjgcdnGBMtZyFqCO26xbJHzwWmVyEenbPvQ6F8dI4IRQsM0BB-hRkLAdc_uiZDjzwbiKNq9VlKYn9TRsF7Vxvxi8j26glWyIrVCJvGIb4MLfN52jj4vmAR6mr507gbL46sTburbgZ-e762wL0m0AfNHU6w4Hk3BOu6KqtisgPHOEiNqbxBz9j0Pk_AdDhT9ZRF2FNnhqhuB3jqsPMoG1rGwkNvqc2-B2ijLSTTwuEz5yDHYQypRttew_8niSM_oR-52F51FRgl7bztX2k1BcIIpzg5L9L4WxcCd0FwrxA3XEPUppsa1uRAEM23sSQC-TxFfqBkGehC4v-EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: از نیمۀ دوم سال حداقل برای بخشی از دهک‌ها افزایش مبلغ کالابرگ خواهیم داشت  @Farsna</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/458044" target="_blank">📅 23:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458043">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gaj0JsHDbiKTPnbG2iGz8WH6PntJtAzU-Cdl1KKjtrZQWUBIhJYOmRco3A6XQ7P60LFto1fSABYasTcAQnSYge6Zpa96hCP-BwS6N5idybmT76M64v_z7n2GTaZG8Ote1RaKRsKTTb3-NYAh1ighzKL530PfoKyzwUOuDdvVeGyZDdOum_hzv5bNFq4Jghum2inLQ6_UHMvJ0XO1WzqAKQSMbMqmg9tOlXwhYYL7ijreIpItGT8perrNhOhiH8JQdPVuSKuz2RHc3S-ewDthwVRmcVznAf22PmRnD4ukSE_XLE-t5ChlGNF_yaWX_Zf1QPXu7CC3ayB7NCZes5slyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش‌وپرورش: معیشت معلمان در اولویت کار ما قرار دارد
🔹
کاظمی: معیشت فقط حقوق نیست و ساماندهی نیروی انسانی و پرداخت‌های مختلف نیز بخشی از این موضوع است که اقدامات قابل‌توجهی در این زمینه انجام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/458043" target="_blank">📅 22:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458042">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRqaQmSPD9HoZ_dFz5ddaAFxLWnJ4DcsvYHEAySYz-IscXJkttGr98ZHnSYsJJKt7zQTNvwAF5g4L5a5lXGzIYH-9GS24n_f5UII1elrSSF5uXOa3Rf47wEqPr9vfKYKBaNZ2X0iO8vgxMxVGLb8grCLFxtxfodHIljmGY1p0VFCK95xBaa46pWAE7HWA4LrHljM59sAcIUgUKFMBx_J4k-u3bek-GODXAX_phy3LvuSQw8ES8e_X9L-9yPURWMGab1MVbMgACrlZ0_NihkybRBUc7Jn5H9znmAKKk7v6JuKEmmcmxBNtTjOK_xMy-TnhM_NjClhpBx-J68L_26J1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستادکل نیروهای مسلح: مدیریت دولت در طول جنگ  تکیه‌گاه رزمندگان در مقابله با دشمنان آمریکایی صهیونیستی بود
🔹
ستادکل نیروهای مسلح و قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): مدیریت دولت در این دورانِ دشوار، در پرتو رهنمودهای حکیمانه و هدایت‌های ارزشمند فرمانده معظم کل قوا حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای (مد ظله العالی)، علی‌رغم تمامی فشارها و تحریم‌های ظالمانه، تکیه‌گاه رزمندگان در مقابله با دشمنان آمریکایی صهیونیستی بود.
🔹
تدبیر و حمایت‌های همه‌جانبه دولت در مدیریت لجستیک و بسیج امکانات کشور برای پشتیبانی از نیروهای مسلح، قدرت بازدارندگی نظام را در برابر دشمنان متجاوز دوچندان کرد و این هم‌افزایی، همان رمز ماندگاری و پیروزی‌های ما در برابر بدخواهان این سرزمین بوده است.
🔹
نیروهای مسلح جمهوری اسلامی ایران، ضمن تجدید میثاق با آرمان‌های شهیدان، اعلام می‌دارد که با تکیه بر توانمندی‌های بومی و دانش نظامی روزآمد، همواره در کنار دولت خدمتگزار برای صیانت از تمامیت ارضی و اقتدار سیاسی کشور ایستاده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/458042" target="_blank">📅 22:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458041">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409d0b0c66.mp4?token=RMa56G0vbRz-2qVhInbn7gUbufEnTeAs0uR1HYO_l24stttc59I9yiXddIrW6lAKBxQFaXJnp77GwnzckvAFc1CWAvxMNbWbIMwizdG0lLwNy6__AYJlruNEgmFbChwOtQtTQjC1XUPdYcfoO7V_yqZ0mCm-V80l9jQUAudlho97orVgk65SiukthCu5IICQGkj91QZLm0r0atBfK9pKfU7a1SNExKDGUSuymKqiWEA8qbKKYUI1hIkDWUrHeLNmnbNohHJ5txcw0NdM99AkATrWx6T8zRbm3fL54axpHxy6ZR1Fyyl53cfiRXoj7cMIJHtpiC0D_kPAvLdCOR0DEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409d0b0c66.mp4?token=RMa56G0vbRz-2qVhInbn7gUbufEnTeAs0uR1HYO_l24stttc59I9yiXddIrW6lAKBxQFaXJnp77GwnzckvAFc1CWAvxMNbWbIMwizdG0lLwNy6__AYJlruNEgmFbChwOtQtTQjC1XUPdYcfoO7V_yqZ0mCm-V80l9jQUAudlho97orVgk65SiukthCu5IICQGkj91QZLm0r0atBfK9pKfU7a1SNExKDGUSuymKqiWEA8qbKKYUI1hIkDWUrHeLNmnbNohHJ5txcw0NdM99AkATrWx6T8zRbm3fL54axpHxy6ZR1Fyyl53cfiRXoj7cMIJHtpiC0D_kPAvLdCOR0DEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: نیمی از بودجۀ دولت از طریق مالیات تامین می‌شود  @Farsna</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/458041" target="_blank">📅 22:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458040">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e285c274b.mp4?token=FO7cOEYun-I5NRaahS9SdkCHFFF6lZXFiOmCCO7GXPjD2W_8IQ6LuoucSmi2vbUm995-53jxD8WX-YVBMT9wh0qchTeVAD7xM_oI-ExYMUVa7ttLtcXJ5ghBunnSo9jG7ed9H7PuYwNC81xv-PMQOXBPcpn57neSGAjHcfHaLEcSZqNJOl7DvKdOuyxn-XqPAE_Lg5_-9AkTFigp_S3-2Pz5H7IVyW07WwY2tx5V8BpRsS_YKUazxw81E3pcHIJ8uaN7pQVNSJ_4qtkYk3mxGoVCr6UQjAG0lPp1b_wZST3lorcuAzhBJHHVBZz67JFVpfuPT_7f3Gfo9tamW2HpeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e285c274b.mp4?token=FO7cOEYun-I5NRaahS9SdkCHFFF6lZXFiOmCCO7GXPjD2W_8IQ6LuoucSmi2vbUm995-53jxD8WX-YVBMT9wh0qchTeVAD7xM_oI-ExYMUVa7ttLtcXJ5ghBunnSo9jG7ed9H7PuYwNC81xv-PMQOXBPcpn57neSGAjHcfHaLEcSZqNJOl7DvKdOuyxn-XqPAE_Lg5_-9AkTFigp_S3-2Pz5H7IVyW07WwY2tx5V8BpRsS_YKUazxw81E3pcHIJ8uaN7pQVNSJ_4qtkYk3mxGoVCr6UQjAG0lPp1b_wZST3lorcuAzhBJHHVBZz67JFVpfuPT_7f3Gfo9tamW2HpeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: افزایش فعلی قیمت ارز ناشی از التهاب در فضای رسانه‌ای است
🔹
تلاش می‌کنیم وضعیت بازار ارز را به حالت عادی بازگردانیم. @Farsna</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/458040" target="_blank">📅 22:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458039">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJJW5pBh_tBhn1VB8V6IPhK86IZerhUhYmuAZ99z-_QVKJXfW07YdJDkq-p1F6EhdO2Znx7eriMFRC9VyXn9nDfQpXgh3OHWmTLIztJb8Hj99tFEItXASWFaV-Ih_zkHndlQASQi6VEJ61VHOj8NqUxvWUCxt5L4lqG8hZkk08A3WJtJqrG_Xc5izYRzpAtmx5BoNkwhq4L0OxmDSqboj_vZsrMLcKL9wPyUIWJaikUigvJjj3EZySjCsN-C8Ahu-txYegSRP9eMVvndqfJeFux8J8kWLrWhy9YujZ6iuKyID3E3gtYOGsVoZ3_qTItr3nPKQbmJ118dRByPB574Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار فرماندۀ ارتش پاکستان با رئیس‌جمهور ایران  @Farsna</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/458039" target="_blank">📅 22:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458038">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a7d7db24e.mp4?token=pFIbsXOjhA7zf03QlBtCPEwNwS3VQ8tNu0atMHfQql9jtOU6D6V7Mpzz15EMzGcCXDyBQogHx6P61CGaEhuGwvificgPErNd_ugJgi6ddaPw4ZVeFcVXSqRO0pCaQCzL7XdEMcEcimS_k1ILEsihn6oN0pYaQcSaTZh5SVrcfa0gcVzlivuBiNtqQiilWvmy3Uc1kYjd2MSQYF3Nuw2BvG7f50b8dQjHgL4Ttm21kJJQTz5ct26cHOpe4Lh5jhi62hys7cZnq9UWQCS4lYhnKlYrzQYS9P2YJb56Jx6H3B8WQLQS9PAFXhSWmzV9RRYYNTpNNXR417n25n_0MXb-rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a7d7db24e.mp4?token=pFIbsXOjhA7zf03QlBtCPEwNwS3VQ8tNu0atMHfQql9jtOU6D6V7Mpzz15EMzGcCXDyBQogHx6P61CGaEhuGwvificgPErNd_ugJgi6ddaPw4ZVeFcVXSqRO0pCaQCzL7XdEMcEcimS_k1ILEsihn6oN0pYaQcSaTZh5SVrcfa0gcVzlivuBiNtqQiilWvmy3Uc1kYjd2MSQYF3Nuw2BvG7f50b8dQjHgL4Ttm21kJJQTz5ct26cHOpe4Lh5jhi62hys7cZnq9UWQCS4lYhnKlYrzQYS9P2YJb56Jx6H3B8WQLQS9PAFXhSWmzV9RRYYNTpNNXR417n25n_0MXb-rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: در میانۀ جنگ اقتصادی خیلی از اطلاعات و تاکتیک‌ها را نمی‌شود بیان کرد  @Farsna</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/458038" target="_blank">📅 22:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458037">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEQBPrzf1ftTCP81cQ3TuPuXLBUMlmmM7gZ6PJcLDwH84sfkCCFWdI2Ra231hN5GAZdyNE3ECjOEDLLjVKB1rEj1Q04_99NKIUH9por5ldoCqL6HgrFTREJAWeg7GHEL69iu99rk50P8P_ysjK_AHcL2rVhsdRW9izxbdx-7vzoO_RVAQcuzYG-o_R-vZAua7yIBp6_vAkobMxJJP8VX1tI7Cu9GCviokEjHQxqkJ6jitRw4nIjPybnR8NHNRHdbsVwLwHgwHOZLNdSM-gmcVQ_YAZP-LpfNhPNt8y1bDpW2yirrvCKAH0kgC0i2_ugrX5fa1swwue-M9dWQoQHmJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقلال در صدر ماند
🔹
پایان هفته سوم لیگ‌برتر ایران
📊
نتایج:
فولاد ۳ - ۰ صنعت نفت
گل‌گهر ۳ - ۰ چادرملو
ذوب‌آهن ۱ - ۱ مس شهربابک
خیبر ۲ - ۳ پیکان
ملوان ۰ - ۱ فجر
تراکتور ۱ - ۰ پرسپولیس
@Sportfars</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/458037" target="_blank">📅 22:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458036">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ee66b32e.mp4?token=GtZ-zcPjD5EZSn-LjfCmGbZJ2JjGXt9s0p_DMxguPfCTvWw37h0q1uw1iomo9ku8qYIBg2RuuIieB8AKaX4hk5KJZw4pR5fr0hBsF9DnYyDHTa0jACEK52Z1dc3h5eQvYsSSWMWqhO67KTWmWQowwps-NLO5oWkJLwdl9dTBy09W3dxOK5PDM6nU5tBomp85GrvmVDxrQPu1YGKVGJE9FAt5aghU4QTc4-MNxGua1PrFpz6Xkoa_NLZu8PqydUnSgnWzqRm_h3lnA3A8tiDYsZwF5OMil-eYZWc_bwF2bFxi5JfnOLHXVLTuNuuZhRKR3NG3bR1PNYcpjvYw4KM2Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ee66b32e.mp4?token=GtZ-zcPjD5EZSn-LjfCmGbZJ2JjGXt9s0p_DMxguPfCTvWw37h0q1uw1iomo9ku8qYIBg2RuuIieB8AKaX4hk5KJZw4pR5fr0hBsF9DnYyDHTa0jACEK52Z1dc3h5eQvYsSSWMWqhO67KTWmWQowwps-NLO5oWkJLwdl9dTBy09W3dxOK5PDM6nU5tBomp85GrvmVDxrQPu1YGKVGJE9FAt5aghU4QTc4-MNxGua1PrFpz6Xkoa_NLZu8PqydUnSgnWzqRm_h3lnA3A8tiDYsZwF5OMil-eYZWc_bwF2bFxi5JfnOLHXVLTuNuuZhRKR3NG3bR1PNYcpjvYw4KM2Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ وزیر اقتصاد به اسکات بسنت: این‌بار هم شکست می‌خوری
🔹
ما مدت‌ها منتظر این روزها بودیم و می‌دانستیم که آن‌ها چنین برنامه‌هایی دارند.
🔹
دولت کاملاً برای این جنگ اقتصادی آماده است. @Farsna</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/458036" target="_blank">📅 22:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458035">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52051e8e8b.mp4?token=ma1ynH2vJvaMw76b5-PCR88_zQWnI2fRa_7N7gPRyi3Qj6yCj7mZ1AUv4j29aOcnyVo5JW03OlafyAnSEG9hVwi8qCblAOzJ6HaG2uOLMr1V79MPM-1VAEo68LgAa_rAv58Aw9fGCG4qjIiWKROsvy78bTuY9o6hFm2EGN4bman0nJkQTuVSFnYabT_wT0Vry4hzSu8ym5croy5o-W6hUf10_L_9JQUVM0laLj5qu0_weas0HDuX5fbZjkEa022QOhkvUgkltSZZtDIeV6fDTfYIgLYLmfTTiJdfdMvReqxy2HExJBZgS5H5CPKx81N3qOUxauKrJZIDgFiiRjn7Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52051e8e8b.mp4?token=ma1ynH2vJvaMw76b5-PCR88_zQWnI2fRa_7N7gPRyi3Qj6yCj7mZ1AUv4j29aOcnyVo5JW03OlafyAnSEG9hVwi8qCblAOzJ6HaG2uOLMr1V79MPM-1VAEo68LgAa_rAv58Aw9fGCG4qjIiWKROsvy78bTuY9o6hFm2EGN4bman0nJkQTuVSFnYabT_wT0Vry4hzSu8ym5croy5o-W6hUf10_L_9JQUVM0laLj5qu0_weas0HDuX5fbZjkEa022QOhkvUgkltSZZtDIeV6fDTfYIgLYLmfTTiJdfdMvReqxy2HExJBZgS5H5CPKx81N3qOUxauKrJZIDgFiiRjn7Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبیر شورای‌عالی امنیت ملی: به آمریکا بی‌اعتمادیم و باید رفتارش را تغییر دهد
🔹
سرلشکر رضایی: در دیدار با فرمانده ارتش پاکستان: آمریکا باید رفتارش را تغییر دهد و اقدامات عملی درخصوص اجرای شروط تفاهم‌نامه انجام دهد. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/458035" target="_blank">📅 22:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458034">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e5f443076.mp4?token=EqSIAGqLiklksHx9tJli-ILtV22xrM9waKcqI3BDKRRGfRx2WI9cWtW4in-24Na3KaEAuMFpcB2x9gIUV3wHjcbcXhSW29Uskv8T2GUjtkdTXnCSgvhMw0awLuZENgV0Ng_fZk6jVKFXpGdoy3n_q0085oGafIQeu4ycrzzR6iURb-jHj4t0RjRi6VJn2eGfKqKZJTOfNRSxXhk9iyBj5JERD6HLBVIi-m-7VEUof1_ynZhYTVu00eWOceuCICmTQG4DxAm0sh3LiADPQsnX7WflSbXKsMrAR91L59a2R9eRzXTclFNsFh_qqnaaktjBZspjf63_dSv7gyKcVUBF8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e5f443076.mp4?token=EqSIAGqLiklksHx9tJli-ILtV22xrM9waKcqI3BDKRRGfRx2WI9cWtW4in-24Na3KaEAuMFpcB2x9gIUV3wHjcbcXhSW29Uskv8T2GUjtkdTXnCSgvhMw0awLuZENgV0Ng_fZk6jVKFXpGdoy3n_q0085oGafIQeu4ycrzzR6iURb-jHj4t0RjRi6VJn2eGfKqKZJTOfNRSxXhk9iyBj5JERD6HLBVIi-m-7VEUof1_ynZhYTVu00eWOceuCICmTQG4DxAm0sh3LiADPQsnX7WflSbXKsMrAR91L59a2R9eRzXTclFNsFh_qqnaaktjBZspjf63_dSv7gyKcVUBF8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: پس از جنگ از بیکاری ۶۰۰ هزار نفر جلوگیری کردیم  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/458034" target="_blank">📅 22:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458033">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a6cab2e09.mp4?token=FanmKuNcI-nFPWaCNKYjfXKVOk-SvQdIWcrh5WnFPuSiv2i-6Fj32A-I2Goewf4ECdYr5F2nY65oI92fi__L4T2atPVVeMWCMYUjw9yRdOheQmQ7up5wnNgeaNSWN7GmQ6IaMfw-wJPmda9zYeK7unbhmZqLuz_51zwC_rNrml1WMJ5Z-QrfaTnB06Fh2ZJdr7_3h3ap3MJL0oZOH8JIVzBC06Bk0dvM7GdtJm2SE7bzAk2R6qj6bXmxaF_7gp3Wk5QFDi_d2r0K-v82w0ltiTDMSSyh5Y_SkNnj_MikrkPY5-TZs9GiBr8zlZ4n5CH5ogMD-atP5GFaR1Ewa8BFXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a6cab2e09.mp4?token=FanmKuNcI-nFPWaCNKYjfXKVOk-SvQdIWcrh5WnFPuSiv2i-6Fj32A-I2Goewf4ECdYr5F2nY65oI92fi__L4T2atPVVeMWCMYUjw9yRdOheQmQ7up5wnNgeaNSWN7GmQ6IaMfw-wJPmda9zYeK7unbhmZqLuz_51zwC_rNrml1WMJ5Z-QrfaTnB06Fh2ZJdr7_3h3ap3MJL0oZOH8JIVzBC06Bk0dvM7GdtJm2SE7bzAk2R6qj6bXmxaF_7gp3Wk5QFDi_d2r0K-v82w0ltiTDMSSyh5Y_SkNnj_MikrkPY5-TZs9GiBr8zlZ4n5CH5ogMD-atP5GFaR1Ewa8BFXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: پس از جنگ از بیکاری ۶۰۰ هزار نفر جلوگیری کردیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/458033" target="_blank">📅 22:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458032">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cfbc72996.mp4?token=J89NMhkE37tIddhTz-F2PzLxA7TDtlLLDWHAw39pq2r7sFAgXyFzYLLl63NR0h9jJIwgtqFULunj-GFF_lwg1gxf-w-E6z7RQ9JH_DcpA2demb2uU-6yDLBtBpQx94hJwNst2zvHAf4afwvXxK-9zBZkmJHxu5DfngVSr_04I_5POqj6HgA18SMnL1yF4jQCx5m2FsqTPAyGAeWnBKNm65e5OQIzoqMFJ0pN4KpLGZI8XXPPjKgg2-HljIk1QD9-vqAil2gueYZ3VoZroOi4E_A2dcK9e6OOdITA7qcl4iLH70N0SZ0hZmYwknIXy69uYzuOrkCkuPDWWHWlmd2WMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cfbc72996.mp4?token=J89NMhkE37tIddhTz-F2PzLxA7TDtlLLDWHAw39pq2r7sFAgXyFzYLLl63NR0h9jJIwgtqFULunj-GFF_lwg1gxf-w-E6z7RQ9JH_DcpA2demb2uU-6yDLBtBpQx94hJwNst2zvHAf4afwvXxK-9zBZkmJHxu5DfngVSr_04I_5POqj6HgA18SMnL1yF4jQCx5m2FsqTPAyGAeWnBKNm65e5OQIzoqMFJ0pN4KpLGZI8XXPPjKgg2-HljIk1QD9-vqAil2gueYZ3VoZroOi4E_A2dcK9e6OOdITA7qcl4iLH70N0SZ0hZmYwknIXy69uYzuOrkCkuPDWWHWlmd2WMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دختری از تولد شیرین تا شهادت در کنار پدر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/458032" target="_blank">📅 22:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458031">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac5db7e37.mp4?token=qq3ZuwN2qE8OX-AGPFRWwWCwgqlbRDfoQG5dIrvztJoYV2cFhnWgjQYsiIDAEKhTTyIiq_eig5nzKXwnF6Y61GC4JMdpYzOEyEADI4ktWkaKXByuq5ca-Zk4wM6RcOxa1Mkk3hJWGaXsiWaSpppKds7-g0MAgHS6VyBkkbmbfF1Gt1x_i0sXQaCYOqyAJsKu7TFbXjJ5uJP2mmqidEDE87Qgu4A66DxL_ArcuMawNcPm0iQ3FcM1S_DTr-xmd5wD9Hvltku4rZ0HkAQpkhFd7Q7VBSvEgzaOTIY2V2r7dhOH-KpfkyP7AojCJnct4knN4dC92r_nwKL7g6DNQBDML2_M-oYFIk1fG2dPjeBlV3u1WH9gBSvM6xlxwcDTb0-_nfuZnvv1TjlpD4DfZayCSSm4h8wi2SF_1DGuamXpTKIJ4h5VoK5Gd28n_Sni6M8dvqG1DQrWVoQyh8kgQUaNTMzZFV0v9RisaSmj6CZ9wwvvYJt_U3Ef-lctvfc9aI6eSCicDqJPSueeGyBHRO9RyH5BokBvb16C_sqIuFr3s1mVLlhW-xCS9Qz04dFDUIUNVwtHLj25Tpa1yevKxudVENfI9a4E411bH2Y7d3TmGPPo_OU1njhemOLyeKk0T0xCjVYV5MpMHDCLolIpcZburuuXroUDsMP95On8LCJ8Bb8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac5db7e37.mp4?token=qq3ZuwN2qE8OX-AGPFRWwWCwgqlbRDfoQG5dIrvztJoYV2cFhnWgjQYsiIDAEKhTTyIiq_eig5nzKXwnF6Y61GC4JMdpYzOEyEADI4ktWkaKXByuq5ca-Zk4wM6RcOxa1Mkk3hJWGaXsiWaSpppKds7-g0MAgHS6VyBkkbmbfF1Gt1x_i0sXQaCYOqyAJsKu7TFbXjJ5uJP2mmqidEDE87Qgu4A66DxL_ArcuMawNcPm0iQ3FcM1S_DTr-xmd5wD9Hvltku4rZ0HkAQpkhFd7Q7VBSvEgzaOTIY2V2r7dhOH-KpfkyP7AojCJnct4knN4dC92r_nwKL7g6DNQBDML2_M-oYFIk1fG2dPjeBlV3u1WH9gBSvM6xlxwcDTb0-_nfuZnvv1TjlpD4DfZayCSSm4h8wi2SF_1DGuamXpTKIJ4h5VoK5Gd28n_Sni6M8dvqG1DQrWVoQyh8kgQUaNTMzZFV0v9RisaSmj6CZ9wwvvYJt_U3Ef-lctvfc9aI6eSCicDqJPSueeGyBHRO9RyH5BokBvb16C_sqIuFr3s1mVLlhW-xCS9Qz04dFDUIUNVwtHLj25Tpa1yevKxudVENfI9a4E411bH2Y7d3TmGPPo_OU1njhemOLyeKk0T0xCjVYV5MpMHDCLolIpcZburuuXroUDsMP95On8LCJ8Bb8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر دیدنی جشن میلاد پیامبر(ص) در الحدیده یمن
🔸
فردا آغاز هفتۀ وحدت و روز میلاد پیامبر(ص) به روایت اهل‌سنت ‌است.
@Farsna</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/458031" target="_blank">📅 22:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458030">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66c7a7ecd2.mp4?token=lT1aLFAkiIEZqXmkbcDFODU9HVTSyp6BsXY4Q54jtz8kQQSNSQx261K-7KP3kC2aQUxTH_AW6dhoS6KGZsjGQhVDk7Ebegii3HKQ333E8BHQiqI-vc3Ws1VtusZN2GKFx5W5TboDZuPILHr-VYjZOB8ujZR_2ooRx4GpUIpZUOz0FlVXAVpNriheCFxAfqVN7_BCRGHlIpgLfPnFh7wTQaFcA4ZfgvEXe-k8NrkbK77COcA1o6ys1-rDAuHZUxdztIg3aOfIgHG92zITuHh4oddvE4iFm83Qq8_Io17R_73vsuXhScz57PCTFSwE9oIlG0vTriiWzFB5lX3cfuCWVBlIOfdpDQylOU4Vx3RSXrXAS9s5lZQBoSaZ_OvH4Q6GqE0XJYStEEGR2vu9DfKS9WC9swJNeijRZtN6GqQ2U4HL8yKGJKAf8o_G4cMfvqSK8otuxwFJSgeoGhd3bdJ31fazhsqhoB8X-Jk_BHHIqa0E8oHgoyM1P-5_rCbB6A7JtK9Kn7QXcxYCF6lplmc1ZI_FLM53cSKqINZ2fEeD_-AxX1i7GTUyueq-C2zRCrJyKKpojRTxflg10Bu5Ac0d2RVdiL6Coi8VYtRcA51kVnfvIgWsG9T2s0YdPB9AhixwHLKsxDPJWpq-xEcjQdahCZTb9FhnlDjiH-f_si2MUv4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66c7a7ecd2.mp4?token=lT1aLFAkiIEZqXmkbcDFODU9HVTSyp6BsXY4Q54jtz8kQQSNSQx261K-7KP3kC2aQUxTH_AW6dhoS6KGZsjGQhVDk7Ebegii3HKQ333E8BHQiqI-vc3Ws1VtusZN2GKFx5W5TboDZuPILHr-VYjZOB8ujZR_2ooRx4GpUIpZUOz0FlVXAVpNriheCFxAfqVN7_BCRGHlIpgLfPnFh7wTQaFcA4ZfgvEXe-k8NrkbK77COcA1o6ys1-rDAuHZUxdztIg3aOfIgHG92zITuHh4oddvE4iFm83Qq8_Io17R_73vsuXhScz57PCTFSwE9oIlG0vTriiWzFB5lX3cfuCWVBlIOfdpDQylOU4Vx3RSXrXAS9s5lZQBoSaZ_OvH4Q6GqE0XJYStEEGR2vu9DfKS9WC9swJNeijRZtN6GqQ2U4HL8yKGJKAf8o_G4cMfvqSK8otuxwFJSgeoGhd3bdJ31fazhsqhoB8X-Jk_BHHIqa0E8oHgoyM1P-5_rCbB6A7JtK9Kn7QXcxYCF6lplmc1ZI_FLM53cSKqINZ2fEeD_-AxX1i7GTUyueq-C2zRCrJyKKpojRTxflg10Bu5Ac0d2RVdiL6Coi8VYtRcA51kVnfvIgWsG9T2s0YdPB9AhixwHLKsxDPJWpq-xEcjQdahCZTb9FhnlDjiH-f_si2MUv4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌پیروزی لحظه‌آخری تراکتور مقابل پرسپولیس
⚽️
تراکتور ۱ - ۰ پرسپولیس @Farsna</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/458030" target="_blank">📅 22:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458026">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RC0PlvI_4BzUg5g9p4ELd5n0qO_pV1f4HK3M2IHH0Et1IdSPijk7Ijgb4JS1xn9y4ICBTFrcjfb6014cGBkGaGl6esYXbsn1_r1cZm6hYsplPER3VuPCelNaYQe5goK7bGUJ7DgBKnkMGCVOTu13Lej0oY6eEVF1UJXz5Ez-4jQlmr6I9h4qxLsLYllGV7EbwEVEIaP-jJbozYOl8TCwiA1HG3qY2AUbOplZfq7k7Lo7KTNYOmJTvvSBghyxYCrWdsEUXrNWkpvnr9nZgXPIEBeiQTkeN3A7mTQ07fXgnFjbgXq5W2kMRiutIRRxfj1pRVtVDBZskH9vKkxh6usC0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HdZIjkfTA9FCLOKtUnNcftp03B1nucf3lsZcIhapLlIv3IpuuAZj4FuVDTGwgc7tGPLkSoeX1h_DIH97jOEH21FlD6_m_lP9GfMuldKyb8PXuB5lFfUCt--Lw5TJwDKi7vtwvU0YHrYaLbJhuSFmkNW9Roe3RjU_IXu-P5Ap4pkPdAGN0PpMoYm_WOwxlVBjBNOySgzpWpsGvS6bMZOdG5pn2QElyMeVVM53heF8zMFM4D5IA32Q4XHp2kvmoSqW6Njb5txvZH1Np8IqomQz2DwOBa2L4zAmrPX87ehJ812FsCdTYFNGm4ls8_OoQT5PG-k8voiYgBEKZTqqt387QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vxLUMCr-MbD7cWyoQsI6QzRg2iNgt55P9fXqH8jOA5t5BhfJisX2dcbxCqflCsi1eZ9roE9w_vTc05FvwwWgUB-mvOLiBwTMhyD8Y6x7X1LewHSfrCYfrYWwAMIkL4T6kYLQgas5SORGb2WKNiHLAaZkj1VO5vRzwjWn2pU2Qjs3TCWJFJdbQfKoIf8de5ZBiS6kpu4ETVY8_YTC69BXC8C0j-ikn0RAGNRJ7i2Lmx65dMy3HkvTbSOqlRKH3TE1DVDuzpISf35ysj7wVcngNPnu6tSPzdxOPQIsRSVBeTMjnGBHert7rzNkUc94uw3SJhTgrTutoxWuXVLXGhYSyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iNE0uA8UsjJOjZ0XsltMWYWXAj8zTCDe9T_52wwoxgNZk8KSDLGdZ4y_sJW6ap6PzDfF_jUoulNcVbq5mTKjeIKKxFCtFENy5xcuxBE1J2eud7KUcwSjpzjiDEMBYvcOVtWyTy4beB7dSlwxiSU4-pA9kQnei8l4L3EjlWgrA5Y553eMTbubF77876xX247cQJ4Tlo-Oz2aydlaun75hTQNupbskBK7nd951znq3tm2rNNy2QFKyyC1JaSHzv_ZstiVa4LoOvUe-3o21-zjzgtz1F7MQZfa-JzZhe3zigcqNu9xDUSZpkGDVxHk78nxut4GvMsHrunEBdg_bCFBHZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دبیر شورای‌عالی امنیت ملی: به آمریکا بی‌اعتمادیم و باید رفتارش را تغییر دهد
🔹
سرلشکر رضایی: در دیدار با فرمانده ارتش پاکستان: آمریکا باید رفتارش را تغییر دهد و اقدامات عملی درخصوص اجرای شروط تفاهم‌نامه انجام دهد. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/458026" target="_blank">📅 21:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458025">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b47f59a878.mp4?token=nWTE_8M2qMXQ2bi_aAHRrgD_PQ0AavNV8YlwBRm8MMyoLRh-eqqjqg1v3iuXOELoDhjAztBZEwdqn4_VnKN3PGjyxY3CmprMFe679kt1y7LZNrOLGAh6DwtJI_1mO7lPuc5bsw59XXLXG90KL_wWLBc8Hi17AuTB8fjw0TuC0WJvcIiKgSxVY9xkyTdHvGkSCQ7gKOuL6dfK5M-KdlN0Qlz5KAxDvBHq7bb2rTVnlRkj7pcBTgAtIFPMOh7uBeL2f9lgQGjYFUAFNG0Z_6a4yH4KOF4bcu9HMpS6xP3hWG7BwUZXRQa4bBeuld30YVXR8giwbnY9HswC8OYiYUycRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b47f59a878.mp4?token=nWTE_8M2qMXQ2bi_aAHRrgD_PQ0AavNV8YlwBRm8MMyoLRh-eqqjqg1v3iuXOELoDhjAztBZEwdqn4_VnKN3PGjyxY3CmprMFe679kt1y7LZNrOLGAh6DwtJI_1mO7lPuc5bsw59XXLXG90KL_wWLBc8Hi17AuTB8fjw0TuC0WJvcIiKgSxVY9xkyTdHvGkSCQ7gKOuL6dfK5M-KdlN0Qlz5KAxDvBHq7bb2rTVnlRkj7pcBTgAtIFPMOh7uBeL2f9lgQGjYFUAFNG0Z_6a4yH4KOF4bcu9HMpS6xP3hWG7BwUZXRQa4bBeuld30YVXR8giwbnY9HswC8OYiYUycRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی سازمان تعزیرات: با هرگونه امتناع از عرضه کالا در فروشگاه‌های اینترنتی، برخورد حداکثری می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/458025" target="_blank">📅 21:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458024">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اداره‌های کردستان فردا زودتر تعطیل می‌شود
🔹
ادارات و دستگاه‌های اجرایی کردستان فردا سه‌شنبه، ۳ شهریور، از ساعت ۱۱ صبح تعطیل می‌شود.
🔹
این تصمیم به مناسبت ۱۲ ربیع‌الاول، میلاد پیامبر اکرم(ص) به روایت اهل‌سنت و آغاز هفته وحدت گرفته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/458024" target="_blank">📅 21:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458022">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTJTS11bGKV0xizMoteGzc3Sul3wtwzwS--rf_P5ypi_Tw8IF-FOFZLKMPkz8b8B2pVEqs62j0H8oV_I57Npn0uzoMyb4Bix1XaifnaGxgIgNuWPEbLtBE2gGzKVAV_BjoX6VcCu0VftI9vygoCsyhxSx36s94jBpYOAUO0FEnmFQkF56-RUZuOv7-BXg47iOqnVOCK_BR4OiaqhON0_TpViwvQBOxV5TUX_AXn2VMmmYpOR-OwIO9z7jmydJtpJc2eQ8LIY97qYKLGcB4gR2m38em_K-PMJzsNKdkqmDLBO-TEfMRKwJp-653WbPbzfxoDv7vmd8LWDPexWAG8VaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح تحریمی جدید ترامپ؛ تکرار فشار حداکثری با پیوست تبلیغاتی
🔹
اسکات بسنت، وزیر خزانه‌داری آمریکا امروز جزئیات طرح ادعایی جدید ایالات متحده برای تحریم‌ها علیه ایران را اعلام کرد.
🔹
اظهارات اسکات بسنت نشان می‌دهد که طرحی که ایالات متحده قصد رونمایی از آن را دارد مشابه همان فشار حداکثری است که در دولت نخست ترامپ اعلام شده بود.
🔹
اسکات بسنت گفت هر کشور یک جدول زمانی مشخص برای متوقف کردن فعالیت‌های خود دارد و اگر کشورها اقدامات لازم را انجام ندهند، ما از طریق اختیارات خود به‌صورت یک‌جانبه دست به اقدام خواهیم زد.
🔹
وی همچنین گفت: وزارت خزانه‌داری ایالات متحده: ما به کشورهایی که قاچاق نفت از ایران را تسهیل می‌کنند و اجازه استفاده از بانک‌های خود را برای منافع رژیم ایران می‌دهند، هشدار داده‌ایم.
🔹
وی تصریح کرد: کشورها برای بستن فعالیت‌هایی که توسط وزارت خزانه‌داری شناسایی شده‌اند، از جمله بستن شعب بانک‌های ایرانی در خارج از کشور، مهلت زمانی خواهند داشت.
🔹
بسنت گفت: هر نهادی که فعالیت‌های پولشویی را به نفع ایران تسهیل کند، بر اساس سیستم مالی مبتنی بر دلار آمریکا از این سیستم کنار گذاشته خواهد شد.
🔹
او همچنین خاطرنشان کرد هیچ‌کس در برابر تحریم‌های ایالات متحده مصون نیست.
🔸
دولت ترامپ بعد از خروج از برجام نیز اعلام کرد که قصد دارد تحریم‌های جدیدی علیه ایران به کار بگیرد. اساس آن تحریم‌ها نیز تحریم ثانویه کشورها و شرکت‌هایی بود که اقدام به معامله با ایران کنند.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/458022" target="_blank">📅 21:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458021">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/754b64eb06.mp4?token=mcEsjOhfwH8OVxnVWCQU5r28kJF2LJOBXF3GZ5_a6heJEBZCSBhGdTwxPPyYlAsm11C9aNj-A76MiimvHFlsu5Z33CUnIv-WNW-w4P1Y1wUZ7211uzltqNawmdf2V9TGBPcc4hYr6CQX4-nAKCf-uiOEisem8HqDcIIepinf4vPoa_pYjvumrXVirkac25BZevQmUACCKNH91DzwajUHDmVoNdepy8njHqOkLSoufH04uwIjwkc7kyj4l9l9D7GnGPxwwaXQTA9qZbTUq2qKxyviPp9VwCmuA2GTDaj333NuUi_57jRSv7ou8AecIJLz86GmjJ31d0_NNbhMocv1gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/754b64eb06.mp4?token=mcEsjOhfwH8OVxnVWCQU5r28kJF2LJOBXF3GZ5_a6heJEBZCSBhGdTwxPPyYlAsm11C9aNj-A76MiimvHFlsu5Z33CUnIv-WNW-w4P1Y1wUZ7211uzltqNawmdf2V9TGBPcc4hYr6CQX4-nAKCf-uiOEisem8HqDcIIepinf4vPoa_pYjvumrXVirkac25BZevQmUACCKNH91DzwajUHDmVoNdepy8njHqOkLSoufH04uwIjwkc7kyj4l9l9D7GnGPxwwaXQTA9qZbTUq2qKxyviPp9VwCmuA2GTDaj333NuUi_57jRSv7ou8AecIJLz86GmjJ31d0_NNbhMocv1gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده جنگ آمریکا شکست خورد؛ نوبت وزیر خزانه‌داری رسید
@Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/458021" target="_blank">📅 21:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458020">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c117fcb8c4.mp4?token=udjS7ENhG9SMpVOQH9L7EAikdYu0KIEneRccAhxb0TxVLFrfO37DyctYIYm8vetZLQ8RAGvD01YkzwRwCMtLQl4hIsuzlWHI1CvaYu_wBiIQpUWVk3h1b1kKkiojPAzOaZevoSXdyDaUmzGrkfjnhFLJ4CzK5vuWha86jElBis-5nOxTRdWPYejc4ShDI2Swf_Ckda0xJYLZHnIJjC78KJ0xn9linx3KxzDDm94NOaK-TaM6Nb6eO94QYOB3xho8c1Nu-PGkzYOsHuvUG-lmQA_t-ETAudVpXdwsGIiLnV9_xAMWjS2fT4Q965FLPFXC1VHaS9b-M_wvTj_peUNu4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c117fcb8c4.mp4?token=udjS7ENhG9SMpVOQH9L7EAikdYu0KIEneRccAhxb0TxVLFrfO37DyctYIYm8vetZLQ8RAGvD01YkzwRwCMtLQl4hIsuzlWHI1CvaYu_wBiIQpUWVk3h1b1kKkiojPAzOaZevoSXdyDaUmzGrkfjnhFLJ4CzK5vuWha86jElBis-5nOxTRdWPYejc4ShDI2Swf_Ckda0xJYLZHnIJjC78KJ0xn9linx3KxzDDm94NOaK-TaM6Nb6eO94QYOB3xho8c1Nu-PGkzYOsHuvUG-lmQA_t-ETAudVpXdwsGIiLnV9_xAMWjS2fT4Q965FLPFXC1VHaS9b-M_wvTj_peUNu4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استانداران و فرمانداران سکان مدیریت را به دست گرفتند
🔸
رویکردی که با عبور از پیچ‌وخم‌های اداری فاصلهٔ تصمیم‌گیری تا اجرا را به حداقل رسانده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/458020" target="_blank">📅 21:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458019">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6cb723a7e.mp4?token=QYnj_EMMTM2SAhMr22sIQ3KWQ4rxKjNAVCwa0gaiOkXQcZolYv-bcQlrLb4e-IXepEIC3s1a2y728lwYlF-N3jf4M7uF8JIP0Z187dWZi-P94uKs-5bvbPKdBfadC0p1fA9A_dm45E_JzkOyXzJ_dIax7JH_VRZErNn-sQGChghNYLVnQdXlLg1XrHjP82zuSIg7dZgjb3vTu9-1Ft4KIVfftm9nOK38T-1HLfa_GEBwpHifrJt1GOseJvKnrBUex54LRGj7yS690wBcUfjKkOaPU98aCbOBbbpDvrOXXyK1s6hS9SQXLhEWxeF22PcmY4-NayOQiZUw96pdu9aKoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6cb723a7e.mp4?token=QYnj_EMMTM2SAhMr22sIQ3KWQ4rxKjNAVCwa0gaiOkXQcZolYv-bcQlrLb4e-IXepEIC3s1a2y728lwYlF-N3jf4M7uF8JIP0Z187dWZi-P94uKs-5bvbPKdBfadC0p1fA9A_dm45E_JzkOyXzJ_dIax7JH_VRZErNn-sQGChghNYLVnQdXlLg1XrHjP82zuSIg7dZgjb3vTu9-1Ft4KIVfftm9nOK38T-1HLfa_GEBwpHifrJt1GOseJvKnrBUex54LRGj7yS690wBcUfjKkOaPU98aCbOBbbpDvrOXXyK1s6hS9SQXLhEWxeF22PcmY4-NayOQiZUw96pdu9aKoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس اتحادیهٔ طلاوجواهر: قیمت‌ها ممکن است هر لحظه افزایش یا کاهش یابد؛ مردم معاملات خود را به زمان ثبات قیمت‌ها موکول کنند تا متضرر نشوند
@Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/458019" target="_blank">📅 21:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458018">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYJqMYnDakxOyLuWzybXUaBvkK-kui6FFaF4Xlwuz3vGJyHNJfKB999PyR8A5ORh9pdW1TmuvAypvIYK8rfhTFdn7NHlDBxM0Y3XfdBdHlWY-xsM76TRANCZEcRKE05CwUgM63517NKMMb4KbmCWNpnQVwxF2YgjlAQ_VYljbe4rlcplnURiDPMhjWvXE5jnDfZlZPPy4LzpbiladJ-7piRgNL62WygPbBdU_F6at_Tg022x8tUanSvqf7dc3K75H76CjmRzXQKLWu8khSnaAkJy2N2jL8GG3Gfmbr8ki8x82qdZuPZTyx1i-nDH-zOnpDhbcfp4zRnMCrvPu7SXeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
«راه تاز» برنامه‌ای متفاوت در شبکه سه با روایت دستاوردهای جمهوری اسلامی
🔹
فرهاد جم، سیروس میمنت، علی مسعودی، شهرام قائدی، پژمان بازغی، شهرزاد کمال‌زاده و آرام جعفری در این مسابقه با حضور در پروژه‌های بزرگ کشور، از نزدیک با بخشی از دستاوردها و پیشرفت‌های جدید ایران آشنا می‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/458018" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458017">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarmaye Bank | بانک سرمایه</strong></div>
<div class="tg-text">⭕️
💰
📣
✨
نسیم سرمایه
۳۰۰ میلیون تومان وام قرض‌الحسنه
با کارمزد ۴ درصد
‼️
📅
حداقل مدت میانگین حساب یک ماه و بازپرداخت ۳ تا ۶۰ ماه
🤩
🧮
لینک محاسبه مبلغ وام و اقساط
📱
لینک افتتاح حساب از طریق اپلیکیشن سرمایه
🔷
اطلاعات بیشتر
‼️
وفق ضوابط چنانچه حائز شرایط ­باشید
تا یک میلیارد ریال بدون ضامن،
تسهیلات دریافت نمایید.
#تسهیلات
#تسهیلات_بانکی
📞
با ما در ارتباط باشید: ۴۳۷۳-۰۲۱
#بانک_خوب_سرمایه_است
🔽
بانک سرمایه را در شبکه های اجتماعی دنبال کنید:
📲
اینستاگرام
📱
تلگرام
👨‍💻
وبسایت
📲
بله
📲
ایتا
📲
روبیکا
💖
آپارات
📲
سروش</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/458017" target="_blank">📅 21:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458016">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/458016" target="_blank">📅 21:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458015">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/315f30fd87.mp4?token=RvtH__5weUwnvLsV9ysNKX8FVTx8_j_j9RJRjPwWl4_rR0zKN5qZ0tlL0aCJP21Vf-fHGDl_2k8LX_qDi9wWkpHhf2IozZDrtQgsovpPv95MERM0BRyMvry8c8XC3DzzWbdDZLv4j7auzyspdY7jwZa91iusIGU6YghBaFzUd6dZ-M6VDrpT8xbQx7cbe6BMERTeuw5bibZrHw4BR1BayGPOFKwYAbsLBhjaZiLDJmpgzdm09WtDydPvkLA07Xr-_gAH1ZFkxB0DU_dxLyWF1ZDVhFlJZ29MvztEUgQxUFESGfwr5hoypkzmA5gulsOkNIE9TxwzMt6Z9hsh5dCpoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315f30fd87.mp4?token=RvtH__5weUwnvLsV9ysNKX8FVTx8_j_j9RJRjPwWl4_rR0zKN5qZ0tlL0aCJP21Vf-fHGDl_2k8LX_qDi9wWkpHhf2IozZDrtQgsovpPv95MERM0BRyMvry8c8XC3DzzWbdDZLv4j7auzyspdY7jwZa91iusIGU6YghBaFzUd6dZ-M6VDrpT8xbQx7cbe6BMERTeuw5bibZrHw4BR1BayGPOFKwYAbsLBhjaZiLDJmpgzdm09WtDydPvkLA07Xr-_gAH1ZFkxB0DU_dxLyWF1ZDVhFlJZ29MvztEUgQxUFESGfwr5hoypkzmA5gulsOkNIE9TxwzMt6Z9hsh5dCpoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات محکومیت دولت آمریکا به پرداخت غرامت با شکایت بیماران پروانه‌ای
@Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/458015" target="_blank">📅 21:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458010">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcMumUn4Yf36gWRYlexo9qRI2RzVUEfAJ28NMe1W-8MJ5zSx4KH6chCguiS6a5dej10rBQEFnsF7yClS_UHeFy56n-MhjEsebB96OiECarMIhOLyxQBpFQ5uKkO5oP2McVr5pZTzibJrvAtvw4sm-oVWCviFmRXBBJe7ighWBfebkcjLqi4euQ3aSiws8hjvizb8CSdYfGEft5eJzELidTdh6h6jj7w-jVQ3r0gObNs7nX7HdTTGQ51_nG2_T2jE77vQtLYmo3vFsdVvNjoam3Q85-J3TPnpBZej3rvB2dr9JoIIHpVj3ifKgb9l2gT-kF0HVzxvghoYu-CcLj0Hlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: کسی گُنده‌لافی‌های آمریکایی‌ها را باور نمی‌کند
🔹
شرکای تجاری ایران‌ به ما اعلام کرده‌اند که اظهارات آمریکا را به هیچ جا حساب نمی‌کنند. @Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/458010" target="_blank">📅 20:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458009">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTXvWQ_-kuWE6IzvMP8CRchSyrO7vXa5M9SknWHuqJoVMpnPLYqLhuLkVq50-IZz-3FK24gIxGIzcDRoHxklTJk_Isn8sq57mQiYmC7n7eN3v4CfhVRzmNUhwWhzRmoXZfiWuBUNLzlEUHXA7vLebd4RCj8Qwl1OKEF3KYKYPH9dHyOnyUxeZULzv_-DidL-v8gb_I5yvehXigckVApOD9UWmTB2W3A0DkOYeVSClOFWq4XtsdxwTW0oBWiw6rk2meNNbX1tq3F5jcjon_pRLL39FhjesTVASrtqRsA14YDE8JsPL9Te62loYYsFytOKkjuf1qJGIRDjBTdP7NFVNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهش ارز، دوباره بیماران کاشت حلزون را در انتظار قطعه گذاشت
🔹
اگرچه عمل کاشت حلزون شنوایی در ۱۶ مرکز دولتی کشور به‌صورت رایگان انجام می‌شود، اما کمبود قطعات یدکی و مشکلات تخصیص ارز، روند درمان و زندگی بیماران را با مشکل مواجه کرده است. از کار افتادن حتی یک قطعه می‌تواند به معنای
قطع شنوایی فرد و بازگشت او به دنیای سکوت
باشد؛ موضوعی که برای کودکانی که به مدرسه و زندگی عادی بازگشته‌اند، تبعات جدی دارد.
🔹
در پی ثبت پویش خانواده‌های بیماران در «
فارس من
»، پیگیری از مسئولان نشان می‌دهد تغییر سیاست‌های ارزی باعث تأخیر در ترخیص قطعات شده و برخی قطعات یدکی نیز
۱۰۰ تا ۲۰۰ میلیون تومان
قیمت دارند و هنوز تحت پوشش بیمه قرار نگرفته‌اند.
🔹
مسئولان تأکید کرده‌اند باید قطعاتی که واقعاً با کمبود مواجه‌اند شناسایی و برای تأمین فوری آن‌ها اقدام شود. جزئیات کامل این پیگیری و پاسخ مسئولان را
اینجا
بخوانید.
@Farsnews_My</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/458009" target="_blank">📅 20:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458008">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7db85dfe90.mp4?token=EDDLhzy_P_v8twGb4R9zrVBftj0nipcdTrtJMOkrSnyh6f6ihH0JufcZg6uX01eIfY2II4y2omlGRTOsSaCOeSBfluo5vI-qq3SBLCmFYKVI3Bq638oSDiklYU8vPAzYbYC1qPHVL8pZLIp7KqZOJ53TVCpbeuVGBMHMh0M0C37ziSz23yJoYpWuH97D9FbB4aoUZDNiKnvaDjTU80RocfWplF8R65PGFYJ-g1HTfscDAhpYob0vbHrWskRmo1KPIi9agA9EpUxAur0I2wj4iQ64ZEebUXvh3WJidOJEK1lksFKsKhGLtVO9Onau3AF8Xo6bV0BsJ__u-7DkG_m2KWnBjepvT-xHmP8cXxTZBwg8X4lECP9bcMDvr7xq6na2TCi_7Mg_FB92uFqXqvefNDYs0uleF3ucQbuiDAU68u3Sbj0JRehKCZqHA89jY4crgvhpRb4mSJu2ADGoEPj8AK6SwRt1NDZUReuDmqD0pfoQzpr7FaC3XomitREasG98IQLh2YgekwafAtEDUuZcPucNQtt769a7csLvJogb5H2TZyCid-FCyLrro_CZ96n-uJZRs04nE-2ksGVV3bDFRfUh1LzwJNxU92KQK3s2e4FeoVHz62SRg5-zslrglv0H2u4G4y3AKqFevOyz911ceoQfm525vTJ3QkZAQjxc4Co" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7db85dfe90.mp4?token=EDDLhzy_P_v8twGb4R9zrVBftj0nipcdTrtJMOkrSnyh6f6ihH0JufcZg6uX01eIfY2II4y2omlGRTOsSaCOeSBfluo5vI-qq3SBLCmFYKVI3Bq638oSDiklYU8vPAzYbYC1qPHVL8pZLIp7KqZOJ53TVCpbeuVGBMHMh0M0C37ziSz23yJoYpWuH97D9FbB4aoUZDNiKnvaDjTU80RocfWplF8R65PGFYJ-g1HTfscDAhpYob0vbHrWskRmo1KPIi9agA9EpUxAur0I2wj4iQ64ZEebUXvh3WJidOJEK1lksFKsKhGLtVO9Onau3AF8Xo6bV0BsJ__u-7DkG_m2KWnBjepvT-xHmP8cXxTZBwg8X4lECP9bcMDvr7xq6na2TCi_7Mg_FB92uFqXqvefNDYs0uleF3ucQbuiDAU68u3Sbj0JRehKCZqHA89jY4crgvhpRb4mSJu2ADGoEPj8AK6SwRt1NDZUReuDmqD0pfoQzpr7FaC3XomitREasG98IQLh2YgekwafAtEDUuZcPucNQtt769a7csLvJogb5H2TZyCid-FCyLrro_CZ96n-uJZRs04nE-2ksGVV3bDFRfUh1LzwJNxU92KQK3s2e4FeoVHz62SRg5-zslrglv0H2u4G4y3AKqFevOyz911ceoQfm525vTJ3QkZAQjxc4Co" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان همچنان در اختیار مردم حماسه‌ساز
@Farsna</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/458008" target="_blank">📅 20:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458007">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lT4z2jHP11U8gSaTZWybwu1goBGhzMbxuHjp1yOiSU3pe780hEldJlfzrXDrWG_PQcYHwsb6C3irkuHFdkHGuS6ScpPTD0TlSzzyquJQw4YTjxuKoVqC3tilnijfU6ij9kv8R0kiUOjTMyITVtbbyMJ6flm3NcxSFayDqOkW7qLhkMU3SYzW5ErhqxhTapdCRJl-Q6zTtnehzeVtN8l2pT6VUl8g8oILYyWzz1MyO55D9pIv0destYKwNQeXBral-fux5UIk2daYsVs1j6zDdpb93xwZcjZal5j4kbTgUgeNhbacKEgaNBHmrfuKV_JHESv44uOvJSoc_kuznnBA-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قانون‌گذاران آمریکایی خواستار اعلام هزینه‌های جنگ علیه ایران شدند
🔹
نزدیک به ۵۰ نماینده دموکرات مجلس آمریکا در نامه‌ای خطاب به ترامپ و هگزث  خواستار ارائه جزئیات دقیق‌تری از هزینه‌های تجاوز نظامی علیه ایران شدند.
🔹
نمایندگان دموکرات در نامه‌ای که در اختیار ان‌بی‌سی نیوز قرار گرفته نوشته‌اند: آنچه که به عنوان یک عملیات دو هفته‌ای معرفی شد، اکنون به جنگی تمام‌عیار تبدیل شده است که بیش از ۱۵۰ روز به طول انجامیده، بیش از ۳۷ میلیارد دلار هزینه داشته و جان ۱۸ نظامی را گرفته است.
🔹
در همین حال قیمت‌ها در سراسر کشور به طور قابل توجهی افزایش یافته و بار این درگیری بر دوش خانواده‌های آمریکایی افتاده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/458007" target="_blank">📅 20:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458005">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbWgkOWDJkMkKEaSyuSD9hEgT3ZRBTab1UK6zGAqpQq75vuTkWQM-_EhVKHC3XRLSxCRb4UOm6O0UcKhyBebrJpqZJExWXJzvVh6Drx-tQASF8X2VNzcpT69HE2ri17NeqY9G9po0uJReR7bKjLKskwMsUkFMjh7DsfIonSTPhm4-DacaptrCFgmNZ3aqRLz5xSvBRiVfkKWoR3TFKBCRMNjAd8c697lyRup0hC5tziD_xLpPsrDl_VrfokDoaDajTi5rLRryqS256TFLyAyOrpKcbESXgF2ZFoJIfZfapdKmj4dQoezjcytv9ubH5rP4WYkNbcktRdR89BFtFOZCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گل اول تراکتور به پرسپولیس توسط اشترکالی روی اشتباه ایری
⚽️
تراکتور ۱ - ۰ پرسپولیس @Farsna</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/458005" target="_blank">📅 20:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458004">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zq8Tc-XySr50nYPDcFMi6XXx98nzfJ0ObCEJBAT60f0jd003KnXeLJU5lxYz1hvOh1INYoxNUdWz2l6GMaAK-1qzDyA0BzLTHYsbY783nDo2UOjZHsF0MgWa1hEaem3bHx0BWTafvyMwp0jTtVudaJ4rrRRQNoC8wt4NThtNui3e7NOIuFBtTSx4KUqW74COeEC7p53WcrLaWkmU1S-sOcF3rFichndpvn_z882Adk4zfCSda3NjzZbr1OoyuBxYAdPySOnzOjT2p-oo-YsSmk97rc51QZTutSGYZmU5lOFLFKNSlZt5OprRahPSCnZqvMzQAYQfNFKmWsljOChFGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف محمولۀ یک تنی تریاک در نی‌ریز
🔹
فرمانده انتظامی استان فارس: در بازرسی از کامیون حامل برنج یک تن تریاک که به‌ طرز ماهرانه‌ای جاسازی شده بود، کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/458004" target="_blank">📅 20:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458003">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ee0470c1.mp4?token=lejFqCGwlxMXq1lRN3kExmWcUl17dUkr4LOqwclWCR4bmYKcyXoMqWK3dQbKPAUFEznF5a3ugwVfZparBYiTsssW8eGtO_vv1nEwFPT15nlbptzfaDDTmF4a5qdmdlDp57iDWWXMXE2GWcpsX7oWH_nOykAUWeY1YIblT-Lv_vHyEYVahb_-0itzzzlk2vJAJMxU6ApJ1_wO9Bj7Z4J42kmaNnQEiiYO706cqji5DJBElVX8J_d0g6_PsPV9Eq283dXJsvT1ia9VPHW7OSh4DyDl_DRJY-5eIvQArrdmOi25AlIof1BpHvry4Gd0i4r0ks9XrNyGgOnuuV8KfhZHsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ee0470c1.mp4?token=lejFqCGwlxMXq1lRN3kExmWcUl17dUkr4LOqwclWCR4bmYKcyXoMqWK3dQbKPAUFEznF5a3ugwVfZparBYiTsssW8eGtO_vv1nEwFPT15nlbptzfaDDTmF4a5qdmdlDp57iDWWXMXE2GWcpsX7oWH_nOykAUWeY1YIblT-Lv_vHyEYVahb_-0itzzzlk2vJAJMxU6ApJ1_wO9Bj7Z4J42kmaNnQEiiYO706cqji5DJBElVX8J_d0g6_PsPV9Eq283dXJsvT1ia9VPHW7OSh4DyDl_DRJY-5eIvQArrdmOi25AlIof1BpHvry4Gd0i4r0ks9XrNyGgOnuuV8KfhZHsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین‌باری که ایران تحریم شد
@Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/458003" target="_blank">📅 20:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458002">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1601c35a78.mp4?token=L72Aw8FBNFFQns9wADnDm6J9iFi8VOysm_4V8cgpsf8YLBwbjiSeqBroYEnAsfuHlQcWNkCecT7DGa5uZHSS3d8PbDVuhMi0TkSnmat9k1GljBABJsBBlGuJgU9iigAbVpPO8yrPfWQHzCel8dD3fXu-kCDjcxZ-m26NNlFW0HsXFBs0iMhsQosxysBNhfukrJi_MWpIU4F5a9u0ORngfr1D4ECUefSqzkHINSwJ3q_yXdTzq6vqqbnh75xPcHGJCv0vuxmAloPSyew3qdQAd495PlEXtJQiSM_Q8SZFs8blClYlgPY_OlFdtAsyH_y76azn_vd7XCLslqNO7DRMGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1601c35a78.mp4?token=L72Aw8FBNFFQns9wADnDm6J9iFi8VOysm_4V8cgpsf8YLBwbjiSeqBroYEnAsfuHlQcWNkCecT7DGa5uZHSS3d8PbDVuhMi0TkSnmat9k1GljBABJsBBlGuJgU9iigAbVpPO8yrPfWQHzCel8dD3fXu-kCDjcxZ-m26NNlFW0HsXFBs0iMhsQosxysBNhfukrJi_MWpIU4F5a9u0ORngfr1D4ECUefSqzkHINSwJ3q_yXdTzq6vqqbnh75xPcHGJCv0vuxmAloPSyew3qdQAd495PlEXtJQiSM_Q8SZFs8blClYlgPY_OlFdtAsyH_y76azn_vd7XCLslqNO7DRMGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول تراکتور به پرسپولیس توسط اشترکالی روی اشتباه ایری
⚽️
تراکتور ۱ - ۰ پرسپولیس
@Farsna</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/458002" target="_blank">📅 20:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458001">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFqqKT40Pb-J9RLk08T2gMn91OhRkqtVgM2LV8F_paFDkJK7o21is5cZzn8t78GuRs7v0p2AzinTBPNiRky87f9Y9YNDwzfWUoXYEYCfAZfONugfAM2GbHf3P94KumlU-sdWXF2lRi4zWj-T-5DSWGPu0UmJX0eoTqHka6shxSakm-0DxGlzZT81dmz1r3bNX3SrVPgBDrdoTokVPyqpOqi-dvIcAQ9N2whehXFxiiRThoCZyykzbRZK1zJnchB4mbbJ3_S2JV4n0SVpQsV9KNyoCC9PCdJuAbyvr9bvZxTHPsk9g28FejihSctOi6f9y_DlQ8ZJ8ieeOCY19C0aLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: کسی گُنده‌لافی‌های آمریکایی‌ها را باور نمی‌کند
🔹
شرکای تجاری ایران‌ به ما اعلام کرده‌اند که اظهارات آمریکا را به هیچ جا حساب نمی‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/458001" target="_blank">📅 20:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458000">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAyLnRAWaY4zfuCqrFQ3B-kOmDiQxlvn_cZlkVNw0lDhbJ6dDkvVhQ1eq-qRb8bnINGkf5YADdQ8Ag6Wd7Z5O8CDTzE_okFU_PWMB2VdaiezvT8QFXSEaaeXE-QgGxktlcEJdROKpRy9LSmXzmZ7RUG8w2DtPjdtmQO9UkHIZQFNzm4ryYMvOsHSVG8u78liOi7YN1S901dN8V0BPYwUXpbEzpGmxrX9QlgCUTgFpTa1NBUDgBcheNKop5dnI4aFvXpnhhpRQ2jrodp0TGc7OZMaZ3gV1RMeDia34MfLcCYNVoNBUzHNHvWIPaiLlOnTc084ww_MxRJtViHbIF34kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو: ایران تلاش کرد یکی از پسران من را ترور کند
🔹
نخست‌وزیر رژیم صهیونیستی در گفت‌وگو با شبکۀ ۱۴ اسرائیل: ایران تلاش کرد تا یکی از فرزندان من را ترور کند، این نشان می‌دهد که محافظت از آن‌ها تجملاتی نیست.
@Farsna</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/458000" target="_blank">📅 20:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457997">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXf4TFLSeINpX50qnqy4kXBdVgyWx5BAHb-lsnAwgWv67c11wjs5pFwRuD--HEvYAzDOgSlC1_6BH19Z3Z7X_ksphcXDH0eq2s7jrXBR6PyDVNld-7xCH7swtH_P4nc8m0t0dwEdcUBhrpNo5Yk3enMGSB9816MZ3q-lGYxZlQE99YhNkhjRhOJwFBWXnGlTvUFb8pylVarq39Vcl855ud-T6yOlvYh7XOPIpW95vK_kJdW-0-fFABVo36vg3xR-43895pjrcxa727G-2wyqKJNwFwpKOmxS51bsrbrfBiaUPmnYXMT_UIbU9thnjXsw2JOcL4FwGy7l3abx18Q0Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIb_VY_Eq3YuPCDLE1Gk6E_VgP-kDW6TFnpdKmdU_fg9EPpc-uJrTiohMysgMNARp8eXgGKtnNXnXScTzdEf3IrGMBuKEdA4tBWgG8WPH-uZqVUrWpc6aedn-rBgS5o2_gWj3wxy3sl4k7BJgaOmBBShOtHezUxaV38GM8vN9bUuqUonjetshP3U1TuGn0eavkiynlQZNm24WacWhbRvWQjxQyGDh2OD-hBJy-IlTBojxFDkQe76gVtjb790XLyNdr0wrPnEBSo4UCNKeVHjBca-kYoGIJyoGjmpNNOBPLIJCoglhtqUNYz4a39t4f-R9Am1Fq7HZXI9QenIZglXYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IZfE_DLdj6CLcG9gwpQSH4wxt9eKgB9ZYC3tKcxoj6-dakzSobB2RJOmWVaQ2EygIYPzm_pPAgsZKs2wBa9wls_zJhUnqKGw51tb0Va0EbbJBDRdRDTLxF_d5lXgY49DvnMhDtTige74hVWKiDSOTSzU8Pwu_Zma7MEi_jiqzNa829NV3bA4aPp4Y6kTwowxjbJDsnMVjB0KJ1lLGVRfFyv33p6c1VLn2M2XN_JJ0Lu-yErbYkmhyZyU-8ObrbO94UkOJZvKXKvHJwNnWgXBPCEmLB_6ffEQhhQAhdOuHBcFQiV1Kaeua3IHqkVHZRfWNpdnxrrS7y3Sbd9Omh5a_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قالیباف: پیگیر اجرای شروط تفاهم هستیم و این آمریکاست که باید به تعهداتش پایبند باشد
🔹
رئیس هیئت مذاکره کننده ایرانی: تعهدات طرفین در یادداشت تفاهم روشن است و این آمریکا بود که با بدعهدی مانع برقراری ثبات در منطقه شد و دلیل دیگری برای بی اعتمادی به این کشور…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/457997" target="_blank">📅 20:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457996">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILixsGII2vuTpXaPSSJ3znV2qG2R2CvcQtPapIHEvmi3PSC0FQZ-9r8Eic7IwKRu4LiN0D5Lz9cDOwScV3lHD0YB4fea1Zj6KzIdbmH1L_OBfP1ldPuzhNNi3sBa7_cnga3tSIDBfIZaMuN9HO7f79oy6JM9zaEndyP9eLZzsAlF6tmuwhSar-pfFtYFaZnwBpbLrW_4K8DYoTGNyYOYppdsskQ27lqyIyEvGFe_P7vwLdN8x3gPll6KgyO-ksQteTXs-oBSEBieE0OUZ1_A9gFywBi9gsT7Aj1WScEwAeNYs3igzF1FMPxZuE28s21bIF9cVQWvhSEf2C-N_f-Tag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگلیس فناوری ساخت موشک‌های دوربرد را به اوکراین می‌دهد
🔹
انگلیس در اقدامی بی‌سابقه، فناوری طبقه‌بندی‌شده موشک‌های دوربرد استورم شدو/اسکالپ را با اوکراین به اشتراک می‌گذارد.
🔹
این تصمیم به کی‌یف امکان می‌دهد تا این موشک‌های پیشرفته را به صورت داخلی تولید کرده و وابستگی خود به تأمین‌کنندگان خارجی را کاهش دهد.
🔹
استورم شدو یک موشک کروز دوربرد با قابلیت شلیک از هواپیماست که برد آن بیش از ۲۵۰ کیلومتر است.
🔸
اوکراین پیشتر از آن برای هدف‌گیری اهداف راهبردی در عمق خاک روسیه استفاده کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/457996" target="_blank">📅 20:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457995">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9b993397.mp4?token=kAk6hSjQDka3xrARwgS5i8vZs1E_d2sdS61nz9oI0Tow77-7naTlRfLt6zhNy5dqw992tnh5wX_SzAh0o9qgupuqpJexrKON8koMP9jedhVBS-uIcL6acZjzb8gcnDOYzCANdKnYvhy8KpvJIs0Zel1phlXc1x7IN2VakwULzBiZkZ9TbSDRu586wnyG0QQdbK9g9jG-QEk31y1qq5qri1ZELF60A10oy-9MUqkeSLwmU7FBeYJ7jn3sK0CqwuHD6CQGrp8OJQy_d5Vrow7M4_3_mgGafgobUddMd9nxoRzSIlyuojTUQUsutU06aShj0q1qJtqduJpG3kSqthtJyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9b993397.mp4?token=kAk6hSjQDka3xrARwgS5i8vZs1E_d2sdS61nz9oI0Tow77-7naTlRfLt6zhNy5dqw992tnh5wX_SzAh0o9qgupuqpJexrKON8koMP9jedhVBS-uIcL6acZjzb8gcnDOYzCANdKnYvhy8KpvJIs0Zel1phlXc1x7IN2VakwULzBiZkZ9TbSDRu586wnyG0QQdbK9g9jG-QEk31y1qq5qri1ZELF60A10oy-9MUqkeSLwmU7FBeYJ7jn3sK0CqwuHD6CQGrp8OJQy_d5Vrow7M4_3_mgGafgobUddMd9nxoRzSIlyuojTUQUsutU06aShj0q1qJtqduJpG3kSqthtJyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعترافات صریح ضدانقلاب: جمهوری ‌اسلامی تسلیم‌ناپذیر است
مردم هنوز به خیابان‌ها می‌آیند. بچه شیعه شکست نمی‌خوره!
ایستاده می‌میرند اما تسلیم نمی‌شوند.
تا آخرین نفر و گلوله می‌جنگند و رفتنی نیستند!
@Fars_plus</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/457995" target="_blank">📅 19:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457994">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlVESqFlKgLnNv0Tr4Zox4nwnlNEk0hg2D48GsKVkdv6pNqjiYWow_7rTwQV8Cbh_yqnjS0y_kZ6wXtrW-fSTmwHfPTes3y_DjVrCWauEqoRDqTXz4HqfBGj0wtZvhWSKzD2dY3upDWoAhxfdAj1ApHzXd-pBxEoIft_fbeLB_lpf9Rpr3Btf3stbKQ9sMmHMCEmqZqbPPlyN-mDH2LGB-wP5uizjTxAVjF8GhHx3IhQg9jGTfBwBflJMzvzEF9xVFWTzlACFmMy2cMzLfKoNGHB4iJXjlpnzcjxb-KlHvs0L31mZJR34x6vN4odnLyra_e_RknYaQu5q6WyoZmXcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش بدون قرعه‌کشی ۲ خودروی میلیاردی سایپا
🔹
سایپا از ساعت ۱۴ روز چهارشنبه چانگان CS۵۵ پلاس با قیمت ۵ میلیارد و ۶۰۰ میلیون تومان و سیتروئن C۳ XR-V۱ با قیمت حدود ۳ میلیارد و ۳۰۰ میلیون تومان را تا زمان تکمیل ظرفیت در
سامانه فروش
خود عرضه می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/457994" target="_blank">📅 19:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457993">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e21f2ed615.mp4?token=h6KB4HimAbnLVrNp80OFeuyMHILNgVjme45GBAIvM4NI9Dh_f8tdM8t5ZhFJlDu3WME4jhnoYFzt5H5fkwMNF9p1B9TVnct3Z_QkE2Zl_4oSFM0hlahl5sJ5B16peOu_LaDlo233j6bwa7GsWUchJ60RBFShLE03VwYeI7DdCsHkeeUG58bAOsxpWqwTGxuMfvzpi1GX2mjp_gHFyTbCIWsT3MvUP0rMkQl3cH-zZvujaCn15I0nazoKlAgBECSyRt4smNK4R4DUOfbfEhLI-JUmE-yVOpVyp7TkWbbSwcMQ_U-HFuJ2xnAYQdJPa6fHXCJhYctS7JHBRGk87GLFyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e21f2ed615.mp4?token=h6KB4HimAbnLVrNp80OFeuyMHILNgVjme45GBAIvM4NI9Dh_f8tdM8t5ZhFJlDu3WME4jhnoYFzt5H5fkwMNF9p1B9TVnct3Z_QkE2Zl_4oSFM0hlahl5sJ5B16peOu_LaDlo233j6bwa7GsWUchJ60RBFShLE03VwYeI7DdCsHkeeUG58bAOsxpWqwTGxuMfvzpi1GX2mjp_gHFyTbCIWsT3MvUP0rMkQl3cH-zZvujaCn15I0nazoKlAgBECSyRt4smNK4R4DUOfbfEhLI-JUmE-yVOpVyp7TkWbbSwcMQ_U-HFuJ2xnAYQdJPa6fHXCJhYctS7JHBRGk87GLFyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفتند قبل از رفتن به اینجا اشهدتان را بخوانید  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/457993" target="_blank">📅 19:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457992">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRRXq88W6VfI2YBQgOQ_zhDt05SWaErZGfv4yLinR0v-W54ou89TLkg7W-6EVW2Dlgbvah_6MbNClBu9_TWVQzUy1GCxmZ3ua8DoJbHyW2IlsgJn7UAKG7lftUgboOtezObZe-cD3l6NvHWTIScfRROwlRt-upBZevA62ggCy0pL611-g5qlyYGnQZb5qMzNz8dZZSKgIhnQZX3ot8yqd8yCxfT3ZRbNCoyLypG8J40R5bGxeCTqHSxVGXnEzlaDjicTmTmbn1bVq70euO1H2lgsjSMDAsAUqMHO3Wyje1UYk40dWFb3tiiH7acbiKkg-F4zFUcD0MQ4IEy8bNNgPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار فرماندۀ ارتش پاکستان با قالیباف  @Farsna</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/457992" target="_blank">📅 19:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457990">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">📷
دیدار فرماندۀ ارتش پاکستان با قالیباف
@Farsna</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/457990" target="_blank">📅 19:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457988">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjCCkBauihlKtcPONBRXlastedTtgeu8sP6y23lCXQ_g1V456QCU0w4oSIuX-U37oZkq7NDdRp_4lF8uSbI5_8HLMHRbZ_a6PyNbMytASqj2_8NApXoKUK_nuWLfLWPC7KiiHyLq2ZkCKQojtEHlnOH6vM9Bgz4H9Xv6EMWS7AwrOa-DKseP01F9dDp56f_6-l0w6lFYXHKyNQlZQTCG0aB4HM9DRWmBes009yuE0P2s6nopon1PgzWjolTx1TOvBQ6tJvw7C0i067waa2fFTWGB_e6FrVwswhlSzlXTzv-g0vHTs-6TuEhcOjhBi1c2xzBjrdB_JMDGyZ_0LdTPbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقلای ترامپ برای ازسرگیری مذاکرات با ایران
🔹
شبکه خبری الجزیره به نقل از یک منبع آگاه خبر داد رئیس‌جمهور آمریکا دونالد ترامپ هفته گذشته با فرمانده ارتش پاکستان، عاصم منیر، به صورت تلفنی گفتگو کرده است.
🔸
به گفته این منبع، ترامپ در این تماس، درباره پرونده ایران گفتگو کرد و از او خواست تا از نفوذ پاکستان برای از سرگیری مذاکرات استفاده کند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/457988" target="_blank">📅 19:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457987">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8987415951.mp4?token=n8vGb-njPUK8NMq6kfV-FtJkda97qZRfA2x-4c-3JZhsL0kshIkcRFXHmW5CjlPqe0KqMZ-F6jhAIRjPnAv5FTsAc-GcfEW7c7s-RxJOlTxH9qrIgkHAsp_P_hrLa2WXP3FzPlHHLiwgTCXEsgXq-9MOt2VSAgFpy6oEWYgtsb5ohg7JW8VzQG4B5XgS-w3sLZn8g2wpdb6tZ7vk0QMzsRCmeEtfpMGnOme6u68aFmwT1UQ2hb1lxszyFHSjKJtmp74PPSnWd8qZCoWllHrg7puZr2zcgh38LaNSrtn8X7HCdILtHjMNJyNbovQkiVZu4Rcpig7a2tMdjgpx5nA81Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8987415951.mp4?token=n8vGb-njPUK8NMq6kfV-FtJkda97qZRfA2x-4c-3JZhsL0kshIkcRFXHmW5CjlPqe0KqMZ-F6jhAIRjPnAv5FTsAc-GcfEW7c7s-RxJOlTxH9qrIgkHAsp_P_hrLa2WXP3FzPlHHLiwgTCXEsgXq-9MOt2VSAgFpy6oEWYgtsb5ohg7JW8VzQG4B5XgS-w3sLZn8g2wpdb6tZ7vk0QMzsRCmeEtfpMGnOme6u68aFmwT1UQ2hb1lxszyFHSjKJtmp74PPSnWd8qZCoWllHrg7puZr2zcgh38LaNSrtn8X7HCdILtHjMNJyNbovQkiVZu4Rcpig7a2tMdjgpx5nA81Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کار مرا به گردش چشمی تمام کن...
🔸
نماهایی خاص و متفاوت از حرم مطهر رضوی و حضور عاشقان «آقای شهید ایران» در جوار مزار نورانی ایشان
@Farsna</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/457987" target="_blank">📅 19:14 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457986">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pd_jubxKwkPbmd81sgk2D74s0yJj7m4V587TS6uUupFEFFaZKvR3uFQYCAXrcJxQtBjKlFvQ0gEp_dVPYaYzx4cwR5N3UQ66RQeG9bDWxm28NwQbttR5Uv5b_7t1W5LE5U-55ABj8_poXjHB4we43gkoFoHlqIMm37n0aICFQa9g4XtlfdnwDC-Oq8vVSsHYfTYT55tEYm6x4Qov10coTg0A5hS_FQAlkpJ9QWYDTIXpDxhoLN8MgZa-DaG-8s3KE3gE5OU66Uuikhfh-4x4ZiomLYP2aDNg-ObxUzhotFV_dpdykpLzIBbXYFl9LJuZ_L0IwxbRdIWeDp6wJaCPJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخبر: پاسخ ایران قاطع‌تر از گذشته خواهد بود
🔹
۴۷ سال راهبرد خصمانه شامل تحریم، جنگ و توطئه برای تجزیه ایران، نه‌تنها به نتیجه نرسید، بلکه امروز با انسجام ملی و بازدارندگی جمهوری اسلامی در تنگه هرمز مواجه شده‌اید.
🔹
این شکست راهبردی، هشداری قطعی برای تداوم محاسبات غلط شماست. پاسخ ایران قاطع‌تر از گذشته خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/457986" target="_blank">📅 19:07 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457985">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVLdnL6UUGfEA6lqAnNJ_9GIC7LT2ciewzMqA_3U3MfNFUIiBOzKGgk2dUE7uT3r3ffFDsymaLnEoiHVB3QXOJT_p1-slRZkCXXZF1pVoL8ndV7kb8y0YxlzUqZ7aY0gfwAXZ6rEzSJuPSfkF7vzqEmKluWxE_DOysubG1DyPto24kgtV3LHwIYINxF7KYlTstG-JLFcvpzB_HgeL6-5pn6f_HGE2qVviTEnojz8DOYWmWampkbJFdDrHSswVxw7uKpaJOf1SeWhpLM-RbQJmeEPZnTwX9RW0viurT1fZiZ6vzIb01HBBc5_2EKdTX--kTuXskMs_5ojhToYElKHIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانادا آمریکا را به قطع صادرات برق تهدید کرد
🔹
کانادا تهدید کرده است که در صورت تشدید جنگ تجاری بین کانادا و ایالات متحده صادرات تمامی برق و مواد معدنی حیاتی خود از جمله نیکل با عیار بالا و اورانیوم به آمریکا را قطع خواهد کرد.
🔹
داگ فورد، نخست‌وزیر استان انتاریو، گفت: « شما حتی یک دانه شن از انتاریو نخواهید گرفت» و افزود: «آن‌ها بدون نیکل با عیار بالا چه خواهند کرد؟»
🔹
داگ فورد همچنین اعلام کرد که «همه چیز روی میز است»، از جمله تأمین برق ۱.۵ میلیون خانه آمریکایی و همچنین مواد معدنی حیاتی مانند نیکل و اورانیوم با عیار بالا.
🔸
این اظهارات پس از آن مطرح شد که ترامپ از اعمال تعرفه‌های جدید ۵۰ درصدی بر خودروها، قطعات خودرو و فولاد کانادا از سال آینده، و همچنین تعرفه‌های ۵۰ درصدی بر ارزش ۲۰ میلیارد دلار از کالاهای کانادایی از روز شنبه خبر داد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/457985" target="_blank">📅 19:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457984">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIc9loS3JhVO5sqffaCjs_aMQo9zwhlGX3TwYuaFbrhSXLChN85HtpgekXs0x2X2-6yoqluArA3sBG3lAxq6gldSLcRt8N4IH4MOxKxFcaf2Ml0ew6td11wQ7rA0AjYAmHcOE8QY_6xqnzl2J1Lv4GxvRo7XR5JS_cDTrPUMFM1nzBOnxVtk7x7jyihuIxqR_oXurVEkSof1i13_nhRehDO41th0ZEXwY5c6NA9KHHltQSPStY3YlDwo_Gi4SrqqtUibcSW6LZwFh4KuYNjcyGhv_3K_borwLMIQItXxkZgR4dVMEsZPjrmQXNx8P4oFXpIJVi3Xmf4j1o-v9etltQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: طرح مقابله با نفوذ بیگانگان به فعالیت علمی ضربه می‌زند
🔹
معاون اول رئیس‌جمهور: تصویب این طرح برای فعالیت علمی کشور زیان‌بار است و می‌تواند استادان را نسبت به تعامل با دانشگاه‌های معتبر جهان نگران کند.
🔹
فکر و ذهن استاد و دانشمند باید بر پژوهش متمرکز…</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/457984" target="_blank">📅 18:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457983">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5baa8d43fa.mp4?token=sDGSxsSRzV8F2QtEApToUpycJA0qyy7u53KbCexLrxmiQKux01VSPM1QNS_QzCHNeW7F7PgfM9qPVnZt87aPY0HFOCYR8KhCEHNriV61ZMqzBVDwdJOWKaFKE9wGOBmi3wR-Ej5P_YzQd9hm-FasiT8wNUlLQ94SVQvZVtKkjbSQMP3XtMsuLLBUuzljV1lN0TbYDNwaq6Mnjgll7SvCvwy94WxoKU0nTLZYoKex9I2PnspTwegdsx8d4lsJhtJo0gggUH8Dn5HF0SEpxj1QW2calxYn8YRnXDdGu11Z0yeb-97jHO9Rnagk4kq2fXMahuyQsGroDUKj4-VX3XP-qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5baa8d43fa.mp4?token=sDGSxsSRzV8F2QtEApToUpycJA0qyy7u53KbCexLrxmiQKux01VSPM1QNS_QzCHNeW7F7PgfM9qPVnZt87aPY0HFOCYR8KhCEHNriV61ZMqzBVDwdJOWKaFKE9wGOBmi3wR-Ej5P_YzQd9hm-FasiT8wNUlLQ94SVQvZVtKkjbSQMP3XtMsuLLBUuzljV1lN0TbYDNwaq6Mnjgll7SvCvwy94WxoKU0nTLZYoKex9I2PnspTwegdsx8d4lsJhtJo0gggUH8Dn5HF0SEpxj1QW2calxYn8YRnXDdGu11Z0yeb-97jHO9Rnagk4kq2fXMahuyQsGroDUKj4-VX3XP-qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویلاهای ریاست‌جمهوری در قشم فروخته می‌شود
🔹
دبیر شورای‌عالی مناطق آزاد: ۲۸۰ میلیون یورو برای تکمیل پل خلیج‌فارس قشم نیاز است. این پل از طریق تهاتر نفتی توسط پیمانکار ایرانی ساخته می‌شود. پل خلیج‌فارس، قشم را به بندرعباس وصل می‌کند.
🔹
ویلاهای منتسب به نهاد…</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/457983" target="_blank">📅 18:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457982">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfGiYrKZ9uVyBHYkiq1KxmrP1oqv5-_zZAWCdq5ZkgzI8O46FeeE_kmkVZKG993voerHfk0zQ3vdUhIq51pr0QPFKeIeJ9UDoBIYtBPNcCwglXUUP_XU4TVhaU9B6ZPnLuP3MZmvlxmueuQH7iV_ko2-d0iP48KB_R37BWDN6iUdhLeAZGe0PLttVta0DhJA01zZTu_vUwCZKhr-svV-S_eBy7wHePj7ZAO3DHQVaZ_wlCcMWS77VL7P0bVp-eiI2nP1yYQKfmQ0zbbjuI7SuW_OkuW3k3t7vTxHsEJsBu1hIsiIqhXlexEw2OX_LyTdaGGJiJVji7AV4pMFgGUSfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ دولت با «طرح مقابله با نفوذ» مخالفت کرد
🔹
هیئت وزیران با گزارش کمیسیون امنیت ملی مجلس دربارۀ طرح «مقابله با نفوذ سرویس‌های اطلاعاتی و دولت‌ها یا نهادهای بیگانه» مخالفت کرد.
🔹
دولت دلیل این مخالفت را ایرادات جدی طرح، از جمله ایجاد محدودیت‌های علمی، تشدید…</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/457982" target="_blank">📅 18:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457981">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYG_V6RBGxR4bSs8ZAIrRhOPft1PiR3wLM_6Kr6IWd7MheUtLtsTITbK4AX-kzzgbb0uCm8-YzVbv2vnmlniU8F_IJqLttx_xtmTXilby-tJYLBjID8imoN88WQwP4KF3VB5R4N1c5MPaKu4ZXGuqkKlTvcjkAnY_-lnRz3KW_Y_v1EjBsUB4iBkDO9MdPXrbD3g9uO8_hTAAXR6AyEr7DlMqohQUk6a8MMEnkV2NEesDEkO3ssDrtrydWnoSvlq74J_WPpzgehFR_QVogNgSPW9EtEUPwJLUoNN2j0YpP7wVyaHct5C-7_dv5ys6H_YnRoulDE2J1ePyUeIxyK4Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوچ تجار ایرانی از امارات به چین
🔹
شریعتی، عضو اتاق بازرگانی تهران: ۸۰ درصد تجار در امارات تجار واقعی و ۲۰ درصد تجار با شرکت‌های کاغذی صوری بودند که از اختلاف نرخ ارز سود می‌کردند.
🔹
همهٔ تجار غیرواقعی که از امارات رفته‌اند. تجار واقعی مثل ما هم به چین که «شریک اول تجاری ایران» است، رفتیم.
🔹
تا پیش از جنگ فقط ۱۰ درصد تجارت ایران با امارات، مربوط به این کشور بوده و ۹۰ درصد مابقی تولیدات، مرتبط با کشورهای دیگر است که امارات مبادلات مالی آن را پوشش می‌داد.
🔸
حالا بعد از جنگ ایران بخش اعظمی از واردات به مسیر شمال، مرزهای زمینی و ریلی شرق کشور منتقل شده و ایران به صورت مداوم زیرساخت‌های این مسیرها را افزایش می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/457981" target="_blank">📅 18:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457980">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOoD5-plpPkBtulSr-7jI5Xj67QAm9tKDlCIh9QyavwYH7G9achHUsFpWLWJj3L0EZWXYbCrB-heeJM06hg282h7pw6cROtzOhRidqQjWc3633EP4MqJVCQo-uY7xuBc82SzLyYgJco_4Ypr-c3ywAyGW-105cD62_RB4cSiKptNm1JhPBoqeywyizmTyqIywZLU2PS4meY3zPoIsfWue4n-XMDwT5NC3qYk-6FP7CCslrhDpWcbPEwe1QA5urhr8AWtSOTzg0NrSScc5VNJHr6vX7GOkQJR3ncvfbEssFBiuFcOXkwlEOvaeKJum257XsyTvXrzgZem-QToI1pWlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: برخلاف تصور دشمن تولید موشک‌های هوشمند و هدایت‌پذیر ما استمرار دارد
🔹
سردار محبی: دشمن در این جنگ به دنبال ایجاد اثر ادراکی در جامعه بود، آمریکایی‌ها با هدف قراردادن نقاط کم‌اهمیت و برخی چهره‌های ارشد نظام، به دنبال القای ناکارآمدی ساختار سیاسی و نظامی ایران بودند. اما واقعیت میدانی نشان داد که با حذف یا تهدید افراد، خللی در ارکان اداره کشور ایجاد نمی‌شود؛ چرا که نظام اسلامی بر پایه پیوندهای عمیق میان مردم و حاکمیت استوار است، نه بر فرد.
🔹
دشمن با هدف قراردادن پایگاه‌های بسیج و پست‌های بازرسی، گمان می‌کرد امنیت خیابان‌ها فرو می‌پاشد، اما حضور مقتدرانه نیروهای فراجا و بسیجیان در عرصه‌های عمومی، این سناریو را بلافاصله خنثی کرد.
🔹
با این حال، دشمن در محاسبات خود یک متغیر حیاتی را نادیده گرفت؛ همبستگی ملی و ایمان مردم، مولفه‌ای است که هیچ هوش مصنوعی و ابررایانه‌ای قادر به محاسبه آن نیست.
🔹
ما نیز در مقابل، فناورانه جنگیدیم و با هدف قرار دادن اجزای شبکه عملیاتی و اطلاعاتی دشمن، چشم و مغز عملیاتی آن‌ها را از کار انداختیم.
🔹
برخلاف تصور دشمن که ذخایر تسلیحاتی ایران را محدود می‌پنداشت، تولید موشک‌های هوشمند و هدایت‌پذیر ما استمرار دارد. مهم‌ترین دستاورد این جنگ، انتقال آسیب‌پذیری به زیرساخت‌های حیاتی و مراکز وابسته به دشمن بود.
@Farsna</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/457980" target="_blank">📅 18:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457979">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qj5zPOapjQHZSgWPQ7F2vfibCNCSu5GKUMmukZ1U9L-7ghcPTlWHk85hAF6o9DU8OYun0fxwzvdsATLJGOyd_bgX64Q06K5laMEwsVTt8Zy7c4tiymQ-so8CwgksiIJzLZdfFGp9PNOWAQMaO1azzPh6e1Pi6HzspJ-yts3ldpt7QN8ccAUxd8196j7D9O1TQghdsUGkCGaYhLduf5cwCa6b-f7b_PJ-cGGNwT4mNXUQPSZps1IDeva506i24mpcDreep1lXzpLwgMNK0qTijxbVi3SQdU1t14vDW6NqqTNplZA-ALo_J0bG7D7P6hDX031wm2sjXuA4xdW6ueIbUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸۰۰ هزار میلیارد تومان پول مالیات در جیب دولت
🔹
آمارهای رسیده به خبرنگار فارس از سازمان امور مالیاتی نشان می‌دهد در ۵ ماهه ابتدای امسال ۸۰۰ هزار میلیارد تومان درآمد مالیاتی وصول شده است.
🔹
این در حالی است که سازمان امور مالیاتی در ۵ ماه اول سال گذشته ۵۱۲ هزار میلیارد تومان درآمد وصول کرده بود. این یعنی درآمدهای مالیاتی ۵۶ درصد رشد داشته است.
🔸
در ۴ ماهه ابتدای امسال درآمد نفتی پیش‌بینی شده در بودجه هم تحقق ۹۹ درصدی داشته است. نفت و مالیات دو منبع اصلی درآمد دولت هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/457979" target="_blank">📅 18:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457978">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38b2c1deee.mp4?token=hQhAlslL6FUHyBG3WuyaRbS_IjBlshTm_7W8tg28B8eULb1OWYtUqHu9QLCdedFZy6coreWSBl8_xwfSs6CbA8flw8Wo3H0h5L3Yor1UBRqzXS3rz4k-5DkiZZSNVylP5dQqKBKITzpNK6uZPsL8CtkHqIDEsdhegOND1-Z1MHxUj6pm5UfvVCt2yYwiJtgPr7Qr9mzNPykgdG7hp_YVUpDg8-H_-8un34MHcVDGgAKdl-OQ1VX1M41dNNH3ELlAyoVp1v4F9XQrDrWbTjS1dSK8SJO6ByzfpWohCWE94yNw0E3H4ivGKG8Fcbc-YGz3v1VTa2V0FwobyBJYkILhqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38b2c1deee.mp4?token=hQhAlslL6FUHyBG3WuyaRbS_IjBlshTm_7W8tg28B8eULb1OWYtUqHu9QLCdedFZy6coreWSBl8_xwfSs6CbA8flw8Wo3H0h5L3Yor1UBRqzXS3rz4k-5DkiZZSNVylP5dQqKBKITzpNK6uZPsL8CtkHqIDEsdhegOND1-Z1MHxUj6pm5UfvVCt2yYwiJtgPr7Qr9mzNPykgdG7hp_YVUpDg8-H_-8un34MHcVDGgAKdl-OQ1VX1M41dNNH3ELlAyoVp1v4F9XQrDrWbTjS1dSK8SJO6ByzfpWohCWE94yNw0E3H4ivGKG8Fcbc-YGz3v1VTa2V0FwobyBJYkILhqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ هوایی اسرائیل به جنوب لبنان
🔹
خبرنگار الجزیره: جنگنده‌های اسرائیلی ۲ حملهٔ هوایی به شهرک المنصوری و مناطق اطراف آن در شهرستان صور، واقع در جنوب لبنان، انجام دادند.
@Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/457978" target="_blank">📅 18:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457976">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee6df3ac2.mp4?token=THG5ZP1Ogk2Gd-ov6l2iNsMz95z4DqucovSHeXBDkk4tonptUl09oNhBudwmM0KwTDi6K6KWg3r577b6_wLLhv5ZcipA_R7JQ_JFNzPKGeX2nKURZW7lh3skJT8Fk6WIWQndOwKaawN6X906wPdKQiYrfGYcG6mCtYFZ2alFdtVO5-OEXXJ1pmHOBYIbrTX4k_ytLHT6-E3Yu6h5rltbkeaoTIrC2L-d0rBNTGqGEQWiptVWDJVsqCETE_x5EG0whxw0QSqgB7omxDTzkKEDrlrovXrC-_Y7Y6CVGYJW_YcVdiR01zpTxVm7Wr7UMRt18eO5U0dbQROa6XNNJdj1TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee6df3ac2.mp4?token=THG5ZP1Ogk2Gd-ov6l2iNsMz95z4DqucovSHeXBDkk4tonptUl09oNhBudwmM0KwTDi6K6KWg3r577b6_wLLhv5ZcipA_R7JQ_JFNzPKGeX2nKURZW7lh3skJT8Fk6WIWQndOwKaawN6X906wPdKQiYrfGYcG6mCtYFZ2alFdtVO5-OEXXJ1pmHOBYIbrTX4k_ytLHT6-E3Yu6h5rltbkeaoTIrC2L-d0rBNTGqGEQWiptVWDJVsqCETE_x5EG0whxw0QSqgB7omxDTzkKEDrlrovXrC-_Y7Y6CVGYJW_YcVdiR01zpTxVm7Wr7UMRt18eO5U0dbQROa6XNNJdj1TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودروسازان چطور بنزین‌ را می‌بلعند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/457976" target="_blank">📅 17:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457975">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‌ حملۀ موشکی یمن به تجمع نیروهای سعودی
🔹
نیروهای مسلح یمن: در حمله به تجمع نیروهای سعودی و یک کاروان حامل تجهیزات نظامی، بیش از ۱۰ کامیون حامل سلاح که از خاک عربستان وارد یمن شده بود، هدف قرار گرفته و منهدم شده است.
🔹
همچنین چند تجمع نیروهای سعودی در منطقه…</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/457975" target="_blank">📅 17:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457974">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‌  یمن: یک کشتی سعودی را با موشک بالستیک هدف قرار دادیم
🔹
نیروهای مسلح یمن: نفتکش امزان متعلق به دشمن سعودی در نزدیکی بندر ینبع با موشک بالستیک هدف قرار گرفت که منجر به آتش‌سوزی در کشتی و فرار تعدادی از کشتی‌های دیگر حاضر در منطقه شد.
🔹
این عملیات در چارچوب…</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/457974" target="_blank">📅 17:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457973">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یمن: مانع عبور ۴۸ کشتی شدیم و ۸ نفتکش را هدف قرار دادیم
🔹
سخنگوی دولت یمن: نیروهای مسلح یمن از ۲۰ ژوئیه گذشته تاکنون، موفق شده‌اند چندین معادله جدید را در برابر عربستان تحمیل کنند.
🔹
نیروهای مسلح یمن توانسته‌اند معادلهٔ «محاصره در برابر محاصره»، معادلهٔ «حفاظت…</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/457973" target="_blank">📅 17:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457972">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70cfdea7b6.mp4?token=HJlRZqFuyUIk8Y0BXu9QmQFccFymCdCy9vdB9XvwVg3powyf9HPvsI7QGw-CrO6Zv9VDfPV74EPIO5dsLnU1jiVXJ6HwpySeqrzuYJqNVcWiiP2lExZoFQiX4DlzvmHf-R99o6xRY7fR5POh5YNF44lLhaXrdY98Q2Z1XC2hyS0k71-awMTVZfKbu9j4Pk_Sr45EdZuzGDvRnehtlcx-qfdqWOkHBrU27b66Z0QxSWZQLABu9pEptFeIRBlY34PkU_hZVVcdk0QT1qyqc9hZJLMFM8vQ85DV4-nZTVAJz6zVZ_FMzChD3I_VNyM5x6ns18bhX7iIlGDqNXij5LkFiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70cfdea7b6.mp4?token=HJlRZqFuyUIk8Y0BXu9QmQFccFymCdCy9vdB9XvwVg3powyf9HPvsI7QGw-CrO6Zv9VDfPV74EPIO5dsLnU1jiVXJ6HwpySeqrzuYJqNVcWiiP2lExZoFQiX4DlzvmHf-R99o6xRY7fR5POh5YNF44lLhaXrdY98Q2Z1XC2hyS0k71-awMTVZfKbu9j4Pk_Sr45EdZuzGDvRnehtlcx-qfdqWOkHBrU27b66Z0QxSWZQLABu9pEptFeIRBlY34PkU_hZVVcdk0QT1qyqc9hZJLMFM8vQ85DV4-nZTVAJz6zVZ_FMzChD3I_VNyM5x6ns18bhX7iIlGDqNXij5LkFiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درپی حملات انصارالله یمن انبارهای تسلیحاتی سعودی در گذرگاه «الودیعه» به آتش کشیده شد
@Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/457972" target="_blank">📅 17:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457971">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d357e8d93.mp4?token=CdvpVF6XwETcYD1Ijfe7QV4fIyJVLJTgJmJzOHca3y8lhZWbFroupWC23hCEeMRv6BBSnp5lRxzUJtzjs2RF53l4yUGBIPMGyo-YfbI54OQkC4tL9cK7DGzHB3wRzHl6R4OA4uFNTo0DmKY8rMi0doykfCP3Qq4dV3dZ8dFL_MdNwbleQCmh216JtHST4HnTMdKrfLv519MUO0wQcmqX7PYS_Iykxm7V-BPAB6iAHiwO44CW9WYmlpbUhhG7G4FDNYE-rNQtMtaH5F0I175H-ZFD-0sGs8G2xHyCJHNlITeX0lskK4Fx9yfNCdxF1GhP30jijFHEFFaD4KnVLxLuQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d357e8d93.mp4?token=CdvpVF6XwETcYD1Ijfe7QV4fIyJVLJTgJmJzOHca3y8lhZWbFroupWC23hCEeMRv6BBSnp5lRxzUJtzjs2RF53l4yUGBIPMGyo-YfbI54OQkC4tL9cK7DGzHB3wRzHl6R4OA4uFNTo0DmKY8rMi0doykfCP3Qq4dV3dZ8dFL_MdNwbleQCmh216JtHST4HnTMdKrfLv519MUO0wQcmqX7PYS_Iykxm7V-BPAB6iAHiwO44CW9WYmlpbUhhG7G4FDNYE-rNQtMtaH5F0I175H-ZFD-0sGs8G2xHyCJHNlITeX0lskK4Fx9yfNCdxF1GhP30jijFHEFFaD4KnVLxLuQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مخبر: مسئولان نظام برای احقاق منافع کشور هیچ اختلافی ندارند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/457971" target="_blank">📅 17:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457970">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r02ANR8hfSNJAIvTUCWxhi_JyboSC9Rae9Jok6DTtD2oi_MTddAZII7IpovWt5gwMhzU8_XmjhzWv59ppDkhg7pI-NHQu_I9vXHGa5BIMgYXR7vcC2c1XGoicBQ7DdMDDwknszULc0iyV89qAQK-tZm1zmyNIiCODUOe0TG65402-39ymilgAt1-QvzBNoOSTL5JYb5i6ITMVS2ga1F9awLpJU7cOkyfoXN98j_kG7Y5LLk-BstvcqgVjE9_CY9SJCBnF37m8WnpPEq5q3XiGNpP3xDv6EyqI1Ko7jVkFWY2QmgIb0b9ZKlSI-sDco6J2O6tD9SFgOl_D4pYG_vimg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی وارد بازی ساخت «مغز» گوشی شد
🔹
رویترز: شیائومی با توسعهٔ تراشه‌های اختصاصی Xring O1 قدم جدی‌تری برای کاهش وابستگی به تراشه‌سازانی مانند کوالکام و مدیاتک برداشته است.
🔹
این شرکت حالا تلاش می‌کند بخش مهمی از فناوری محصولاتش را خودش طراحی کند و تولید تراشه‌های پیشرفته را به تی‌اس‌ام‌سی بسپارد.
🔹
شیائومی برای تولید تراشه‌های جدید خانواده Xring با تی‌اس‌ام‌سی همکاری کرده است.
🔹
این همکاری نشان می‌دهد هدف شیائومی صرفاً ساخت یک تراشهٔ اختصاصی نیست؛ بلکه این شرکت می‌خواهد کنترل بیشتری بر قلب سخت‌افزاری گوشی‌ها و دیگر محصولاتش داشته باشد.
🔹
تراشهٔ Xring O1 اولین گام مهم شیائومی در این مسیر بود و این شرکت اکنون توسعهٔ نسل‌های بعدی تراشه‌های اختصاصی خود را دنبال می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/457970" target="_blank">📅 17:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457969">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtJ_H3N6rpe3RYyd8nC_LCftF9Dk4voh9Md65Ufpec5t9EB2xOm-Enh8Lx8HovhGbZfM9Bfjg4MYxidRKoREpweNMBStanKsW2-E5JUtZdOpuXOtmmUtpfdzKQvVvmvlOdEKqtS07nfuIY4DI-SZwKEVJHPJ16ik3ojgfZJcAHYvQNAx2noSFVkseBN-Ugm8V5-rx4PLEreW9ecXabcwJq_9VH3GujP_nylpg7uu3pbnFi2g3vZKgANII8BOfkahuT9qKERS1R5P7fPjh9uwSqZt-HhiF88H4_Jbr1A9AArMI4RpSYVYdUQeFZvgrG6a9QHwiTY4p1VaP1ag4fN1Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور چین خواستار تشکیل کشور مستقل فلسطین شد
🔹
رئیس‌جمهور چین، در دیدار امروز با پادشاه اردن ملک عبدالله در پکن تاکید کرد که مسئله فلسطین یک مسئله محوری برای خاورمیانه است.
🔹
شی جین‌پینگ،در این دیدار خواستار «راه‌حل سیاسی، ازسرگیری مذاکرات صلح بین فلسطینی‌ها و اسرائیل و تحقق هرچه سریع‌تر تشکیل کشور مستقل فلسطین» شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/457969" target="_blank">📅 17:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457968">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1816d0d414.mp4?token=IpulSI9UnQOeNJF3Y8AneTw7H7Ehd_S8fHuxbkINrFJQTZ8iz9SyHLQ8UJ9TWjP201r19WyJZ6q-ER10eSbqsvhZQwyy8Jz7Ee98V43NR5LJ97F4wKosORqrurzDu46E73IB0dTQFJJ33G095d0_iJsaBPP0LapxUsfBchwxuSZF8MZQSyJPxP7c1X5uXq0Pv2IFN_HdouQqJR1mn-lnBmBiC50PNdsT4wyOOe7IKBtu2gF7IV77q0S3rPeHhAbWa-dELziu6YeINELsQtOfk2bTrv82iFu9lwPz-fuU_zWlO9bqeiLybF6EAFY5fxqy6qe5_xX5Up8_vOSuWZrDoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1816d0d414.mp4?token=IpulSI9UnQOeNJF3Y8AneTw7H7Ehd_S8fHuxbkINrFJQTZ8iz9SyHLQ8UJ9TWjP201r19WyJZ6q-ER10eSbqsvhZQwyy8Jz7Ee98V43NR5LJ97F4wKosORqrurzDu46E73IB0dTQFJJ33G095d0_iJsaBPP0LapxUsfBchwxuSZF8MZQSyJPxP7c1X5uXq0Pv2IFN_HdouQqJR1mn-lnBmBiC50PNdsT4wyOOe7IKBtu2gF7IV77q0S3rPeHhAbWa-dELziu6YeINELsQtOfk2bTrv82iFu9lwPz-fuU_zWlO9bqeiLybF6EAFY5fxqy6qe5_xX5Up8_vOSuWZrDoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم امام‌رضا(ع) برای میلاد پیامبر(ص) چراغانی شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/457968" target="_blank">📅 16:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457960">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XAQqa9hgVm3me4uCWDyv1Uku5PGYyTNDHUHu0Q1V3tWCmPWz_qFiz8SwfkQDe_NAozOt25BF7LQolOeNuetmwEr4qQU8g5C5bq_i1STILyEOCvh6VJ6oZkUTp9S1KUcjgwCbhbObR-uN5CslCC76z37pAGEAdeTBf5_p3gA4IncYHm_-Z1RsEqPJ8QMp-xpGH76RGSCEnF9PHMZCSQfVvS3TwEsr7TMpMwSzfhDlgwhNQi4l7YyQpN_oabVUEXcUpmNVDrUOJfz7LiocHDmN4rWcH-J7cD1zXjSx3ZfgvaHOhod287s2LpFrsStZOmGNfYlnvyXInbuFY51WmIvLcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z4L8MlhtboUyDo8zf8k1FIiCIUL3cVXuogTRJA4MDS93bYTb3jLltBjXw1or89joIKrdiUYwXi60mqduOQ_cnylr8n_gujM9zmOLCrof9qB6HAq4uyVOX06m5-bPoD6RPij36-hWvWaBhHn_FQL3QPIj_b1BTIUykBYuPh1Z0JzgJjq7qb_lIREv0sWRbt2KookzpeRXaNrh3WOweExhIGWrbVjb0Tl1IkY2qjywDDy554J4sd1XmGqTK-AtcxTS9fF7o4lr8Es__QKrW2lvqD_DdKspJDqiImhJGc1R6kId-RpfbVQ4lkFvs6YUjk84UIBPbzW3-Av4DvlIWaaLsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kRL5Y_r1IwS_bge-zfau3ZRBqluKhsZBFxD_IvLYw3GHx6mtDnlNXsvQ1ZC6ahxVzCNyl7hCe-V3XDdFayVzbxzpUX4vv9mePXN63cYdOufpRVNxFjSrMVhwQd2u1Yw2_lhlJQzHVSj4N9JXClWbj1Mxuly1j-7KEV8cQ_IpcdsxPNDHvnt2rFqptBeKXYKJJRPVOmhuGT4tRw4KghlCjBk2Ul5irQuDbC9XCCVZNzrEpro6eybKFMYEHVs_I5sDSPpdNZi_u4x_85JOvCa-TaHa2PZhZBxNfj2dCZfn0dJWes9zqTCUWT1CnaUFGhDA1Gplr9etu9EysZwGH8IYMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDbTJriCScx4Nlkx40-zswxCUUQzCJXMimWcESloPN3NLSt4yxqHVV8NICEoxBNQgMljY-Xt0lAzsKtF5Dm99gfLhO3i409ogINKk1fUEEBbAMQ1B96-1FHGHw6_Ycrrl_kVdsdnTCok6HgT7-kMCYyq7oO5eCQSeh-q8Ifhru2aCPF_kjvNb226lVINzn3WTzaY0d53eLbS-aF2FV_pCDBZOZA6G1rPbX5dLG0Gt4_oCEPZGAxYhJZ2BY3_yhzFzkKbpYTW8vhkIYUfJ_i_Ud5hx5Nq4vJGxCpL2GscD7MBjsL-JoRjnNOLv5fPf9A8bXHQ9EN49hqFeyBxGPtVmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q0N7c4qWL6l3EnCGpxnV5RXBvJ83xhR2Z4TVkkUrk1GYqSrduK94ADE2QbihEbejF4jistp0P7CgryV9cPk7fUB7DWIaFqFr4Xwr7ZMxOAlF5KKEnRMaInITc8yQVreIDSk4S8e-TM2ddLPHgw9uPNnGxK-Wd9xcnt-U8xPtlckmc2FoMOMOblwkA_0l6oECETp_nd1f4_SMQCWMCSQOyFXblqN9JQqHZ-cxQFODcd7qzl69rWjgOXWzsWfGmsIcYqg35aMJxpP8ZLomplM_8XC5R4aNBspI8x_5v9qnHB0N1_CKGdRMNs4GcXk8tpvt7m0B5Q96BMWstp3BIU1SpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EMC5TESIieftm5hIR9sGCb6bcvWBzZCOXsX8ovqfS89nCqMhL9ff2OEnH-8yWf3Fa-FyAqRxRY3uAUhjomXaLpS-qCcrwLzWuk2-1eAzVhqiFzny03lCoV4pciNlhFv5Hf2BjGYIGvwKi6Ll1awesFZ02_VJGr0ht86pCGavn2p404SB3NlBmm8PziDWSaqxqh0DBJfNkKQAkfweZCwyGpeOn9GtW-7T6x_87AxyRpXCCJGbee2_nPToBCyVij6KxjnihINwrHvLiYSVGPWeQAmbdmJr0D09znKajFDQDatE8OPDdEpt05dVykcQVEjPjugdkP8Z6GqzfnhIIRgAXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/trXvNaE1tjYyAo4IyoIMVNXGJTVrPvGg7-7Ra6x4HpxjfrvdAV6A10Hfrr8rbEuCiieoKosliEzozzuGshI7CFHNkWsVwTGR_ShGt52JMfMI9TPzqTM7HJZE2JtlEXD4GXrACkowvVtydtxW-7d1CbEqvAwe_doPYYwH2-loisS7ZIfpBahM9XoQecQFwgYE9sDtDiPl6CwV7xPJ4sMfXkT_xmf2vkrk3RxgemEAOJZtzXT47IPsGgcojpb858oCdxJ27qq5JWvBcEWOnm6edFbA1wo5RZhTJ1V0tPksq_Cewu_mJaudexObXtbDtdgu1YxYLkHBaPJGbbvWhT-jig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گرامیداشت روز پزشک در ارتش
عکس:
هادی ه‍یربدوش
@Farsna</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/457960" target="_blank">📅 16:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457959">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ارتش: آمادۀ کمک به دولت هستیم
🔹
بیانیۀ ارتش به‌مناسبت هفتۀ دولت: امسال در شرایطی هفتۀ دولت فرارسیده که ملت ایران در معرض آزمونی بزرگ و شرایطی متفاوت از گذشته قرار دارد.
🔹
شرایطی که اداره امور کشور، حفظ اتحاد و انسجام جامعه، تأمین نیازهای اساسی مردم و استمرار…</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/457959" target="_blank">📅 16:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457958">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBysBC5G9OLWx14o1RwEFcPENzvkaqMuolydbC18g1igL7gW0igS0gazIuuaqFCmtwOmli4VY3DjZHI3caGSekfjcey_ARPJGgFjfr-q_XDf2E8jOWkllHuMSb_dX0D0-YJkl3pGIbhK3ZlXsDaAxcpxbxNi8YqeRuiNOE1MxNJrzZPWyObXlsLx9lkFbD2QXAWLEjUCcKRtPTTIHrhZupaozWkaD1PuSCOQ3qI-xoDL0RRNZR1QENWumHFukfHMmFfr-X7fdDFb7H593CSC7PrQbMooKKj6mlr2OkiB9zsqYTs4C96XFhN6ZVnD9pzDCLt442thgV9cGoRYBETNEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۲۴ هزار لیتر سوخت قاچاق در بندرعباس
🔹
دریابانی بندرعباس: درپی توقیف یک شناور در سواحل شهرستان، بیش‌از ۱۲ هزار لیتر گازوئیل قاچاق به‌ارزش ۲.۴ میلیارد تومان کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/457958" target="_blank">📅 16:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457957">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGg3pgkHuy8DvdyNoGw7SrwAKECj41Cx90Megawv3_yB1PRVglkUxYWx3UDNQVAL4AeJ-BuuJLQA-FbOnw0ky8-lIiwDQ7LUGAGMJv8f9FHLXSFdb3bRyQqa08aVGNQOvpBGNYuI0NXxEm04eNtIrUz87M8H2efZVDoFTNWozlLP8FR0stl-koOuuAlIZE_NdoFF19BDvBKvti6pE8p-5SQ-atJcq1yyb3Vf-67qyp67-5euP6t7GcLSrO9GHQ535t2UetslKvhE5sDi0YIT7mwx5YdmlYi7_gfDr1J5LBV8f6OIUJwFYrqm_TTz0tCSDkQZffcvV8LnfA_eT6ASjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیدین: روش ما مشخص است؛ فوتبال شرافتمندانه
امیر سیدین، نماینده تام‌الاختیار مدیرعامل شرکت معدنی و صنعتی چادرملو در باشگاه، در آستانه دیدار چادرملو مقابل گل‌گهر، با تمجید از عملکرد بازیکنان و کادر فنی در فصل گذشته، بر تداوم مسیر موفقیت این تیم تأکید کرد.
سیدین با بیان اینکه چادرملو فصل گذشته شایستگی حضور در رقابت‌های آسیایی را در زمین فوتبال به دست آورده بود، گفت: «برای ما بازیکنان و کادر فنی چادرملو برنده‌اند» و مجموعه مدیریتی باشگاه با تمام توان از تیم و حقوق باشگاه و هواداران حمایت خواهد کرد.
وی همچنین تأکید کرد: «روش ما مشخص است؛ بازی شرافتمندانه و تلاش برای نتیجه گرفتن در زمین فوتبال.»
نماینده تام‌الاختیار مدیرعامل چادرملو ابراز امیدواری کرد این تیم با حفظ انگیزه و تمرکز فصل گذشته، بار دیگر شایستگی‌های خود را اثبات کرده و در پایان فصل مردم اردکان و استان یزد را خوشحال کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/457957" target="_blank">📅 16:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457956">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cATB54xK-q3yEny7LJGwUFRU-ADEtFLjEBXxCdWHWSlruvFwG1qcItmLup_qgLZO6Pz-NSeZ0JGK-zgKv1DAjHHL8Nsy37zWvBEPmrbdVlNJujZ7zppPRU_SSPeWaMGTJiIgw6csBoZ1aavNKR4icUPK3d8yslPkkLb3r4hVx34Go7mATsMe_WdXK45f66jENRKGqjYjGea2D-LkolBXhhjUhZTQf7IPZb6Zcxv97TRnOdnxmAlu8K5YNK-q9UR5T6ZdRudFemfiFnfK_Spy8S_QYVCqLFYhbiLGY4K0NTKaqlsNwawz8SWMbgHwz6iPhG1aZdZXCeaP0e2q_2ja1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
آخرین فرصت ثبت‌نام در دوره تخصصی «هوش مصنوعی در روابط عمومی و رسانه»
📝
فقط تا ۳ شهریور با تخفیف ویژه ثبت‌نام کنید:
📝
دوره حضوری با ۲۵٪ تخفیف
دوره آنلاین با ۱۵٪ تخفیف
۲۴ ساعت آموزش تخصصی، کاربردی و پروژه‌محور؛ ویژه مدیران و کارشناسان روابط عمومی، رسانه و ارتباطات.
🔹
ظرفیت محدود است؛ فرصت را از دست ندهید.
🖼
مرکز آموزش‌های آزاد خبرگزاری فارس
ثبت‌نام دوره حضوری
ثبت‌نام دوره آنلاین</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/457956" target="_blank">📅 16:22 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
