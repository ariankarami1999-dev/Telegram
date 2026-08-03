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
<img src="https://cdn4.telesco.pe/file/jG8lb3WrLKFdL9tZMulcP6Pi6-_bKDPMzqvTsBq4TLAj2tALaDJCEtYI27Fpln92udpfY-TVzldOw3twUQWFH6TEQyiMYGtGyvOvsalMrk9Schd5m8AF8o2BD2HjwViiRHoZlsfKIyTA5CymoHdTL6D8vPam_a4Yow9fffSYuyjoIuaW3BZT0wcld-mOOy14uSvCkyNQjWKGFGXK5q6ZctdloOFqwk77motg4-cqnvAzHDYswGtk3OtSOSPhTsxx-kxni0weC4ZCph3j_Ob8GEE-npklHVOeCzC2uYqrr8pFLtkgQDBBWwjfrIeggQq027KdTYCtQr6qI427q48nDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.06M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 17:48:11</div>
<hr>

<div class="tg-post" id="msg-678099">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
برخی منابع عربی از شنیده شدن صدای انفجار در امارات متحده عربی خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/678099" target="_blank">📅 17:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678098">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f75305259.mp4?token=DQO8f6m02wxeTjc-dS63k-HN1_Z2sd3dzdvTa4YRwCDdW6jzFROM-brrFa_Obqwhn0lyvo8Yra8yms2QmLS4tBxPoKqEDehvsrElqveejCiRWrlozWQtXm2spAcKnTcvZPTHlBtq2YlnBZQsMwdnzkd45cHxqeGkMgKXTRYPp4KXiVQY8Y5gR67nBx5XDrAc9KE8CQkRLjWqyjkQUBXP3kr76aGs8zZAeD0eBfi4XIUQlMGJXssz6Gjq2BN225dCqlLs0ald3-VxkuhnHSfU25Oh-6Cm-i2QaeFpw90SNCHThDU9of72SfMhR6OmN1ZNTljZFe7cYPNJZyrOsTgcuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f75305259.mp4?token=DQO8f6m02wxeTjc-dS63k-HN1_Z2sd3dzdvTa4YRwCDdW6jzFROM-brrFa_Obqwhn0lyvo8Yra8yms2QmLS4tBxPoKqEDehvsrElqveejCiRWrlozWQtXm2spAcKnTcvZPTHlBtq2YlnBZQsMwdnzkd45cHxqeGkMgKXTRYPp4KXiVQY8Y5gR67nBx5XDrAc9KE8CQkRLjWqyjkQUBXP3kr76aGs8zZAeD0eBfi4XIUQlMGJXssz6Gjq2BN225dCqlLs0ald3-VxkuhnHSfU25Oh-6Cm-i2QaeFpw90SNCHThDU9of72SfMhR6OmN1ZNTljZFe7cYPNJZyrOsTgcuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚗
هر آقایی یکی از این جاروها توی ماشینش نیاز داره
👨‍🔧
🎥
برای دیدن کاراییش ویدیو رو حتما ببین
❗️
✅
سه روز ضمانت بازگشت
🏠
پرداخت درب منزل
تعداد محدود! همین الان کلیک کن روی لینک زیر،
تخفیف ویژه
رو دریافت کن
👇
khabarfouritel.affdn.com/lead/44273
➖
➖
➖
➖
➖
➖
➖
➖
➖
5000 محصول تخفیفی دیگر
👇
khabarfouritel.affdn.com</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/678098" target="_blank">📅 17:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678097">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0geMGIEh1G8ETTKnAArdBkzTjAuMMINHswIjg7QICS2chY1xdO4Cu2W2sfAk57R2F2a-8akUSj899HJnzr_BhnulF1PqhHAt8ZltNV1-KdMkXtUCKFIziVC6LuXqhDKZwB-9iUfO2477YN7ALrZnBJ0zjuPGgOv3LIKsnfe5T0bMKmu_UpfizmhZ88r70QqQmm_0wvB5CEUeLd_BiVNPtCdRHZwbTgVTFXzHstXvcdomO-g_w-mxB-s3y9hGViQ--FvITx27YDH_DVTysLuZlfbO6wyiaNaQljylUwMrlIWLLsEPgnJ1d3qh0gwjubStP8IeiwMCp_lvE_Yg_lzlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت مژده لواسانی از اولین زیارت اربعین مادران داغدیده میناب؛ روایتی از دل‌هایی که سوخت
🔹
مژده لواسانی از روایت مستندی با حضور خانواده‌های شهدای جنگ رمضان خبر داد که اولین زیارت و اربعین آنها پس از شهادت فرزندانشان محسوب می‌شد.
🔹
لواسانی درباره روایت این مستند عنوان کرد: من هر ساله در اربعین حضور دارم و معمولا برنامه‌ای برای اجرا به من پیشنهاد می‌شود که همیشه استقبال کرده ام. اما امسال به دلیل ماهیت گفتگومحور و متفاوت این مستند، اتفاق بسیار ویژه ای برایم بود. به نظرم الگوهای تکراری مانند حضور چهره‌ها و مهمانان معروف کلیشه‌ای شده است، اما این فضا همچنان بکر و تازه بود و خود من نیز از آن تأثیر عمیقی گرفتم.
🔹
مستند راویان پرچم سرخ به زودی از شبکه یک پخش می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/akhbarefori/678097" target="_blank">📅 17:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678096">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
آکسیوس به نقل از یک مطلع: نماینده ارشد شورای صلح و مشاور این شورا امروز با نتانیاهو دیدار کرده و به او ابلاغ کردند که باید حملات به غزه متوقف شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/akhbarefori/678096" target="_blank">📅 17:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678095">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/069f15d0bb.mp4?token=Ska2EqK5tWie-3eSgkGj6gXusKIgFg3zNdig7J4HaXS2tu10XG-IEBC-YSUDylrRaKbwnKTFXIR7fhc_dKcJKeXsANPDqqNZWEm8VNUO6f1tPGnqIJqsKO3EP3AZW61r5hkeSirHOnBkos712KXW-1-W3qiA6r8q2_BB_o-2odrqZHXvIcIE5DNtk7qpnSNzuv2BW4vB1tN5kEUKmb3EOC7B76xka87SpOV5b--5NOQlLaYGtfc5LnH6SXq2c-X0WtWbDDHHbkg4qv2ysNAqagDV1JvYN62i7VWQ_omOePXqU7uwXp4MX8EMZuU5t9K61AbBphj3J6wwgZ0VZQN8qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/069f15d0bb.mp4?token=Ska2EqK5tWie-3eSgkGj6gXusKIgFg3zNdig7J4HaXS2tu10XG-IEBC-YSUDylrRaKbwnKTFXIR7fhc_dKcJKeXsANPDqqNZWEm8VNUO6f1tPGnqIJqsKO3EP3AZW61r5hkeSirHOnBkos712KXW-1-W3qiA6r8q2_BB_o-2odrqZHXvIcIE5DNtk7qpnSNzuv2BW4vB1tN5kEUKmb3EOC7B76xka87SpOV5b--5NOQlLaYGtfc5LnH6SXq2c-X0WtWbDDHHbkg4qv2ysNAqagDV1JvYN62i7VWQ_omOePXqU7uwXp4MX8EMZuU5t9K61AbBphj3J6wwgZ0VZQN8qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عاشقانه‌ای از جنس فلز و سیلیکون؛ اولین ازدواج ربات‌ها در دبی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/akhbarefori/678095" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678094">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
سی‌ان‌ان: سنتکام برای مقابله با مقاومت ایران ایده کم آورد
🔹
شبکه سی‌ان‌ان به نقل از منابع آگاه گزارش داد فرماندهی مرکزی نیروهای تروریستی آمریکا در یک ایمیل به تحلیلگران نظامی از آن‌ها خواسته است برای آنچه «مقابله خلاقانه و غیرمتعارف» با ایران خوانده شده است، راهکار ارائه دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/akhbarefori/678094" target="_blank">📅 17:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678093">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7hecKzL5HZyJblfWMFNcjCKeqEuQvQCRgUXh2zb4lYClIvR0QPbPfdWCR1zbN2VBvOcp9xJnNXVgbfPE3HEyPndYktZhcAaSRicIgiPa65Nl6Pgj2zQNHrfQay3WSgUp5vNVRr6FgeFiweoDmNMqKUzw1_kS40MUeoLgXhnOc9kOia-TsFSBBnh_TECaGgA3sQGAif21vjR2IMfbch2bg2hv9XqRvr1zb5zeAUMXf8M1or7abBxlJ4LSmhcl_uKETGXS2W7SRo0iv21HPGhJbWTN1JqpXaMydiSxHA5yy_LwqrIJXi5tFpjgEIyeh1EqZHP3Jg5KXoPKR9YF855VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیست هزینه‌های ساختمان که هر مالک و مستاجری باید بدانند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/akhbarefori/678093" target="_blank">📅 17:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678092">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
تیزر قسمت بیستم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای علی لعل یوسف که با خوردن یک آبمیوه مسموم، روح از جسم ایشان جدا شده و توسط یک دست قدرتمند آمیخته با خشم و مهربانی به سمت بالا می‌رود و در آنجا آیه‌های قرآن را به تکرار شنیده و اینکه مهم‌ترین اصل آفرینش افراد در همه ادیان الهی، انسان بودن و زندگی انسانی قابل قبول درگاه خداوند است را درک کرده و بخاطر کارهای نیک و بد دنیوی‌اش پاسخگو میشود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: علی لعل یوسف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/akhbarefori/678092" target="_blank">📅 17:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678091">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
نمایش بنر منقش به ابرمرد شهید تاریخ در بین‌الحرمین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/678091" target="_blank">📅 17:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678090">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fp8iE47rDGKBxbkD9LRFbamWUs9bo0k430iucY1T1IjKw1OyYpjUtec6lkaQIPAxX27A2jQGXtSvZd9n8FiQDs0KlEVefYU6b_VUmKqz_gEejYeM_I3ZpHsz9_SIGOF-P8MccZOLDjiDJVihThS69-bZJuhvKN86i-TLiFWN6IcGAGr7yh3i6MM9uHa0wY6Wtn5kJS8qumzn7YpzCrSn5stKYIebTqb_Qd9jcElrWlVLIJux6GbbJhbSJsXWxc9xHsxmHkrD16bPTR9hAWEiwL0xVahQ9oBk3BsIlLeL2YD1KQqhCDot4uvtaCm5FJwU-Rj6R6dVJSsfpNYynY7Fxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون شوراها در مجلس: خدمات شهرداری تهران در اربعین رضایت‌بخش بود
🔹
سخنگوی کمیسیون امور داخلی کشور و شوراها در مجلس در ارزیابی اقدامات شهرداری تهران، بیان کرد: شهرداری تهران در مراسم‌های مختلف، از جمله تشییع پیکر رهبر انقلاب، عملکرد بسیار خوبی داشت که جای تقدیر و تشکر از همه کارکنان این مجموعه دارد. واقعاً خدمات ارائه‌شده بی‌نظیر بود و آن چیزی که نیاز بود، تا حد امکان انجام شد.
🔹
بیاتی درباره نقش شهرداری تهران در خنثی‌سازی جنگ رسانه‌ای دشمن نیز گفت: دشمن در کنار جنگ نظامی، جنگ رسانه‌ای را نیز به راه انداخته است و موفقیت‌هایی را که ندارند، بزرگ‌نمایی می‌کنند. البته در میدان عمل دیده می‌شود که شهرداری و دیگر مدیران حکومتی ما به بهترین شکل در حال تلاش و کار هستند.
🔹
وی همچنین عملکرد شهرداری تهران در خدمات‌رسانی، برگزاری مراسم‌ها و فعالیت‌های فرهنگی مرتبط با اربعین را مثبت ارزیابی کرد و از تلاش کارکنان این مجموعه قدردانی کرد./ مهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/678090" target="_blank">📅 17:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678089">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8HDegnBjK6xrw1ChuBygfOrZVPIYZ0LZoeFrTUcsBRT88YCPGdgO2QoYJvaLpBO-OedoZTrr8dAjVk6HASJcPiwr5rUHmyjBZrlgOrFfzkzzw8D7lZYt0LHfj4klT8fPwpTIzDymKL1SiqWr0B4yE9Gw7dPuJIqshCStOwp3mHWhVGuvVbBCmaj62tHeUrx8WYI4CvydPEFJO2QLNfPaHkWQ4vb7ux1-FAE8_ibmx9Be0-qllJMX0ozPmQsT_mKrdAc4mKHdbFVWtslSjE8SRdSt0BH9XwEt72kYv95l0-CwCfaAZS26pDdtMU60tvBpJ-xme8yE784Ni9FI-rcmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۲ عامل موساد اعدام شدند
🔹
امید بهزاد و پوریا صفوت، به جرم همکاری اطلاعاتی با رژیم صهیونیستی و ارسال مختصات و اطلاعات مراکز نظامی و امنیتی، بامداد امروز پس از طی مراحل قانونی و تأیید دیوان عالی کشور اعدام شدند.
🔹
این افراد در جریان جنگ رمضان و جنگ ۱۲ روزه…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/678089" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678088">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
به‌صدا درآمدن آژیرهای خطر در سفارت آمریکا واقع در منطقه سبز بغداد در مرکز عراق
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/678088" target="_blank">📅 17:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678087">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHVPcwFcHQFW0HikVTqm8D70WbYW8PcXK8TuEeRUsHNmJmYyQ_kP2PdlXOWtIbN4PibWD2rKl45P8w9OzvPT8gWojzZMJ7_4zmv-3KvgHDtIGaReiQOGNaoaABDAxlSrXrno1g3e3R_WYpC_Lmx_yndWbqqJ0MRXdhciRIsNM86GNTbm8JRkDWaFoKSVR_A6qGkMCO8w9YTo4HPUNjLvajo4XNc4_r6-wDXPgnrLrIUGxdYc67EA8lcdlqDuOkblXqTN2WKdUCqH-q5Rup86kNIFKfdo3rvrQ_EWtAvFZmLZf5GZSQUP_JsiC-oWAcesf41fWZFW1xZJjOVk1OL8AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هاآرتص: مشکل اصلی کاهش ذخایر موشک‌های رهگیر پدافندی است که سریع‌تر از تولید جایگزین می‌شوند. ادامه جنگ با ایران برای آمریکا و اسرائیل پرهزینه‌تر می‌شود و ترامپ این هزینه را فهمیده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/678087" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678086">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
ادعای سنتکام: نیروهایمان هوشیار و آماده هر مأموریتی‌اند و از کشتی‌های تجاری مایل به عبور از تنگه هرمز پشتیبانی می‌کنیم؛ از مه تاکنون به عبور هزار کشتی کمک کرده‌ایم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/678086" target="_blank">📅 17:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678085">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e43657be2.mp4?token=ogLrwhtuEtVunXwTHf2CoxFPmxAhk1Wu7nWb7eLPWX8pC62hXjJIuuaIGhMdhoXVztfYneLS8yviGxioUy-MhOqBq8wtJnkaNwmVKp87SPbXGlAgco5yPnSsSvbk-JfnMURCTA9rufqJjCDOOKfqcOJAZIIYHuXHuRYq4orMlbr9LTaKNaPO6idfHRhkkLN4vofeJynSW1b3BHEPEkn2_r6wnRy7AJccyBSrNAmztcF1U5YAPl9kn9GGf15r7TO8ZR9HFN3bMErSVKyl2a1rJwc3YDNBt4Cf5VK9fC4XsEPubFZ7EIMt4Etz2QDK2ygkSQZi3akKQw3DZwKR-2kzlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e43657be2.mp4?token=ogLrwhtuEtVunXwTHf2CoxFPmxAhk1Wu7nWb7eLPWX8pC62hXjJIuuaIGhMdhoXVztfYneLS8yviGxioUy-MhOqBq8wtJnkaNwmVKp87SPbXGlAgco5yPnSsSvbk-JfnMURCTA9rufqJjCDOOKfqcOJAZIIYHuXHuRYq4orMlbr9LTaKNaPO6idfHRhkkLN4vofeJynSW1b3BHEPEkn2_r6wnRy7AJccyBSrNAmztcF1U5YAPl9kn9GGf15r7TO8ZR9HFN3bMErSVKyl2a1rJwc3YDNBt4Cf5VK9fC4XsEPubFZ7EIMt4Etz2QDK2ygkSQZi3akKQw3DZwKR-2kzlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام شهاب مرادی در مستند راویان پرچم‌های سرخ: ایستادگی مقابل ظلم و دفاع از عزت مسلمانان، مسیر یاران امام حسین(ع) است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/678085" target="_blank">📅 17:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678084">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlxUoRSm0Uc8JxLABeXvzExPCg-QUDyX7LDXVC1OlFBofFI-KX8VANx_rOunsVJA6KtciUn2oJSlE-Ns-8KtyMakNa7je84jm9Y5lqlIRubBPtoeRKHgPX0giLxpYAhw4mrnn_FlP8y31jGQw1awSZzSq7gXGY2UamyQzNpk04QCEQZ3SHMW9N5wSw_CTyt0xE-ewOjFJ3cStRVN7IX2r3cfzvxoJk4lOY_zSH2wDDCmxTRG4hL21l4YhIhO17aQIP3T5UJemfvnVJYlzcT9rfrDZ9utgHnJs6J0C8r7jf5eUeCAqukOu1UaOTQUpDa9J-UKzz4JZnWnKC3TGF9X9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صفر تا صد ساخت پیج میلیونی اینستاگرام با هوش مصنوعی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/678084" target="_blank">📅 17:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678083">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
۶ نفتکش بزرگ سعودی در پی محاصره دریایی یمن، مسیر خود را تغییر داده و به‌جای عبور از باب‌المندب، مسیر جنوب قاره آفریقا را در پیش گرفتند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/678083" target="_blank">📅 17:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678082">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
المیادین: ایالات متحده در موضوع مربوط به بسته ماندن مسیر جنوبی در تنگه هرمز، امتیازی به ایران ارائه کرده است
المیادین به نقل از یک منبع ایرانی:
🔹
ایران در پاسخ به آخرین پیشنهاد آمریکا، با رد این پیشنهاد اعلام کرده است که تا پایان کامل جنگ، تنگه هرمز را باز نخواهد کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/678082" target="_blank">📅 16:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678081">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
بقایی: پاکستان میانجی‌گر ایران و آمریکا است/ میانجی‌گر جدیدی از جمله چین اضافه نشده  سخنگوی وزارت امور خارجه:
🔹
پاکستان میانجی‌گر مباحث مرتبط با ایران و آمریکا است. قطر هم در مواردی که لازم باشد کمک می‌کند.
🔹
ما با چین رابطه‌ای بسیار دوستانه و همکاری‌ای نزدیک…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/678081" target="_blank">📅 16:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678080">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaXu1ZRt7McGADIs0w96CCtYKvXmjG9q6_kdDyjATIWEOo83haI3XKXXl855ti3rj6vXkkiRvkFmp_43BP7QY0_Wifl8im4gPQ_7sZ5jlirbHHv2HlQzYq3caQCObChN5-O-banLq7Pqa7ceHjJZn-LENEovHat7xn8gP5i6HHLoTGGcf50ZDV5Xg8_57YGJ8-g-28q9o3gv-C0zeADlGIfn67m-csByx-H8g3Yu5fN9d33Bgkb2YxEP_9ar-5wFvsd0DbyJa3edd_EP_fBcNWcGJv7j4aMdEczzEVk9TSnN1Lv9eJ0f7mmCQtQRM-bH79Lbk-4IDLfgQ6gigywCRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از خفیف تا خطرناک؛ کبد چرب گرید ۱، ۲ و ۳ چه فرقی با هم دارن؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/678080" target="_blank">📅 16:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678079">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkRsxp94bNY6JU8X9MySi9Rsd8cHrFqPkXgMj_U4CUYK9NzMOrw3Vl2F_peXA6Hrod_kpeJecW_uCxabsQKejjRiS5IeW3wi1AyrlRv4mOdBQR_rgTVex-YpKqJzJfLjdr64WvnYFjfEsvu-4Yi0SE-Crcz6PD7MHEHMEmQcBnS5FiJpkcZ1vjIrh4mRYcRfyffG4if3IAn5ReF3SLUxUCIYhUSQDVskYT0gkrLY5pCqTlGZAFqa88XGsMUg-m0yXezeIfrDXuOqKNxXhgdPvlGPnT9FX4POm1IGwjZHAWb_AeTkn4cwVUMLBfU623uJNhEXDGR9nmSM7oLEeAxkaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
نمونه واقعی کاهش درصد چربی بدن با تزریق زیکورپا
روند ۱۷ هفته‌ای درمان آقای ۴۳ساله، در کلینیک ایرانیان
⏲️
در درمان چاقی، مهمه کاهش وزن بیشتر از چربی‌ اضافی بدن باشه و عضلات، تا حدامکان حفظ بشن.
این نمودار، نمونه‌ واقعی روند کاهش چربی مراجعه‌کننده عزیز با
آمپول لاغری زیکورپا
هست.
در کلینیک ایرانیان، پزشک بعد از آنالیز بدن، درمان با
زیکورپای عبیدی
را شروع و روند درمان را پایش می‌کند.
👨‍⚕️
برای دریافت
مشاوره رایگان پزشکی
، اقدام کنید.
کلینیک ایرانیان
مجهزترین کلینیک زیبایی و لاغری ایران و خاورمیانه</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/678079" target="_blank">📅 16:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678076">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
جان مرشایمر: ترامپ دچار سردرگمی و دست‌وپا زدن بی‌نتیجه شده
جان مرشایمر، دانشمند علوم سیاسی
:
🔹
ضربه اصلی و مهلک ما به ایران از ۲۸ فوریه تا ۸ آوریل به طول انجامید و با شکست مواجه شد
🔹
ایران برنده جنگ شده اما ترامپ از پذیرش این واقعیت سر باز می‌زند و در وضعیت فاجعه‌باری گرفتار شده/او هیچ راهبرد نظامی معقولی ندارد و فاقد هرگونه دکترین پیروزی است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/678076" target="_blank">📅 16:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678075">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
معاون اطلاع‌رسانی دفتر رئیس‌جمهور: در آستانۀ سومین سال ریاست‌جمهوری، گفت‌وگوی پزشکیان با مردم به‌زودی پخش خواهد شد.
🔹
توانیر: از هفته جاری در تمامی شهرک‌های صنعتی کشور محدودیت یک‌روزه برق اعمال می‌شود.
🔹
نتایج آزمون‌های ورودی سمپاد و نمونه دولتی هفته آینده منتشر می‌شود.
🔹
رئیس ستاد مرکزی اربعین: یک میلیون و ۱۰۰ هزار زائر ایرانی همچنان در عراق هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/678075" target="_blank">📅 16:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678074">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbnOoze-MqooJBEJk_FluCkjHppG_x00Rd-JDgrPigDImzGi1Aawi6hLG0o0Oy_ojFDO3AiEvsSFpXVKbJ_nwxUwqRiR-HejWUa6cJ7mWUQ42HA42FWlc1S_koIAiUSkhKXs-be-R5BCxSV8TofOANSpzksbvH0CsB8_Dp4YJuyMgmvLRj0avuV84C4-EZXGt8lOHnAerxt0PfOuzm_lQcw2g8VwqYqdiuXwVyr07mQSkyBCXjq2ZGfRyHEA9d2BoFRDrHVKkidfT3Q5X2ovrLlu4pcGCHzYGT5pESwA2dYeVdhGUTQN9Mft5ywxUh5XJfyU5UGf2V2dQfzca2M_nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هوش مصنوعی نقاشی‌های گمشده را پیدا می‌کند
🔹
یک چت‌بات هوش مصنوعی برای ردیابی آثار هنری غارت‌شده توسط نازی‌ها توسعه یافته است.
🔹
نازی‌ها بین سال‌های ۱۹۳۳ تا ۱۹۴۵ حدود ۶۵۰ هزار اثر هنری را سرقت یا به فروش اجباری وادار کردند.
🔹
محققان دانشگاه سانتا کلارا امیدوارند با این ابزار به شناسایی و بازگرداندن حدود ۱۰۰ هزار اثر مفقود کمک کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/678074" target="_blank">📅 16:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678073">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
پزشکیان: ایران خواهان گسترش تنش و ناامنی در منطقه نیست
رئیس‌جمهور:
🔹
ایران خواهان گسترش تنش و ناامنی در منطقه نیست، اما در دفاع از امنیت، منافع ملی و تمامیت ارضی کشور با تمام توان عمل خواهد کرد.
🔹
نگاه دولت به اداره کشور، نگاهی سلامت‌محور است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/678073" target="_blank">📅 16:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678072">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0607e9ae8.mp4?token=bOWBZZX30Oa1mu3c0vkBcffcu4X4zucDXfkO20f4_EwVQLCSzGO5sBPXWvuLfXqkcL3tqTM6KRXJ6S9Sm-jhbpqf_wfL1w-HOFVSdCh2xvEbGmXqL5W_w2BWvHbHbje2HfMs3MUpfEGZmSTsovHZ9603ZrcsACYDm1uU2sUnkTqeteUiVVpaz9PbWStO135dvcuQ88nRb97mxcMsG2MjfMafQw4Pghy3izysyuRQdD4qxoOKVwo-nqZn9IopJT501ocDOuxyJZQoyUUs8-RLq4-2HdgRKhnf1qnJGmLaJMT2Wx2DHvzWWrz5_mAkPBgP3CCSQ2-4jp3NFVxl4bLXGE1C9CuF-n3EB4mbJ-W593A-yWEL0u4kiQPAZMi74yGQkxVWbg5KTycVkgA71i35JBMWWFhyB0XpLtsOSBBczCKI2VgJ_RBYX9hb1eODSarBdZKwVEmjZeXicJ7SZDi9SgCFb_yLW0t6kiKt3SvFV1HVA_VcshR7_ndl-rbF98qKmtgiZCcMaOIvu7AD1r8mYG91g3yG6YLrbrFXZhuFuYxP2iNEOTcDQ7mRPh_lymNoMG7L17eCUkEsnN5RidhmySefRmd3Hqnyyjwcj088af6xAakVRSnovzBa1rUqTJN3k2-P-uPAJahkOWtcyQIvlDVsWUcu8cs239Kx5cvCoNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0607e9ae8.mp4?token=bOWBZZX30Oa1mu3c0vkBcffcu4X4zucDXfkO20f4_EwVQLCSzGO5sBPXWvuLfXqkcL3tqTM6KRXJ6S9Sm-jhbpqf_wfL1w-HOFVSdCh2xvEbGmXqL5W_w2BWvHbHbje2HfMs3MUpfEGZmSTsovHZ9603ZrcsACYDm1uU2sUnkTqeteUiVVpaz9PbWStO135dvcuQ88nRb97mxcMsG2MjfMafQw4Pghy3izysyuRQdD4qxoOKVwo-nqZn9IopJT501ocDOuxyJZQoyUUs8-RLq4-2HdgRKhnf1qnJGmLaJMT2Wx2DHvzWWrz5_mAkPBgP3CCSQ2-4jp3NFVxl4bLXGE1C9CuF-n3EB4mbJ-W593A-yWEL0u4kiQPAZMi74yGQkxVWbg5KTycVkgA71i35JBMWWFhyB0XpLtsOSBBczCKI2VgJ_RBYX9hb1eODSarBdZKwVEmjZeXicJ7SZDi9SgCFb_yLW0t6kiKt3SvFV1HVA_VcshR7_ndl-rbF98qKmtgiZCcMaOIvu7AD1r8mYG91g3yG6YLrbrFXZhuFuYxP2iNEOTcDQ7mRPh_lymNoMG7L17eCUkEsnN5RidhmySefRmd3Hqnyyjwcj088af6xAakVRSnovzBa1rUqTJN3k2-P-uPAJahkOWtcyQIvlDVsWUcu8cs239Kx5cvCoNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایتی کوتاه اما ماندگار از پیوند اربعین با یاد شهیدانی که امنیت و عزت این سرزمین را با خون خود رقم زدند؛ یادی که در مسیر کربلا هرگز فراموش نخواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/678072" target="_blank">📅 16:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678071">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVO_oXiVO19dbwBruR2Cn3dIWhObePzHLF7RGT0vrw3OetMZtg_oykr4Ab6eM4Rgp6B28V6C5un8RK0VJpmCWnruTVjF260Eh-efJC32aGBafsdVuf_ItfB8hRfMALx8nMlEEDRdZfA7ai8m7QLWBEaPmn-UMKRhr2U2Yi7xvyPqDxKAK8RX-9Se2mvVKa8ou_rV_uC2x5mXvK04ZqVSbC_7RPqigbqrL66tVdH4BpROsFkIKfAZMwzxMEj49kciRvnvgvD_OvR6sdU7e5HdWcG7akL7479fYWo9FZEkIJhTyOm5mjOA0WyDDu4ykfl-bs_tKyUEk-tHYtdGgNAF_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام الگوهای مصرف نیازمند فرهنگ‌سازی‌اند؟
🔸
در این نظرسنجی بیش از ۳۲ هزار نفر شرکت کردند که سهم روبیکا ۵۶، تلگرام ۱۵ و بله حدود ۲۹ درصد بوده است.
🔸
به عقیده ۳۵٪ شرکت‌کنندگان، الگوی مصرف انرژی و از نظر ۱۶٪ نیز الگوی استفاده از رسانه و شبکه‌های اجتماعی در ایران نیاز به اصلاح و فرهنگ‌سازی دارد.
🔸
اصلاح الگوی مصرف و تقویت فرهنگ استفاده صحیح از منابع، یکی از مهم‌ترین پیش‌نیازهای توسعه پایدار و افزایش بهره‌وری در کشور است.
@amarfact</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/678071" target="_blank">📅 16:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678070">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
چیپ مغزی ایلان ماسک، ویلچر را با فکر حرکت می‌دهد
🔹
شرکت Neuralink ایلان ماسک قابلیت جدیدی رو به چیپ مغزیش اضافه کرده که به افراد دارای معلولیت حرکتی اجازه میده فقط با استفاده از سیگنال‌های مغزشون، ویلچر برقی رو کنترل و هدایت کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/678070" target="_blank">📅 16:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678069">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4f484d0e6.mp4?token=Mb79eRDeNRoPOdRUqipQzC8UlJgXR5K_Ts-mIjV7HhUPBNKgS2A1lMKCSeGrgnGp9vvScEdBheZ2uZDULn_ZWSpDOTCmr9hNCmbay0FiyQ7pRxZ5h_n-3ZKqP48wNOaX91eYXSOZsYOcPUhaqn2JuZZRsdkbMj5U2dGkukRz5Zxh3KXpyaUSiz5LduNnJ9MhCNvgr3TNwiB4lBmXq79Qe8Ge5LrPEg1HoJpJtV24us40550g-GlEiAg9dj05hmt7mOzjTguhoq7WACdPJhc8ta0xlHUY50-HUyUUvidiwiFbtyGiaY3iyKbSeukyH5PTOs5aqFhOZHiskE7ImXq0JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4f484d0e6.mp4?token=Mb79eRDeNRoPOdRUqipQzC8UlJgXR5K_Ts-mIjV7HhUPBNKgS2A1lMKCSeGrgnGp9vvScEdBheZ2uZDULn_ZWSpDOTCmr9hNCmbay0FiyQ7pRxZ5h_n-3ZKqP48wNOaX91eYXSOZsYOcPUhaqn2JuZZRsdkbMj5U2dGkukRz5Zxh3KXpyaUSiz5LduNnJ9MhCNvgr3TNwiB4lBmXq79Qe8Ge5LrPEg1HoJpJtV24us40550g-GlEiAg9dj05hmt7mOzjTguhoq7WACdPJhc8ta0xlHUY50-HUyUUvidiwiFbtyGiaY3iyKbSeukyH5PTOs5aqFhOZHiskE7ImXq0JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مزایای سرمایه‌گذاری در املاک دیجیتال در یک نگاه #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/678069" target="_blank">📅 16:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678068">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxePGyUODxay-RS4XJ6wYAeGyu7a6WHdNNPZAcfgkQWhYRAaBUrXbbj-rUK0uo1eUSvNDKAm-3ZmP6AJSxF1xEDq2MbY0dwFk8ZAGDqS0ryZlcop9DsihGn75FoflQHSXAbfT4ic5nw8J8NMyH0f-L5QExj1pnVr3ZDJqA64a0Ni-J0Xe3PDVPpvgtF_IUUY2FaZFjJu1iVNhh4g8vtm00nUkVtjCUcEoL6mMUzCZvQC3oYjDbyPAqOrzcwzdlAyHycftMdl958kq-jFj2cw9ICpegyr7Jyy683Bg-eCVQksUk0x5-k2LuI61K9UZaTuzXYb_9Xtp4xCILJZK0IlXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاسبی جدید با سهمیه اقامت برای واردات خودرو
🔹
با مجاز شدن واردات خودرو با ارز شخصی برای ایرانیان مقیم خارج، بازار خریدوفروش «سهمیه اقامت» داغ شده است.
🔹
قیمت این سهمیه‌ها از حدود ۲.۵ تا ۸ میلیارد تومان اعلام می‌شود. /خودرو یک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/678068" target="_blank">📅 15:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678067">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWdKWE6hm7OKtEOIsCk9JJ2o3RIzMCC4u6i3w8CWO7ePYfzkr-A1rz4Ge3A0Hmo9agpCDqoceGA1m_jMyebv3Bm1S3OK2A7xmGHSYVQY8r__1kzy3rf7WcOozhd5L6mXKjKQF9_sUemBGawX6ttohF_5O2MVugnEkru_6DqlJEhruf3al7gHxmqqwFURU0MvKmWvP4TvEjuli3OzQAqLcAYO7qh0vXlp_clzPaBekRzlwjatSrYljRvSehZyPAo6ATA5J3oWJybOwKniFEUHJG2GxJcjcp_0k9xwiS7Dqg09F3RB6y33ED_QvcjmHLx63CLzeNkqgATsr2rn3veiPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عضو کمیسیون صنایع و معادن مجلس: قاچاقچیان برنده اصلی ممنوعیت واردات لوازم خانگی هستند
🔹
مصطفی پوردهقان، عضو کمیسیون صنایع و معادن مجلس، با انتقاد از تداوم ممنوعیت واردات برخی اقلام لوازم خانگی، این سیاست را عامل گسترش قاچاق، افزایش قیمت‌ها، شکل‌گیری رانت و تضییع حقوق مصرف‌کنندگان دانست و گفت:
🔹
ممنوعیت واردات، قاچاقچیان را به برندگان اصلی بازار لوازم خانگی تبدیل کرده است.
🔹
مصرف‌کنندگان مجبورند کالاهای باکیفیت را با قیمت‌های چندبرابری و از مسیرهای غیررسمی تهیه کنند.
🔹
ممنوعیت واردات، نه‌تنها به تولید داخلی کمک نکرده، بلکه بازارهای زیرزمینی و قاچاق را تقویت کرده است. درآمدهای گمرکی هم به جای خزانه دولت، به جیب قاچاقچیان می‌رود.
🔹
رقابت، مهم‌ترین عامل کاهش قیمت و افزایش کیفیت محصولات است و تولیدکننده داخلی باید با کیفیت و نوآوری رقابت کند، نه با انحصار.
🔹
تجربه بازار خودرو نشان می‌دهد، سیاست‌های انحصاری، هزینه‌های سنگینی را به مردم تحمیل کرده ااست.
🔹
دولت با همراهی مجلس باید هرچه سریع‌تر ممنوعیت واردات را بازنگری کرده و زمینه حذف رانت و مقابله با قاچاق را فراهم کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/678067" target="_blank">📅 15:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678066">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/647dbbcc5b.mp4?token=e4xYvcXXsdLfrslCm_tMdwRgx-pmoVZpQkw-j1o7Deafe8Gf74MphIIs80H-c8F6C7y4AljxGmuMsZ-qLar3N_LKlVRhm2O7ESJ7saXULf0okI0MZiWWnpsb_FyIUtIHK0l4E4vkMZ6zvHMjtyvocRfzjE_w7MjTbcUo5RRj1xfOMypBDdRIBbCqD6XUueaRxj3Hiuhh0KsCwcT2h4yN5p3K48NWVOiRd7ZmKn-advB1yf3rCc-BW5P1cdPPzr3zbe60MDa88lkVe4KgNtTLOSxjazA2v-7agIYOIo20wUms6rxyfDgTxt3HcEVwAnroJV543kkuQzRNYtZJ0pvfOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/647dbbcc5b.mp4?token=e4xYvcXXsdLfrslCm_tMdwRgx-pmoVZpQkw-j1o7Deafe8Gf74MphIIs80H-c8F6C7y4AljxGmuMsZ-qLar3N_LKlVRhm2O7ESJ7saXULf0okI0MZiWWnpsb_FyIUtIHK0l4E4vkMZ6zvHMjtyvocRfzjE_w7MjTbcUo5RRj1xfOMypBDdRIBbCqD6XUueaRxj3Hiuhh0KsCwcT2h4yN5p3K48NWVOiRd7ZmKn-advB1yf3rCc-BW5P1cdPPzr3zbe60MDa88lkVe4KgNtTLOSxjazA2v-7agIYOIo20wUms6rxyfDgTxt3HcEVwAnroJV543kkuQzRNYtZJ0pvfOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از این ترفند کاربردی برای روغن ریختن داخل ظروف استفاده کن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/678066" target="_blank">📅 15:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678065">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
وال‌ استریت ژورنال: مثل همیشه باید ببینیم ایران چه می‌کند و چه می‌گوید، نه ترامپ و دولتش!
نشریه آمریکایی:
🔹
پس از توافق ۱۷ ژوئن، بعید است ایران وعده‌های ترامپ و آمریکا را باور کند و باید عملکرد ایران را سنجید، نه اظهارات واشنگتن.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/678065" target="_blank">📅 15:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678064">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f21018831f.mp4?token=XH2eOIlap5cpke4qapkN1pKtVoPFXSJ0Y9il4ppMR3sDVJE4JTON3tm7wFiuNv1G1oKOHnG1WGZ4LjFVAM8OM09toJmB3OG5wnGJSNMH_Q7XcUThoVt2bHQUyqPdoYJtSWe0s8J_8JzuFM8UGWNkC-w0kceZzfr80p5_RjcvKqEgvpUAvCnXRcp4SLDFOxzzi7-MZQAak8PiFhrGwMgJE2c1yo_9woSEGX0t-M0Jea7gw73RRzR9NFixU8hooFRuLjoDEUBmB2Fyj8wNKRbBL00tWQoN9oUxRlgMNa_nBSqsuDpHXD430LT4epHJHVc7RNQ7F8UdHALe11dy2Bxn8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f21018831f.mp4?token=XH2eOIlap5cpke4qapkN1pKtVoPFXSJ0Y9il4ppMR3sDVJE4JTON3tm7wFiuNv1G1oKOHnG1WGZ4LjFVAM8OM09toJmB3OG5wnGJSNMH_Q7XcUThoVt2bHQUyqPdoYJtSWe0s8J_8JzuFM8UGWNkC-w0kceZzfr80p5_RjcvKqEgvpUAvCnXRcp4SLDFOxzzi7-MZQAak8PiFhrGwMgJE2c1yo_9woSEGX0t-M0Jea7gw73RRzR9NFixU8hooFRuLjoDEUBmB2Fyj8wNKRbBL00tWQoN9oUxRlgMNa_nBSqsuDpHXD430LT4epHJHVc7RNQ7F8UdHALe11dy2Bxn8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حدیث میرامینی: با اولین حقوقم دوو ماتیز خریدم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/678064" target="_blank">📅 15:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678062">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
پاول دورف و تلگرام به برندگان المپیاد بین‌المللی هوش مصنوعی جایزه می‌دهند
🔹
«پاول دورف» اعلام کرده که به همراه تلگرام به برندگان المپیاد بین‌المللی هوش مصنوعی ۲۰۲۶ جوایزی اهدا خواهد کرد. تلگرام قصد دارد به منظور تقدیر از فعالان این عرصه، ۲۴۰ جام دیجیتال اختصاصی به مدال‌آوران اهدا کند.
🔹
این جام‌های دیجیتال در سه سطح طلا، نقره و برنز عرضه می‌شوند و حداقل قیمت بازخرید آن‌ها از ۳۰۰ تا ۱۰۰۰ دلار متغیر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/678062" target="_blank">📅 15:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678061">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47a0937f99.mp4?token=eBtkfgWgNcuIsaBmbrkM9-GdaqwCifRCt0e0JxGVWiRniBiHoCE6JOwUpBgUifegExboCtTJZYt2QFG8Kbq1y3pHDPcIRzWNhsaEfE1Arn7sdEvMUM7Y7103Zrmn-nQ6WrnUohf4A80dbXiAO_5oSpvaAm3po1QUH8RDOxFNSUtC6Ri0dmtCGdBbDP7knCaMecoGWhvGnbe3LljnGfavAh46IkwpZEKmpk-1TNHGcFeKRcmACzLHTTZT_shq-Qhb6Or5r9pk3lGF4u6qgCq90LGPcbBl6ft-rE1XRxFURN6LtU53PP3MbLzZpzkC0D4cJVVCO_FEv70LKJAX34xyVV5cQ0cmsiWsS7yYejhsZ5Pp77_l6LTtEvfeZbUIgZAkPczJuAH4C_FzGkptjlP7vgNXZWopx98gkP77vmvJjW4Y4YZQaM89BEHk-qd2Row-uYdiC3uAmIU_rzK3tzPHsY198zk5fpXM1JXP0yw3mwigVdkoZG8UaOQ7Wg7uOrF1ntY-LERGXkBLmJ0gjMvcPhWh4vUBlCA-NkIbc4nKsCQo_mLKguecLGd_vQNQOHbowdRT-y9T6mEEK_mW5dFEXgB6afc8YAvvsQrm3hYMhVzKzCqbdC2M4Dey41OrLVixpffKpTbrjmuGbiykHQlputsWz7c1HY5nXzlJH0jXe8s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a0937f99.mp4?token=eBtkfgWgNcuIsaBmbrkM9-GdaqwCifRCt0e0JxGVWiRniBiHoCE6JOwUpBgUifegExboCtTJZYt2QFG8Kbq1y3pHDPcIRzWNhsaEfE1Arn7sdEvMUM7Y7103Zrmn-nQ6WrnUohf4A80dbXiAO_5oSpvaAm3po1QUH8RDOxFNSUtC6Ri0dmtCGdBbDP7knCaMecoGWhvGnbe3LljnGfavAh46IkwpZEKmpk-1TNHGcFeKRcmACzLHTTZT_shq-Qhb6Or5r9pk3lGF4u6qgCq90LGPcbBl6ft-rE1XRxFURN6LtU53PP3MbLzZpzkC0D4cJVVCO_FEv70LKJAX34xyVV5cQ0cmsiWsS7yYejhsZ5Pp77_l6LTtEvfeZbUIgZAkPczJuAH4C_FzGkptjlP7vgNXZWopx98gkP77vmvJjW4Y4YZQaM89BEHk-qd2Row-uYdiC3uAmIU_rzK3tzPHsY198zk5fpXM1JXP0yw3mwigVdkoZG8UaOQ7Wg7uOrF1ntY-LERGXkBLmJ0gjMvcPhWh4vUBlCA-NkIbc4nKsCQo_mLKguecLGd_vQNQOHbowdRT-y9T6mEEK_mW5dFEXgB6afc8YAvvsQrm3hYMhVzKzCqbdC2M4Dey41OrLVixpffKpTbrjmuGbiykHQlputsWz7c1HY5nXzlJH0jXe8s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
اولین کسی که به زیارت امام حسین (ع) رفت چه کسی بود؟
#طریق_الحسین
#اربعین
@Heyate_gharar</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/678061" target="_blank">📅 15:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678060">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/816bc40848.mp4?token=UK__7fDUCPg9VBR_hkXpLCIRMEdsB7teZ6qxNN0NeszUNx4pB7-Cq5a9qN1yy6iK2i9xvfXnx8Fzbb9SrfOViKBDh19VQdM8rs7VSaai5jlD9l457SZn4tb-kWSGkMnAjLgtjpnZ5GnLE_siGjmAXob0LqNW52AdcTBTAwccCDP_8Mj0forb34Itz8TsrYUFIVhtS8K92aaly99NCoAeESgirXH9p-t2_i6hJpaigUmj69SCHLlFtu-YvvAXgJdTODYwkAww_XZw-eA8f544fzD8SwOzx5Nzw3N2-TqH4fJY9S1mf8i-nVLJ4ivkpgswpfuFRt036mjN_598dtpPzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/816bc40848.mp4?token=UK__7fDUCPg9VBR_hkXpLCIRMEdsB7teZ6qxNN0NeszUNx4pB7-Cq5a9qN1yy6iK2i9xvfXnx8Fzbb9SrfOViKBDh19VQdM8rs7VSaai5jlD9l457SZn4tb-kWSGkMnAjLgtjpnZ5GnLE_siGjmAXob0LqNW52AdcTBTAwccCDP_8Mj0forb34Itz8TsrYUFIVhtS8K92aaly99NCoAeESgirXH9p-t2_i6hJpaigUmj69SCHLlFtu-YvvAXgJdTODYwkAww_XZw-eA8f544fzD8SwOzx5Nzw3N2-TqH4fJY9S1mf8i-nVLJ4ivkpgswpfuFRt036mjN_598dtpPzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش سفارت ایران در کنیا به عقب‌نشینی مجدد ترامپ
🔹
سفارت ایران در کنیا با انتشار انیمیشنی از «عقابِ عصابه‌دست» و «موش صهیون» در فیس‌بوک، مدعی شد عقب‌نشینی دوباره ترامپ نتیجه حملات اخیر ایران، بن‌بست راهبردی آمریکا و هزینه‌های سنگین گسترش جنگ است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/678060" target="_blank">📅 15:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678059">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
یک تدوین زیبا از آهنگ «تلک قضیه» درباره داغ این روزهای فلسطین/
فریادی علیه دوگانگی‌های سیاست‌مداران درباره غزه
🔹
حجم فاجعه و جنایت در غزه به حدی رسیده که آدمی نمی‌داند با چه زبانی، با چه اقدامی، با چه کاری می‌تواند خشم و بغض و غضب خودش را فریاد بزند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/678059" target="_blank">📅 15:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678058">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRaLw-RJq-9KHsO9OPBAE8oVirQt-yvKfYJzohD9L1WKseh5gfKZIkMrvzsIOZYBjD2Wh7bDIpPquR2nwUsm5Jv2zdbOwnuyxRgNXW2Q6r-Z5jgoy7ub4zWuOek3gkwSkRmdnDZmZbsJIbam4311ghHxcaMIrCzfPWIrxq9nuYg5Q5lfIob3Upqw5qIviEDiPIKNcUAuXDiznxkB_HkpUjOWBw_BBgPR0sQkLUdq-TW-uWhjfQvv6QbV9uzKA9eFPR0oLT-hgHUSOFrqfX3DtRLcTW8RaZ5F2jsvqSYLirIIRFqc65RgkWrGSv4RxOMn9pq7QtbHIDy3hRwvePTIvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس فیفا دست به دامن سگ زرد شد
بن جیکوبز، خبرنگار انگلیسی:
🔹
جیانی اینفانتینو قرار است با مقامات ارشد دولت ترامپ دیدار کند.
🔹
او به دنبال جلب حمایت برای ادامه فعالیت خود در فیفا است.
🔹
اینفانتینو در حالی که فشارهای فزاینده برای استعفای او شدت گرفته، با فدراسیون‌ها تماس گرفته و از آن‌ها خواسته است تا علناً از او حمایت کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/678058" target="_blank">📅 15:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678057">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d685dd8189.mp4?token=dj-kN72vbV0Fhq2V9fkYspMBzFOwv1JX6w6rUmEbZN0EcdEngqJGfzAKPMFROz7yCUIekwIuZog5YwZUr6Ih89Dhn53lPlY_z4eJ-36o4vOQ2L5wddwEgANW-SwF_SiyC-KfitnNPlqaD2JaMksrkzL9hA9g_5uoN1KhVyBFkEzNpJR3KUE2-Si_nW5WDh9iI-t_C2r6x3wbD2xTC8z7SATaVSGu7d9EQ93m4xRxYeAJ_QRddj8SNUTpVkLN3DxTHUXmG1GEKGZ4nViRZ-4oiiL-mBbz4e4J86UL1rpYZF7l5Kbos_I0eH6sVjbNfZM-tzaNkLE6ol8LA-EMAKXBeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d685dd8189.mp4?token=dj-kN72vbV0Fhq2V9fkYspMBzFOwv1JX6w6rUmEbZN0EcdEngqJGfzAKPMFROz7yCUIekwIuZog5YwZUr6Ih89Dhn53lPlY_z4eJ-36o4vOQ2L5wddwEgANW-SwF_SiyC-KfitnNPlqaD2JaMksrkzL9hA9g_5uoN1KhVyBFkEzNpJR3KUE2-Si_nW5WDh9iI-t_C2r6x3wbD2xTC8z7SATaVSGu7d9EQ93m4xRxYeAJ_QRddj8SNUTpVkLN3DxTHUXmG1GEKGZ4nViRZ-4oiiL-mBbz4e4J86UL1rpYZF7l5Kbos_I0eH6sVjbNfZM-tzaNkLE6ol8LA-EMAKXBeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وجود برق روی بدنه وسایل؛ خطری که نباید نادیده بگیرید
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/678057" target="_blank">📅 15:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678056">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
ادارات و بانک‌های کدام استان‌ها چهارشنبه؛ ۱۴ مردادماه تعطیل شدند
؟
🔹
قم
🔹
هرمزگان
🔹
ایلام
🔹
کرمانشاه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/678056" target="_blank">📅 15:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678055">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
مهم‌ترین زیرساخت‌های هسته‌ای منطقه در تیررس موشک‌های ایران
🔹
در پی گمانه‌زنی‌ها درباره احتمال حمله به تأسیسات هسته‌ای ایران، هشدار داده شده در صورت هرگونه تعرض، مراکز هسته‌ای منطقه نیز در معرض پاسخ متقابل قرار خواهند گرفت.
🔹
از مهم‌ترین این مراکز می‌توان به دیمونا و سورک در اسرائیل، نیروگاه براکه در امارات، راکتور تحقیقاتی ملک عبدالعزیز در عربستان و راکتور تحقیقاتی اردن اشاره کرد./ جریان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/678055" target="_blank">📅 15:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678054">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZDp88JT10WU49M0T2Tc3thqy2ivY0dst6RTAgRalOcziE39YXHZ99MpdG21PHmt641ncGuJZng9HUs2z4qC87IOtGpQyF947Fizw8eN2wZe_yBq3iL_EgrIouKN3J3GgSV5aFS4EJZ9S7BQ21L0z3jqvvOor1h8Z08sBUY-0RAQwBleRf9X8uz9AisX0dDSPZ2P9RMt_sA26TQXdADKlHKHgJ9r7Jkq659ju2jFKGtqZqDdTysl4ay_M7jnjU_1uH-m81EsXDRlPpYbn1qbARqE4apE8VPgavDu-O_q3j6idVjbXrX9srIygNfvlRo1GfdlELNJG0F74dVr3X7-nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۲٠ کشور برتر جهان بر اساس میانگین آیکیو در سال ۲٠۲۶ با قرارگیری ایران در رده چهارم
🧠
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/678054" target="_blank">📅 15:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678053">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fddbf2f7f2.mp4?token=s5UCGKQuiCVWBSJnVpJQfv7q9Ep0LZWp6JeMpktEGrmF4KZIwiCYymfPBneqBwtWnJF-3MASi-A_1EcgyC0HmLVupJCPVZ7rIz2QS3fu5AjNUgHnPAqbZOiqNN4fNw1VAmBFm_gf-gZhZjR0fwlsjJifcIvkFHJIHn71rPQrR9sKRsQ5FKsusJvb9rI1J2ZGsJQiYb5LkwJH5vJHbvLz_5-cHRn4xptPEWpC7Bqlfko61NXpSutCEcJy9OUeTWjdkhwaVGd3w15XiNyFxNTkhShq1WuaKZ-J3GPlmb5KiImPWyjRBMUs3flWttWX1BXWyVDCmRKAAijoqXYNVo6p-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fddbf2f7f2.mp4?token=s5UCGKQuiCVWBSJnVpJQfv7q9Ep0LZWp6JeMpktEGrmF4KZIwiCYymfPBneqBwtWnJF-3MASi-A_1EcgyC0HmLVupJCPVZ7rIz2QS3fu5AjNUgHnPAqbZOiqNN4fNw1VAmBFm_gf-gZhZjR0fwlsjJifcIvkFHJIHn71rPQrR9sKRsQ5FKsusJvb9rI1J2ZGsJQiYb5LkwJH5vJHbvLz_5-cHRn4xptPEWpC7Bqlfko61NXpSutCEcJy9OUeTWjdkhwaVGd3w15XiNyFxNTkhShq1WuaKZ-J3GPlmb5KiImPWyjRBMUs3flWttWX1BXWyVDCmRKAAijoqXYNVo6p-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استقبال گرم پلیس مراکش از مهاجران بازگردانده‌شده از اسپانیا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/678053" target="_blank">📅 14:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678052">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
عملیات ویژه ارتش ایران در عراق؛ ضربه سنگین به ضدانقلاب
مشاور فرمانده کل ارتش ایران:
🔹
تکاوران تیپ ۲۳ نوهد طی ۱۴ عملیات زمینی در مناطق سلیمانیه و اربیل عراق، مواضع ضدانقلاب را هدف قرار دادند، شماری را به اسارت گرفتند و بدون تلفات به کشور بازگشتند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/678052" target="_blank">📅 14:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678051">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6sRe-qsVKGTXXbYf6Ev0GyQKIFVRMsEujiefTLpGMsIPa6cFpphAunvPtZ6R2sKZTVYibqdo4m8WDBUD8MlguTUNetIu_hWoC-Zgk-_BQjslM3SHRcimjtaH9x76K5Y6U1rErFJoHUn4t_oSea-lWYpQqFg_9YsFFIm18rphNkmOhEGF00Q9wr0g4KWtI4GdNV1F571MVBKrcuLBfQv1JK_oB1W1DGhPq1dZbSprvOxRpVOnozbyom0kKUVEQQ5segXoD_Sw5OnYVexVVTDVmFwILOE_hJEw35u8XNDydEdGcI_bNu36D715pOADiGg-Ht_B046-pXAuje5DcHJTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا از صبح سه تا ترابری سنگین نظامی فرستاده امارات
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/678051" target="_blank">📅 14:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678047">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mAXW5_rXlAEqOoD16fw01C77dnEYgvZSncvMcLEdN7EnVnDo89A9S-4wQid4OTynsiV2O9HA8GvoKG9Cj2tQwqJ10LLia9CWEpzy5nelH4A-CcclFHXeX2tJ176SD0_gtV5yC4SUJtlKqmGM91TIvC3Ez71sf2w7HV4lAqzN4LH7yyNiv0Ufc7Gom1jr4JwOX0LI1IRz4f0Coqs0sr3WAnFl4GAhW3ZJIGQvNoqitZpBK31vVz2OcZI8YKqacD90ENLu6_otSFWfIneA7KA6XgYmi9PdKa8nnxMaLhBqh9DSwkIkEFE5r2xPFA3UeRybHRhy-p9GGrCuOT4PKKdQFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fa-0a77W4mTQJJgHZ_4M_UYmATNI2RfJu7kzjIdw7lDuQJtm8QiX41WnmG-WCxoXAk8otTKSK64eEMeAJyhQ8nqbH9NGSL1aWNM-HGXuaH1rcmTSehaxr3qYee-rOPOw5SxSFDzrN6ikXcGpGUqV-yyuwnkGzk6d_Fl3O46_02I3tO4UxkaglzvUGHilOl4z5RSC5B6v2jn9O-CHEw9BoLu3eneaVbIcFDcZZJMeke0_4ijJp5OdCUHuqDlnIhL1E6Rv-xUw8gYXs9xuWwUN1Ne7VPVZwZvarsFQi0mTlUdmjasgkjDADFYZbRz7Ou-5c0buj1rNea2cKDZ1Km-xdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LEMTrytwElQL-FfrU0QbEHygXRDDUwrkkFh7Zg1laGJOeDd2LsWE3ambi_H-0nqh14_rR93MWdtanQ5pIBAWAv4GSXm273a5m9x_AFir0tgMjsR7RM6AHO8ZrUE2v2a3KHvAVzFnwell0_g28jfD0HGn4I69LjltlQ6l7Mm18WC7RkSTcSgcqFfnBWVE7sMQJ9COXLuWAm3FZ_qKCjfKZoaaNiWfdNPII2kM_h4Ti_TWRJoRrhBZO6RRygqElWCnyUkcXBBWgoIQCPY4Lb5QScjWKdUOaVz6zAWQdJ7mEvVDZDB-JzjUDc5lgcuOn-9AYlsLImn7uVLDlPSGdw0xwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDhYb8tmbYcz4Tz-OiBnp_3dnCIh7DN-3Vvl4LWuhaStEsDp0_RYuKbqTFoENUCgGl8bV3F9iO-pFt_q48CY-IVba6xkvit-x_G-erNLFMNGgAKHBKI0agx8Ua5A_tMtUGYZ_MVnqclLTLSfpCRQFeOxwMvGfb_JVkIFnHK7wUkvo8cbQGsPPXkclR07nwcxezoMfVam4FbYGZ_SdxcYP-OMVB7lxfJCEhiC6oENIsnna_X04cgIOs1aYmFlCLvC76MWuXu1pBLz_oF_Y9oTdpJK8JHyJlZoUQEchY2MFEPuPhwB7eCI3Wv7u4igedHNo63MGfq0cNN6UYG-NDnzdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
حفظ منابع آب، با انتخاب‌های ساده و مسئولانه روزانه آغاز می‌شود.
🔸
هنگام اصلاح صورت، شیر آب را باز نمی‌گذارم.
🔸
در صورت مشاهده نشتی یا شکستگی لوله آب، آن را گزارش می‌دهم.
🔸
از شستن پیاده‌رو و خودرو با آب خودداری می‌کنم.
🔸
مخزن فلاش‌تانک را تنظیم می‌کنم تا آب کمتری مصرف شود.
🔸
الوفوری را دنبال کنید
👇
#همه_باهم_برای_ایران
@Alo_fori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/678047" target="_blank">📅 14:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678042">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
احراز اقامت، شرط ادامه دریافت یارانه و کالابرگ
سخنگوی دولت:
🔹
افرادی که پیامک دریافت کرده‌اند، تا پایان شهریور فرصت دارند با مراجعه به دفاتر پیشخوان دولت، اقامت خود را احراز کنند؛ در غیر این صورت یارانه و کالابرگ آنها متوقف می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/678042" target="_blank">📅 14:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678041">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAcdYvzMx7vuuParSMZNkrz9KE_Z1R1nkL_MBpew8VC_98sTSotDGyGauznCQLF1e7aCw-my51RGSClrbF7xtGeLAFUGoQOY7ts1QGZIN0LYN3PYtnaflKbpN4ed42f4zyk_hk97jrKcX9bfWGl9Tf_dAnP6_7Sz_gUeJusZwlJCkRwJCEB_uRrZt05cGvfJU3TZggaK9yva6hNV6ZDyILNHJmCpbx7xhrJjPGDeeZumdHRgteZ_b1ZmNVHIxmJUaCu4QX-RnR9MyIvNUtlFuTmfpY9OIaucpfbCPq-_H4MJgu3z4erO9dMAX5NsnXOoho5VslUYQsmJWdiNqQzoHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شلیل؛ میوه‌ای طلایی برای سلامتی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/678041" target="_blank">📅 14:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678040">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyP6eePhP2A8nzBMVykYBN8zBrjsFlNHcGZhEmCBG8oPtHPAU90PauylJHt4IdQzgf8Xzyqje0qZkQ3Di38HXX-PKgIrhhiAV0W6qoQQTpbKfbxJrQO5oIxJ-m_xoKJw8vjngYLzlVvzD0Lwlfh9OQIp4S80dtgQxALqrqBZTcmCcb9QhA2rCnTMKeiWoWazufw6KJ2z1CHKJczg6jKXOqtb5Ejmwl_CvwPasD0Azc4cu4voZkP1qk-O9qrq4pgsUcTz0neSnnH_mb5_qdouG2wcQpaSGRAqkzkY0Dxr76Yc_WyjmQOLA2-9XlOjhjf3BkwjHNWj2EIEDZPyKZJxkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله به زیرساخت‌های ایران، این مراکز انرژی را در منطقه نابود می‌کند
🔹
اگر ترامپ بخواهد زیرساختهای ایران را هدف قرار دهد، کدام مراکز انرژی منطقه در تیررس خواهد بود؟
جزئیات بیشتر را اینجا بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3235237</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/678040" target="_blank">📅 14:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678039">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
تکذیب خبر بازگشایی مدارس از آبان ماه
وزیر آموزش و پرورش:
🔹
سال تحصیلی جدید از اول مهرماه به صورت حضوری آغاز می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/678039" target="_blank">📅 14:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678037">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7319b39b1a.mp4?token=RjFDcCByZnwxbCa-85NH46JfmgqC9j1-9x-CZ0ZU_Lp3IqyNO_M2oc_Eni-5LK8sDlWt2UyrFxIM7X7JTyTYhgzaKpKFxV8Obaz_I6kRWV4ts3WMKfsq0-fJ3NpHX7-6q4LTr7vVmhelJsHcBYbzmkROfV6UyDYmLWRvbOICSNLHuFfq0MwNq9nUfqM2b71QM6JrROWR1GfpiFDe8RUqgnjZUlZrvywwQqyYeeMnXgPEn08BFIqDEoGyAYyBQ5jFf8ThdRrlOB2K8l7ZrdrhepN5_KrX-EAMruo2rMHH0dyFc7v49pgxB_iGNsTA3dGWaMXuHWgOgRmca-zZX8hf9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7319b39b1a.mp4?token=RjFDcCByZnwxbCa-85NH46JfmgqC9j1-9x-CZ0ZU_Lp3IqyNO_M2oc_Eni-5LK8sDlWt2UyrFxIM7X7JTyTYhgzaKpKFxV8Obaz_I6kRWV4ts3WMKfsq0-fJ3NpHX7-6q4LTr7vVmhelJsHcBYbzmkROfV6UyDYmLWRvbOICSNLHuFfq0MwNq9nUfqM2b71QM6JrROWR1GfpiFDe8RUqgnjZUlZrvywwQqyYeeMnXgPEn08BFIqDEoGyAYyBQ5jFf8ThdRrlOB2K8l7ZrdrhepN5_KrX-EAMruo2rMHH0dyFc7v49pgxB_iGNsTA3dGWaMXuHWgOgRmca-zZX8hf9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات‌های چینی حالا بسته‌های پستی را هم با دقت مرتب می‌کنند!
🔹
ربات انسان‌نما در حال تشخیص، برداشتن و جابه‌جایی انواع بسته‌ها روی نوار نقاله است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/678037" target="_blank">📅 14:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678036">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwZR7_yDAHdCFIB7xHD5lJsqFImHe4fPQXPF32lnBiMg3TUweK2lDFJlXXSs7YyJHdSZ8oYl8YqQeGeLDVZ4Meq9hX05pibsY3mDM8KTZu71zYbvIwdsjTGJb-oEYuF1nGCek_whl3tgHgXcEhzcwuAuoRTJRPOQVc8tI7W7sk3O-6vkg6q7nkgp8_kn9GIzHzaoi9c28VwKMSWzrpfIdCT3bVc8BRISonCX0VKmqqoRy2TU4NskhxZ21-5u8dEetuUFuv1TakvCKB9nN1uua5ZELBrP7ZtnIhbMlBptKgXlFGZ-pQnPwXOfh4-WoAmvUFx48KcC6lJDmtvwWPtBPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۲۵ کشوری که بیشترین مقدار قهوه را در جهان تولید می‌کنند
☕️
🔹
در سال ۲۰۲۵/۲۶، برزیل با تولید ۶۳ میلیون کیسه ۶۰ کیلویی، ۳۵ درصد قهوه جهان را تولید کرده و بزرگ‌ترین تولیدکننده قهوه است.
🔹
بیشتر تولیدکنندگان در «کمربند قهوه» بین دو مدار رأس‌السرطان و رأس‌الجدی قرار دارند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/678036" target="_blank">📅 14:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678031">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jgOyYycDRwYiU0-Z3mn6Q9torMe6dAsE5SJtsHoETra1gZ64eh-E_uiFUam2RWMX8VkL8a5A6JEKWNgCAtKlfUwCGGoIx8139sULD7x5q22hkA1cMRKav0x9PGZyQm5iEidKmPHEHzWzM8fEwFxraLv3dpKh2PCN1z2Oc2PIQVoP8vt-r9FUn-aRsz_eNg0rFAg9trd-imAU5-54Gt4eYwtJwP9ZLPifx8jXgfWf8rkrMHIRBhNK91pkNFAIwv-CvzBEKe7dWjm8NVNb8SPtI3g4l1lGsJjDD5Q3LU7p11BCy50vj7U-8hiMPbiYc4Zazi0MVs0LqRYqHq6-bqv-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j0Pi3TvSorhL9X41zgLVdE1E8iJsAMLS3V64_3uZCawxJYM4dfoqhh3OK8CGzpo6-LOqkrtMr5A_xjK_B0vjlzJ6eRkXFESFSwb0WxU628bN0OpyUIGyx5N8Ro1wTS9Ep8Gqw_nnIuqC2_qfzAz0ru0IZVIr61b9rwqorCItlkPN_pUgtIVPzr5RoLZh1qD4SHNWLeX5-Y_LUDxrObIo4EdMsJHxy9NzBj4q2yEtXMfBwQWEAQkPtQ_q1tRdqcvGIJ3ciI7fivqk3Sz21EBLbYhGP2uVe8arpPeGe9uaMgAR1xcBc8jIp7smUuC8256X0HT8HXG6BJPVJlWCM5fI4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این ۱۶مدل آستین رو هر دختری باید بلد باشه #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/678031" target="_blank">📅 14:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678030">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromوحید یامین پور</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c06f8046c6.mp4?token=e6PMXiNNjTlMe2dvVW1efP3FEQHjVQe8p_nJER3nPlCFl_AH9Ug_FOmhuwHbNLOXSacXUNVpmgy5PIHbdmDOZEkB9mzP__75ZHWBYDYuEeixq3aeAcqLlB50SVL_MnhyhNXy0_ZELo0r8VgIpkIkT0O_ddlZ0QZdljCoRrfeOocayFmavH7QyelDeKvxczNO49EYyJH3ZCuMP20bE8ywZKuJLXjGqATGSSv_s_oi6hGXNw_mdtpm8ObjHdpld0LJCjsrGtM3a25XyJkk86ddywUezuNNDnnrcNzxgyZ5bAEForJyErzCzisPLNd1srom40fUf8ucLqL2vK30wSA0Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c06f8046c6.mp4?token=e6PMXiNNjTlMe2dvVW1efP3FEQHjVQe8p_nJER3nPlCFl_AH9Ug_FOmhuwHbNLOXSacXUNVpmgy5PIHbdmDOZEkB9mzP__75ZHWBYDYuEeixq3aeAcqLlB50SVL_MnhyhNXy0_ZELo0r8VgIpkIkT0O_ddlZ0QZdljCoRrfeOocayFmavH7QyelDeKvxczNO49EYyJH3ZCuMP20bE8ywZKuJLXjGqATGSSv_s_oi6hGXNw_mdtpm8ObjHdpld0LJCjsrGtM3a25XyJkk86ddywUezuNNDnnrcNzxgyZ5bAEForJyErzCzisPLNd1srom40fUf8ucLqL2vK30wSA0Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان آزادی عراق را خواندید. این هم داستان "آزادی سوریه".
❌
وضعیت اقتصادی سوریه در فردای «آزادی» زیر سایه محور ناتو ـ اخوانی و حکومت جولانی
سوریه‌ای که با شعار آزادی به ورطه آشوب کشیده شد، امروز با واقعیتی تلخ‌تر روبه‌روست؛ اقتصاد فروپاشیده، زیرساخت‌های ویران، گسترش فقر، ناامنی معیشتی و آینده‌ای مبهم برای مردمی که بهای سنگین پروژه‌های خارجی را می‌پردازند.
➕️
@yaminpour</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/678030" target="_blank">📅 14:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678028">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGGzbs_cxih9kJb00DODxSIM0v0yBxmP3hLSSfyY38N8kK_n7p8HBJYMXwt7WYWiJW96LTbU8N5ImCNoTkrXGZYHFLrZ183eHDHK7PsEtOpQK9i7uAU5Q8pjjHGwR3DCZ7_3QIAD5AJBVKQy4hLnmlRJJBFFqrQKTQuhthC5DCvfZdWMw89HXBaMzJB6Vk-zNvFnPC4rCxP-Z66fhIQhF9_efGXnupSgXwhptilROo5y1VZMsjUrXsi7pdLLE9yWe2jqMQp2OzUXmWO0KY5QdEisEHofoGEY51mWZHNt2SpKGXgPGLt9iE1Y1JBRMT5jztU4Lu-yBtovJRcWrvMcdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر زیبایی از دماوند از داخل هواپیما
🔹
محمد حسن مقدم‌نیا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/678028" target="_blank">📅 13:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678027">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/il0--cvtX6yj1_8F0pDcz3jWqf_IgbLZo-0QlnVuoT2Kzq3UgkGrCoQonuluzhZq7nybClHNWQJSL5LlQWxMUwAct6V9CqQpMXIsqLYjJeg0yhlTnRhvpDoPPohheseIbgh6AL0nfrZMYtBIQUz9le3OCYKp2eUJidTw179ySVZbtl_rKDza1yoDF8HiDfqbR7fHWDzkeNRDAibelZ0XY1vYjUvWSslQCgvcYEswMZJK9DCh1ZPTyBJd4_Kf8iunf4Do716YuJisQqfd6YGP_WdAAFyxc3ketx9Bbg4wQVkKKYvj-pEh64mCdkBoxGFlhdRwn7TyFYCC3epAgiAluA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیاده‌گویی
سناتور جمهوری‌خواه: باید فشار حداکثری را حفظ کنیم؛ تحریم‌ها، محاصره و بمباران کوه کلنگ!
جان کِنِدی درباره احتمال توافق میان واشنگتن و تهران:
🔹
از تلاش برای صلح حمایت می‌کند، اما حاضر نیست توافقی را که به‌زعم او «بد» باشد، بپذیرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/678027" target="_blank">📅 13:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678025">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4074d30983.mp4?token=ucqqI-2tt8I8XjUWL96Dl8IrTQ4Mu8q6x2a_rw9480GyEnWnwF_1iUupWW4-RlIIz0RiF_6YQJCqRwhStvUv6e-d5Iia6JRkQA-8UZsxsv7h85Vy--7IqdVinPZm4OQk_1L1GW6CASIqjyLND7XPBDqbSgx7GN5BiuUDPS56JSGo6i5aNiQDlYqtnAopaExz21IfTEzAhKslOitIQb8e2M5XE0-t1vGO4ZjtoMFzE3JiQ_mnNkGopqqaQ9xV8XVJYtPOycrfZSLYdrKCZSRpu4kOMY4o1FJfe9LxmiwmvCbIIqG7Tn9SqF36cRY5k74S_rZ6zEizXyfuqvfMFwEsgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4074d30983.mp4?token=ucqqI-2tt8I8XjUWL96Dl8IrTQ4Mu8q6x2a_rw9480GyEnWnwF_1iUupWW4-RlIIz0RiF_6YQJCqRwhStvUv6e-d5Iia6JRkQA-8UZsxsv7h85Vy--7IqdVinPZm4OQk_1L1GW6CASIqjyLND7XPBDqbSgx7GN5BiuUDPS56JSGo6i5aNiQDlYqtnAopaExz21IfTEzAhKslOitIQb8e2M5XE0-t1vGO4ZjtoMFzE3JiQ_mnNkGopqqaQ9xV8XVJYtPOycrfZSLYdrKCZSRpu4kOMY4o1FJfe9LxmiwmvCbIIqG7Tn9SqF36cRY5k74S_rZ6zEizXyfuqvfMFwEsgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تغییر نظر ونس، گراهام، تد کروز و روبیو درباره ترامپ پیش و پس از ریاست جمهوری او
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/678025" target="_blank">📅 13:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678023">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e443f1ab91.mp4?token=QXyQ_0khhRicFZcZIcFbA50oox7mAmQ_DkZcAYUtkwpcL7b25DI_LM_KRNhKMgwU0ugZXnHbO4xmEUCgNGKVty7qCdLBcpRYzopkZne0VxjkzEnlVoqTHLd8mhqFsR6ITrwKo7AChPjR4EQKjhpnakmRXnZ8SVKOO5E_FedTa5c2Lqoig_gkPoPGEeX2NnIECvutSLItQdJqFMMsQcpk95yYosGrDqSG3W3R6O3-b7lp07FgztAVuBUwq2dMzZLibcpR0Nx70A_s9uUfFyJ2wVq82wC0_OKpgPlshwMtGctBIaHJzRSn_LT8dgBuqijKJYYDXjsOirdJAVpcsa8rgK_fbV9cQgkQ1vLj2cU_PThH2v1T9FNwEXRCMx_-2YvpMZL3xRZlKH-oCeEbifIoNo8VbgzzKuV7OCyqnBqZuGIgPJMnweMrdXvIghE0ubnM3ns1f9WVpWcOrTtsDcUAg7BdMP-Wpx1TU2G9Kim05FefSNLL_jx8F5pzhOvgvKsnOHQgfOTsY27Mb0u7SyzzMFl_BiShnnrayWWbV9eocJZeyz8YI5Y1l-XdDx6HLLyGy42LL7Oj8i_Kcl_-nUtWnCRYGK4e7jDjyPLmjzVXnjNMQi-blabYEgUQoJaZ8hHhcoEdpGuYzDmnx8L_Dl59Zr_GmKDnbvooA4fLHwMTptw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e443f1ab91.mp4?token=QXyQ_0khhRicFZcZIcFbA50oox7mAmQ_DkZcAYUtkwpcL7b25DI_LM_KRNhKMgwU0ugZXnHbO4xmEUCgNGKVty7qCdLBcpRYzopkZne0VxjkzEnlVoqTHLd8mhqFsR6ITrwKo7AChPjR4EQKjhpnakmRXnZ8SVKOO5E_FedTa5c2Lqoig_gkPoPGEeX2NnIECvutSLItQdJqFMMsQcpk95yYosGrDqSG3W3R6O3-b7lp07FgztAVuBUwq2dMzZLibcpR0Nx70A_s9uUfFyJ2wVq82wC0_OKpgPlshwMtGctBIaHJzRSn_LT8dgBuqijKJYYDXjsOirdJAVpcsa8rgK_fbV9cQgkQ1vLj2cU_PThH2v1T9FNwEXRCMx_-2YvpMZL3xRZlKH-oCeEbifIoNo8VbgzzKuV7OCyqnBqZuGIgPJMnweMrdXvIghE0ubnM3ns1f9WVpWcOrTtsDcUAg7BdMP-Wpx1TU2G9Kim05FefSNLL_jx8F5pzhOvgvKsnOHQgfOTsY27Mb0u7SyzzMFl_BiShnnrayWWbV9eocJZeyz8YI5Y1l-XdDx6HLLyGy42LL7Oj8i_Kcl_-nUtWnCRYGK4e7jDjyPLmjzVXnjNMQi-blabYEgUQoJaZ8hHhcoEdpGuYzDmnx8L_Dl59Zr_GmKDnbvooA4fLHwMTptw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیاستمدار انگلیسی: وحشت در خلیج فارس از پاسخ ایران/ بار دیگر ایران پیروز شد؛ آمریکا دیگر توان رویارویی با ایران را ندارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/678023" target="_blank">📅 13:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678021">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ایران ۸۷ میلیونی شد
مرکز آمار ایران:
🔹
جمعیت ایران تا لحظه انتشار این گزارش به ۸۷ میلیون و ۷۷۷۷ نفر رسیده است.
🔹
بر اساس جدول پیش‌بینی جمعیت کشور که مرکز آمار منتشر کرده جمعیت ایران تا سال ۱۴۰۷ به حدود ۸۸ میلیون و ۱۹۰ هزار نفر خواهد رسید که نسبت به ۸۱ میلیون و ۵۳ هزار نفر در سال ۱۳۹۶ حدود هفت میلیون نفر افزایش را نشان می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/678021" target="_blank">📅 13:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678019">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEmsuy9nWxypRPtb2ro_gpogdqyzMfiJK99Nys-PEAI8-F79AVfB9_sLIsvzAXAWOtq-tsPwmj1pUjG26AMnIalSdVxXKp1B-mcwDt4XUhq6ao0Pur1v3Cq5KJGJ-PZVU-xK-9RQ62URbQJJI0GQZkQrYPV-IMUJcHyeh-ACuMWRU3wR7Rm7ZUTZ1QW8qjOtK-3XMsO2vC6JJaYRuHCBLqZ-M5ahSP9mm7ucd1MiKju5ShQpzUzMgDRWmMe58IBWjvrzcvBJZYfdWdXNpCouELk3DbC_XwSuSnl89fhQBOH69lNsSRSi27ZiW1EAReO8qvv5ALyVnwsFwMxz3WWAkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چه طلاهایی برای خرید مناسب هستند!؟
🔹
اگر قصد خرید طلا دارید، این راهنما به شما کمک می‌کند بهترین انتخاب را داشته باشید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/678019" target="_blank">📅 13:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678018">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c223a9b104.mp4?token=d19Gw1H8N6EzBFYB0goq61g1FvxX7z24enhiFqcAqypGsz4u64CfaCiP9UmEMxmB6unIkn4SyP_mOWeVkyLjBvlGUhZbJS38mSnPw6ukwvgVdSMUPVOHTwLii5u2qs-aREX-qZMU6NC3UT2R_UXpKt_2e8j-b0an6l0ODIqJC4DcyvZc1s82gq5Exe-ciSC39ju7_CImCTY1ZqdtFu2o7hNOPzbCp2sUJ1nlM9u557wzbfh1qns-ul-jvavA8Xjl0h7LItdBPKLXlIKGVtRy43QR5bnj4OxFt6ZT__m8cbQH50UAIj1GeAiSJxslhZ28REUWq7lpLOIef1vZbK8sjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c223a9b104.mp4?token=d19Gw1H8N6EzBFYB0goq61g1FvxX7z24enhiFqcAqypGsz4u64CfaCiP9UmEMxmB6unIkn4SyP_mOWeVkyLjBvlGUhZbJS38mSnPw6ukwvgVdSMUPVOHTwLii5u2qs-aREX-qZMU6NC3UT2R_UXpKt_2e8j-b0an6l0ODIqJC4DcyvZc1s82gq5Exe-ciSC39ju7_CImCTY1ZqdtFu2o7hNOPzbCp2sUJ1nlM9u557wzbfh1qns-ul-jvavA8Xjl0h7LItdBPKLXlIKGVtRy43QR5bnj4OxFt6ZT__m8cbQH50UAIj1GeAiSJxslhZ28REUWq7lpLOIef1vZbK8sjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دل‌های بزرگ در قامت‌های کوچک؛ موکب‌دارهای کوچک اربعین
🥹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/678018" target="_blank">📅 13:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678017">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abc33793d4.mp4?token=AmQD4c39HW9tKluI-6k5vkzZuopRloYrjwnj7kRBpZXWssMo6lHOsyJ_m0dTXLvP2-KDCWzzBXvlpbG7WslXpvQLpW_JrfbRGJE8P_a91gQVYVAuYADs1HH-bDCn9nP8tfcBAfwBT1S9bT6wcL0lQNgljAjiRelMXGiX1anegQzE3W1ek9jYqPCOHtQNt28bKcyBu4td71EcGX0jLqZA-alM15T1kuklNulTSwv6GHSJaXK7lTH0oU0dKJ6bYdQT6HA_ROXnza8U7T6uC66LFGanQJLxqHhWy68jV1JnINYeFL-OZNfrXuO5MFm-_hO4vIvG9RO4o33zr4s8PiHYXSUZv0_i8Q2E68sa7I388cuBBd-IHb4lR_907PYXHo0X__Z7Grd8OYJvl8HrYXVdMJiaHdbvjBZxvglCoqiqlpiPYhNuXYWICmxl-xVpVWpDYUJmYKD5ms8CpmOtK1i7PdEc3dpo2lih7MFsLh0bHdeayNMskluDIe4w8jegbaUhEL-BjEDzsFiEb92wMu4ONtKF2BtADhvPVgwpGNYdYSVsUzDxjvC3Q4YL0RxJ9mfXNw04-zh13jn5US4p8Txx24BfRNiM7_XxJ0epRXf4jXClgHX8DvZpp6XdJrewfaNMNjXqPxo7R5LVyXXWCyVmR7PnQGc6tXZisNlQ9xqssOc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abc33793d4.mp4?token=AmQD4c39HW9tKluI-6k5vkzZuopRloYrjwnj7kRBpZXWssMo6lHOsyJ_m0dTXLvP2-KDCWzzBXvlpbG7WslXpvQLpW_JrfbRGJE8P_a91gQVYVAuYADs1HH-bDCn9nP8tfcBAfwBT1S9bT6wcL0lQNgljAjiRelMXGiX1anegQzE3W1ek9jYqPCOHtQNt28bKcyBu4td71EcGX0jLqZA-alM15T1kuklNulTSwv6GHSJaXK7lTH0oU0dKJ6bYdQT6HA_ROXnza8U7T6uC66LFGanQJLxqHhWy68jV1JnINYeFL-OZNfrXuO5MFm-_hO4vIvG9RO4o33zr4s8PiHYXSUZv0_i8Q2E68sa7I388cuBBd-IHb4lR_907PYXHo0X__Z7Grd8OYJvl8HrYXVdMJiaHdbvjBZxvglCoqiqlpiPYhNuXYWICmxl-xVpVWpDYUJmYKD5ms8CpmOtK1i7PdEc3dpo2lih7MFsLh0bHdeayNMskluDIe4w8jegbaUhEL-BjEDzsFiEb92wMu4ONtKF2BtADhvPVgwpGNYdYSVsUzDxjvC3Q4YL0RxJ9mfXNw04-zh13jn5US4p8Txx24BfRNiM7_XxJ0epRXf4jXClgHX8DvZpp6XdJrewfaNMNjXqPxo7R5LVyXXWCyVmR7PnQGc6tXZisNlQ9xqssOc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احمد الشرع درباره نام پیشین خود: «الجولانی بخشی از تاریخ من است»
🔹
من اصلاً خجالت نمی‌کشم. الجولانی نامی است که بخشی از تاریخ من است.
🔹
تاریخی که من با خود حمل می‌کنم، پر از بار مسئولیت، خونریزی، شهدای فراوان و ناله‌های بسیاری از مردم است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/678017" target="_blank">📅 13:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678016">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l00QK449epvlPN3oozruupEivP4C6m1hkuGF8XXYp0RioYnEsKcirwHFI_dVNbU99y8IoYg3AipzsfA3qufrWiI04bX1y3zC_ulODZ8ceSiDK1eA727ibFvr-frffInFT-a_Tek7G2n4PsY1oZ7vXimkJJb_Ikz8F3gMS6JbdkmXT8aREdODc-uMYTUgjYe1gs61BeMTGgyvLzdkgyjNmQTCWySY1-Znv2Swr_gmoLa_gYq1j0Nk36x8QgsuOpN3d57pEDMy8Y3BbUhSm80bfvAH2BlL-utq1AcA92VqIlNJ2miTQ_ZKaDooizJTbFbFXtD-c8yiBC72fOcdueWiGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعترافی متفاوت درباره جایگاه ایران در معادلات قدرت
آلوهن میزراهی:
🔹
چین و روسیه هر دو از نظر اخلاقی و ایدئولوژیک به‌شدت ضعیف هستند، بدون ایران، ما هیچی نداریم.
🔹
این هم سفیر چین در اسرائیل است لعنت به شما و ربات‌ها و پل‌هایتان
🔹
بدون اخلاق، شما هیچی هستید. دیگر هیچ چیز مثبتی درباره چین منتشر نخواهم کرد، بروید به جهنم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/678016" target="_blank">📅 13:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678015">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b093430262.mp4?token=lCeLnEfAP8MMfj5_6y3JO5qZ5eh7WLGOPAqesjTVrFtA7lkAGVjdhiRRyJw3DIog2EAnqLFHzOQlrLN4cbgnqTnbrvpbVwutmsV4TsFG8P0WmBmjgn2jArbQbhcBPx-pVlyZNLs9KY8gxFOiFnW9jcXa2H5rfAWQMGQE4saP12aZ-jKYbsOoNjUtDahVMs5fT7WaIRRVCIHn2P_EsX2GOyIfvPJgrRvMSW-XREkAm0FYsBUkNnTsdHS7RyV0pHFCj_mu3VEaR2OvNbAWK269ttkMuWDSyceYrBT29ZPgKyfyuP9BenH4Fnkr05cX0T8zosO-7_Dtr49OsWlGwisBaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b093430262.mp4?token=lCeLnEfAP8MMfj5_6y3JO5qZ5eh7WLGOPAqesjTVrFtA7lkAGVjdhiRRyJw3DIog2EAnqLFHzOQlrLN4cbgnqTnbrvpbVwutmsV4TsFG8P0WmBmjgn2jArbQbhcBPx-pVlyZNLs9KY8gxFOiFnW9jcXa2H5rfAWQMGQE4saP12aZ-jKYbsOoNjUtDahVMs5fT7WaIRRVCIHn2P_EsX2GOyIfvPJgrRvMSW-XREkAm0FYsBUkNnTsdHS7RyV0pHFCj_mu3VEaR2OvNbAWK269ttkMuWDSyceYrBT29ZPgKyfyuP9BenH4Fnkr05cX0T8zosO-7_Dtr49OsWlGwisBaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از کمک تعدادی از نیروهای پلیس عراق به یک زائر ایرانی برای تهیه ویلچر در فضای مجازی پربازدید شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/678015" target="_blank">📅 13:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678014">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🇮🇷| پناه هستم</strong></div>
<div class="tg-text">از این خادم حرم امیرالمومنین پرسیدم
دوست داری ایرانیا در جواب خون ریخته شده‌ی سیدعلی چیکار کنن؟
جوابشو بشنوید.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/678014" target="_blank">📅 13:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678013">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf79599adc.mp4?token=qv6G6HjBwc1qOp92pr-AGArzWf0V6kZEJdME7bkpRXcAZOj1J9dLyOC0PBOeH2NdDwhwArWbiciXNEsPMp6s2lPHsRI2OZtcwASUZln_T9jNN1V6RFg2BGL_f8ahu9RNvLIVQBOwWpa_SA6EeeIXaFUZ9CykCFUNkTbwmDsR7_xVcRM19QuRseigwd6wmmACxEo7TVy_rSmISRoZkDL3zfc4VqPqbT9mSrw5UvrG6DkZXsSG3sotmQ4AmvN6C3Qokt87jHZpQCB8k-ijytn01RFiApgTnEhzAHVKRpV1r4lbr4HIrMqvLlZGFyg1Fn_r4S423CO1qDwEAxi_raCysTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf79599adc.mp4?token=qv6G6HjBwc1qOp92pr-AGArzWf0V6kZEJdME7bkpRXcAZOj1J9dLyOC0PBOeH2NdDwhwArWbiciXNEsPMp6s2lPHsRI2OZtcwASUZln_T9jNN1V6RFg2BGL_f8ahu9RNvLIVQBOwWpa_SA6EeeIXaFUZ9CykCFUNkTbwmDsR7_xVcRM19QuRseigwd6wmmACxEo7TVy_rSmISRoZkDL3zfc4VqPqbT9mSrw5UvrG6DkZXsSG3sotmQ4AmvN6C3Qokt87jHZpQCB8k-ijytn01RFiApgTnEhzAHVKRpV1r4lbr4HIrMqvLlZGFyg1Fn_r4S423CO1qDwEAxi_raCysTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جاسوس موساد: باز شدن تنگۀ هرمز بستگی به خواست ایران دارد
منشه امیر، جاسوس و سخنگوی موساد:
🔹
ایران قدرت بستن شریان‌های حیاتی جهان را در اختیار دارد
🔹
آیا تنگه هرمز باز شد؟ مسلما نه! آیا باز خواهد شد؟ بستگی به خواست ایران دارد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/678013" target="_blank">📅 13:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678012">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwGAZmhAr_r3vJO-yMYFXxlfTRyilXVGWIDGepNwG0p_CpCx2Lo6q7sMjI8qN-o5ZLmtP4dkWsRp5kgUWp_Gt0rb_g5vcFR5xaFsbcQNqK6PS9Jr_BMm7ABT6qbpVgb-o0TwqLuYCUFZjL5049NlqNYpkHY8fMsicB6DK_1TCG1x-YkNqNGWnggRmnoJLEtMRb-HykhO2Lk6EjL6tSQ8Ud0lAFnJID62qlwrXCre79dGRJUcYIV6RROi6-oXRBBvOSt9745fJ7JeP6rsq12vrWf-mnualFBwa0CtIfzQPWJnodp-ujiclQTCXwLxB-zoo4LXNhk9dvZOQ8TL9QFtpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت روز طلا در ۱۲ مرداد ماه
🔹
بازار طلای امروز با کاهش محسوسی در قیمت سکه بهار آزادی و امامی مواجه شد.
🔹
قیمت‌های اعلام‌شده از اپلیکیشن میلی، به‌عنوان مرجع قیمت معاملاتی طلا استخراج شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/678012" target="_blank">📅 13:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678005">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HxLFcaQFd3stzjPjIn-ikm1MlNJQNdiGNNdUod-G-sD9bZTOBy7a16lib7zc0QHntuHr5Sr1-lidnxszvl8uGsBUv24bGUjOZeYqbVQ5r4i4tq5M4CnHG4IjVF1uUuhUhZKYF1s5POkQXG9pyccjYY9_EuW_KxUvY_Q0v9uWUNfr4Wcus8oYgEMoNdrBXPeWdrvcacPrgKhg6kNhK8Z1rW3dP5FUQBmSd3OfrxXmFzesKi_8pM01rEvJQalIVfMXK4V6AlCyaliAbGer1sw5xfglwwAvfdzoRCA-QrkTXN8axFQm0u-SjVkmjrdxH3BYRyWIikJYTN94e8q2U_9w2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BI0UkYojFpnFQs9ZrhueIlllKgkx7Lp-kIU2vb4KCtIyotMHVfLaW2TmlAgMo88mzC-qLu7HZ9eLYJ1CtPF78OKPrcSSzMLNkhDcNjr_bpeOgVjptRzMtB_vLfddAWbf6ePeultG_BbkCWKuxwefW3bv-2WmfqRFZBxBIzdoOVo3M3d5GqvCa4spS61UwWHtHys9QAzqR3G82VSvovjmWYnxJRjNOc0h94i-ecVaL0wVL3G26x-ZdGQCfrOganwESxn7QE_7CYpLaMc6attQSKOzgWt-LsoX2CyDMavhw9IEdwdEEDgXo3dHgcQwcskF67PomkLlN2OVjypQ_fMGEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XplaslhNaRGSIfPuNsE9gW3OGTXTI5PpzWqzNKFjxDf0MJsshCSUWc3lDpmYdwECZ0MO7w44k8Bybo9V05uQfam5PJm2fICIB-8lPQ6_7lrYTZeEqPg3JvGCGKlqjyBqWuM-2Fq0pN42hoIY4acHgSj781wnK-wN4EPCt3cHTKTdV4lPYTSevOyJ9GT9elOPiCeQe3nPL0Cj1ldu0Y1Vj0hS0EZVk77XdxrX86HKBsyyzFuPJq1yhEgjQc6NryqQRBbiyo0qhqpEho174kk8hzciLNfY4KJxfzej5AsX71ruCb6MpfYnov1axmPwvj-Yb1nlasyNMyrB87j_XEStyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ax0Op_C1rikdPySBI0nuBOHmalrwK-YW6HSRtkzMqcvbmL2bUhQgm2yjYYmwPpCvQu97wh5IVBp0_CQSt3_CBPDTG1GSzhIIudAFcRuIQQdjwzEPuSMgXY7YcfK1kqTK7C7cXOyRSPuqC6pr5DZXieD7QvDtgYbdq34_E-iaf-EMeypvTnEGSLW_EfyWMAoPirmFxYnYSrTM4_6wPbYpIDdyZQwScNns9w4fRjB03p8xQAhanXaFgBx2RocNheKMsypJ9t9IfweyijRKuBiytoXuhSRbuivIbAHObB8S5WusagbZtV19XEi7GGKhpAfzv-4DmY23mQvSM5jsB9y2Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dzy5SC5VrsEKY3uygfmruB5bJ1a75LgH8KgUkyXz4F5AbL4RoY8YWv4em1r9yJSJJvo6F0A8mT-HgYz1anZPGTk-tzCj_zF-6rGD_ChZMjVp-YZdng8gok8PNgLXlvdi7HqOKK2rgu6Y6ShNCe4M0tOg-IVWOlA79A4UpAjTzn8iVw3LmutSyFIN7d0zcrRgH7CmS8YoYz11v6n2TcGDKb4X-JkVVOhRUHu-2JluFXj9RmIXN1LbM74l-5UWERldFkvc1D_DaifDdJ3dpk8zHnuF7kr8RIO__SLbuRYVQHbovZn9QWqaQ2xsQWOyr3wWSLMMk5Xv5Y2-L6SKdBF85Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQk1SMclsgVdqi1WcjGY33UFIISLnf1LKVgMFjwSW7eqOpJUun2l25LnIZhTV5kLkwb4thKqdbdGhcQAzwvfRKc9-YgBZulREo-ce0k-dLvi4U-AJpADhdEwSr1PUlVgmKTPxu5AVB94_YUiLWOSs7eCbU25a7ywlgwAC17Y6Q1LrxDVufFPJ3UTYJEPQAmroxZ8TsFdDsGy7u96EUtBwtinSzDs_PdcgGvYYyIeGASKEnF9xseu0FWTfbymVdKGwTNVCCMusaDBGJB8bgGBN-Kl83-usLWki0qUwoU0oYA1T-NHCzyMudOL3PJnEfQMth4CRC_0g0emeOEadU0xYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAiRiR4-QRkDgqP-HuaccKxIN2gZxwLELpBTx1sVX9c3zR6DRId27BSt-BFnMk0niQyTczs52BAD3RLQU5YJwQIuECE23zWfM91OQ4TbHKxIcNPjod1a-gKHXV-bi_WuKYAPaAY1qbQHpCrl8fwzzGOSKWrp7fHBWOqzrOonOJd5PpH-d-8FfMjvYs3aVI7pD7hsW_2TlVzW0h3SzOaVjnSMP07ykYeU9MM2Yp9FrH2yxw7MRsB2eSnB6fxaptNq-Z7-BTlixKeYjkoIVYofoqid7ARicNYY_1r3S9sF-PWxD8KUNvZhRK2Hpe-MoyzFEmwHsnvvAYoiPnKu8RyX2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۷ مدل قهوه بدون تجهیزات در خانه
؛
با حداقل تجهیزات هم تو خونه میشه قهوه‌های خوبی درست کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/678005" target="_blank">📅 13:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678003">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12bacc8c1f.mp4?token=jMNPJMYxpJyo-crjxTRZ7lWqLFHCq6Fj2Ok9oZF_v9I_h7aJ7r1smcTvKfx0aywK8Mjcq0AI1sbjCufvhiJHO9Fvkk5nuaKAUwzKAGE4f4ym0cm5waCZvrubyTsBxlkXNEYNeznF29W7XtNBSKD7u7rk7ShDBfqKpb0tEdjybV-bQRd3hqFzxTmz4B_cBEaqDP4Hit-E10-Ta_AbcvGRV-3_XWjH_1zTpfNUEtEPkAVQe8UOavSgRwMr24_zKSo-OhvUWYUlfLzUKsNhWYzfP0HmKq9aLyRvbJnlMRjSEmqHBQ9DOPnFFH4TQj8y2LA_NjlAZHYtgEIHa4T7pHBqjoSLgg5vhTSdChRMEtD8zYDW7BM-MCMVoZKRvmGgL1StQ_Kjf-Vpxx4683ZSnnyh-m2FGDIi-_ZPe8_F1p36raXTB50JrfDmTJ7xfm1Cd2eADj9xuS0aArolFxB_3kTr1p1Y6jCG1Fsrt8OQ7q3287N9xxpbW35Bmk_NSkrHcsAkDInKwDqVX84C1mpwE2FxIq5gUsQzKM8I4iUrGeZYlFBXeL7Lq8kOP3il1_QbHfif_NME2QUY9TnzWQ0LivEKpy8lOwO2JkyFYWQU6hSR7EisMyt8fePFN3uLroXsu3_LBgNEZnEzT2ROyd4D7SUiU1P7SabXSLpHfCEFIrCdk1E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12bacc8c1f.mp4?token=jMNPJMYxpJyo-crjxTRZ7lWqLFHCq6Fj2Ok9oZF_v9I_h7aJ7r1smcTvKfx0aywK8Mjcq0AI1sbjCufvhiJHO9Fvkk5nuaKAUwzKAGE4f4ym0cm5waCZvrubyTsBxlkXNEYNeznF29W7XtNBSKD7u7rk7ShDBfqKpb0tEdjybV-bQRd3hqFzxTmz4B_cBEaqDP4Hit-E10-Ta_AbcvGRV-3_XWjH_1zTpfNUEtEPkAVQe8UOavSgRwMr24_zKSo-OhvUWYUlfLzUKsNhWYzfP0HmKq9aLyRvbJnlMRjSEmqHBQ9DOPnFFH4TQj8y2LA_NjlAZHYtgEIHa4T7pHBqjoSLgg5vhTSdChRMEtD8zYDW7BM-MCMVoZKRvmGgL1StQ_Kjf-Vpxx4683ZSnnyh-m2FGDIi-_ZPe8_F1p36raXTB50JrfDmTJ7xfm1Cd2eADj9xuS0aArolFxB_3kTr1p1Y6jCG1Fsrt8OQ7q3287N9xxpbW35Bmk_NSkrHcsAkDInKwDqVX84C1mpwE2FxIq5gUsQzKM8I4iUrGeZYlFBXeL7Lq8kOP3il1_QbHfif_NME2QUY9TnzWQ0LivEKpy8lOwO2JkyFYWQU6hSR7EisMyt8fePFN3uLroXsu3_LBgNEZnEzT2ROyd4D7SUiU1P7SabXSLpHfCEFIrCdk1E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
#تماشا_کنید
💠
رونمایی از طرح «
کیف پول مهارت - کاراکارت
»
با مشارکت بانک تجارت، سازمان فنی و حرفه‌ای کشور و شرکت کارت اعتباری ایران کیش با حضور آقای دکتر عارف معاون اول رییس جمهور
✅
کیف پول مهارت یک اعتبار اولیه و محرک است برای کسانی که انگیزه یادگیری دارند اما برای شروع مسیر آموزشی با محدودیت مالی مواجه هستند.
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/678003" target="_blank">📅 13:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678002">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c045e4b74.mp4?token=LT9KSu3u6m9Tf_utukC8YI9v-THoFa11jnLeMPt4L1I1x4FmdNXQL1Dg0-SirpYbqlxukdovMS1Yktvk-x9h3TAYz4xhN_YMZGHWBOprtfBSABenSKer4LlpN8H2-atlWA2Mc2yMonhbrcdl5_tajXYN4Or5aw6zHk5JBqV4vfZEXEPLFiOEOt_6tEvMFJ4CXjSyp6FWvWh-M7PcNa4hwWhJu_uLTyVzbiWsZ17GE3Lya_vfijR1duP2iHDAUVsyDy_dCOUCTFLZLBBb0TeWEU5UqXjalEL1l2B-2HAwQZHk-53pavumuoZO3NbsKydnDlcmtnG6jwCNO-1D-9oCDnJYH7fQXsOhvc7hAxsnb_8ESNXiKiAfsio6RbohZqshJgQJmoOKbArqCEXIGkQtU48TswYPJpodzGdBpz4cGEFZs8nhq_l765MtHmW74cfIuVLFT2DA4RR2XpxnRLxZxEyLFM3PgT-2MjjhB_RYoaNCagYBorApZgBUZvZ0R9ViGa1qV5d6xXT3YMF-Wh5MUESBtZlLOfGFvAosSw5WQIVHUS-9KFN5GSxi71HyDEsEZ5OpENu1hSsi78wn5NjHwkL2nTTR5Ae9xdmM2vxqRk102d7i1-_tPhbm_dy1p6XHF2FWaUGA1JTnkXQLmxWwmBtoxPhaJ3Aym6_cZp4DytA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c045e4b74.mp4?token=LT9KSu3u6m9Tf_utukC8YI9v-THoFa11jnLeMPt4L1I1x4FmdNXQL1Dg0-SirpYbqlxukdovMS1Yktvk-x9h3TAYz4xhN_YMZGHWBOprtfBSABenSKer4LlpN8H2-atlWA2Mc2yMonhbrcdl5_tajXYN4Or5aw6zHk5JBqV4vfZEXEPLFiOEOt_6tEvMFJ4CXjSyp6FWvWh-M7PcNa4hwWhJu_uLTyVzbiWsZ17GE3Lya_vfijR1duP2iHDAUVsyDy_dCOUCTFLZLBBb0TeWEU5UqXjalEL1l2B-2HAwQZHk-53pavumuoZO3NbsKydnDlcmtnG6jwCNO-1D-9oCDnJYH7fQXsOhvc7hAxsnb_8ESNXiKiAfsio6RbohZqshJgQJmoOKbArqCEXIGkQtU48TswYPJpodzGdBpz4cGEFZs8nhq_l765MtHmW74cfIuVLFT2DA4RR2XpxnRLxZxEyLFM3PgT-2MjjhB_RYoaNCagYBorApZgBUZvZ0R9ViGa1qV5d6xXT3YMF-Wh5MUESBtZlLOfGFvAosSw5WQIVHUS-9KFN5GSxi71HyDEsEZ5OpENu1hSsi78wn5NjHwkL2nTTR5Ae9xdmM2vxqRk102d7i1-_tPhbm_dy1p6XHF2FWaUGA1JTnkXQLmxWwmBtoxPhaJ3Aym6_cZp4DytA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▪️
تاب‌آوری سازمانی کلید عبور از بحران‌های پی‌درپی
🔺
تاب‌آوری در کسب‌وکار دیگر انتخاب نیست؛ ضرورتی برای بقا و رشد است. این توانمندی بر چهار پایه حاکمیت چابک، اندام‌واره‌های قوی، تاب‌آوری مالی و تاب‌آوری جمعی استوار است. براساس
«
نسخه سخت‌جانی بیشتر
»
👈🏻
دریافت مشاوره:
۸۸۷۲۵۲۶۹
(۰۲۱) |
۰۹۱۰۲۶۶۹۷۱۴
|
service.tccim.ir/intl</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/678002" target="_blank">📅 13:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678000">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqYvF0Cd-xTW_bLtOobypF-JiMj38y4jRmkXnZupv_y7ecDimooy4A3Vgm4OYRca48jBoP6CNzCAiCEOIbEnJo7pvZ8IshwwJVoS9QZWVXJkQlBxG_bLPMlPG0tFgWwR-K9dQpwme1SLrzXJb9TwZcvDHbCsaXTA3XZ1fr01nWaeOZszp2wb40XekXoIRRNFGIB3wpa-ccStroNYojlzCT10HYrBtCbB2sOVZsvuH2ZCeRgOULrT68ACCuf05HOMbAYK4wNf-M_hqcU4386rn2hq-Rw6AztP7NsZnqfWKqvCiS8dtBMianu7P-BoTVUNxRcvVOlS_Acq9wyMpJ-Khw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0fd8c243.mp4?token=XPXPrIGFyvOCN-tAepMyISCN-ddsJZa2GF3YZrY7jrtM5uvl97dm0QID8ZG0jjnKbjmHn3LEZp9h9AS5a4Sj9K9ei__tsSHl8qq0Fx4SSvgcAbSk4eD0EXDte5VFabdAPm8N_WYpapmV-2pAuzCOwO-C-OCsCyb-cUi99i6Grjf99HLGJ5HaDqFC8Qzw67X0EB9jkBem5b4TkVdrZRETUB4uP4sRqj1YnT-tmqcLOPCa6LNP_iqKE4MQYr6Z5sPxyibU-xQG12ePf70pOcEjazsYusSu0gXfKOVJp7ZcusgI2CLgXJWpKbG2wIS6lRnMUFrgaGxEAAI2JjSTXF0ZKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0fd8c243.mp4?token=XPXPrIGFyvOCN-tAepMyISCN-ddsJZa2GF3YZrY7jrtM5uvl97dm0QID8ZG0jjnKbjmHn3LEZp9h9AS5a4Sj9K9ei__tsSHl8qq0Fx4SSvgcAbSk4eD0EXDte5VFabdAPm8N_WYpapmV-2pAuzCOwO-C-OCsCyb-cUi99i6Grjf99HLGJ5HaDqFC8Qzw67X0EB9jkBem5b4TkVdrZRETUB4uP4sRqj1YnT-tmqcLOPCa6LNP_iqKE4MQYr6Z5sPxyibU-xQG12ePf70pOcEjazsYusSu0gXfKOVJp7ZcusgI2CLgXJWpKbG2wIS6lRnMUFrgaGxEAAI2JjSTXF0ZKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با کمک این افزونه رایگان، می‌توانید ویدیوهای گوگل کروم را دوبله فارسی ببینید
🔹
افزونه جدید Livdub برای مرورگر کروم امکان دوبله زنده و هم‌زمان محتوای صوتی وب را به زبان‌های مختلف فراهم کرده است. این ابزار با دریافت کلید رایگان جمینای از گوگل کار می‌کند و صدای ویدیوهای یوتوب، پادکست‌ها و استریم‌های زنده را با تأخیر بسیار کم به زبان دلخواه پخش خواهد کرد.
🔹
این افزونه بدون نیاز به ساخت حساب کاربری عمل می‌کند و کلید API کاربران تنها روی دستگاه شخصی ذخیره می‌شود. دسترسی‌های صوتی این ابزار نیز به‌صورت انتخابی صادر می‌شوند و کاربران می‌توانند دسترسی هر وب‌سایت را به‌طور مجزا مدیریت کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/678000" target="_blank">📅 12:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677997">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lS47PY3xBXl3vyT0xsT9uCZpBXQ7Ak1lsXph2iO7iDm1HQbMGlLvadYe75YMWsRIRyMSr4p_Cc4Dt4KsEhCr4MwNd6MG_atExvN0HSzxR7ecTxOw0VhCuaXM2Y6kng6YPu8RqPE2I7dq4wWjQpv0DK9eKihv7ANI2rEonaUAwe0eVToB01L_6FZ12Q3Cu9YiK_ac7pMQTZ4OYcu9H_dME7a2zYkW6HKjLOs2MtCtQla5DnqphDFKpRlbvhvnfNkILW-2eNY2_0bOC4cR1krkrKMMdcf_RsJXYoWzC4WaG-Vc99xV7WT3xrETJzSruhBza9aly2YEvgIULJeOrB8LvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱۲ مرداد ۱۴۰۵؛ ساعت ۱۲:۲۵
🔹
قیمت دلار در بازار آزاد امروز، با شروع معاملات افزایش یافت و به ۱۹۲ هزار تومان رسید.
🔹
ارزش این اسکناس در یک ماه اخیر حدود ۸ درصد رشد کرده و در مقیاس سالانه نیز با جهش ۱۰۶ درصدی مواجه بوده است./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/677997" target="_blank">📅 12:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677996">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca2d856288.mp4?token=g8yyf0l3iTimcf6FXIsHMJSlUcEGtFEPphgzwKcrgosHzur_XIVhdusXymaRftNo3a2-WWFeifo3YYcrK4q2adp60PHi2qDMIfdYicRfQOK9KVAbvQJ_f4763U-QxL_qh2A5XVzCgVi__bQ_ItQivZFPm9sWKy9J_0iJ_h1Z5XSWW13Fmy60yGJP4aLRq9NjcdT8e-_hHZgVsgrjyMxcSlqjGxhTy6gmfFtxMnmLMeKiEcEuhBfZnRi5QqQLaeICzsXFVHjtaUNEDZvLZtDt5c3DCV05x-l0YYRq_KjrfBQ0UJL7pqoYPuClSfD10RH7u1-UxK-EsQFoYaBhcU2vWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca2d856288.mp4?token=g8yyf0l3iTimcf6FXIsHMJSlUcEGtFEPphgzwKcrgosHzur_XIVhdusXymaRftNo3a2-WWFeifo3YYcrK4q2adp60PHi2qDMIfdYicRfQOK9KVAbvQJ_f4763U-QxL_qh2A5XVzCgVi__bQ_ItQivZFPm9sWKy9J_0iJ_h1Z5XSWW13Fmy60yGJP4aLRq9NjcdT8e-_hHZgVsgrjyMxcSlqjGxhTy6gmfFtxMnmLMeKiEcEuhBfZnRi5QqQLaeICzsXFVHjtaUNEDZvLZtDt5c3DCV05x-l0YYRq_KjrfBQ0UJL7pqoYPuClSfD10RH7u1-UxK-EsQFoYaBhcU2vWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ویدیو در اینستاگرام پیدا می‌کنید که بهتون بگه عمل‌های زیبایی چقدر قربانی داشته؟
🔹
انقد محو زیبایی‌های پوشالی شدیم که دختران‌مون در سنین پایین دنبال عمل‌های غیر ضروری زیبایی می‌روند و از عواقب اون کاملا بی اطلاعند... @AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/677996" target="_blank">📅 12:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677995">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
هم‌اکنون | رهگیری پهپاد MQ9 بر فراز تنگه هرمز
🔹
یک فروند پهپاد MQ9 توسط آتش سامانه نوین پدافند پیشرفته نیروی هوافضای سپاه بر فراز آسمان تنگه هرمز رهگیری و مورد اصابت قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/677995" target="_blank">📅 12:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677993">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ftc0SrvluKcYWAjeCdmr4LuuGCCjIsbc6x4PzA3mO8uRnptgUEUu_qo0HvSX7IHEaZDVIj8ZqEHwi_50bzaG2txSX8Y2cceCei4vTx6bDeN3EGUr1dXzqkCa93ms7MB_ypeo1OOtxf1QoiRajzSgz9j6oRsCjbWJTzp9hp7eydcebzfDqzTo6_4ta74DR0M-nRElRcrcJjX0xkd48bAlhC9-0FzWzh_XAHKampthZyGoV-VFDsDerKfBNMEJnYRkjDrBcte3qDxkNBMommBN9Wa4BKah7TT7O2-YY99ROAw2mqMnmOEQhuyso9uiJfpW3vwX7OMS5K1Vr68RxLKGjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت محمدصادق لواسانی؛ خبرنگار فرهنگی سینمایی از پخش یک سریال متفاوت در شبکه سه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/677993" target="_blank">📅 12:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677992">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b4b2ba517.mp4?token=OkRf1az47IgeaModJqMiWPEA6CGo76NeslLVuj1i0S5cNkNRllWu0aJ-IVShth9yX_3hLG-aHUPY4ZQaLdU4R2ZUrr2vx0Gsc9jSVLaXlqc_8DtaZQtwcgRveLLdR1fukDU0x3rX-qH6uYVcN1BB8nFm8F0Mx02rpKG4vIbVLirXDjslpW5AYk1oToNrGlhvjjDeqnQuxOcjhe9UG6f0vtguqI95L89CkPM67K4NKIGeasOI-FRLtW3bqf8NzUDHZXV7IOCsLtY4KJr0xSirylafa6wDAH6Cp-wIC9Ol_wZ-imCxi5QNmbFMJGjrECJwS0Ca64T5XlQNW1cMtqpYrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b4b2ba517.mp4?token=OkRf1az47IgeaModJqMiWPEA6CGo76NeslLVuj1i0S5cNkNRllWu0aJ-IVShth9yX_3hLG-aHUPY4ZQaLdU4R2ZUrr2vx0Gsc9jSVLaXlqc_8DtaZQtwcgRveLLdR1fukDU0x3rX-qH6uYVcN1BB8nFm8F0Mx02rpKG4vIbVLirXDjslpW5AYk1oToNrGlhvjjDeqnQuxOcjhe9UG6f0vtguqI95L89CkPM67K4NKIGeasOI-FRLtW3bqf8NzUDHZXV7IOCsLtY4KJr0xSirylafa6wDAH6Cp-wIC9Ol_wZ-imCxi5QNmbFMJGjrECJwS0Ca64T5XlQNW1cMtqpYrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا کوه کلنگ برای ترامپ مهم شده است؟/ اطلاعات ارسالی اندیشکده‌های آمریکایی و صهیونیستی درباره این کوه به ترامپ چه بود؟
/ تلویزیون اینترنتی مدار
این برنامه را در تلویزیون اینترنتی مدار ببینید
👇
https://youtu.be/ZSHebN8ENME?si=eoY_qIGU4ksK53-n
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/677992" target="_blank">📅 12:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677991">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1424633e1.mp4?token=pRLYS4DrCaijLRKEacXa0z1HOsHJjWGsG8im1HLtabr1E5pmRrgTvcjV5JsxQww25mRUk0OSDfJndMJaHz6-p-5-gGmKf4fOsJEyVWFlnoiMbers9U1lqIEl7stVItPLm2PwUnBs92x7tq9R7PyhQAQbzSUz96kTq3BID4n2mnHsg9MiMY6_kINdi3mXLc7zsGv2ZQT62lEubbPeKUDxxCEvgS-CGHrqyvA8URu4qM1-45TS8csfn2BYq7naAS_goAXrEwGNdQcAcA3-c1sqn0BxEIoUsHmc4-26_FIiHcoOxONrVdq0OBT6_gUOQFvsGWsJQH-dJ-AuQJ4ps3Xh1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1424633e1.mp4?token=pRLYS4DrCaijLRKEacXa0z1HOsHJjWGsG8im1HLtabr1E5pmRrgTvcjV5JsxQww25mRUk0OSDfJndMJaHz6-p-5-gGmKf4fOsJEyVWFlnoiMbers9U1lqIEl7stVItPLm2PwUnBs92x7tq9R7PyhQAQbzSUz96kTq3BID4n2mnHsg9MiMY6_kINdi3mXLc7zsGv2ZQT62lEubbPeKUDxxCEvgS-CGHrqyvA8URu4qM1-45TS8csfn2BYq7naAS_goAXrEwGNdQcAcA3-c1sqn0BxEIoUsHmc4-26_FIiHcoOxONrVdq0OBT6_gUOQFvsGWsJQH-dJ-AuQJ4ps3Xh1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاور پیشین سازمان جهانی بهداشت: کووید ۱۹، ساخت آمریکا بود
🔹
در حالی که آمریکایی‌ها بارها گسترش کووید ۱۹ و همه‌گیری بیماری کرونا را به گردن چینی‌ها انداخته‌اند، اکنون جفری ساکس، استاد دانشگاه آمریکایی اذعان کرده که این پژوهشگران ایالات متحده بوده‌اند که با دستکاری در ژن ویروس‌های کرونا، ویروس کرونای جدیدی را ایجاد کرده‌اند.
🔹
پژوهش برای دستکاری ژن‌های ویروس کرونا، «با تأمین مالی مؤسسه ملی بهداشت آمریکا (NIH) و توسط یک تیم تحقیقاتی در دانشگاه کارولینای شمالی انجام شده است.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/677991" target="_blank">📅 12:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677989">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8KmY_Lfh_-R9L3pDfLJoy07KgHnQ89ldMT_UcY1fyrqPj5BVFz2fFglQUoYldRARe6h3l2XFKynphnUVADg1zks39l277nWuCzq7HpXHQAqpCxw65bRbNgatizvyysRWA-Wk58n9EsGSDjYHMeaDua8RSUEdIA0mazfuPGuInSAqHHKJgUVoViZ0c1PXe0pOfq6qVZe7Ko_KdMz2LpGpXbr0xwBmFYa7WtlOH1mrWKZ6Ok8E6R32OjmjS2-ldregJyjnzErL3zbGhZ_MN_nBVRckD6IZMliUB1hFxRuKCwPaoBZOeeTD4eKtJ4ESuz9xGQPrAWtoY_wkn8BYhKLnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سایه‌روشن مذاکرات ایران و عمان درباره تنگه هرمز / پیشرفت گفتگوها زیر سایه خروج تهران و واشنگتن از تفاهم اسلام‌آباد / بیانیه تازه‌ای در راه است؟
🔹
خبرهای رسمی حاکی از پیشرفت گفتگوهای تهران و مسقط است هرچند رسانه‌های غربی می‌کوشند این توافق احتمالی را نوعی عقب‌نشینی ایران پس از تهدیدهای ترامپ نشان دهند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3235099</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/677989" target="_blank">📅 12:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677988">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlBhjgTu2Wr5KZ0ZXB_8zmK13GpzdmBnOR7xbgYT2H7UyOKR7sMC0YGANTuaZwVG08r1fToT-woZWaMcUBqiEYxKefdshBiGMXdFsPd74sG4gKTCDFO8feKJ9zYbRJaeGuM9Wk27EUn7QTmimtVWZ-VhEaAPzhVsE1FbR1Ieg_2DnAegATBWqRxxOMuCoRxEFd7d22YL-AOiCr-YRup7Mc6XCoCGfqan2XUm58g0JFnEIuW4tZL_7MZGr5ARx03A3IeZshB3fKiOGEsxOT5wR_4myKeHkvYrmO7d_S-6Ce6UK9Mz1y-61ioLFgzWJJdX_reifyYl8xl1VSkqe4pVNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آشنایی با مخفف‌های پرکاربرد پزشکی
🩺
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/677988" target="_blank">📅 12:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677987">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
میرشایمر: اسرائیل یا باید خلع سلاح شود یا از بین برود، جهان توان تحمل این بار را ندارد
🔹
اگر اسرائیل در جنگ شکست بخورد، ممکن است به ایران حمله هسته‌ای کند مبادا در جهان هیچ دولت یاغی دیگری باقی بماند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/677987" target="_blank">📅 12:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677984">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQmUxjtfVXqiyjy-XZhhZcKDIOLkV-2Nc2GYbdGTEVXcPraAEhPbse3TnltDGGOOQIvKCcHwgwYH08D-9nXWidwBvlb6E0uJAZNS6VMokg0qKLwkvEoWIdoJK_W4VI_WKue1Mzi7MCSIMoTBYuWYefHrWCPhJMDSMnURC_KHKJNCL6pyDu6V7T1iQE-0MjYXYBvHz1rUoPGjjtCoSblrM7mfTascmK2mG64mIQtvbl4RDOTMOF9ZyXPvYxmrdlAo-TW1mYVgpWK-glyYyBE3ouRvCJkjgthXlcHsDCftEFp5Gj6FJurX9z0zErkmx6YLMlBYKH0uQZq8H0dmIK6u7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویژگی‌های بیش‌فعالی در بزرگسالانی که ای‌دی‌اچ‌دی دارن، چه شکلیه؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/677984" target="_blank">📅 12:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677983">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0467809d.mp4?token=lfBES8NFbo3-41-StavNwuIeXEqQW2LYxil-w7JUNu15f_eKP5jnRiuGsMP9P20eRhFgL1uSS7UZLfzZU0FoPAR6niupjCLTZA9wS5qvhRpgH-80qB8b237BkKB9OiObhwN_dY2HGxzyaxF_wY5huBp3WM6ycChVDgj7626yOb6zwY8PBH4XONFh8pWscgttQJDKw1utxycK4s04uvJ5OCLJgtUoaRQzgwGZMYNVxEmW6UDWz_IOQue2WFfzOolQM_IqevJZ46U8o0AJ-L-6iswVUa9PhyortdIclnyDrnd3EwJE8rcPA-BEWXGIMAFHwGMkOoEZRDWYIb-lC7PjjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0467809d.mp4?token=lfBES8NFbo3-41-StavNwuIeXEqQW2LYxil-w7JUNu15f_eKP5jnRiuGsMP9P20eRhFgL1uSS7UZLfzZU0FoPAR6niupjCLTZA9wS5qvhRpgH-80qB8b237BkKB9OiObhwN_dY2HGxzyaxF_wY5huBp3WM6ycChVDgj7626yOb6zwY8PBH4XONFh8pWscgttQJDKw1utxycK4s04uvJ5OCLJgtUoaRQzgwGZMYNVxEmW6UDWz_IOQue2WFfzOolQM_IqevJZ46U8o0AJ-L-6iswVUa9PhyortdIclnyDrnd3EwJE8rcPA-BEWXGIMAFHwGMkOoEZRDWYIb-lC7PjjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری به یک اسرائیلی: بر اساس حرف‌های شما، جان یک اسرائیلی به اندازه جان هزاران فلسطینی ارزش داره
🔹
شخص اسرائیلی: نه، این کاملا غلطه، جان هر اسرائیلی به اندازه ده میلیون فلسطینی ارزش داره.
🔹
مجری: اما این نژادپرستیه
🔹
فرد یهودی: آره هست، چون خدا ما رو انتخاب کرده و شماها دارید حسودی می‌کنید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/677983" target="_blank">📅 11:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677982">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromانجمن تجارت الکترونیک تهران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae2e4338b.mp4?token=IOCs2Rp6hPt3LDwFe52fMFFgyEleL7mIm5pgi8yN0LExcg9-ayOcGcoIzFIr4lLQllCAP3dDFuVOOOZYgzRax_mU67m944ywGyaAZl2ErutBa1z8PX4bmFVHUwDv4GWGI8JL9mWyass0JU6TSg6AQL7brMJKCqhWvXpU01hsngr-2LFWayrlFhWrmsHVkkvV5NShziT71t2VKpxO4AdAcgjawlSqLdflEs445yLH2D3SxArKeYA1z9EHGPjSmmH7FkG3QjGAJZebAeEkXLw_T4UbNR06MVMJk1L1YNT87bDzkpAgHWKEMGkd8FueGNxPRliG14MHegkd0ho9NyPUVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae2e4338b.mp4?token=IOCs2Rp6hPt3LDwFe52fMFFgyEleL7mIm5pgi8yN0LExcg9-ayOcGcoIzFIr4lLQllCAP3dDFuVOOOZYgzRax_mU67m944ywGyaAZl2ErutBa1z8PX4bmFVHUwDv4GWGI8JL9mWyass0JU6TSg6AQL7brMJKCqhWvXpU01hsngr-2LFWayrlFhWrmsHVkkvV5NShziT71t2VKpxO4AdAcgjawlSqLdflEs445yLH2D3SxArKeYA1z9EHGPjSmmH7FkG3QjGAJZebAeEkXLw_T4UbNR06MVMJk1L1YNT87bDzkpAgHWKEMGkd8FueGNxPRliG14MHegkd0ho9NyPUVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسابقات جهانی مهارت (WorldSkills)، بزرگ‌ترین صحنه بین‌المللی رقابت‌های فنی و حرفه‌ای است؛ جایی که جوانان ماهر، نمایندگان صنعت و آموزش، گرد هم می‌آیند تا ارزش تخصص را در اقتصاد امروز برجسته کنند و استانداردهای جهانی مهارت را ارتقا دهند. این رویداد، پلی است میان آموزشِ مهارت، نیاز کارفرمایان و آینده شغلی نسل جوان.
🔸
انجمن تجارت الکترونیک و شرکت‌های آروان‌کلاد، اسپارا، بیت‌پین، جیبیت، دیجیکالا و گروه مدیریت سرمایه لیان کپیتال، در این دوره از مسابقات ملی مهارت، حامی رشته‌های تخصصی فناوری اطلاعات هستیم:
توسعه نرم‌افزار، امنیت سایبری، مدیریت سیستم‌های تحت شبکه، پردازش ابری، فناوری‌های وب، توسعه نرم‌افزار موبایل، طراحی گرافیک و رباتیک.
🔹
همچنین رسانه‌های ایرانیان استارتاپ، پیوست و‌ دیجیاتو، جزو حامیان رسانه‌ای این رویداد هستند.
🔸
اگر در این حوزه‌ها تخصص دارید و آماده‌اید تا مهارت خود را در سطحی نزدیک به استانداردهای جهانی به چالش بکشید، جای شما در این رقابت خالی است.
برای کسب اطلاعات بیشتر، آشنایی دقیق با رشته‌ها و ورود به سامانه رسمی ثبت‌نام، به لینک زیر مراجعه کنید:
etchamber.ir/worldskills
🆔
@etchamber</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/677982" target="_blank">📅 11:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677981">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7abafac1a.mp4?token=b4InKA4TZy25ZuA47vmBIP9UoPKZgLCTn-8SWkn31HyMytXehJriQYSbHxHiePVZ5iOQpMi2uZZ-bJFiW5-qc1TPmORrLLiho_iHEWixCroJohBdFyjtGOnzFJTIn9mRRuL_MqHvJEdtqLnR6baeR4oyCflxdYIwb3HfwzEhSIk2ncahh4A6CvC6L0nNPsOmW9aN_g7yd-ogO3dxjWIvG0I0YhTC3s8OfaIqsJ7_cbK7VlBUJQ_b28O_kHXBVJ4206GA_-xajvywXpuKO8k8lpoYT9SfwcCQotIXn7KeiqyGXmGLuYtxcUEJn3YF7_iKrIg_6GwNkZwYMhOK2DClpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7abafac1a.mp4?token=b4InKA4TZy25ZuA47vmBIP9UoPKZgLCTn-8SWkn31HyMytXehJriQYSbHxHiePVZ5iOQpMi2uZZ-bJFiW5-qc1TPmORrLLiho_iHEWixCroJohBdFyjtGOnzFJTIn9mRRuL_MqHvJEdtqLnR6baeR4oyCflxdYIwb3HfwzEhSIk2ncahh4A6CvC6L0nNPsOmW9aN_g7yd-ogO3dxjWIvG0I0YhTC3s8OfaIqsJ7_cbK7VlBUJQ_b28O_kHXBVJ4206GA_-xajvywXpuKO8k8lpoYT9SfwcCQotIXn7KeiqyGXmGLuYtxcUEJn3YF7_iKrIg_6GwNkZwYMhOK2DClpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در شبکه‌های اجتماعی ادعا شده این زن برزیلی ۱۲۶ سال سن دارد و هنگام پایان جنگ جهانی دوم در میانسالی بوده است؛ ادعایی که به‌ سرعت مورد توجه کاربران قرار گرفته
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/677981" target="_blank">📅 11:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677977">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enu2cQFbIChSxEnABcSPOxDpT_z0qYytmD0q_GYJMzOsxA9plKt1wIxOpVAWVsvfYQvnEy_CESACb-Iki8U17TP0r5LPXmEgg9MR_i_hi6qkD8I0pK_SXR0Yo_Y1lb7ew6GL7BZZHnoSZyluYuv6HvyKkULrbZaKmpUxoi6jljoKAfF5vcC4LmOkKAgNRSOIuivCdO_qPZGYjkTr-W2ykMh4HTk-IiQpKBNECAxgjo8C7KqpowD_Cy1WM_ARogwm4fB7oCLmq6BCjBLgF7FblE0A5fOVXVfOAbxCwfooz3Tp7hlJU_ac95puRgP2m7ToPV2ItLtY7UHUQ5-wK4TOGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آگامای خندان، خوزستان
🔹
سیدباقر موسوی
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/677977" target="_blank">📅 11:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677976">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromامـیـن‌الـلّـه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d206ee0a.mp4?token=pp9mZjC-NqgYIV8DU6HCBJxjRCF2_QdD_OewG3oixxJCjfN-j1jmcdiwJNvXZ_kEnJ7djG58alffu1r4cm5vXSKgOWMsYbuGfKWAEzJDf6Mg_3NzRUgvlXsI8dE-Y-ydqWVSkK3wQPqOPPK26hZiPUoKn9raBD15BTxU5ftVB67jFVPIfmqEnfVTMknsEf6RK37eoNFvmGTK2Dl-3nO5-Ddhh6sYX5RVtt36iX7UEruErUoSq2_XHbvLltFaltb8YH0pav2UXTionVWvu2iwHvf85qHT6eiW4tOwJnHgyv16R2IqPyCIhyflbyqCpcBQ6PkocQUZ20Xp0tlyVvneIVwufpNe3fGhgVUgiLeS7JKpsibNmZ8zyXoISeaacV-vOFK-NsucG4JYxJ2HavNGXJqxu1r8oO6r-kSZ0lGqWdL6kQckZspXgJWfd1xqRPwv7rA8KLc5Zr8eR1MUgtkZKa4Zm3pgMxymw-cbWmF5pGVN8-xLxCBc2__LK-NOFj3opHDzRvpTfJ8IWGGeZ9SDpij_mHQdQ0jnG22ELU7LbocxLM5j_4N2oo1FPPnUYY6qex8zgag-d6-MVQBKIZizVmnMIwe28k7naRB4NC39WNHSvGsgHT7xnNC7mnWh5UamN6Shn4DKXmUwpT5AbceW-XVD4WFwvOu-tYTKjCEJOU8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d206ee0a.mp4?token=pp9mZjC-NqgYIV8DU6HCBJxjRCF2_QdD_OewG3oixxJCjfN-j1jmcdiwJNvXZ_kEnJ7djG58alffu1r4cm5vXSKgOWMsYbuGfKWAEzJDf6Mg_3NzRUgvlXsI8dE-Y-ydqWVSkK3wQPqOPPK26hZiPUoKn9raBD15BTxU5ftVB67jFVPIfmqEnfVTMknsEf6RK37eoNFvmGTK2Dl-3nO5-Ddhh6sYX5RVtt36iX7UEruErUoSq2_XHbvLltFaltb8YH0pav2UXTionVWvu2iwHvf85qHT6eiW4tOwJnHgyv16R2IqPyCIhyflbyqCpcBQ6PkocQUZ20Xp0tlyVvneIVwufpNe3fGhgVUgiLeS7JKpsibNmZ8zyXoISeaacV-vOFK-NsucG4JYxJ2HavNGXJqxu1r8oO6r-kSZ0lGqWdL6kQckZspXgJWfd1xqRPwv7rA8KLc5Zr8eR1MUgtkZKa4Zm3pgMxymw-cbWmF5pGVN8-xLxCBc2__LK-NOFj3opHDzRvpTfJ8IWGGeZ9SDpij_mHQdQ0jnG22ELU7LbocxLM5j_4N2oo1FPPnUYY6qex8zgag-d6-MVQBKIZizVmnMIwe28k7naRB4NC39WNHSvGsgHT7xnNC7mnWh5UamN6Shn4DKXmUwpT5AbceW-XVD4WFwvOu-tYTKjCEJOU8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">؛
جنگ نخواهد شد، مذاکره نخواهیم کرد..
چرا و چگونه؟</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/677976" target="_blank">📅 11:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677973">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
شاهکار تازه بی‌ام‌و؛ M 1000 RR 2027 با سرعتی فراتر از ۳۱۴ کیلومتر بر ساعت
🔹
یک سوپربایک آلمانی تمام‌عیار و یکی از سریع‌ترین موتورهای دنیا که با موتور ۴ سیلندر و حجم ۹۹۹ سی‌سی، قدرت خیره‌کننده ۲۱۲ اسب بخاری تولید می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/677973" target="_blank">📅 11:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677972">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q66WYdKNe4DWHlSHVpebT1kYkXuSFyirSKSBFdJI_HJVZetxDF2tuvKUAFk8jQCzvGJxp28kdhhucKteGZqE55Mj7pJiogkx3-vfVcTqZ8U0fuw0yV4FsEnLJmm9-k1jDn-6IyHzEoo5FQBvWHRsXK1Ifsr-4kcRdW_ySwSQYhYvnS3_nGJPtePcUT7SmsSHXMVVzA_NBtenJUdZtiZ9WfJbjAotC_L-VG-x4GDrE8IPqAF6pL7vF5GgpeB1pjZh-ziM8nTCLdWOlIs6XgOxFUgqyVb3VCF-DWeI-PoEPPCYyF_P2XduWOREctBVQSQ0qNlTk9OODk0SkyMluRqCxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعمیرگاه موبایل شلوغ‌تر از موبایل‌فروشی شد!
🔹
مراجعات برای تعمیر موبایل از خرداد ۱۴۰۴ حدود ۴۰ درصد افزایش یافته و تعمیرات سنگین مانند تعمیر برد نیز به گزینه‌ای اقتصادی برای کاربران تبدیل شده است.
🔹
سهم فروش نقدی موبایل تقریباً نصف شده، حدود ۴۰ درصد خریدها اقساطی است و استقبال از بیمه موبایل ۲.۵ برابر افزایش یافته است.
@amarfact</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/677972" target="_blank">📅 11:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677970">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26fe6ccecf.mp4?token=DIZdYtPFOVHlHzDv9rEm5x5mzh8HA0HOUS7HkjM7rcPRWE1m5bKaGR1pvsbPWgIlzbMXqiDr8HBh63wNc8bTxuEbZvow7hKhh8u7NdM6d0ZMTS99HjrPQpUR44ioMVMYDeLYSyX4FiKEJmdUorOn6ASEB_n54gyZBAMEUa3vf9gN19ZU3LPXQDnVM_4hAMiXYe6WxZzgcio5I6dT6BbM2GWEh60E0kTEkf0Uhkj9YtPqelESagjCoTfFhPDYn4WIsHoXAbaKbje-7WHUZ5T6pkUwDPVEplWytMB9Z-g11RtW4CZ-AgcedDjybDZ5z9CgxY5Jz3lXdftwGOFJoclxByj46DnFoEAZjyZocb8LKsY4KXB58exiUZatHBhk00ddMIxnjaQd8aW7g-A2oVctx-IQ2WiiSMRer95C4bhzhS2QB59ctbVhWYEfyQkMgMgJA4tjsw9hqT7g1V7PMCbv4iv2uJfQESlhEJcD4HCwu1Do7i8J3E6k6sdpVkyEWwQPFa6paqoEBQpnAE-HPKSZOFID1N0h7cwMjlxFNN9nHaWY1KZIy-bSP6rxAGOP6UQ1teUC6fJVUyGNxjHKH8eoMEZljR22bBbNjIFBQi5yIcRU1EPO1P3OixliS27ANTv_YHh2CQn9pkqDtLZSiMOGBRevQParH1we01RdPl5ZKLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26fe6ccecf.mp4?token=DIZdYtPFOVHlHzDv9rEm5x5mzh8HA0HOUS7HkjM7rcPRWE1m5bKaGR1pvsbPWgIlzbMXqiDr8HBh63wNc8bTxuEbZvow7hKhh8u7NdM6d0ZMTS99HjrPQpUR44ioMVMYDeLYSyX4FiKEJmdUorOn6ASEB_n54gyZBAMEUa3vf9gN19ZU3LPXQDnVM_4hAMiXYe6WxZzgcio5I6dT6BbM2GWEh60E0kTEkf0Uhkj9YtPqelESagjCoTfFhPDYn4WIsHoXAbaKbje-7WHUZ5T6pkUwDPVEplWytMB9Z-g11RtW4CZ-AgcedDjybDZ5z9CgxY5Jz3lXdftwGOFJoclxByj46DnFoEAZjyZocb8LKsY4KXB58exiUZatHBhk00ddMIxnjaQd8aW7g-A2oVctx-IQ2WiiSMRer95C4bhzhS2QB59ctbVhWYEfyQkMgMgJA4tjsw9hqT7g1V7PMCbv4iv2uJfQESlhEJcD4HCwu1Do7i8J3E6k6sdpVkyEWwQPFa6paqoEBQpnAE-HPKSZOFID1N0h7cwMjlxFNN9nHaWY1KZIy-bSP6rxAGOP6UQ1teUC6fJVUyGNxjHKH8eoMEZljR22bBbNjIFBQi5yIcRU1EPO1P3OixliS27ANTv_YHh2CQn9pkqDtLZSiMOGBRevQParH1we01RdPl5ZKLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاله جای مادره؛ آخه سینا مادر نداره
🔹
سینا ۲ ساله شهید شده، مادرش هم شهید شده؛ پدرش هم شهید شده؛ مادر نداره که در فراقش بی قراری کنه؛ خاله جای مادرش بیتاب فراق سیناست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/677970" target="_blank">📅 11:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677968">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b10fa703e3.mp4?token=UMSMfBWRBGC-ny8_853PRyMaEH4NO56Fq0n_lug_nBOBZsO2j0AHQ-Eyzj5_mjQHYJ8tLqUK_kyy7Gj8cTQYNlzGwlwp_rkOeqCFK7QMJlfnZkbNJWLedvRuFEuhSCJWe7469-LE5upC5h7StyNVWx9x-wRhuy1D2u0FLeRvFQZo9oXVCoR2Kp0ccg8qLyUmAZUfQEhyLIDCJp7gpOb-BQsTNdMAMsPmzmKO5mtiUYTc5x-oV0W3QIt_HB-MbUXdAMb0Co4cJDps2Mo9bbi5PzxSfcilgT4YB-l-bgBYCVgWrYBu81SzpC1DV-_39RdaEn2jHAInF4wcV3oh6CfjpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b10fa703e3.mp4?token=UMSMfBWRBGC-ny8_853PRyMaEH4NO56Fq0n_lug_nBOBZsO2j0AHQ-Eyzj5_mjQHYJ8tLqUK_kyy7Gj8cTQYNlzGwlwp_rkOeqCFK7QMJlfnZkbNJWLedvRuFEuhSCJWe7469-LE5upC5h7StyNVWx9x-wRhuy1D2u0FLeRvFQZo9oXVCoR2Kp0ccg8qLyUmAZUfQEhyLIDCJp7gpOb-BQsTNdMAMsPmzmKO5mtiUYTc5x-oV0W3QIt_HB-MbUXdAMb0Co4cJDps2Mo9bbi5PzxSfcilgT4YB-l-bgBYCVgWrYBu81SzpC1DV-_39RdaEn2jHAInF4wcV3oh6CfjpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: به‌تجربه برای ما اثبات شده که چیزی جز اقتدار دشمن را از شرارت بازنمی‌دارد
🔹
بقایی:
قرار نیست ظرف این روزها میزبان هیئتی باشیم یا خودمان مهمان کشوری باشیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/677968" target="_blank">📅 11:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677967">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ما از روز نخست هیچ جبهه‌ای باز نکردیم/ موضوع یمن به خود یمنی‌ها مربوط می‌شود
اسماعیل بقائی:
🔹
موضوع یمن به خود یمنی‌ها مربوط می‌شود. این کشور سال‌هاست که تحت ظلم قرار گرفته است.
🔹
اینکه بخواهند هر موضوعی را به جنگ تحمیل‌ شده به ایران مربوط کنند، نشان‌دهنده استیصال آنان است. آتشی که آنان به راه انداخته‌اند، مسری است و مسئولیت هر اتفاقی در منطقه، با آمریکا و همدستان آن است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/677967" target="_blank">📅 11:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677964">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff96cb6e64.mp4?token=Q0I6UJ0tRTPu1lk_AE9AXUSj37ezUlGYZXyQwl5_eq5Yr4sNF_7FUb2bHk3I1-JP4bGMXDT--jliSoZaA8nmp7uI7lPn1tcpHKj7gMarAO945DynklO5CpwI0_eT_3-mX3zG1vWjvgOcnXzeCUEKQWm5RwSCVwi8uaE1mRjq8SD2f_3CBmzq2Ox3yAI7ZlWd0KAzTx4OEP0bFdv8FVE7lDL49K9j4jonHYW5pAJkVs6BduBy_uPKHO7KKx32XeP-D0SnfX3peEPt2JsuISK7Pg1bzS8Rog1IR57zur4kCDgbSlMTw-hm_1U75aqwsC3fgl8B425w0wyJsIjKkthbfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff96cb6e64.mp4?token=Q0I6UJ0tRTPu1lk_AE9AXUSj37ezUlGYZXyQwl5_eq5Yr4sNF_7FUb2bHk3I1-JP4bGMXDT--jliSoZaA8nmp7uI7lPn1tcpHKj7gMarAO945DynklO5CpwI0_eT_3-mX3zG1vWjvgOcnXzeCUEKQWm5RwSCVwi8uaE1mRjq8SD2f_3CBmzq2Ox3yAI7ZlWd0KAzTx4OEP0bFdv8FVE7lDL49K9j4jonHYW5pAJkVs6BduBy_uPKHO7KKx32XeP-D0SnfX3peEPt2JsuISK7Pg1bzS8Rog1IR57zur4kCDgbSlMTw-hm_1U75aqwsC3fgl8B425w0wyJsIjKkthbfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر جدید از لحظات اولیۀ حمله به مدرسۀ میناب
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/677964" target="_blank">📅 11:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677961">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
بقایی: پاکستان میانجی‌گر ایران و آمریکا است/ میانجی‌گر جدیدی از جمله چین اضافه نشده
سخنگوی وزارت امور خارجه:
🔹
پاکستان میانجی‌گر مباحث مرتبط با ایران و آمریکا است. قطر هم در مواردی که لازم باشد کمک می‌کند.
🔹
ما با چین رابطه‌ای بسیار دوستانه و همکاری‌ای نزدیک در همه حوزه‌های مورد علاقه طرفین داریم. چین هم‌نظر با ما در نگرانی نسبت به یک‌جانبه‌گرایی مخرب و ستیزه‌جویانه آمریکا است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/677961" target="_blank">📅 11:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677959">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/973da53f7a.mp4?token=dg0Z13-N6jcW66YZu5rTHGM4yzOSxGClo_S_2P5YTYS1enbgr5qcN-oCER6hISNFb-aGzOI2_Vxp5Wv2ODgTJrod8e6vZmhnZjJmSnNZ0VlXeIuG5ipJ_tvTPSZVmklTDeS8o877wDUOL0nnyXPX-M7pUx61ulpUoliHb1mV-eku5carZ-Jpph4L13wkYe6QzWddOIYcNDrT0wedire-weH3Ybcaj4KXJhsM1-fGK_eFVSeI7EVc525jitMkeFjX9RA8MuhXVfUrZqFGNCzkXh0pWZB7eN1Ue06PDCxVI4uslgMvUSjpOOM2_0y9cgcEouR70siISmKHxD8EoicfOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/973da53f7a.mp4?token=dg0Z13-N6jcW66YZu5rTHGM4yzOSxGClo_S_2P5YTYS1enbgr5qcN-oCER6hISNFb-aGzOI2_Vxp5Wv2ODgTJrod8e6vZmhnZjJmSnNZ0VlXeIuG5ipJ_tvTPSZVmklTDeS8o877wDUOL0nnyXPX-M7pUx61ulpUoliHb1mV-eku5carZ-Jpph4L13wkYe6QzWddOIYcNDrT0wedire-weH3Ybcaj4KXJhsM1-fGK_eFVSeI7EVc525jitMkeFjX9RA8MuhXVfUrZqFGNCzkXh0pWZB7eN1Ue06PDCxVI4uslgMvUSjpOOM2_0y9cgcEouR70siISmKHxD8EoicfOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: امروز عراقچی راهی سفر اربعین است و باقی اعضای هیئت مذاکره‌کننده هم در ایران هستند!
بقایی:‌
🔹
چین با ما در خصوص اثر مخرب آمریکا در منطقه هم نظر است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/677959" target="_blank">📅 10:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677958">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ما الان مذاکره‌ای با آمریکا نداریم
بقایی:
🔹
مذاکرات با عمان و متمرکز بر مسیری است که کشتیرانی ایمن از تنگه هرمز را تأمین کند. تلاش می‌کنیم در اولین فرصت با مشورت و همکاری عمان مسیر موقتی را تعیین کنیم که ایمنی کشتیرانی در تنگه هرمز فراهم شود.
🔹
بنابراین مذاکرات دو جانبه و بین دو دولت ساحلی است. حضور دیگران در این مذاکرات می‌تواند سازنده یا مخرب باشد اما موضوع بین ایران و عمان است.
🔹
تنگه هرمز به دلیل تجاوز آمریکا و رژیم صهیونیستی مسدود شده نه به دلیل اختلاف نظر ایران و عمان.
مادامی که تجاوز نظامی آمریکا و رژیم صهیونیستی و نقض تفاهم‌نامه ادامه داشته باشد تغییری در وضعیت تنگه هرمز ایجاد نخواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/677958" target="_blank">📅 10:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677957">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0d5058d2.mp4?token=cv42Z7bLpC-PvJBwCTd7unGbv_GrhsaWcJhVC7KY9-1NvE28mjm6pahE44CgUDlwgk3r6Ce_oQSuDBB1KDOHxy23yKxA2ST6G_1KE-hgh7FB2onWylEpcyU-odEazdMVdV9Rnn7MYn8GcnFuQUPcpicopa8ocBhSSUizN6A3m3r-fdy4z7pN5jMMkhTgZAcYf4QgxswJ8UktcUA0ax6g0nkbW4irBUDJeYuS7tRAK9Iv0kI-YXk86XjPrnTo9oEsZrd-1WptuM0eKcPbMNC4yDrUhdFmN6_-9tjbuHxHCOGsN31bhecDv_1k4SIic7ep9nPjAXbo5ab2nZDhMKulKbYpZVkDfNQQ7kky_FtcS8gHWtbNutie_8kbMrtXXmasu4rzxx2Am1WhONuecYeENELk33wiH2XSdsIFydnqvztpfTysk6kKcxD4RgavwU5TFeEpubjoX5iB85Hse4GCSkpiqB78og2DPFmULquPSG0MUc_en3oXWMt3yR4E7HERtx78iSN9GOfOp8_lxnrOl6eQRe4FHingptEoO84dMLNrkTSqaufTGgD9cdNXWL5892J39pSzXLrwCFCIUApOnCS2fOUSsOaGoMtzieu-uuyXaYkW47V_ro24fof7d7wAPzsOwEOK0rQ2dTGrg80lb0MWjPuCp7NsGYjcUgT3aZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0d5058d2.mp4?token=cv42Z7bLpC-PvJBwCTd7unGbv_GrhsaWcJhVC7KY9-1NvE28mjm6pahE44CgUDlwgk3r6Ce_oQSuDBB1KDOHxy23yKxA2ST6G_1KE-hgh7FB2onWylEpcyU-odEazdMVdV9Rnn7MYn8GcnFuQUPcpicopa8ocBhSSUizN6A3m3r-fdy4z7pN5jMMkhTgZAcYf4QgxswJ8UktcUA0ax6g0nkbW4irBUDJeYuS7tRAK9Iv0kI-YXk86XjPrnTo9oEsZrd-1WptuM0eKcPbMNC4yDrUhdFmN6_-9tjbuHxHCOGsN31bhecDv_1k4SIic7ep9nPjAXbo5ab2nZDhMKulKbYpZVkDfNQQ7kky_FtcS8gHWtbNutie_8kbMrtXXmasu4rzxx2Am1WhONuecYeENELk33wiH2XSdsIFydnqvztpfTysk6kKcxD4RgavwU5TFeEpubjoX5iB85Hse4GCSkpiqB78og2DPFmULquPSG0MUc_en3oXWMt3yR4E7HERtx78iSN9GOfOp8_lxnrOl6eQRe4FHingptEoO84dMLNrkTSqaufTGgD9cdNXWL5892J39pSzXLrwCFCIUApOnCS2fOUSsOaGoMtzieu-uuyXaYkW47V_ro24fof7d7wAPzsOwEOK0rQ2dTGrg80lb0MWjPuCp7NsGYjcUgT3aZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدرضا باهنر: در کره جنوبی اگر کسی مطالبات غیرممکن و غیرواقع‌بینانه داشته باشد محاکمه می‌شود/ برخی برای رای بیشتر حرف‌های غیرواقع‌بینانه می‌زنند
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
مطالبات غیرممکن در دولت و مجلس و مجمع تشخیص و تریبون ائمه جمعه و غیره شنیده می‌شود.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/677957" target="_blank">📅 10:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677948">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M5-hKwj0_FkA4W-uBH8p0NLmm0Mf4XtE5XrDqPe7urx2ATiTBvcKmQKW612wuIurOV2tc3q2HmowUfOFPOmC-0HM-KMVOLWtVH2_6rk5n6SX5XASWYWUv4H6CjWWAqsccWIHSs0bnwJCgnQS5N_1rt6eKZxlKJf-LYaEEnwR39b_JZbK88zfsFZoMU2TqNFTwUzmla0JUMZB4PjXXJ9i0ZYXnNK8LJQHuigBbyq3IGsg7FWmGuU3cLFvKG-qprw3x3tLNX-vWR0CTWbcDHZw2QxE3aPs_2-01M08ri1bF0u07D2TtfCuBjgjhkY3k9ofM8ilbs1a9mBQbZWqcoek1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sxpmgQ0cROJdNl41ngrXOFs6UfBxWYSZUY3kNX0sj5RRUgHPJHeUtHH-7cCNwzD6ftlNWZ7BhQZyZt21aVBOC1TAR8szSFw6k5K5DrvlgyalGWrqz7xi5UA12PWymAdXNfb7XKc4Yoa2zHwJuq59a52l4qq1e2p2Ezg3NenmlBPqENQScDnT5LzrdKKG1U2gx-Bjhgn-g-qI_3xrUedTpCIHNxwwsZArPwrhYcsUEEdTYiLYnGBu2aWHf7DFi0-wkJ0TP1FoTbABcpF4kKirPl9OttHewhv-WTORYUm7I7X3V6seFv4h_isw3pxa1KMYp9XmwCeE6MEGWXeFDdnn5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hsrVhgRddsBs_yEsngoTVmpzwzjN4aiVqJJTEV48hJEobD0qjC2U9T_yJgCThaq6WtjlZvrfWi4jJnrm_aJMt5IxyLpDzqDc_bNtS0u9gFFgHa7dyr84-3n_Pq8yI1AcQG4ot_iFfHCQjXMFohzsSs8eHKMRHk1cfFReGBR2etfjj4t3GLPaGczmmHSoIygEqUkDhp4VvUHklXzpOUzt2yaylvZ--b3lI22t3ztWZH0PQmcyjXFkOeEUKaU5eAbft51Puvriw7g6cRcSTI18mL8s97JUCStpNeRSjRYNgqY5nE8rxRKSDfagDBkw0yP5pvBcFK5paR6ucbVPgmUdUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HYDmJurMSw3hYeXPcWcXMna90au5eXR1SHxFyqRS6esSQTAbFF8205-dJZ3QcgHXGwD-QMcQomjAMGNWiKfi33217i4Np67yP3ulliyjdzKYXnrAilDaKZA-kANqPUn7SY0UfMluMmk3IZ4lTZ5vR7FioGQdOqUybAFtp6GHL-s5FUahHJyvNZP4trGirXmAI9JKmycPEf3ZXqRqUQfHhKroRCY3CXSqYyFBKHGkaa-9rLM3Z_lYFnk2XWZE__hz7lqhP4F6nPUz12BMq8Xsi0trB1q124jbRolsaXs5JvoV4nwGGBZtdZ74bEgMujwWwt_82r2ieAoC-W2i6754Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4tvByEKm-l3BMrgUKEExfSV-ZN47zrR2J6ekfaBkjJKVtIDv3_qBZQ5heWO4xmAmaqSuRGtbxrgKrx8-jSHGjxtw1ppjqErsHVVGg8Qg_FMSs0etdnelnqV__hE2NiNurJwVTn5Q0X3GVqBSKXH1kHz4LA__SlR051i6A3E1HxAqXyA-80-ny2-v4pTjV1wdmfmLmWGdweLlPxnYTWX5-sXscOwtne4m-3coEHh7uKRGjCp9Nn0V6D-4-0mTiFfpkajdZJjOJEhMfC6haQnkueMZ8J3_Stl6rWAehZrIoH96vAVYORd23UWwX3ccUO-cezM9wChM6Q-o_znXSSyeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AY0hLBoK8FIw3BVP4em6kxTA1gnXGFm9T7tlQmRjjvVOksqCnjFEVrdVkBHSlnigCCWr1blHF3U6f5zZWhI6vaLXT4FtC3INr9DY4CcUjYISVPkcoiWG7QlXKZRJjGWEqb09FXdaN291ulUu0N0TVkacJoD2tJf_HcSz3MbwbgjCLZSHqTd3fMI3MINylLiXBCfELJ7l5JcKmPKjjFNyeOK3NIrNWEOgxi7hT1gVT59-OcKsvQRivlzGgJdba5fFNdSqEwRjZTMne8utbT_VQ9w5CCxFuRvk9bc3UNuxXQn478cwuhQ1wzRSRdQZoPHiyJB_SrHrYUw1gAEGTj0hbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر هوایی از حجم تخریب آتش‌سوزی‌های گسترده در ایالت واشنگتن
🔹
در پی وقوع سه آتش‌سوزی گسترده در شهرستان اسپوکن ایالت واشنگتن، تاکنون دست‌کم ۶۰ هزار نفر مجبور به ترک خانه‌های خود شده‌اند و صدها ساختمان نیز در آتش از بین رفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/677948" target="_blank">📅 10:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677947">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70ffcd59a9.mp4?token=Z5Zb268XMFNSwgO53sjC_3u-N7FxnptTsPXY_Cvfc1dxlsEXfsXjfZz8aVFb88crSrXgJ9ZWLAOPlanQ42kMoXThfE7WOY77yheLYclCQkujYy7f7Awl4EiRAvxavsnQzwSfvQy0sy2ZcjZ_iFf_5BUtKPvE2AkINzMO40j4IZ-Q6TXP7sOYEaPwE6_L7frpvYaYMg8lRzYCSjYVZV4-ywRHyFZDNRV0RVFXD0Oj1F8eYkL_bkVGcg8218bYwP6aNwenCzv1f3xWyYbcrbOvWCzD1PeIauQ-EZxqVjcY-cLVPcDGY0p6JaG1ZkEGphC4rP-JExREHIDWtWGvu1WyRoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70ffcd59a9.mp4?token=Z5Zb268XMFNSwgO53sjC_3u-N7FxnptTsPXY_Cvfc1dxlsEXfsXjfZz8aVFb88crSrXgJ9ZWLAOPlanQ42kMoXThfE7WOY77yheLYclCQkujYy7f7Awl4EiRAvxavsnQzwSfvQy0sy2ZcjZ_iFf_5BUtKPvE2AkINzMO40j4IZ-Q6TXP7sOYEaPwE6_L7frpvYaYMg8lRzYCSjYVZV4-ywRHyFZDNRV0RVFXD0Oj1F8eYkL_bkVGcg8218bYwP6aNwenCzv1f3xWyYbcrbOvWCzD1PeIauQ-EZxqVjcY-cLVPcDGY0p6JaG1ZkEGphC4rP-JExREHIDWtWGvu1WyRoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در بخشی از مسجد جامع اموی در دمشق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/677947" target="_blank">📅 10:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677946">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ni5e9YrzMx4As1orzGRYlvuDy-useBA9tqDXziM7eCrCwFM8vhfN6v1gvCxXpBMjHNawx-xFtNi4CtwUpONTjWammE-sEr3YoanTFin6fYakakV60Ar9X9jfgF5peEVVdPCovOisC5nm31MwWDfJW_k-Ag0ZXzgvHrPDWD0MZ4Mn732K35d-jPYVgBEDg8jW4-UXHJ_B833xdu2RL8AorJGXL2dsLhMwzA7Bdz1Hk6ENvDWwlVoh7Ld1_P2swJnAz5be9MOg5N0v2lowuSdVeMjWTCvf3eYMmXTHQUEib_TmBVYWqE_j_mZliHCicQ3bC3v7HnXya9XigYY19bVZzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به لطف هوش مصنوعی؛
خوک هار خودش را به قاب واشنگتن و لینکلن رساند؛ رؤیایی که با واقعیت فاصله دارد
#Devil
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/677946" target="_blank">📅 10:11 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
