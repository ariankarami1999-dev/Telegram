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
<img src="https://cdn4.telesco.pe/file/dY4l4vfx1LLu86P3nolCTfId0RMjPQY1OecpXgfFa8f5Sld6U8_COjqmUDbFvYDMFRP4_qZZUKSY6GnW2WQKeim2Moutqvb31FmqyJx53pmZ2I1wm1AcR9oZbZ5F7Rnqdy4g_tv2nREA3R2i1pY2wzKSnID-U4LRA48Ee2BTNPi4uDRQXBz-zGVupQ7si20tHoVwrpwjnVFvQo6Cbu_yTcMO5q7uGNOxo7W4NNFMtYgh3Jt-6eqcNRIUuc3Fd72F037XHMUduokEQwIQPJvHbJ0iJUxmV0WnectyNnmxIUuiVcZX4CDIHriLsk7tEW_F66lEZpujVttJDeoFpdECKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 443K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 17:53:49</div>
<hr>

<div class="tg-post" id="msg-20346">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فقط خدا رو ببین
🙌🏾
🤣</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/withyashar/20346" target="_blank">📅 17:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20345">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">شستشوی مغزی Brainwash چگونه انجام میشود بدون آنکه متوجه باشید
@WarRoom</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/withyashar/20345" target="_blank">📅 17:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20344">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">میدل ایست نیوز: دقایقی پیش اسرائیل با استفاده از پهپاد چند حمله به بلندی‌های‌ علی الطاهر در جنوب لبنان انجام داد.
@WarRoom</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/withyashar/20344" target="_blank">📅 17:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20343">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نیویورک پست : انقلاب در ایران ممکن است «هر لحظه» رخ دهد؛ رهبران اعتراضات در تلاش برای مسلح شدن هستند!
@WarRoom</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/20343" target="_blank">📅 16:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20342">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">صدای انفجار در‌ پارچین کنترل شده است و اعلام شده بود
@WarRoom
⚠️</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/20342" target="_blank">📅 15:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20341">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlejandro Sosa</strong></div>
<div class="tg-text">هی میت ، داداش یاشار گلم چطوری من نگاهی به چنل های ۶۰۰-۷۰۰کی حتی ندارم رفتم بالای ده تا چنل میلیونی رو هم چک کردم، نه به اندازه شما ویو دارن نه مطلب و تحلیل مفید ، همشون فیکن!!! فقط یک خواهش دارم به عنوان برادرت در غربت… حرف آدمهای آشغال رو گوش نکن، همینطور برو جلو و همه رو به یک چشم نبین ما تا آخر با شما هستیم یادت نره تبلیغات منفی بهترین تبلیغاته برای شماست چون میان و حقیقت رو میبینند</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/20341" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20340">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تتر : ۱۹۵،۶۰۰ رکورد جدید تاریخی @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/20340" target="_blank">📅 15:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20339">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">آژیر خطر  حمله موشکی پهپادی در اردن به صدا در آمد
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/20339" target="_blank">📅 15:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20338">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فقط همین کامنت را لایک کنید و با نگهداشتن روی آن، اد تو استوری و کارهای اداری دیگر را انجام دهید.
https://www.instagram.com/p/DbiPnCyMgQw/?carousel_share_child_media_id=3954792076531598384_1638317016&comment_id=18015084023866564
ترجمه کامنتم برای بیبی نتانیاهو :
آقای نخست‌وزیر، بی‌بی عزیزِ جانم،
این رژیم فراتر از اصلاح‌پذیری است؛ شما این را بهتر از هر کسی می‌دانید. هرگونه معامله با آن، فقط خون کسانی را که کشته شدند می‌شوید و آینده نسل جوان ایران را قربانی می‌کند. یک عملیات سریع، قدرتمند، غافلگیرکننده و از هر جهت می‌توانست به این موضوع پایان دهد. اگر اقدام قاطع در ۴۰ روز اول انجام می‌شد، رژیم می‌توانست ظرف دو هفته سقوط کند؛ آنها در حال فرار بودند. لطفاً رهبری این کار را خودتان بر عهده بگیرید. شما این واقعیت را بهتر از هر کسی می‌دانید.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20338" target="_blank">📅 14:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20337">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">رژیم ایران ایلان ماسک را به فهرست اهداف خود اضافه کرده و ادعا می‌کند اطلاعاتی به دست آورده که ثابت می‌کند سیستم‌های پیشرفته ردیابی ماهواره‌ای و شبکه‌های ارتباطی رمزگذاری شده ماسک مستقیماً توسط نیروهای اسرائیلی برای یافتن و از بین بردن آیت‌الله علی خامنه‌ای، رهبر سابق ایران، در جریان حملات هوایی دقیق اوایل امسال مورد استفاده قرار گرفته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20337" target="_blank">📅 14:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20336">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کانال 12: تا زمان خلع سلاح حماس، اسرائیل حملات خود به غزه را متوقف نخواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20336" target="_blank">📅 13:18 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20335">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه،با تکذیب خبر بازگشایی تنگه به نقل از منبع آگاه، در واکنش به گزارش کانال ۱۲ اسرائیل درباره موافقت عباس عراقچی، وزیر امور خارجه، با طرح بازگشایی تنگه هرمز، نوشت: «هیچ توافقی درباره بازگشایی تنگه هرمز وجود ندارد و اخبار منتشرشده در این باره کذب است.»
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20335" target="_blank">📅 13:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20334">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رسانه های رژیم : سرلشگر غلامرضا رضاییان رئیس سازمان اطلاعات فراجا ملقب به «ابوسجاد» به جای سردار رادان فرمانده کل انتظامی در جلسه شورای دفاع نهم اسفندماه شرکت کرد و کشته شد
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20334" target="_blank">📅 12:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20333">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تتر ۱۸۹،۰۰۰ تومان و همینجور داره میاد  پایین
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20333" target="_blank">📅 11:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20331">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">میدل ایست آی:ترامپ از اسرائیل خواسته به حملات علیه ایران بپیونده و یه لایه دیگه از فرماندهان و رهبران ایران رو هدف قرار بده
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20331" target="_blank">📅 11:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20330">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20330" target="_blank">📅 11:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20329">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20329" target="_blank">📅 11:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20328">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سرپرست وزارت دفاع ایران: اظهارات آمریکایی‌ها بخشی از یک جنگ روانی است و ما به هر تهدیدی به عنوان یک تهدید واقعی نگاه می‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20328" target="_blank">📅 11:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20327">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خبر ها رو نگاه نکنید ! حمله ناگهانی خواهد بود !  خواهید دید</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20327" target="_blank">📅 11:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20326">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">همشهری: از مجتبی خامنه ای هیچ صدایی منتشر نمیشه؛ چون آمریکا و اسرائیل از روی صدا هم همه چی رو میفهمن و جاشو پیدا میکنن حتی اگر فیلتر استفاده کند، آنها با معکوس کردن آن، از صدا الگوی تنفس و استرس او را متوجه میشوند. فقط ۲ یا ۳ نفر با مجتبی خامنه ای ارتباط دارن. اون احتمالا توی کوه های قم یا تهران مخفی شده.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20326" target="_blank">📅 11:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20325">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">در همین لحظه پل هوایی سنگین جهانی ، از آمریکا تا خاورمیانه.، شش سوخترسان که حتما هواپیماهای جنگنده جدیدی را از آمریکا به منطقه می آورند و همکنون در حال ورود به آسمان آتلانتیک شمالی هستند. همینطور هواپیماهای لاجستیکی سی-17 در سرتاسر این مسیر دیده میشود. @WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20325" target="_blank">📅 11:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20324">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کانال ۱۲ اسرائیلی: وزیر امور خارجه ایران شب گذشته با یک توافق میانی بین قطر و آمریکا برای بازگشایی تنگه هرمز موافقت کرد. بر اساس این پیشنهاد، کشتی‌هایی که به سمت کشورهای خلیج فارس حرکت می‌کنند، از آب‌های منطقه‌ای ایران عبور خواهند کرد و از طریق آب‌های عمانی…</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20324" target="_blank">📅 10:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20323">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کانال ۱۲ اسرائیلی: وزیر امور خارجه ایران شب گذشته با یک توافق میانی بین قطر و آمریکا برای بازگشایی تنگه هرمز موافقت کرد.
بر اساس این پیشنهاد، کشتی‌هایی که به سمت کشورهای خلیج فارس حرکت می‌کنند، از آب‌های منطقه‌ای ایران عبور خواهند کرد و از طریق آب‌های عمانی خارج می‌شوند. با این حال، عمان درخواست کرده است که تأییدیه رسمی دریافت کند مبنی بر اینکه سپاه پاسداران انقلاب اسلامی ایران از این توافق حمایت می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20323" target="_blank">📅 10:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20322">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00731102ad.mp4?token=Md7l5VeW3QYTsWMOppp3-ilwMNdNh1pWw_3fIb7uIQusi6Cpy5kq4mybpLZ9H9r9Ks6Eu3yFwHBRcaLzyt3cUtqhmUayLCM5MbV8KRu5qWtb52PA2WDfkcID_PSc8Jdec4VEggatf4Onkg-vFuWU6ev4EXXiqj6bKiw3k4nZUajNj0bduY_BDlOZZLEDM89qFCUEx-0_r7TNn4eQc66tpucZAlDDYl_lgf4U0ghifx4m1m5VKffuHWCs0F2Qrl_E-ZHIY-dpzzhLW5r8Pe9Ss6guVGqldHMEfvnfTTNQfYpkIz_zIOcom1WemS2z1Eb_8-OmHspvZt6C54tQnRDiZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00731102ad.mp4?token=Md7l5VeW3QYTsWMOppp3-ilwMNdNh1pWw_3fIb7uIQusi6Cpy5kq4mybpLZ9H9r9Ks6Eu3yFwHBRcaLzyt3cUtqhmUayLCM5MbV8KRu5qWtb52PA2WDfkcID_PSc8Jdec4VEggatf4Onkg-vFuWU6ev4EXXiqj6bKiw3k4nZUajNj0bduY_BDlOZZLEDM89qFCUEx-0_r7TNn4eQc66tpucZAlDDYl_lgf4U0ghifx4m1m5VKffuHWCs0F2Qrl_E-ZHIY-dpzzhLW5r8Pe9Ss6guVGqldHMEfvnfTTNQfYpkIz_zIOcom1WemS2z1Eb_8-OmHspvZt6C54tQnRDiZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو وزیر امور خارجه : حکومت ایران باید تغییر کند؛ ممکن است سرنگونی رخ ندهد، اما خود حکومت باید تغییر کند؛ آنها می‌خواهند انقلاب را صادر کنند؛ این موضوع حتماً باید تغییر کند
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20322" target="_blank">📅 10:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20321">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خبرگزاری NBC به نقل از مقام‌های آمریکایی گزارش داده که روسیه اطلاعات شنود الکترونیکی و (SIGINT) داده‌های هدف‌یابی شامل محل استقرار، مسیر حرکت و الگوی فعالیت ناوها، هواپیماها و سامانه‌های پدافندی آمریکا در خاورمیانه را در اختیار ایران قرار می‌دهد، این همکاری توان سپاه پاسداران برای رصد نیروهای آمریکایی را افزایش داده و دقت موشک‌های بالستیک و پهپادهای انتحاری ایران را بهبود می‌بخشد، مقام‌های آمریکایی این اقدام را بخشی از گسترش روابط نظامی تهران و مسکو می‌دانند که در آن روسیه در ازای دریافت پهپادها و فناوری تولید آنها از ایران، اطلاعات اطلاعاتی، پشتیبانی فضایی و تجربه مقابله با جنگ الکترونیک غرب را به ایران منتقل می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20321" target="_blank">📅 10:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20320">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">روزنامه وابسته به رژیم ایران ، نیویورک تایمز گزارش داد که هم‌پیمانان آمریکا نسبت به این موضوع که جنگ با ایران به سمت یک شکست راهبردی سوق پیدا کند نگران هستند.
هم‌پیمانان آمریکا می ترسند که ناتوانی در ایجاد تغییری پایدار در ایران، نقطه‌ ضعفی را آشکار کرده باشد که روسیه و چین از آن استقبال خواهند کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20320" target="_blank">📅 10:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20319">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2oX44AxWBmHo7HQ9xVc1t_aCRnkXfcz9asrCteUsWM4DWnf1_dXdF756Z69lTj-2jWDO9CtIEm5jckD43m9wk9tMrZ6C6B_RbkrBDl92Bo_Zry5H0rOE3zgypRqy_efyURMqUB6PnJ2RAg6ONsDEcuG6qBuigSyXmpfidD5-iQK0F8QiSf9qEakw6RNtN4CZDqpEaAVb-qSJHmB6xbsj5vPRgSQEZjcRwdSwT1oSmbuJbiJ1fMZOLn0MPRMepg7BgYcLlmSlKENSa2IsZXJQ5by-AvVGOo9LsRssXrFYeb7FoZG4mC4Mo0N1lOd0D7pFF8w7V0FTRGqLGpZi8SBag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏در جریان مرحله نخست عملیات مرمت دبیرستان تاریخی انوشیروان دادگر تهران، کارشناسان میراث فرهنگی موفق به کشف و نمایان‌سازی یک کتیبه سنگی ارزشمند متعلق به سال ۱۳۲۶ خورشیدی در ایوان جنوبی این بنای تاریخی شدند.
‏این کتیبه اطلاعات ارزشمندی درباره تاریخ ساخت و افتتاح این دبیرستان، یکی از شاخص‌ترین بناهای آموزشی دوره طلایی ایران‌ساز رضا شاه پهلوی ، در خود جای داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20319" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20318">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ایلان ماسک در حال نشان دادن کارخانه تسلا به بنیامین نتانیاهو، نخست وزیر اسرائیل و همسرش
@WarRoom
هم اکنون نتانیاهو به اسرائیل بازگشته است</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20318" target="_blank">📅 09:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20317">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اکسیوس : پیشینه لغو حمله ها ، که همچنین نشان می‌دهد چه کسی (عربستان) این روزها واقعاً بر ترامپ تأثیر می‌گذارد
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20317" target="_blank">📅 09:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20316">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سی‌ان‌ان‌: عربستان به عنوان یک متحد کلیدی آمریکا در خلیج فارس، نفوذ قابل توجهی بر ترامپ دارد
وابستگی دیپلماتیک واشنگتن به ریاض در خاورمیانه، تأثیر زیادی بر تصمیم ترامپ برای عدم حمله به ایران داشت
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20316" target="_blank">📅 09:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20315">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVYcQM9raKhm18h_zui-YRgobEmEJWQ4FZMgKadzlMCwrWjSZhCYFJZOdteZB151ZsSyU4ZJ35sfHw7SndWMXcrsq1dGKl7GeZ_e424-urPlQuKUs9_CvNZBbMlkmOFX7JSfvG_h4fciJHjQm_WEkUq2CQEbOfZF4rwW9e6pVYBzQXTlsCr8B7YeUvp6EZNWkiR-geEjODS8cW8yDy1PyPeX2hSt6mXMNAG8ah6OyvoJA3uNlZBv-rbonNbGz8cAnGhiG3RlKVKVS13eHYk_81J3e7v5CgknkDMCHOIZSUZQ1fsSooyaBRFBHF7nASEaoQxvhKoaHiTyr36OggstcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در ‌تروث: آمریکا مسلح و مجهز آماده حمله به جمهوری اسلامی ایرانه، با سطح وحشتناک نظامی، قدرت و زوری که از جنگ جهانی دوم به این طرف ندیدیم.
با این حال، ایران و چند تا کشور دیگه خاورمیانه ازمون خواستن حمله رو عقب بندازیم چون چارچوب یه توافق رو قبول کردن، این توافق شامل باز شدن فوری، کامل و تمام‌ و کمال تنگه هرمز میشه و تموم شدن تهدید هسته‌ای ایران.
بر اساس این درخواست، من موافقت کردم برای نفع آینده کل دنیا و همچنین بقای یه ایران موفق و آباد، حمله رو لغو کنم، به شرطی که بتونیم سریع یه معامله ببندیم. کشور اسرائیل هم تو این تعهد با من همراهه. همه دست به کار بشید و این توافق رو نهایی کنید.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20315" target="_blank">📅 09:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20314">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فاکس نیوز:رژیم جمهوری اسلامی در واپسین نفس‌های بقا؛ در حالی که آمریکا قلب توان موشکی آن را نشانه گرفته است، سایه فروپاشی بر تهران سنگین‌تر می‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20314" target="_blank">📅 09:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20313">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نتانیاهو : هر کسی که ما را دوست نداشته باشد، آمریکا را هم دوست ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20313" target="_blank">📅 05:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20312">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgTbJMQ8Vht8_t-4axx1py-vahyUffDyIZc4BOx2wmR2PfBuYQo1BNInEoIDl3171uAPs57NSPNLzE9P-dpXOPCIRoVw6UQBesMBBETArYUuqa3GcVEjCfTd-2XFcC3nYi9tTSIRQ2ze58hU0C8yi7ldi1vwZpb2vUqsnL5kKvwRAHkABJNNzjZzV7_DyDrRqyx7MI_1EJnwFZpWczElXdQJ8GDm8wFdWU0hqqM1bJU08BanLvudX_C0S92QzkiMo1XlQZuIdl__EOP815lFn-BB5OnMOkmZIwN-QQ4-it903vOVn6wI_nKU6LnKpNtuDIxduuMgv0NzL1yyIb1YZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین لحظه پل هوایی سنگین جهانی ، از آمریکا تا خاورمیانه.، شش سوخترسان که حتما هواپیماهای جنگنده جدیدی را از آمریکا به منطقه می آورند و همکنون در حال ورود به آسمان آتلانتیک شمالی هستند. همینطور هواپیماهای لاجستیکی سی-17 در سرتاسر این مسیر دیده میشود.
@WarRoom</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/20312" target="_blank">📅 04:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20311">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کانال ۱۴ :
ایران مظنون اصلی حملات سایبری به تأسیسات آب آمریکا؛ رسانه‌ها از احتمال «پرل هاربر مجازی» خبر می‌دهند
حملات سایبری هماهنگ به تأسیسات آب‌رسانی در هفت ایالت آمریکا، نگرانی‌های جدی امنیت ملی را برانگیخته است. در این گزارش ادعا شده اگر نقش ایران به‌طور قطعی ثابت شود، این حملات فراتر از یک حمله سایبری معمولی بوده و مستلزم پاسخ قاطع آمریکا خواهد بود
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20311" target="_blank">📅 04:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20310">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">@WarRoom
😂
❤️‍🩹
🙌🏾</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20310" target="_blank">📅 03:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20309">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">آکسیوس: سایر قدرت‌های منطقه‌ای، از جمله پاکستان، ترکیه، امارات متحده عربی و قطر نیز بر ایالات متحده و ایران فشار وارد می‌کنند تا تنش‌ها را کاهش دهند.
واسطه‌های قطری، جلسات جداگانه‌ای با عباس عراقچی، وزیر امور خارجه ایران، استیو ویتکوف، نماینده ویژه آمریکا، و مقامات عمان برگزار کردند تا به توافقی برای بازگشایی تنگه هرمز دست یابند.
این مذاکرات پیشرفت‌هایی داشتند، اگرچه هنوز مشخص نیست که آیا این پیشرفت‌ها برای حل بحران کافی خواهد بود یا خیر.
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20309" target="_blank">📅 03:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20308">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20308" target="_blank">📅 03:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20307">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohsen</strong></div>
<div class="tg-text">آره یاشار تو کیش همه میگن هیچ باری دیگه از اون سمت نمیاد قراره کلا دریا تخلیه شه</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20307" target="_blank">📅 03:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20306">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مقامات آمریکایی به Axios: ولیعهد سعودی، شاهزاده محمد بن سلمان، روز شنبه با رئیس‌جمهور ترامپ صحبت کرد و نگرانی خود را در مورد برنامه‌هایش برای انجام حملات نظامی گسترده جدید علیه ایران ابراز کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20306" target="_blank">📅 03:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20305">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04c3771c8f.mp4?token=CuZ7dNj2BkdZZvKkTq3j01gNqubBbWtgzanrbKS7yrVIG3Y6obpqlFg7BwpKKDEDXQVeMlCciOl7ZW9s0OyA6cweKgiURM6mlMtmWY6zXI20wv0D5NPBKJWcIOKrM5fEh2PGu80FjhWvV4jxrwWx5idZf5KzdXfcSOUnX14V8TJmcQMS4lkKxf9GIg_XPXUW0FsoJbAKknZCkgfuzELQeLWa8c6MmJgQLZWXENn2KwfD6OMgBmBOw2Iq7j11Hpz-D8TJok_oiGj9kwhnu0BKLpgckritVEIdTbOjtfCb-5HIvxjaJ288A0WrgSSPm-2Dza1r2715pZzWOsMMLqkbRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04c3771c8f.mp4?token=CuZ7dNj2BkdZZvKkTq3j01gNqubBbWtgzanrbKS7yrVIG3Y6obpqlFg7BwpKKDEDXQVeMlCciOl7ZW9s0OyA6cweKgiURM6mlMtmWY6zXI20wv0D5NPBKJWcIOKrM5fEh2PGu80FjhWvV4jxrwWx5idZf5KzdXfcSOUnX14V8TJmcQMS4lkKxf9GIg_XPXUW0FsoJbAKknZCkgfuzELQeLWa8c6MmJgQLZWXENn2KwfD6OMgBmBOw2Iq7j11Hpz-D8TJok_oiGj9kwhnu0BKLpgckritVEIdTbOjtfCb-5HIvxjaJ288A0WrgSSPm-2Dza1r2715pZzWOsMMLqkbRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون فعالیت سیستم دفاع هوایی C-RAM در اربیل عراق برای مقابله با پهپاد های شلیک شده ایران
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/20305" target="_blank">📅 03:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20304">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">قوانین دریایی امروز کشورهای خلیج فارس</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20304" target="_blank">📅 03:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20303">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20303" target="_blank">📅 03:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20302">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گویا لایو از سخنرانی قدیمی‌ بوده</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/20302" target="_blank">📅 02:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20294">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حمله پهپادی سپاه به اربیل عراق @WarRoom</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/withyashar/20294" target="_blank">📅 01:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20293">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">عراقچی گوشی رو گرفته زنگ زده پاکستان ، ترکیه ، عربستان و … نسبت حملات آمریکا هشدار داده
@WarRoom</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/withyashar/20293" target="_blank">📅 01:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20292">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">همکنون هواپیماهای جنگنده اسرائیل حمله‌ای را بر مناطق شمال غربی شهر غزه انجام دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/withyashar/20292" target="_blank">📅 01:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20291">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رویترز : شاهزاده رضا پهلوی : «این وظیفه یک دولت خارجی نیست که تصمیم بگیرد چه کسی یا چه چیزی باید جایگزین حکومت ایران باشد. این به مردم ایران بستگی دارد.»
@WarRoom</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/withyashar/20291" target="_blank">📅 01:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20290">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مارک لوین : رژیم ایران بیش از آمریکا یا اسرائیل از قیام مردم خودش می‌ترسد
@WarRoom</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/withyashar/20290" target="_blank">📅 01:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20289">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حمله پهپادی سپاه به اربیل عراق
@WarRoom</div>
<div class="tg-footer">👁️ 189K · <a href="https://t.me/withyashar/20289" target="_blank">📅 01:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20288">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بیمارستان‌های اسرائیلی وارد حالت بحران و آماده‌باش شده‌اند و پرسنل پزشکی در حالت آماده‌باش قرار دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 194K · <a href="https://t.me/withyashar/20288" target="_blank">📅 01:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20287">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">المیادین:اطلاعاتی وجود داره که تایید میکنه گروه های کُرد دارن توی خاک عراق خودشونو آماده میکنن تا از غرب کشور به ایران حمله کنن
@WarRoom</div>
<div class="tg-footer">👁️ 199K · <a href="https://t.me/withyashar/20287" target="_blank">📅 01:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20286">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کان نیوز: نیروی هوایی اسرائیل در آماده باش 100 درصدی جهت حمله به ایرانه.
@WarRoom</div>
<div class="tg-footer">👁️ 199K · <a href="https://t.me/withyashar/20286" target="_blank">📅 01:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20285">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کانال ۱۳ اسرائیل : ترامپ تصمیم به حمله گرفته و این حملات انجام می‌شه مگر اینکه ایران لحظه آخر همه‌رو سورپرایز کنه و بیاد پای میز‌مذاکره
@WarRoom</div>
<div class="tg-footer">👁️ 192K · <a href="https://t.me/withyashar/20285" target="_blank">📅 00:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20284">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">حساب رسمی X اسرائیل:
ما از امپراتوری‌ها جان سالم به در برده‌ایم. می‌توانیم از بخش نظرات شبکه های مجازی هم جان سالم به در ببریم.
@WarRoom</div>
<div class="tg-footer">👁️ 204K · <a href="https://t.me/withyashar/20284" target="_blank">📅 22:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20283">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کانال ۱۴ : اسرائیل آلارم خطر نظامی را افزایش داد
مقامات ارزیابی می‌کنند که حمله گسترده ایالات متحده به ایران قریب‌الوقوع است.
@WarRoom</div>
<div class="tg-footer">👁️ 203K · <a href="https://t.me/withyashar/20283" target="_blank">📅 22:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20282">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تتر : ۱۹۵،۶۰۰ رکورد جدید تاریخی
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 205K · <a href="https://t.me/withyashar/20282" target="_blank">📅 22:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20281">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">این خبر فیکه یه چنل برای تبلیغات گمراه کننده زده همه کپی کردن
نتانیاهو: اسرائیل به زودی به همراه آمریکا دروازه‌های جهنم را برای آنها باز خواهد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 201K · <a href="https://t.me/withyashar/20281" target="_blank">📅 22:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20280">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fABh0Qpt3ee1XUkULR0U2OqLoEUd95L2gZ2FsVdnvA9rkUAJgwT_rdwTMZ35tvt0Z3yuOvGFq48U7_TwXoCojDiDDZTFXDG_Rf4Oc8Qk0cHBloK3UeHcRGiO4PSaKnOvLBJ3NdTtVxp5v14fsx-k1WEJpIBwfVWqk8ixoPSAndVGp22UDOZvbYOldbGOKGPrC4n3q-_zOARnNe8V1RE9O5ixg3NhL8sv4fWpQWln_Z4HxbtXuP5pVDUz8xRdL57ml0ZHHBob5Ha2XmkziqONGgDvH1zjUdwzfAW7LwnhktANLoN58_S2kFY0WIBZHCLGyAms7Q1C_iakgWqvR7kdPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ در‌تروث : در حال نابودی کامل ارزش پول ایران هستم. در شروع دوران ریاست جمهوری من دلار ۹۰ هزار تومن بوده؛ الان شده ۱۹۰ هزار تومن.
@WarRoom</div>
<div class="tg-footer">👁️ 200K · <a href="https://t.me/withyashar/20280" target="_blank">📅 21:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20279">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEsU6GxDoHjqvWd3o8koeFajvxr32a82V8xRC8T-bNmrjCJYTrovrqYyrGoOA5siwF9E3upFPu9I-W9r1QYNMuzmc0J5qIxPuHVFk-a0QXUyQuQPIOnWImgWmMfqD-ve-Y66Q7gtDJHeNuA-nOjdI9rFVspwMAX1GAS-5jSpj-Ay-zaBX7PKZhby0QnpVePeKf6DipgY2rjPL7yTbFW20YGiCqn431NTK7bwuJGEG3S3A6DqNc-nQ2AlEWpPFxvsSHJhuBpRS4zDFhMQzDVrfNYX10NMft09I4MesezShJZ8Nd4UgibGuuChFvxHCZN5wi2E5GMeZ2aFHEtmjSucUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما آدام فضایی را به مقام انسانیت می‌رسانیم
@WarRoom</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/withyashar/20279" target="_blank">📅 21:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20278">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کانال ۱۳  به نقل از مقام‌های ارشد:
انتظار می‌رود ترامپ دستور ازسرگیری درگیری‌ها را صادر کند و آن‌ها ساعات آینده را “بسیار سخت و بحرانی” توصیف می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/withyashar/20278" target="_blank">📅 21:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20277">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/844f298602.mp4?token=seJO8LRUxXQKGsh4jYc0NUNEsfgxVAYvBTUJm3IGzdznLhGIWWzeE-pZ32kz0YkZZoRirnS8Gsv-zSWhBDpQuuuTyJFic5iRTu50zxiYN0DVfKkL1lIRnOoXEh2cPpsreBnfS3EfA-OFninIyTeVcHu8eW4zMPCZQUTXCC6TFQmGu8HZzqeaF5T_C35PrZJEzRDshVkihWICAyotW29g1hyucIBCYjT5GO1zSMp2JPJWPS0PXRKtfTK4_ibOeA--5G5oNPxkhgO9PgyCmIc5KLY6xzpoSRTuL7cRLb1OyiEpICvgNUsC5whhv8v11Skn64wxG5xy5fGkh7e8c1XCow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/844f298602.mp4?token=seJO8LRUxXQKGsh4jYc0NUNEsfgxVAYvBTUJm3IGzdznLhGIWWzeE-pZ32kz0YkZZoRirnS8Gsv-zSWhBDpQuuuTyJFic5iRTu50zxiYN0DVfKkL1lIRnOoXEh2cPpsreBnfS3EfA-OFninIyTeVcHu8eW4zMPCZQUTXCC6TFQmGu8HZzqeaF5T_C35PrZJEzRDshVkihWICAyotW29g1hyucIBCYjT5GO1zSMp2JPJWPS0PXRKtfTK4_ibOeA--5G5oNPxkhgO9PgyCmIc5KLY6xzpoSRTuL7cRLb1OyiEpICvgNUsC5whhv8v11Skn64wxG5xy5fGkh7e8c1XCow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قطر در حال میانجیگری بین جمهوری اسلامی و آمریکا
@WarRoom</div>
<div class="tg-footer">👁️ 192K · <a href="https://t.me/withyashar/20277" target="_blank">📅 21:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20276">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">واشنگتن‌پست به نقل از یک مقام آمریکایی: کشورهای خلیج فارس ، به رهبری قطر، در حال مخالفت با تجدید جنگ با ایران هستند
@WarRoom</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/withyashar/20276" target="_blank">📅 21:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20275">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">شبکه ۱۲ اسرائیل گزارش داد که نهادهای امنیتی اسرائیل خود را برای دو سناریو آماده می‌کنند: یا ایران ابتکار عمل را در حمله به اسرائیل در دست بگیرد، یا دونالد ترامپ به اسرائیل برای مشارکت در حمله چراغ سبز بدهد.
@WarRoom</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/withyashar/20275" target="_blank">📅 20:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20274">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">@WarRoom
shabbat shalom</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/withyashar/20274" target="_blank">📅 20:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20273">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اسرائیل حالت فوق‌العاده اعلام کرده است. یک مقام اسرائیلی در یک نشست خبری با رسانه‌های خارجی گفت: "ما منتظر چراغ سبز هستیم."
@WarRoom</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/withyashar/20273" target="_blank">📅 20:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20272">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کانال ١٢ اسرائیل : مقامات اسرائیلی معتقدند که حملات دقیق و هدفمند به تاسیسات کلیدی می‌تواند تاثیر قابل توجهی بر رهبری ایران و افکار عمومی داشته باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/20272" target="_blank">📅 20:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20271">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یک منبع آگاه به i24NEWS گفت: "ترامپ صبر خود را از دست داده است، نتیجه نهایی در آخرین لحظه اعلام خواهد شد"
@WarRoom</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/withyashar/20271" target="_blank">📅 20:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20270">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9YE6F0MgGx2vKZqaN-yHIjw4Zpy7IX9qSW88-yMuK-rWx-DrFGnm-3ppEb0aHVUE2C3pLWiY1Iij3l2Dq3lR_PvQs4wMdVnIzpHTWp0j_gYvTJPiJ2HZlUZiXu62P0wmAmEcN1JrigaOf-ltzvE9BSpylfyRsvPGJFqrH08Upkb8xr-COW0AdKaEEklI5qCPu9n4ZUh1Lww-Ma_nhZGtMERzZXyRC5yOIdz0uQc8FrWtfblgBtnbf3ebzPrrLzesHqgUF_5aXmOIEVavo6zOXFSJUmWilRaJtKZKi46eXM048qdj5ba5I5P-34h4_cnsq5TVx8Glxn60r006BrQFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام با انتشار عکس از یک هلیکوپتر شینوک دو ملخه که مخصوص عملیاتهای نیرو زمینی است، در حال نشستن در یک مکان خشک بیابانی‌مانند جنوب، پشت یک سیم خاردار که نماینگر یک مرز است، تصویری نمادین و سیگنالی از حمله زمینی قریب الوقوع داده.
@WarRoom</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/20270" target="_blank">📅 20:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20269">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/20269" target="_blank">📅 20:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20268">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کانال ۱۲ اسرائیل: یک مسئول اسرائیلی گفت که ایالات متحده از هر زمان دیگری به تجدید جنگ علیه ایران نزدیک‌تر است.
@WarRoom</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/20268" target="_blank">📅 20:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20267">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کاخ سفید : خداوند سربازان ما را حفظ کند
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 188K · <a href="https://t.me/withyashar/20267" target="_blank">📅 19:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20266">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کانال ۱۴ : صدای چندین انفجار در کویت شنیده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/withyashar/20266" target="_blank">📅 19:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20265">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نیروهای قدس , برون مرزی سپاه : مجتبی دستور اجرای مجموعه‌ای از حملات پیش‌دستی علیه کشورهای منطقه را صادر کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 184K · <a href="https://t.me/withyashar/20265" target="_blank">📅 19:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20264">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وزارت امور خارجه آمریکا: ایران و گروه‌هایی که از آن حمایت می‌کنند، ممکن است منافع آمریکایی یا شهروندان آمریکایی را در سراسر جهان هدف قرار دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 187K · <a href="https://t.me/withyashar/20264" target="_blank">📅 18:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20263">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc9dba0c46.mp4?token=DiojRTUE-g8oIaFKF7huf_gx-kmcv80n3_gvWe3dTKhbzWMaLv52Dfu62Kj5OSrgv8Y88AL0OmrJSNfvsHLPtmofC3s3Wznp-J30vrBe5UMOjKyJSyksFMolOcAU_Qcj8VJjNTdvH9lr7mNcxr_yR7smjf15l8o13CZttv73ijpWjgNF4n_KCEWw-kinPUwU2o7RSR3GWNggrU1qpMzfgdgVT6bGHGgss6c1HzmSEUUL9MBRnJ02dWTdp5hT8eDV7pXKHGc9ti8YB8Zt-xlH4ghm6JyXQd696rFGWp5fssrqLcM4FPPzKsoL_TIRAk7n-Y0Pv6jDkIEZnnaqyHj4Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc9dba0c46.mp4?token=DiojRTUE-g8oIaFKF7huf_gx-kmcv80n3_gvWe3dTKhbzWMaLv52Dfu62Kj5OSrgv8Y88AL0OmrJSNfvsHLPtmofC3s3Wznp-J30vrBe5UMOjKyJSyksFMolOcAU_Qcj8VJjNTdvH9lr7mNcxr_yR7smjf15l8o13CZttv73ijpWjgNF4n_KCEWw-kinPUwU2o7RSR3GWNggrU1qpMzfgdgVT6bGHGgss6c1HzmSEUUL9MBRnJ02dWTdp5hT8eDV7pXKHGc9ti8YB8Zt-xlH4ghm6JyXQd696rFGWp5fssrqLcM4FPPzKsoL_TIRAk7n-Y0Pv6jDkIEZnnaqyHj4Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسک های ترامپ و پوتین در کارناوال آمستردام ۲۰۲۶ در نقش کاپل همدیگر را بوسیدند
@WarRoom</div>
<div class="tg-footer">👁️ 187K · <a href="https://t.me/withyashar/20263" target="_blank">📅 18:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20262">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ساعاتی پیش سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی از یک حادثه در فاصله ۱۱ مایل دریایی در شمال‌شرق لیما، عمان دریافت کرده است. افسر ارشد ایمنی (CSO) یک نفتکش گزارش داده که این شناور با یک پرتابه ناشناس مورد اصابت قرار گرفته که باعث آسیب به اتاق…</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/withyashar/20262" target="_blank">📅 17:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20261">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سی‌بی‌اس به نقل از یک مقام دولتی:
ایالات متحده در حال برنامه‌ریزی برای قطع کامل برق در سراسر تهران است
@WarRoom</div>
<div class="tg-footer">👁️ 187K · <a href="https://t.me/withyashar/20261" target="_blank">📅 17:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20260">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJuWZJOuQT9vbuCwUVhmhRJkEuEmU60_K25Fg5zFp-tIMdeRePph_KNw6aV0jEFb4Mw-8Il5J2UdYWI-K8ouv8ehL9CGYtuGvcGuKB7QTxHGuVnTWyAG3rn505bQmi8GTIfDc3wcWeI9_g6Ffe-6hqUvS4DokFe6NCjlkyY8Ga0jzntZNpPDAz9Hs9pLBwmvrLi-jpcAgyp66xuvYfOHIhuz3LQCV_5zVg0A1O7TQG8wITbfwDtsPHrOzPc8GdAC3qGZxZJT14osp8L8R4i1QZ0V4XPfNT_S-9C-iM1r_DKTN3ShqRS_Z-l9mkjll5IhgRN0NaiEEhV4qoAWk9r_AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان شیراز - صدرا
@WarRoom</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/withyashar/20260" target="_blank">📅 17:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20259">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFPgtypZMkoHLRlmIaIRNFdE2V8DSsM5Q5-Af_rGvTIFN3tndHGCmCPa0mL4pVtOxMFilUSCFulaIpukTnKRgVUtE0B3t4C8oTY1tMaK3vhj1XdpcbBno2vG9XOJRDZ6yA7buMb0M-B8e19qCuVYtAxgii0CegAfQIY5wqsxYOdmewMZfjLb3To9g21T3HsdPcFziy0GRwKMuDTTyU363aZdYKCOfZWtTVeCDnJXF_H-n75kbCcVsPTA7Wqf6QV8pReGS9fQy94BBgp8XEt5KSaS9AKuyAN_4Pj7IUNHPc6iWuest01ZWoEiiAK9LX-jUX9dc-1r6vGlyLJMMDXyxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان جاده هرمزگان، به نظر من خودرو تحلیل اطلاعات پدافند باور ۳۷۳ هست
@WarRoom</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/20259" target="_blank">📅 17:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20258">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اتاق جنگ با یاشار : امشو شوشه ؟ بوی کوه سوخته میاد
@WarRoom
⏰</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20258" target="_blank">📅 16:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20257">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGzVR7jW4y4lvD8Yqk1hH5LkYKiegC4BL1KBQosZHiLBmDgSGvexZTX8oEC2cyC9qUh3AcZ6WYY0s9Ai8Z4DpwZltTMPutBUzveFUKaZq67Hi8mTOU0mWFIqZrIeWm9kb3-Iw_TWglyxPPcbIQjjo-uK-Tf2nquxAtIUgiIsRFZWzOhT7KcFjjE-e6CfSo8J3VEgLQ9njysFOaS9-6knyE5bZjct5aj3NOlXU6wP9hJFO0xYjc5jK-5IoMtGMxhGQLaP84oA1VORoRun-6Y7_rpMhij8wljPvyt2rNZ6hN_WoWQd7TbqgwG3KA181AgkNBLBUPFE7IDKYdaSsUhisQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون منابع محلی در اهواز گزارش دادند: ستونی از تانک های مدل T-72، متعلق به تیپ زرهی 92 ارتش در حال حرکت در بزرگراه آبادان و اهواز، به سمت آبادان مشاهده شده‌اند و به نزدیک ترین نقاط مرزی می‌روند @WarRoom</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/20257" target="_blank">📅 16:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20256">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سفارتخانه های آمریکا یکی پس از‌ دیگری در حال اعلام بالاترین سطح هشدار برای شهروندهای آمریکای مبنی بر خروج از خاورمیانه هستند @WarRoom</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/withyashar/20256" target="_blank">📅 16:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20255">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">instagram.com/yasharmotors
لطفا همه این پیج دوم رو فالو کنید ، بعد از جنگ هم کلی کارای خفن میکنم توش
🙌🏾</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/20255" target="_blank">📅 16:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20254">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بلومبرگ: یک نفتکش قطری حامل گاز طبیعی مایع، شب گذشته در سواحل عمان و در حین عبور از تنگه هرمز، مورد اصابت پرتابه قرار گرفت
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20254" target="_blank">📅 16:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20253">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">😮‍💨
پیج  در ۱۵ دقیقه برگشت</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/20253" target="_blank">📅 15:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20252">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">روزنامه «وال‌استریت ژورنال» به نقل از منابعی آگاه گزارش داد دونالد ترامپ، دستور ادامه حملات نظامی به ایران را صادر کرده و احتمال دارد دور جدید این حملات
روز یکشنبه آغاز شود
. تصمیمی که به‌گفته این منابع، پس از کاهش اعتماد ترامپ به نتیجه‌بخش بودن مذاکرات با تهران گرفته شده است.
به‌گفته این منابع، ترامپ به دستیارانش گفته است دیگر به دستیابی به توافق با تهران از طریق مذاکره خوش‌بین نیست و مقام‌های ایرانی را به جدی نگرفتن مذاکرات متهم کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/20252" target="_blank">📅 15:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20251">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HclIRXo1_qdC5-M87MqUV3IsbwQiAoG6f0W1QdPsed7bMJcCi7hWKVspjri6sXK-nVAafuFYsTKzIc9RXKn9u2FkGzGyvuhjRtheOKKvez93Vgy5RJjmr0WqvvaySGQBz-anVj5Z3PaxweMer0ZhbaeuMDymbx1bkyE-3iQHH3aJerXBfFVUMRX63m9q4JDcwmLmC7-8MSVyxNrCtTpXieL-kKu7ihZQzgTPV5wYVO1WBys4Qh0yG8jHTVWVmQXPOTuuC2U64VgPviaPIN2hoslhHNzKsTmjaQt4vlHlu_OI13mu0DW9cIu_MlYALcDiJhqhBSf1uET3KPfFbevdjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای
C-12 Huron
یک هواپیمای نظامی بر پایه هواپیمای تجاری
Beech Model 200 Super King Air
ساخته شده است و به تجهیزات پیشرفته اطلاعاتی و شناسایی مجهز می‌شود. این مدل‌ها می‌توانند مأموریت‌های
شنود الکترونیکی (SIGINT)
و
جمع‌آوری اطلاعات ارتباطی (COMINT)
را انجام دهند؛ یعنی رهگیری و تحلیل امواج رادیویی، ارتباطات بی‌سیم و سیگنال‌های الکترونیکی. همچنین از آن‌ها برای شناسایی اهداف، پایش تحرکات نظامی، پشتیبانی از عملیات ویژه و انتقال اطلاعات لحظه‌ای به مراکز فرماندهی استفاده می‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20251" target="_blank">📅 15:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20250">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fo8ME2VdmrxZJ6ejli6LFF7K3SKNylGk3B9yQSv9VuI3oKbs6Vk45v9tsWiu-1SNRi407D81XnAqea9Hr00Br_OhueRBc7YeiMaPDwNmEZTJ3EytJxp4ZmnAZhIzMWEJCob80VjE1TWI1gzs88OrR7gkNeBmqC9f7I6uYuUC9O9e9k-2_kMkcs6IdwfKpqL1B0cOzIgyg8-2yHuUMqLiGtRd_3ozY-5lKLQlSq1WuAfG_vGo6xbmT1bq0ogxDpjTODOckjVgtC4Kw2rM8N88yox7nHOCcV2PWeXhceLAIAkLEo8htLb7bhs_Cxn9YTuDA9tDcvS7SNRzOzGxC9xHdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین بروزرسانی از موقعیت ناوگان نیروی دریایی آمریکا، همچنان ناوهای هواپیمابر بوش و لینکلن به همراه گروه آبی-خاکی باکسر موقعیت خود در جنوب دریای عمان را حفظ کرده اند و در محاصره دریایی ایران مشارکت دارند.
همچنین رزمناو پرینستون(CG-59) و 17 ناوشکن از کلاس آرلی برک نیز در اقیانوس هند،دریای عربی، دریای سرخ و مدیترانه حضور دارند:
میسون (DDG-87)، ماستین (DDG-89)، جونز (DDG-53)، اسپروانس (DDG-111)، پترسن (DDG-121)، کوک (DDG-75)، راس (DDG-71)، میلیوس (DDG-69)، مورفی (DDG-112)، فین (DDG-113)، بلک (DDG-119)، هیگینز (DDG-76)، مک‌فال (DDG-74)، پرالتا (DDG-115)، گونزالس (DDG-66)، روزولت (DDG-80)، ایگناتیوس (DDG-117)
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20250" target="_blank">📅 15:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20249">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رسانه های داخلی : نیروهای مسلح جمهوری اسلامی وارد بالاترین سطح آمادگی شده‌اند .
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20249" target="_blank">📅 15:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20248">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سفارتخانه های آمریکا یکی پس از‌ دیگری در حال اعلام بالاترین سطح هشدار برای شهروندهای آمریکای مبنی بر خروج از خاورمیانه هستند
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20248" target="_blank">📅 15:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20247">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وال استریت ژورنال: ترامپ، در ساعات پایانی حضورش در باشگاه گلف خود در نیوجرسی، طرح‌های جدید حمله را که به او ارائه شده بود، تأیید کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20247" target="_blank">📅 15:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20246">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سفارت آمریکا در اسرائیل و عراق : آمریکایی‌های حاضر در منطقه باید آماده باشند و در صورت تشدید تنش، خروج از منطقه را در نظر بگیرند
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20246" target="_blank">📅 14:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20245">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JP99k8GUZFu55QuYhocdsO5sOme9yEqJujTm7pPoJUYYwscZh7QGn7klH8bWHwRVzLMGjhiiuBZVwJISjX30hpAjG7nUgpqtpQ_4nHMzbBfKKTz1aiIRD7Y_eOGJQ_7Cc0M0-BBnTqb7LrtPKsXo_V-Z88KjhK0Ka3ppCVoit6EMBF9dn0-xo4H4M48mQoc534-_VBY8FLPB3ngxrifXxePzoKT4Fp-yOJUUAZc4RKg_JACeEi2cAqU7WHrd8c1tTF0hfB5O9GkcDzT0UUW9SxOGRpkxN6LWf5cDtKgh1jrwYTAhWi9ZxmEcv3Ttu3dtihCCsxgHstvAiVwr1a3-MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر فرد ناشناس با هویت البیبی التانکینیاهو
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20245" target="_blank">📅 14:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20244">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تسنیم : گلوله توپ زمان دفاع مقدس ۸ ساله منفجر شده است و حمله ای رخ نداده @WarRoom یاشار : واکنش صدام به این خبر</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20244" target="_blank">📅 14:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20243">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZLrISLnwF0ig3lnf_W18uSGuTuTR2ZbwjcjE34lShLuZgCLuvNNfYRLUJonjgZl-2eAoY5mKEdkW9aPdK5s43_2KoRv4yPmPFZZykdzTbWdC_fGijKBhIFZlguvJTwpL_xO3mZZ-1NPvaKkl_vcVCOxqUnUZNkhVy_7F1aaykZfLD04ZKG1gUWvoUDRlI7m8I-RMyPdg5YWt1VoB74Ey8t9aWwwNveH1G8Cu9xfsFEntMdBfJVmDrLNeqSsBOIw2-BGMAQrS5FEDMUZAMyPGssYDfAOUYFrU9CAtmxTddi0TtD7o3vqEbJUKV0gihIc7I745Y5S9S574lsmlz5G3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش غیر رسمی‌ ، یک لانچر که در کنار پل کمر بندی در شاهاباد استان کرمانشاه بود هدف حمله قرار گرفته @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20243" target="_blank">📅 14:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20242">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ارسالی : یاشار تایید شد خبرایی هس پادگان چهارم شکاری دزفول تمامی سربازارو فرستادن مرخصی به خانواده های نظامیا داخل پادگانم گفتن تخلیه کنید تا عصری
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20242" target="_blank">📅 13:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20241">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsK167WhdFw_ZMSrWh7c0_2f3c8l-PZgfaomBclUaOQ5Ygf91CBt11Z-NBPFW009aivA9fJbpDquRq2uRp0VHejystWgG41GN_eg0T1D00HXTAlzgFyrKDP4G0rSV0IrAuh5QA-AXpZwlqKduw6ZRBZuCKeTpj5ay-OHWWzh9KudXewDVYteeX0__56sgmub1p_0HRLO3AR9zQ6iM4GTOqsyYWDg972XWmwZArt1aSp3wXclr4Qx_qW4_xwsha5TQR5kLIMerz-Ua7fecj6OVILxucOW3wW99BhaZBYev_UuxuBpqu9kQS-GXHU0dKqtKjej1rnHXDge-fWf7JQPYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش انفجار در شاهاباد، اسلام‌آباد غرب ، استان کرمانشاه @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20241" target="_blank">📅 13:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20240">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">هم اکنون منابع محلی در اهواز گزارش دادند: ستونی از تانک های مدل T-72، متعلق به تیپ زرهی 92 ارتش در حال حرکت در بزرگراه آبادان و اهواز، به سمت آبادان مشاهده شده‌اند و به نزدیک ترین نقاط مرزی می‌روند
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20240" target="_blank">📅 13:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20239">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گزارش انفجار در شاهاباد، اسلام‌آباد غرب ، استان کرمانشاه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20239" target="_blank">📅 13:33 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
