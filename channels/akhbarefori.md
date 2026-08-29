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
<img src="https://cdn4.telesco.pe/file/Lym_dcOQXWsF_VmRN1_gihXvKoSBq_mwDQe0GkDvQevnF1oxcQurBQ6Wmu8wey00Ym0hH_6LlQT9d4LK_DewhnlPj_m85LgO_V7zcxj93fYEhR83A9YxvJmZJrsiXhnNQ1d56jASgwupaHCvKf6-F57xGRqC7X7OlnzFyDQn_9NL-Xx3l7hk7eI-ZGmkkMu4iyznv1h1RSGa8Asux5aP3v0e7NNp_s3ADvpu5l1Ud8UL_2u9pVMLK9mFJR4Tul8V-UVKRVYhRrv34oOYGH7cCmzQ5NA-4peqOo8-SyPrMno5PRKx32CvNXUZ91yBasYXVaDw0EddgHp0W19AIlIJfw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.38M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 01:20:26</div>
<hr>

<div class="tg-post" id="msg-685462">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d243bf411.mp4?token=LPSe8CiHGYo1cc5B8GFaCnXwqsEaK5kMUR0ep7PsicXJCbhqDB58q_dv2p9v795Ru8-5OdWGVXHo6O7FIsZRDeZAVSod7vfBNet7xbq8niM7JqlIgx_Q3c8TYVwBlRe3yjLvpudo-hkPsc7mr0ZPxeqP0uqbY74HTHT54J-phgCvFZA_c5mUsQx0mkgmLEYflnBgZkDp8Lj5BtBRwB13UB4I4c9q_xnc0i4cw3CSr9tuReCHastLgWQI-SzK7dq_pkSod6Cob5vy3n8qpbB2iNjEeIYtLYd__uNuIxlaK90RJ55w32L7InBjZXrjt8929c1j--5wIeXFzZ9QjnyGxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d243bf411.mp4?token=LPSe8CiHGYo1cc5B8GFaCnXwqsEaK5kMUR0ep7PsicXJCbhqDB58q_dv2p9v795Ru8-5OdWGVXHo6O7FIsZRDeZAVSod7vfBNet7xbq8niM7JqlIgx_Q3c8TYVwBlRe3yjLvpudo-hkPsc7mr0ZPxeqP0uqbY74HTHT54J-phgCvFZA_c5mUsQx0mkgmLEYflnBgZkDp8Lj5BtBRwB13UB4I4c9q_xnc0i4cw3CSr9tuReCHastLgWQI-SzK7dq_pkSod6Cob5vy3n8qpbB2iNjEeIYtLYd__uNuIxlaK90RJ55w32L7InBjZXrjt8929c1j--5wIeXFzZ9QjnyGxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده سابق کنگره آمریکا: ترامپ باید از والدین دانش آموزان مدرسه میناب عذرخواهی کند
🔹
ترامپ باید از من عذر بخواهد.
🔹
باید از آن خبرنگاری عذر بخواهد که صدایش کرد «خوک».
🔹
باید از آمریکا عذر بخواهد که وعده‌های انتخاباتی‌اش را زیر پا گذاشت.
🔹
باید از پدر و مادرهایی عذر بخواهد که روی مدرسه‌شان در ایران بمب ریخت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/akhbarefori/685462" target="_blank">📅 01:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685461">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
امارات گوش به حرف آمریکا؛ بازرسی از بانک مصری کلید خورد
🔹
بانک مرکزی امارات فقط ۹ ساعت پس از اقدام آمریکا در تحریم یک بانک مصری، از آغاز بازرسی از فعالیت شعبه بانک مصر در این کشور خبر داد.
🔹
وزارت خزانه‌داری آمریکا پیشتر مدعی شده شعبه امارات بانک مصر از ژانویه ۲۰۲۴ تا ژوئن ۲۰۲۶ حدود ۱.۸ میلیارد دلار تراکنش برای ۱۰۳ شرکت پردازش کرده که احتمال ارتباط آن‌ها با شبکه‌های مالی ایران وجود دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/akhbarefori/685461" target="_blank">📅 01:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685460">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
پرس تی‌وی به نقل از یک منبع امنیتی در ایران: افزایش قیمت بنزین در آمریکا شواهدی است که با ادعای آمریکا مبنی بر باز بودن مسیر جنوبی تنگه هرمز در تناقض است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/akhbarefori/685460" target="_blank">📅 01:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685458">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88955a0ff5.mp4?token=uPtXjWpruOUGD4G2UwsmW-SjS6GoXkTGtm22mfmyHSUkAiepRjb-DgdXzeEJHxABKqZ986B5XrNHnt78tLZM3Fv9i5n_FnKlOaU53lwJy1CN_ouIALzjZkplYIWntZbRBKGfhQgukkJvY-Lz6ipVspPplVXxUqSmqvaS3alksaQJWIXZfXXpvmT89FnPyzVXq2a6RLp3dF9YrIlQLY4r8fQG8fyLt5xVn3QmC8TZq_KPlQFQPlnItD3EwY7CWB4QWKklb3rRmgRhzgujqYjFGgWdRgkYMwucnFnhEpyfXgmJ4u21lm2xZxmmkbatMLEotoO_hh3yGMbxBujgXHHovg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88955a0ff5.mp4?token=uPtXjWpruOUGD4G2UwsmW-SjS6GoXkTGtm22mfmyHSUkAiepRjb-DgdXzeEJHxABKqZ986B5XrNHnt78tLZM3Fv9i5n_FnKlOaU53lwJy1CN_ouIALzjZkplYIWntZbRBKGfhQgukkJvY-Lz6ipVspPplVXxUqSmqvaS3alksaQJWIXZfXXpvmT89FnPyzVXq2a6RLp3dF9YrIlQLY4r8fQG8fyLt5xVn3QmC8TZq_KPlQFQPlnItD3EwY7CWB4QWKklb3rRmgRhzgujqYjFGgWdRgkYMwucnFnhEpyfXgmJ4u21lm2xZxmmkbatMLEotoO_hh3yGMbxBujgXHHovg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تظاهرات مردم فرانسه در حمایت از فلسطین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/akhbarefori/685458" target="_blank">📅 00:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685457">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
حمله لفظی پسر نتانیاهو به «بن‌گویر»
🔹
«یائیر نتانیاهو» پسر نخست وزیر رژیم صهیونیستی از ایتمار بن گویر، وزیر امنیت داخلی رژیم صهیونیستی انتقاد کرد.
🔹
او به طعنه در شبکه اجتماعی ایکس:‌ در دوره تو، پلیس کاملا به ابزاری برای اجرای دستور کار «کاپلان» تبدیل شد
🔹
کاپلان نام خیابانی است که اعتراضات علیه نتانیاهو به دلیل اصلاحات قضایی در آن شکل گرفت و جنبش اعتراضی، این نام را به خود گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/685457" target="_blank">📅 00:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685456">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54cb7f1f24.mp4?token=pIo2M1dRtYtYKG6VLge_l9f1p4030CX6YyWeAdlA3uHHfv9oqYnuO3WMJEJ5BSN-ddlxlG7N2GmD3ufDy4eKHop5MqgS5YnGrjaeMgmzuPdYvD8xzphR48SWTxrq35gS2hmacf6hgKcNwseS2CW2WeeesAHhtccGSyNKP_yONQ7hNcn3Sgwy6bxnddVF2uIPx-E9Ozla0rHOYGS1NtxIo8SZoVyUply2uwD0AMrqsnYq0D_dExjrZNERltA9UAEDXZsaGtRy3hzbZhxvzzNXt6mhiUhK6CrYuk43IomBeZfdVvJ4TQxvf72AdQFQMI6ZabRgrs878KNfPudOwruuIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54cb7f1f24.mp4?token=pIo2M1dRtYtYKG6VLge_l9f1p4030CX6YyWeAdlA3uHHfv9oqYnuO3WMJEJ5BSN-ddlxlG7N2GmD3ufDy4eKHop5MqgS5YnGrjaeMgmzuPdYvD8xzphR48SWTxrq35gS2hmacf6hgKcNwseS2CW2WeeesAHhtccGSyNKP_yONQ7hNcn3Sgwy6bxnddVF2uIPx-E9Ozla0rHOYGS1NtxIo8SZoVyUply2uwD0AMrqsnYq0D_dExjrZNERltA9UAEDXZsaGtRy3hzbZhxvzzNXt6mhiUhK6CrYuk43IomBeZfdVvJ4TQxvf72AdQFQMI6ZabRgrs878KNfPudOwruuIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نحوه عملکرد برف‌پاک‌کن‌های خودرو: توضیحی ساده از مکانیزم آن
#موشکافی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/685456" target="_blank">📅 00:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685455">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
تلاش عربستان برای اقدام نظامی آمریکا علیه یمن
🔹
شبکه اسرائیلی «کان» مدعی شد که عربستان تلاش کرد آمریکا را به اقدام نظامی علیه انصارالله در یمن متقاعد کند، اما واشنگتن درخواست ریاض را رد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/685455" target="_blank">📅 00:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685454">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
عزیزی: آمریکا با محاسبات اشتباه خود در باتلاقی خودساخته فرو رفت
رئیس کمیسیون امنیت ملی:
🔹
اقتدار ایران هیمنه آمریکا را در دنیا شکست.
🔹
آمریکا با محاسبات اشتباه خود در نبرد با ایران در باتلاقی خودساخته فرو رفتند.
🔹
مقاومت، شجاعت و ایستادگی مردم و نیروهای مسلح چنان درسی به دشمن داد که تا ابد فراموش نخواهد کرد.
🔹
این پیروزی با سه‌گانه ژئوپلتیک، میدان و نیروهای مسلح به دست آمد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/685454" target="_blank">📅 00:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685453">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ای نخ عبات رشته نجات</div>
  <div class="tg-doc-extra">حاج محمود کریمی</div>
</div>
<a href="https://t.me/akhbarefori/685453" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨️
ای نخ عبات رشته نجات
ای یم نگاهت معنی حیات
ای دم و صدات صدای قلب کائنات
🎙
حاج
#محمود_کریمی
میلاد
#حضرت_محمد
(ع)
💚
مرجع رسمی مولودی و مداحی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/685453" target="_blank">📅 00:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685449">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da12c27796.mp4?token=hU1lPfudrwQc78WZ32ymBGDkWFMlMSFiHJIL40_2ec9m7G6o2P7N6csV3LHDth7H8551CdgWJKlB6fkpkxc5dybtyqsl-kOJPgo5I4wwO4edfRp7DKhmx5s5JDdrRrSUxqYitT1MDC5O1DYZ2v3KMyk3KMQbO8E19DI7tMSRvpLOQLNf6r8wov-C4UaUt7YB9pOU4uoxZOz8ui0EHlWEWYiwZntv-QNCv8ip1WOFtY1wpE7EwS2dxyltx_kRH_a6OtwEjcb3VnC2gpaRE74yEFpVkdgTe3P79rfATzpFpZ8HzjkWqJ0jC-8-UH6t3_EdrZnYdaGw9PcVxiFaygizGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da12c27796.mp4?token=hU1lPfudrwQc78WZ32ymBGDkWFMlMSFiHJIL40_2ec9m7G6o2P7N6csV3LHDth7H8551CdgWJKlB6fkpkxc5dybtyqsl-kOJPgo5I4wwO4edfRp7DKhmx5s5JDdrRrSUxqYitT1MDC5O1DYZ2v3KMyk3KMQbO8E19DI7tMSRvpLOQLNf6r8wov-C4UaUt7YB9pOU4uoxZOz8ui0EHlWEWYiwZntv-QNCv8ip1WOFtY1wpE7EwS2dxyltx_kRH_a6OtwEjcb3VnC2gpaRE74yEFpVkdgTe3P79rfATzpFpZ8HzjkWqJ0jC-8-UH6t3_EdrZnYdaGw9PcVxiFaygizGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو‌هایی که در روزهای اخیر از مسابقات تنیس در باشگاه انقلاب در فضای مجازی پر بازدید شده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/685449" target="_blank">📅 00:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685448">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTtd5fpmscmqh8Qt2whaHjfi2DHRekrK2CmFFStEUvTw8Xvc6lUdNVR_BGGpauRa0n6SAhgDgIakN5fu5IGMruNVpZXsPDb8VczfU5KJ2nA73qn1NBgSy16zsjOmCrr6lZmp-YO8YAbZWmFtvatJ9W2II8IlFwYBM1J2OD31i6wcN6QAPVhwr5v0DWN_oulrvgCK6mkK7mIHK6EfFP5nNdFoTqW0qXwyBxmADkypBMQ3q2iE_OgDgIWk59hoBM3_dk-R8UNrzpFxWStclOJaERmmo2o_e-xySeG0AeudAE8jJQEviJi2MoMaXmOcHPG-nsTsDk8cXnTohbVP8Tnf6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش‌ها به پیام محسن نامجو به همسرش | آیا او به همسرش نگفته بود به ایران می‌رود؟ | نامجو یک هفته پیش از بازگشت ناپدید شده بود!
🔹
بازگشت ناگهانی محسن نامجو، خواننده و آهنگساز سرشناس به ایران پس از نزدیک به دو دهه مهاجرت، به یکی از داغ‌ترین سرخط‌های خبری و رسانه‌ای تبدیل شده است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3241385</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/685448" target="_blank">📅 00:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685447">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
هشدار احتمال وقوع سیل در شش استان کشور
🔹
سخنگوی سازمان مدیریت بحران کشور نسبت به احتمال وقوع سیل و آبگرفتگی معابر در شش استان کشور هشدار داد.
🔹
احتمال وقوع سیلاب و آبگرفتگی در استان های آذربایجان شرقی، آذربایجان غربی، اردبیل، گیلان و ارتفاعات شمالی استان های کردستان و زنجان طی روزهای یکشنبه و دوشنبه وجود دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/685447" target="_blank">📅 00:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685446">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f9410a23d.mp4?token=USB3jvAuxxfQes-OOCD5bQ-BLAGYe0miqiuy8Rg_Yx7nF78qDJ608KGGNc3cuV3zL8zbwHEVpAU0N8427LVZR205xwn4mNDwvW_bi0bYqOrbnZUw65s9hzuJ6dQMWzBqJOd6AkBTgd5T1WiUTCQ8M0u3gtJkxdru1pw7DcJPAv15KGE43iRM_o9M_iKmLrA-l3p1uNF0BGJnCwCIBVaEjUMCgGbO1hg5rEXRv7EUOWlc_H1PP6_xE1F-wRqxVWe6Tn3Cznj8MAnsh_izSt3DZs-kazGrnVWf148hKRHSVhDChPoJtRrNaAEZKXoQu6n8Vb_FOm-Mcxn5k3-hMQGQHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f9410a23d.mp4?token=USB3jvAuxxfQes-OOCD5bQ-BLAGYe0miqiuy8Rg_Yx7nF78qDJ608KGGNc3cuV3zL8zbwHEVpAU0N8427LVZR205xwn4mNDwvW_bi0bYqOrbnZUw65s9hzuJ6dQMWzBqJOd6AkBTgd5T1WiUTCQ8M0u3gtJkxdru1pw7DcJPAv15KGE43iRM_o9M_iKmLrA-l3p1uNF0BGJnCwCIBVaEjUMCgGbO1hg5rEXRv7EUOWlc_H1PP6_xE1F-wRqxVWe6Tn3Cznj8MAnsh_izSt3DZs-kazGrnVWf148hKRHSVhDChPoJtRrNaAEZKXoQu6n8Vb_FOm-Mcxn5k3-hMQGQHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تداوم حملات توپخانه‌ای صهیونیست‌ها به شهرک «المنصوری» در جنوب لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/akhbarefori/685446" target="_blank">📅 00:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685445">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9rM-aMf53MqavxpSFsZhvbh7JEBqVccOlUmsfw_QzmfQ9_bafVEwO4fEGbO7N0Reuqe-mk2upyLXUMhy8BWib6Fjjycn40Wegmu930Pxz_JO1rO_xsoZenc8x_89J7XOEABjx2W9VC6wnPrPMJ6S3uuQmJtepZlPpz3wD3QRpSUGkky-QUv-bncxn_O2WI0yAwmGeMj1UaSgrBhwgU13s0hYEZUIrq64b2eVsUi5LHlmsn-GWREKWWCysr9ois6kFM4fNRGqsUaRasHJdme1eaQPRDJC1_C6aqzw5HXMjB3rkhbmZjvFYUl1Fw-yu-OK30oMEfMEPxdRQrq87fwWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/685445" target="_blank">📅 00:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685444">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ هله یا ایها النبی</div>
  <div class="tg-doc-extra">حنیف طاهری</div>
</div>
<a href="https://t.me/akhbarefori/685444" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨️
تو معجزه ات قرآنه ولی
معجزه کردی با برادرت علی
اومدی که به همه بگی
ناد علی ناد علی سینجلی
🎙
#حنیف_طاهری
میلاد
#حضرت_محمد
(ع)
مرجع رسمی مولودی و مداحی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/685444" target="_blank">📅 23:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685443">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
حدادعادل: نباید مردم صبح جمعه بیدار شوند و ببینند بنزین گران شده است
🔹
پیش از اجرای هر طرحی، دولت باید پیوست وحدت و انسجام ملی داشته باشد و واکنش اجتماعی و احتمال سوءاستفاده دشمن در نظر گرفته شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/685443" target="_blank">📅 23:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685442">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6fe597b54.mp4?token=hAuWf1boxmzoLKvwB8JWBSRz4iVoo6sZA3VocC7KaVxPio7tKjmyGm9uvtNBjNwrAJHsKp0ICfltLivdRtuupCY9dPiEhUqeqxEcgaRrrc4jddjnmUzVIZlQtD5Z8mrBDU97atCVNc-jbIehbzlATWb6xpjSS37VDJvwfvM9MicptO37hk1s4siTUK2Ftr37oaHeKAedWdXetiV-VfDApH0qeDQXh7E1q15FT8HmPT7-eUHhjSrRrqjxXOR50IQSp6b0SamoBTyJ8hGuDni3iADAkAOSH88Ybs3Dr7eQN3QLlUQdROqG7IkyjuSeGgoBGWEE6vKKwfW5qhwx_Bk8wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6fe597b54.mp4?token=hAuWf1boxmzoLKvwB8JWBSRz4iVoo6sZA3VocC7KaVxPio7tKjmyGm9uvtNBjNwrAJHsKp0ICfltLivdRtuupCY9dPiEhUqeqxEcgaRrrc4jddjnmUzVIZlQtD5Z8mrBDU97atCVNc-jbIehbzlATWb6xpjSS37VDJvwfvM9MicptO37hk1s4siTUK2Ftr37oaHeKAedWdXetiV-VfDApH0qeDQXh7E1q15FT8HmPT7-eUHhjSrRrqjxXOR50IQSp6b0SamoBTyJ8hGuDni3iADAkAOSH88Ybs3Dr7eQN3QLlUQdROqG7IkyjuSeGgoBGWEE6vKKwfW5qhwx_Bk8wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تفسیر حدادعادل از پیام رهبر انقلاب درباره مذاکرات و خطاب به افرادی که قصد دارند مذاکرات را غلط جلوه دهند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/685442" target="_blank">📅 23:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685441">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
رسانه صهیونیستی: آمریکا حاضر نشد وارد درگیری با یمنی‌ها شود
🔹
شبکه کان اسرائیل گزارش داد که عربستان سعودی تلاش کرد تا آمریکا را برای رهبری کارزار نظامی علیه انصارالله یمن راضی کند، اما واشنگتن دستِ رد به سینه سعودی‌ها زد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/685441" target="_blank">📅 23:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685440">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
اصلاح سهمیه‌های کنکور به امسال نمی‌رسد
وزیر علوم:
🔹
اصلاح سهمیه‌های پذیرش دانشجو که از مهر ۱۴۰۳ در دستور کار دولت قرار گرفته، در کنکور ۱۴۰۵ اجرا نخواهد شد.
🔹
در نظام پذیرش دانشجو بیش از ۳۰ نوع سهمیه وجود دارد و طبق اعلام مشاور عالی وزیر بهداشت، در برخی سال‌ها سهمیه‌ای‌ها بیش از ۶۰ درصد پذیرفته‌شدگان را تشکیل داده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/685440" target="_blank">📅 23:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685439">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1340f65a8.mp4?token=Rj52YmYdJPiA9bPMJF_Toe9h3RQr9i5HXi2xjoBmK0jyK68pHjFZiZHaz_1QTjVx5sIy7oUT15gXYJP20mWyJYvr35h-xLp5lDoDN24_UrFRn15NKT8B7E5F81V-WmILtTXjulGgmASkbRlVbqmwqKTRr5bZjLJQD0M8ecsUOsfADxMDHEz6KP1WI9jPJ2c6I5g3kuyRq2BDDULaJg4TywMnN37K1f6jqF1qjN3R5SJNubWfeytlFXe49bl4IzJU1D4bNcRLbSdVlkVkeLzsFfXpwlsNiGXxxFdXlVJnNDdc3vqCPR2W3pJJqg353lLK5fTQHA0Ex7tEzrEdK-kYzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1340f65a8.mp4?token=Rj52YmYdJPiA9bPMJF_Toe9h3RQr9i5HXi2xjoBmK0jyK68pHjFZiZHaz_1QTjVx5sIy7oUT15gXYJP20mWyJYvr35h-xLp5lDoDN24_UrFRn15NKT8B7E5F81V-WmILtTXjulGgmASkbRlVbqmwqKTRr5bZjLJQD0M8ecsUOsfADxMDHEz6KP1WI9jPJ2c6I5g3kuyRq2BDDULaJg4TywMnN37K1f6jqF1qjN3R5SJNubWfeytlFXe49bl4IzJU1D4bNcRLbSdVlkVkeLzsFfXpwlsNiGXxxFdXlVJnNDdc3vqCPR2W3pJJqg353lLK5fTQHA0Ex7tEzrEdK-kYzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تفسیر حدادعادل از پیام رهبر انقلاب درباره مذاکرات و خطاب به افرادی که قصد دارند مذاکرات را غلط جلوه دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/685439" target="_blank">📅 23:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685438">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f8a45ff7e.mp4?token=sFfORJGC7ga02deNBs1SRiUB7T1qYWHuVzoKZnSUaPSClCP-wg6gOWTP2pqBIcrMeyipRHJ2J5c-N1vOXKbPS9XtxShjBPRrN1Zi3_KTRxzqqgDx-08Fo7GkG-HfhfMnDquklpH22623bMyAFQtzEPzxIL-z-NYBEkaBEWWn6Uwpnyq04Hr4446qgE5627pYEYhtx6VhZHpA5VJwUFQ9meObY-N06CQ7q7nwuj31BhYqKZB-uLIZMD6puG91ti12i3sLtxUFnqPL1LzrteQ85ftFWMzQPpAa-dR_onAdnksCi7oZmxApTmpKFWSN50IA5gWk7ORweGxisMPiaq_ETQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f8a45ff7e.mp4?token=sFfORJGC7ga02deNBs1SRiUB7T1qYWHuVzoKZnSUaPSClCP-wg6gOWTP2pqBIcrMeyipRHJ2J5c-N1vOXKbPS9XtxShjBPRrN1Zi3_KTRxzqqgDx-08Fo7GkG-HfhfMnDquklpH22623bMyAFQtzEPzxIL-z-NYBEkaBEWWn6Uwpnyq04Hr4446qgE5627pYEYhtx6VhZHpA5VJwUFQ9meObY-N06CQ7q7nwuj31BhYqKZB-uLIZMD6puG91ti12i3sLtxUFnqPL1LzrteQ85ftFWMzQPpAa-dR_onAdnksCi7oZmxApTmpKFWSN50IA5gWk7ORweGxisMPiaq_ETQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نجاتگران چینی در مناطق سیل‌زده نپال، هنگام جست‌وجوی بازماندگان گرفتار زیر گل‌ولای ناشی از سیلاب ناگهانی، با فریاد زدن «کسی آنجا هست؟» تلاش می‌کنند نشانه‌ای از افراد مفقود پیدا کنند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/685438" target="_blank">📅 23:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685437">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18c117eae.mp4?token=KcKGSbTj_xIrEY_x5tjZd5sYuainFaj6vt5CjEwuBmNLrtfwDbcTPnJYivTTs2fVRIYAtQRT0js-Z8nIln7aLPxoiIqvbBNdoNpkdTUThaPELNtOwRNZ4aFiog5w-XdswyH0Z0nNmJofNz6AKH98-C036XfMeZkanWV_eRwxd0fghOUrd30oGA3z04iIsxW9_mWaEtSrdNJcfO2DzNoYLtzovtfS-OEbpDPkOzAl2lezSgdWXu3qdmBRjWI66Bq0D75JXB2gqL6IHBinDz2Yobt8odTvwx57LF5GZVj_prUDllWlh17XJe8Zyfb-rTbfKQyAuwdAxLZBC_RKhYgDEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18c117eae.mp4?token=KcKGSbTj_xIrEY_x5tjZd5sYuainFaj6vt5CjEwuBmNLrtfwDbcTPnJYivTTs2fVRIYAtQRT0js-Z8nIln7aLPxoiIqvbBNdoNpkdTUThaPELNtOwRNZ4aFiog5w-XdswyH0Z0nNmJofNz6AKH98-C036XfMeZkanWV_eRwxd0fghOUrd30oGA3z04iIsxW9_mWaEtSrdNJcfO2DzNoYLtzovtfS-OEbpDPkOzAl2lezSgdWXu3qdmBRjWI66Bq0D75JXB2gqL6IHBinDz2Yobt8odTvwx57LF5GZVj_prUDllWlh17XJe8Zyfb-rTbfKQyAuwdAxLZBC_RKhYgDEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازیگران فیلم جواهری در قصر در گذر زمان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/685437" target="_blank">📅 23:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685428">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TiEHooVdzaBSQd0fSCso0-I6nXwypKiVWDYrVAj8IzDmmvqZBXQv5FXimtsiP5AJxUAxJs1DQt26WupkavlzAx4lrYS4lUfzfuWh55a01r94zeIYuaetxO1M02bT7FM9qN-r5xJ6zcxcNQx358_9dF7HTLObfePCphBVe2CEZIH4hPvfTG1Bs_nIi6MC7jyyp2kngUEUGTaGr-OpLWE7ZutQFu7lT4DD8Sqx1AvqlZ26DY4gMl3ozxPsMGIXDB6GxNKY8UsY_2mX1BGxcevHPSfSEV4TzAGWrSbR-CRlkNQo6f5eY9bJU5dlnJ5UI43mjPsS6dVxbEOwS5o3dILfyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gb_ElnHAYrcs-2B-dSUl9is2tC_CbdUhbtP9U9nt9YCuPveM2nxisV4VrF0OFGxqEBlUNNV05wgKpSMURertFJ3nHyjDnK6qu3dz7SMfPEjAqYAbKXWqQKZ1LrXbVkpeAyDKwQ7u0R1IljZH2-QCZdoq7mU3De9Qv-f4gUaQT6p0XmxckwmnvcrOcFHchllzWwd8N3xBTsoDTGPZptmhv6CZo7WKnPSblkQZQtvL_lg-v5Lf6BYhrPFlMMgqOkA45MuqmiISAzWUmPt2l6ttt1FSwA3N3uE3t4nUNB0uBD3yOYTCnM2bNgbVpdm8362DJypOfwqA_w2-3qexHpPfVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/neWtAqlUxFFshHYgr2dJIJlbERccRdjQLUZrG_C3H56cY6DvkCLFo-sVr_B4bkWN2HShSpL0OXK9K23jRjgzWRl6zlr4BKz7z0XXBO5AhPx-36-cbWWwaLZF1JK8nTspHoIed4jhhvYLuffYtMupBTipc9OPVs1eqg5dwYwLq1exyqAFbKjvlrH8Xkp3bhDzXRHfQoZn8d5OIIVUkIVYyUB6S4ab9ucYyhgSZeQlcjWl2VFeCRL3DdUc2da-OHz-E-fiJJfcRUkNRVg1ykxz5fufriq2VCemCrgDBIP_w94wNMJcmdUc2r13rR5kbDF5vEZmYteYNqGBdqd8ry2CPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HvatyUvAty7bk_1l1GqnhiuYqnobcpA1smsBgeQzvwiO05pOy75qUl3oWQm9jBWDCIILJ03h161G9ja_YAMfuSs3GYVimiZAnLMCQkPRjn7FCZi1NuPnSW1YGILOxPQf5diczC_g4pNDVrUn08TH5jE9vcIalXxTbJIm6lUDiRZLgTe5RQpUVh8k13uLZHDCgwbrM6JpWWKOraBj7TD8QcA6AaU3uYds-PaggU-dZmS7ZE7CqieGPQO_IytECgQzifJjCNJdjb9HdMzC7V3G0uvoBdGHukB61Pjg3kxOtZQus4OkURbYhAPSirEp5Inz8HC2cZNmuJFj2HS552WPuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KNElhP2g2V_w9YYq9eImPG48Xo7fth_S28J_K2vbspxnlhIBbtRIBQRiy8tH-E_NPb4mUnRa_-qUZJJARWox7hwZDPg0bWHsDaq7tBagQr4LWzMSTnh4FKs2YwxdECYRs_VifTJjccLqwsrshggnCIucgq0EobrQYHLkFhoQa4UaB_VtyECd3XvLY83ZIHHC80TEwGVQqPijkXAjKzEAmBSHgfY8lyGU8O8J2gAWzIGkVB6BOiPDPTrjIynewYJWkp39RurUlZAfhfeMzfAzQEa5dwmQmAYVzghZttT3ZhCWTL_HmRY2ptpfY8avSabKk3dVNfdJVnbzL-0HtV4pTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LRBL1ivHtYHw6-pLCzpHJ-925nBG4lex3aQgcRf4gekIErUldRe3bvrdI-Y23ZKqGR1I2JMqBwh2ZAKxgG9TyaByHDLyJyeA5eXIxG1ucWQIv_4wYmiedKDHPS0qb-iZg60GMrnENRGO-QF4HZHnuqKqUvWa0FPR0HgQN2ScfvPp4jdtGIlNxcAz0kKvbeM26uRIXL4HW7qrGGsx7U85jlJbW8qZSLP1tiBxnzrE7nRtkw4D8mnnRYyklcm_lgoR2jk5TGJrza7v7jjlECzo2Ew0aacslboHTs3hY4d9d2WT-PApw-89TabFbnROoT_kys-7JpyvvbTH74roe3iYlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nwP36kFLX0HxYDqgEdGKYQVrwF_KoTJUf-EbfFh3IoTUDKNZjGl-eSD5APMzS-osp4nkhJs4jFfsHKiSa2fCxT7UZM4AgSbb-gKtZBBs0EMrkQGOtNvMHg2urQSaejtGPWmfQu8-LaH3wiUmYOcZsSwWVSFxKoQOD9_Mm6tHUW1fXVFadg2YebZ7NyZU2yiQqgPxWI3TI8B7h2Ri6sWnwAAFwjM0DIilA93dCX2w37GsMTaJc8vurxTGaaQ1Awu7XAzGNX1huyTonDelW4MltoH97PYjWZu-3okopreMHtB0GoJ1ywrKMEk1D338y7tolo-hM3wQtCG71PRBViCaGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cad3UB_TO-4C4ZOzhyEgLcJqT9mKOkPlbBIfDLh8Dc_JGk5w9LHQ1D0SpEVOiwybpIIEA72d_o1oo22sRA0QBAfI-7DGnHfn66P9kAAYqbNeDSJj6CW24sPWPRiQ0wt-xP-sq7gU2mtejEZ-h7eeBHma3Q4VQci_43KBg_viYHfimBZQVa-0gyk6jayz9tGg80Q0o7T5_EGzwc2Rzozyw9c4dTWIu0sDG6-AMkJ-YGinkJqd3w-gAom0JHihwe9YW6pDrdql3X9s7Ot2ymIbewnDHeFmr7CUP5n4aMgYChztuftypEzYht34RffRgH5168DQGPORLk59ndfkiXluNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDVJ81Y3C1LUHCE2cMtX-X_e9uJ9ldsiVvuJCy2vkhmWRXzDqMO26SIcMNLmag7GZikpcfZBR1t8NHSR-nJpvKcL8EU7SGFEcRRihL6tVh25WjL5OQB8noGcZrS4zS3uCD9-oCuilgrJu90ZxFnnKeJ_Fsys14w_CpMofahxcgG8oXjacT0YGnrmymHwHWkjVKBTobwMyOvDCziIFgRKuGATx_4y7YifEMjI1ixnStUFVRNiZ3r7h0zbDq4nXV6Ikh71FYwnk5pjScWPjGBL0Ahllco5k3zpII2cw_F-aDicnz8rggEwpONcTNoy0qdHTEhV7Tsy9fy1KKa9OPuLzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
روایت بیماران از بحران تهیه دارو؛ سرگردانی در شهر برای یافتن نسخه‌هایی که بی‌پاسخ مانده‌اند.
🔸
الوفوری را دنبال کنید
👇
#درد_دارو
@Alo_fori</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/685428" target="_blank">📅 23:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685427">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
حملات صهیونیست‌ها به انبارهای دارویی غزه
🔹
در حملهٔ پهپادی امروز اسرائیل به انبار دارویی بیمارستان «شهداء الاقصی» در شهر دیرالبلح واقع در مرکز نوار غزه ۳ فلسطینی مجروح شدند.
🔹
در همین ارتباط، مدیر بیمارستان شهداء الاقصی از جامعه بین‌المللی خواست تا برای توقف حملات اشغالگران به مراکز درمانی در غزه مداخله کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/685427" target="_blank">📅 23:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685426">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🌹
دسترسی آسان به فایل‌های تصویری برنامه "زندگی پس از زندگی"
داستان افرادی که از مرگ برگشتند
#فصل_پنجم
🔹
اول
🔹
دوم
🔹
سوم
🔹
چهارم
🔹
پنجم
🔹
ششم
🔹
هفتم
🔹
هشتم
🔹
نهم
🔹
دهم
🔹
یازدهم
🔹
دوازدهم
🔹
سیزدهم
🔹
چهاردهم
🔹
پانزدهم
🔹
شانزدهم
🔹
هفدهم
🔹
هجدهم
🔹
نوزدهم
🔹
بیستم
🔹
بیست‌و‌یکم
🔹
بیست‌و‌دوم
🔹
بیست‌وچهارم
🔹
بیست‌و‌پنجم
🔹
بیست‌وششم
🔹
بیست‌وهفتم
🔹
بیست‌وهشتم
🔹
بیست‌ونهم
🔹
سی‌ام
🔹
سی‌ویکم
🔹
سی‌ودوم
#زندگی_پس_از_زندگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/685426" target="_blank">📅 23:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685425">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
پاسخ نیروهای مسلح به هر تهدیدی محکم‌تر از گذشته خواهد بود/ جزئیات عملکرد پدافند در جنگ ۴۰ روزه منتشر می‌شود
امیر زاهدی، فرمانده دانشگاه پدافند هوایی خاتم الانبیا:
🔹
نیروهای مسلح جمهوری اسلامی ایران در هر لحظه آماده هستند و پس از پایان موقت جنگ نیز آمادگی خود را حفظ کرده‌اند.
🔹
پاسخ نیروهای مسلح و ملت ایران به هرگونه تهدید، محکم‌تر از گذشته خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/685425" target="_blank">📅 23:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685424">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01cc087fc5.mp4?token=nlFPlEprMQB0MPBJCAPzzc95fklFAKco4o_skLhrq-t9U3Ra-eNEnWkSJ4eA8sQ_jSHNT9yg8itx3c0ziYBO5fGvSy9PtSmWpdrt_u2UrTr06qDAUhG1HIfPt-aTA6JivdhYH_4fzVbwm5m0TA-3DaCA3iLez2fxo1ucgH9pVvL_MMMAJApCqhKz3I8_aHOnJplCBTf1O3Gg0IBszBpTJe3AhAkgScwBjlHkkQ68snhIsnWzRG7MNzJBWSz2GO3i7z4REZ4BHiXr_M_w-mxnfFQbIvd0Mz2zfAEAk0vhG1CuBDVYVg-lqL3bk9MD8T8gdNg5-O3zsksoaXEbwbRgRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01cc087fc5.mp4?token=nlFPlEprMQB0MPBJCAPzzc95fklFAKco4o_skLhrq-t9U3Ra-eNEnWkSJ4eA8sQ_jSHNT9yg8itx3c0ziYBO5fGvSy9PtSmWpdrt_u2UrTr06qDAUhG1HIfPt-aTA6JivdhYH_4fzVbwm5m0TA-3DaCA3iLez2fxo1ucgH9pVvL_MMMAJApCqhKz3I8_aHOnJplCBTf1O3Gg0IBszBpTJe3AhAkgScwBjlHkkQ68snhIsnWzRG7MNzJBWSz2GO3i7z4REZ4BHiXr_M_w-mxnfFQbIvd0Mz2zfAEAk0vhG1CuBDVYVg-lqL3bk9MD8T8gdNg5-O3zsksoaXEbwbRgRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوشی‌ای که براى خيلی‌ها، اولين تجربه استفاده از گوشی هوشمند بود
🔹
گوشى Samsung Galaxy Gio از مدل‌های اقتصادی سامسونگ در اوايل دهه ۲۰۱۰ بود.
🔹
اين مدل براى خيلی‌ها يكى از اولين تجربه‌هاى استفاده از گوشی هوشمند محسوب می‌شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/685424" target="_blank">📅 23:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685419">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135e761d0d.mp4?token=u0Vn04oD_pkzj_NTi1n0ayQlVyGNtiHUnClTqdxrMBaaP80NVHjC18mYJm9nUODCRDv6bglixbaZ3mWYnxVfLaDn8aTH0z-JC_t6qTXUpcolYpFRppva97PfaZSDrVXqiuHopbrXvM-U0OWHWApddshQivsg3DUqIREmCbd7l_VGL_Db6N5fqsz0WNz7vVx4TSeTcXG_hiZGOC_PTMOkIOwRKKV9m6HGIJRlcWjeOKGEa8jxW-9wgRMBesskrl4QyCp8_a3nGkWS57cDg2FfuDzi9KB6IdKMBkv4ywK_9cHBHtQxw3W_p-OIgsDIHiJ4rbCYUbCsomowYx6U7gUWmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135e761d0d.mp4?token=u0Vn04oD_pkzj_NTi1n0ayQlVyGNtiHUnClTqdxrMBaaP80NVHjC18mYJm9nUODCRDv6bglixbaZ3mWYnxVfLaDn8aTH0z-JC_t6qTXUpcolYpFRppva97PfaZSDrVXqiuHopbrXvM-U0OWHWApddshQivsg3DUqIREmCbd7l_VGL_Db6N5fqsz0WNz7vVx4TSeTcXG_hiZGOC_PTMOkIOwRKKV9m6HGIJRlcWjeOKGEa8jxW-9wgRMBesskrl4QyCp8_a3nGkWS57cDg2FfuDzi9KB6IdKMBkv4ywK_9cHBHtQxw3W_p-OIgsDIHiJ4rbCYUbCsomowYx6U7gUWmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨️
هزار طایفه آمد و هزار مکتب رفت
و ماند شیعه که قال الامام صادق(ع) داشت
#پک_استوری
ویژه ولادت امام صادق (ع)
💚
@Heyate_gharar</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/685419" target="_blank">📅 23:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685417">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
غریب‌آبادی: ما با عمان بر سر ترتیبات عبور از تنگهٔ هرمز تفاهم کرده‌ایم اما تا زمانی‌که آمریکا به تعهداتش عمل نکند، تنگه باز نخواهد شد
🔹
ما همچنان به اقدامات خودمان برای دفاع ادامه خواهیم داد و برای هر سناریویی آماده‌ایم‌.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/685417" target="_blank">📅 23:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685415">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
غریب‌آبادی: عبور هر کشتی از تنگه هرمز با هماهنگی ایران انجام می‌شود
🔹
در خصوص تنگه هرمز، ترتیبات لازم با دولت عمان اتخاذ شده و مسئولیت اجرای الزامات بر عهده طرف مقابل است؛ هر زمان این تعهدات انجام شود، ایران اقدام لازم را انجام خواهد داد.
🔹
تنگه هرمز همچنان…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/685415" target="_blank">📅 22:55 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685414">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
مشاور امنیتی الزیدی: عراق برای رسیدن به توافق میان ایران و آمریکا تلاش می کند   قاسم  الاعرجی، مشاور امنیتی نخست وزیر عراق به الجزیره:
🔹
روابط خوبی با ایران و آمریکا داریم و تلاش می کنیم پلی برای ارتباط با هدف رسیدن به توافقی باشیم که حقوق تمام منطقه را…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/685414" target="_blank">📅 22:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685410">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pyftUbFW6ZoCU3RFfXR6cV510Iy6gldotvdcvvipmmIjNgnMC0f78gI6wacyV06rihtBrsQPPqvfqQajB5waJqfotZvCHUdTPpDUkR2sEd3QNxyYFZIFz5nIOySu51YqwWNP54fAFd3Qks92rW9VF6k63v1ycsZ85xbUxD6KBooi3OCSBygIzws-QGFYbvAZ-arUF7J7BX3bkQs22QTXoNpGB5IMTVfxH_uj64GeP-fVDZKvW8Ti4jchnWYiYJzSAhDyzpIfg4jYAAUN94-bD_HOU0dSoM-3IZy6T-1NvexAaLQOnQP07jJeTLKlQ1fhqhcAebygJQvFrw5yjLiDEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jp7eIDQ7VY41GRTwkpMkhXwiyhctiIW79C_ZAEUvZHtQnjZckTQZL6QjSFyeErDJZdD4yr5sAq0B1SPKqZZ7QlJD5J-iSMU5eWmLVQ2nJScp4m9Nr18AUI76nWYF1sO2Xs0E-RDyPPWfZmDPAXOvBfE9slGlpSdy8y_obigBC7l0gLu6QSYTXX_MqU2eTAaQbCnPDAEkdZi6ZhacE6H62Zfe0W3W1EGwP0h-sYQGpca0TaqXjwqzE-y7-6HS7qD_yf4v-9kOG3tu-zNXawmuPF6fHgZNuxGFJBadtANOn7XvbGrMjAXklkaws6wWl1UlUYGgRMaRIAgo_BDAEW7a4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U5dTMTenLhSmVEbHuwxTLi4SVzKV4o8mhBx15lFlqWD_5UI09wpcRci_1QtjHsYvTPWTSYp3hbrxn79fuZG2HhEMBRog6ANo-YCqkEarWw3VvN8vIC6-adsVZaP4LZSQmKVFOcLxpX7ySOBOSL9tNnfK892PbbnROLmjLfqJuaLhwJjt1hppNWGXMSCJczi9OyKSPzfMEaeOsDhreQlbAoLPtv_6IQeE1sl07Nnx4XMVkDnqsYYKkpWG0Gof0GNOkGArOOoEA7X61RSAOEPFsLIU5Pw50CriMcEhfpGieYTg4kzLXfsxdEWdQMiwkpd6DTz_CVcA1b0kD6BHt-xVNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ep4T7v8qIbsOtc-yQCEo-LWF8-LpE9vdMufB9Ol_IpHc3oEu6qU9IRyeZuODty5S6QyLjvRII4fJiYIz1U870l23Bg3Cf4KYzdzjaOjg31Nouaif1Ti6SMfF-mRIKejPzh2zZVkustox5D7Xz-eHfj9klwpGH2IH7oLWsVhfWydT_ucn4nA_D9Qo7Qxu0QjIrfc52yn4g1gzQ4HjYVfgBbEA1thwpIKMhUetuK6GEHz6XNsZAKtonD-oFI9e5sUlFppUlUoCo4HNsLejSecnqbJ27wgAHk3nXsC4NnusbQiyLGXvHcSGyjb9MXTSO1bgzlcJKbsT4lTmqKZtW937Iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨️
دوای درد دین و درد دنیا ، درد بی دردی
حضورت دردهای مرگ را حتی طبابت کرد
▫️
#والپیپر
به مناسبت میلاد حضرت محمد (ص)
💚
دریافت فایل تصاویر
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/685410" target="_blank">📅 22:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685409">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
غریب آبادی: ایران برای بازگشایی تنگه هرمز تعجیل ندارد/ تفاهم تنگه هرمز با عمان وارد مرحله اجرا نمی‌شود مگر با انجام تعهدات آمریکا
🔹
جمهوری اسلامی ایران با عمان درباره ترتیبات عبور از تنگه هرمز به تفاهم رسیده است، اما این تفاهم به‌صورت خودکار وارد مرحله اجرایی…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/685409" target="_blank">📅 22:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685408">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55c81e867b.mp4?token=tLB6gWNIb6L8w5YjUVJlk_AHHfo56MxMl7MgDUFp7IWF4cyzcdChr5N7ccG_hQ1Yv8oyjcK1rBMdwVpJ8eKObFFyhTXutMY5lv6TP0pbLUioGkfKeoJ0a4s52PJWIcbSq171Vw7lxFIi2M5lQyciKXZhOGjaf1peDB3CmaAGe0_FR9QxEJkNro2lcodAmRwWJDamVIJOsFum_BDfifKlI8XTx4LaeEsiWD6Z8V1MSU7PzDWis_Pxj2X-5e21FeoJAj-ahGKIz4ICsFdstlMFxiUf_10AiVHEDHpHDKKDLQUnoafOQsgSE-FoJfuAQkA8o39bvAP0EBX7agX8t07R3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55c81e867b.mp4?token=tLB6gWNIb6L8w5YjUVJlk_AHHfo56MxMl7MgDUFp7IWF4cyzcdChr5N7ccG_hQ1Yv8oyjcK1rBMdwVpJ8eKObFFyhTXutMY5lv6TP0pbLUioGkfKeoJ0a4s52PJWIcbSq171Vw7lxFIi2M5lQyciKXZhOGjaf1peDB3CmaAGe0_FR9QxEJkNro2lcodAmRwWJDamVIJOsFum_BDfifKlI8XTx4LaeEsiWD6Z8V1MSU7PzDWis_Pxj2X-5e21FeoJAj-ahGKIz4ICsFdstlMFxiUf_10AiVHEDHpHDKKDLQUnoafOQsgSE-FoJfuAQkA8o39bvAP0EBX7agX8t07R3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی عجیب از درگیری چند دختر باهم؛ گفته شده این درگیری مربوط به دعوا برای یک پسر بوده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/685408" target="_blank">📅 22:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685407">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
پشت پرده گرانی‌ کالاها با وجود افزایش تولیدات در کشور، چیست؟
وزیر جهاد کشاورزی:
🔹
هیچ مرغ آلوده‌ای در کشور توزیع  نشده است
🔹
اقدامات ترامپ و جنگ با ایران سبب افزایش قیمت جهانی برخی کالاها شده است و در این میان برای ایران آنچه که بیشتر از سایر کشورها افزایش یافته است، قیمت حمل و نقل است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/685407" target="_blank">📅 22:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685406">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
مشاور امنیتی الزیدی: عراق برای رسیدن به توافق میان ایران و آمریکا تلاش می کند
قاسم  الاعرجی، مشاور امنیتی نخست وزیر عراق به الجزیره:
🔹
روابط خوبی با ایران و آمریکا داریم و تلاش می کنیم پلی برای ارتباط با هدف رسیدن به توافقی باشیم که حقوق تمام منطقه را تضمین می کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/685406" target="_blank">📅 22:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685405">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-poll">
<h4>📊 برای سلامتی همه شیعیان امیرالمؤمنین علی(ع)چند صلوات هدیه به محضر پیامبر اکرم(ص) و امام صادق(ع) می‌فرستید</h4>
<ul>
<li>✓ ۵ صلوات</li>
<li>✓ ۱۴ صلوات</li>
<li>✓ ۱۱۰ صلوات</li>
<li>✓ ۱۴ هزار صلوات</li>
</ul>
</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/685405" target="_blank">📅 22:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685404">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ایران دلار را از کجا می‌آورد؟
الجزیره:
🔹
با وجود تحریم‌ها، ایران از مسیرهایی مثل فروش نفت به چین، دریافت یوان، صادرات غیرنفتی، صرافی‌ها و واسطه‌ها، تجارت با کشورهای همسایه، حواله، طلا، ارز دیجیتال و تهاتر به ارزش دلاری دسترسی پیدا می‌کند.
🔹
چین خریدار اصلی نفت ایران است و بخش زیادی از معاملات با یوان انجام می‌شود؛ سپس شبکه‌های واسطه‌ای این درآمد را به ارزهایی مثل دلار و درهم تبدیل می‌کنند.
🔹
عراق و افغانستان نیز از مسیرهای ورود دلار نقدی به منطقه هستند. در کنار آن، صادرات پتروشیمی، فولاد و محصولات کشاورزی میلیاردها دلار درآمد ارزی ایجاد می‌کند.
🔹
در نتیجه، تحریم‌ها ایران را از دلار جدا نکرده‌اند؛ بلکه مسیر دسترسی ایران به دلار و ارزش دلاری را پیچیده‌تر و غیرمستقیم‌تر کرده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/685404" target="_blank">📅 22:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685403">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
غریب‌آبادی: ایران آماده حرکت در مسیر تقویت وحدت و همکاری با کشورهای اسلامی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/685403" target="_blank">📅 22:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685402">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
وزیر جهاد کشاورزی: ایران در شرایط سخت جنگی، برای اولین بار در تولید گوشت مرغ خودکفا شده است و به سمت صادرات آن در حرکت هستیم
🔹
تولید گوشت قرمز نیز افزایش یافته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/685402" target="_blank">📅 22:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685401">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
غریب‌آبادی: ایران آماده حرکت در مسیر تقویت وحدت و همکاری با کشورهای اسلامی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/685401" target="_blank">📅 22:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685397">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">السلام علیک یا رسول الله</div>
  <div class="tg-doc-extra">ماهر زین</div>
</div>
<a href="https://t.me/akhbarefori/685397" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨
به پایش ریختند از نور‌ها آن قدر از بالا
که سینه ریز خورشید این وسط ناچیز مثقال است
#پک_مولودی
ویژه ولادت حضرت محمد (ص)
مرجع رسمی مولودی و مداحی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/685397" target="_blank">📅 22:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685396">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d2d0487e0.mp4?token=Rmp5d2woqEcgAIa4P-ZN-A40QjZDD2hyYsbL7ioeTxrxwKry7HQoliLeh7QvYUBFzG9Y0sJCX-EOjbwgaFVdI4xhf5aer5PzDjvPEAOrp5npHIW31KoOj_iQMWbCRuRhKC4oHj4fz8b7O_mNEDSMNME7ypdX2yl8QEjjWB4HNVohgdoxv3il4J452C9z0tqoTvkLI7KzMXqJLp5zxWKnYXkvAhMTxMS9PLO9-EYzBm8PLjwXtDAvmJbTdJ0JRErBV21e60nGSdTceQwkhIwQF7Wvg5RtNlycoRq6--MvXeNiOHgYcYQud5iOQCo1xYymAcTLtA-eIUxzBoDiaS9Llw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d2d0487e0.mp4?token=Rmp5d2woqEcgAIa4P-ZN-A40QjZDD2hyYsbL7ioeTxrxwKry7HQoliLeh7QvYUBFzG9Y0sJCX-EOjbwgaFVdI4xhf5aer5PzDjvPEAOrp5npHIW31KoOj_iQMWbCRuRhKC4oHj4fz8b7O_mNEDSMNME7ypdX2yl8QEjjWB4HNVohgdoxv3il4J452C9z0tqoTvkLI7KzMXqJLp5zxWKnYXkvAhMTxMS9PLO9-EYzBm8PLjwXtDAvmJbTdJ0JRErBV21e60nGSdTceQwkhIwQF7Wvg5RtNlycoRq6--MvXeNiOHgYcYQud5iOQCo1xYymAcTLtA-eIUxzBoDiaS9Llw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایان زندگی هرکس مرگ اوست، جز مرد حق که مرگ وی آغاز دفتر است
🔹
دست‌نوشتۀ سپهبد موسوی فرمانده شهید ستاد کل نیروهای مسلح
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/685396" target="_blank">📅 22:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685395">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXEKAptPPKkdsvVd3798tkBIi3DDMoF0eYi9qo4zQ0pEd3oMc-4lcMs5gtqFYzAiHOhSbXIVxUWSdprCBcbiTU2Bivh6GwTRY9lUFS9Z_la901gerv15DDzwhNoou8Wud0uXo_BOeCv9XdPsoZlQzIs0A81HErK9Kwu-8SvKtOYSEseOpkjOFBH8bXvB6yUfvm2D67BqBKOPhmm6azeU1Pbb-moVL3mNK1TlhKSQ8Mwwt-AhGDiZv8xClyXFwJTbkDLHxXiIHn1uRpjZvA-KL6B2pOEtuKhlG_lpz9DP69P3cnVejMrnmhn1Eoe3drLe8eXJZLCdNeJklzajef2gKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایالات متحده تهدید کرده است: با حاکمیت بریتانیا بر جزایر فاکلند مخالفت خواهد کرد اگر انگلستان هزینه های دفاعی خود را به ۵ درصد از تولید ناخالص داخلی خود برای ناتو افزایش ندهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/685395" target="_blank">📅 22:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685394">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMo-f0I_HiYVvZ7UIS5z9YKiY5GQGNwWZH8bIDuVdLFW8FLx3179rc24hYYxFfgEyhm1oHeu7xv3L83Gcae9X___9kwD7klXqUQ8jv39gaYYCjI2Cd_EGX9F0koH_1SqskP2nPJ6mOAFJsts-C75TqrBwpgwYeGaejL9kKIUk_5aH5Aj8szEtw77JuHe-aQ2X5cn233o7CnGk862Yq0ncl_T4Zs4UAR_WWBcYdQk6QpzFzPxqEFPkVEfO6w4qC2suwTYfstYSCj0FzNSEGUS3KubKo74Yd6R-miGvQnQptpecIdflIl8KHp-6LthHs7JURKckuKq8fOAjbI6Yg2QFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نماینده مجلس: بدهی تراستی‌ها باید دلاری تسویه شود، نه ریالی
🔹
رحیم زارع، عضو کمیسیون برنامه و بودجه مجلس، گفته بدهی تراستی‌هایی که پول حاصل از فروش نفت را بازنگردانده‌اند باید به ارز و با نرخ روز تسویه شود و تبدیل آن به بدهی ریالی قابل قبول نیست.
🔹
وی یادآور شد: در سال ۱۳۹۶ نرخ دلار نزدیک به چهار هزار تومان بود؛ یعنی یک میلیارد دلار حدود چهار هزار میلیارد تومان می‌شد، اما این مبلغ تاکنون تسویه نشده و با احتساب نرخ ارز به رقمی بالغ بر ۲۰۰ هزار میلیارد تومان رسیده است. یعنی ارزش این ثروت حدود ۵۰ برابر افزایش پیدا کرده است.
🔹
این عضو کمیسیون برنامه و بودجه مجلس بیان کرد: دولت باید بدهی خود از تراستی‌ها را به نرخ روز ارز بگیرد، نه اینکه معادل ریالی آن را دریافت کند. اینکه دولت بگوید معادل ریالی ارز را از تراستی‌ها می‌گیرد، درست نیست و اقدامی اشتباه است./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/685394" target="_blank">📅 22:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685393">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVzSlGDWFYIyw6sL_60hHcl3DkW3tC75KOtO7LVNWtFi6mG9nTSMOxSwyb5NWzdP5oDzsP1DTpf0wdPrf6qxZudowaRTmjmmACGtHdceadzJz60URmIJdkng7w_VTn5FoUTxj8HbvqQT7tt486FxkR3tER84-bIx059nht71XuCl2vPJ33a7o6aSu9pIlbxKfGQdorbGq5aSyrOLz54oEHTVfJpX5872MdXZ7mst0tSUR9FJ7CFEP7NzUZL58eVK_DuslWxoHt1UFFamtknNqsLHGZuNXqwzpcICE1dpMYKB-GECMx2G6Wgwuj59GIe8h2dCv7d62IQBWvg5z7i5Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شیفت دفاعی ایران آغاز شد/ استراتژی جدید ایران در مقابله با آمریکا: درگیری مستقیم، حفظ سایه ترس و دیپلماسی با همسایگان
🔹
اکنون، ایران در سال‌های ۲۰۲۵ و ۲۰۲۶ در دو جنگ دیگر شرکت کرده است و درس‌های جدیدی را علاوه بر درس‌های قدیمی فرا می‌گیرد. واشنگتن باید به این درس‌ها توجه زیادی داشته باشد، زیرا آنها استراتژی ایران را برای سال‌های آینده شکل خواهند داد.
ترجمه گزارش پایگاه The Dispatch را در وبسایت خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3241350</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/685393" target="_blank">📅 22:06 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685392">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef7f9f7d3.mp4?token=DOsnoMkBaLNEOjxqNe7zYsfp2j1Xg-FjEPmzjQqFcdFJSS4tM_chynt-NemYGqr1w3QpGBvMgyIHMY5D0YiYq8w2LY4Hzi_In8oPg5ZxVgP1nzlhRk5u1Fsv2AC4eD4HI7ZkIy95pkAbxJBdR1H4GYIJB8VtnMYQrTCwnxav9f1cDTgj4s1H44aVuFOA5PixXryovQirSlLjyga_ZbOg3EpTvvrS6Y2HppnnPDtjdQCsOpgci6ssVcrWs6XnPcoKdxHxoVrH2jk-srOPEHCP938Z51IiMDgOyrmdY8WLbPjlr3_tsO_ZWU0aRiQDBMYgpxo9VSJkUDZ8MCRFKHDm9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef7f9f7d3.mp4?token=DOsnoMkBaLNEOjxqNe7zYsfp2j1Xg-FjEPmzjQqFcdFJSS4tM_chynt-NemYGqr1w3QpGBvMgyIHMY5D0YiYq8w2LY4Hzi_In8oPg5ZxVgP1nzlhRk5u1Fsv2AC4eD4HI7ZkIy95pkAbxJBdR1H4GYIJB8VtnMYQrTCwnxav9f1cDTgj4s1H44aVuFOA5PixXryovQirSlLjyga_ZbOg3EpTvvrS6Y2HppnnPDtjdQCsOpgci6ssVcrWs6XnPcoKdxHxoVrH2jk-srOPEHCP938Z51IiMDgOyrmdY8WLbPjlr3_tsO_ZWU0aRiQDBMYgpxo9VSJkUDZ8MCRFKHDm9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلویزیون دولتی روسیه نحوه نابود کردن بریتانیا با بمب اتم را بررسی کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/685392" target="_blank">📅 22:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685391">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkEEUC2RFvXoKqH3mum7TWKO1ghhbEWfpVzu80q_BgfcKnO-9wm4P4XBkM6Fn3mVxUAmBhS_hBlXTbnNyPOl-SDJHEytKYfQXew29dbEGcc75QiO46SEIIE5tlKQx79Pdnj44p0HdrAlRTv1ijHLuFIL91t4xhm33tXdntr6_L6vvWAAtVEb-rp7h5ppusuGdOISsomj-JBBQxixPc6Vi2e6jlLV73qlLtc8Ce86oxnIincjQkdSE7Xahc5zHNtVoug8pxi9mRpqZn4VvwiXW7ObkDOKo4g_WwtUU8Qr0S76khCwIr2FtoykRrs4PSdHjqr6a0uYb6i652DP-dDiuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صبر، فقط تحمل سختی‌ها نیست؛ انتخابی آگاهانه برای رسیدن به چیزی‌ست که ارزش انتظار کشیدن دارد
🔹
امام علی(ع) در نهج‌البلاغه می‌فرماید که صبر دو گونه است؛ صبر بر آنچه ناخوشایند است و صبر در برابر آنچه انسان دوست دارد. گاهی باید برای عبور از سختی‌ها صبور بود…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/685391" target="_blank">📅 22:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685390">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
اروپا علیه شبکه‌های اجتماعی برای کودکان؛ اسلواکی هم وارد میدان شد
🔹
دولت اسلواکی در ۲۶ اوت طرحی را تصویب کرد که بر اساس آن استفاده کودکان زیر ۱۶ سال از شبکه‌های اجتماعی ممنوع خواهد شد؛ این طرح نیازمند تصویب پارلمان است و شامل سازوکارهای احراز سن می‌شود.
🔹
نیوزیلند نیز همین هفته طرح ممنوعیت استفاده افراد زیر ۱۶ سال را مطرح کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/685390" target="_blank">📅 21:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685389">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a4eecac98.mp4?token=RWOBphbVAb--yM10jqmFXdkJ5CiJbsi1td_NGKBi6dWUlGoqBsETGRVH2HWCHTbTzLtdnG04QYVskAKxRDSIBPubvvj2qv3cCybVFjDSDHS3KRJxgqCn-tGFK8UJyivLSZ6HbIfHJpck8de2P6ybno5iQ-JePkppC030ly_PEP42RwrGs59ZbOtrwSG8vV7gl2SLrkABZxTjzIkUcAIkpit6Ge0ROaRvnvuvJzMzjytzWuApsUDSB3nvduZaToY7xI0MjScHNT0uf_ohHwwG_ZkaTuA61XW9drU4eF-gKru84UwWbZSTt1JZOkDu3Qo1bIzQ5AxXdKRF0y4nEBKJIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a4eecac98.mp4?token=RWOBphbVAb--yM10jqmFXdkJ5CiJbsi1td_NGKBi6dWUlGoqBsETGRVH2HWCHTbTzLtdnG04QYVskAKxRDSIBPubvvj2qv3cCybVFjDSDHS3KRJxgqCn-tGFK8UJyivLSZ6HbIfHJpck8de2P6ybno5iQ-JePkppC030ly_PEP42RwrGs59ZbOtrwSG8vV7gl2SLrkABZxTjzIkUcAIkpit6Ge0ROaRvnvuvJzMzjytzWuApsUDSB3nvduZaToY7xI0MjScHNT0uf_ohHwwG_ZkaTuA61XW9drU4eF-gKru84UwWbZSTt1JZOkDu3Qo1bIzQ5AxXdKRF0y4nEBKJIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
اگر عاشقی کنی و جوانی
عشق محمد بس است و آل محمد
اینستاگرام هیئت قرار را دنبال کنید
👇🏻
👇🏻
https://www.instagram.com/heyate_ghararr?igsi=YXZnNWZhaHRycTlm</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/685389" target="_blank">📅 21:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685388">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992b33ce12.mp4?token=QQG27vifPhN8cVZ-lue3CMu_oh8xnq4t4zXJs1HuqM0pGXMwFeyvaKXBpsffQeyll1OD_Z7NHsFxGPNEjB1GJCCZmXoZD9HHtNmPUUQpCF43_TmsT1DghmhPuvjzDA1mSIJ0abbc5SjUkb6kOq7r0756NUiIBGYWN_VCR-iftbxfEL-no9zKW1hp2dF9klpQRVeLUURIe8bSnvi3Kygy68V1MZkOvcJaBI_k3DHSIDCnAVcYNoukq7H8UnrRfCGy628VjfF9uy2QFrcWbfQbvHaJaWjAIqBG6it0SKKO0nJQcmFyYImVaF3exmQrEb1WpWbVEAvnYPkCv0kzXaX2xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992b33ce12.mp4?token=QQG27vifPhN8cVZ-lue3CMu_oh8xnq4t4zXJs1HuqM0pGXMwFeyvaKXBpsffQeyll1OD_Z7NHsFxGPNEjB1GJCCZmXoZD9HHtNmPUUQpCF43_TmsT1DghmhPuvjzDA1mSIJ0abbc5SjUkb6kOq7r0756NUiIBGYWN_VCR-iftbxfEL-no9zKW1hp2dF9klpQRVeLUURIe8bSnvi3Kygy68V1MZkOvcJaBI_k3DHSIDCnAVcYNoukq7H8UnrRfCGy628VjfF9uy2QFrcWbfQbvHaJaWjAIqBG6it0SKKO0nJQcmFyYImVaF3exmQrEb1WpWbVEAvnYPkCv0kzXaX2xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر کشور: تفاهم‌نامه اسلام‌آباد بهترین توافق تاریخ معاصر بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/685388" target="_blank">📅 21:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685387">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR2e0ipjQAMpv6XERjYQ3ccJ13pVcjQ4ZvEEJHjlGeinD29VE5iio2yW-h_lvM8UCw2DUtJiGm1iJ0tqn5D24u4i-4g0opXzCMuAhh9e0mxfG4_a-Dd-XzRrGHI_wkPHgdE4gHtL-iPpklS9OtBvcEYTklitdBwy7CI-iB9LwRO6topXLc6ywI6aOMT7eJpWYK4oOW1kzsKYdJuXATNLHXtbd5IfuR2Au82ClJ06mHlhcljdXEiEIdzND8IN78Gi_eva87ETwvBEp1qGH909GbxrAML4Y8d_q3N9pkjF_2GtR2QJ6E4xzGpVAsx4g1T6S5-CqquEACr9O8zIuH45hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام رهبر انقلاب اسلامی به مناسبت هفته وحدت صبح فردا مصادف با میلاد باسعادت پیامبر اکرم(ص) و امام صادق(ع) همزمان با قرائت در اختتامیه کنفرانس بین‌المللی وحدت اسلامی، منتشر خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/685387" target="_blank">📅 21:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685386">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvAhpo5E83TPGmVfbsUg8yOHLbXp7Q8Yhfzkv_7a003fln-gwEVq0NXbCdhOpXBUUsWWBwPFPBAZDaDsfK1-B7Akmy0HTTGaMStmIAsW2_DtcGPqn5gBJJRpgvU36YigfqbG5E69_3RXGmDcuu1MP9jbK_hWxKJakJXgTXhdKQ6BeLW2K2iCknIJmUtCsh9OCShkj9hdxdzG8DLtL_pzLBiwtusNCnPclhFyuO4c-oZc-skychiQnCJYbWovrJ8Kcy2d0bPYICd9xDo2smfP_dnHwXyJxMkZwxQUMOuxHC22hcZUyXwCRabBHq_ACTAw07j9z4q7gluCUNlILv5JEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرسپولیس قبل از دربی درخشید/ بازگشت شاگردان تارتار به تنظیمات کارخانه
🔹
تیم‌های فوتبال پرسپولیس و ملوان در هفته چهارم لیگ برتر امروز شنبه ۷ شهریور و از ساعت ۱۹:۱۵ با قضاوت سید رضا مهدوی در ورزشگاه شهدای شهرقدس رو در روی هم قرار گرفتند که این بازی با نتیجه…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/685386" target="_blank">📅 21:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685385">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4StMquAmCDj4ik6lzjiTNJmzq94T1LSGYjoLDXPuautC4h7m0EpKF1gTk4IwMgi8g3T4HTCVfGoQIfPZYW9BmIyp5Hofa-cQNy0yTrN2FMWQx4SLgImkhm_k4yCYWexxCeP0NfNFbGUIQ-ZWGR1AOolaFx5saFS9ulhfEx4O_w9uFbYlXElrD6QoDe1_RxVXSnH8DFApWYYsAmWGDuRT8SwchTIoOnks-ZIaJzX9lSMCGvRKhR4xAXS5IxeeYXI0vAWj_TWrev3_hIzm9S7WrgRxiHJyXJ4681siHcuvth7iTzq5Yi962HWnhs6XMOhhB3S5hUl7itU4xO13C57uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ریچارد ژئوپلیتیک و سیاسی: خودکشی یک هژمون
🔹
جنگ ایران به عنوان یکی از بزرگ‌ترین اشتباهات راهبردی آمریکا ثبت خواهد شد. آنچه به عنوان تلاشی برای نمایش قدرت ایالات متحده آغاز شد، در عوض محدودیت‌های آن را آشکار کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/685385" target="_blank">📅 21:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685384">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bx2Unt0f2zKnWA4TRPqszE3vptIFJvmEfnhzLQho3FiYQika0i0rN-YY_rJ6WFzJPxERvRtmd1xP8wztgXRujrdoE1u3dtOr0M01A0gkMdLGbEKhDO_Ow1PWxnKTAh58NZTq_dd6Q5xgfWgFuyjW94UEIND6JK9DX_3Cc_uQCV90YJhrLv6OlAeXCxDmaja3yTu-JV_cILEGELVh68SmAapPXooAAHcxo5Ves-mDiAo95ASWwr0PmXqcaswJC3eLGswPVhZIxA_gEsa97cknF8pkziL_KbsZ4Ek3jjZlL6jEAuuI97gw9bBjj2rSP47vdM1vuHX92xagOcmg9sW_NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای
باراک راوید: دو مقام اسرائیلی می‌گویند ابتکار بستن تنگه هرمز از سردار علیرضا تنگسیری، فرمانده وقت نیروی دریایی سپاه پاسداران، بود
🔹
در ۷۲ ساعت نخست جنگ، ایران اعلام کرد که تنگه هرمز را می‌بندد و هشدار داد که نفتکش‌ها و کشتی‌هایی را که تلاش کنند از تنگه عبور کنند، هدف قرار خواهد داد.
🔹
اما به گفته مقام‌های اسرائیلی و آمریکایی، سردار تنگسیری در پشت صحنه دستور استقرار مین‌های دریایی در «طرح جداسازی ترافیک» (TSS)، یعنی مسیر اصلی بین‌المللی کشتیرانی در تنگه هرمز را صادر کرد که وضعیت را به‌شدت تشدید کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/685384" target="_blank">📅 21:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685383">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
دولینگو (معروفترین برنامه آموزش زبان) اعلام کرد آزمون‌های این برنامه از ۱ سپتامبر (۱۰ شهریور) برای تمام ایرانی‌ها متوقف خواهد شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/685383" target="_blank">📅 21:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685381">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESw1tpLYlmNfRfvosPMSn-2p_D2g7il38U3XGx9liSrQPd3kp79JQtXoPHVFRTYdDjPset4VUn-6drJbVktITDRmwUo5roB4Itrde16qsKpV-32ySmVJBA6VTWXMPUfEkBfYS-qsTAVkOKIEAPno0Hxr8iCFMxVscPVFTE7SNGsiUpJ6hb3p0ohWwZFJcaggGPtFG3SQjVeyfrez88le9qoQa1k2rDr7NdXvLtFYzYn-L88ViH497SA1AFPmXecsKldIwzalakgHre8O4WjC37P37QrIhyix9e9bZ9VDuKj65kWyWXzLVYok-FnfTGyGgQunj-cxDw6-8oEFitUjvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل سوم پرسپولیس به ملوان توسط علی علیپور ۵۶
🔹
پرسپولیس ۳_۰ ملوان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/685381" target="_blank">📅 21:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685376">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RZMl1xtxyL2xcv2bd_sFvDmzON7GJNwACNXKNVdbq37bGageln2plwJhYNn6soRgdLmwMvv9vyNym3kjlxDvjtnJN_qDHT9ocdB4KPFlpbtxrAIfG1gzRCJ5Eqm1EE_0zM4MfZS-e9bFpeYshuneiIODfY7j4XJR3gbmGoup5bO_n6WB_nIkMBe1KRZWkNfyxetD_D0ENwMf6cZSy3PrawAk5mkfKYVW1Ao5O1q6UYhBXNJcAOxjdXtBeUUUJuQY3zDsWmKeI_IykN-k7kuxEqc4D2NCvOh_CuOcH7KyaB3nNVfbUzZNqwRnXbLILhtyI_9dUBePgL7XPbKOUkMCDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CLtvjI4PllOQ596NKKcgCKyZFmHtWRGOC6QF9-kcfoMVxdnNwvhKxdUEsLAtcqjDe8-sn2CyOuE41TCZNcczasbGZoRXkOzsu6e1GIuR4QR88XnTB0RizaM4jHwyFNcHxHSewXXVuZSfIEz5JUlwwPlAnJKLaf5zyrdk2jH44arb5Wd5Wie54iZQUAKsO5d6aFBU78IvTcimyHI_EA7EeQjqESoC9tNu1C3UVQ3Yuc4etePSHYeOrrNCtnP9b1WNmzYDOZD_kfjFqSteHnAtwwSg631AJlL981VBMi7DfsPDnPwsPBursj2RZimVx2PDKdx7bYEjCV7T9RvfgC_k9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دیگه با کپ کات یا اینشات ویدیوها رو ادیت نکن، چون هوش مصنوعی واست اینکارو انجام می‌ده #هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/685376" target="_blank">📅 21:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685374">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHQ6RWuemk9tUlDgcpGaruaRruPlvPnTk6-qtbznUfXxOJZ4Qx5STpsdTY--4vRXLEeIBIugfx7SgJDrwnPnEVYagBDxRlTYt0ENCsXrMx6vwuhShbDzEtAK1vylEZ3zsSIxohFowVf3JwBWrmoNjvY1CmoCRbUvB5WpLuXkyh_wm7SOKNlMR0Tn6tyru8k9PF2tEwD9meNwJGmOXKjO_M-dGTa2w5v5yZLZFPdoDAIFH3d-jZ9r9KmPW75lZTltQz3MdBcw1NaP5KbhF7wTHWlrNrA_H0-YrYZtjT8JSEQl2I_hOpwzx8sOGcmelo8ovGSvR_uIR3A5UIZRcXFg-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ایران قوی، ایران علمی
💠
اعطای بورسیه تحصیلی و صنعتی دانشگاه بين‌المللی امام رضا علیه‌السلام به داوطلبان سال ۱۴۰۵
🔹
ویژه داوطلبان کارشناسی ارشد مهندسی برق
🔹
ثبت نام تا تاریخ ۱۵ شهریورماه ۱۴۰۵
🔰
جهت کسب اطلاعات بیشتر در مورد شرایط و نحوه دریافت بورسیه با شماره‌های زیر تماس بگیرید
👇
☎️
05138041 داخلی‌های 1421 و 3108
🌐
imamreza.ac.ir
🆔
@publiciriu</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/685374" target="_blank">📅 21:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685372">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VG-dgo1jKl3xYwjG7l5DhU51jTXUi-qCiTWdvz_qz8VCmp6HJwE46OyR5T2t-wMv8o1CFYIZi9mPl2p3ycoODdZnImhjvg_z-70bUX8mtzjz8eNSULvmXFclAs01SmOuI_pPd4CdqZLB2piRzNB6LFHZDd9rk-DgwGkjdyNPWy6DcskiK-KKbQ2Gf82oo8jnl0hEARdKl7sjW9EdQDYWmJU_EjZkTR1ghm8FlGqhiRbJXbjvnmpH-pVOnF6nAhYqZGB7IlN6A06yTfp-oiL6nLtxs0aNVA2NNr5pYmzeJvxv5kIJSK20fY9uqRIXY8v6zlPqnBIa8THA73Z4xPyEBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بخشودگی ۱۰۰٪ جریمه بیمه شخص ثالث!
📢
طبق اعلام بیمه مرکزی،
از ۲ تا ۱۳ شهریور ۱۴۰۵
✅
تمام جرایم دیرکرد وسایل نقلیه فاقد بیمه، به‌طور کامل بخشیده می‌شود!
فقط کافیه در این بازه زمانی، بیمه‌تون رو تمدید کنید.
✔️
تا 2میلیون تومان تخفیف با کد
pnsc
👈
تمدید بیمه شخص ثالث
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/685372" target="_blank">📅 21:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685371">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257f5fdf48.mp4?token=CXvsOkHAKkb9ZPeDj_f3FJYB8_TpOVg0INzLNCMCxHyycDYb7whZyx4y9aYPvUsWUZPM_KbszAMzeN7EbW4d-8Oqf--es2w_grG1Av3h19IJ7oBkTiq5IqCtUNLgpYY_EmG7xyIzIHLZqtpAfDkcBnaxifWzFPno6lXcw6PIN-Kc4wo29n9LBym0-USAXnRvXFVQ1KEHCn_POxUF79AUffMCvX_XBsy8xCKWxIBHhrfvJ-C1J80baNR9gDXjV8kOxFD2aiSe5KFM3OfQnVeUHDyo4b-NjzTFI489Ek3_IBoGZVolGG4rrzarjJcSVIsqBW9E73CG2pmHvRDlj4F0VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257f5fdf48.mp4?token=CXvsOkHAKkb9ZPeDj_f3FJYB8_TpOVg0INzLNCMCxHyycDYb7whZyx4y9aYPvUsWUZPM_KbszAMzeN7EbW4d-8Oqf--es2w_grG1Av3h19IJ7oBkTiq5IqCtUNLgpYY_EmG7xyIzIHLZqtpAfDkcBnaxifWzFPno6lXcw6PIN-Kc4wo29n9LBym0-USAXnRvXFVQ1KEHCn_POxUF79AUffMCvX_XBsy8xCKWxIBHhrfvJ-C1J80baNR9gDXjV8kOxFD2aiSe5KFM3OfQnVeUHDyo4b-NjzTFI489Ek3_IBoGZVolGG4rrzarjJcSVIsqBW9E73CG2pmHvRDlj4F0VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان سرخ در حمص
🔹
طوفان و گرد و غبار قدرتمندی آسمان و اطراف شهر حمص را در سوریه سرخ کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/685371" target="_blank">📅 20:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685370">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/276adae82c.mp4?token=j46kau0oT3EXbrft7Favh5r-679BC_ebzRqFcQYtuYIhEQ74_GAoHSZx9HZwlkoYEwbuA086Rq6oGw9wOuqJAvqMz3OoBgYVXoBIn_sxI7shnZ8od34lUBL6elJufh99YCPpZDUlO_GixITq1rjlYpwmnUPLoEMq8X5X7u2DBpdrcCk2zjby6dkiZYXbHncyjPx2jFb7Xm47qCpCSmFWcxUuZj3QPoNFaeRRGSgoRlrvCabVs0goxE7LE3r-Z_D4qZlfI3eEM9Mnb3M-PIhmBDmSiRIPPFBvimIQp0cuWWqZ4O4aPXSeqxqwR40xFzdITQeAFBArb2pObf30R9JKiahB9EdxQ5Npc1jMl-kQUt_dXqMt1TRB6sr9lvRhBXd8xaZjKabbU7xhRoDbmcEoYV2NaX4hxejx9l2WGee0973l-DatZQRajDIHesCWoxMuKjF9KNbQZDejl91KKM_2rXW-0DMwhZUBY_PAizF0pvE_Iuw6QLlySvhMreMf7zrH4SyADkgFocPdokvSbcsMffgsMP28tVeFPin6OBcDXysH-Gqj6p7XGDeGr_8eTtzH8ootVs9mlI10zykZ17R1eRRdU0mXvhoFoEFt2YjNg0MesuKlBUs_T1IyiLG1ArhspIxAwPy115PcJodDE2KDudHB5Z455Wa7DM_3zbg7sVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/276adae82c.mp4?token=j46kau0oT3EXbrft7Favh5r-679BC_ebzRqFcQYtuYIhEQ74_GAoHSZx9HZwlkoYEwbuA086Rq6oGw9wOuqJAvqMz3OoBgYVXoBIn_sxI7shnZ8od34lUBL6elJufh99YCPpZDUlO_GixITq1rjlYpwmnUPLoEMq8X5X7u2DBpdrcCk2zjby6dkiZYXbHncyjPx2jFb7Xm47qCpCSmFWcxUuZj3QPoNFaeRRGSgoRlrvCabVs0goxE7LE3r-Z_D4qZlfI3eEM9Mnb3M-PIhmBDmSiRIPPFBvimIQp0cuWWqZ4O4aPXSeqxqwR40xFzdITQeAFBArb2pObf30R9JKiahB9EdxQ5Npc1jMl-kQUt_dXqMt1TRB6sr9lvRhBXd8xaZjKabbU7xhRoDbmcEoYV2NaX4hxejx9l2WGee0973l-DatZQRajDIHesCWoxMuKjF9KNbQZDejl91KKM_2rXW-0DMwhZUBY_PAizF0pvE_Iuw6QLlySvhMreMf7zrH4SyADkgFocPdokvSbcsMffgsMP28tVeFPin6OBcDXysH-Gqj6p7XGDeGr_8eTtzH8ootVs9mlI10zykZ17R1eRRdU0mXvhoFoEFt2YjNg0MesuKlBUs_T1IyiLG1ArhspIxAwPy115PcJodDE2KDudHB5Z455Wa7DM_3zbg7sVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وحدت؛ توصیهٔ رهبر شهید که رنگ عمل گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/685370" target="_blank">📅 20:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685369">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVFb4Ik943PXeBYb-WpK0v7ZPbENwk1loVRWNFSae-Zl215fehymGOeCEmfPUmO_AvUVVwTBphP1FoDyY9J0UA-oNBkK7gyrjMjrKu_X3Zi-gO2ffqQnLMegYQ4EcxYQaC8VIE0zR4hLItEcd6yKDUAWwZ4VhC_CMdMUucA4XFSn3hON_-EBHw5fAPXdODV9-T3QvG7wpktd1rDXTNul4XNSUssdZAPsaeC91fktqesHNHeQuEw-2kyFf4V5FkDdW6Qbk9Ml4JcaqCRBBJGDfaXh99jisnWKBxWROe7jg4rTQYrdchPGeVz4LvSr-KzPKRmJaMHvvJn6JEncXnDtmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری این‌بار از نزدیک با شماست
✨
🔹
بیست‌ونهمین نمایشگاه بین‌المللی الکامپ، فرصتی برای دیدار، گفت‌وگو و همراهی با تازه‌ترین جریان‌های فناوری و تجارت الکترونیک.
🔹
در غرفه خبرفوری منتظر حضورتان هستیم...
سالن ۶، غرفه ۳۲
۹ تا ۱۲ شهریور
ساعت ۸ تا ۱۵
نمایشگاه بین‌المللی تهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/685369" target="_blank">📅 20:55 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685368">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ef114bf55.mp4?token=qDiIOysZWtfM3TyNxLfCAMzmM7QeEpoukCypE2zhke3dPbLqjMc2PLAzHB5Lyvezt4DGds3hVQiahjK6F8CmxR8wDQAUlS07C9C8YzqYIB6QiHu1E6OtWdxU0S3in_J2SedkF-k5_8S5ms6BgoUHLfCdDgsgK0g1YwbgGGX_U3P__Roq8ZQC4nOex9Kl-6Z8JRUs9_nN8409LKDKwRy1m67cvbnoqj7SLzvKln6AaOokoyLUzTyWGH_TMF6Sy3MsTBWnAOkWGfaSo-PdwQVqriKsnfVMVhYgVVIm0IgivEO82o3IdtLH2TNc8d9mi6i5qmhgyUigHgfnFgi7PA5Vaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ef114bf55.mp4?token=qDiIOysZWtfM3TyNxLfCAMzmM7QeEpoukCypE2zhke3dPbLqjMc2PLAzHB5Lyvezt4DGds3hVQiahjK6F8CmxR8wDQAUlS07C9C8YzqYIB6QiHu1E6OtWdxU0S3in_J2SedkF-k5_8S5ms6BgoUHLfCdDgsgK0g1YwbgGGX_U3P__Roq8ZQC4nOex9Kl-6Z8JRUs9_nN8409LKDKwRy1m67cvbnoqj7SLzvKln6AaOokoyLUzTyWGH_TMF6Sy3MsTBWnAOkWGfaSo-PdwQVqriKsnfVMVhYgVVIm0IgivEO82o3IdtLH2TNc8d9mi6i5qmhgyUigHgfnFgi7PA5Vaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم: حالا فقط یک اقیانوس کم دارم!
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/685368" target="_blank">📅 20:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685367">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e809ca549.mp4?token=DH3ptzF5SO4WT7AVHh7kDNkgrXfv53bLnqFgypWRaJAYAsPNuwWWcHMSZCYzZwPtE_mpZVJkAwyWu4PNl3oVHPenNukZUwZcwM9o5i1nJm1wnYELdC54Hm7oioj8Q1XjuTJKo7-jMm_DbT4AvCGA71Wrm3jD0j8_Xnhz5Xk_Puv1HZdTFaClB8jkZ_mdH-iOHJFWorcKxW7856U4pkVJrj8jRDDD2w6LQYlbKuv6jCN-HS9XJdA7FcnHtiify4r_lmnNx09WjGXro6Ho93K9DsTH-LTqesg2HIDY3akEEXx-Wuak4Ug_5QWePc0JEzToY3ZZHl451QxvoKbmzrLuF41shyP3yq8OpM4BVnBT998-qfMdJg8B9jCSa5HfR6esPTkDshXKJYUE4oybe2gsIHBqACURun0jkEo3tlgZxF8f5CPCJeTva6aFrQrJkDc3sewKCmWWByJX1h_IeIVlzvX2gPGD7h9XvJEtOp-cKwUBGB_Ru7rodxVL6afeYVl0m_9cj_mtQBJffv2_dy77UzyTdgY4iTEInLZloKJmbXdbo4T3cf6s7K4YstaGXIkuN7UV34EVx3Au-cf2e3002UVpUnnqLb6cK-lorseilBTXohDnNasgyCM8Kgu9Toath0jKXmDNGDzRm24CtAMg_-3i7oUjKFi-0rEb8LEI2PM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e809ca549.mp4?token=DH3ptzF5SO4WT7AVHh7kDNkgrXfv53bLnqFgypWRaJAYAsPNuwWWcHMSZCYzZwPtE_mpZVJkAwyWu4PNl3oVHPenNukZUwZcwM9o5i1nJm1wnYELdC54Hm7oioj8Q1XjuTJKo7-jMm_DbT4AvCGA71Wrm3jD0j8_Xnhz5Xk_Puv1HZdTFaClB8jkZ_mdH-iOHJFWorcKxW7856U4pkVJrj8jRDDD2w6LQYlbKuv6jCN-HS9XJdA7FcnHtiify4r_lmnNx09WjGXro6Ho93K9DsTH-LTqesg2HIDY3akEEXx-Wuak4Ug_5QWePc0JEzToY3ZZHl451QxvoKbmzrLuF41shyP3yq8OpM4BVnBT998-qfMdJg8B9jCSa5HfR6esPTkDshXKJYUE4oybe2gsIHBqACURun0jkEo3tlgZxF8f5CPCJeTva6aFrQrJkDc3sewKCmWWByJX1h_IeIVlzvX2gPGD7h9XvJEtOp-cKwUBGB_Ru7rodxVL6afeYVl0m_9cj_mtQBJffv2_dy77UzyTdgY4iTEInLZloKJmbXdbo4T3cf6s7K4YstaGXIkuN7UV34EVx3Au-cf2e3002UVpUnnqLb6cK-lorseilBTXohDnNasgyCM8Kgu9Toath0jKXmDNGDzRm24CtAMg_-3i7oUjKFi-0rEb8LEI2PM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم پرسپولیس به ملوان توسط علی علیپور ۵۶
🔹
پرسپولیس ۳_۰ ملوان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/685367" target="_blank">📅 20:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685365">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2512adc8b.mp4?token=kG-f_H5hxBfTeQpL2UFncNKyicPd93JrW0uDcDeF9Z9YEJ9bD44L250wSUE1Wrbd_L_uNPQLa_cmIiEuOV7IWYDZqDQ5-NZJpo2ph02NP3ScaULgML8T-9A3nC3mWdyYzNKCxoaz0rPRTFtkHg8GHvNLGJcEVTG7bNQ_sZxeZTjWBmi_qtwONbQlAqZXMH8xnhx18uSryq42aRN3EVm5jjuqR5Tl1v7E2-zDP9A4wEe0fllFg9sTr_GIu2Am_zi5QVhhCN0m7AVcMHTg0K7lhg285y-_zTbtPIuYTQNG7_peprnK73OZTnDFVowe1kWtEsZ2tpiCvbfa9SN6R3eMow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2512adc8b.mp4?token=kG-f_H5hxBfTeQpL2UFncNKyicPd93JrW0uDcDeF9Z9YEJ9bD44L250wSUE1Wrbd_L_uNPQLa_cmIiEuOV7IWYDZqDQ5-NZJpo2ph02NP3ScaULgML8T-9A3nC3mWdyYzNKCxoaz0rPRTFtkHg8GHvNLGJcEVTG7bNQ_sZxeZTjWBmi_qtwONbQlAqZXMH8xnhx18uSryq42aRN3EVm5jjuqR5Tl1v7E2-zDP9A4wEe0fllFg9sTr_GIu2Am_zi5QVhhCN0m7AVcMHTg0K7lhg285y-_zTbtPIuYTQNG7_peprnK73OZTnDFVowe1kWtEsZ2tpiCvbfa9SN6R3eMow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تکرار نقض چندبار اسرائیل این بار
با
حملۀ رژیم صهیونیستی به یک مرکز نگهداری سالمندان در لبنان
رسانه‌های لبنان:
🔹
رژیم اشغالگر اسرائیل یک مرکز مراقبت از سالمندان در شهر حولا واقع در جنوب لبنان را منفجر کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/685365" target="_blank">📅 20:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685364">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
منابع آگاه به روزنامه «الاخبار» وابسته به حزب‌الله گفته‌اند که نبیه بری، رئیس پارلمان لبنان، اعلام کرده است از جوزف عون، رئیس‌جمهور، و رودولف هیکل، فرمانده ارتش، تضمین‌های روشنی دریافت کرده که بر اساس آن‌ها ارتش لبنان هیچ قصدی برای تسلیم شدن در برابر هیچ‌گونه فشاری ندارد و ایده رویارویی با حزب‌الله در دستور کار نیست
🔹
گزارش شده است که بری و عون روی توافق اروپا و آمریکا برای حفظ یک نیروی بین‌المللی، حتی اگر صرفاً نمادین باشد، حساب می‌کنند تا بر اوضاع جنوب نظارت کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/685364" target="_blank">📅 20:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685363">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80057e224b.mp4?token=XcCN9L7n8onutt5ZcrRDQqBjOS_8njLU0YdPA15-BPFJUY_d6hJCpbrvpXUyRMNgMGL4LjoOgVP2NFlGTMHADIVFJxdwDRwzW8Z4DmWVYErf8M9gTNSJx7s3s78QOfPQKmzFmKb7GHKip5-bHaVoxaj2sHoWs9legssXZ00lEB51WULbFNF0NPQsVSy4CXZ6M_jDNh-ZScg7eaM5gVxv0utZHJ4araMdylk54MRnBReCcB0ZYBTP3NusLlAGdhLNLy0V4jyUD2Mosx-BNXwB3tWq174DCQqBWvTgGrpQBtpBCVB6DTYEXDMKiJbrw6_VipGLJpPVTWOPzF6ahUyuGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80057e224b.mp4?token=XcCN9L7n8onutt5ZcrRDQqBjOS_8njLU0YdPA15-BPFJUY_d6hJCpbrvpXUyRMNgMGL4LjoOgVP2NFlGTMHADIVFJxdwDRwzW8Z4DmWVYErf8M9gTNSJx7s3s78QOfPQKmzFmKb7GHKip5-bHaVoxaj2sHoWs9legssXZ00lEB51WULbFNF0NPQsVSy4CXZ6M_jDNh-ZScg7eaM5gVxv0utZHJ4araMdylk54MRnBReCcB0ZYBTP3NusLlAGdhLNLy0V4jyUD2Mosx-BNXwB3tWq174DCQqBWvTgGrpQBtpBCVB6DTYEXDMKiJbrw6_VipGLJpPVTWOPzF6ahUyuGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم پرسپولیس به ملوان توسط تیوی بیفوما
🔹
پرسپولیس ۲ _ ۰ ملوان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/685363" target="_blank">📅 20:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685361">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
سازندهٔ چت‌جی‌پی‌تی شمشیر را برای ماسک از رو بست
رویترز:
🔹
اپن‌ای‌آی قصد دارد ارائه مدل‌های هوش مصنوعی خود به «کرسیِر»، ابزار برنامه‌نویسی مبتنی بر هوش مصنوعی که اکنون تحت مالکیت اسپیس‌ایکس قرار دارد، متوقف کند.
🔹
تصمیمی که بار دیگر اختلاف طولانی‌مدت میان ایلان ماسک و مدیران اپن‌ای‌آی را به کانون توجهات بازگردانده است.
🔹
این شرکت دلیل تصمیم خود را نگرانی دربارهٔ نحوهٔ استفادهٔ اسپیس‌ایکس از فناوری‌های اپن‌ای‌آی و تجربهٔ قبلی از نقض مفاد قرارداد توسط برخی شرکت‌های متعلق به ماسک عنوان کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/685361" target="_blank">📅 20:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685360">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53e66bb35c.mp4?token=k0BHE4gTO-VFH8B5pwglo7NBXazUSUa3k6Fq39Y_7AS2yP44zdZpf-fjN3HA9r0LrJzGA5oIgMiG1dv643UZd4Iv3snxHi7ertulJjOXjMiKa5soM0ljtZpntIXbKxYjSyMw6vPuk8gpI0XgbWSSFdjxmO2SsisYdkfai2HSG8eTXhRHetp5Zw-M6ZxvBulDLVECM_1CLY_cNDHtY9RcOYkOVB_rVqL2xOyq52UL2J3SVUaslOu4TEf-RY-gVnWV_HsskqBBm_lAYErbS_3zjUltepxRXbYL4ssZkjuL0m13flAUxiSVBXSJ_2Px7LFaF4pClWbLc8RjLdUpWDtkfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53e66bb35c.mp4?token=k0BHE4gTO-VFH8B5pwglo7NBXazUSUa3k6Fq39Y_7AS2yP44zdZpf-fjN3HA9r0LrJzGA5oIgMiG1dv643UZd4Iv3snxHi7ertulJjOXjMiKa5soM0ljtZpntIXbKxYjSyMw6vPuk8gpI0XgbWSSFdjxmO2SsisYdkfai2HSG8eTXhRHetp5Zw-M6ZxvBulDLVECM_1CLY_cNDHtY9RcOYkOVB_rVqL2xOyq52UL2J3SVUaslOu4TEf-RY-gVnWV_HsskqBBm_lAYErbS_3zjUltepxRXbYL4ssZkjuL0m13flAUxiSVBXSJ_2Px7LFaF4pClWbLc8RjLdUpWDtkfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر بالگرد چینی از سرچشمه سیلاب مرگبار در مرز چین و نپال
🔹
یک بالگرد چینی خود را به نقطه‌ای رساند که در آن یک یخچال طبیعی فروپاشیده و حجم عظیمی از آب آزاد شده بود.
🔹
این پدیده که به آن GLOF (سیلاب ناشی از طغیان دریاچه یخچالی) گفته می‌شود، یکی از خطرناک‌ترین…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/685360" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685359">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTLeGbHucf1R0a4hAoU2qRdP7f3FeTzZCtX27qA8UfViTiIRH2HvZHzAsmEebA5wgI_SC-dAPbb3yx6Mo294Q4iPTuwf7YN8dBkJfNRYlvWH7y1LHL3XzYPyZ_l8u9IZOTG3AugQ5Dm9tRs_6pfYqBO9nT-Q7FqWsXDILcv1EXg72ZL27T4eUapINH5syyJ1qsOn7s8dkrhPbTqOCP4DjIFIaCW8LbMFpnCxVVJvAKj9_vge3gAw5Qbk1nBd6wnOrI1rIP_tVY2iGPf4S5K3uporoRF0V0scbYnfXlX_dfHJcrtCPIVQbvAOZbWIUxYB6EEB48AE2GlsKL4KZMoo8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روغن، رکورددار تورم نقطه به نقطه مرداد ماه ۱۴۰۵
🔸
بررسی آمارهای تورم نقطه به نقطه کشور در مرداد ۱۴۰۵ نشان می‌دهد که اقلام خوراکی و پروتئینی بیشترین جهش قیمت را نسبت به سال قبل تجربه کرده‌اند.
🔸
در این میان، گروه «روغن‌ها و چربی‌ها» با ثبت تورم ۲۵۸.۲ درصدی در صدر رکوردداران گرانی قرار گرفته و بیشترین فشار قیمتی را به سفره خانوارها وارد کرده است.
🔸
پس از آن، گروه «شیر، پنیر و تخم‌مرغ» با ۱۶۳.۷ درصد و «دخانیات» با ۱۶۰.۹ درصد در رتبه‌های بعدی بیشترین افزایش قیمت جای دارند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/685359" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685358">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4508efc7.mp4?token=QGC4VKL5p2bchAdtDPlYwXABbNZGPw0FLSbv9euMyukYGv3Kf0UtviGZTQOg00Jis9qPCAQLCas00FJ-8eY0uydN_x2oRd3xM0E-Qg8N80Ot7Pg2Vh-Cm7pC2G_HHPhum4G6TCZ2bk0uwwsCGv9GnCUKTgLbhSK-qp3HQRwYKu1ZnChuHszqs9jg_oYUp3R_6E5mzfw8sF0h-ZF6Mgy2OW91fu_78DVjmHIuqMuap2F3oUqAsdQGAj2ayC9FkyVPSdRbapFMubQpoEJaP-uKNoTltlABRKz7QtqxiZ8C9Jf7NQIQps3k7eMcRvUQaelN6iSSLQmXgLV9K9YWLSUy5iEpUnRsVkHISj4frZhZDDVAuU4ZfEL8en_v2ABaap1IQf_MlqqO2nSp5BcLCFxE1czgDcu54LOmL8U7wxqEj3ul1jN_2dIn7Qwgfm1Md_wfYJi1dIIYZFOD5NNG9wNQAkDudNFFxlaZYALZjTslR6K72HiFU4LicgauprHZ4EE2DiHrzTzjD9hDajzAgkfGumZMQ-QbsFQSTIFM8-1pi46_uZYwIHZVVU3O1ZhP4QFoRQsgNVsF_za2V0T1wkjRCOk0bPP4vO9oBE9RbmaQp8RtHKB-c9eIRr2c3hCG6rA02MSMFhoemUMVlndaHgSMf4YqYrbXLqpT-FpNbfjt7ec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4508efc7.mp4?token=QGC4VKL5p2bchAdtDPlYwXABbNZGPw0FLSbv9euMyukYGv3Kf0UtviGZTQOg00Jis9qPCAQLCas00FJ-8eY0uydN_x2oRd3xM0E-Qg8N80Ot7Pg2Vh-Cm7pC2G_HHPhum4G6TCZ2bk0uwwsCGv9GnCUKTgLbhSK-qp3HQRwYKu1ZnChuHszqs9jg_oYUp3R_6E5mzfw8sF0h-ZF6Mgy2OW91fu_78DVjmHIuqMuap2F3oUqAsdQGAj2ayC9FkyVPSdRbapFMubQpoEJaP-uKNoTltlABRKz7QtqxiZ8C9Jf7NQIQps3k7eMcRvUQaelN6iSSLQmXgLV9K9YWLSUy5iEpUnRsVkHISj4frZhZDDVAuU4ZfEL8en_v2ABaap1IQf_MlqqO2nSp5BcLCFxE1czgDcu54LOmL8U7wxqEj3ul1jN_2dIn7Qwgfm1Md_wfYJi1dIIYZFOD5NNG9wNQAkDudNFFxlaZYALZjTslR6K72HiFU4LicgauprHZ4EE2DiHrzTzjD9hDajzAgkfGumZMQ-QbsFQSTIFM8-1pi46_uZYwIHZVVU3O1ZhP4QFoRQsgNVsF_za2V0T1wkjRCOk0bPP4vO9oBE9RbmaQp8RtHKB-c9eIRr2c3hCG6rA02MSMFhoemUMVlndaHgSMf4YqYrbXLqpT-FpNbfjt7ec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله نظامیان صهیونیست به خبرنگاران فلسطینی
🔹
نظامیان صهیونیست در حین تعرض و یورش صهیونیست‌‌های شهرک‌نشین به بخش قدیمی شهر الخلیل، به خبرنگاران حمله‌ور و مانع از پوشش این یورش شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/685358" target="_blank">📅 20:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685357">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc5cd16df0.mp4?token=NtkN2OPhK0j2YhfPCQeCDkewAD5XKhrYE08IKuPlNhoh3dr6oJ71_i3uePEWG6B5xU_MQEcnqcolJEuuv_QOpSd6dnn6ttG62-vv5a25OGvaARCFZ-_YTQgm3A2no7JnLqlvHN2Yj59y7tisW4QFIlE-u-_IGJLpyyihoFIHRDqOgleOUuq2JjE0vwl0VVOuXanOSyn4yB6IXGP81BR8r1hjfGhrKUTqluof04XNseO_TMk2Jyb9eBQMOk-N6vsZtoE4pomrB0WmxG-kwm-7rvf3FJa4Ek1hbVItLEzgI8PJ4G3gr6UtfX9byK0Zrt0riWaFDN3xXKtkndcUYFaPwJUGmCSyLX5wnGeHYtIx2voVK0fxy_l9RTdkjWgKHCnneCGJc6wT192bzmLD6Roa5XJXepKtjn7sjdAC2ekbQU623nmhiSb6qXWwIZsXcITsNIHcLxrWjGmMiP-FIwKvLoYBxPVRd7SM8ahuw3nHTLcyWYrMgW0Wl_VGNaEoBVPKkXYNYr2PZm1-smAc6B_g5LNAOJzybV7Dsw5pU4UtYZoO0zsqNvfF3UsKXKTXtSXtSEK6mD55g8G8_rAhongC7fuZ9T2rotKidGLrrOoUckao7jJXQKWIvLbm526zGCf42o4SsgztlSvpEe-tjC5OsmfJ9uyyg2oa8S4FDHjxQdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc5cd16df0.mp4?token=NtkN2OPhK0j2YhfPCQeCDkewAD5XKhrYE08IKuPlNhoh3dr6oJ71_i3uePEWG6B5xU_MQEcnqcolJEuuv_QOpSd6dnn6ttG62-vv5a25OGvaARCFZ-_YTQgm3A2no7JnLqlvHN2Yj59y7tisW4QFIlE-u-_IGJLpyyihoFIHRDqOgleOUuq2JjE0vwl0VVOuXanOSyn4yB6IXGP81BR8r1hjfGhrKUTqluof04XNseO_TMk2Jyb9eBQMOk-N6vsZtoE4pomrB0WmxG-kwm-7rvf3FJa4Ek1hbVItLEzgI8PJ4G3gr6UtfX9byK0Zrt0riWaFDN3xXKtkndcUYFaPwJUGmCSyLX5wnGeHYtIx2voVK0fxy_l9RTdkjWgKHCnneCGJc6wT192bzmLD6Roa5XJXepKtjn7sjdAC2ekbQU623nmhiSb6qXWwIZsXcITsNIHcLxrWjGmMiP-FIwKvLoYBxPVRd7SM8ahuw3nHTLcyWYrMgW0Wl_VGNaEoBVPKkXYNYr2PZm1-smAc6B_g5LNAOJzybV7Dsw5pU4UtYZoO0zsqNvfF3UsKXKTXtSXtSEK6mD55g8G8_rAhongC7fuZ9T2rotKidGLrrOoUckao7jJXQKWIvLbm526zGCf42o4SsgztlSvpEe-tjC5OsmfJ9uyyg2oa8S4FDHjxQdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسن روحانی: رهبر شهید بارها نگذاشتند جنگ شود/ در سال‌های ۶۹، ۷۷، ۷۸، ۸۲، ۹۲ و ۹۸ تا مرز جنگ پیش رفتیم و عبور کردیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/685357" target="_blank">📅 20:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685356">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2LR9xCmgNVPUREZC2Ai0WaAoq2rEZNoEtPgMwDM-LLTR0iPXBIaOhyAn5LM5HzQ1Y1dYbfa5kbaXG9bUv_MoUDdeN8c7lEF1snRoFfGmoJDRS08m14QQ1On9pb_5LnbkRdDpq5nBA-BWh37OeDCXi3YlukO0ohmNT5uWQopcGfLOSSVd1gjPWtF1RNSdBYQBTY5Z9QdjmiI9G5ymByYipDx2EH0EtIe5RLbPnJjt-d_UOVdvt73txiluaYZVM-pAoNmuz8jaioHCWk02qpV2ador1Git5cKkvfhOjRThWT5KcaIUNTwCuxC16G4GQMrx-WQw3zCLgttgeqCqNNOnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ خواستار تغییر مدیریت و مجریان CNN شد؛ به‌جز مجری‌ای که از او تمجید کرد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/685356" target="_blank">📅 20:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685354">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39cdccc011.mp4?token=TW5b7VmTUXgi6YJqvBn-P5J-v-0R-EpRBrFGAhUzNsfgZ2wuckvcteOJ9z9ii4zeYVJiszAvNliwfD2YOPta8MKnO11IgOwNLuHRjSFra96mF28oOa-PLBZkZePnCWaFOopcDnHY-3ZVFs5MCau3CxpOL7AqiFfupXgrPT_Yw9Mbsg0d7gUFjDuYGFQh9IE57V46WRE-ZBrOXeGDMX7ex5W4eFOFdCXPREDkX9WvuRkjLMzod-zW9PBK5hvFOLWvo4Q_mgJj6HQByYgMoEN02AHGr3cxRpCqUfRzWiJIODuHGDMCmZB6_D5nJpLiJzutQrTjAehQ2Rx81_IGoYy8Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39cdccc011.mp4?token=TW5b7VmTUXgi6YJqvBn-P5J-v-0R-EpRBrFGAhUzNsfgZ2wuckvcteOJ9z9ii4zeYVJiszAvNliwfD2YOPta8MKnO11IgOwNLuHRjSFra96mF28oOa-PLBZkZePnCWaFOopcDnHY-3ZVFs5MCau3CxpOL7AqiFfupXgrPT_Yw9Mbsg0d7gUFjDuYGFQh9IE57V46WRE-ZBrOXeGDMX7ex5W4eFOFdCXPREDkX9WvuRkjLMzod-zW9PBK5hvFOLWvo4Q_mgJj6HQByYgMoEN02AHGr3cxRpCqUfRzWiJIODuHGDMCmZB6_D5nJpLiJzutQrTjAehQ2Rx81_IGoYy8Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آپدیت جدید تلگرام ویرایشگر متن پیشرفته
🔹
کاربران پریمیوم حالا می‌توانند متن‌های طولانی را با ده‌ها ابزار قالب‌بندی و کمک هوش مصنوعی، حرفه‌ای‌تر ایجاد و ویرایش کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/685354" target="_blank">📅 20:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685353">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">07-2 Ane Manaee (1403-09-01) Marghade Sheikh Sadoogh</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/685353" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه هفتم؛ بخش دوم
حجت‌الاسلام امینی‌خواه:
🔹
زنگار دل، قصه‌ای از چرک اعمال [00:50]
🔹
وقتی قرآن هم بر دل اثر نمی‌کند [5:37]
🔹
از ترک عمل تا خروج از ایمان، فاصله‌ای کوتاه [6:38]
🔹
آنجا که زکات و انفاق، آزمون بندگی است [10:05]
🔹
حج‌گریز در شب اول قبر: انتخاب بین یهودی یا مسیحی [12:30]
🔹
بخیلان کافر؛ فراموشی فضل الهی و وظایف بندگی [15:17]
🔹
حسادت؛ زمزمه‌ای از کفر و جنگ با خدا [17:23]
🔹
رجب‌علی خیاط؛ مردی که با فرار از گناه، چشم دلش گشوده شد [19:55]
🔹
انفاق؛ آزمون سخاوت یا سقوط به کفر؟ [21:31]
🔹
عیب‌جویی و فضاحت‌طلبی؛ قدمی به سوی ظلمت کفر [23:50]
🔹
احوالات حضرت زهرا (سلام‌الله‌علیها)؛ تصویری از باور عمیق قیامت [27:34]
🔹
محشر حضرت زهرا (سلام‌الله‌علیها) در صحنه قیامت؛ هفتاد هزار ملک، عود، و پرچم‌های تسبیح [30:18]
🔹
قیامت در التهاب؛ روشن شدن آتش جهنم به خون‌خواهی فرزندان حضرت زهرا (سلام‌الله‌علیها) [37:27]
🔹
محشر در حسرت: ای کاش ما هم فاطمی بودیم! [41:44]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/685353" target="_blank">📅 20:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685352">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tURStc0mxS0RZ1aeG_3SeWdrlv1wWOISRBeRnseIYzUNI13xmu5Ltgbur7tmKfflkwjgrN0RWOoEUjUWt7UHbW7nsrlFaaiO2ZLqffsfJmEiA0UnRDvaY2F6yvXtrHuH70C4eVg-MT93oxU02NY_1_jqBH73sOLjX6110UEDJhsYJBHZvKLH38iBDsMvstL3BTBDBnF-meWb7XzmVpad-PLcddN6V5XHR9u1MO7n0d38XHyUj-Lsr6SNvbIuuJaooo7oTWdVspvWcAV2TkJmKlJHJ1M2cvtn875NVaE9UogrVPLKzWBF5lxjmEB8WdBi707G9cTosAQ5EBOFMsq3Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چند تا ترفند که روزی به کارت میاد #ترفند_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/685352" target="_blank">📅 20:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685351">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eob_HCvC0-la2h7tWWpEyo4_CZtSWPkKvHQKdvoIgkuUFq4sLlRtbKo3kYVTuPLr5lIobLQFipoln7ibdRYCvYo8pjpZLH6Zh6qxo8DxZ5Vi9bKj749oWtkDie_JTY9T0kWIT8ZrnjGHD19v7NjC5unEe0o_tGeac1b75BPNUaQmDInvPl6SjQYlSs8zLZIVf5a_7jvRSBedCz3RJw1ejrbBtUvMQwZudZBOSJIq3Re8MPrJPbfrZCd4K-6QHU9IXYF64DeaIgYu6AHDgSefh56NC-VsJO2hE2WVsKa4Amv63OgYiLr35DCq6fih0DgYdgHvmE73-3ECq-7RIXe7Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬇️
به مناسبت هفتاد و پنجمین سال آغاز فعالیت بانک صادرات ایران
🔵
اهدای جوایز ارزنده به کاربران سپینوی بانک صادرات ایران با برگزاری کمپین «۷۵ ساعت تا ۷۵ سالگی»
🎁
بانک صادرات ایران همزمان با فرارسیدن هفتاد و پنجمین سال فعالیت خود، جشنواره «۷۵ ساعت تا ۷۵ سالگی» را در نئوبانک سپینو برگزار می‌کند. کاربران می‌توانند با شرکت در این رویداد ویژه، یکی از ۷۵ برنده جایزه نقدی ۷۵ میلیون تومانی باشند.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#سپینو
#جشنواره
#جوایز_ارزنده
#اخبار_سایت
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/685351" target="_blank">📅 19:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685349">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8aac8cd06.mp4?token=TkiE5BEJ9gk334T0FowCaEIYKpEF0WSKtwWmAYlbXpHGM2lEIjDpcyh8c5xkxJowMIRzedcA6ZelHyV6zhhlXYRAnN-jp7rX6sDgMWVgISq8kNqX7-hN8lQnrrZt_HXds_YjEX2Xs8Uu5Cw_TO439ATURVwt7KUfgoDQyEjTJhkN0ObpZC573cybC2Ltu-4pSJKNvtBeBZkm6l9YG4maY8UyyhOheP1ElA9gcFwXk2jZszq8nYtj7O2-bFa0tNPTEgKCsOW97hZaS8_z_XSJx2VypAm677USBry1BL5c9ptwEJMQ0O0YhTgaFueWXGyQbAKwmb9-IjK_cEPBe_WIsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8aac8cd06.mp4?token=TkiE5BEJ9gk334T0FowCaEIYKpEF0WSKtwWmAYlbXpHGM2lEIjDpcyh8c5xkxJowMIRzedcA6ZelHyV6zhhlXYRAnN-jp7rX6sDgMWVgISq8kNqX7-hN8lQnrrZt_HXds_YjEX2Xs8Uu5Cw_TO439ATURVwt7KUfgoDQyEjTJhkN0ObpZC573cybC2Ltu-4pSJKNvtBeBZkm6l9YG4maY8UyyhOheP1ElA9gcFwXk2jZszq8nYtj7O2-bFa0tNPTEgKCsOW97hZaS8_z_XSJx2VypAm677USBry1BL5c9ptwEJMQ0O0YhTgaFueWXGyQbAKwmb9-IjK_cEPBe_WIsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوشحالی والیبالیست‌های نوجوان ایران بعد از قهرمانی در جهان
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/685349" target="_blank">📅 19:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685347">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d17b66253f.mp4?token=eBWuehNxN23GdhsMhNbDA8nuZUf0KjE1AnGzhMVIeUeeChq7iLDswx_POTgfeNkKybWmPkJhoB6kE3uaaEv0QaJG9Ni4vbWXhOYC3ehuvHD8xwRaveJ4dG8B_odmmWrpyqMV_nmuJq49TZqENks3dQOqPoEwaAR6JOR_E3J_Pc7pdBBMSffYAcnpAvwS5691Vs5e3duERqz1ri54kFck7hCUikLZ40SiboigSRJB6C8uRppgfBmrto3aewzCaWcDtLOBTYFcc_02IY4uzrY0jAntz9AfNAsJ3TbihAQD3TRT-q-ji9w8fknIOA_AAQxXerFci-MNcvAPdProbWaq7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d17b66253f.mp4?token=eBWuehNxN23GdhsMhNbDA8nuZUf0KjE1AnGzhMVIeUeeChq7iLDswx_POTgfeNkKybWmPkJhoB6kE3uaaEv0QaJG9Ni4vbWXhOYC3ehuvHD8xwRaveJ4dG8B_odmmWrpyqMV_nmuJq49TZqENks3dQOqPoEwaAR6JOR_E3J_Pc7pdBBMSffYAcnpAvwS5691Vs5e3duERqz1ri54kFck7hCUikLZ40SiboigSRJB6C8uRppgfBmrto3aewzCaWcDtLOBTYFcc_02IY4uzrY0jAntz9AfNAsJ3TbihAQD3TRT-q-ji9w8fknIOA_AAQxXerFci-MNcvAPdProbWaq7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول پرسپولیس به ملوان
🔹
پرسپولیس ۱ _ ۰ ملوان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/685347" target="_blank">📅 19:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685345">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0835b0d18.mp4?token=Sb840zkE-bfouQpCUuL5lCGz5NdDENQ32z83jWgSgTG83flkvESF6fnNYvYUwZePvA9i57bh1L0iIITABKklXjgsQ8bEEBPntjIdoWxJPHASY-RKQ_tGbvxUhAsMghTZlXlk0RhShdlWNkhPPW66d2BpFK_KEQW75Czl36ahe_X-GfK1TLSd3KuswnxpVcQJKGK8oYE5Ai0GVRU36ghL59m-lw9vV-abI3-iPjpbm2pJAzdgLSqsreX98Li9eXkmvA_XJGdyQsUbPbkhOjRgGOW667tYvNQYTl43JNVoQf64sklMLzSgH2yCa70bn7WlFKMiYpkAy3CeIhFSuMheCIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0835b0d18.mp4?token=Sb840zkE-bfouQpCUuL5lCGz5NdDENQ32z83jWgSgTG83flkvESF6fnNYvYUwZePvA9i57bh1L0iIITABKklXjgsQ8bEEBPntjIdoWxJPHASY-RKQ_tGbvxUhAsMghTZlXlk0RhShdlWNkhPPW66d2BpFK_KEQW75Czl36ahe_X-GfK1TLSd3KuswnxpVcQJKGK8oYE5Ai0GVRU36ghL59m-lw9vV-abI3-iPjpbm2pJAzdgLSqsreX98Li9eXkmvA_XJGdyQsUbPbkhOjRgGOW667tYvNQYTl43JNVoQf64sklMLzSgH2yCa70bn7WlFKMiYpkAy3CeIhFSuMheCIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار برای نخستین بار
/
لحظات اولیه حمله به انبارهای نفت تهران در جنگ ۴۰ روزه
🔹
این آسیب‌ها، بخشی از ظرفیت پشتیبانی و توزیع سوخت پایتخت را از مدار خارج کرد.
🔹
انبارهای شمال‌شرق و شمال‌غرب تهران، دیگر در چرخه تأمین سوخت قرار ندارند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/685345" target="_blank">📅 19:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685344">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4s7aCocXBh5Mdhq85zD_4TZytx_KI0fg3csivsedPGji3ogRCe5F8ORu2U_DgpZjo2iecSOgEeYgYSeQeHDyhHEcJEAptO2azqZhnUF3Jrr-tCi9QGTVUUCva2agws9ASXHACSP6P4MFcp3AYoNaBUcsFgRVKeN4wZ7pgllcWu4cYYNe5wg2QCLOgMyAKlssIM1bUyxhAkyI8DCVlyOLXS7oE3vzdR9KioTBzmxk7qUUETqh60QDxf39DqS1DM9yQYmI4au_0hn4dpNYKXzVYXgiAmfDD9Lg6tL4Z5uD0n-8XzW6T82nw9jWp2h0P9-ucb7omRoACc5CTBIH6mb5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف به ادعاهای وزیر خزانه‌داری آمریکا پاسخ داد: «ای دروغگو!»
‏
🔹
رئیس مجلس، در واکنش به اظهارات وزیر خزانه‌داری آمریکا درباره ایران، با بازنشر مقاله‌ای از پل کروگمن، اقتصاددان و برنده نوبل اقتصاد، عملکرد بسنت را مورد انتقاد قرار داد
🔹
قالیباف با اشاره به ادعای بسنت درباره عبور ۱۳۰ میلیون بشکه نفت از تنگه هرمز طی دو هفته، این رقم را با دو «۱۳۰» دیگر مقایسه کرد: ۱۳۰ میلیارد دلار هزینه جنگ با ایران و ۱۳۰ میلیون دلار ضرر یک شرکت فعال در بازارهای کاغذی نفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/685344" target="_blank">📅 19:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685343">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78351ed32d.mp4?token=OkWkOdi-TElLjdv5uTnFyoNvdmPeQmORKWaucz8zYWZzO1XeUko9GxmvBpimDfy25p6YumaQQkAl4bT9C1VNqtoiXbONZBpVXQinFbJ27VVKYbSegoukIpA4nFPfqyciO_2jzXzeTxkQFG38aBx5RwX5wuC_XGAAPizueCjptsv2NCv2USijoy5MtdtCGJwExzq-B1M5Mg-vQDz_ONYEUAoJt9uwYiF1XSF7rvYSOkTdhkSBXiWsKCaEb-J3bQ2e-9XuPuZOt5hbvaAqP2vF7a1LYB-TzTaBNA9n-AahObRK0QDHAAQ84_o6HxwF7YnTKs3UDP3jYS69IYudLVtpFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78351ed32d.mp4?token=OkWkOdi-TElLjdv5uTnFyoNvdmPeQmORKWaucz8zYWZzO1XeUko9GxmvBpimDfy25p6YumaQQkAl4bT9C1VNqtoiXbONZBpVXQinFbJ27VVKYbSegoukIpA4nFPfqyciO_2jzXzeTxkQFG38aBx5RwX5wuC_XGAAPizueCjptsv2NCv2USijoy5MtdtCGJwExzq-B1M5Mg-vQDz_ONYEUAoJt9uwYiF1XSF7rvYSOkTdhkSBXiWsKCaEb-J3bQ2e-9XuPuZOt5hbvaAqP2vF7a1LYB-TzTaBNA9n-AahObRK0QDHAAQ84_o6HxwF7YnTKs3UDP3jYS69IYudLVtpFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول پرسپولیس به ملوان
🔹
پرسپولیس ۱ _ ۰ ملوان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/685343" target="_blank">📅 19:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685341">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JH9P2Pi21h5aD9DhPZYe8L8JVQRDGurDfyc3VkjzGJzWXNlKoXUEpPXd8maMsuYZJBjBc3h_lhms4LW3JuCFjDxIb7XS1D-gJ6IhBiQVwO7N-wiUdFLJ1okcw6OF7pG1t3_pIYdkiD0cUA2i1OPGy8iSKuGOhjUps-_ofyz67AOWTctV5E3z8ggiMUlGmUFQpkbbVDWc91aomUnNhiW9cqHcwX2qIDGkY_uuPu_vV3BrAjVIf2dX5t9krdc1ZaCM3JE8dsR3QNVn_LbhCJjJNQNbidQe-Ge0RY72sTzV_levq3KIPo-nK8MK68HElldTdLES-ggi6zmC-p0xeYx7Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری ؛ درد دارو
🔹
اگر برای تهیه داروی مورد نیاز خود یا خانواده‌تان با کمبود، گرانی، نبود پوشش بیمه، نایاب‌شدن دارو یا سرگردانی بین داروخانه‌ها مواجه شده‌اید، تجربه‌تان را برای ما ارسال کنید.
🔸
در چند خط یا در قالب ویس حداکثر ۳۰ ثانیه‌ای، روایت خود را همراه با نام، شهر و نام دارو برای ما بفرستید
👇
#درد_دارو
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/685341" target="_blank">📅 19:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685340">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e872d9b3c8.mp4?token=n-sMqXpvfeUBqAb5Kn4KwuAl2G23LD9RTCipoKmAUZkEyaWIe58JpfSLbsW9gbS2R45i2GXSI_sO-QgoCfQu8gjRVTfGw8EaZljQHeoMCTG_8a0WSzo-Js1qltw8nsPG2OaGuzCILuPzLCWI4EkxQj6VFDUtNhUzGBRcCRJWgiDS2OLbnkDuuDJ5IdKhbBAj3vobrFg2MicHyT2FkpKbFF804O-m2KG-rq3Yr0CuqOYX3AbnKr47cpAZF6349zExZexLDRV8gaAdWekD4slWHH26ix-1DWpRcRIWsoPh2f3yr3Xw7AsWlW-v-sykmlQQ3rGBmtH2sOpfimILiDJ6kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e872d9b3c8.mp4?token=n-sMqXpvfeUBqAb5Kn4KwuAl2G23LD9RTCipoKmAUZkEyaWIe58JpfSLbsW9gbS2R45i2GXSI_sO-QgoCfQu8gjRVTfGw8EaZljQHeoMCTG_8a0WSzo-Js1qltw8nsPG2OaGuzCILuPzLCWI4EkxQj6VFDUtNhUzGBRcCRJWgiDS2OLbnkDuuDJ5IdKhbBAj3vobrFg2MicHyT2FkpKbFF804O-m2KG-rq3Yr0CuqOYX3AbnKr47cpAZF6349zExZexLDRV8gaAdWekD4slWHH26ix-1DWpRcRIWsoPh2f3yr3Xw7AsWlW-v-sykmlQQ3rGBmtH2sOpfimILiDJ6kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوشحالی والیبالیست‌های نوجوان ایران بعد از قهرمانی در جهان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/685340" target="_blank">📅 19:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685339">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/000f0a3f47.mp4?token=JAiOCAqsm5YXPLdr6Ttl9TSlgeJCRGS1CFMcFYT1U7jLYEIzX1Tcn3HkL5MBALZI6Wt7q1Z6GaPbyoBnPVXd-DYIbMPBZ-JlFgoS500Cqc8CMNvVdNbHQ0x0-S4MNddEAHjqVftYfBTvKROYYjGx8FuPo09r5lL_yQhmk6ErlDWHGPdnYUkJumTdw674lbfENFzUVueoELHiRlgUmQLBwmgYc1vQsVhuvdnA9eUci4CkEnh0s3H4K0WPHN23nEDRQMnm6rtG8b47SuC4fxqXeUX-cPWZSaFW5vYSPFUlrmCTVIsB-Unio_qXo08q8mjhcnpOhj1Kii5Nqwg2G9w_HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/000f0a3f47.mp4?token=JAiOCAqsm5YXPLdr6Ttl9TSlgeJCRGS1CFMcFYT1U7jLYEIzX1Tcn3HkL5MBALZI6Wt7q1Z6GaPbyoBnPVXd-DYIbMPBZ-JlFgoS500Cqc8CMNvVdNbHQ0x0-S4MNddEAHjqVftYfBTvKROYYjGx8FuPo09r5lL_yQhmk6ErlDWHGPdnYUkJumTdw674lbfENFzUVueoELHiRlgUmQLBwmgYc1vQsVhuvdnA9eUci4CkEnh0s3H4K0WPHN23nEDRQMnm6rtG8b47SuC4fxqXeUX-cPWZSaFW5vYSPFUlrmCTVIsB-Unio_qXo08q8mjhcnpOhj1Kii5Nqwg2G9w_HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوجوانان والیبالیست ایران قهرمان جهان شدند
🔹
تیم ملی والیبال نوجوانان ایران امروز در دیدار فینال رقابت‌های والیبال نوجوانان جهان با نتیجه ۳ بر یک مقابل فرانسه به پیروزی رسید و قهرمان جهان شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/685339" target="_blank">📅 19:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685338">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
احتمال درگیری تمام عیار بین رژیم صهیونیستی و ترکیه وجود دارد و آن روز پایان ناتو خواهد بود
دکتر بیکلینی روزنامه‌نگار برزیلی و استاد روابط بین‌الملل در
#گفتگو
با خبرفوری:
🔹
این یک احتمال واقعی است، چون رژیم صهیونیستی همچنان از حمایت ایالات متحده و متحدانش برخوردار است. در سال‌های آینده حتی ممکن است شاهد افزایش تنش میان اسرائیل و ترکیه باشیم.
🔹
همچنین رقابت و تنش میان اسرائیل با کشورهایی مانند پاکستان و ترکیه می‌تواند بیشتر شود و احتمال یک درگیری گسترده‌تر در منطقه را افزایش دهد
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/685338" target="_blank">📅 19:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685337">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/072008c1e8.mp4?token=pqtarN-Jqespq14Lz_WGll12YqlxLxci3ivYrvdk7z1HFuL5RXHtSYtbtvAYSbOxTPpKRJr_4OupeVplNAiyoQK95n8CtTE98ZMaFmOlFXRymu12KuTfsmDDM1HF0Zum-q3DkL696lILy16qxZ4q7_PyCpC9f_s6kSE4PGwDlgIm85QmctoA3sOLJzxXuhyjbdx8hXmCsFavdmuLNm-LbWn0L5E6kQrwsdX8fINXDMqSCusyZWHITADBUDT2_PhPSYFO62MdWWiUPQo34mQKE5c3STDCJEY_gpj_tq5r-mTXA0JzZ5y3o4EJe8LHl8hnYdq-pCjLM0i1ThIdDwgrXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/072008c1e8.mp4?token=pqtarN-Jqespq14Lz_WGll12YqlxLxci3ivYrvdk7z1HFuL5RXHtSYtbtvAYSbOxTPpKRJr_4OupeVplNAiyoQK95n8CtTE98ZMaFmOlFXRymu12KuTfsmDDM1HF0Zum-q3DkL696lILy16qxZ4q7_PyCpC9f_s6kSE4PGwDlgIm85QmctoA3sOLJzxXuhyjbdx8hXmCsFavdmuLNm-LbWn0L5E6kQrwsdX8fINXDMqSCusyZWHITADBUDT2_PhPSYFO62MdWWiUPQo34mQKE5c3STDCJEY_gpj_tq5r-mTXA0JzZ5y3o4EJe8LHl8hnYdq-pCjLM0i1ThIdDwgrXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیلاب در مادھیا پرادش در هند
🔹
تصاویری از منطقه چترکوت در استان مادھیا پرادش در هند نشان می‌دهد که آب‌های سیلاب تا ارتفاع نزدیک به یک ساختمان یک طبقه بالا آمده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/685337" target="_blank">📅 19:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685336">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ضربه مهلک مرزبانان هرمزگان به شبکه قاچاق سوخت/توقیف۲ میلیون لیتر گازوئیل در خلیج فارس
فرمانده مرزبانی فراجا:
🔹
مرزبانان استان هرمزگان در یک عملیات مقتدرانه، ضمن شناسایی و توقیف یک فروند بارج یدک‌کش، از خروج ۲ میلیون لیتر سوخت قاچاق از کشور جلوگیری کردند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/685336" target="_blank">📅 19:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685335">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgqYnK1GVANxhYqel_LAwKrGHts848lTHcvVTpxkZySEvh8D775wP5eMfxWWUW0hzuS2KzAwPMUT5eJhvxrVIDksCtZmi4E2dOSASschjnx_9B6v-ANBCVNM5_Z4Tf0UcZVYVh0KW5L_vOGgzCFmOqRyzdUIELKSRTkaMjGiKsk_y7ibaagG4e-q4PmA3zBwazk65K6QR11ylEBAr6t6OdM6hqNHsF5jdIKmpA1lcXL2HVTLQjiOvPpq-CtHQ4sxTefly_Jy0cdL1q1zSh2-I1U5HVyaMsz6A0Feh8NTRGvbyo25VpYWe2PSoVKZM2JB9qppTjUHbDtyiDo1fC-64A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میوه‌های خشک به جای دارو!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/685335" target="_blank">📅 19:06 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685334">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rp9fGXaUiB1FlspbPspw4Ak0Y15eysIBYBpUV9u8PBvkhYM0eUAjP4FLVAzOBoAND7vZtw_96oLYQWZWOR5XbZLgvD5t3z7EsjVMRC_piI90ex17y4pgUMSc4SP057CqNrNQzO4gFz744aNk_OTwOVUj1pLKQYL37fkvUE4Z35wSnGGveK3QjjQtkIvtkVU_EFCbfNohpU_lZ8pYtR4WilnTB_bDqiON60fIIli4H1G-122oqJLoDO1wsKALs2NVbhNMmriipu7v0OZdkQxLPiIta_bQptj8zrRE0tm5YuLo99oGCB83oQ0Lo60bywilpn39zc8Wk6Rohuhf8q4Xhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏳
خوبا زود پر می‌شن
زودتر قسطی اجاره کن!
🔥
🏡
ویلای استخردار تا کلبه جنگلی
⭐️
اقامتگاه‌های کمیاب و پرتقاضا
⚡️
رزرو آنی و قطعی
مشاهده اقامتگاه‌ها
👇
https://www.jabama.com/landing/jabama-best?utm_source=telegram&utm_medium=social&utm_campaign=news_0607
@jabama_com</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/685334" target="_blank">📅 19:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685333">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPeLI9OL8lk6ZZNCwWZHtVQSH3Cww3my8BAM5eIC-kz2mAmbEQFW3VzpSct_TRk0ucphyjuo5FZsru50lRI7bQJVBp3RZLsV1Zt1LFQ8NM0mL5gJPk8VFVpSaLHASz_lagO9_4myQ-F1Z3TbB0yyYIXf38OosE-wo0WQpfwLk62WXkGMPx7VnowxS_qblY0PGUXbsvh876vVIPyw0SVUL8_lfOawdbGLjJig1GnjBVOx8uxeZPFOs75dqtT5gzlSfYj2gGEFg3eU7VErdHD9KQDsqhE8JCpR1h9bA1145N6Xz2riKloCkL_wieIQoPa82nmM2Q8YGINAL7fkOt5XMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه کریس مورفی، سناتور آمریکایی به پدوفیل: تنها دلیلی که قیمت بنزین سر به فلک کشیده، این است که رئیس‌جمهورتان جنگی را با ایران آغاز کرد که هیچکس آن را نمی‌خواست و او به هیچ‌وجه نمی‌توانست در آن پیروز شود. انتخابات ماه نوامبر، همه‌پرسی درباره بی‌کفایتی او خواهد بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/685333" target="_blank">📅 18:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685332">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ba8def8e7.mp4?token=YEJtP8ztjjQdX1VXHTbhkRwJ6inbpqAtnSViPZ6TH3mlI9Nqzg_T3ExHaDlYzLEpodPeVwiYTz1VSgneIR8H1fuQcYWn53GwRnnvhEnFrYdkMjsPxjFXhyR3cUc5F8WPQfU1f3ErsQMkge8DcJlF3gRlCI4ZiCaYAPSfGloE10dYvmmGEfu6zy8ZMAWPqf3vZV5ysaI6NY58p4AqbRNIo0vRvuD8UkCmqLs8Oo8y1YA0uNz2XDMy6N4sL0fRUMpD-jjHc2XGlMee_Et1JaWderGVVOQvyUixPylHRDRcFcmWVJukhXfSlaLqC4MnK0MOnVwvUjTwq84ZYCbHZWIjBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ba8def8e7.mp4?token=YEJtP8ztjjQdX1VXHTbhkRwJ6inbpqAtnSViPZ6TH3mlI9Nqzg_T3ExHaDlYzLEpodPeVwiYTz1VSgneIR8H1fuQcYWn53GwRnnvhEnFrYdkMjsPxjFXhyR3cUc5F8WPQfU1f3ErsQMkge8DcJlF3gRlCI4ZiCaYAPSfGloE10dYvmmGEfu6zy8ZMAWPqf3vZV5ysaI6NY58p4AqbRNIo0vRvuD8UkCmqLs8Oo8y1YA0uNz2XDMy6N4sL0fRUMpD-jjHc2XGlMee_Et1JaWderGVVOQvyUixPylHRDRcFcmWVJukhXfSlaLqC4MnK0MOnVwvUjTwq84ZYCbHZWIjBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راسته میگن پول رو بذاری رو جنازه بلند میشه؟!
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/685332" target="_blank">📅 18:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685322">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MIfGPiSOUVhH9CYa8FkxXKuv_g4n6D_NBZE-qbqINnJZwq2HfsXNDUwVxQSsNoBktgAfFxasgfm6k3RfCJhgaWpPdpWSSWAg71YKTPevc-YypHdLsAFpUQqf0CDk0BXBHnXdkPEwrhN7HMLQ0IYxZpaR4UaClVF9CbLubR35F7jzfIPmmI3Ub35d6FdoP2_oDMDXW0Ulovg2TuRC4LuMmR7HGbpCJFDf3g8iTfZTrlgiGPZnAVNz31NRHk0LgWulooNNXlf4oaamYHsYyOAS3fxXYeanvRKeWSsSROzS2QHxInNILCpKbOVGp7ou77L1osyXr7ifOAiYYFPv2co2cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qMEVyb1lF6Am7fncZS3C83r66j2-AqWQ7hS6WSy8Q7RHQATdjYN7Avp_XD-rGRunt7MooCcMQsInCcg795dgazxlCSI16ENfIBzvRKUIhYcCjfdjDaAF-Bvrpt34wALH3DvIR_ePlUTQEIjWvvjwbUkdtNGP0MciRCYQ5zptqCKdvv0WYZCpmEv_OuCMKDMHS_YMcyEwdiC3F2_0ayCQEPZricYy1O7VyZK7yS3CBrU2hq5fM76veYwLEx2AmTvB2N_mCk6iMpFfP8RUu-poGauG7kcpfhqRvX_p02LMBQs83ELO6jEUVd9ZX4Yko6ElZqQST0AtJwko21vCp4ep9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Si-u7AW4x6BPW6GtUP0zfmkAjVfzblWTkZAh0HCJ416k5pzEhQSdrF2ZObuhYabuoYMZC53VCB5VsnO4D7IMLRxitMMgScpqksQfjpB_HxG1ePxyhHFWl3xHN4OAfucuU0u_8DlRhMvnT1SEQZyHybvedDNvfNyQPWZCL689K2ZdE7dol6Fgj8yEQ861wr3u02jxERU7CkCECQdAgKRgSa812tLB2VPja8F7CoatlUXpNP3IHQgSz73ujRTW7n70YQJTAWL1B_bfCeqCQxKvNdPtWJd18rKHrWB7c44VHjlshmm78HZcS1dqvRFCHlu-G9DJpKwhTdalRcN65GX61g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6Cxa4Z8AxHnDRgMF3-9F1HWlng7QTDd6P-KM4gG3fjySKtY13OQ1Rr0J80gQUX8BFWg-QBVuN8tDSwp1dGoZE86iHr64VEDByUb9lxE2jpbV1C78SuvwEbZEHVbZIoqa3vSB-Cbbe-TfI8ptNSJZ99Qjv_A_PDwuQM-mI2MEnEIXtw72TAG54tHnDwimNQ7BS567ILN3PtvfhET9f58tyuibhJp7Ofa0HjgnMsZiiWezqpAEqDYGN0uuZuQCki3NCg5bD1z5uZpoXkRO4-t9U9pZtkEEm9W7haaBy_7DmYC6fwQYALFrcnnciHX0Wcwx9yqTEqazy0GZlf84DaPAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i3JtvDocuM_68SaWCALc9GTHaK-a_DGEimGlMJhu6s0BnQ_ZqRwU30PZiLp5-BKBaFXjaSixXjefCiGLhA1RIedlXZPVfGzHZSNsp3CmxwWQfEjIr-m3uqnet3M1NJrkn5JijgeJ9kWv7ir_tn__g2P9-jKoNRjD6tpm1g5-WwKc5smSgedx9DaArDW08_nVc-fMeGpy-jtqgUcBqS82IHQjy5kLffn-dZZbstQFUecs2v-sWYPqCbJyUfIpR9kPmNgI14pIkSYiLW83uNObFsG4UmbXhzSkClqp2ysOLLfWkWF75IxHCcLBIeGhSV2kYMico5CqkrTeapn3BbV0BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FJZ8SA2GQBhjQlTZDP7Qh3DVxZHN2ivzg0YqD8ZOeFZ48P53QxH87pFRjqdtmQTUGRqrNrQpK3jj2blqjQE1gzr-Xn8EFXwSRvHQLXHHyhFxqV1RgH9DYvkUBRX7PsKNoOqbo3hNxP4MxG8mTr907V6u-u-HkFu7nD5qNP4vb-rB2rioEze2Vwi5olGOLuW4_Fk5XvbsAV0_LkOfjhS2pMbWoloq_QQ3p-BIWasRJMy0IJctYc-WMdzfieRxRaf0EW-N9fQCxw3fuFlr57yQkzGSTdDwJtKNbaS5VtMhviKaHc4a7y0WyiFhmYfB6CEshfXydYweuNy6RDTf6JIgOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M3Z47lEaSOvlkEJ6417awittXyh5tEsZYMeOktOBgA3-HNh5uYeKc6RjN2TwVjZ6eVkwVcHXh8dprOenohBrXO3ReJxpcUkjuUtbv-9nKSW-k2Bi6lKwlGU7dpSrRTMKzTIAPdhBUtW3nu-203Hyu3YeouHRYq8ZqliHoJahdW_0_jqNd3wi5mqXNHajPr2tZFNMqsfS9WVz4Q8imUCjxDDexUjEMxGX-Hw8Yi6yxNUCERNIM2VkTlcOouCHlm8Fxiwsm4t-Ri1CfipfsAlbPeVsiF1H7sPKwHaTfV_5StUwfuAIPUU9FWfjq5jQVSIrohh97tBuROoNmJNpWFLCTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AznZDHy1275cNVm7i7Tg3gEbhLOkiw6mAmjrIFLVAWuDLpf5m8-UosLcezbmONmyAnMTcyHvstcG7Cn1UCr6fAAcKCZHH5F1imHFOwX2mfi3MfOeInGbCnP1tfdCnqC1-U4dVkdVyWfwju5fS1xerbxjyw10MnHzmAYbSR3uGcoyVARVqYlT0h6neFGz3K1rD4VrrrI9zK1nzGGHYFMgtRw6N85m48JvZPxyExMqAk_b2aw7fAjew3rZ2ZqaifjpJprwOFSUuy2nbM8KHVF5nDVvazD2ojcisxmLIK-drTlIl8sVXJ7FS9FgpEBfrqbAvoM39YNSViaS4NSlPgiTzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HdUosus-67wcMffmKdorzJiNO-pWH0fx8mWzSrlkzD1GEbShIiny1jfTKMjXR7JN-orLSPsrCtE_g_kjaYTzfk57P0RWLlWh7SNHAeefcoy53QvYnAaSy0OyPuGNeQYpLTYM_weKspx3NS7rIY9ZRjBwjoF-AqzKtX2_JFgTZYymUVTcIZ9aAEiXIldTqMsGrVtxUPVOIg-M7EEa7coKi_gasQ9mpPmfeUGJ8gncRSVQDJcYIlj_WwyK0bnYGffP5pjz9tQYoORqwygqC3neluFHqqUA6OUMj5C2WbxEMpHxPkqLHcyVOVMNYozjQGj_ew762B8aQ_UVvZS3u-WA5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت دل‌های هم‌قدم
💫
✨
وقتی دل‌ها برای یک نیت خیر کنار هم قرار می‌گیرند، هر قدم می‌تواند بخشی از یک اتفاق بزرگ‌تر باشد.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با نذر و قربانی و توزیع گوشت قربانی، در مسیر حمایت از خانواده‌های حائز صلاحیت، این هم‌قدمی را ادامه می‌دهد.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/685322" target="_blank">📅 18:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685321">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
آخرین وضعیت توزیع بنزین در جایگاه‌های سوخت
سخنگوی صنف جایگاه‌های سوخت کشور
:
🔹
تامین و توزیع بنزین کماکان بی وقفه ادامه دارد
🔹
امسال به دلیل شایعات فضای مجازی تقاضا برای مصرف افزایش پیدا کرده است.
🔹
احتمال می‌دهیم از مهرماه با کاهش سفرهای تابستانی، شاهد افت مصرف هم باشیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/685321" target="_blank">📅 18:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685320">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مصطفی را وعده کرد الطاف حق
گر بمیری تو نمیرد این سبق
نام احمد نام جمله انبیاست
چون که صد آمد نود هم پیش ماست
میلاد حضرت رسول اكرم (ص) و امام جعفر صادق (ع) مبارك باد
🌸
✨
💚
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/685320" target="_blank">📅 18:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685319">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
نتایج امتحانات نهایی اعلام شد؛ آغاز مهلت ۷۲ ساعته اعتراض
🔹
رئیس مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش از اعلام نتایج اولیه آزمون‌های نهایی و آغاز مهلت ۷۲ ساعته اعتراض خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/685319" target="_blank">📅 18:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685318">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46f82268e2.mp4?token=q4knbE8LK_bh9nynUOdPTr_NBDq8K7FTRII-iIuFvEA0hUxFRhLdelsipYbR32KEuHmDxgtJsYSvXKqpa5Kay-uD_RWceFb9cQu4X-FPEAQ-rkvAnewtVveL3sj0RcFuP92tEiz6c-eGS3OoRBiWGSpLLSHZwo0eP7l2PQ9qFREvTBCbFKoGyWZYUamaSAshsqTRiDYC-1Er3CxqBvGSscexMHMCjHzC7MGCYDmRl8Gvix7GmX2exV7UDV4nGtGitXB_nO6w42EM6R3N1k2LhybCEv5QjSTvFBan8WwQ2ebuG69-O1Xhddv1_CfJ8jA1K_t9ICLgxoViMnSEX4aixA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46f82268e2.mp4?token=q4knbE8LK_bh9nynUOdPTr_NBDq8K7FTRII-iIuFvEA0hUxFRhLdelsipYbR32KEuHmDxgtJsYSvXKqpa5Kay-uD_RWceFb9cQu4X-FPEAQ-rkvAnewtVveL3sj0RcFuP92tEiz6c-eGS3OoRBiWGSpLLSHZwo0eP7l2PQ9qFREvTBCbFKoGyWZYUamaSAshsqTRiDYC-1Er3CxqBvGSscexMHMCjHzC7MGCYDmRl8Gvix7GmX2exV7UDV4nGtGitXB_nO6w42EM6R3N1k2LhybCEv5QjSTvFBan8WwQ2ebuG69-O1Xhddv1_CfJ8jA1K_t9ICLgxoViMnSEX4aixA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تگرگ‌های غول‌پیکر در ایتالیا خسارت به بار آوردند
🔹
یک ابرطوفان شدید در شهر برشا و مناطق اطراف آن در شمال ایتالیا، تگرگ‌هایی با قطر حدود ۱۰ سانتی‌متر بارید؛ اندازه‌ای نزدیک به یک کف دست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/685318" target="_blank">📅 18:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685317">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAX3HsMZ6XHH9-EISRU4bacqSMQPeW4DTvDvWkHa6F4CfqXae-3vnvZ-z7e54i9IbXW4g0raHTB3DhB_vIlkKIBeGFbskVfgVBhNUpOa2MwicIsajgNu3rfiYkiicPAZcz7iAlE0GZtqqBWq17PUu2xYz5Zuf3Hpfk-o8D44_5VqERLSuOxnHWPKXrW1s2-OEHddMmnV19y8wQAXNGwNjyewaJGQQArzIGjHNNLOyTF8igdltrr4ZbI_RmDAn5vTpztqKq2vbOi24RRRUNactwy5_j6HEYxEFGXMBrtOgyKgOt8oFDv1NLpaWm70U3KnMGrCyg6Zv29xGzKK1Dn7Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شوق پرواز
🔹
تیم ملی والیبال زنان ایران برای نخستین‌بار در تاریخ، با صعود به جمع چهار تیم برتر آسیا و مرحله نیمه‌نهایی قهرمانی آسیا، دست به افتخاری تاریخی زد. ملی‌پوشان امروز هرچند برابر چین شکست خوردند، اما عملکرد درخشانشان در این رقابت‌ها باعث شد با کسب مجموع ۱۱۵.۷۲ امتیاز، سه پله در رده‌بندی جهانی صعود کرده و از جایگاه ۴۰ به رتبه ۳۷ برسند. در ادامه این افتخارآفرینی، تیم ملی زیر ۱۷ سال ایران نیز با پیروزی مقتدرانه ۳ بر صفر مقابل آرژانتین، راهی فینال قهرمانی جهان شد.
🔹
هشتصدوچهل‌وهفتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/685317" target="_blank">📅 18:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685316">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOiDUWyjiBsf6Hg_XFe3tOY9tt935C9YeO2R1fJbO9ohdJOhI1yaHZBVzpnR_C9KpYoaoUBI1APb9FX05zSxTZVzdKesEHvXsGEdtZ1WWyeccX7ayuYSSc2FsL4XpWVesjK_P71qRMb8asELEc45OJAarlF4pyrZwIbtNKeQmD_Vp2-ZELHgD3VKx26wYbFfuzM2EukNm7zKW8s2QPds2WdV1OKv-r8QtJ4iPSIs0Apjw4Pj8Bl1DZPMCU9tNoSw6mtzrFn_JahkLqcSMvQsFlfoadDOkDTtIfiRKHapDwsBAW5ls6-BUX9oVI4SUFNM_i31iPSD-SwdYF_9r-Sy7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/685316" target="_blank">📅 18:09 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
