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
<img src="https://cdn1.telesco.pe/file/eTxF0iM9X7iD5Yfw0qVF9p0xii-v7wkijDnTiHpR12OdQetdbRTmeVzYvcJ4VrhMthRRMuspNAvyZ64SxOd9J6q2J24IvJ0zS14FRgiY6u0QMQ_B0pyU4rEDgtgkky33_fKRpU1u9fArPKktCl28gemVsV3QcpDKzDNL0t_ZS8E10pX76WZwo12EKHKhfR-ZMz2q_dAMZxcHzHyyl0gsfQfW47VNNP3eqVQMMHkAnKMWlNs5hJzcOUm9M023JBC_L7NCQNTlQk3nh673FGga6tR7FQKmYLp6asD0VsauUM_-136Oz1rcO16t5T1sEKeCIMn5lA_lUVEXhBuC4PRjlg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.8K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 01:42:52</div>
<hr>

<div class="tg-post" id="msg-2374">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U2w7Bdq7y8j_L_v1Tgc8OEp5P2iXY7JL6TtoSHNM8DyozfrVhuJYPMG9HlxSPbFC7_PO0qoFajIhe7TbqiWrB8a7FqELe8DH3RSUyzEzEZjEuAAAezmUTdz5CQin-4ypq_AsP-x1zmlZ4yL4xBvus1QEZFEH3EImRA5BYHVHkFxJwk1oaTsRVt1dmy25r7rNCbbgK-V0CTr2GB-f6YWDRBAHcUSHsgXiFqhCQmyEMpJ3IMXPydW2I5xNPMQq2zD9xVl-Xf0ddIGx_JizllakYsTjpdRhjfJ8gX23jX-0h113HbusSqc6ZTqyhz7gF7Yn-ztsymfeCsmW8vczseH0Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸۵ روز از قطع سراسری اینترنت در ایران گذشت!
قطع اینترنت در ایران، یک پروژه چندوجهی است. قطع شده تا بین "هواداران پهلوی" و "پهلوی" فاصله ایجاد شود و همزمان عده‌ای بتوانند روایت جعلی بسازند.
صدبار دیگر ایران بمباران شود، نظام با بمباران تغییر نمی‌کند؛ چیزی که جمهوری اسلامی را ساقط می‌کند، آن مردمی هستند که شعار دادند "این آخرین نبرده، پهلوی برمی‌گرده" ...
با تمام دشمنی‌ها، سرنوشت محتوم ایران محقق خواهد شد.
©
AmirHadiAnvari
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/ircfspace/2374" target="_blank">📅 08:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2373">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v8tcbYE9xxtU4_8f9esCWPwh5vi25rH_f65D7L8WvXeZuFbnNPfxbIXbYdct7mE2o-i2Om0ExbVvKIbzZM5mnyO1MdhGkVGBEpyN85Y3bSSyHf901GUWnmyVgsGqE1g7CNKfhaFRqOUFtggeEeOo0U6NKGdOh9SJvSVll9brY41k-2bcHi8lkcj49RV7iwQgJ9HErZhWvnH8tcQrSGtXJdvJU1ZJCzEszeVWRyix_m3nBIttBDtCEVVLMvSZgsRE9qGr1FAhbilr75JlfVb2IXCeQZ7utGh98EFhgZwPsT86t_6jcV3G7ljSHv7BlMxdPpSBA9R049zhPmBOg6bIkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طی یک عملیات بین‌المللی، سرویس VPN موسوم به First VPN که توسط مجرمان سایبری، گروه‌های باج‌افزاری و هکرها استفاده میشد، از کار افتاده. در این عملیات بیش از ۳۳ سرور توقیف شده، دامنه‌ها و سرویس‌های Onion بسته شدن و یک مظنون در اوکراین هم بازجویی شده.
مقامات میگن این VPN در تقریباً تمام پرونده‌های بزرگ سایبری یوروپل دیده شده بود و برخلاف ادعای بدون لاگ بودن، نیروهای امنیتی به دیتابیس و اطلاعات کاربرانش دسترسی پیدا کردن و هزاران کاربر شناسایی شدن.
©
eurojust
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/ircfspace/2373" target="_blank">📅 08:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2372">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">جمعی از سازمان‌های مردم‌نهاد و فعالان حوزه حقوق کودک، با انتشار بیانیه‌ای نسبت به تداوم محدودسازی و طبقاتی‌سازی اینترنت در ایران هشدار دادند و آن را عاملی در تشدید نابرابری آموزشی و اجتماعی، به‌ویژه برای کودکان و نوجوانان دانستند.
در این بیانیه که به امضای ۱۹ نهاد رسیده، تاکید شده دسترسی آزاد و برابر به اینترنت، بخشی از حقوق بنیادین شهروندان، به‌ویژه در حوزه آموزش، دسترسی به اطلاعات و رشد فردی است. این بیانیه، با اشاره به تعهدات بین‌المللی ایران از جمله پیمان‌نامه حقوق کودک، محدودسازی اینترنت را در تضاد با این تعهدات دانسته و همچنین با اشاره به نقش اینترنت در آموزش و معیشت خانوارها، تاکید می‌کند که اختلال در دسترسی بر شرایط اقتصادی و امنیت روانی خانواده‌ها نیز اثرگذار است.
©
hra_news
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/ircfspace/2372" target="_blank">📅 19:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2371">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r3KPPRbd926M0eT1rf1v1QPQmBl4apK7BNqDPvxHmB9GjlIWrrCec8ifSXZppqTr_27Vw7GqrhJmCfY-CBOv8wYF_-XvLsH4soILneBNCJIkotXdM47ngJ4qVwJY1TND-AeR_TyGJuZzfPH9Z_EoqLZqIvC07RldthwZdQFvoGZL6Ek6a29C4EiGf4i3bxrRrsfYmTpR1rcOrt9BOd1nLEMvFcRJl_DPejgbvxQ9vHzCZxXBoHWq2_keaDImky9Q-BqdPcjGwUcfgjwAQ4nij_uh6kSwBra0TTDQBBf5zvJk-HPuAYmI_93zLKjFdR_pBSa-tgHIQA71issY8s9WgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع سراسری اینترنت در ایران با ورود به روز هشتاد و چهارم، از ۲ هزار ساعت عبور کرد. هر ساعتی که می‌گذرد، شکاف‌های اجتماعی و اقتصادی عمیق‌تر می‌شوند؛ به‌طوری‌که هرگونه ارتباط با دنیای خارج به جایگاه، تبعیت و امتیاز وابسته شده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/ircfspace/2371" target="_blank">📅 19:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2370">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خیلی راحت آمارسازی میکنن و میگن ۹۰ درصد مردم با قطع اینترنت مشکلی ندارن؛ به همون راحتی که احتمالا قراره تعداد ثبت‌نامی‌های سامانه
#جانفدا
از کل جمعیت ایران بیشتر بشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2370" target="_blank">📅 20:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2369">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کسانی که قبلاً کانفیگ می‌خریدن، الان ترجیح میدن دیگه نخرن، دلیلش هم تکراری شدن خبرهاست. دنبال کردن مجازی دیگه اون‌قدر براشون ارزش نداره که بخوان بابت هر گیگش خدا تومن پول بدن.
از اون طرف، کسایی هم که سیم‌کارت پرو گرفتن، خیلی‌هاشون توی کسب‌وکار خودشون موندن. چون درسته اونها اینترنت دارن، ولی دیگه کسی نیست که بخواد تبلیغشون رو بخونه. تقریبا اون چرخه‌ای که باید بین محتوا، دیده شدن و فروش می‌چرخید، به بن بست خورده و کل سیستم رو از کار انداخته.
©
NR2OH
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2369" target="_blank">📅 20:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2368">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QgHjEUiv1ylJuRHOAOlsL0LePINAnTFjKJFn3AI9E13exHbdqxFkNG4QfjJa-wAKbx263-1212UlcBSu-xIjwlhY9VAE5wGGoinmPC8k8nbEfHGMesShMrU4xsbG4GZ11cjy_8axUqhmnku3rubtDUbzG-sZt0O4dD2Vh6aZX1jHi_aYlbchxRUMBoq9vLUgCJljsbYbTUSwUXd0WmY-YN365zvAZEL1tSUY6VrTrZ9gEws09ji4bLBEuIzgVNl6AwF6EY_7Z-bI-VWMcfqd1qiGaz9_7TvXHqf1cLS1qKcJArhUXpip7iXk6W2_-uoOlc4LxQU_9iX08PT9wn3Ipw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا فرزانگان، اقتصاددان حوزه خاورمیانه در دانشگاه فیلیپس ماربورگ آلمان، گفته است حدود ۱۰ میلیون شغل در ایران به‌طور مستقیم یا غیرمستقیم به اقتصاد دیجیتال وابسته هستند.
او به وال‌استریت ژورنال گفته محدودیت گسترده اینترنت باعث کاهش بهره‌وری، تضعیف اعتماد کسب‌وکارها و افزایش نابرابری می‌شود؛ زیرا در چنین شرایطی تنها کاربران ثروتمندتر یا افرادی که به ارتباطات بهتر دسترسی دارند، می‌توانند اتصال پایدار و قابل اتکا داشته باشند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/ircfspace/2368" target="_blank">📅 20:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2367">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qLpcq8ToCJgn4n5Kmb1J4I8C1alLfPtEBWhh7uXFdgrWrhDEZ0TDa81iASlpkvbz5TaSfsHnOnsl_35g1fo2ePzlL9v25EkLQrzWwgAYvRhco48f-gepbxx9Lu7nvYfDz3Jj33kTeLdvAU6Mnvj8iyAju7nEueX8J4bPAIVIrmHasoPlK-RguzzA7065__5hBV7lCcR-Gs7JOeIiutKe_LpSBWO0Dhu8imZ0O-HIVvyqkl28wKYrhE-LiZmX03pc8fmCHpJbITccVsxm6OcTiX0ZpDgFBuKLRXx0T-uFgXFwQfaicrvDDAeNbhKAOAeTq1NuxSWXSlvoUzBf16al2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زارع‌پور، وزیر قطع‌ارتباطات دولت قبل گفته "جمع‌بندی رئیسی این بود که اینترنت به خاطر هیچ‌چیز نباید قطع بشه"، ولی یادش رفته که رئیسی با ۶ کلاس سواد حتی جمع و تفریقشم افتضاح بود.
جهت یادآوری واسه
#قوه_عاقله
، اینستاگرام و واتس‌اپ توی دولت سیزدهم فیلتر شدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/ircfspace/2367" target="_blank">📅 20:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2366">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یزدی‌خواه، نماینده طویله مجلس گفته "در شرایط فعلی تصمیمی برای بازگشایی اینترنت جهانی وجود ندارد" و "با قطع اینترنت، کسب‌وکارهای مردم از جهت ارتباطات بانکی، خرید و فروش و بسیاری از سایت‌ها همچنان در حال خدمت‌رسانی هستند و مردم مشکل عمده‌ای ندارند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/ircfspace/2366" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2365">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C2hI_Ij_ARP0DOkiLpg0efCg-TngkbgSXt37PpT-e8ctnBss-YH3Cq9qirYM1UvQmGWNGZ5KTt5AJ_65icvOrCNy02dqmeUEssaTSSRPdmlMTfaXZ8WjWZ1o3_IHhk0Mfq2RWBLqV_TOGk-2_HQ0UfsRH6iZ6QDH_3j_NNTPn2aS4AMzh24WFRma_UEyLT5h8VyzCmFyeluGIx0i1LRjV2ZCz-se3rVgxHqRHl-LnjC-fsTeSgjVPnNDKVltvdwegoSncNkXl8O_E74zpMFMSgdofOWOmjGRMwRkAnRw-e9mECn7PZXvdpD6pI0lZXRX1OvKDjVisEsXEUXX5JO6DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه عاقله در همراهی با سایر قوا، قطع سراسری اینترنت در ایران رو به روز هشتاد و سوم کشوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2365" target="_blank">📅 08:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2364">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گیت‌هاب گفته دستگاه یکی از کارمنداش از طریق یک افزونه آلوده VS Code هک شده و مهاجم تونسته به تعدادی از ریپازیتوری‌های داخلی خود GitHub دسترسی پیدا کنه و اطلاعاتشون رو خارج کنه.
فعلاً میگن شواهدی از دسترسی به ریپوهای کاربران یا داده‌های مشتری‌ها پیدا نکردن و موضوع فقط مربوط به ریپوهای داخلی خود گیت‌هابه. البته دارن لاگ‌ها و میزان دسترسی مهاجم رو بررسی می‌کنن و گفتن بعد از کامل شدن تحقیقات، گزارش کامل منتشر میشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/ircfspace/2364" target="_blank">📅 08:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2363">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">عضو هیأت رئیسه مجلس: تصمیمات مربوط به اتصال اینترنت فقط با امضای رئیس‌جمهور انجام می‌شود؛ تشکیل ستادها نمایشی است.
این هم خبری دیگر درباره اینکه مسعود پزشکیان نه‌تنها مخالف قطع اینترنت نیست، بلکه در ساختار سرکوب و محدودسازی اینترنت کاملاً همراه و همسو با حاکمیت عمل می‌کند؛ تمام نمایش‌های رسانه‌ای درباره «بی‌اختیاری دولت» فقط برای فریب افکار عمومی بود.
©
alirezaer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2363" target="_blank">📅 08:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2362">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SgqCYN-3_FrLqoU5A95HVQePdkz93ufzCob86dyPD6Nbo1RWwPt2QopgVGVh4bDBwnY7sV_OogPPyyakP48610nujoRXZSloQvSPsymIAeTMYQ7lEaCDjhUYsAZ6XhdXSImKZ8vFz1bkH96Iz9NtSgd5jcS5SeFLVNW0V9tq2ivev-RW0HKAxkZivQST0oaoeGk6Eb-iEG-JeWZmTp0JoOtb44dDeTbubWFrKbO7Zkwdn_z970Bupl7i_Pd35TSlmiz-bezHba6nrs3ZIaYk7QJVt9Rc30CDq-BYyC1C_vtNcNVcdEdHe5EudkMJzKyJw9LUy4u6rR6tKIyxJf5WAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار نشون میده در ۳ ماه گذشته یک پاکسازی طبقاتی دیجیتال در ایران رخ داده. در این مدت سهم اندروید از ترافیک اینترنت ۲۵٪ افت و آیفون ۱۸۰٪ رشد داشته. این به معنی خروج میلیون‌ها کاربر طبقه متوسط و پایین از فضای آنلاینه. اونی که آیفون داره (احتمالا) از پس هزینه کانفیگ یا اینترنت پرو برمیاد، اونی که نداره، اونقدر دغدغه مالی مختلف داره که عطای اینترنت رو به لقاش می‌بخشه.
©
arashzd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2362" target="_blank">📅 08:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2361">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FhNBmz3I7gjfearaA0bhXphB3GAYVSuEd2IwHtRJgLrtbGVGLoYhOxAW0ut_pVjAX_nRfz0jaGllWIeCukc-2XFdM46NG86ao3BdgoARvkQz7OH_lGz50gtTTgFAGF1FwfkkB91fDOptFejUfIJO8YiGPvvnP6qCGX0sim5jVkkmgSOWjTIO7Nh8YqOyTNF5ydeF_zYH_lGcTd73S1Tos2QB_rJ9XmkEprkvSG1dcH7BqORBLWw2i18lyo6_ALoz0wYv2gt1YWb9-mrMOPdwOdLIwt-fvv8eLZix-gZt5aiwFN7wQFIDE_YcKlnrC1nvPzpVzQ2T4Pt05xUmk_cp_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتاد و دومین روز از قطع سراسری اینترنت!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2361" target="_blank">📅 09:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2360">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">قطع اینترنت به خاطر تأمین امنیت، یک دروغ بزرگ است
گفته شده قطع اینترنت به خاطر تأمین امنیت زیرساختی، نرم‌افزاری و سخت‌افزاری است تا کمتر مورد حمله‌های سایبری قرار بگیریم، در حالی که این یک دروغ بزرگ است. حمله‌های سایبری و ناامنی زیرساخت هیچ ارتباطی به قطع اینترنت ندارد. متخصصان به این‌گونه دلیل‌تراشی‌ها پوزخند می‌زنند. البته نه به این معنا که زیرساخت مخابراتی ما یا زیرساخت شبکه ملی اطلاعات ما در حال حاضر امن است؛ نه، ناامنی وجود دارد، اما قطع اینترنت کمکی به تأمین امنیت زیرساخت نمی‌کند، بلکه لطمه بسیار جدی‌تری هم به امنیت زیرساخت می‌زند.
در همین مدت دو ماه و نیم گذشته ده‌ها آپدیت امنیتی برای باگ‌های «زیرو دی» یا اصطلاحاً باگ‌های روز صفر داده شده است. این‌ها باگ‌هایی هستند که می‌توانند دسترسی بسیار بالایی برای هکرها ایجاد کنند؛ روی گوشی‌های مردم، روی مودم‌ها، روی شبکه‌های صنعتی داخلی. این‌ها هیچ‌کدام آپدیت‌ها را نگرفته‌اند. آپدیت‌های ضروری‌ای که حتی یک روز به تعویق انداختنشان گاهی باعث ایجاد ناامنی می‌شود، الان بیشتر از دو ماه و نیم است که دریافت نشده‌اند و ما با یک بمب ساعتی در ناامنی زیرساخت شبکه کشور مواجهیم.
من فکر می‌کنم وقتی بحث امنیت مطرح می‌شود، بیشتر از اینکه منظور امنیت شبکه و زیرساخت باشد، منظورشان کنترل افکار عمومی و جریان آزاد اطلاعات است. اگر با این چارچوب امنیت را فهم کنیم، بنظر می‌رسد حق با این آقایان است؛ قطع اینترنت قطعاً باعث جلوگیری از جریان آزاد اطلاعات می‌شود. دلیل اینترنت پرو هم اتفاقاً همین است. اینترنت پرو نهایتاً شاید به یک یا دو میلیون نفر ارائه شود. یک یا دو میلیون نفر با ۵۰ یا ۶۰ میلیون کاربر فعال ایرانی خیلی متفاوت است و باعث می‌شود جلوی جریان آزاد اطلاعات گرفته شود و در واقع کنترل افکار عمومی و کنترل جامعه راحت‌تر شود.
چطور اینستاگرام یک پلتفرم آمریکایی است و ممکن است لوکیشن و اطلاعات مردم را در اختیار مثلاً نهادهای امنیتی آمریکا بگذارد، اما سیستم‌عامل اندروید که متعلق به گوگل است، نمی‌تواند چنین کاری کند؟ اساساً منطقی که مطرح شده، پر از اشکال است. وقتی شما اینترنت را قطع می‌کنید، عملاً یعنی تمام زیرساخت‌های رشد و توسعه یک جامعه را متوقف می‌کنید. به یک معنا، ما با این مسیر داریم گام‌به‌گام به عصر حجری نزدیک می‌شویم که در آن از فناوری اثری نبوده.
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2360" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2359">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">امروز هشتاد و یکمین روزیه که اینترنت ایران بصورت سراسری قطع شده، ولی پروپاگاندای حکومت بدون لگ داره کار می‌کنه.
امروز هشتاد و یکمین روزیه که جمهوری اسلامی داره
#روز_ارتباطات
رو با قطع اینترنت جشن می‌گیره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/ircfspace/2359" target="_blank">📅 08:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2358">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nOnG21eFibMnnvbZQIWxseDUmgmpRTVaYiKOsrsGYlty7mH5mLnusbuTxKd0YIsToLdb8_bRxRsBG59pDIuzL5mV2d-W16EQaWVG9vNYTWxqby8Wg6vNDGz5XYCePo0i939scAl-q39cpP640srfxOEZY1IyfDcOORZnnx2LqTuh5YtNopuKscE2dD8WxsGrWj6z75tHFpnJT6h7VWSi2QMtKdzJHUgyuKFAsvqQH8kIkHI6zLkMcS5Es5dR036SNdpBzkMUawlo7YuwVDNfuhVAq9LCmjQuWCr3daqke9p0aEcxok13PmId97BUyZBpO0qUihblAI5pHHMdmNSViw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در بروزرسانی جدید از اپ Network Checker برای اندروید، ویندوز و لینوکس، قابلیت اسکنر آیپی Akamai (جهت استفاده در اپ
#شیروخورشید
) اضافه شده.
👉
github.com/mirarr-app/network-checker/releases/latest
💡
t.me/PersianGithubMirror/5227
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2358" target="_blank">📅 08:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2357">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k-1lmC6CEmxUAzYcOcwPZeXlhfOmLyk1_79lySowKjZD_bdRZab9Fw9I_QXbmyZt1ahy-uxIwywET7RPT0VWAy2QdkSXG9wPUj5nB0_VzwEgq0Rr468shyzXn1hA2Ta0GiZpYrVF6pGjHh1RWkBkaE4vQ0XMOZpHtYIE68_a09tYwfjgTHxT-Ev_vAH8Xxf7fAu_HjI7VtD25-sa3q7Qc3W9lZyn5c9earj9Tdx63T-xG5p9f1cN8mbcs13iX1x5554-YnUjPaVRzJQp_K7ZLeafj3UpfnVtqE5QkVUtHgVjMNsi-ngcvQHxHoEFfXwKRAIm9WtkT_c6CaspqflPGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ NexaTunnel یک کلاینت رایگان برای مدیریت تانل‌های StormDNS در iOS هست، که به شما اجازه میده کانفیگ‌های مختلف رو وارد و مدیریت کنین، وضعیت اتصال و ترافیک رو بصورت زنده ببینین، DNS Resolverها رو تست کنین و خیلی راحت بین پروفایل‌های مختلف سوییچ کنین.
این برنامه با رابط کاربری ساده طراحی شده تا بتونین وضعیت تانل، سرعت دانلود و آپلود، پینگ، IP عمومی و سلامت اتصال رو بطور لحظه‌ای بررسی کنین و مدیریت بهتری روی اتصال‌هاتون داشته باشین.
👉
apps.apple.com/us/app/nexatunnel/id6766783641
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2357" target="_blank">📅 08:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2355">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">توصیه اکید من اینه که برای وصل شدن به اینترنت سعی نکنید از سرویسهای ایرانی (خصوصا سرویسهای متصل به نهادهای امنیتی) که شمارو قبلا احراز هویت هم کردن، سو استفاده کنید.
به هیچ وجه حتی برای امتحان کردن هم ارزش ریسک کردن نداره. و به هیچ وجه هم روشهای مربوطه رو معرفی یا پروموت نکنید! اگر کردید بهتره همین الان پاکش کنید. از سر دلسوزی میگم، بچه‌هایی که از چندسال پیش در ایکس فعال بودن میدونن دارم در مورد چی حرف میزنم.
©
aleskxyz
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2355" target="_blank">📅 20:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2354">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SpiYvQDQ8olLJ1hACXljhGIFzAwnh43cmosLeLOCktUlvZE9-MydUuH24okPdpQ8ott_rMnNW7C5KR9p-RV-ZwGMZJcMlTH6l8LaQ_TcKvc72MCgQSlkS8rQAV3z7Jkn8xi9mAoT4OVghqXUbFYLGWyLptqlBhELED3T10-4oi94BF2TVLJMhC6zmw7VcQsFQIGXt57tVvgDvGuPetLl0-HWzoxYzc1KzD2NnJYHNsuDEg2qlXgop-IbQQJkvT8yqLIWmdZZHQrfzb9eJbFhgOJSfb4yYuMuCa4X2hsz_uYdvea7_TrQqiNNxKxJ6VWn1Lbt7QCvwvPlIVT2WkFz6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما در انجمن تجارت الکترونیک تهران تجربه واقعی کسب‌وکارها در زمان اختلالات ارتباطی را مستند کردیم. از میان ۹۴۴ کسب‌وکاری که به نظرسنجی پاسخ دادند، بیش از ۸۰٪ اعلام کردند در زمان قطعی اینترنت، فروششان بیش از ۵۰٪ افت کرده است.
اما یک نکته مهم‌تر در داده‌ها وجود دارد: حدود ۳۳٪ کسب‌وکارها گفته‌اند در زمان بحران، «پیامک» مهم‌ترین ابزار ارتباط با مشتری برای ادامه فعالیت آنهاست. پیامک در زمان اختلال اینترنت، یکی از آخرین مسیرهای باقیمانده برای حفظ ارتباط، اطلاع‌رسانی، پشتیبانی و فروش است.
حالا تصور کنید پیامک هم قطع شود. بیش از نیمی از کسب‌وکارها گفته‌اند با قطعی پیامک، افت فروش جدی (بیش از ۳۰ درصد) خواهند داشت. پیامک بخشی از زیرساخت تداوم اقتصاد دیجیتال است؛ نه یک سرویس فرعی.
©
NimaQazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2354" target="_blank">📅 20:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2353">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h8ixE5b9IidU34DLRdmu6-3XPsd4iFwfOydxx54Tkudoza_YvXDIF67n9p6SK4fPg1BiZZLaQ-ztqRzpHyVpjeWBvSPlNXrBX55yo-5KlaLKdHiP-yc3R8kt4nwb_IRFC1Z9DF55SqOxaHwOhmC9CUJTDRFiKGrEN8RwcAJWdvMGoZPS40xCn2RmpdyDYCcMQo32dM8qwnWMiVmxOv6mIZ1Mjmx6VIH6rFUaHcwyXdjqTWl-alPb2Js-OMlckajY8at37rSmgWzDfna1SAEIn9YsC0YG_ro6p7x6ofJOyU7QnZm5OeNAj-6q2xpT2033r2ZCCutaeOstR0DYegP1MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید به افتخار وزارت قطع‌ارتباطات ایستاده
شاشید
!
آیندگان در کتب درسی از تمامی دست‌اندرکاران فیلترینگ و وزارتخونه‌ای که اسمش ارتباطات بود اما ۸۰ روز متولی قطع‌ارتباطات شدن، بعنوان
#قصاب_اینترنت
یاد خواهند کرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2353" target="_blank">📅 16:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2352">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K1HY6xCbKftNImqqQ8EUQDTEZ_scb-37v7kBDH0ik2rhQxpNIpo7etujv1qTQPA8gMZ1oz3rIIjxiGfKc6qDH-vY7NYyB0FE_gaXXDkavm1EfK5NprADiXtiFvgNbWV-P-EAIdOl_ISO5NpTeATqJ31KDApnOkv5BRLe_5AkNrvSv2YUQNnXgJ6HeXSZdZQf-TELthcbGWmXYXGNMRslg6ejUeLmAguAfu66BhPsf84D39Tfegm4LquCN5foX8U-_tVe2MVor3R-hhsix4uu_B0YtFUrRL_hEhcoCLcfWHYxPcdp7lB3EiXd0O9y6hIX0NGVwjnxvIhcn0aUGDsA6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستار هاشمی از پایداری شبکه ملی اطلاعات در دوران جنگ تمجید کرد و گفت: شبکه ملی اطلاعات کارکردهای متفاوتی دارد. در شرایط جنگ شاهد پایداری شبکه داخلی کشور بودیم تا ارتباط بین مردم قطع نشود و خدمات مورد نیاز مردم ارائه شود.
وزیر ارتباطات افزود: در دولت چهاردهم نشان دادیم شبکه ملی اطلاعات ورای یک شعار در میدان عمل کار می‌کند. این اتفاق بی‌نظیر و شاید در دنیا کم‌نظیر است. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2352" target="_blank">📅 16:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2351">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DB9P-rhR5Dn7txHQGK8pW7AuZTQ4uLRxBagUuyYoz0dVHruROzxHqw94fdO7FdBvLJI5xD3VKKxCpyID0RjhBdyQtzS0fF3EoWvd6Xg_-2ooAhOJGGh_Rw-aSZybnq8NCNr0qCQysNx3dlhwfDvfsspn1HpuNjzKDxnhpc3tmplQA9g-DO4aLuuJWsMkhXNzUCNvoWS04C1pIs4uSJdZsRunhH9DsAg2zxwRaY_jssRGqJ--cdjdj7CiMRnUz_z9liPexnQNfovw6XRkjSeZnHuanjybpb7iDELiJhxLE4hj8EweYDR-0Edlphjew8Vnf0e3sSlicRrqHJ3I0O8ufg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ اندروید
#چشم_عقاب
نه فقط یه خبرخوان، بلکه یه راه آفلاین برای دسترسی آزاد به اطلاعاته، که بدون اینترنت، بدون VPN و حتی بدون داشتن مجوز اینترنت روی گوشی، خبرها و اطلاعات رو مستقیما از ماهواره روی دستگاه شما میاره.
کافیه کانالش رو روی فرکانس 10762/27500V ماهواره ترکمن‌عالم باز کنین و دوربین گوشی رو سمت کدهای QR که روی صفحه نمایش داده میشن بگیرید، تا اپ در چند ثانیه اطلاعات رو بخونه و روی گوشی ذخیره کنه.
اپ فقط به دوربین دسترسی داره تا QR Codeها رو اسکن کنه و هیچ عکس یا ویدئویی ذخیره یا ارسال نمی‌کنه. تمام محتواهایی که دریافت می‌کنین، قبل از پخش با امضای رمزنگاری‌شده Ed25519 تأیید میشن تا اپ فقط اطلاعات واقعی و معتبر رو قبول کنه.
👉
play.google.com/store/apps/details?id=com.filtershekanha.cheshmoghab
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/ircfspace/2351" target="_blank">📅 10:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2350">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">باورم نمیشه قطع اینترنت به ۸۰ روز رسیده!
وقتی حکومتی برای حفظ خودش حاضر میشه یک کشور رو وارد خاموشی دیجیتال کنه، یعنی مردم هیچ اولویتی براش ندارن؛ وگرنه امروز وضعیت اینترنت، اقتصاد، مهاجرت، ناامیدی و زندگی روزمره‌ی مردم این نبود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2350" target="_blank">📅 09:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2349">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NZWRR5zyUsd5nMwBdTUH_4jpm0ivGQHOwGmMxlba-3IpuLMIKSo5i_a029GuyvqFnHejtu6lLudg0ornHCBgR5kDWhuStbgKO2_Q6DiRkk4YnU3yDr2ZEdNEz9t9OIW0AxjdJtE7BuO9YYipggnpuphX1Ud_pd1V_V8ovtG_CMrGsX2eV9SOAnz4UmmejNuzU6zaI6GopDBNU0mL9DLkQOrCArzZ4QPYc6wVhZ6U-so1TwvhonvySEut_F4xVoTwD5eb4FWAEOKC53Y5b3j-Zx2PUbNJUNx1aMNB-zNufHK1B8n_Bkyv3MuQjhkLk9XodNpyuJULysl0jepwq9W5FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان بعد از ۷۹ روز قطع سراسری اینترنت در ایران، روز جهانی ارتباطات رو تبریک گفت!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2349" target="_blank">📅 21:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2348">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l974CtXMWGEOLG_5fE8oJ3uSt04QWfvib0fy8pmjvQFZhkgfTt03uZ4N6B58aUTlf3VVyZIC3S2HVbJ3Un9BTR8LN5PS_Shk8VntVjV0iMw0Gin054rsAjl6ANq0ivORmzN0I6V_vAOKMCB81zwOTFuhVb8y6xqJrGJkMwXbWx4lx-fyxpNNRUmuLBGpGxtIWo469QGJgLD1ZS_HE1oqrpxBAAVTvYQyiHHW-YifGyqNcVw1tK7Zc0FXoCFLElclpo2nh-tRsiGzS5FlAAZjdJQiN9jq0-eknSfsK1UYA7OTStF6YjVuUD7f1gh0Z_nrXnyCUB30ZrQrgBaSBF3r0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیمکارت‌های بدون فیلتر، حفره‌ی جاسوسی برای مسئولان!
در رابطه با قطع سراسری اینترنت به بهانه امنیت و اعطای
#سیمکارت_سفید
، سیتنا در مطلبی نوشته: طبق منطق فنی، وقتی با سیمکارت سفید و بدون فیلترشکن به اینستاگرام، واتس‌اپ یا سایر پلتفرم‌های خارجی وصل می‌شوید، هیچ لایه واسطه‌ای برای مخفی‌سازی وجود ندارد. یعنی دقیقاً در همان لحظه‌ای که یک مقام مسئول درحال چک کردن دایرکت‌های خود است، اپلیکیشن‌ها لوکیشن دقیق او را با کمترین خطا رصد می‌کنند. اگر نفوذ و ردیابی، خط قرمز امنیت ملی است، پس چطور با دسترسی‌های ویژه، عملاً موقعیت مکانی لحظه‌به‌لحظه خود را تقدیم سرورهای خارجی می‌کنند؟
تناقض وقتی اوج می‌گیرد که می‌بینیم مردم عادی برای اتصال به همان شبکه‌ها، مجبورند از کانفیگ و پروکسی استفاده کنند. این ابزارها با وجود تمام دردسرهایشان، حداقل یک لایه پوششی ایجاد می‌کنند که لوکیشن واقعی کاربر را تغییر می‌دهد. اینجاست که بوی یک تجارت کثیف بلند می‌شود!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/ircfspace/2348" target="_blank">📅 08:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2347">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اینترنت برای عده‌ای خاص، محدودیت و خفقان برای بقیه مردم
امروز هفتاد و نهمین روزیه که جمهوری اسلامی اینترنت رو به روی مردم خودش بسته، تا زیر سایه‌ی خاموشی دیجیتال، سرکوب، اعدام و پروپاگاندای خودش رو پیش ببره.
چندماه هست که هزاران کسب‌وکار اینترنتی لطمه دیدن یا نابود شدن، اقتصاد ضربه‌ی سنگینی خورده، تعدیل نیرو و تعطیلی‌ها بیشتر شده و مردم حتی برای ساده‌ترین ارتباطات روزمره هم با مشکل مواجهن. با اینحال هنوز هم بهانه‌ی امنیت رو تکرار می‌کنن!
این قطعی تکان‌دهنده معلوم نیست قراره چندروز یا چندماه دیگه ادامه پیدا کنه؛ اما همزمان جمهوری اسلامی با پروژه‌ی اینترنت‌پرو هم جیب خودش رو پر می‌کنه و هم به رفتارهای متناقضش ادامه میده؛ یعنی اینترنت آزاد برای عده‌ای خاص، محدودیت و خفقان برای بقیه مردم.
در این بین، عده‌ای در شبکه‌های اجتماعی تلاش می‌کنن با فضاسازی‌های ساختگی یا حتی ری‌اکشن‌های فیک، تصویری غیرواقعی و عادی از وضعیت کشور به دنیا نشون بدن؛ رفتاری که علاوه بر نبود بلوغ فکری و ناتوانی در درک عمق بحران و رنج واقعی مردم، برای خیلی‌ها نشانه‌ی هم‌پیالگی با ساختار سرکوب یا فعالیت‌های سازمان‌یافته‌ی سایبریه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2347" target="_blank">📅 08:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2346">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pbz2Sai24T5n1E6v6dIiK3sNFUon_adEMeeu5KEM6e5ZHt1Sa8EL48UNT1He8ZxRC_WOiH_pVmjJCKQ80ti2jyyV-iKtomI4ZmFaonzlCbYJkXZUerkTqi6BCeA0X7jGWavVmayTb_H2RHmHVy00uLS-Dfv-XEV70gwn9mC_LaM8lYi8eyTbi4zV7mMQZc2vKY2-gZgoy3tq9Vbak48P6sbPyTnkNj1BMN2d5iqq8YrxetHn6EfVSIsU2rbsyqsuKccuunAiP0KY_W7Yyln8I1L38GGh2V51o3OsjeFhH5zYzjXy7leepFZH9LyDL4WMhLlTYVflQrFW6iHA9Ydc1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱۶ از فیلترشکن
#MahsaNG
برای گوشی‌های اندروید در دسترس قرار گرفت.
در این آپدیت هسته‌های MasterDNS، GooseRelay و FlowDriver اضافه شدن، قابلیت CDN-Fronting سایفون تعبیه شده که میتونه شانس اتصال رو در برخی محدودیت‌های شدید شبکه افزایش بده، امکان وارد کردن دستی HTTP Type لحاظ شده، یه سری از مشکلات رفع شدن و اسکنر DNS حالا IPهارو بصورت تصادفی بررسی می‌کنه تا نتایج بهتری ارائه بده.
👉
github.com/GFW-knocker/MahsaNG/releases/latest
💡
t.me/PersianGithubMirror/5051
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2346" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2345">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اپ
#شیروخورشید
بعنوان یک فورک از اپ رسمی سایفون بصورت متن‌باز ارائه شده و توسط گیت‌هاب اکشنز بیلد میشه.
آپدیت جدید این برنامه تونسته دسترسی هزاران نفر به اینترنت رو در محدودیت‌های شدید فعلی فراهم کنه و همونطور که انتظار می‌رفت، افرادی سعی کردن برنامه رو به حاشیه ببرن و برای کاربران نگرانی ایجاد کنن.
علاوه بر متن‌باز بودن پروژه و امکان بررسی کامل سورس و روند بیلد، متخصصین حوزه امنیت و افراد فنی آشنا با ساختار این نوع ابزارها امکان تحلیل دقیق رفتار، ترافیک و عملکرد برنامه رو دارن؛ نه اینکه صرفاً بر اساس برداشت‌های سطحی، حدس و گمان یا خروجی‌های بدون اعتبار AI، درباره چنین پروژه‌هایی قضاوت بشه.
در رابطه با تفاوت این روش با MITM هم توضیحاتی از طرف توسعه‌دهنده برنامه منتشر شده که پیشنهاد میشه مطالعه کنین.
روش کار کلاینت شیر و خورشید کلا متفاوت هست و اصلا MitM انجام نمیده، که نیازی به سرتیفیکیت داشته باشه! دلیل اون روش این بوده که بیرون هسته سایفون میخواستن ترافیک رو در v2ray تغییر بدن، پس باید از سرتیفیکیت خودشون استفاده میکردن (که در صورت بی احتیاطی نا امن هم میتونست باشه). در شیر و خورشید تغییر تنظیمات SNI و ... که روی ترافیک ایجاد میشه در خود هسته سایفون اضافه شده. در واقع اگه کد رو بررسی کنین میبینید این قابلیت Domain Fronting چیزی هست که خود سایفون در نظر گرفته بود، ولی تنظیمات و قابلیت تغییر درستی رو برای فیلترنت امروز ایران در نظر نگرفته بودن، که الان در شیروخورشید اضافه شده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2345" target="_blank">📅 23:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2344">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z7iSk8rn_2yd5k0om7NEQPyBVMbmmYyKrcUxXNxcHEV5k2aGl3Eq6I45VmOLaM3bCth6kVRm9560Uevmg8u5wd21n02g13sQCWlBH35CblO-ik8LzqQbgd4wBWE8O24diRCrBflHVgv8RaVvcAu0b2bk4fPWIkVhu5MjE_fwIdZHB9Y4nNqgcZ4aJ9y4IroqHv0Kmvolwju-Bdvc337UeYfXWcN5iaz3cgZwikKeXi6q-AQaHuNINJ9Snd7MctZOcwOySSLtJFB0tvU4UbQyLtUf7cURRx2GQX269RMTy4bw1TWGLx9Waf_NldLIEf184Cs23eFGU0gwQSMzmI9mGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتن هرچی که تهش Hub داشته فیلتر کردن؛ حتی گیت‌هاب.
قوه عاقله‌س دیگه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/ircfspace/2344" target="_blank">📅 09:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2343">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FHCNL1qw7ugAehw01Qw06ttEVpwusfsIfJLW8UePjdd0lPA_w7vGUE1tuB0Bt1zh91_pfBMLs9XauZ8TWLw7xkxJDC5DGN5aAIWgY0E02a1jI0d31lm_mmmrRfz8Ah_sZmN1W7r5kCGvfeyVA0E2H1-XuNUhLH6OOYTwnF1CnN7CQUbyvlDsX5QQmM14G9DngvgP3k-wGHePcWzUy2H22Hj0eEyR7h6XTIZznUgBFFNofIO9aWz3MOEOoGOoEK9-HCxK5tcXCM0YdJhFEWKQ4vfcMIjLCGoZK3YWepOlG_-hObj5RAvcd3Vwmf6FLpiGeGvDtBZ87gChVQ_cFkG_cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان TunnelForge یک کلاینت L2TP برای اندروید هست، که از امکاناتی مثل حالت VPN برای کل دستگاه، حالت پروکسی با پشتیبانی از پروتکل‌های HTTP و SOCKS5، مسیریابی، پشتیبانی از چندین پروفایل همراه با ذخیره‌سازی اطلاعات لاگین، بررسی وضعیت اتصال، امکان استفاده از DNS سفارشی و تنظیم مقدار MTU برخورداره.
👉
github.com/evokelektrique/tunnel-forge/releases/latest
💡
t.me/PersianGithubMirror/5008
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2343" target="_blank">📅 09:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2342">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YZ4tS84-vaerUqV5K7kelInXKGBP2QxDa5oNwSsDlN01uVY1NAin6ADQzQlOC0-yu5xHbwjub7tLKh6XFDbBvEbBUOtCt4ko4vGwHnGObFd1yu9-aC8v9RwHpHmGCIRSSk31wNuezlSzGIfpjM3JtHQ3_lqlueF0CYY0s8LCtXRwGKwfpXcbnTxbucK8OBMy7omxLYsRN4zbAZC9ELY9CsWf6Jwu_pHTJXsAJmbXb-OTxK_-fbxuwBvxcSJQR73PpTFkwi1tvmQVyrffa__ocP4lhi5y0Pi7M1Kt2ZiERUO_vHYvGHAxhpsrnnhGmb25dA3n3Upm4TqzXCId1XBbXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه آسیب‌پذیری جدید به اسم YellowKey در سیستم‌عامل ویندوز پیدا شده که توی بعضی شرایط میشه BitLocker ویندوز ۱۱ رو با یه فلش USB دور زد؛ البته فقط وقتی مهاجم به خود دستگاه دسترسی فیزیکی داشته باشه. برای کمتر شدن ریسک بهتره ویندوز و BIOS آپدیت باشن، سیستم کامل Shutdown بشه نه Sleep، و برای BitLocker رمز یا PIN قبل از بوت فعال بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2342" target="_blank">📅 09:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2341">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cl80q7cN7cifcRDCUbQFWVnxYEU24P1N8h2Dz882cLtZGyG_W0qYwXNsAyxdWkGgoRSR_GeF8SkRIekoBjkmwO2OL9FgmeYtOE7BgdN0DNlKXPI5rlzk_Rxm4c-PcREEP6cbt8Cj9Ly-lZFRSQeomm2OLDOJlBjLeHkNYsq33uRbvqvZgijatFUqPDVdJK5KU-qhCUBCibKtj5nYc5uGqns_Y6kpMkNBCcy8Bq_Boo9Xdnsw9B4CQi84mdFmR0x2jB0JISEIRKYvD9A7dTVf9QzdMgx37jrr3DfZvnaLH9B5Ty0Xy_U5wOb0H6Z2Q3FWmeHVI9pGBxrgzTzEXFnusg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استارلینک مینی به ۲۰۰ دلار رسیده که فعلا اشتراکش هم رایگانه. کنترل اینترنت با اینترنت پرو و قیمت‌های کذایی یه توهم زودگذر هست!
©
imanraisii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2341" target="_blank">📅 08:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2340">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tdPE1J-68TPs2IDg87E-YR6Ce_-uzPvCYsgvp-pcHmPf2VRR5qx9lpAsrO_zuN_8wwkzOjinWV2D--2iyM5sDt-FvHoyDvtMh_rkyDsZzSlZYXteQA355pOBgT6SSC9eN6QJwrHjXsoYv6YwcX4s-thrJvO8DhZWAFoHbmXc_mWZMj1bIfLsKagrDmg0KCRffgqFnYYny6FreLH6Wsv5U9m6lj4PU3j_XyI6gk1F_PVfMghVc_oBYgO2CtYiOm92D_CpXN4woMlSm4cwc_tTg8GF5AxiLamw62V8Qwhsj2Aaspk6KrLOb39AyhySd8alouTcbUD_6A0bn_mHWSMl9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در هفتاد و هشتمین روز از قطع سراسری اینترنت، از جدیدترین روش ترکیبی عبور از فیلترینگ با ذکر "لعنت بر جمهوری اسلامی" رونمایی شد.
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2340" target="_blank">📅 08:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2339">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CK1Dif-js3199Xg0Nz3jg3Iy4AwIbZFc_ZqGrSbqEITxYxld7pl5bJL8Nd_hDeFi8qsVLSVSp976vLVaOGu3VNqfW4zbHZ6PEj7EK5aPNFt0UKnLO1iGUVTnir7OMjjO4ne1YjsEwTI-hpLdWKuaXSZ8bt08bsgf8c5Xrwce-enFqnX8rew3RJaVxQ0yIGuSq_KwtVTD1qD-COOEOwPFb0NIbrzOcTxSzmHwK1wPid0wYb6i4l8leWnj77MQIad1PAF3aFJWDALmVHlfOMLdlWjE6-Q62YP61p4f1_jL0qJRpemBRjXzxilaylvxLx_Wst8QAAN-pcoTxwq8GNEhsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتگ از تبعیض بگو!
اینترنت غزه که قطع میشه، اتحادیه بین‌المللی مخابرات میاد محکومش می‌کنه، ولی وقتی که اینترنت ایران برای نزدیک ۳ ماه قطع میشه، سکوت مطلق! ۱۰ ساله در مورد ایران توییت نزده!
©
markpash
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2339" target="_blank">📅 08:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2338">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PWtNY6CTsP9za70ViXquBUGdC3HA2oANglLDmCQfM-7rafwcgTWIibfxOgp_Sz9ocHyxZHEaCcUaABZHDbv5_VbtQJHbVIV2wOgpnIdEtd-gsOqc8ctplnDukpnjcU17ewaVz5_ZVpidcF4w6yg5YozPwXrgo1ig2cul0hQ8wYlb1btYyVZrdAkqsavWBKiiVzvKvBTppbQR3Sc8cwWBDe2YnQ56RHR2qgb77PZ7hbGVxVGCIeMZAuGdfbXWH9ABQHpRtljz6U6CUwX_HaFErc9idvePWg2oyRC29LW5h4ClcgjkWa_TjOuNPG-JNo7hhjsVaZ60hL7GAcNEfzAVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد حساب این الاغ [توی ایکس] بسته میشه، داد میزنه که آزادی بیان نیست...
©
AminSabeti
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2338" target="_blank">📅 08:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2337">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تقابل اینترنت و امنیت یه دروغ بزرگه. مردم نه‌تنها  دسترسی به اینترنت رو به امنیت کذایی شما ترجیح میدن، بلکه هر چیز دیگری که خلاف ترجیحات شما باشه رو هم به انتخاب و تصمیم شما ترجیح میدن. شما هیچوقت جسارت برگزاری همه‌پرسی در هیچ موضوعی رو ندارید.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2337" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2336">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ستاد فضای مجازی با مدیریت دکتر عارف در اولین روز کاری برای افزایش رفاه مردم و تحقق وعده‌های دولت وفاق ملی، گیت‌هابو فیلتر کرد.
©
pey_74
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2336" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2335">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/su4E5qQ2e9tkSCZab9-N-vLGEl6eZDY5Y_upKFqiynmVbpQWCIXJPxksHxr400zPHwpg7rCLrWMJPxcaH6E9TgJ5SD5fu-AghdYuJOlS6IlUaUzPiMUN3IzMd3PPYat47BeTbdzksk0iJrFO8WGuusASMZ9kV9K3c69n1r0A4ouM3vFzce-vGdNRfwKMMaPrLm2t7xvp6bHDCflIFGPudm6yZC4OtJrOFN-aSkGftwppIl49Ihr6PuROaoLH8GGwZvB7lqwjjwe8LacBxT--r8V7Q2lcUYAHyVf4dEhkx3pN_X3ohjTz8G4oxNF2qzsKrSxUdI3qpbK1AuM0GjjZzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش
MITM
در آپدیت جدید از اپ اندروید
#شیروخورشید
گنجونده شده و می‌تونین بدون دردسر ازش استفاده کنین.
برای استفاده بعد از نصب یا بروزرسانی، باید وارد Options، سپس More Options و بخش Connection Protocol شده و CDN Fronting رو انتخاب کنین.
همینطور در قسمت CDN edge IPs اگر IPهای وایت‌لیست شده
Akamai
رو بذارید، سرعت اتصال بهتر میشه.
👉
github.com/shirokhorshid/shirokhorshid-android/releases/latest
💡
t.me/PersianGithubMirror/4954
©
PawnToPromotion, mahdavi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/ircfspace/2335" target="_blank">📅 16:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2334">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نحوه اتصال رایگان و نامحدود به اینترنت آزاد با متد ترکیبی MITM + Psiphon
👉
github.com/patterniha/MITM-DomainFronting
©
patterniha, MatinSenPaii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/ircfspace/2334" target="_blank">📅 16:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2333">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">روز هفتاد و ششم از قطع اینترنت.
معاون دفتر پزشکیان گفته "درصورت برگزاری همه‌پرسی، مردم امنیت را به اینترنت ترجیح می‌دهند".
وقتی گفته میشه هدف از قطع سراسری اینترنت و خاموشی دیجیتال مسئله امنیت نیست، دقیقا مطرح شدن همین اراجیفه که به جای نظر مردم به افکار عمومی تحمیل میکنن.
زمان زیادی از کشتار دی‌ماه نگذشته. به جای این چیز خوریا، بهتره یه همه‌پرسی بذارن تا وضعیت مشروعیت جمهوری اسلامی دستشون بیاد!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/ircfspace/2333" target="_blank">📅 09:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2332">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r58RA0Uhw65fBG3HC0mM-v7palvdXDl7iI2QDGKFReUlm27f7jRpgaCGDBG04JxtRx5E2xNOxIB0jlWUsiGIliNMDsbl0N6jYzCjOcVvzG5eQwdrDRidWymSgU9r-MQdsto_m7eF9Hvd4YhbBId3RAfVfoxWcLLbiPdmc5iHeZlKlwtisWoOZfyeeae5HNjURPEJiRjYQpA62WR74hvthacOHQhW6glz8nr33cHIc6m0DvEtT4tZ8hxbTYeeN3D2ZFY2GfAnKdg5RBreY_x3tmUNf9FOl8L0yOuyazMX13rpE1ZJ-9RrOp5ABGc7GzkS1UqzLq5737XYEr1Oi2afqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون فرهنگی مجلس: امروز پیامرسان‌های داخلی گوی رقابت را از پیامرسان‌های خارجی گرفتند.
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2332" target="_blank">📅 19:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2331">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZH_xsenpqCZ_jiq47Ip87UaycrfXJODJLpv82wshW-ZN-yMQEw8Lxm6vjm-mfphJyg0gS_PDDcI7OaavLA1J1KhRUgRh58oixLKzXkdkEnelHJh4XbjD37xoOoDBKgY8oMiShZvoIl4XPHG39WOulFXtpppEcOHqik6YKw0zbqu93o9hy3P1_pyLf57xZOT9RUSVHSYdoExhpLQ_0grNJ70q731GdIAFL33Gltp091fiA8hiF3pFTkWxfHYP91dHBtviVmHLbZczArK-ZhvwjArbV_xixa3kRfd2_M18Txm614QKlWDjDP-BbKZouEy5mps-5Kiifsnx64mQKF2V0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷۵ روز از قطع اینترنت گذشت؛ همزمان درآمد یک کانال فروش فیلترشکن از ۱ میلیون دلار گذشت!
©
mosi115
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2331" target="_blank">📅 19:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2330">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QkLfg4jxmUgePk0For_LpVwN8mY_lLiqHyhQo8KKkmQbzWzdP8-szDNblofunp2zdLxRqpvGmlfuae_smYHaQCDQOyO6y_GjiITh0fP2UqetbaW5KtPPO0-QsYu3x00C6lX9Er7MNNUGdDpQOm-ekTx5qwekyaWcFlV6RntUn32kq4jB6g3V6MQvwSgpX02ybcfVFLYfugdi-wDnzWgD1k8cEkMLTyz1gTKyEN4_7PEXqPCZW8gbCwpGamMxAYozImsO1T-fIqTVz_wudOBtugPH0VkusdANiZv-HQVVSB1baC6goMdUzWJaZa4RlO387Oy61gcLlLVfNEbwnltoSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میاد مرحله‌ی جدیدی از
#اینترنت_طبقاتی
شروع شده؛ دیگه خجالت هم نمیکشن. قدم به قدم دسترسی برخی افراد و کسب و کارها وصل میشه، تا عموم مردم به عصر بدون اینترنت و بدون هوش مصنوعی برگردن.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2330" target="_blank">📅 19:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2329">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سی‌ان‌ان در گزارشی نوشته
#اینترنت_طبقاتی
در ایران خشم و نارضایتی عمومی رو شعله‌ور کرده و به نمادی از نابرابری ساختاری در جمهوری اسلامی تبدیل شده ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2329" target="_blank">📅 19:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2328">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">قوه قضائیه در یک کشور مردم سالار آنجایی که حقوق مردم با تصمیمات دولت یا نهادهای امنیتی نقض می‌شود واکنش نشان میدهد. در ایران رئیس این قوه نه تنها حق مردم در دسترسی به اینترنت و کسب و کار مردم برایش مهم نبوده، بلکه چندبار شاکی شده چرا اینترنت پرو را سختگیرانه نداده‌اید!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/ircfspace/2328" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2327">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=s4usmKPeIyWige-5A0rHLR5yNQiUBaN4L-TMsQfoadHt67Q7Ztb8bBkkY19Cg-uIb14rWhMPx68d86Mj_ZFwFEg-qalg_dbK-zJF_sxvZpOSXjgYYtSzOMlE_5uINzSlaUtGcTPthEwb7OFdo5shvK1t-RxMr3hGttDlQk_PJsqC8acPFATixF1tmpsos3MwujKSyIGOwsWx4ePYpSy8ic-JA37nBicMQsLiWaEmBwnD0bv_KfoL8ux7f_sSl8jd-XCDawO9IDpYSUSAmbNs0LU-chnsOQQojcgj4CqziNTZYcuudR9dZaeHHeyKnZpIokcex7QTAuHhqQJ9l8thQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=s4usmKPeIyWige-5A0rHLR5yNQiUBaN4L-TMsQfoadHt67Q7Ztb8bBkkY19Cg-uIb14rWhMPx68d86Mj_ZFwFEg-qalg_dbK-zJF_sxvZpOSXjgYYtSzOMlE_5uINzSlaUtGcTPthEwb7OFdo5shvK1t-RxMr3hGttDlQk_PJsqC8acPFATixF1tmpsos3MwujKSyIGOwsWx4ePYpSy8ic-JA37nBicMQsLiWaEmBwnD0bv_KfoL8ux7f_sSl8jd-XCDawO9IDpYSUSAmbNs0LU-chnsOQQojcgj4CqziNTZYcuudR9dZaeHHeyKnZpIokcex7QTAuHhqQJ9l8thQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر هکر بودین و میخواستین بانکهای جمهوری اسلامی رو هک کنین، سرورتون رو کجا میذاشتین؟
علی کیافی‌فر، متخصص امنیت اطلاعات: در جنگ دوازده‌روزه، نوبیتکس، بانک پاسارگاد، بانک سپه و بانک مرکزی از داخل خود ایران هک شدند. مثلاً نوبیتکس توسط یک سرور زامبی واقع در یک مدرسه‌ی علمیه خواهران قم هک شد.
قطع اینترنت امنیت رو کمتر میکنه و نه بیشتر. سیستم‌ها نمی‌تونن آپدیت امنیتی بگیرن، سرتیفیکیت‌ها expire میشن، ابزارهای دفاعی (فایروال، آنتی‌ویروس) از کار می‌افتن و هکرها (داخلی یا خارجی) راحت‌تر کار می‌کنن، چون نظارت و لاگ‌گیری مختل میشه.
©
farhad_mottaghi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2327" target="_blank">📅 19:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2326">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k73iOQLZ1ZEFXUf6eC3u3t_99H_oErTUBaWjIcijVTbCHnynHtD_6emH68k_P6H9ZXpayJVbGZWzZiAcdXr6BtQ1P4OQzbd19MedEqir918En_kQGJDH5Mu5YuX2Ne1XOadyiXpRQGl6rKA5ntYBI4p9QiC0VVZcXvstMuCmt_f-H8GVU5w4-KtEHhrefm7TNoUUEdKWgujHh45bI4MCBv1LD1-QRLkQ7_UTI85Ihxm5IAJUrpsxB5NTjY_zTPEJ6ibeRwZwT4N1tcm3l5YznTBuD3s2Ci6qUseN23g-enAfrLQuALChPYXCO4WxiIqoXTFVOkNnTzfDc-RgxHSGGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آگهی یک دفتر پیشخوان دولت برای فروش
#اینترنت_پرو
©
mamlekate
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2326" target="_blank">📅 19:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2324">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wl02YmKMwDVDRPYAfAAm9ZOytNoTYApN5P3L3b16xVDj09T86awIfAT-rRBzsy5sckFJh02Xemgu58qfxlnWOCNSru8ZrLgkmNWMJU2lUteexs1bpIS53xTjazH_DiFY2WvY22TAbyVZTMtVO1m31B9D8z7ewPkLWuT3VMQZbYHpWWhs9nvN9eMk3Wk_My3IfVBkViCWHMOZQyAVSSz1uit3fzKtYmxTb_J-nux76gw2bDLUbKqYq7Mpa9pqQFzE6hOQC3NM2chJfm6NSj30g4kYwnWcWnm4Sj7dUgwv_pSIrJO6QIzDGaOZ8qSzQecoJ08QBcuigQNbKBYqa0Nwvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا دسترسی آزاد به اینترنت در متن سخنرانی‌های رییس‌جمهور و هیات دولت برقرار شده!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2324" target="_blank">📅 10:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2323">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تعداد کاربران اینترنت پرو کمتر از نیم‌میلیون نفر است!
تا امروز یک اپراتور با ارسال بیش از ۴ میلیون پیامک، برای بیش از ۴۵۰ هزار سیمکارت،
#اینترنت_پرو
فعال کرده و اپراتور دیگر با ارسال بیش از ۵۰۰ هزار پیامک، حدود ۴۰ هزار کاربر پرو فعال دارد.
©
aghplt
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2323" target="_blank">📅 08:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2322">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FpbANXPIWaZ3vozbXyaH2U2ZFy-mFKGYmgJsrsS47-g4ykZpCq4pyDiE7q1XSyZ_L5ENY7ih4dykt6zKIQJyPax-zjyBVSH8FrsUYycr2njN9AYHRze5mGlS_bPAvrFnzeJfzxpx1wDpl6H1LsRSakqORPe9d0a0lrd3--3tZIq_MOATMxF69mnvKXs3JNrD1MgmFZoPx8NguHWgQzbYJZq2xBJ_KwAhyU54e28kFNeO3rtlH2QP2zp-0G_jODt-haTMJGms6DNOdQrOFNYW8jBpg46JLl8j5bSYzHD-hBIMG3kCzqlSRbidnWKFluon-MyHu6d7yNVK5BDvoASpsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن مهندسان نفت برای دریافت
#اینترنت_پرو
واجد شرایط شد.
۷۵ روزه اینترنت رو به بهانه امنیت به روی میلیون‌ها ایرانی بستن و هرکی که کار و زندگیش به اینترنت وابسته بود به خاک سیاه نشوندن، تا
#اینترنت_طبقاتی
رو اجرا کنن. مدیونین اگر فکر کنین کیسه دوختن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2322" target="_blank">📅 08:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2321">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بدتر از قطعی اینترنت فکر اینه که سالها درس خوندی، دکتر و مهندس و محقق و پژوهشگر شدی، بعد واسه کار علمی دسترسی به اینترنت بین‌الملل نداری؛ اونوقت حمید رسایی با حول و حوش دو کلاس سواد برات تصمیم میگیره تو اینترنت نداشته باشی، تازه خودشم تو ایکس وله!!!
©
NiHa_Mehr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2321" target="_blank">📅 08:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2320">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bMM3enCHpWk0OjMyb_XiGeD9nDn_86v2o0lZpGvc64tAQxA5yv4lK0tnMaS8Hab0dgV91j2_34JaAy2csnp63wsJfBabNpVU6OQW8p2a6iIOrBslnvMgAr8B68soo3VlBr7Gi-toVUZ_jpRc6mUmyQep5_NGDcv7qEDPfzvCN9dAWoMghJ6-r80jO7uzieA4XXHOFTP2ncem4pqXAGhwYPnC3UQej_N7gZlWUocklxnNlEfvOma51jGhtSs4vP0mmJbfAsggg0XNf90Xxl6U8syQs7tuWGM9TQTeeWUo1RIPy-T2xuFSs-pCsh34gMqKEn-PQ73M-6VuztYCSFZdVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس قوای سه‌گانه کشور در واقع ۴تان، که یکیشون به نام
#قوه_عاقله
نه توان قانون‌گذاری داره، نه زور اجرای قوانین رو، و نه در جایگاه قضاوته. مهم اینه که قوه عاقله قصه ما با
#اینترنت_طبقاتی
مخالفه و قراره نقش اپوزیسیون داخلی رو در این مضحکه بازی کنه!
©
nimaclick
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2320" target="_blank">📅 18:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2319">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NnHIn4SzNFlpDAaYssJkVYuSz9Umu8wEn-2_JP2tIQ9_RB03gLvcXdL3XsAhoI4-tQ4Nl8JKaBHngOMYHT_ggqfgs5Jf8JyjrbwSmMsN6AHJhshCsW-7bljicOxkLi0HTtv2brP4WusQ1dOM6qWCVvks1owsDudFcCumjKQXtk4kg7xyHAoHtHw38lIzhpMNld6II-Hc-ihbTEcNwbZtAiikC0LxSZ9onxdj9B3V_2KolFe2MZKOvQ56UC5Je3mKvwBGKOA_FWodJarCEalbpCMOz2D8V02vB20gbmqOIarQdUJT1IscGPXQBxWw_IBgWck6OEMzn99eSPnOnLH1zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پای
#اینترنت_پرو
به اتحادیه صنف اغذیه‌فروشان و مواد غذایی باز شد و حالا با ارائه پروانه کسب و کارت ملی میتونن از
#اینترنت_طبقاتی
استفاده کنن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2319" target="_blank">📅 17:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2318">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xah_OqajnWOtYjdK17t8GpH-OpZOHWxbRyn2xVSGAPSZcageO2fdqtR_LMeunxPpFwkGMdMlXjUbOpT0Jq7DpK51CHtqvMT2GoPo_TWLFDwXHpGnkeykPfsNvzA8YsgQuGpYd0teO73TfkPgXSdHfhqAxPS2H-yvryZ340OlCJqQxO35srDI4FPUOvM3AdgQ9l1M7oxMkQ-Jjb0xkOVtrnQZFdZhAKlT4xrVoWvraKMUHfe4QWyVVdPQFgFFZJ30Xmvgw9K4j3WnzvWCZRP9jq2Q1qu1xkLWV0D82CxHPfx6KPvka6umCmSeT-gJKSbpNOhvRRrobaxv45aN6--nCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان TunnelX برای زمانی ساخته شده که کاربر نمیخواد تمام ترافیک در سیستم‌عامل ویندوز از VPN عبور کنه. با این برنامه میشه فقط برنامه‌هایی مثل مرورگر، تلگرام، ابزارهای توسعه یا برنامه‌های مشخص دیگه رو وارد تانل کرد و بقیه ترافیک سیستم رو روی اینترنت عادی نگه داشت.
👉
github.com/MaxiFan/TunnelX/releases/latest
💡
t.me/PersianGithubMirror/4816
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2318" target="_blank">📅 16:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2316">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OxDdFY4OJLRZE1f0j2K37Bqx3SWnjsuR2XAbvdXThqdwjIQhmkfNeFI7fL4eLOiKN9kUIkdQRFHtZPNd9p94LPV1QViG6KYEwb2P_x_WODHKfcIuZF2kU61Uc_FkOFxhtIQBjhY7Kzb5_5uSTsaaLq1XNDKLW7JNeob9QPYIPXncM8GshCJ-SiegpygUIzJR4n9J8al9M--bmSyB5Ms2Ah6qUueEuplHPkAS0r8O_IuIi-mZKtczm08LBbsADb1nI0pF7-Xfy3rVZFkfX_YZJGwSkIuNF5HkFQDyRMymxjGE0dfagdfS94ltH0r5yJH2N0fg4kp1j4dF6ACNP7yvsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر اینترنت غزه، اوکراین یا هرجایی که حمایت از آن برای حامی‌نماهای حقوق بشر "ویترین اخلاقی" داشته باشد فقط ۷ روز قطع میشد، دنیا را روی سرشان خراب می‌کردند؛ اما اینترنت ایران ۷۴ روز است عملاً قطع شده و آب از آب تکان نخورده است.
فکر می‌کنید اتفاق خاصی افتاده؟ خیر.
ضریب دسترسی واقعی به اینترنت آزاد در ایران به گواه نت‌بلاکس به حدود ۲ درصد رسیده؛ میلیون‌ها انسان نه ۷ روز، بلکه ۷۴ روز عملاً در یک زندان دیجیتال گروگان گرفته شده‌اند و همزمان که جمهوری اسلامی در پشت پرده به سرکوب، بازداشت و اعدام مشغول است، آشغالی به نام "اینترنت پرو" را به‌عنوان راه‌حل به مردم می‌فروشد، که عقیم‌سازی عمدی دسترسی آزاد به اطلاعات و نقض آشکار حقوق انسانی و حریم خصوصی شهروندان است.
ظاهراً برای جهان مدعی آزادی، فقط آن دسته از رنج‌هایی دیده می‌شوند که موضع‌گیری برایش هزینه‌ای نداشته باشد، یا چشم‌های مردمانش رنگی باشد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/ircfspace/2316" target="_blank">📅 10:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2315">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p-Dz8i7-lYa1ATt8XwyogNH97Hx-WunO5-OzSrhltBHTL1-flkgIldYAtrzM2AnrnYLNygUzuc1IpAjU4YWb1xOzxC2aoEbrB2sjDmoxdgiM227XpwCBrLAOZeDlwzrXEhdpfQ5UmQBDoChSRlRLxcbnJU9Hjaf7nvjHD8howqzgDNYxX4DWnec9qrZI7t7pGKH80ARhIVJ-uX15xCA7ptuZQG_dk-mDdoVFYfX3nF96Lp_YElN37AnFEu3qbpwyfOFf5JPK__aza2N9geg1DaQ82tRX4Q5XI7r849BvMwsyA8Qogh1at9G_nHeFulKbbukUAe5O0zWJ1sHv32A5hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در روز ۷۴م از قطع سراسری اینترنت هستیم.
وزیر قطع‌ارتباطات گفته "در تلاش برای برقراری اینترنت بین‌الملل در اسرع وقت هستیم".
نتیجه عملکرد و تلاش ۷۴ روز اخیر این فرد از خروجی عملکرد یه مترسک داخل مزرعه هم کمتر بوده و جالبه با اینکه از بی‌خاصیتی خودش آگاهه، حتی بصورت نمادین دست به استعفا نزده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2315" target="_blank">📅 08:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2314">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lRJKdQ20om91Qm-OTb-5kH3AKNwCccN_HvFdWh8EsnkT7xUMw_YlOFt2cdRq35um8BQ888CYD5pB52CqfMK2kPDUo_xP2iNJqlp7mhVIcB4SMosfV_uqNxnqawAD9nnCpbVR7W4IHX8g1EPAQayaWN2yOeOh6fMyvNFJYpqzOEf-ucksFRaH6s6VihqYKahktqrQ_LQhjMWPpof4zzNi8pVlYeP-rB8GOeJ88541D0nRu61E8jRg6w4-vHT2lYQBQI2o13cpH1ISnHscqlSLZEr3131vvqt5eZwakYd2GrazZDRJvATcHpBp5O8aVOr3zVEnDIZqHuo3cjaTF-GMxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه روندی که نشان می‌دهد تصمیم‌گیری درباره اینترنت و سطح دسترسی کاربران عملاً از دولت خارج شده، وزیر بهداشت برای رفع محدودیت دسترسی به پایگاه علمی «پاب‌مد» مستقیماً به رئیس مرکز ملی فضای مجازی نامه نوشت؛ اقدامی که بار دیگر نقش کمرنگ وزارت ارتباطات در سیاست‌گذاری اینترنت را پررنگ کرده است. /شرق
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2314" target="_blank">📅 08:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2312">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dQgbueUtUx49RwwOY1Kz_cPSjqR8ZoSd_flG44LN5OXaYQWkCQUldUv8_L8lMDhUZw1YD9z1qmMTjPbkprlNuyFs6VSJwrbZMMrKLjdQWxPhJmgnv4eYZkct--DI_FCoqBXermttxEcMgOFgMn8twy_YbEoDs3-yopsc4lkY8fLjSWdAb-5ere9Z2QeUQ-NSPUnnipc8oI1oBLjpUcKZWNcgQPmnqxwzuSHKQQcIiyALWeXDSXqa-5PL5QFe_RPOJFRcmpvk0sWS-CbC8eLGhKQhU6B8kwjSg6yTDLtDWK9Ep3LHUjZ2XyKdT-C9XsZ0XfneUg2mVm6iiS-fZ7m_qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت AIO Downloader یه ابزار متن‌باز و کاربردی برای دانلود فایل و محتوا از سرویس‌هایی مثل یوتیوب، گیت‌هاب، اینستاگرام، ایکس، تلگرام، گوگل‌پلی، تیک‌تاک، پینترست، ساندکلود و ... هست، که فرایند دانلود رو از طریق GitHub Actions انجام میده.
این ابزار طوری طراحی شده که در شرایط محدودیت شدید اینترنت و وایت‌لیست فعلی بتونه بسیاری از فایل‌ها و لینک‌ها رو دریافت کنه، بدون اینکه نیاز باشه سیستم یا سرور شخصی برای دانلود داشته باشین.
با توجه به اینکه این پروژه به GitHub Actions متکیه، بهتره برای استفاده ازش از اکانت اصلی گیت‌هاب استفاده نکنین و ترجیحاً یک اکانت جداگانه بسازین.
👉
github.com/ProAlit/aio-downloader
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2312" target="_blank">📅 08:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2311">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QA9-r3T4Lz-Alx3xZOg30a9mi1c26_GUwU5KdZcLRW3-isLYks7jfm28JA_IqH18eI9jEYC2xTpRlAxsmZkkY2hxx1nJBV-5EIjnQrYuy-M988-QT1HV8Bf3qZRXAwOKvIulp4sfbS7-TZqf-CU8iFalOBsUGBR-wA1F73V0CD2aHs3XuzVKIN_rccnF7VSQ2_AKVghFK9j-w3TxvHheHaNZE5JjdWeIQk7g4_Qsi9yZNYjB1x9nlt7lmYeMAQlA68sVkCBeLmPa5modUj0rT1wgk95DfTBvmuRmpjipZpArMbUztDVFbtaWrbhBZpbPJl3qRq-0q-2T-cZvOC4jNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پیامرسان_بومی
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2311" target="_blank">📅 21:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2310">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kVVeQxW3UYfCEm0VbJGIXD58qgN6lGrqfslaxjzRmaiydXVzbAyC9B9VGKQPuefThwYK7VxLrONh3gbeDO-3DH-NphVyGVpMYps12NVYnXvyPe4tYUXXvgzzQ5BqGWGUQ5i4py6a1ztLu6Ni6wcItg_6eGfDbpOhdWNS93kXIbV8VlXvWIgLWLYJ0R7DP--RApg3Lq_gioEx2Nh-SoL5B8pMvIbETk7WuYiT18T6gJXdHDJ4jJkV1BadgUaH4MALLgc9q8aHfIjaIU3_PCbsOq6pys2oFbAj0jebMzCMCaSX23YTTegA9jiyf51HMQk2X2oULYpRLhQe8ufvNDZpaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه رودربایستی رو کنار گذاشتن و بدون ثبت‌نام و بدون احرازهویت، بابت پیوستن به پویش جان‌فدا ازت تقدیر میکنن
😁
کی به کیه؛ اگر آمارش به ۳۰۰ میلیون برسه هم تعجب نمی‌کنم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2310" target="_blank">📅 21:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2309">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تا الان توی هیچ پستی نگفتم که به پروژه‌هام دونیت کنین، چون حس خوبی به مطرح کردنش نداشتم؛ ولی شرایط همینطور پیش بره احتمالا سر چهارراه نشسته باشم
😂
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/ircfspace/2309" target="_blank">📅 21:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2308">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">قبل از شروع جنگ و قطعی اینترنت درخواست فیبر نوری دادم و حالا اومدن نصب و فعالش کردن.
با تشکر از شاتل بابت سرویس خوبشون؛ در واقع قبل از نصب اینترنت نداشتم، ولی الان با سرعت خیلی بیشتری اینترنت ندارم.
©
itsmralii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2308" target="_blank">📅 11:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2307">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SiDYJtecyPJ3IIw1oglwU8Eq6vZdXXd65PKA2rLqqhZTpunL8WLzpKWCIw3dCdG-aVWdYNAgcbM0s9S_c1CiRuSlj25aA1L5eiEqyrd9yEjPZFeOAT9P5yulQT3yecJGGR3VBh2eJsUbQ4MCKPWu9weC9D5_0YbaJ2XQhq2u5-kFSGvA-de5CZOkBsBZESDodtgVZ0_EBSrxyB_GwOENr0f4nGAdPpkd0F3BUOeLKkcUxcq4RFWroXV6sb5mkraCQKUVSEtRRC7UV8kf45GsC-bevwAhWWrVfLBoa6-FhuFHmKMhpIMu2hi4q183tzMrHIHrPlC0TECeO4Cs8go5RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور از وزیر ارتباطات بابت هیچ و پوچ قدردانی میکنه، بعدش همون وزیر از رئیس‌جمهور قدردانی میکنه، بعدترش همین بدردنخورها دسته‌جمعی از مردم قدردانی میکنن؛ اما تهش می‌بینی ۷۳ روزه که اینترنت قطع هست!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2307" target="_blank">📅 08:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2306">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R2UuAgDyjPHu-1Sf7SE1qpYd1mMctnkenWTh2wHnKisxyri4M-zjEEpq6lYwp0GxUHDCcRT58YdI9O2p4gYltMtbBqb5XhiM4achUTmHr1jtf_w81FHUQGVjaCE707CkBWWShQbR_Q28q9VUkBR-DA9WtQOmE2NBrE81t8UUd7OwuXAj56IYx1Lm96OuRq5JLN79zSRzMPY2CbzHJZFwAidQi8IASo7RCp5wQWZTYN2-qNOLN7TXmNmOD56MSRcNWeQaqWhXNvfjLFfH4QD_Yz34zsAkmY2QwcB8mJjexmSrSaFRau7X7uoPKRiDLLysv1BncU9SaLJqypL8w2jvyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteDNS یک کلاینت متن‌باز و رایگان برای اندرویده، که امکان اتصال از طریق DNS Tunnel رو با دو حالت Proxy و VPN فراهم می‌کنه. این برنامه با تکیه بر MasterDNS و StormDNS طراحی شده و میتونه بدون نیاز به تنظیمات پیچیده، ارتباط رو از طریق تانل DNS برقرار کنه.
👉
github.com/iampedii/WhiteDNS/releases/latest
💡
t.me/PersianGithubMirror/4637
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2306" target="_blank">📅 16:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2304">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qnymqWEVEow3FjyWIbVMJbfl4ILO4Hmi4pw4KnBg95CTH5l7mAbXAp18a8OqIpTZXjieSOB7SqagDoNt1qwQjwI8B3ZYB1-TN96GssugLgfmYdOJmvcapeDv7b9s-UkZOyouUre-dTLDM5sPvWYANc1woyxO4EyJYW4zt_5GafHB5llDVYIJtORPKIFP9uy7HnyA1wDNL3ffsBgNtptOwM1WEca_frhtAATjfYIIc91pkt8mOZv0xo-eBwJ3JXr0yZskFf930rQ3k-Ca4vF-2H6L5hjeJcqcPd7ZRqi59lRjSjFSY_OxnR5_MCFbUPNsB_u_TlRNdyXxNUEaozWd2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز که نت‌بلاکس عدد روزهای قطع سراسری اینترنت در ایران رو اعلام می‌کنه، یه عده میگن "خب شمردن که کاری نداره، خودمونم بلدیم".
ولی مسئله فقط شمردن نیست؛ مسئله اینه که نباید این قضیه عادی‌سازی و فراموش بشه. اگر فکر می‌کنیم راه مؤثرتری برای اثرگذاری وجود داره، خوبه؛ ولی سوال اینجاست که چرا تماشا می‌کنیم؟
۷۲ روز گذشته و هیچ اقدام جدی‌ای برای کمک جهت اتصال آزاد به اینترنت انجام نشده، کسب‌وکارها نابود شدن، آدم‌ها شغلشون رو از دست دادن و سفره خیلی از خانواده‌ها کوچیک‌تر شده. مردم برای یک اتصال معمولی باید میلیون‌ها تومان از جیب خودشون هزینه کنن و در عین حال بخش بزرگی از نهادها و جوامع حقوق بشری نسبت به تداوم قطع اینترنت، سرکوب، دستگیری‌ها و اعدام‌ها سکوت رو ترجیح میدن.
در فضایی که همه‌چیز خیلی سریع به حاشیه میره، استمرار در اطلاع‌رسانی خودش یک کار مهمه و همین گزارش‌های روزانه امثال نت‌بلاکس حداقل باعث میشه موضوع قطع اینترنت در ایران کامل از توجه‌ها خارج نشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2304" target="_blank">📅 12:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2303">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">این هفت کابل اینترنت جهانی در خلیج فارس رو اگه قطع کنید خیلی خوبه، اونا هم مثل ما اینترنت نداشته باشن، بلکه دکان‌های حقوق حشری صداشون برای اونا دربیاد و یه نگاهی هم اینور بندازن و دل ما هم خنک بشه!
قطع کنید.
©
ehsan_369
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2303" target="_blank">📅 12:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2302">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rsaIXERItfdsicZ_0HIYHn5idJb26gP62761VPII_fX8a2QGYsYpnXOgRBRlthwMkv7_cl9foYWp5ChCwrR6kc-Mv2rz3Q4ABCov92lkafv18bBVeNY1lKgjQT5PeRGzRWcGB6w7_Yz3hbihzUnDVhY7SLUjI1DFjlr0pjMvdHbAYyabaIqXLEv9jEZUFn26urwuw3tOC3E6A9QlOKu5x911RkcGeCaEved4HJ7YYNGb3L_EaD0w05bUcgVwGUB1Qa7T6UalrJqt24fGLMcImoDZvjlRILCv1GCT9UV4-71UcG-MJumaDmLJXHESrocbLDNMnhHFMw96wt0oGyyryw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم نوشته تنگه هرمز فقط مسیر نفت و کشتی نیست؛ بخش بزرگی از اینترنت و تبادلات مالی دنیا هم از کابل‌های زیردریا رد میشه، که از اونجا عبور می‌کنن. پیشنهاد داده ایران از این مسیر پول و کنترل بیشتری بگیره؛ یعنی برای عبور کابل‌ها مجوز و هزینه تعیین بشه، شرکت‌های بزرگی مثل متا و مایکروسافت مجبور بشن تحت قوانین ایران کار کنن و تعمیر کابل‌ها هم فقط دست شرکت‌های داخلی باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2302" target="_blank">📅 12:17 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2301">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VFldto3uSX6KHm57Sl7wP7oL9nLQpaaU77N3jZ-jqrKp55nOvtKdbJpuBEstlEi4up8j4z7-XuxG8mVhTMyyd6N8-uX1N048kBkzynpsJB5fHdpo6JTlo8vFLtYRVHCjivlOQGukZaX9JDdJmQ0VrTn5WlFUCblsaZ0cwBZ02HUHd333lPjq3IZsANvWF4US84BpKJeS-jhMeYpBHsAC-MWe1_es8bGQMEDT946m4dCPIqJBD5qrPha4mrzHzjUUGhryeLDbtHfBZzvsFSd9oK4cKfSdgr9iWGZ98XFbNI0qsSVuP0E3RKsX4AlKY5T8VcCqDKBVWB5AvAu1rL2H-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع سراسری اینترنت در ایران وارد هفتادودومین روز خود شده و هیچ نشانه‌ای از بازگشت گسترده اینترنت دیده نمی‌شود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2301" target="_blank">📅 12:07 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2300">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WMkw2Nap0YSfO7_2_3YJJMXFjpHj29dJh2Q0ZjMRlduILqbT75IwMo-4ajhg364lvUhH0z6PIYEKFXGq6sUEuKKcMi_CRNnm6eBabLDJDJ-4NBHI2-cd5hFxlIdnqIvhzQi-5YoE4Ie_tcvuPTBvROV-228tTZPEv8Dc1sQTw7TuuYKNWc7k35sMo4C616BsTg4YzuX_zDMTipdQyLl-wFJA0Vzp3J6tPJeUcYt1Zi_kHTwYqajX00NoBtuM2-1Cfa2BnI9cXC9Cebl01mvx0oPI0zvmswICr-70MqQ8Fd1ERK_RCHJBbTPNYD64pzsRn9u4HdCWUeiuFuIX4nRpTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۳ از اپ متن‌باز و رایگان TeleMirror برای "دریافت آخرین مطالب کانال‌های تلگرام در شرایط محدودیت شدید اینترنت" برای ویندوز، لینوکس و مک منتشر شد.
در این نسخه نمایش پست‌ها بهینه‌تر شده و مشکلات مربوط به کش تا حد زیادی برطرف شده، بخش تنظیمات به برنامه اضافه شده و امکان بازگشت به تنظیمات پیشفرض فراهم اومده. لیست کانال‌های پیشفرض افزایش پیدا کرده و علاوه بر نسخه Lite، یک حالت Normal اضافه شده که تلاش می‌کنه در صورت امکان تصاویر فیلترشده رو هم نمایش بده.
این برنامه فیلترشکن نیست و بر پایه دسترسی‌های فعلی وایت‌لیست اینترنت عمل می‌کنه، بنابراین ممکنه روی برخی از اینترنت‌ها قابل استفاده نباشه.
👉
github.com/ircfspace/teleMirror/releases/latest
💡
t.me/PersianGithubMirror/4599
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2300" target="_blank">📅 18:57 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2299">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">افغانستان تست خدمات اینترنت 5G رو در کابل استارت زده، عراق تلگرام رو رفع فیلتر کرده؛ اما جمهوری اسلامی تا دقیقه ۹۰ درحال آزار و اذیت میلیون‌ها ایرانیه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2299" target="_blank">📅 17:52 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2298">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kkSLkEoKVcCQqV4Z_suuR_jDNCRSKt2RvYhLZ1wMC2BmrBna5ulKRgnBVgOkxnIt8pr1fAqBSg69MrE1SaQ64yZYg2pzwGuySm2g1h2B1EK6dbfi2DAYxtPc7gBX4WnmNmB0wQzISLurRg1Q3b3Eb0FUTgJlEURi_e463lQyIFO2wDRNNoycQPcJ2ZtIQ2qph_mo9dueaAcr3YCWcYup5pCt3btpX2M-dYEP98F-CZV6d3EeKo9WgHMXYgXHpthdn4UM1MAmGOP4B_NWhrtcX38XLl5eqSbvINByhHiWCzzuH4_UDvNyI4ifB3nMp13FRWURNZbFGiWKY7spnRxVIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی خاک بر سرتون (پیامرسان‌های بومی) که با اینهمه حمایت و در میدانی بدون رقیبِ جدی هم عرضه ندارین کیفیت خدمات دهی، پشتیبانی و توان زیرساختیتون رو ارتقا بدین و بعداز اینهمه سال سابقه، آدم نمیتونه ۸ مگ فیلم ارسال کنه.
بعد از خودروسازی، باید شماها رو هم دومین فرزند لوس و بی‌خاصیت کسب و کارهای داخلی دونست!
©
kamran_falahati
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2298" target="_blank">📅 17:48 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2297">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">جمهوری اسلامی ۷۱ روز هست که اینترنت رو به روی مردم خودش بسته!
روح‌الله مومن‌نسب (تئوریسین بارداری با ۲ گیگ اینترنت) گفته شرایط اینترنت به هیچ وجه نباید به روال گذشته برگرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/ircfspace/2297" target="_blank">📅 17:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2296">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i_Sk7awVUY1CUQFKfK0OY4rnQKqNDKozfiWNVMyagF7q2g0T041G6QnsdNh-gXuJOqzLoRHbsL9JfPCstoGnh9KoOnEnqnSS6gwTgecJL1GIUNuOfTVNml2_Yw9a0DFCWx-isRbjd86RdJMu-8pNyCbcqscj0Y5fXfMqHmyKXiN8JeRrSLIH2JkqCk00vW_zNI0CA7zsP7uj0k4KOcz5nxGeIIwGumMVi9fR9G6JBTk5zy5RickztR3Ds7mt-CdFC2mTOyhKfPziHAWZICQRkmpJWuHHNPOGTGd1hsfj4BS8nwOez8yROWsJUv0Jh7HfxrizjhU8U-FBsS4GXwtWFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان Pigeon یه فورک از پروژه تله‌میرور برای macOS هست، که از طریق اون میشه بدون نیاز به فیلترشکن یا لاگین در حساب، به محتوای کانال‌های عمومی تلگرام دسترسی پیدا کرد.
👉
github.com/MaroMushii/Pigeon/releases/latest
💡
t.me/PersianGithubMirror/4500
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/ircfspace/2296" target="_blank">📅 17:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2295">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PhG76juwwYcqdeIhhx0vufYcTD5lz1LrHreyPrJz5g830i6ODAu32szkHJTva8_w-VHvfOq9cspo5XJtyzUoZqWSzW9sXY6AoDA5QSrXH_lzWkTnAZQNQW6GZ5BTnN-zDww84w3wmF4JJhlN_1fHeKAdS7VpdOPC6lwSSQvjk8H9-T4O_dVTQ76VaKciTZaQuOYr2OBrYbuOHc9L2xJg9IK44zI_qVtGvyehVq40rUOziNsNnc6yQkiyynIXoC-CplH8-eAAcfKWYPQEUzZhWRurCYj04EwngG7Mc1XVnGoBshnBota8kw2WzKIRJPiWrt5Tp3-4L3B3rcWKVfLzPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Youtube Sandbox با استفاده از GitHub Actions بهمون اجازه میده که فقط با ارسال لینک یوتیوب توی کامیت‌مسیج، فایل ویدیوی موردنظرمون رو توی فولدر Downloads (داخل مخزن) ذخیره کنیم.
👉
github.com/iphoenixon/youtube-sandbox
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2295" target="_blank">📅 17:36 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2294">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qcz27xbWWZHochG3acMpKzr9cC6-2Ij65o1O0jvIBesOsVTpt9KMJRBk_xxhLbBuHOmXH7d4sw8qQuQOpL9sCPSOPRLU_8Z0N4CPJz2xZxWAB2HGW5bbfDuEEPzYxZuCrdXHnOQweHvkrIGQS3AW-NK0TpLPcSnHod3BFtJOXZtx7ukGnMPPClgbRYyS6v5tZIJft322lnZb0gS5P-n31DlII2GwrcvCCOokb69CpNkvNoWjH-SslYzmqbgClZRZeD2HOcQYOWsO91f3Du9cuX113XoljI1je_smgTFd9pw2avHdIEfqIfI1tfeYAUEb-6_WwYCpx5NQnsNH3wg4Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه گوگل براتون باز میشه و در وایت‌لیست اینترنتتون قرار داره، می‌تونین خیلی راحت با نصب این کلاینت اپن‌سورس به گوگل درایو در اندروید دسترسی داشته باشین.
👉
github.com/aleskxyz/Round-Sync/releases/latest
💡
t.me/PersianGithubMirror/4489
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2294" target="_blank">📅 17:26 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2293">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dHz0EdEwlbDdT-KshTa3C7d3aepjx9Yqfn9_gJUgbS4oPfLTQtFtYlsQu2pxPsR8vIZmc2K03QDtiXyRiBbbHGuZ7eG9CqDNXFedn4qt1PANErWsKryhMOXlrJcdZQJamD8jeEw0UskereOu9UaqLYAEnrIbQzD5YcsVwMAGcsOj08saEoY59yKrS28gYGc2oT9w4EvB7c53VB5uMVj60jX_6mgK9_XQ_L0uaPIiZjYkpdYikHC9ayTMshpoaVoIxcLTLrgfMQ2rae2PlpOpKn9PilbkSUzi5JLDjd3Rc0uOPzAbuCVbQSZ8rK93_BxhEszWEro7WDM_iID2QBIugA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید کلاینت ZedSecure از طریق گوگل‌پلی در دسترس قرار گرفت.
در بروزرسانی جدید این‌برنامه پشتیبانی از پروتکل DNSTT اضافه شده، هسته ایکس‌ری رو بروزرسانی کردن، بخش تنظیمات تکمیل‌تر شده و یک‌سری از مشکلات برطرف شدن.
👉
play.google.com/store/apps/details?id=com.zedsecure.vpn
💡
t.me/PersianGithubMirror/4496
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2293" target="_blank">📅 17:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2292">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">۷۰ روز است که جمهوری اسلامی با قطع سراسری اینترنت، میلیون‌ها انسان را عملاً گروگان گرفته است.
این یک اختلال اینترنتی نیست؛ حمله‌ای مستقیم به زندگی مردم است. کسب‌وکارها نابود شده‌اند، معیشت خانواده‌ها آسیب دیده و ارتباط مردم با جهان قطع شده است.
در سایه همین خاموشی، بازداشت، سرکوب و اعدام ادامه دارد؛ بی‌آنکه صدای قربانیان شنیده شود.
اما بخش بزرگی از جامعه جهانی همچنان ترجیح می‌دهد چشمش را بر این فجایع ببندد؛ چون واکنش نشان دادن هزینه دارد و سکوت، ساده‌تر است.
For 70 days, the Islamic Republic has effectively held millions of people hostage through a nationwide internet shutdown.
This is not an internet disruption; it is a direct attack on people’s lives. Businesses have been destroyed, families’ livelihoods have been harmed, and people’s connection to the world has been cut off.
Under the cover of this blackout, arrests, repression, and executions continue while the voices of the victims go unheard.
Yet a large part of the international community still chooses to turn a blind eye to these atrocities, because taking a stand comes with a cost — and silence is easier.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2292" target="_blank">📅 16:29 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2291">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">قطع طولانی اینترنت تحقیر اکثریت بزرگی از افراد کشور، یک‌جا و باهم است. اما این بین، گروهی که شغلشان به‌هرشکل به اینترنت وابسته است، تحقیری عمیقتر و نفس‌گیرتر را تجربه می‌کنند. با آن‌ها طوری رفتار شده که گویا شغلشان "مهم" نيست. حرمت ندارند و می‌شود با زندگی‌، زحمات، اهداف، آینده و برنامه‌هایشان بازی کرد.
©
DevYara
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2291" target="_blank">📅 16:19 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2289">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بر اساس گزارش جاب‌ویژن با عنوان "تاثیر جنگ بر بازار کار"، محدودیت در دسترسی به ابزارهای اینترنتی موجب اختلال یا کاهش فعالیت در بخش قابل توجهی از گروه‌های شغلی وابسته به اینترنت شده و بیشترین کاهش فرصت‌های شغلی در گروه شغلی دیجیتال مارکتینگ و سئو (۸۳ درصد)، طراحی گرافیک (۸۲ درصد) و ترجمه و تولید محتوا (۷۹ درصد) ثبت شده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2289" target="_blank">📅 12:07 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2288">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Euy5o1Bevw2BFf74DMxqzpV4JbQsyXjdf3fbNlynp2KrYeG2sEbPggnJqku4G_m614DX16AZgj_ttOBOR_Wsamr3lDsYiC5tpOQlI21kgZYwUxLR3ElnxA8r6mzCRChFF_3CSWr20_2XjvqEb2Vhj30CyMmoT5eR63koo4ATWnZ8EgYYCTvBSBn7wuoQXlL0KEKAUesDaD5gs2UKXlOPKZ30p8EjPPE7qMFq-0dPfjK-OzH0cvBRmaG6x7wi6feVrSVogJlxRB1wXKuWf0VCJHnDEa9AJw3r7thT3_SwbCq9hn7rTLzAPSsAIOXncVLE3mEoFwZ0Ze6IWNtGotZJvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقایی شاکی است که چرا با وجود اینکه که پول داده، تیک آبی اکانتش حذف شده و ...
در همین حال میلیون‌ها ایرانی پول اینترنت دادند، اما بیش از دو ماه است که یک شبکه داخلی که فاصله زیادی با مفهوم اینترنت دارد بهشون تحویل داده میشه و از دسترسی به هزاران سایت و سرویس محروم شدند. سانسور اینه!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/ircfspace/2288" target="_blank">📅 12:02 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2287">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">وحید فرید، کارشناس اینترنت گفت: ما تجربه قطعی اینترنت را در دولت‌هایی داشتیم که به ظاهر حامی اینترنت بودند. خود پروژه شبکه ملی اطلاعات یک قدم به سمت ناامنی دیجیتال است. کسب‌وکاری که اینترنت می‌گیرد از نظر مردم رانتی است و روی حقوق مردم پا گذاشته. حاکمیت با قطع اینترنت به جامعه سیگنال ناامنی می‌دهد. /کارزار
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2287" target="_blank">📅 11:58 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2286">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سمیه توحیدلو، عضو انجمن جامعه‌شناسی ایران، قطع اینترنت را از منظر اجتماعی خطرناک توصیف کرد و گفت: در زمینه قطع اینترنت حاکمیت هزینه-فایده انجام نداده و متوجه نیست چه میزان خشم تولید می‌کند. آنچه در این وضعیت تشدید می‌شود، شکاف دیجیتال و محرومیت نسبی و شکاف حاکمیت-ملت است. /کارزار
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/ircfspace/2286" target="_blank">📅 11:37 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2285">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aaAOyg_5YdfqXQdluGAYcYFTJvaYBAYsF4jyA0znFkIvbg8MD-j2bglSVT-rebYdLJW5aAUWQVS_xU56xWXVvfGlc6uTZJWJctt1FIqPfDsQv4ED9F6CM2e6OTuzzaYCYqAqVJDyYzDTCsDVMiUeJRAhYKqkX9Z1HkNTruBVP2mJkcFHeZbMA9_dh4wMd0wOoLgvF-wfmvhDDtOawbVhb6pv-Tg1NqdiGz99WJzdQmEgOe6iXqDn1XLpe0CcDBJCvp5tNcb3cNjqnIq_Mi5ZFUqbgyAwL4HmG0b0MhgeZIxCO1BRMYDpR9MhLxncsSDM3z19MqVYW_ChGudYKdkvCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای شرایط فعلی اینترنت ایران که روش‌های عمومی دورزدن فیلترینگ عملاً کارایی ندارن و اسکمرها و کلاهبردارها زیاد شدن، مدتیه یه مارکت‌پلیس برای خرید و فروش کانفیگ راه‌اندازی شده تا خریدارها و فروشنده‌ها در یک بستر متمرکز و نسبتا شفاف با هم ارتباط بگیرن.
طبق توضیح تیم دیفیکس، خودشون فروشنده نیستن و تمرکزشون همچنان روی ارائه و توسعه سرویس رایگانه. این بخش صرفاً برای وصل کردن فروشنده‌ها و خریدارها از طریق این فیلترشکن و حذف واسطه‌ها ایجاد شده و فعلاً هم برای تراکنش‌های رمزارزی مرتبط با ایران کارمزدی دریافت نمیشه.
در این سیستم، مبلغ پرداختی نگه داشته میشه و برای مدتی بعد از تحویل آزاد میشه، کاربران میتونن به فروشنده‌ها امتیاز بدن و تجربشون رو ثبت کنن و کانفیگ‌ها هم بصورت رمزنگاری‌شده تحویل داده میشن. البته محدودیت‌ها خرید بصورت رمزارز رو دشوار کرده، اما افراد خارج از کشور میتونن برای خانواده یا آشنایانشون داخل ایران خرید انجام بدن و فایل کانفیگ رو براشون بفرستن.
👉
market.defyxvpn.com
💡
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2285" target="_blank">📅 11:26 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2284">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=kSWJ9ThLi5AkFEOHP5m6EVRtdkIcexN8ybH-dQrI96xfiPbsZJQGEj_bzgEawVc1tENM8qN4pJMz-kayaovSWhcsUH8DSTvUUeJiWt7G-TXxVdToFgDbTEU3NWyVLNAbmPGdmoJNrPE4PhwLzHj37-Xil9ZuuAklU74bVpyVMOCNuYuaB6T0jkEIDlqxmaX_G5SubSfZ85x3umMCQSwdJTW4KgFacY-ejGTg_T_2voXIhxTk3GaVYE-u77OKoB9bYPTybBHSOgr4VYwuvT6ZW4oJXkFFnYtbuXxqvrsPc4YZaBqHbLb9bkGqjsMZDmsxiv5jT2OTAocwMx1gKdHiCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=kSWJ9ThLi5AkFEOHP5m6EVRtdkIcexN8ybH-dQrI96xfiPbsZJQGEj_bzgEawVc1tENM8qN4pJMz-kayaovSWhcsUH8DSTvUUeJiWt7G-TXxVdToFgDbTEU3NWyVLNAbmPGdmoJNrPE4PhwLzHj37-Xil9ZuuAklU74bVpyVMOCNuYuaB6T0jkEIDlqxmaX_G5SubSfZ85x3umMCQSwdJTW4KgFacY-ejGTg_T_2voXIhxTk3GaVYE-u77OKoB9bYPTybBHSOgr4VYwuvT6ZW4oJXkFFnYtbuXxqvrsPc4YZaBqHbLb9bkGqjsMZDmsxiv5jT2OTAocwMx1gKdHiCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبقه اشراف و طبقه رعایا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2284" target="_blank">📅 11:01 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2283">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وارد روز شصت‌ونهم شدیم. میلیون‌ها نفر رو با قطع سراسری اینترنت گروگان گرفتن و بازداشت‌ها و اعدام‌ها در سایه خاموشی دیجیتال ادامه داره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2283" target="_blank">📅 08:16 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2282">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g2ZWgiMbPYRWSwGoRhK8zK1H9Kv5yMl-XW7fZ3BsGGSCiaDjXDpP4P_mPryU2SR7lm4C6LuLlsfqRpkG5QiIa3wpdaRdgjB_TJZEHw8LoL0ibCJ4rKOuBU9bhI-PICCx5h8krqvrtORcxcfSiEPkzCnaGoa4Jlw1IFvUen37yGtbdVSieprk5XrcKSdMneAc1hlY1Mtoy0FWB2IgyV8Px8lweWKe9zH2ZiPjx3fqG-44Ti3EA8QPZveciC8usQial7UlBjEdjUNlZQzGkcErdTEWijd84FIM9dSBruBa4kvr93zQz9_2JIQyQhM6Hdl5bo9GTWCKyLIxQ3eYPc2t6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آپدیت جدید از اپ theFeed امکان فراخوانی محتوای کانال‌های عمومی دلخواه فراهم شده و پشتیبانی از اندرویدهای قدیمی‌تر، حل مشکل رندر نکردن نظرسنجی‌ها و ...، بخشی از تغییرات جدید هستن.
👉
github.com/sartoopjj/thefeed/releases/latest
💡
t.me/PersianGithubMirror/4273
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2282" target="_blank">📅 18:20 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2281">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ejH_WQowZwDbA9Oq3d6p0fMgpkAwf4xnjjhEP6ADD0Wb2tXP_ISfDQL2tfKVVUZLvAiGU8RzpZRm7aUdDj1OtzMPz1epKEZap0zxAiyuJcr7mG0SyP9HhNbK1VpC4g6_Gur5voF5NVrsuugUxcrqlScEFax7GsS7sOiGSxuJGExYhHFK4lzSjRwTf5GU4c8yfkazS5gORBmwS9vWizovYquvl26usB6q7sS-sFX0wCMLZbOEuyfBS1wISc4ES9wbYG8VeUGmsWuOcJeIPMbnJyOWLwUVQTPlWqPCJyJMV2abdsC5YgdO6-ekN-kmWIWCpfVeRWZ38lQsux92ZMvHhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای آسیب پذیری اخیر کرنل (
Copy Fail
) فارغ از اینکه آسیب پذیر هستید یا نه، آپدیت کردید یا نه و کدوم لینوکس و چه ورژنی هستید، همین دوتا دستور رو واسه محکم کاری بزنید و تمام:
echo "install algif_aead /bin/false" > /etc/modprobe.d/disable-algif.conf
rmmod algif_aead 2>/dev/null
ریبوت لازم نداره، ضرری هم نداره؛ چون به صورت معمول شما به این ماژول کرنل نیازی ندارید.
©
tiosus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2281" target="_blank">📅 18:11 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2280">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">قطع اینترنت به بهانه امنیت ادعای مزخرفی است.
پشت پرده اینترنت پرو و سود حاصل از این رانت در جیب “ستاداجرایی فرمان امام” و “بنیاد تعاون سپاه” می‌رود.
حدود ۹۰٪ سهام همراه اول در اختیار شرکت مخابرات ایران است و مهم‌ترین سهام‌دار مخابرات هم “کنسرسیوم اعتماد مبین” است. این کنسرسیوم متشکل از “گروه توسعه اقتصادی تدبیر” وابسته به ستاد اجرایی فرمان امام و “شرکت سرمایه‌گذاری مهر اقتصاد ایرانیان” وابسته بنیاد تعاون سپاه است.
در واقع گردانندگان اصلی این مجموعه و به نوعی مخابرات و همراه اول دو نهاد ستاد اجرایی فرمان امام و بنیاد تعاون سپاه هستند.
©
yasharsoltani
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2280" target="_blank">📅 09:22 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2279">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">۶۸ روزه اینترنت بصورت سراسری قطع شده و در همین تاریکی دیجیتال، بازداشت‌ها و اعدام‌ها ادامه دارن.
قطع اینترنت فقط خاموش کردن ارتباط نیست؛ پنهان کردن حقیقته، اما خون با هیچی پاک نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2279" target="_blank">📅 08:21 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2278">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XOrO-c0nuLiahAiwDF36noKEVXS0tNYdw032pTWUEidO7TQ0b0UASv83J2jwIB5HS-wdXeWZFcRrG0C7AO2dalNoueWxeg-EoNODZZtiiKumff0fJRQC2OXLASVQQ7qhdudq33J_7fRo50yfR_z7UBRlOV3cK--BCH-ekcoBc91GXzjQnHY2YrBVsLsn2aXKpmCqdJiKh3zXDgU6jPOiF7cOwl43UcrshNEc0NUFimk0fw01YrVCuXbdO5B1VT4X094Xpr9IYDnP9DzNGXJF8gigefjT2XAQtUwUjZD_xp-Qd8GY36ynfCR6Tn6z7h0nvCe-BFdUd798lg9von30BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۲ از اپ متن‌باز و رایگان TeleMirror برای دریافت آخرین مطالب کانال‌های تلگرام در شرایط محدودیت شدید اینترنت منتشر شد.
در این‌نسخه بیلد لینوکس و مک هم در کنار ویندوز اضافه شده، برنامه چندزبانه شده و یه سری از مشکلات برطرف شدن.
این برنامه فیلترشکن نیست و به وایت‌لیست فعلی اینترنت متکیه، بنابراین ممکنه روی یکسری از اینترنت‌ها کار نکنه.
👉
github.com/ircfspace/teleMirror/releases/latest
💡
t.me/PersianGithubMirror/4295
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2278" target="_blank">📅 20:49 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2277">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uOLgwvmMae3H3dGomaj_ZKEf4LvWswiL8deZq1OLd6z4nkjfZu_zMFr3lMTKIuO4CO2xOtNPzlg93TrRNTVnVJ41WRaNdAFCsyGt6tupxRTVWQHehMrv6dYY-bNm05-ZDEBYuLgSIl8vjm35-ogHH2sAiTXj3wfP41oA9CeTocOwjv7bjH9eHHywxOGhtJLYboeyTScg742_7m6FGFine3kPhv46gPQbLLV7IIlYxmJNci0wRq8zfV89HUHLJaoM78_WH_qjtVxdmFuRzOL5NjZf9eN4K5oB0H-FW5tBTPWVVMRBnfhHba3SQS2Ukv4MhgAh_qY-mbArtfMq14xWgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک آسیب‌پذیری بسیار خطرناک در هسته لینوکس با نام Copy Fail (CVE-2026-31431) شناسایی شده، که به کاربر عادی (حتی بدون دسترسی sudo) اجازه میده تا کد مخرب رو مستقیماً در حافظه (RAM) فایل‌های سیستمی تزریق کنه، بدون اینکه تغییری روی دیسک ثبت بشه؛ به همین دلیل بسیاری از ابزارهای امنیتی قادر به شناسایی اون نیستن.
این حمله به سادگی و با پایداری بالا اجرا میشه، میتونه برای فرار از کانتینرها (Docker / Kubernetes) استفاده بشه و تقریباً تمام نسخه‌های لینوکس از سال ۲۰۱۷ به بعد (Kernel 4.14+) رو تحت تأثیر قرار میده.
اگرچه با توجه به وضعیت فعلی اینترنت در ایران بروزرسانی کار دشواری هست، اما توصیه میشه در سریعترین زمان ممکن سیستم خودتون بروزرسانی کرده و وصله‌های امنیتی هسته رو نصب کنین.
©
Bamdad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2277" target="_blank">📅 17:02 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2276">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KJ_bVSzrg4V8kcOg9_CYmBoHXEimNkWsowSz6z2ZcJ-I9Z6Oxco7Xlg9tJDCpOAl5pB2TDunetj2qBi1wgLuFQ_MvPA8lcUjLO5phMWKlhoZjqNc9ziK3DIInJ8tkBLR3o7uWScc_gfjF0IrUNj0VxNa1JH7r1vLaaC1v3IXZO09i8qSkS86Itad3oPXMH1oN36oLkZlcQlO1L7jR_RYfPqMeOtty_OxzjCsZ1SsXm0bCbHlBnO7inxJd6FisTc4EayXsBryTeIQnhNJj62MfCDL4Hos9Wg3mjMD6myzDtcXRrd5lNwTXe5rziMhY3dYkEIJCUzCcfi_JZs11D00fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل آموزش ساخت فیلترشکن شخصی به کمک گوگل و کلودفلر از طریق متد MHR-CFW منتشر شد. اخیرا یک کاربر فورک جدیدی از این پروژه رو به زبان GO بازنویسی کرده که مشکل سرعت پایین، لود نشدن برخی از ویدئوهای یوتیوب و همینطور یکسری از خطاهارو برطرف کرده.
👉
github.com/ThisIsDara/mhr-cfw-go
💡
t.me/ircfspace/2259
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2276" target="_blank">📅 16:49 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2275">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">توی خبرها دیدم که دستیار ویژه وزیر کشور گفته "محدودیت‌های اینترنت احتمالا تا ۴۵ روز دیگه رفع میشن"؛ بنابراین بنظر میرسه باید خودمون رو برای کابوس ۱۱۰ روز قطع اینترنت آماده کنیم!
😐
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2275" target="_blank">📅 16:42 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2274">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hT6troMWCSmB8BGNxj6r2Exh3CntduS8HBl28c9POl1-9wPLtPw_WenE1Ayfri1POrtKdjsJn7SRcDGmy-rkgKgl9XQfFxBWOAJthJraw3gmoX-hQecReNYZr0V5Js5YdeNq7_58IXNfbrhYKYF9EmKPqhMLFBPN9NT1GyZkisBCH1yfXVIUYA6rcXJUhwuqeJPrHENYSXGQKUVlXALfgUCi6_buPeEpRupa7KNUsn7k4uwZ5aw81Qsk65mrYTkMVoHECQCJ9YcGoD2xdlgohFerprSceDlae-qOlySqgXGEJqGNfYOsNk-_mwhPhEuWY9UuXtq56VQSh4mbX-jBpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز خبری در رابطه با قطع اینترنت سفید خبرنگاران توسط ایرانسل منتشر شد، که روابط عمومی این اپراتور گفته نقشی در این ماجرا نداشته و "هرگونه قطع احتمالی دسترسی متفاوت برخی کاربران به اینترنت، لازم است از نهادهای تصمیم‌گیر پیگیری شود".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2274" target="_blank">📅 16:38 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2273">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vbAK-zG080yctNQgKGjqwSmyGzt_285H7UPNa6Vym0J76ZS-VVauLMHTAFmiHwy3TZ1RbKV3KwSQBaKuWLoBah_eXXnZfi1Je5pNGXtpgJonYxx8BgwH0j-QFYO1A69tmlypeUG_yz5seiSti-YftpJqwmIorrykUy4iAusyl3JBMEcpOefhMHv-LURRJXxTneDMKbM01wtf8YYGMVMwWVGiurwfbpAtHHBJvSM55UHAyVtgnUWBJJl_piysREmV0Ng1EtlSxQD2mByUqVKNW90cUXdC9icb-Pd9peMTSCgYR4Yt8Qdt2OQ8kL91W1m3SBF6esUhKkzvoX-ulzJS-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع اینترنت در ایران اکنون وارد روز ۶۷م شده است. اقدام به سانسور دیجیتال، پرده‌ای از سکوت بر افزایش گزارش‌ها از اعدام‌ها می‌افکند و قربانیان را از دیده‌شدن، پاسخ‌گویی و حق ابتدایی شنیده‌شدن محروم می‌کند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2273" target="_blank">📅 12:26 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2272">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">توسعه‌دهنده اپ SlipNet متاسفانه از توقف توسعه این اپ کاربردی خبر داده و در بخشی از توضیحاتش در مورد علت این تصمیم، نوشته که "توسعه ابزار آزاد، رایگان است اما بی‌هزینه نیست. متأسفانه در جامعه نرم‌افزاری ما، فرهنگ Donation هنوز جایگاه خود را پیدا نکرده است. از سوی دیگر، جنگیدن همزمان در دو جبهه (فیلترینگ از یک سو و خشم و کامنت‌های تند برخی کاربران در روزهای اختلال شبکه از سوی دیگر) توان ادامه مسیر را از من سلب کرد".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2272" target="_blank">📅 12:22 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2271">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کاربران میگن ابلاغیه‌های مشابهی رو از قوه قضائیه با موضوع "پرداخت وجه و تسویه اقساط"
دریافت کردن
، که توسط "نوآوران پرداخت مجازی ایرانیان"، یعنی نام تجاری دیجی‌پی (زیرمجموعه دیجی‌کالا) ارسال شده.
با توجه به اینکه ثبت اظهارنامه آنلاین از طریق سامانه عدل‌ایران امکان پذیره، احتمالا تعداد نفراتی که پیام‌های مشابهی گرفتن اندک نباشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2271" target="_blank">📅 22:24 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2269">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pvnLdk5BeyAZ83kWjIJBKJPcnuSUVICpFQ3BdhUQxs-DlBpFAEFFm-0zUo4L_0BT9Dkv-5yHsInXRh_NK70o7LqdzOOqOEDIBb4Y8m8bIe_QBTOfHnK80P1N4V4Kr6m7ckq59Clny50KFNRIBfYu2oCTaYMXVOPOlyuBl3AmxJyH8VHv_W042Ut8KUHNw73h1yW81cQeTPf7Nm0XsNt0dhUGNXi0mnwRFUwRJ4Pufe8EIKnSbj7n8LEcC4oc6qmipWr4QU59ahlZoXXrzyHh18K0uvcCT5ntYGYjf1SaRywGhaj8KWXLAn7WL1WvoFt0FV5iPCRC7RGjBLDU32pAcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبری که امروز در مورد "ثبت رکورد ژاپن در رابطه با سرعت اینترنت" در صفحات مختلف منتشر شده، مربوط به حدود ۹ ماه قبل هست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2269" target="_blank">📅 22:15 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2268">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pG7ZiczWK35yIJxBclddH7Yay8-_zTjR3iQOXUDVj07dKre0u0sSHXvdPYSbA1zJOD4HfhCeXrCHL6NM_OOm1QAlb6XWkvbIj_KwhZmIErLCTUU3DN5l0xx_OWQ4KwTVWybYcF-74jfiOvHY0jO-sitRR45rIe2cO9xdZVxoY4A00qfJTbAE0wH6csaFk7CrSxYeo83dDHAHfLDra4LQQrLTYY7Iqp64-1BR9C4qI2ffEJeZCCRjHL1C6Vj4qP4cnGkfygs9sip--iDkx1i-a-MHjXVNrQZASvDf_cKopR78FGUfSThJLbEjVsC8sR62OP5sEZgPxnIjTcFBMua9-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیجی‌کالا خیلی اوقات در رابطه با خسارت‌هایی که بصورت مستقیم و غیرمستقیم به مشتریان و تامین‌کنندگان وارد میکنه پاسخگو نیست، اما در شرایط جنگی از طرف سرویس دیجی‌پی بخاطر ۲۰ روز تاخیر در پرداخت قسط اظهارنامه قضائی میفرسته؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2268" target="_blank">📅 21:57 · 14 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
