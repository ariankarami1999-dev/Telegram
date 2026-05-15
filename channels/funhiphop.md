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
<img src="https://cdn4.telesco.pe/file/svl3zbtzpya8HQi56RyvSy-_YUHFq4HkZI2bIfCxLOE7e4etYp_4ks0tlFZG9ZdDvwWslLV-EHcNB8JxpCY748D0kThn5WV64GrH9MYDh1bwx5jg7xGpEL1Eq5Wi3ZKhepddP4IsH-FulLlqCw-y-XdBzrgpPpX_aNW57WQOQVm90Qw1PFZ4HS-tywHp9b5uPaNgP2aDLiv4C1C7EmINjPLte-wQn4IIdYP8duQLKTc8kkXBRAgP7aaXyoEqtIyIVkxDdF0HWjOdskeYm087QNxaCInuJaLCcOXzj6XMfh0yueCldjVNfQLQaOs_OwKPsfDgPy2Gf2okIB5bdqirpw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 142K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 08:36:54</div>
<hr>

<div class="tg-post" id="msg-74947">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">توییترو باز کردم دیدم یکی توییت زده اپ شیر خورشید رو گارد جاویدان ساخته، بستمش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 516 · <a href="https://t.me/funhiphop/74947" target="_blank">📅 08:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74946">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzOil4jwcCs0HH3PBJUJyOxBLhHo0d7DpQj2o89rcDQ8fYezAK--z2m2lOqrO9YZV4qz5XrI8wnoAzLdf1W24p1VDaKufR44I0CtrQdU6cVDEAguxER3TXu-7tgFAllTkX8F8RgHPtm_LztzwEMwzpCBS2r3y_5vlmL68SzWCXXhbFJthIQIkKQ2PZx90___Uy5gFvh9EcUINC3XYdiKK-QWkGJ1jRY21pNpVYjcB3kdPSivYc8eBF4qBGLE1l0UPbGilegx4bgHJskxCL3nmAn7q0HNchARj0-Fv-b_RXHrWyn20IpZtSN0sjgXUybvXd4521I2K55TVGU6o1i-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗿
وزارت امور خارجه آمریکا
اعلام کرد که در اواخر ماه آوریل، ونزوئلا
بیش از ۷۳۴۰ کیلوگرم اورانیوم با غنای بالا
را از راکتور هسته‌ای RV-1 در منطقه آلتوس
میراندینوس
به مرکز
ساوانا
ریور در
کارولینای
جنوبی
آمریکا
منتقل کرده است.
این محموله اورانیوم با یک کشتی
بریتانیایی
جابه‌جا شد و آژانس بین‌المللی انرژی اتمی نیز ضمن نظارت بر تمام مراحل،
حمایت‌های فنی لازم را ارائه داد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/funhiphop/74946" target="_blank">📅 06:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74945">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">😠
دونالد ترامپ
فکر نمی‌کنم گرفتن این اورانیوم جز از جنبه تبلیغاتی ضرورتی داشته باشد. به نظرم این کار بیشتر برای رسانه‌های دروغ‌پرداز مهم است. من همان کسی هستم که گفتم اورانیوم را پس می‌گیریم و
حتماً هم این کار را خواهیم کرد
.
ما کاملاً چشممان به آن است و زیر نظرش داریم.
به آن‌ها گفتم اگر بخواهند نیرویی به آنجا بفرستند تا شانسی برای خارج کردنش امتحان کنند، یا اگر ببینم کسی دارد تلاشی می‌کند،
فقط با چند تا بمب آنجا را می‌زنیم
و همه‌چیز تمام می‌شود؛
آن‌ها جرأت این کار را نخواهند داشت.
ما در آن سه سایت، ۲۴ ساعته با نُه دوربین همه چیز را کنترل می‌کنیم.
راستش را بخواهید،
اگر اورانیوم را بگیریم خودم هم حس بهتری دارم
، اما معتقدم این کار بیشتر از هر چیز دیگری جنبه تبلیغاتی و رسانه‌ای دارد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/funhiphop/74945" target="_blank">📅 05:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74944">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">😠
دونالد
ترامپ
به نظرم آن‌ها اتفاقاً از خیلی جهات خیلی منطقی‌تر شده‌اند. از آن رده‌بالایی‌ها و رده‌دومی‌هایی که دیگر بین‌مان نیستند، باهوش‌ترند.»
هنیتی:
پس چرا مدام شل‌کن‌سفت‌کن در می‌آورند؟
یک توافقی می‌کنند و بعد فردایش زیرش می‌زنند... مثلاً ما پنج روز منتظر نامه‌ای ماندیم که باید یک‌ساعته می‌رسید.
داخل کشورشان بدجوری به هم ریخته و آشفته است.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/funhiphop/74944" target="_blank">📅 05:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74943">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🤑
دونالد ترامپ
در حال حاضر، هیچ نفتی از جزیره خارگ صادر نمی‌شود؛ هیچی، صفر.
مردم دارند جاهای دیگری را برای خرید نفت پیدا می‌کنند، مثلاً تگزاس. بنابراین، نمی‌خواهم بگویم که داریم ثروت هنگفتی به جیب می‌زنیم. اگر این را بگویم، آن‌ها می‌گویند: «اوه، او آدم‌های معمولی (قشر ضعیف) را فراموش کرده است.»
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/funhiphop/74943" target="_blank">📅 05:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74942">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">صحبت ها مقداری زیاد هست
بابت حجم زیاد مسیج ها پوزش مطلبم
❤️
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/funhiphop/74942" target="_blank">📅 05:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74941">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">😠
دونالد ترامپ
من به شی جین‌پینگ گفتم شما نیازی ندارید که ایران سلاح هسته‌ای داشته باشد.
هانیتی: او چه جوابی داد؟
🤨
ترامپ: او خیلی واکنش نشان نمی‌دهد. آدم بسیار خونسردی است. قرار نیست بگوید «بله، حرف خوبی زدی».
هانیتی: فکر می‌کنید موافق بود؟
ترامپ:
فکر می‌کنم بله.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/funhiphop/74941" target="_blank">📅 05:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74940">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">😠
در ادامه
مجری فاکس نیوز، هانیتی: فکر می‌کنید شی جین‌پینگ و چین توانایی تاثیرگذاری روی ایران را دارند؟ با توجه به اینکه چین یکی از بزرگ‌ترین خریداران نفت ایران است؟
ترامپ: احتمالاً… ببینید، او با تهدید و جنگ وارد نمی‌شود. تا الان خیلی خوب عمل کرده است.
هانیتی: منظورم تاثیرگذاری بود…
ترامپ:
آن‌ها می‌خواهند از آمریکا نفت بخرند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/funhiphop/74940" target="_blank">📅 05:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74939">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">😠
دونالد ترامپ
امیدوارم ایران این حرف‌ها را ببیند.
ما
دقیقاً
می‌دانیم چه چیزهایی مستقر کرده‌اند.
آن‌ها یک فرصت کوتاه پیدا کردند و حالا سعی می‌کنند دوباره بعضی تجهیزات را
جمع‌آوری
کنند. چند
موشک را هم از زیر زمین بیرون آورده‌اند
، اما همه این‌ها در عرض یک روز از بین خواهد رفت.
تمام کارهایی که طی چهار هفته گذشته انجام داده‌اند،
در یک روز نابود می‌شود.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/funhiphop/74939" target="_blank">📅 05:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74938">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">😠
دونالد ترامپ
جنگ ویتنام ۱۹ سال طول کشید. فکر می‌کنم جنگ عراق هم حدود ۱۰ سال بود… در ویتنام هزاران نفر کشته شدند. اما متأسفانه در این دو جنگ، ما ۱۳ نفر را از دست دادیم.
13 نفر در مقایسه با 75 هزار نفر و یا حتی 50 هزار نفر.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 976 · <a href="https://t.me/funhiphop/74938" target="_blank">📅 05:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74937">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">😠
دونالد ترامپ
قیمت نفت نسبت به چیزی که بیشتر مردم، حتی خود من، انتظار داشتیم خیلی کم افزایش پیدا کرد.
😶
فکر می‌کردیم بیشتر بالا برود، اما برای یک دوره کوتاه این موضوع قابل قبول بود؛ چون ما نمی‌توانیم اجازه بدهیم ایران به سلاح هسته‌ای دست پیدا کند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 971 · <a href="https://t.me/funhiphop/74937" target="_blank">📅 05:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74936">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">😠
دونالد ترامپ
اگر بایدن به چین می‌رفت، حتی فکر هم نمی‌کنم می‌توانست با رئیس‌جمهور چین دیدار کند.
من فکر می‌کنم شی جین‌پینگ آدمی گرم و محترم است، اما کاملاً روی کار تمرکز دارد. اهل بازی و حرف‌های حاشیه‌ای نیست؛ درباره آب‌وهوا یا چیزهای بی‌اهمیت صحبت نمی‌کند و من این ویژگی را دوست دارم.
اگر قرار بود برای نقش رهبر چین در یک فیلم بازیگر انتخاب کنند، دقیقاً باید کسی شبیه او را پیدا می‌کردند. واقعاً فردی مثل او کم پیدا می‌شود؛ مخصوصاً با آن شخصیت و قد بلندش.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 973 · <a href="https://t.me/funhiphop/74936" target="_blank">📅 05:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74935">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dm_Tyfbn5GTY-zQi7bIksh9BWNINpEAnFw9dzfqPn-uEvodh_dWyQEnTM6_NeKVfke-UvsBu_r-gGrP4VigkJB8Bh7p7mm7rUoYo3YyYlseg3xaSFDK7jl5a8mlTUuK8ofDrWdCJaiRn9ZNq-ADhRm0-FJ9Q8op0p5IBgMj6ZzMlW7nae4mPsMudbRyWsn5H-jtWYHDwRoV6S5sVAk9CKcajxpb8lGXdbhk7iNIi7xa1rnXGKu2nSO3ax3pO57QycGdd32b6i-87HTinnGAoDSMjMPaEvU2RAJZnq6MZY3a0L9cxnQBowLNODMGRyzVCV9hZaXFYvq08DP7zYT4Hqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز عصر دفتر نتانیاهو گفت طی جنگ ۴۰ روزه، نتانیاهو شخصا سفر مخفیانه‌ای به امارات داشته تا با رئیس امارات دیدار کنه و چند تا مقام نظامی هم تو این مدت رفتن اونجا که درمورد جنگ هماهنگی ایجاد کنن.  الان امارات کلا همه چیو تکذیب کرده گفته ما هیچ‌کس رو اینورا…</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/funhiphop/74935" target="_blank">📅 04:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74934">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">کانال ۱۳ اسرائیل:
اسرائیل در حال آماده‌سازی برای احتمال جنگی تازه با ایران پس از سفر رئیس‌جمهور ترامپ به چین است.
مقامات اسرائیلی تخمین می‌زنند که پنجره احتمالی برای اقدام نظامی آمریکا ممکن است از فردا آغاز شده و تا شروع جام جهانی ادامه یابد، و انتظار می‌رود ارتش اسرائیل در صورت از سرگیری درگیری‌ها درگیر شود.
هنوز نشانه قطعی وجود ندارد که رئیس‌جمهور ترامپ تصمیم نهایی را گرفته باشد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/funhiphop/74934" target="_blank">📅 03:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74933">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ابی ناموسا تو دیگه چرا</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/funhiphop/74933" target="_blank">📅 02:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74932">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بابک زنجانی یا همون ایلان ماسک ایرانی
🔜
یه زیر ساخت بومی بلاکچین ( ارز دیحیتال ) برای اپلیکیشن خودش یا همون
پیامرسان دات
وان تاسیس کرده.
مثال
: پاول هم برای
تلگرام
اومده
تون
و تاسیس کرده.
البته با این تفاوت که تون یک سیستم بلاکچین معتبر و زنجیره وار درون قلب سیستم بلاکچین جهانی هست و بر خلاف پروژه بابک زنجانی یک چیز معتبر هست!
پروژه بابک زنجانی و حتی نمیشه جایی پیگیری کرد که ببینی معتبر هست یا نیست
که به نوبه خودش بسیار بسیار جالب هست.
خوب حالا اگه یادتون باشه با اون حرکت
توییتر
و حذف شدن
تیک
مقامات
, بابک زنجانی اومد گفت که دیگه چنین وضعی و تحمل نمیکنه و میره سراغ اینکه اپلیکیشن خودشو بیاد تاسیس کنه و خوب تیک ابی کسی و هم حذف نمیکنه و از قوانین
دموکراسی
پیروی میکنه.
این وسط یک چیزی که
شفاف نیست
این هست که ایشون میخواد یک
شبکه بلاکچینی بزرگ با ظرفیت 90 میلیون ایرانی
بسازه ولی در صورتی که بزرگترین خزانه داری کل روی کره زمین که تو آمریکا هست ایشون و به
پولشویی و همکاری با سپاه پاسداران انقلاب اسلامی
متهم کرده و چند وقت پیش هم کامل این شخص توی
لیست تحریم های کشور آمریکا
قرار گرفته.
تا اینجا اگه خوندی دمت گرم باقیشو هم بخون که مطلع بشی
❤️‍🔥
حالا اپلیکیشن دات وان چیه؟
🤨
یه اپلیکیشن شبیه اینستاگرام هست که مثل تلگرام یه ارز دیجیتال مخصوص به خودشو داره که با تولید محتوا و فعالیت بهت از اون ارز دیجیتاله میده و تو عملا میتونی توی این پیامرسان کسب درآمد کنی.
این اپلیکیشن با اینترنت ملی بالا میاد و یک ترافیک نیم بهارو هم شامل میشه
بدین شکل که شما اگه 10 گیگ بگیری 20 گیگشو میتونی تو اپ بابک جون مصرف کنی و حتی درآمد زایی هم داشته باشی.
البته اینو تا یادم نرفته بگم که این پیامرسان تضمین 100% بابت این داده که
تحت هر شرایطی کاربر هاشو آنلاین نگه میداره و نمیزاره کسی از اینترنت و فضای آزاد و شفاف دات وان دور بمونه!
😶
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/funhiphop/74932" target="_blank">📅 02:18 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74927">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بابک زنجانی یه پروژه کریپتویی داره با همون پیامرسانش ( دات وان ) میاره بالا که به شدت مشکوک هست
اطلاعات تکمیلیشو حتما اینجا قرار میدم براتون
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/funhiphop/74927" target="_blank">📅 01:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74925">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ
رییس جمهور چین برای مدت کوتاهی بهم گفت نابغه
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/funhiphop/74925" target="_blank">📅 01:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74924">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رئال بازی خودشو برد و یک قدم دیگه به قهرمانی لالیگا نزدیک تر شد
🔥
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/funhiphop/74924" target="_blank">📅 01:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74923">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tarCeFYCl37fhvGFjqnHvCKQdd31l4766HZZolqZep-JnqXTmj4dgsjwDl3q5NRvCxOF7efhBujXB_y8fWOpcuXi00i12ghr7vulboBl-EeQ5AOItDlDPOY9Na_T-i8syhpZMWR2prOIPp8n0kUv8e7E5SwUxkC3ZSYwZSwYPk8D_x1g1c_kKwWg8Kbz9GmuYTzqdkUWfpdw0K8-8QHPDZLwFUiY3gyjnBwv_Mch9fqKl_Fd9orLmFJrA9TkmJfoNE5f1E_59SiYTXrtU1rJ81G3qvILBuvPyv6bSrR1vTobB8_kvHhEKCm8-1sJCjN9qJZvhlq5qx68Kyb3aNJw1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار بورس اوراق بهادار تهران در ۷۵ امین روز بسته بودنش رکورد تاریخی‌ای را شکست و با ۲۰ درصد رشد، قله‌ی جدیدی را در تاریخ کشورمان ثبت کرد.
❤️
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/funhiphop/74923" target="_blank">📅 00:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74922">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فاکس‌نیوز:
ترامپ و همراهانش از ترس اینکه مبادا چینیا لپتاپ و گوشی‌هاشونو هک کنن یا نرم‌افزار جاسوسی روشون نصب کنن، همگی از گوشی و لپتاپ‌های جایگزین برای سفر به چین استفاده کردن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/funhiphop/74922" target="_blank">📅 00:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74921">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سی‌بی‌اس:
رئیس سازمان CIA امروز تو هاوانای کوبا حضور داشته و با اعضای دولت این کشور مذاکره کرده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/funhiphop/74921" target="_blank">📅 00:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74920">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کان نیوز:
اسرائیل معتقد است که رئیس‌جمهور ترامپ پس از بازگشت از چین در پایان هفته درباره آینده جنگ ایران تصمیم خواهد گرفت.
مقامات اسرائیلی می‌گویند گزینه‌های اصلی مورد بحث، از سرگیری درگیری‌ها یا از سرگیری عملیات نظامی در تنگه هرمز تحت «پروژه آزادی» است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/funhiphop/74920" target="_blank">📅 23:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74918">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">به به  سازمان عملیات تجارت دریایی انگلیس:  گزارشی از وقوع یک حادثه در فاصله ۳۸ مایل دریایی در شمال‌شرق فجیره در امارات دریافت کردیم.  قایق های تندرو سپاه پاسداران یک کشتی را که خارج از تنگه هرمز لنگر انداخته بود را تهدید به هدف قرار دادن و سپس توقیف کردند…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/funhiphop/74918" target="_blank">📅 23:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74917">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">میگم مگه مجلس تعطیل شده؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/funhiphop/74917" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74916">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ: کوبا بعدیه.  اوه، لطفاً وانمود کنید که من این را نگفتم، لطفاً.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/funhiphop/74916" target="_blank">📅 23:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74915">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">عزیزی، رئیس کمیسیون امنیت ملی: پیش بینی کردیم که هرکس که ترامپ رو به هلاکت برسونه، 50 میلیون یورو پاداش دریافت کنه.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/funhiphop/74915" target="_blank">📅 23:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74914">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دوستان این رفیقمون که چند روزه تبلیغشو میزاریم تا حالا هیچ شاکی ای نداشته، اگه نیاز به کانفیگ دارید بهش پیام بدید ازش تهیه کنید با قیمت خوب
ایدیش برای خرید
@r_downey_jr
ایدی چنلش
@suii_vpn</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/funhiphop/74914" target="_blank">📅 22:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74911">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کان نیوز به نقل از دو منبع اسرائیلی و آمریکایی:
تو هفته اخیر جلسه مهمی بین ارتش اسرائیل و سنتکام برگزار شده و همه منتظر تصمیم ترامپ بعد از پایان سفرش به چین هستن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/funhiphop/74911" target="_blank">📅 22:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74910">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ی زمان اینجا پست جهاد خامنه ای علیه کشور های بیگانه ۶۰۰ تا ری‌اکشن قلب می‌گرفت
یادش بخیر
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/funhiphop/74910" target="_blank">📅 22:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74909">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bb2vQd4livPirjvdKGbd6YcP3WD00tbw9jGbFK_QwzEnXe3BVkDqGqekqCH69Tf2Jbi9L7UX40C2MdQBHBetOQAuv-F9mOdEECamKI0cZDBVaGgcjg-mfuiYslD8UeDKRctCKVsM-OECrOcGaM7D-oxB_1zOsV3FdGz5hfpxVMyX4F9UQaw-roZ2EnxGIUsmXp4KPssAA_fCd58FVCvD38iBdmFAsOrHVTABybg2YpoX3v2Ow9vRO5F3_63T3a9IsQe332OOgFLMfs_DUsM09QaFFqhWm2eCLhMImKVL1pNdq07tCFXE9doIQiYahOnzwpZFqNeCwIjOkxN7Ll1htg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه نمیدونن یکی از ادمیناش برای پسرعموش ساک زده</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/funhiphop/74909" target="_blank">📅 22:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74906">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftuZ58Za00UfXPUC-L5s_3zvQJKHrb2uDkv8c2pxoq02c6q41mpVpsr77vSd74ISQLDrHI2j4tGHfnDI0Lwy4HEH6vCpZV9H1n0QE2209pb4pOZ85uIibrQwWDvX0DboxgVJO4ONDEigQWsRD_YQ7T9Mh9QEoQl56VHQBBKbBnvLTyVw9in7Ygvl2N_ea1zygXMBu7hezEqw-aptsmcrzIp6IOzBa3CDDetToqC7sPzOIuxWUpmsm050FDDlkzLoVkiIJhPyO_y3lHWKo0F9INm25JwhT_zmxOlLIGTV7UZc4vdPhCkczdt7cMK2wKSzENDgh9oyPuH-qMw_dWcfdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دختر پسرای توییتر میخوان شات از فان هیپ هاپ بزارن بگن رسانه ی خایه مال
بعد سرچ میزنن میبینن عه؟ ما به نام خلق فعالیت میکنیم
بعد یکم میرن پایین تر میبینن عه؟ علی از پایگاه داره پست میزنه
بعد میان پایین‌تر تر میبینن عه؟ ما کصخلیم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/funhiphop/74906" target="_blank">📅 22:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74905">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9609b2009.mp4?token=bu6wajFcx2s9FwCUBtoUTdjBEh7oO5A2XFPaCIP6WYWal7FxF9EGN6JpIgcGdWmYYLg8rsNHPh6iJmVfS1T4Esbn7AFPaEEDEhuqZ4ki43bvCPSAkG2-vkgKewGrrdbbAoZtcUM_CHKO59LMigHLMy24thIZ8ctcB3baBBAtE-upOx0ES6ZnHyZYcq_HSpGBis7JKp1ATJ3y9JIk6xfo8ixKLkLNJHeiKrz6mWqRJYPP149OoKRCIR56ZvLhGJTm7oxmgjD25x3yZaCR87BsEHr50huFt4it4vkMDSG2vTbRGxmHIQknRTYUY9iUeREZdPRESXcjT7b2-NjA5nkwpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9609b2009.mp4?token=bu6wajFcx2s9FwCUBtoUTdjBEh7oO5A2XFPaCIP6WYWal7FxF9EGN6JpIgcGdWmYYLg8rsNHPh6iJmVfS1T4Esbn7AFPaEEDEhuqZ4ki43bvCPSAkG2-vkgKewGrrdbbAoZtcUM_CHKO59LMigHLMy24thIZ8ctcB3baBBAtE-upOx0ES6ZnHyZYcq_HSpGBis7JKp1ATJ3y9JIk6xfo8ixKLkLNJHeiKrz6mWqRJYPP149OoKRCIR56ZvLhGJTm7oxmgjD25x3yZaCR87BsEHr50huFt4it4vkMDSG2vTbRGxmHIQknRTYUY9iUeREZdPRESXcjT7b2-NjA5nkwpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناسان صدا و سیما :
در جنگ ۴۰ روزه زیر ۲۰ درصد از شلیک‌های ما به سمت رژیم‌صهیونیستی بوده است
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/funhiphop/74905" target="_blank">📅 22:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74901">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآقا یاسر</strong></div>
<div class="tg-text">رضا پهلوی یه برنامه معرفی کرد بود ریختم روزانه 500 مگ اینترنت می‌خورد با اینکه نمی‌رفتم توش</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/funhiphop/74901" target="_blank">📅 22:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74900">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دوستان کون خودتونو پاره نکنید
بنظرتون کسی که ۳ ماهه روی تلگرامو ندیده براش مهمه  اپی که نصب میکنه به کجا وصله؟
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/funhiphop/74900" target="_blank">📅 22:07 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74899">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdXiYeuv_09uU764gD0q5Yug_ZKw9pX2LyjPe5PynEE1HUEVjpvI6dh42sQqJTWkWCTLzoI8d19B2uwygyiXrsofbNycdiB9mE9HSAFi6bLJMG-7SaibNow52y5U3OZVuoqc_R3rbxDmK8VXY-2oTnOpqYD4rkJfsEkm1zSVW_xN9nKskO7Oa0gOjq9POpkOwKQ3jbcUJlv1tI3I_vKK9AiVqYJvWUrsRJGF-QRwah1oZD7aU6KL2zKVjx_T6ag5hoDKKstcqYeaRxy0tpqutXTtr3fS0NqFYZ8_rzDypkidRXo5Kx89eHO0lYmp5MyhWIv0Fa-F9v-zOs4tNA_mJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خایه هام چسبید
مکس تو استرنجر تینگز‌ هستن
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/funhiphop/74899" target="_blank">📅 22:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74898">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خبرنگار:  همزمان با حضور شما در اینجا و حضور دونالد ترامپ در چین، مسئولان آمریکایی و اسرائیلی تهدیداتی علیه ایران مطرح کردند و گفتند که به محض بازگشت رئیس‌جمهور ایالات متحده، حملاتی انجام خواهد شد. پاسخ ایران چیست؟ دکتر عباس عراقچی:  ما به این تهدیدات عادت…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/funhiphop/74898" target="_blank">📅 21:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74897">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کانال ۱۲ عبری به نقل از منابع:  اسرائیل سطح هشدار را به اوج می‌رساند تا برای احتمال از سرگیری جنگ با ایران پس از بازگشت ترامپ از چین آماده شود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/funhiphop/74897" target="_blank">📅 21:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74896">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">باراک حسین اوباما:
ما بدون شلیک یک گلوله برنامه هسته ای ایران را متوقف و 97 درصد اورانیوم آنها رو خارج کردیم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/funhiphop/74896" target="_blank">📅 21:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74895">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کارشناس کانال ۱۴ اسرائیل:
رژیم ایران به شدت به پول نیاز داره و در حال انجام تماس‌های مخفی و مستقیم با دولت ترامپه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/funhiphop/74895" target="_blank">📅 21:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74894">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کانال ۱۲ عبری به نقل از منابع:
اسرائیل سطح هشدار را به اوج می‌رساند تا برای احتمال از سرگیری جنگ با ایران پس از بازگشت ترامپ از چین آماده شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/funhiphop/74894" target="_blank">📅 20:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74893">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اما حقیقت ماجرا چه بود؟  نه صدا و سیما دروغ گفت و نه خبرگزاری ها اشتباه کردند بلکه این خودرو دقیقاً داخل هواپیمای ترابری هرکولس C-130 آمریکایی وجود داشت. یک دستگاه خودروی پارس پلاک ملی داخل هواپیمای ترابری آمریکایی بود تا نیروهای ویژه آمریکا در پوشش مبدل به…</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/funhiphop/74893" target="_blank">📅 19:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74892">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDLulrqh7CoMfWIShNfkqPXOCGFSP5qLrF972m9iIMTku4Pa_C5wCfw1Mp9bKdUSJmmKrWjpTe8HGQoNm0BW4vHPIGqxmRfv_hfjTyr3shDle9Tz8UBg3h1YuGjTihyTfOx5_Ir_xi3iUw6k84vRGbaaxd8OvgoBPakgV3nzhU0EExrjYiSJ7wslGSy537qKlGPdkmIjJ-DIWxGF2mTtICKGC7skSYfoSncRvGsGnfqhqhkiZbjZePBSheRFdOWbih28g3VH5iL4Vo8S-JtaeX300jMvtKBZQaa_MhYNxKs1VbObahcxalSCTMFHqM8aDAPYfvghdCp0vOv-W-Wu2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال های حکومتی عکس یه پارس که جمجمه توشه رو دارن پخش می‌کنن به اسم هواپیما آمریکایی  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/funhiphop/74892" target="_blank">📅 19:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74889">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اینایی که واسشون پیامک میره اینترنت پرو شما تایید شده بعد بدوبدو میرن پرداختشو انجام میدن در جریان باشید بعد پرداخت برای احرازهویت عکس ممه تون رو هم میخان  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/funhiphop/74889" target="_blank">📅 19:35 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74888">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اینایی که واسشون پیامک میره اینترنت پرو شما تایید شده بعد بدوبدو میرن پرداختشو انجام میدن
در جریان باشید بعد پرداخت برای احرازهویت عکس ممه تون رو هم میخان
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/funhiphop/74888" target="_blank">📅 19:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74887">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">فرمانده سنتکام در کنگره:
مذاکرات حساسی با ایران در جریان است.
وظیفه ما این است که آماده باشیم، و ما آماده‌ایم.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/funhiphop/74887" target="_blank">📅 18:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74885">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Mehdi)</strong></div>
<div class="tg-text">اگه سردار سلیمانی زنده بود تا الان یه دوتا گروهک مقاومت تو اسپانیا و فرانسه ساخته بود
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/funhiphop/74885" target="_blank">📅 17:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74884">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وزیر دفاع اسرائیل لامین یامال تصمیم گرفت علیه اسرائیل تحریک‌آفرینی کند و در حالی که سربازان ما با سازمان تروریستی حماس می‌جنگند، به نفرت‌پراکنی دامن بزند؛ سازمانی که در ۷ اکتبر زنان، کودکان و سالمندان یهودی را قتل‌عام، تجاوز، زنده‌زنده سوزاند و به قتل رساند.…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/funhiphop/74884" target="_blank">📅 17:54 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74882">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cx6s87IZMtSaFJE6KJFpuAfLAwaLqWiuZT6syy_Mk31d8qyE9gW9GmPbWw0xSNRZxkRghLqzGSNGGtyc_VL2299AqCLWLfGxFul-7xvTlj3IjuH6OHZJcJyF5xa3ST7VJppQrW14gwRfpZOhc6t8GLyIOVjaJDzAqLmYl3qhaHDZoitRi3zfRKr1P6OKIEMZskb3H28fe4-mgypSXtThpApDM0oSoBvebcsFp-dtzTolJSW2qyMMMhu3gYJ1TKsuYwZ942R2VfhLM1rASavDg97cLKIi8ZdzdFGeqsfFPhLDuKEkWO4BHSZ62lAiE2gRGoILudq40K6JtIbkUJlqHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aIkU91NHSDMUDfCv4egrnPn3KG2E3cpYSQsh1tbHzxplsXnhGeQ-ku-P5h41yPMLgczWmXfaXDD6gi-PpQvq7osHwlJy6FRo4x5Q5CDLZLG_f-js-DneQllFEn3iPpCWf2XrmnNgQwNxZosYFmgpyBgQ8i07kCo4eqeOgqoK_5147GzPlAe6OvuqSDxz9AAqkSt12sIAStil3dch3GnAXg1ywRRThLgiShgbjJeYC6hfCKlgcbb2f7-mLKuaQ5IE3KRsSm8o8zH5ll5LmXZ-jNrdq7XMcvFX1QFTCyyvp6BsDQJEQ67Os6E3VkXe3AyjUZxRg6V3Q5gSElaDBPAViw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزیر دفاع اسرائیل
لامین یامال
تصمیم گرفت علیه اسرائیل تحریک‌آفرینی کند و در حالی که سربازان ما با سازمان تروریستی حماس می‌جنگند، به نفرت‌پراکنی دامن بزند؛ سازمانی که در ۷ اکتبر زنان، کودکان و سالمندان یهودی را قتل‌عام، تجاوز، زنده‌زنده سوزاند و به قتل رساند.
هر کسی که از چنین پیامی حمایت می‌کند، باید از خودش بپرسد: آیا این رفتار انسانی است؟ آیا این اخلاقی است؟
من به‌عنوان وزیر دفاع اسرائیل، در برابر تحریک علیه اسرائیل و مردم یهود سکوت نخواهم کرد.
از باشگاه بزرگی مثل بارسلونا انتظار دارم که از این اظهارات فاصله بگیرد و به‌صورت شفاف اعلام کند که جایی برای تحریک، حمایت از تروریسم یا نفرت‌پراکنی وجود ندارد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/funhiphop/74882" target="_blank">📅 17:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74881">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRiOJmP1QDr0kNlrSjT1o-f6cT71zkYxRghf_M7qGbJrI2od-OqRfyYbwxsScEdGwdvI_HsH0j1OT6adSiclmZACwnksW0WJRk5Masfy7gZDgGuZz28ZyYwfRtGTeEoOvYrCeUagJk7npd-lGfkxRd_LHR_8FQlABn1OYbhiWRge2zjbA0qFam5Dz3Mfx6AC5FUk0SnafkygikM2mh3yeMRp6E97GmSBxlV5686IvVlOlcMT2AxOyw5qjOJVI9raXAXHMrZuVZIRBpT9EDPaNo1zgkwh31WA-dl6fQuJwZsgcAePm4Ysq0dvm7FPdvkfYq_L8w5O-b9gZuFNzBancg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/funhiphop/74881" target="_blank">📅 17:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74880">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اگه دنبال کانفیگ با سرعت و قیمت مناسب میگردید از این بات استفاده کنید داره گیگی ۱۵۰ تومن با سرعت خدا میفروشه:  @vipamomamadconfig_bot</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/funhiphop/74880" target="_blank">📅 17:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74879">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اگه دنبال کانفیگ با سرعت و قیمت مناسب میگردید از این بات استفاده کنید داره گیگی ۱۵۰ تومن با سرعت خدا میفروشه:
@vipamomamadconfig_bot</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/funhiphop/74879" target="_blank">📅 17:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74876">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5Jwnh4GcY3b8qlPZFhDNmRKly6XX0Jr5qnGbHNKez1o3TKlt2e_zfuHb5pQMSTtxkIy1QqBu8YBhrgmltdwn3lk-qyVJYL0qJH-_5VPr15w3EOmX5JbjuX6wClPqEyfimq8Vdk4dseidfusZogWGYBg8xhAqjQ3gHFKLkw_-9HUto1YlGeNiSNn-Opav-Nbsr29j9w95fGFuQCld4JhP8IdXYuWn9GwFRNLLGMkrJf5HRKk4wjVjnjhNhvdsNyT39-bmB29ESAJNEuQexjG4cN-j7YHVO8hl-0wCqSroD6YYyFBErPc55AcIpmHjsoasTcQ0L0u59zToCMCpEIKxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چگونه آمریکا را قیچی کردیم؟
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/funhiphop/74876" target="_blank">📅 17:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74875">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">به عنوان یک بارسایی امیدوارم که مورینیو سرمربی رئال نشه چون در این صورت رئال دوباره قدرتمند میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/funhiphop/74875" target="_blank">📅 17:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74874">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سنتکام
تا امروز، نیروهای سنتکام ۷۰ کشتی تجاری را تغییر مسیر داده و ۴ شناور را برای اطمینان از اجرای الزامات تعیین‌شده از کار انداخته‌اند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/funhiphop/74874" target="_blank">📅 16:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74873">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/si3WNtj62IC1coI6jZzXY7KUdtWiF0Ofo41USymk70vY0StB6yKTNUtnvZ3lDTrTKZj93O2oAFaEoTid2SFG2hO8e_meMe1nx6YLuvdtdC_w0I7I3PJFJIknX8Kbcr6EGqNue9nHZnvPiFh3o5JJ-_MW__ZrnHHX5HybjwD5p3R50QNqdnCJcVCf5-JCgphFrhkHFR7Di1ZZJctzVuHJ1IcZ8_iIH7bgUxCOnUQymN4yV7JSkazo8vVP0q84TaK0671Kh_8H2PZ0e-Zn6t_aZkTUeagzyKD01j-L9cd1DKrVW3MT3yj6z5aQB8x8U2sNcmvgi5OYZb_eQ4eUAH7t1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرهیختگان
خطاب به کارولین لویت : بچه کش مادر شد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/funhiphop/74873" target="_blank">📅 16:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74872">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">وزیر دفاع اسرائیل
ماموریت ما هنوز به پایان نرسیده است.
برای این احتمال آماده‌ایم که شاید دوباره مجبور به اقدام شویم؛ حتی ممکن است این اتفاق خیلی زود رخ دهد.
اگر اهداف موردنظر تأمین نشوند، دوباره اقدام خواهیم کرد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/funhiphop/74872" target="_blank">📅 16:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74871">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مارکو روبیو
طرف چینی اعلام کرده که با نظامی‌سازی تنگه هرمز یا راه‌اندازی سیستم دریافت عوارض در این مسیر موافق نیست و موضع ما نیز همین است.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/funhiphop/74871" target="_blank">📅 16:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74870">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اگه نگران امنیتتون هستید بیایید برید از بات رایگانمون کانفیگ رایگان بگیرید که دیگه بدافزار نصب نکنید  @SonicVPNRBot</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/funhiphop/74870" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74869">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اگه نگران امنیتتون هستید بیایید برید از بات رایگانمون کانفیگ رایگان بگیرید که دیگه بدافزار نصب نکنید
@SonicVPNRBot</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/funhiphop/74869" target="_blank">📅 16:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74865">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یادم باشه یه بدافزار درست کنم اسمشو بزارم شیرو خورشید
نصبش توسط همه تضمینیه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/funhiphop/74865" target="_blank">📅 15:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74864">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اپ شیر و خورشید یک دقیقه باگ خورد شمشیرش شد ذوالفقار
خداروشکر امنه باز
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/funhiphop/74864" target="_blank">📅 15:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74847">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اکسیوس
تیم Donald Trump در حال بررسی گزینه‌های تازه برای افزایش فشار و تنش نظامی علیه ایران است.
به گفته مقام‌های آمریکایی، احتمال دارد پس از سفر ترامپ به چین، تصمیمات جدیدی علیه تهران اتخاذ شود.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/funhiphop/74847" target="_blank">📅 15:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74846">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رویترز
ترامپ از شی جین‌پینگ، رئیس‌جمهور چین، دعوت کرده تا ۲۴ سپتامبر به کاخ سفید سفر کنه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/funhiphop/74846" target="_blank">📅 14:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74845">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ
مذاکرات پکن بسیار مثبت و سازنده بود.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/funhiphop/74845" target="_blank">📅 14:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74844">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آکسیوس
ترامپ بین افزایش فشار روی ایران و جلوگیری از رشد قیمت نفت و تورم در آستانه انتخابات گیر افتاده.
در حالی که مذاکرات هسته‌ای متوقف شده، تیم ترامپ گزینه‌هایی مثل فشار نظامی و تشدید اقدامات علیه ایران رو بررسی می‌کنه، اما ارزیابی‌ها میگن ایران توان تحمل فشار اقتصادی برای ماه‌ها رو داره.
یکی از مشاوران ترامپ هم گفته ایران روی نزدیک بودن انتخابات آمریکا حساب باز کرده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/funhiphop/74844" target="_blank">📅 13:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74843">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پاسخ عراقچی به ادعاهای امارات در اجلاس بریکس:
ائتلاف با اسرائیل هم از شما محافظت نکرد.
من در سخنرانی‌ خود نام امارات متحده عربی را ذکر نکردم، به خاطر حفظ وحدت و ترجیح دادم به آن اشاره نکنم. اما در واقع باید بگویم که امارات مستقیماً در اقدام تجاوزکارانه علیه کشور من دخیل بود. زمانی که این تجاوز آغاز شد، آنها حتی از محکوم کردن آن خودداری کردند.
آنها اجازه دادند از سرزمین‌شان برای شلیک توپخانه و تجهیزات علیه ما استفاده شود.
همین دیروز فاش شد که نتانیاهو در زمان جنگ به امارات و ابوظبی سفر کرده بود. همچنین آشکار شد که آنها در این حملات مشارکت داشته‌اند و شاید حتی مستقیماً علیه ما اقدام کرده باشند. بنابراین امارات شریک فعال این تجاوز است و هیچ تردیدی در این باره وجود ندارد.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/funhiphop/74843" target="_blank">📅 13:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74842">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">چین که چیزی نیست جرعتشو داری برو کره شمالی  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/funhiphop/74842" target="_blank">📅 13:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74841">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">چین که چیزی نیست جرعتشو داری برو کره شمالی
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/funhiphop/74841" target="_blank">📅 13:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74840">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پشمام معین میخواد برای همکاری چین و آمریکا آهنگ بخونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/funhiphop/74840" target="_blank">📅 13:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74839">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کاخ سفید اعلام کرد دیدار و گفت‌وگوی ترامپ و شی جین‌پینگ «
مثبت و سازنده
» بوده و دو طرف
مذاکرات خوبی
با یکدیگر داشتند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/funhiphop/74839" target="_blank">📅 12:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74838">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آمریکا به چند غول تکنولوژی چین مثل
علی‌بابا،
تنسنت،
بایت‌دنس
و
لنوو
مجوز خرید چیپ‌های پیشرفته
H200
انویدیا
رو داده؛ اقدامی که نشون میده
واشنگتن فعلاً نمی‌خواد جنگ تکنولوژی با چین بیش از حد شدید بشه.
این خبر برای
انویدیا
و کل بازار
AI
مثبته، چون هم
فروش انویدیا افزایش پیدا می‌کنه و هم شرکت‌های چینی می‌تونن مدل‌های هوش مصنوعی قوی‌تری توسعه بدن
.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/funhiphop/74838" target="_blank">📅 12:51 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74836">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کاخ سفید اعلام کرد در دیدار ترامپ و شی جین‌پینگ، دو طرف بر
حفظ امنیت و باز ماندن تنگه هرمز
تأکید کردند و همچنین برای
گسترش همکاری‌های اقتصادی
به توافق رسیدند
.
طبق این گزارش،
چین قرار است سرمایه‌گذاری‌های بیشتری در صنایع آمریکا انجام دهد
و در مقابل،
دسترسی شرکت‌های آمریکایی به بازار چین نیز گسترده‌تر شود
؛ موضوعی که می‌تواند روی معادلات اقتصادی و تجاری جهان تأثیر مهمی داشته باشد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/funhiphop/74836" target="_blank">📅 12:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74835">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یک مقام کاخ سفید اعلام کرد
آمریکا و چین
در موضعی مشترک تأکید کردند که
ایران نباید تحت هیچ شرایطی به سلاح هسته‌ای دست پیدا کند.
این اظهارات در حالی مطرح شده که
تنش‌های سیاسی و مذاکرات
مرتبط با برنامه هسته‌ای ایران همچنان زیر ذره‌بین قدرت‌های جهانی قرار داره.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/funhiphop/74835" target="_blank">📅 12:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74833">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3a3103e12.mp4?token=rseO7r5y6HBUf8jYbSfG_a5fzJ9VtxnZ5iN9XLmu_btXbrBIZ3WWiIK1eERDCJoo4aQBzm5mU1mQgZMBYwAX9ywD2KHaN4jpIhwWM2xH1v_XBtiO7hpxVlaatt8ZS_-C_hnva4Yf0EnXN7fJKyzQU3SeCozWH703bsQYZtWC0fbtoeCQyqjs1JKb86v0suypgbp1Te5GaG3D75PG9DSjKazq80ArC20ehbiBT5kC5nKPEwV3bWflwUo4wFUy3lv0B_oJc8V1Y1fZVVj3YztpHH5s-u8SfhTByrRT62plCDaVnp8Obyfdg617_zt3fqD20OWsdHW7-96EDgj556uaUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3a3103e12.mp4?token=rseO7r5y6HBUf8jYbSfG_a5fzJ9VtxnZ5iN9XLmu_btXbrBIZ3WWiIK1eERDCJoo4aQBzm5mU1mQgZMBYwAX9ywD2KHaN4jpIhwWM2xH1v_XBtiO7hpxVlaatt8ZS_-C_hnva4Yf0EnXN7fJKyzQU3SeCozWH703bsQYZtWC0fbtoeCQyqjs1JKb86v0suypgbp1Te5GaG3D75PG9DSjKazq80ArC20ehbiBT5kC5nKPEwV3bWflwUo4wFUy3lv0B_oJc8V1Y1fZVVj3YztpHH5s-u8SfhTByrRT62plCDaVnp8Obyfdg617_zt3fqD20OWsdHW7-96EDgj556uaUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با نحوه دست دادن همیشگی خودش خواست شی رئیس جمهور چین رو به سمت خودش بکشه ولی شی خیلی محکم سرجاش واستاده بود و ترامپ موفق نشد.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/funhiphop/74833" target="_blank">📅 12:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74829">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">هاردن چه مادری از دیترویت گاییده</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/funhiphop/74829" target="_blank">📅 12:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74828">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryFgPN6JFs0bg_ANd6x9lDES89GzzdkW7A5MIZsQV0CwOZJYhLwVL-kxT9dpgri_Gq7G9QyweBuRFRVSJTOwepyR0dsOMOaYdS_F6ivgrjctkvxif31iJ6PnewowxnrFzcZSZd29VT9tvbGMjxdBfU3OGszfibY_SwLpPx6FdeKzJp5Jzam1PTJwXjAF_CaRUnb3S8W0aDx4G5DJQUpPpr4oNbD8KzcUNNWJ7QqX1B-KO6HR4hjh0RZuY0F-Tyg_m1fPw51sZhN2WmNXJd-CgYxeesHkYmR1cIMjqxrJFbX2qqyEeJIxf2AGuh5koP0fXQAaoRUj8mzWHKhGwWawfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت بلاکس
📵
قطعی گسترده اینترنت در ایران وارد
هفتادوششمین
روز خود شده.
این محدودیت‌ها حالا به شکل یک اینترنت
طبقاتی
اجرا می‌شود.
مدلی که در آن فقط گروهی خاص به اینترنت آزاد دسترسی دارند و بخش بزرگی از مردم عملاً از جریان آزاد اطلاعات
محروم
شده‌اند.
ساختاری که خود مقامات سال‌ها
مدعی مخالفت
با آن بودند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/funhiphop/74828" target="_blank">📅 11:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74827">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">به به  سازمان عملیات تجارت دریایی انگلیس:  گزارشی از وقوع یک حادثه در فاصله ۳۸ مایل دریایی در شمال‌شرق فجیره در امارات دریافت کردیم.  قایق های تندرو سپاه پاسداران یک کشتی را که خارج از تنگه هرمز لنگر انداخته بود را تهدید به هدف قرار دادن و سپس توقیف کردند…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/funhiphop/74827" target="_blank">📅 10:58 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74825">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1MwEXgLXMtSBtuHxWxbwHDtNyFU0ae3D3_qrNRoWflGsDPn49l3FwKQoplr3uBQSBHCnZrGh3RpCXhF2WRMA0tw9SkxxQKJcHV30AEXn_bs4YuTc2_F8Qi-MleavqD-PRVgjDzRH-w3sKlcnlX3tzXcRloRCGY8uTc11C-w-odsxjeb89mFZs_3bwTqef1Jjsvo0FRGyX3TgtigL6u0pciqZG20TAycpJvEHP0YSPpy95KDOfxNEmPFUdPySGYJXPDVPWqfGe9jOkJAhThVpXXwzgxkGqU8O5_4sJqwGSCG6MquEfxWgZPtgIwYLO35juRyd1i8cZeMTb8FOkYM7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به
سازمان عملیات تجارت دریایی انگلیس:
گزارشی از وقوع یک حادثه در فاصله ۳۸ مایل دریایی در شمال‌شرق فجیره در امارات دریافت کردیم.
قایق های تندرو سپاه پاسداران یک کشتی را که خارج از تنگه هرمز لنگر انداخته بود را تهدید به هدف قرار دادن و سپس توقیف کردند و اکنون در حال بردن آن به سوی بنادر ایران هستند.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/funhiphop/74825" target="_blank">📅 10:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74824">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDX6CsKmr2xuWTXBzQXJxxztiTTlq4UI5NumETUPh8qTtTK3WIBANWevw2mwOf_QUdUbjnGioSvXpuRdQP-5M__n5my_Vlyy_DGh1sKy5jWrgJEyiOqcddct_Kn5oXXiwHTcJzXHaWAuH03ze0mwqrAZM9GcppH0Ec9dSdVBrOSeaF2ovkBbhMml4uPNtfIO1MN90qG9gNoWrl39mAK80zLM28g_7gyYiMflKWsb0uiqqQeW4F980jYGKCQ0B1n-fAybTSUqQfJEF9jaw3Pe-V1MEIPlp14qjJ6IF9sLZngzS39oTLlMS5WUnq9hFwYSEIL61F5Oid2EPiIW0xT76A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی پسره قراره 6سال منتظر بمونه؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/funhiphop/74824" target="_blank">📅 10:27 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74822">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">حمید رسایی:
تنها دلیلی که برای تعطیلی مجلس به ذهنمون میرسه اینه که نمیخوان مجلس با نطق ها و تذکراتش تو روند مذاکرات خللی ایجاد کنه.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/funhiphop/74822" target="_blank">📅 10:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74821">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سخنرانی دکتر عراقچی در کنفرانس بریکس: من به نمایندگی از جوانانی صحبت می‌کنم که نمی‌گذارند گرد و غبار جنگ آینده روشنشان را پاک کند، به نمایش از مردمی که تحت بمباران وحشتناک، تصمیم گرفتند استوار بایستند؛ به نمایندگی از مادران میناب که زیر غم از دست دادن فرزندانشان…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/funhiphop/74821" target="_blank">📅 10:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74820">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سخنرانی دکتر عراقچی در کنفرانس بریکس:
من به نمایندگی از جوانانی صحبت می‌کنم که نمی‌گذارند گرد و غبار جنگ آینده روشنشان را پاک کند، به نمایش از مردمی که تحت بمباران وحشتناک، تصمیم گرفتند استوار بایستند؛ به نمایندگی از مادران میناب که زیر غم از دست دادن فرزندانشان خم نشدند.
ایران از کشورهای عضو بریکس و همه اعضای مسئول جامعه بین‌المللی می‌خواهد که به صراحت نقض قوانین بین‌المللی توسط ایالات متحده و اسرائیل را محکوم کنند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/funhiphop/74820" target="_blank">📅 10:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74819">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ و شی جینگ پینگ چه در نوشابه ای دارن برا هم باز میکنن</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/funhiphop/74819" target="_blank">📅 10:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74817">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdgyoD9V6El1Ax-3jFAx5p4JZbd-sFUPLMZ62jnKayu9nSj4MPQq72GK-IE9TxOqEz7r8HIKYkPiOlmYOEIQieZiN7eY8DNfEQ-BEXAE_4163dBk-pWvIH6eqUrGbJA8L1xYEA6gUeqtwESfIk3MmKAzdnu4OSXiiT5U1uRQcG1xryFX5m73XNfXIMGArlO3K8R1R9MC3pACQrevavo4x_CZE2NNM977u57tu6wFuVcgCPTdTWE8iocKwgAxYs7YUam0woG8ANLAwX6hVVzz-FLQj909yOzELAWnek3E66acFCyqQBqL7KtiS4PsG4CBqcgX5vmrRRFOoFxjYNkPXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل اینکه معین قراره واس تیم ملی بخاطر حضور تو جامجهانی اهنگ بخونه.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/funhiphop/74817" target="_blank">📅 03:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74816">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مارکو روبیو:
امیدوارم چین نقش فعال‌تری در متقاعد کردن ایران برای خودداری از رفتارهایش در منطقه ایفا کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/funhiphop/74816" target="_blank">📅 01:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74815">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxtIf5OSllMftLL8Q9G5QSfYfnib3xb12ic9xERLIUnNPiCI5OkbGfn8PbnjJxUIYaV0vU3y9ZJkemV8g39txEjVsGwNwP7NfYB-5XtxUV_Sx9TgirwrjwFOZZG4NJQhrp6cLYkg5p6OT2y2kKAuCskGOpLNPoGaKXrK3o9N9MLNUWIgyaHcM5tmEMMcwDIcc9_LHiE8klH5AVGkpKHSxecVWt6Zqqg-_U1Z09giehsmyt_a-Y_BF0xwsUI7V9I9FHsozf1tje3Lru725DYiQPw3I2bVFnKviOsdTLkAMQetf8Y-ecRMFfLpAT3TZS-j9JF_w9_VcugQkYZzQfzzyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز عصر دفتر نتانیاهو گفت طی جنگ ۴۰ روزه، نتانیاهو شخصا سفر مخفیانه‌ای به امارات داشته تا با رئیس امارات دیدار کنه و چند تا مقام نظامی هم تو این مدت رفتن اونجا که درمورد جنگ هماهنگی ایجاد کنن.
الان امارات کلا همه چیو تکذیب کرده گفته ما هیچ‌کس رو اینورا ندیدیم و اینا همه‌ش دروغه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/funhiphop/74815" target="_blank">📅 00:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74814">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مثل اینکه معین قراره واس تیم ملی بخاطر حضور تو جامجهانی اهنگ بخونه.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/funhiphop/74814" target="_blank">📅 00:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74813">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مثل اینکه معین قراره واس تیم ملی بخاطر حضور تو جامجهانی اهنگ بخونه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/funhiphop/74813" target="_blank">📅 00:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74812">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یه بات زدیم که کاملا رایگان با رفرال گیری میتونید کانفیگ بگیرید ازش، چون جدیده کسی استارتش نداره و راحت با پخش کردنش بین دوست و آشنا و گپا میتونید چندین کانفیگ رایگان بگیرید   @SonicVPNRBot</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/funhiphop/74812" target="_blank">📅 00:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74811">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یه بات زدیم که کاملا رایگان با رفرال گیری میتونید کانفیگ بگیرید ازش، چون جدیده کسی استارتش نداره و راحت با پخش کردنش بین دوست و آشنا و گپا میتونید چندین کانفیگ رایگان بگیرید
@SonicVPNRBot</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/funhiphop/74811" target="_blank">📅 00:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74810">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">جی‌دی ونس:
فکر می‌کنم مذاکرات با ایران درحال پیشرفته.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/funhiphop/74810" target="_blank">📅 00:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74809">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a5eb89bfd.mp4?token=D2YhnDx6-yFRHZvwhDxwk4QfNKHkGvDCxnH9CoCZcOfrXGcm9054mdxcTJpsx_h94PsSkNi_m6cpbR3FuAhzipYKvLqfDaiY-AgXg16qqnG20za_iMgNzMDEQJ7WYsjyfzC2EmHsOzPsUcunVgQS_HUbDp7PnyiA48lbm277vas26bLbYB0H-4BQJZDZX923tqcTGB4ilIbYoZy6btBkQae9EKF_5M9EvlC4ZAk-qfCqiWr7sGC1CgRHgdyIApRJt7lp6hgQ4T5wXmqsxpij4vBAj28uM9hlS3jrEScdQWm1qecJfJstHJ5r8MtKrrrC9ke7tH4xpOZ0DGxQo4MYLnCO5_adCPYMh6AGAVcZ4WCkWXh2Jq_CgcyAyfNsjFtijbBuZEPFg_Yrw_LDA3WAbmGc4smLZszy1sOhvpn0vqVOl0XaXEjXH81vG3pPizzIGacgcIgS4WD1bNvkll5oBYyIpIMnf0G42axyE_Wk374NdLcAvPEjTF6BwI97P6sx7JwU-zmPb_2n2c7erXHys449iWz7Znimj-okgsCHo2HhHe6HCQgyXCeTaK8Bt_SvPHTz0-GUgoiEH1VhNSE15W_St99lUFrrviH3uf9k72383wtnz9DgdebS1U_CDemYlDiUOA1RQwCo9soN8DEA5bdFt-CNtPpIKEUPVYtaKzU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a5eb89bfd.mp4?token=D2YhnDx6-yFRHZvwhDxwk4QfNKHkGvDCxnH9CoCZcOfrXGcm9054mdxcTJpsx_h94PsSkNi_m6cpbR3FuAhzipYKvLqfDaiY-AgXg16qqnG20za_iMgNzMDEQJ7WYsjyfzC2EmHsOzPsUcunVgQS_HUbDp7PnyiA48lbm277vas26bLbYB0H-4BQJZDZX923tqcTGB4ilIbYoZy6btBkQae9EKF_5M9EvlC4ZAk-qfCqiWr7sGC1CgRHgdyIApRJt7lp6hgQ4T5wXmqsxpij4vBAj28uM9hlS3jrEScdQWm1qecJfJstHJ5r8MtKrrrC9ke7tH4xpOZ0DGxQo4MYLnCO5_adCPYMh6AGAVcZ4WCkWXh2Jq_CgcyAyfNsjFtijbBuZEPFg_Yrw_LDA3WAbmGc4smLZszy1sOhvpn0vqVOl0XaXEjXH81vG3pPizzIGacgcIgS4WD1bNvkll5oBYyIpIMnf0G42axyE_Wk374NdLcAvPEjTF6BwI97P6sx7JwU-zmPb_2n2c7erXHys449iWz7Znimj-okgsCHo2HhHe6HCQgyXCeTaK8Bt_SvPHTz0-GUgoiEH1VhNSE15W_St99lUFrrviH3uf9k72383wtnz9DgdebS1U_CDemYlDiUOA1RQwCo9soN8DEA5bdFt-CNtPpIKEUPVYtaKzU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدرقه تیم ملی برای رفتن به آمریکا و حضور در جام‌جهانی ۲۰۲۶ با شعار مرگ بر آمریکا
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/funhiphop/74809" target="_blank">📅 23:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74808">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خبر تکراری و حوصله سر بر
صدای انفجار در اربیل عراق
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/funhiphop/74808" target="_blank">📅 23:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74807">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رپر ایرانی از عجیب ترین موجودات تاریخه، یکیش میگه چرا از خون بچه های میناب نمیگی در صورتی که چندین هزار نفر کشته شدن و جیکش در نیومد و تخم نکرد حتی چهارتا پست بزنه واسشون، اون یکی میگه چرا از خون ریخته شده چندین هزار نفر نمیگی در صورتی که خون ۱۷۰نفر از کشته شده های میناب براش ناچیز تر از اون چند هزار نفره، جفت طرف جون کلی آدم از این مملکت شده براشون سپر بلای عقاید تخمیشون، اون یکی ادعای وطن پرستی داره ولی تخم نداره به کسی که وطنشو بیش از ۴ دهه مورد عنایت قرار داده چیزی بگه، یکی دیگه اونور میگه وطن پرسته پرچم فلسطین نمیگیره دستش ولی خایه های اسرائیل تا ناموس تو دهنشه.
اینور یارو تخم نداره به کسی که اینترنتشو قطع کرده چیزی بگه میپره به کسایی که خواهان جنگ بودن در صورتی که بود و نبود اونا فرقی نداشت و اولو آخر جنگ رخ میداد، اونور طرف میره کنسرت میزاره که کمبود درامد از استریمشو جبران کنه
خدایا کیرم تو این کشوری که مارو توش اسپان کردی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/funhiphop/74807" target="_blank">📅 23:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74806">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شجاع خلیل زاده:
قهرمانی در جام جهانی سخت ولی شدنیه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/funhiphop/74806" target="_blank">📅 22:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74803">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dwCdLCSl60dUyeCI2maq2kHXmRWaD1maQt-1LhxzsQT8STFKQ3GyIqk63DFa6Ia78HvOrh4wMkX9_4WrLJZJL2TI8cAV0CXok3MRSzrz-pdXKJiS-8cqPC-uTDKGR67d86BzOvupofP8CYD-UK03L5tsJ-aHDGzIaBHuE8_f0klSZ7Vfbj-O4yfARxHwyWf6BYh8CC0MxfF2DxniXrL_sL-covh0B-MlLc7rTofGZfGUz1AiuP8xO746kMxDaml_PcDvKY6y51XZdnEEMCuRnGwtuceHIASG_Gn8Vc3qLS5EQFOARcR6e8QmqKk2o_trOtL1HJAJ5vVcPEgncGUE4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tv9nL3uMaupydxySAAuOBUBnezPsYljG5y8rsozRBzm2AQYeBwkke_Xw2LiQsC9QYgr_I52on14sq_uBs5QP4Y_3iX2ZfaWClkGXX2ODwYifwWcdD4I3Usujhg-3u_-OMajgGNRflMp9Yk7172kDjMJPYtoD-1T6ITrrAYsAW5N45YTGqqGvsV0SDWwzkOy4q3x_aqdWxnV9hNXh2Jzragy090JxS5XCXcA-197gYZ9mjiRBQGWi5h3xx8-o3_EhDkKf_-pB-fy73mlaKe7IMONhLnIWaiSbt-2GaS_EeivOluHjkhYyb9oG9HMwQjL2BCg2OdRrG9_cDr_ECrgR6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H3Lbavwl91r2q-_aOFY6-qjp6wgTLhNCmmcSw2fvGn-BLOp7ObPNogjDxdIXIhSMV2DNDAal2btojsNTT1W4QMOXU7EDSwLlxMo8IDg6nvtglmQWknJ2N6t2di0v0ePsPjMLuebORvPntSh67A848JLZi82B-MSv0gUv-oeSKErkPwXZSeouElLezuq_B2_hNpURetdJ0uIivPx8ocRdC20keKH6yw5iTLj01C0hhtuAvXlD2DWUX_tTBm4HSyj9tEktpnCLnmdy4kp8pvic0WX3CgUs7amJU_znMR3MrhU3RS7RjqASeU19ZgvBEvwYUnC0SoHRRqV3xF_gkhZPiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هم من میدونم هم شما میدونید که قراره بزنن و امیدوارم از این وضعیت فعلی خلاص شیم
طبق اسناد از ابتدای ماه مه تاکنون، 50 هواپیمای ترابری آمریکایی وارد پایگاه‌های این کشور در خاورمیانه، به‌ویژه پایگاه موفق السلطی در اردن، شده‌اند.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/funhiphop/74803" target="_blank">📅 22:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74802">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سوپراپلیکیشن ایتا:
امکان ارسال فایل تا حجم ۲۰ مگابایت مجدداً برای همه کاربران فراهم شده است.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/funhiphop/74802" target="_blank">📅 22:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74801">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNwIneRxmcNGbeWY86nfAh8o3Ln7zqmsY7pRX2SJeBJA1T965XpurteOSlt_Sye6z6sE1yVcXS_fD7QV_2eTpWd_3TkLJ4mcnjH5RxNLon_OMC1iRdnaZbjIZUaOoxMAOJt7mkDTXM3TvZQs4Cen_7cNk-17P6xuxlp00tXIYtvDn5Nbpxgn0HibEk0FsQhsYznKj6rQL_O2lQzq2hx3XbcDiFi9HnJXDWiuTPh2cqoF2xnMBllLzJQ4GqR3UYfcX_P5fDqf4FacMHBnDMYfdTDWQfgT2ytfjMu7cjOFCb3KAaWwsOM7JIcgDrNIcBCLXJuxnSORaZcraIBKMLYu5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئالیا درگیر نیمار شدن وینی بودن، امباپه نیمار شد
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/funhiphop/74801" target="_blank">📅 22:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74800">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
تخفیف ویژه زیر قیمت کل تلگرام!   دوباره تخفیف رو تمدید کردیم!
🧃
قیمت هر گیگ فقط 149 هزار تومان!
😈
( فقط 400 گیگابایت موجوده! )
💥
✅
بدون ضریب و بدون محدودیت کاربر
✅
دارای لینک ساب برای مدیریت حجم
🛡
تمامی سرور ها دارای پشتیبانی می‌باشند.
🤩
@TornadoAdmin…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/funhiphop/74800" target="_blank">📅 22:08 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
