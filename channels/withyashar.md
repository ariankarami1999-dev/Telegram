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
<img src="https://cdn4.telesco.pe/file/vb-4gCgT3fjuSRbbrnPOo42wGj4pGyxEtDkZ06V4ik093q8pDL0-97vf9pNkMpTavujGYx4-TpC4laDbZsX-esXgwHV-EfQK3lUhzrDqBd3lmpnO785yqPnWj2wjPULbqExc3jfyAo1lsdl7SbKwn6-XClM5yGntOL8EBvcrep1umNh-F7WTKHYqGxuvX5bo0_DdCHLa-qUjclpPFj2KJuluPltGrrbDOg90jfSbD6zqs2KuTzmGvBoNaI9MPbEX51Zk-nMdKmfU5ZYKziAm2si_9pQNbD2QN2zaoRo37M8qhajgAw7XfEfBd4Zu0GpKPnS62BENu4G2mxB0enpOjA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 331K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 13:27:32</div>
<hr>

<div class="tg-post" id="msg-15709">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وقوع تیراندازی درپایتخت ترکیه،آنکارا رسانه‌ها از وقوع حادثه تیراندازی در آنکارا خبر می‌دهند. @withyashar</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/withyashar/15709" target="_blank">📅 13:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15708">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وقوع تیراندازی درپایتخت ترکیه،آنکارا
رسانه‌ها از وقوع حادثه تیراندازی در آنکارا خبر می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/withyashar/15708" target="_blank">📅 12:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15707">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اختلال بانک‌های کشور برطرف شد
با اعلام شرکت خدمات انفورماتیک، اختلال خدمات کارت محور بانک‌های کشور برطرف شد.
@withyashar</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/withyashar/15707" target="_blank">📅 12:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15706">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">آژانس ایمنی هوانوردی اروپا به شرکت‌های هواپیمایی توصیه کرد همچنان از پرواز در حریم هوایی ایران خودداری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/withyashar/15706" target="_blank">📅 12:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15705">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رویترز: قراردادهای آتی نفت خام برنت به ۷۵.۷۴ دلار کاهش یافت که پایین‌ترین سطح آن از ۲۷ فوریه گذشته است
@withyashar</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/withyashar/15705" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15704">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdtavdZa4ExuZWDdn9YXjEkIshwidM5Kov0GKLOO4qEAwjWtURfAAqMGfN114fN7uXUP2X13lPER3XntxerxiXGH_X2-KPT0GPZR2W3R5JpZyZQn0Gp75hPZjE8ENGrdXHSpHuWIXBu2IKgxU7nrQM3d6PRC7ci5EqXdGnAgHCnYcuxXy4sYKaUCK8slkZ2vztXriE1H_R_yG6ItA0cGenkpgwu9tRohg77zGsKbgRJ85_qofsq3Bsz7QdByBKelVqscKEZUVwxdop6Ie-mNnfcGajzzr2Ya2f_sRv-tHpnBZ2Z2rjp39HdGqJfuTg6QMTKm01Y34lKvCap0FvcY4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ در تروث ‌: ایران رو کاملاً تحت فشار گذاشته بودم؛ در آستانه عقب‌نشینی بود، حاضر بود تقریباً هر چیزی که ما می‌خواستیم رو قبول کنه و واسه اولین بار تو چند دهه گذشته، احترام فوق‌العاده‌ای برای آمریکا و رئیس‌جمهورش، یعنی من، قائل شده بود.
ولی سنای آمریکا تصمیم گرفت تو بدترین زمان ممکن، یه رأی‌گیری بی‌معنی درباره قانون اختیارات جنگی (War Powers Act) برگزار کنه؛ رأی‌گیری‌ای که به بزرگ‌ترین حامی تروریسم تو جهان این پیام رو میده که آمریکا از کاری که من با اونا می‌کنم، راضی نیست و باید متوقفش کنم.
با این کار، عملاً به دشمن کمک کردن و دلگرمی دادن.
این سناتورها فقط کار من رو سخت‌تر کردن، ولی به هر شکلی که شده، کار رو به سرانجام می‌رسونم؛ چون من همیشه کارها رو به نتیجه می‌رسونم!
@withyashar</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/withyashar/15704" target="_blank">📅 11:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15703">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">هم اکنون دلار در تهران به صورت ناگهانی از 165هزار تومان عبور کرد.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/withyashar/15703" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15702">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjTtDFQ53jSxas752-zOrf2_eaOK9ZJsVvcVYZh_ZQb79wScp6ndeMaePRNZzlIkU_2TgzgUrvBKXIJIlntKOoCIBlL_xTndfy4vCHrl3bpYYO0qb7v0HTPKybLZwPQwDJlWWGswaDSdKZDq1vbCsWu4_fY_KS1vxjjcqe_HUzgv_VVrX9rU4RoKu3Bjvl803cWI82yqjAQkmups1hdxoC99HokrLW6O0tyHMqnZaz9kerGGR5860QQSsuTrMdwdtiUVx_nuHyOwQGcBbg2eabylkXERG_ujJf53GVWJnBzLOqG2DmtMAiN9AY8KKGNyqZRPaMPmsSp6YcscEj6K0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هگست:  اولین آزمایش سامانه پدافندی جدید «گنبد طلایی»، با موفقیت انجام شد @withyashar</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/withyashar/15702" target="_blank">📅 11:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15701">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">هگست:  اولین آزمایش سامانه پدافندی جدید «گنبد طلایی»، با موفقیت انجام شد
@withyashar</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/withyashar/15701" target="_blank">📅 11:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15700">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پاکستان: مذاکرات فنی میان آمریکا و ایران هفته آینده از سر گرفته خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/withyashar/15700" target="_blank">📅 11:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15699">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVYQu6_QTcKgAlP_BQyAywBB9zRp5nh0WfFc16ljuvnF0IIZ5vwoWjxG6onIcv9FW5XHJXtBXikOaF_7swIQM2w88ccvE4xa0JkIhM4drhztJJobvXY_Jo5-QQlu4IUwYQdzjJ3gnA10-NsG0EpRJxGvzWh55MCPAdT0gD8KxQCicv13XV1Q7J5LWrrKubGMKQdTBMZejw-C5aLRJywaNlyrMb41Fhe7QchU7qwE9V-ffqSQWgu4SoJempTxOtGcYzzfakr3m77oyj7uXxKOs8ShR5-pdo4uX4eg30pLTCNo9MzVLHJSmOFpEp9K2wByL7-XZVb66Ln1fNbMHbSBWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین بروزرسانی از استقرار ناوهای نیروی دریایی آمریکا:
در منطقه سنتکام، دو ناوگروه لینکلن و بوش به همراه ناو آبی‌ـ‌خاکی تریپولی همچنان در منطقه حضور دارند و بخش عمده توان رزمی دریایی آمریکا را تشکیل می‌دهند.
دست‌کم ۱۷ فروند ناوشکن از کلاس آرلی برک نیز در دریای عرب، دریای سرخ و شرق مدیترانه حضور دارند که توان قابل توجهی در اختیار نیروی دریایی آمریکا قرار می‌دهند.
در غرب اقیانوس آرام، ناو هواپیمابر واشینگتن نخستین گشت عملیاتی خود در سال ۲۰۲۶ را در دریای فیلیپین آغاز کرده و ناو آبی‌ـ‌خاکی باکسر نیز در دریای چین جنوبی مشغول فعالیت است.
@withyashar</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/withyashar/15699" target="_blank">📅 10:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15698">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی: از تأسیسات هسته‌ای ایران بازرسی خواهیم کرد
ما معتقدیم که بازرسی از تأسیسات هسته‌ای ایران در اسرع وقت بهترین گزینه است
اولویت اصلی ما مشخص کردن محل ذخایر اورانیوم غنی‌شده با خلوص بالای ایران است.
ما از محل اورانیوم غنی‌شده با خلوص بالا اطلاع داریم، اما مهم است که ایران ما را از آن مطلع کند.
به زودی با ایران برای تعیین تاریخ بازرسی‌ها و جزئیات مربوطه مذاکره خواهیم کرد
آژانس ما بازرسی را انجام خواهد داد و این به تهران بستگی دارد که واشنگتن یا ناظران دیگر را دعوت کند.
@withyashar</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/withyashar/15698" target="_blank">📅 10:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15697">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">WarRoom with YASHAR
pinned «
دوستان، زیر چنل تبلیغاتی از افرادی می‌آید که در بازارهای مالی شرکت دارند. اینها از طرف خود تلگرام است. حتی اگر من هم تبلیغی بگذارم، دلیل برای این که شما جایی پولی پرداخت کنید و تایید من باشد نیست. به هیچ وجه این کار را در هیچ شرایطی در هیچ کجای اینترنت انجام…
»</div>
<div class="tg-footer"><a href="https://t.me/withyashar/15697" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15696">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca023fa4e.mp4?token=twlu8y7bj97P6fc98_8dMQPvXkvWrBlQoLZMoGNZ7IpXv1j98DCROVk68IiGjyFpEYOugZTa0eZt80BZvOms5WmdjiK5N4CywMAlZCA-ayxsP8GQU1jFpZ68yb4mEqwDuxZybKxpKWrR4Zx0nbhxSbqEGT4hl1Uo3ch9teo72cQftGKaOm96Z8tzX80MhcRXKSf2LWRbIsfzQ8Vyj_jkLxgSv1blvd402ydzabHmxfk93eGv1QPot76eXLd9PjJd5ANp4_R8GxjEIZ9IbFgSg5MGKQjG6maLUq6vgMTt_6DAeLD8DGHTtI0wz7MEtbJANxRya3iDJGNen6pmLv3AoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca023fa4e.mp4?token=twlu8y7bj97P6fc98_8dMQPvXkvWrBlQoLZMoGNZ7IpXv1j98DCROVk68IiGjyFpEYOugZTa0eZt80BZvOms5WmdjiK5N4CywMAlZCA-ayxsP8GQU1jFpZ68yb4mEqwDuxZybKxpKWrR4Zx0nbhxSbqEGT4hl1Uo3ch9teo72cQftGKaOm96Z8tzX80MhcRXKSf2LWRbIsfzQ8Vyj_jkLxgSv1blvd402ydzabHmxfk93eGv1QPot76eXLd9PjJd5ANp4_R8GxjEIZ9IbFgSg5MGKQjG6maLUq6vgMTt_6DAeLD8DGHTtI0wz7MEtbJANxRya3iDJGNen6pmLv3AoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ که توی پیجش قرار داده و مضمونش بر اینه که هیچوقت نمیزارم جمهوری اسلامی به سلاح هسته‌ای دست پیدا کنه
@withyashar</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/withyashar/15696" target="_blank">📅 10:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15695">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6xgU1Bii5a_0FYHJDtvXFAW2tSWutSen6Usjhh-_FXDkpuN3ADICEAx4GEbABsWCscZ96rx5albT_UOrF6VOTkBNSmatU0sW0JQ_AeXlmcDQtvDrMgTttcTkutIdAI46PwHSBnaJrDGMeZyhJz9I_0ff3EL5zYXEcXLQLwP5fB3Q4Hp6uu9uNhX-Ljg7E39FWT3gSYluTS7fNSdByXzP8iYJb-dFMUautSWmJgaMdCc7VxnyZkOettzB6fI5oAqq7KZJjgUUVujPh_ZXHOoOFgpR7HSoAOCrBGT7rQL-I_ZXY-Ugff1eseHUaST3AQEmPdzqLt4Itox01l5ubjS7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۳۰ نفتکش حامل نفت خام ایران که دستگاه‌های فرستنده و گیرنده AIS آنها فعال است!
اکنون به سمت آسیا، چین، ژاپن و کره جنوبی در حرکت هستند و بیش از ۵۰ میلیون بشکه نفت حمل می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/15695" target="_blank">📅 01:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15694">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ‌ در‌ پنسیلوانیا:  ایران قلدر خاورمیانه بود.
ما باید این مسیر را انجام می دادیم. باید به ایران می رفتیم.
شما نمی توانید اجازه دهید که خاورمیانه و سپس ما را منفجر کنند، اگر این امکان پذیر باشد. ما قبلاً آنها را می گرفتیم، اما آنها اسرائیل را منفجر می کردند. آنها می توانستند کل خاورمیانه را منفجر کنند.
به توافق صلح تاریخی با ایران دست یافتیم
ایران عالی بوده است. اگر ایرانیان هوشمند باشند، منطقی خواهند بود؛ در غیر این صورت، مجبور خواهیم شد کار را به پایان برسانیم که احتمالاً کمتر از یک هفته طول می‌کشد.
اما فکر می‌کنم همه چیز برای آن‌ها خوب خواهد شد. آن‌ها کاری که باید انجام دهند را انجام خواهند داد زیرا ما می‌خواهیم این کار انجام شود
@withyashar</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/15694" target="_blank">📅 23:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15693">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سنای آمریکا به پایان جنگ با ایران رأی داد  سنای آمریکا تصویب کرد که ادامه عملیات نظامی علیه ایران مستلزم کسب مجوز کنگره است. @withyashar</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/15693" target="_blank">📅 23:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15692">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سنای آمریکا به پایان جنگ با ایران رأی داد
سنای آمریکا تصویب کرد که ادامه عملیات نظامی علیه ایران مستلزم کسب مجوز کنگره است.
@withyashar</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/withyashar/15692" target="_blank">📅 23:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15691">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کانال ۱۴ اسرائیل نقل قول‌های اختصاصی از احمد وحیدی، فرمانده سپاه پاسداران، خطاب به مقامات ارشد رژیم را منتشر کرد.
1 «ما رئیس جمهور ترامپ را به زانو درآوردیم. ما به آنچه می‌خواستیم رسیدیم. طبق معمول، غرب احمق فکر می‌کند که در عوض چیزی از ما دریافت می‌کند، که البته هرگز اتفاق نخواهد افتاد.»
2 «هدف ما در حال حاضر این است که آمریکایی‌ها را در تنگنا قرار دهیم. هرگونه تخلف، هر چقدر هم کوچک، به ما اجازه می‌دهد که تهدید به بستن تنگه هرمز کنیم و ترامپ و مردمش با هر چیزی موافقت خواهند کرد.»
3 «ترامپ فکر می‌کند پولی را که به ما می‌دهد صرف خرید کالاهای آمریکایی خواهیم کرد. این هرگز در طول عمر ما اتفاق نخواهد افتاد.»
4 «حالا باید به آمریکایی‌ها بفهمانیم که اسرائیل بازیگر بد خاورمیانه است. هدف این است.»
5 «از هیچ چیز دست نکشید. تهدید کنید. و در صورت لزوم، از مذاکرات کناره‌گیری کنید.»
@withyashar</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/15691" target="_blank">📅 23:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15690">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نخست‌وزیر پاکستان: هفته آینده با مجتبی خامنه‌ای در ایران دیدار خواهم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/15690" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15689">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">WarRoom with YASHAR
pinned «
دوستان، زیر چنل تبلیغاتی از افرادی می‌آید که در بازارهای مالی شرکت دارند. اینها از طرف خود تلگرام است. حتی اگر من هم تبلیغی بگذارم، دلیل برای این که شما جایی پولی پرداخت کنید و تایید من باشد نیست. به هیچ وجه این کار را در هیچ شرایطی در هیچ کجای اینترنت انجام…
»</div>
<div class="tg-footer"><a href="https://t.me/withyashar/15689" target="_blank">📅 22:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15688">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دوستان، زیر چنل تبلیغاتی از افرادی می‌آید که در بازارهای مالی شرکت دارند. اینها از طرف خود تلگرام است. حتی اگر من هم تبلیغی بگذارم، دلیل برای این که شما جایی پولی پرداخت کنید و تایید من باشد نیست. به هیچ وجه این کار را در هیچ شرایطی در هیچ کجای اینترنت انجام ندهید. در غیر این صورت مسئولیت با شماست و توسط حرص و طمع خود شما انجام گرفته. به این مسئله دقت کنید و
فقط از تحلیلها و مطالب آموزشی افراد استفاده کنید
. هیچ پکج یا هیچ پرداختی به هیچ بی ناموسی انجام ندهید.
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
از توجه شما به این مطلب سپاسگزارم، یاشار</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/15688" target="_blank">📅 22:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15686">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSyXYdfCNHETiWCqdvzyBQzo0mB9nSzofoMey4a1FQ15rEeZuchGP7GNRLhSQsF7ds227ZguzrWPnCel66PAYU5_kQQFprBCb6f4gyurBUo1BqXeZTvN6LzMTyEc1_XGwO33xNFOD2bDNm6Ee2qd_FmcrupqO4c5KVMxPwayXkgMsv-gBqAE20Ua0e1kuRdG0lgx11PQ8FxL-jdkjDEHPYIPqNYws3vwes5vyZ_6NFMWYNiG22mTyTkxA-au79vu0yU-LyN026J4r9D10RTPykYn0BQI7L-J0TE9mTg6DLcWHMoIMSOGLjaOS3IKjrWXO10qSW2FCzeWMMCAD54hfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه اسرائیل با انتشار نقشه تونل کشف شده جدید حزب الله نوشت:
حزب‌الله با حمایت مالی جمهوری اسلامی طی سال‌ها(صدها میلیون دلار) شبکه گسترده‌ای از تونل‌ها، انبارهای تسلیحاتی، سایت‌های موشکی و مراکز فرماندهی در جنوب لبنان ایجاد کرده ، هدف این زیرساخت‌ها حمله به اسرائیل بوده
@withyashar</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/15686" target="_blank">📅 22:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15685">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7644ffed31.mp4?token=aS4BnQnEPgUYW8udy6MC2XZRoYhHJFFXxvFUrm8z3Ee_cYx_q5QEwptC9BYN6JuevruE8FCzKy5D_DPibf9gy6qtBOSzaZ34xVvtZkCv5nj7Nc79xkzvzEN1uZ-WV5k2hH3pinnkQ8xBG6Mo2SPl3_C6jBAdEUpzKH8qgH5v9gCfBEXmGoqxnOB1O83RbfIpdyoWlXwUW2E9eTufzXjRrN73vlwO3CCLUeHoq0j_iqv0MMIHM4XCtJXQU1QHsbr2tKkhMxZn1uer2JEMwi3HnM60rHyc-eJWfNgSpTfPWFdXi1xV1twPc-ObcrD23vGAb2gK84Oixqfmk7-VjfaUSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7644ffed31.mp4?token=aS4BnQnEPgUYW8udy6MC2XZRoYhHJFFXxvFUrm8z3Ee_cYx_q5QEwptC9BYN6JuevruE8FCzKy5D_DPibf9gy6qtBOSzaZ34xVvtZkCv5nj7Nc79xkzvzEN1uZ-WV5k2hH3pinnkQ8xBG6Mo2SPl3_C6jBAdEUpzKH8qgH5v9gCfBEXmGoqxnOB1O83RbfIpdyoWlXwUW2E9eTufzXjRrN73vlwO3CCLUeHoq0j_iqv0MMIHM4XCtJXQU1QHsbr2tKkhMxZn1uer2JEMwi3HnM60rHyc-eJWfNgSpTfPWFdXi1xV1twPc-ObcrD23vGAb2gK84Oixqfmk7-VjfaUSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک یه ویدیو از محرم پست کرده
@withyashar</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/15685" target="_blank">📅 22:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15684">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7cLNzmXhNDLDIDi57_gyEgV-wjgjzpn0Bq_QxwlQrRf2NO8f1Wyu4R5fJsec0K2nbar4QP5Gq2qAvEuRDKEBR7-47WO41Lllw0nZft2UH6Vj0GOJVluP5v4FmhLoK3-Xct-tMk-sJR3GNWwQuqdEJU1eL_CPhr4MZ-W4sxnBGae8HTIfvq6T7SymrVlWeoQk7ZPTt6fzTt3bkCcVQz4svhZOklNtMjycEaZ10EWtV6i3uHD6AdRttg-FkkFoQbEUS0Szd9K451150eVLbHtMfZtQ2NMoUXFIX2EQt9cKYbvprLyb_2DyBb_6LwBVQFYburs2fYdPb6SY6EKcRnFUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مبینا محمدعلی‌پورثانی پس از ۱۰ روز پیدا شد
سیدامیر احمدی، دادستان عمومی و انقلاب بهارستان:
مبینا محمدعلی‌پورثانی، دختر ۱۹ ساله ساکن نسیم‌شهر، پس از ۱۰ روز بی‌خبری پیدا شد.
این دختر پس از پیگیری‌های قضایی و اقدامات انجام‌شده، پیدا شده و در سلامت کامل به سر می‌برد.
@withyashar</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/15684" target="_blank">📅 21:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15683">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل، در مصاحبه ای با شبکه سیان بی سی به وضعیت شکننده حکومت جمهوری اسلامی اشاره کرد و فروپاشی آن را اجتناب ناپذیر اما از نظر زمانی غیر قابل پیش بینی دانست.
وی با مقایسه شرایط کنونی ایران با وقایع تاريخي غير منتظره ای نظیر سقوط دیوار برلین و تحولات رومانی، تأکید کرد که شکاف های عمیق و پنهانی در زیر لایه های این نظام در حال گسترش است. نتانیاهو با بیان اینکه حکومت ایران در حال حاضر به شدت ضعیف شده است، تصریح کرد که اسرائیل همچنان بر موضع خود مبنی بر کمک به مردم ایران برای سرنگونی این رژیم پافشاری می کند؛ هر چند زمان دقیق وقوع این اتفاق در کنترل یا انتخاب آنها نخواهد بود و به روند گسترش این شکافهای داخلی بستگی دارد.
@withyashar</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/15683" target="_blank">📅 21:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15682">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ: هیچ عجله‌ای برای ورود بازرسان آژانس بین‌المللی انرژی اتمی به ایران وجود ندارد
@withyashar</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/15682" target="_blank">📅 21:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15681">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">رکورد تاریخی رونالدو در جام جهانی ۲۰۲۶ کریستیانو رونالدو با گلزنی مقابل ازبکستان در جام جهانی ۲۰۲۶، به نخستین بازیکن تاریخ فوتبال مردان تبدیل شد که در ۶ دوره متوالی این رقابت‌ها موفق به گلزنی شده است. این گل که در ابتدای بازی(دقیقه۷) به ثمر رسید، به انتقادها…</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/15681" target="_blank">📅 21:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15680">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رکورد تاریخی رونالدو در جام جهانی ۲۰۲۶
کریستیانو رونالدو با گلزنی مقابل ازبکستان در جام جهانی ۲۰۲۶، به نخستین بازیکن تاریخ فوتبال مردان تبدیل شد که در ۶ دوره متوالی این رقابت‌ها موفق به گلزنی شده است. این گل که در ابتدای بازی(دقیقه۷) به ثمر رسید، به انتقادها علیه این ستاره ۴۱ ساله پایان داد.
@withyashar</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/15680" target="_blank">📅 21:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15679">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خبرنگار : ایرانی‌ها می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
ترامپ: بلوف میزنن ، اونا داخل به ما گفتن و ما ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.
@withyashar</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/15679" target="_blank">📅 21:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15678">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ارسالی : یاشار جان بانک رفاه و سامان و بلو بانک هم از کار افتادند ، ساعت شش عصر
@withyashar</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/15678" target="_blank">📅 20:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15677">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26cd4a0fb.mp4?token=DcW4iI8TP3FihLCOgsAtT_5xWaTrF-oC1govTT6kQQNjTWd6KNX2rL0KJnRy6clCzr22-94Q1u99O25ywF9hxQmreBd-6efQrOY4QQVpOH03XiiN0muQah0BHyYRAVCjRh2o19gaeAaMe_gueU4kDjvcy5oBYU2s1IWAgQxUigTC5h2i384jOimeJuHqfWpGx_mpsglw1QrCwtJMio8oMZgCrB7kBTA_rJkz6YvcZYc9kIPSfUu61YRb_iHO9EnW-aWRLQ4yu5-edqAVPJMP6g-vZ8OWnWGw29LKMkP7PPvVykeyzZ0gCsNGIms5aNfyPfnykBAny6Sq0m09c0HLhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26cd4a0fb.mp4?token=DcW4iI8TP3FihLCOgsAtT_5xWaTrF-oC1govTT6kQQNjTWd6KNX2rL0KJnRy6clCzr22-94Q1u99O25ywF9hxQmreBd-6efQrOY4QQVpOH03XiiN0muQah0BHyYRAVCjRh2o19gaeAaMe_gueU4kDjvcy5oBYU2s1IWAgQxUigTC5h2i384jOimeJuHqfWpGx_mpsglw1QrCwtJMio8oMZgCrB7kBTA_rJkz6YvcZYc9kIPSfUu61YRb_iHO9EnW-aWRLQ4yu5-edqAVPJMP6g-vZ8OWnWGw29LKMkP7PPvVykeyzZ0gCsNGIms5aNfyPfnykBAny6Sq0m09c0HLhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان دکترای افتخاری از پاکستان دریافت کرد
@withyashar</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/15677" target="_blank">📅 20:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15676">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تتر 163K
@withyashar</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/withyashar/15676" target="_blank">📅 20:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15675">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/15675" target="_blank">📅 20:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15674">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vlt-Z5aqnE_4yBKJP6AjRWnTAYtIF5r73NXk7ZlgbzAVQtxlP4UTJDew8GeK4WMA4lS9oT7B-bNfPQkWWVSbZ741RHCTJ2KwsWuczBnD_BcJtRW_kB3_M4jq61SVuoTo7q_31iIPiE7Xecm7fGr9L0PiqMp7G07hblCHxBIg9pcLdBSg-4EgEHlR-twtz5-nsPqFw4y5vUt6NgpSPMCcBZE46aq-Hf__SaZBkhpjOnX7khfAG-r73z-sb9bwtTVp4TQIjO0Yla8WM7JWCdOxkkQ8Lo8QWCCZp8-412E6plTgZlqxnVuzfQ7uzBWVIcSsSU-UPJD2WktpSDyypCgGrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شواهد نشان میدهد مدیران دفتر انتشارات مجتبی خامنه‌ای دقیقاً امضای ابزار یکسان ، نسخه یکسان و سیستم عامل یکسان دفتر انتشارات قالیباف استفاده کرده اند.
در‌نتیجه هر دو نامه قالیباف و مجتبی خامنه ای با یک کامپیوتر نوشته شده در ابتدا و بعد از اوایل ماه ۶ میلادی، اوایل خرداد ماه، رایانه را از مک به رایانه ویندوزی تغییر داده‌اند.
@withyashar
پیشتر در ویدیو اتاق جنگ گفتم که ای آی دست ممباقر هست!</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/15674" target="_blank">📅 19:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15673">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ریاست جمهوری لبنان:
ونس و وزیر خارجه آمریکا خواستار تشکیل یک کار گروه آمریکایی، لبنانی و ایرانی برای تثبیت آتش‌بس شدند
آن‌ها گفته‌اند که ترتیبات مربوط به حوزه اختیارات این کمیته و نحوه تشکیل آن، در دست بررسی است
@withyashar</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/15673" target="_blank">📅 18:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15672">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">هاآرتص به نقل از منابع آگاه: تل‌آویو علاقه‌مند است در مذاکرات واشنگتن راه‌حل‌هایی پیدا کند که مداخلهٔ ایران را از تحولات لبنان دور نگه دارد.
@withyashar</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/withyashar/15672" target="_blank">📅 18:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15671">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4IbgHGZtAvuGFRMnUxmFMcWyyogHpUz0YcRmDo8H9QLZP9CAsXjsxkniWC6b8NRS9otMKXH4hqXncTf1NLZpkT-TUTiL4W-MzJXaK81jwJJAa1Bycc_Hj11NW62EJErCHHeGAQuBJD8_V_jH7f1CTvB5BVsHjRtqEf_zNwO3GVM2cQuVQdQLvkqXS8ewPx7p-KkXh1HqUwG2d7l4D4Hlznf-1-wOaj4zZb_POefkNdc9w0uBIST6UTYsnlXuA8YlgMR9sGMZ6jLCbeKtT3-aI0ENf9VCASyUj9SoEiY0ZXSbtqa8uzZQKmiQXoLGMivxuc_-gqnJuyEpuBWtH7T0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: ما هستیم ناو ها هم هستند نگران نباشید
ناو هواپیمابر USS جورج اچ. دبلیو. بوش (CVN 77) در دریای عرب(شمال‌غرب اقیانوس هند ابتدای دریای عمان جنوب ایران ) در حال حرکت است.
دو ناو هواپیمابر به فعالیت خود در خاورمیانه ادامه می‌دهند در حالی که نیروهای آمریکایی همچنان حضور دارند و هوشیار هستند.
@withyashar</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/15671" target="_blank">📅 18:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15670">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">عمان و ایران بیانیه مشترکی منتشر کرده‌اند که در آن قصد خود برای ایجاد یک مدیریت مشترک آینده برای تنگه هرمز را تأیید می‌کنند
این بیانیه همچنین به طور ضمنی تأیید کرد که مطابق با استانداردهای بین‌المللی
هزینه‌هایی برای خدمات دریایی اعمال خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/15670" target="_blank">📅 17:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15669">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فایننشال‌تایمز
:
با وجود افزایش سطح تردد کشتی‌ها در تنگه هرمز، مالکان همچنان سردرگم هستند؛ این وضعیت در حالی شکل گرفته که ایران کشتی‌ها را تهدید به عبور از مسیر نزدیک سواحل خود کرده و آمریکا مسیر عمان را پیشنهاد می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/15669" target="_blank">📅 17:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15668">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">هم اکنون حمله پهپادی هدفمند به خودرویی در جنوب لبنان،گزارش ها از ترور چندین عضو حزب الله.
@withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/15668" target="_blank">📅 17:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15667">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">شهباز شریف نخست وزیر پاکستان: مذاکرات ایران و آمریکا شامل دارایی‌های هسته‌ای، موشک‌های بالستیک و دارایی‌های مسدود شده ایران خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/15667" target="_blank">📅 17:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15666">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzn-TaOvCWUnOrNSy2KyFgj5q8TvYQeIOiYKJSPlZNLRs-P-J02AMaoAoDtZIuIgARSDTn8kV9SOUPRlwWGZqzvl3VhUVRxiWgoxIoZtKmS8VoO5OeEYod8xx4RSxxA5rsEhdvDXIvGH94d-Us-zMFixEWDVC1fkJymHCtfB4nYVhTa0NrzWExOC_AV0XuNJz6Jzxq9oM6mL0ULDQeejaKaedD78gqdbcgNYDF5YwwVIUjHbw0zUxHrzPLdIgDxqUkv8S-JKCYJ4nhJUGWnDdZ9GqQhZBDkxbi-DrL1V0OA5iLcQbGaByX7pon-4UHIkOx_WixMUPTVDMQGjVtbFFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز دایرکتی از طرف یکی از شما دریافت کردم که گفت از‌ کارمندان رتبه دار بانک است و این قطعی نه هک است نه چیز دیگری و به طور عمد از طرف خود رژیم انجام شده وی افزورد تقریبا با یقین میگم پایین اوردن دستوری قیمت ارز و طلا،حاکمیت و دولت با سرکردگی همتی و سیف میخواهند در قیمت های پایین فقط خودشون خریدار مطلق باشن و یک نوسان جانانه از بازار بگیرن با اختلال عمدی در سیستم(چون میدونن سرمایه دارها میدونن قیمت برگشت میکنه به بالا و پولشون رو میکشن بیرون که طلا بخرن،اما با قطع عمدی و به گردن هک شدن)
در نتیجه از دوستان هکر قدیمی دوران جوانی جوییا شدم که در امنیت سایبری بانکها کار میکنند. آنها به من گفتند که بعد از عملیات اکونومیک فیوری که آمریکا انجام داد که شامل محاصره دریایی هم میشود و تمام زیرساختهای اقتصادی رژیم را هدف‌ گرفت رژیم ضربه های مهلکی در رابطه با ارز خورده و این ادعا درسته و میخوان پول رو از جیب مردم جبران کنند دوستم گفت شعبه ها هم دسترسی به هر انتقالی را دارند ولی دستور این است که بگویند قطع هست
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/15666" target="_blank">📅 15:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15664">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6rYuIlzLvr0srlB5ppQ2idlT2cQfmZkFZNOopLbQl17kY01uoty0NtoQuLqfVWwnl3GNKm-Xakrd5bPqKEQsq2kALlQl_D6DgrVXUH8ZvzBs5VaB6Ggzuf--qdICQFJCayKLkg9zhit9uQoFH-_X6L_ILbmUSSgZ5cVnuMQJRv7LOslEtRvMqj944OW3Q_LKJSvXAhcW1BCJ07U-xxU3TVjhvsyTYny29MjmH_Rr9rNZTKqdyx4WIUgxbRMJ5Z8QlQiH5p-z7NiV21mNYsTagk4aS3jJCfwrhVagTHJjpECpxPqKzaidyCgWzuZtv3iUX-UqdWEpuqsyHrNQKi5wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلبان آمریکایی جنگنده F-15 که در ماه آوریل بر فراز ایران سرنگون شد، به مقام‌های اطلاعاتی گفته است که پیش از اجکت کردن، چندین پهپاد ایرانی را دیده که به‌صورت هم‌زمان و هماهنگ در آرایشی شبیه «عروس دریایی» در حال حرکت بوده‌اند؛ به گزارش سی‌ان‌ان و به نقل از چهار منبع.
این روایت باعث بحث در جامعه اطلاعاتی آمریکا شده درباره این‌که آیا ایران توانسته قابلیت پیشرفته‌ای در زمینه پهپادها یعنی «شبکه‌سازی مش‌مانند یک‌به‌چند» (one-to-many meshed networking) را به نمایش بگذارد یا نه.
@withyashar</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/15664" target="_blank">📅 15:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15663">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnO-srv2b03FarGEmlVVLPqDwjnmbUzbM079-ncFGKe48l5e_l127Q-2ewLq5toIuOvdyF3ZoAnqP5Evpinj9FlxmP2XWh0LUJqOomoXd3sb4xcTN5OuZiIPFvS_kz5y4_qJxRqT_pu8vu_Z2ZujdD5R2EgUIDpgy7XZzIM75Nua2qudj0OXa-_SKNl7an-lIgqikE0oyvxXgzX8VIVnWMbp73ybEbyft6JQb-bezLmyL1oBAuGahk0G8zr6Ss4yYFz3iO0kp6uDmzK-ac7Oj4uejKt0kPlV-W4FLJRUd_CsEg_Nd5RkYLrh-Lwqu7cA6wCNNSsGtvQHqoONTIZh7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : با وجود اعتراضات و اظهارات نادرست آنها، همراه با تبلیغات مکرر اخبار جعلی که همه تلاش خود را می‌کند تا پیروزی آمریکا را کوچک و بی‌اهمیت جلوه دهد، ایران به طور کامل و جامع با بازرسی‌های هسته‌ای در بالاترین سطح برای آینده‌ای نامحدود (بی‌نهایت!!!) موافقت کرده است. این امر «صداقت هسته‌ای» را تضمین خواهد کرد.
اگر آنها با این موضوع موافقت نمی‌کردند، مذاکرات بیشتری صورت نمی‌گرفت! بر اساس این و دیگر امتیازات عمده‌ای که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و هیچ محاصره دریایی بیشتری اعمال نشود. با این حال، همه کشتی‌ها در محل باقی می‌مانند تا در صورت لزوم محاصره دوباره برقرار شود، که در این مرحله بسیار بعید به نظر می‌رسد.
پول و یا تحریم‌هایی که خزانه‌داری آمریکا آزاد می‌کند، در حساب امانی تحت کنترل آمریکا قرار می‌گیرد و صرف خرید غذا و تجهیزات پزشکی، به طور انحصاری از ایالات متحده، از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما خواهد شد.
این‌ها چیزهایی هستند که ایران به شدت به آنها نیاز دارد. این یک بحران انسانی است و من احساس می‌کنم لازم است که اکنون کمک کنیم، قبل از اینکه خیلی دیر شود. مذاکرات به خوبی پیش می‌رود!
@withyashar</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/15663" target="_blank">📅 14:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15662">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLLVuVA5eIIULOEB-0fFKpbz5RdLslcqrDrEGnFoMmlW6ls_9xtArkO-eUOfo2A2hhLETT25IcBIyaGBw3LLcVcv9GOFHumo6Yk4Fv5yWd9pKRCALeAQk0AFZ8c1PxlLgT-CS3FiOVopwkSBqtj8cxzZcafah1K12w4Go08rCpk3l9eK9S0jC7R3444q7U3Q4tLq6hp7GyJ0sV4C14QqsFHes4FniNzi-5LTrIK8LaTKBKlPM_P-gst8jkLcLbRyooqKSccoAShKtVyzOzZ50QHk5noCB-Dv8HMi5WAQ4xQrJ5SzrRD1Ktnxsv8OdEtptuGEk8e3fkT4XLPbTJPx-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان وارد اسلام‌آباد شد
وی در بدو ورود با نخست‌وزیر پاکستان دیدار کرد.
@withyashar</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/15662" target="_blank">📅 14:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15661">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9264c7b6d7.mp4?token=eNkxVMgGlKx9SCMpx2u7yr4mk5Tj1t6PbXEf7dAYH-xt8u9RZ7laFQerxnKu_fLunHsB4I77ByAszACCZNwJwoNnptsgGpit_GRgR2yxeXoWX7iK1jV2O5EF9u9JH8KzbQwONawgnxqXpN-mbXaA1hYymnqrqnojbAHmm8SRoHJFUKUGeJt4wWwO3hu7jvD0t6dT2mQxn_YmqIZjD36o7tKxdlq52Bd5nrGfqwbPMSFliADpGQ4B7NX_Xt6Qyo9t4OPDs7k9cAdyhv3otB9uFu7Ay-9L7glPM5CbnE5wcgvT0bmnCvFWZmqv3YsLG1e6y8Vn3GO-hdxvHCkT-eJgXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9264c7b6d7.mp4?token=eNkxVMgGlKx9SCMpx2u7yr4mk5Tj1t6PbXEf7dAYH-xt8u9RZ7laFQerxnKu_fLunHsB4I77ByAszACCZNwJwoNnptsgGpit_GRgR2yxeXoWX7iK1jV2O5EF9u9JH8KzbQwONawgnxqXpN-mbXaA1hYymnqrqnojbAHmm8SRoHJFUKUGeJt4wWwO3hu7jvD0t6dT2mQxn_YmqIZjD36o7tKxdlq52Bd5nrGfqwbPMSFliADpGQ4B7NX_Xt6Qyo9t4OPDs7k9cAdyhv3otB9uFu7Ay-9L7glPM5CbnE5wcgvT0bmnCvFWZmqv3YsLG1e6y8Vn3GO-hdxvHCkT-eJgXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رژیم : هک شدیم ، داریم روش کار میکنیم و مشخص نیست کی‌ درست بشه ! شرکت خدمات انفورماتیک: تیم‌های فنی و متخصصان امنیت سایبری در حال رفع اختلالات ایجادشده هستند تا امکان بهره‌برداری دوباره از خدمات فراهم شود. ضمن عرض پوزش بابت وقفه پیش‌آمده در انجام امور بانکی،…</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/15661" target="_blank">📅 14:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15660">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رژیم : هک شدیم ، داریم روش کار میکنیم و مشخص نیست کی‌ درست بشه !
شرکت خدمات انفورماتیک:
تیم‌های فنی و متخصصان امنیت سایبری در حال رفع اختلالات ایجادشده هستند تا امکان بهره‌برداری دوباره از خدمات فراهم شود.
ضمن عرض پوزش بابت وقفه پیش‌آمده در انجام امور بانکی، از تمام کاربران و مشتریان محترم تقاضا می‌شود ضمن حفظ صبوری و شکیبایی، اخبار و اطلاعات تکمیلی در خصوص زمان بازگشت به وضعیت عادی را صرفاً از طریق درگاه‌های اطلاع‌ رسانی رسمی و مراجع ذی‌صلاح پیگیری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/15660" target="_blank">📅 14:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15659">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">روزهای شنبه و یکشنبه ۱۳ و ۱۴ تیر، تهران و دوشنبه ۱۵ تیر، کل کشور تعطیل است  معاون اول رئیس جمهور اعلام کرد در روز سه شنبه ۱۵ تیرماه استان قم و پنجشنبه ۱۸تیرماه استان خراسان رضوی تعطیل است. @withyashar</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/15659" target="_blank">📅 14:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15658">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">روزهای شنبه و یکشنبه ۱۳ و ۱۴ تیر، تهران و دوشنبه ۱۵ تیر، کل کشور تعطیل است
معاون اول رئیس جمهور اعلام کرد در روز سه شنبه ۱۵ تیرماه استان قم و پنجشنبه ۱۸تیرماه استان خراسان رضوی تعطیل است.
@withyashar</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/15658" target="_blank">📅 14:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15657">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سفیر ایران در لبنان در واکنش به حمله به جنوب لبنان: هرگونه نقض تفاهم‌نامه در لبنان، چالش‌هایی را برای روند مذاکرات صلح ایجاد خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/15657" target="_blank">📅 13:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15656">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اختلال دوباره در بانک‌ها
@withyashar
🚨</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/15656" target="_blank">📅 13:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15655">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dY0wmHxR3QNJTbbRtLm96304M9p8mYf6aiXOvpwXABVHRnYs1KdVE_4HcmsdmpTrxFSJDFVNeAP9sxqi6ZBacQTD6ae8R04bciwtgEx7yvvhnYJbtiUcT_1dAzNXpSjbqbojatIdobZ81A6qm8Cy3geHTkAzMu9pMtygpui_WlED84erDPkOJ5dB3ZZDEkMo1kexbuu4GA6YmgU0tN102iWbQATpmLRb9FGJZVe1mYBdicc-RVFazkYoFLul-Sed2nXUYP6RyBGuyWFXgZXHU61lU7-ZB9it1dLtTM1MEIb57fDypeqUSq9Mxh2TAfeebYw3azMruH8i_U-o8_x6Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقض دوباره آتش‌بس ،حمله اسرائیل به جنوب لبنان
@withyashar
🚨</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/15655" target="_blank">📅 13:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15654">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نتانیاهو: حمایت دوستان آمریکایی‌مان را بسیار ارج می‌نهم، اما نیازمند رهایی از وابستگی و ساخت یک نظام تسلیحاتی مستقل هستیم @withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/15654" target="_blank">📅 13:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15653">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">رادیو ارتش اسرائیل: تا زمانی که حزب‌الله کاملاً منحل نشود، از منطقه الشقیف در لبنان عقب‌نشینی نمی‌کنیم
@withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/15653" target="_blank">📅 12:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15652">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نتانیاهو: حمایت دوستان آمریکایی‌مان را بسیار ارج می‌نهم، اما نیازمند رهایی از وابستگی و ساخت یک نظام تسلیحاتی مستقل هستیم
@withyashar</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/15652" target="_blank">📅 12:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15651">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4MwcoIRf6Iu60hJmANfL7-2b2dn3UBOc2l0hN2D1-VRfGYLX3O6pnTEwPnCkGX0c0MmoxqwpWaU1ch7dvgA2DS52PxEEoyXzcx8g0j513pc3cEV1KXrZJZImgCIhJcRwbKCq_OPtK8wvGnHTbh4zMDMe70vnovDKPk6oizoP8G9KH4nYFVeEDCCXUgsTjcE4AdIWyud-e1ooGBgG9GM9rs2eB09_0CaJ9KS5a5w03C0X9Mfo0wmOrE7CEfj5tX0-ba4Y03jx4020a6h8HvEum9JrAn0MbfAxO1rFsQ5rxsK7-TfKxOXT9-zEbq26ZKef-EQMtsfW0T5KB0wSdXjIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکنون ۷ سوخت رسان شامل، ۵ فروند سوخت رسان KC-135R و ۲ فروند سوخت رسان KC-46A پگاسوس نیروی هوایی آمریکا در منطقه خلیج فارس فعال هستند.
همزمان، دو فروند KC-46A با نام عملیاتی BOBBY 81/82 از پایگاه RAF Mildenhall انگلستان به پرواز درآمده و برای الحاق به یک یگان جنگنده در حال عملیات‌اند.
همچنین بر‌اساس گزارشها پرواز CUBE 31 شامل چهار فروند جنگنده F-35 تفنگداران دریایی آمریکا در حال انجام مأموریت بوده و هماهنگی‌های عملیاتی و ارتباطی لازم را در جریان پرواز برقرار کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/15651" target="_blank">📅 12:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15650">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پلتفرم دریانوردی کپلر:
۳۶ کشتی دیروز از تنگه هرمز عبور کردند که این بالاترین میزان تردد در این تنگه از نخست مارس تاکنون است.
@withyashar</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/15650" target="_blank">📅 12:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15649">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">وزیر امنیت ملی اسرائیل بن گویر:
اگر آمریکایی‌ها فکر می‌کنند ایرانی‌ها برنامه هسته‌ای خود را رها خواهند کرد، آن را لغو می‌کنند و از تمام رویاهایشان برای نابودی دولت اسرائیل دست می‌کشند، بسیار ساده‌لوح هستند.
@withyashar</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/15649" target="_blank">📅 11:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15648">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ: خودروسازان آمریکایی تولید سلاح را آغاز خواهند کرد
رئیس جمهور آمریکا در کاخ سفید به خبرنگاران گفت: «آنها برنامه‌هایی برای تغییر کاربری کارخانه‌ها دارند. ما قصد داریم سلاح‌هایی از جمله موشک‌های پاتریوت، موشک‌های تاماهاک و موارد دیگر تولید کنیم.»
@withyashar</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/15648" target="_blank">📅 11:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15647">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">هواپیماهای سوخت‌رسان نیروی هوایی ایالات متحده پس از تخلیه از پایگاه هوایی العدید در قطر به دلیل جنگ ایران(یک روز قبل از جنگ)، به این پایگاه بازگشته‌اند. حداقل ۱۲ فروند در حال حاضر حضور دارند.
@withyashar</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/15647" target="_blank">📅 11:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15646">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بقایی: توانمندی دفاعی و موشکی ایران هیچگاه موضوع مذاکره با هیچ طرفی نخواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/15646" target="_blank">📅 11:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15645">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">الجزیره: «تغییری بزرگ» در سیاست آمریکا؛ ایران اکنون می‌تواند نفت خود را با قیمت کامل بفروشد
این اقدام صد‌ها میلیون دلار درآمد اضافی برای اقتصاد ایران به همراه خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/15645" target="_blank">📅 11:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15644">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مایک والتز، سفیر آمریکا در سازمان ملل:
جمهوری اسلامی ایران با بازگشت بازرسان هسته‌ای به ایران موافقت کرده و این اولین گام برای توافقی گسترده‌تره.
برخلاف برجام، این بار بازرسی‌ها باید در هر زمان و هر مکان ممکن باشه.
@withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/15644" target="_blank">📅 11:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15643">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">عماد الدین باقی: طبق بند 2 توافق ایران و آمریکا، از این به بعد شعار مرگ بر آمریکا یا سوزاندن پرچم این کشور و لگد کردنش تو مراسم‌ها و اجتماعات رسمی (مثل نماز جمعه) ممنوعه.
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/15643" target="_blank">📅 11:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15642">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">https://t.me/boost/withyashar
یه لول اومدیم پایین ایموجی کم شد لطفا اگر کاربر پرمیوم هستید بوست کنید و اگه نیستید از دوستانتون که هستند درخواست کنید بوست کنند</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/15642" target="_blank">📅 02:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15641">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">@withyashar
FPV  آتش بس و</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/15641" target="_blank">📅 01:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15640">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">@withyashar
شصت روز سنگین</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/15640" target="_blank">📅 01:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15639">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc8773aac7.mp4?token=FoCAUxtUBnSjpBXuUHnR7PpbczksUE1DqP-yvLaLJhSohuFiQUSnSVJiQvgMu7NkSoJEXjx03RecmteMi7-WahsC4KjQdQs6GoOK-5r1buSiI3I2AoEC6HaZZOe8shoJg-1a5RV9tsyZRyirs3gIpgcSXt7DXAHtOC5SiBhndeC73CqQcHXXOIu6012IU52UgTTtQJMnMWBpBwbr9L_fkOYfprvSmAnT4wcJJoIKHaPkHdtv_IRr1BLrFJQWgKzsP1eFQ4U5LO8we2ta_GP4WQInLAKQLtO1JzXm69UYjKSryz6PtxO_A-YlsNArpjDF2zhi-kCKvvqqD4r9EQR93Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc8773aac7.mp4?token=FoCAUxtUBnSjpBXuUHnR7PpbczksUE1DqP-yvLaLJhSohuFiQUSnSVJiQvgMu7NkSoJEXjx03RecmteMi7-WahsC4KjQdQs6GoOK-5r1buSiI3I2AoEC6HaZZOe8shoJg-1a5RV9tsyZRyirs3gIpgcSXt7DXAHtOC5SiBhndeC73CqQcHXXOIu6012IU52UgTTtQJMnMWBpBwbr9L_fkOYfprvSmAnT4wcJJoIKHaPkHdtv_IRr1BLrFJQWgKzsP1eFQ4U5LO8we2ta_GP4WQInLAKQLtO1JzXm69UYjKSryz6PtxO_A-YlsNArpjDF2zhi-kCKvvqqD4r9EQR93Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
آیا می‌توانید تضمین کنید که ایرانی‌ها از سود فروش نفت برای بازسازی ارتش خود استفاده نکنند و فقط برای دولت بعدی آماده شوند؟
ترامپ:
خب، آن‌ها قرار نیست این کار را بکنند، قربان. خواهیم دید، اما قرار است پول را برای خرید غذا برای مردمشان استفاده کنند، چون در حال حاضر مردمشان خیلی گرسنه هستند و آن را فقط از ما می‌خرند — ذرت، سویا.
تباید پول زیادی باشد. امیدوارم پول زیادی باشد.
@withyashar</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/15639" target="_blank">📅 00:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15638">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ: اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من آنچه باید انجام دهم را انجام خواهم داد
با یک تماس تلفنی میتوانم محاصره را برگردانم
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/15638" target="_blank">📅 00:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15637">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ: هیچ‌کس نمی‌خواهد رئیس‌جمهور ایران شود. @withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/15637" target="_blank">📅 23:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15636">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">قالیباف: اگر به سوئیس نمی‌رفتیم، هر لحظه خون بیشتری از مسلمانان و شیعیان لبنان ریخته می‌شد
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/15636" target="_blank">📅 23:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15635">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ: هیچ‌کس نمی‌خواهد رئیس‌جمهور ایران شود.
@withyashar</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/15635" target="_blank">📅 23:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15634">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خبرنگار: نتانیاهو می‌گوید نیروهایش لبنان را ترک نمی‌کنند
ترامپ: ما قرار است به این موضوع نگاهی بیندازیم. من یک حل‌کننده مشکل هستم؛ می‌توانم مشکلات را سریع حل کنم، از جمله با بیبی.
@withyashar</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/15634" target="_blank">📅 23:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15633">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ: «تا زمانی که ایران به ما احترام بگذارد نمی‌خواهم از واژه “ترس” استفاده کنم چون مناسب نیست تا وقتی به ما احترام بگذارد، ما هیچ مشکلی نخواهیم داشت.
ما کنترل کامل تنگه را در اختیار داریم.»
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/15633" target="_blank">📅 23:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15632">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">قالیباف در سفر به مسقط: در سوئیس توافق کردیم تا 12 میلیارد دلار پول مسدود شده ایران آزاد شود.
@withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/15632" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15631">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏زنده‌یاد⁧ مانوک خدابخشیان  ⁩: چه کسی می‌خوهد این رژیم را براندازی کند؟ چه کسی می‌خواهد پایه‌های این رژیم را اره کند؟
@withyashar</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/15631" target="_blank">📅 23:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15630">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/15630" target="_blank">📅 23:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15629">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">شبکه 14 اسرائیل که به نتانیاهو نزدیکه، مدعی شده ایران از یک «سلاح الکترومغناطیسی با فرکانس پایین» برای تأثیر گذاشتن روی تصمیم‌های ترامپ استفاده می‌کنه!   می‌دانم این حرف طوری به نظر می‌رسد که انگار از یک فیلم علمی‌تخیلی آمده، اما واقعاً وجود دارد و همین حالا…</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/15629" target="_blank">📅 22:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15628">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یک مقام ارشد اسرائیلی به کانال ۱۴ درباره لبنان:
امشب دوباره با ارتش اطمینان حاصل خواهیم کرد که دستورالعمل‌های کابینه برای هر مبارز روشن شده است
ارتش مجاز است هر تروریستی که در منطقه زرد شناسایی شده است و علیه هر تهدید واضح حتی فراتر از آن، ضربه بزند.
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/15628" target="_blank">📅 22:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15627">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وال‌استریت ژورنال:
ترامپ این هفته با رهبران پنتاگون و پیمانکاران بزرگ دفاعی دیدار خواهد کرد تا برای سرعت بیشتر تولید موشک و مهمات فشار آورد
@withyashar</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/15627" target="_blank">📅 22:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15626">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXVVXkNMzszsjtyYeJt0FA257rDdStJBNfRQtMA_7KC0Mntif9UK8xHGLcfqrP3nlokVc_nRXEsV9sL_S7e2xOh6wFiuJOQGkvxbOs1MvVdvXSdwWKlTrfpsqzCgGwryMMZp8wGsFeOsgwwHxkjXY1bbR4UiXug-nxRjIhno-c0IkZtdOq2caXyIRI9vA9GjyH8qXFGpBeTEnpy46qiEIKbhqZurnNETJd8s4w0j4_PxkNM3jEAXJ4BQTzhZq-HceoNLZP6GwpGsRFS8BQfLwv53hTAckweiK7e9LVoA4OZOTWm-Up7obsY5H5i2hQjJb1S5IHA5-J-gqrH4TBSu2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای ممباقر (هیئت جمهوری اسلامی) همکنون در مسقط عمان به زمین نشست.
@withyashar</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/15626" target="_blank">📅 22:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15625">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ونس معاون ترامپ لحظاتی پیش سوئیس را به مقصد آمریکا ترک کرد
@withyashar</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/15625" target="_blank">📅 21:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15624">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fe556e38.mp4?token=bN6cUlCi6u_Z0yrdi2ZXiXNXDHbED9FSGh3sHgQHGHOuwQzfwTyEOlmhyoFV8oYQV9sAlxjDw5rZcO6E1EfPMUXeVUB1Kdoa5wc_6Sdc_0tnjLqcMMQmU0MngZqoshLm4tAGniyFSNC4V30uLb3f3YYT-yIeVwW1D94s8IAnLin6_t6AfRBjOFM9Oijo1B_DfCMjajsqnQ-Td_xfOkG4j77J5wybKrI-Wcoj_dczlC5Kwjy7FUIGX58QkrTg6nFG7bVtNLfpIfIcp-p5ooevhfNmdN9v-MYYNaYC9pqH8lTQGqYvpJEf0IQbbSN_Vus4SCiDVZrP5aZas_ujpY2cBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fe556e38.mp4?token=bN6cUlCi6u_Z0yrdi2ZXiXNXDHbED9FSGh3sHgQHGHOuwQzfwTyEOlmhyoFV8oYQV9sAlxjDw5rZcO6E1EfPMUXeVUB1Kdoa5wc_6Sdc_0tnjLqcMMQmU0MngZqoshLm4tAGniyFSNC4V30uLb3f3YYT-yIeVwW1D94s8IAnLin6_t6AfRBjOFM9Oijo1B_DfCMjajsqnQ-Td_xfOkG4j77J5wybKrI-Wcoj_dczlC5Kwjy7FUIGX58QkrTg6nFG7bVtNLfpIfIcp-p5ooevhfNmdN9v-MYYNaYC9pqH8lTQGqYvpJEf0IQbbSN_Vus4SCiDVZrP5aZas_ujpY2cBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف با تقلید از ترامپ دم توالت هواپیما
: حاکمیت ملی لبنان بر تمامیت سرزمین خودش انشاله در این گفتگوها به نتیجه نهایی می‌رسد و تا به نتیجه نرسد، رهایشان نخواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/15624" target="_blank">📅 21:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15623">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3Ad5RbREmxZC58a5yiYkvUFvAQbKveo4DZTtlQWrDAJ7O3uyZh0QU7j4jJE30_rl3OlOSeAqGkW7aqH4TujDPETAkLGn9azCIYS7q4LuSTmu8PpzfZEotBwftGeS7Fw_Zlyycv4e-xADYtHf52rpZ8o7rZhM9FGBYoBRm2UNjqzD3iJouUe7fjpywPDitc1pIV9UMB7Bopu0DTaZIQiX9hXWkmueXeIAwSh-ifp_6s8aT2GXYJy8AZxL_R9NjOeedKrV3EJqmDaHXtk4p_SCxY_-ZPe5zbYucj3pO0bIIRcdLxq43eqVuCXVOQ49ngFX5VPkNTIC6mIbvaDucb5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : همه کاملاً آگاه هستند که ایران برای تضمین «صداقت هسته‌ای» در آینده، با بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد. رئیس جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/15623" target="_blank">📅 20:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15622">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">شبکه 14 اسرائیل که به نتانیاهو نزدیکه، مدعی شده ایران از یک «سلاح الکترومغناطیسی با فرکانس پایین» برای تأثیر گذاشتن روی تصمیم‌های ترامپ استفاده می‌کنه!
می‌دانم این حرف طوری به نظر می‌رسد که انگار از یک فیلم علمی‌تخیلی آمده، اما واقعاً وجود دارد و همین حالا هم در حال استفاده است , این امواج رو داخل مغز ترامپ فرستادن. رفتار رئیس‌جمهور به‌وضوح تغییر کرده. چیزی شبیه تله‌پاتیه، اما از نوع الکترومغناطیسی.
روسیه این فناوری رو داره، چین هم داره و ایران هم بهش دست پیدا کرده.
باور کنید یا نه، از من خواسته‌اند این کار را انجام دهم و من هم روی آن کار می‌کنم
@withyashar</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/15622" target="_blank">📅 20:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15621">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مرندی: ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی به ایران صورت نگرفت. تبلیغات غربی را نادیده بگیرید
@withyashar</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/15621" target="_blank">📅 20:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15620">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">شاهزاده رضا پهلوی در اکس : در حالی که فیفا تلاش می‌کند پرچم شیر و خورشید را از ورزشگاه‌ها دور نگه دارد، هزاران ایرانی در ورزشگاه سوفای ثابت کردند که نماد واقعی ایران را نمی‌توان ممنوع کرد.
دفتر شاهزاده پهلوی افزود صدای مخالفان جمهوری اسلامی در جام جهانی بیش از هر زمان دیگری شنیده می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/15620" target="_blank">📅 18:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15619">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تکذیب تعهد جدید هسته‌ای از سوی بقائی
سخنگوی وزارت امور خارجه:
تعامل ایران با آژانس بین‌المللی انرژی اتمی طبق روال جاری و منطبق با مصوبات قانونی ادامه می‌یابد.
بنا بر اعلام منابع مطلع، در مذاکرات ۱۸ ساعته دیروز در سوئیس، هیچ مذاکره‌ای درباره پرونده هسته‌ای انجام نشده و تعهد جدیدی از سوی ایران پذیرفته نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/15619" target="_blank">📅 18:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15618">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">طبق اخبار درز کرده این معافیت تحریمی نفت ایران در ازای بازرسی آژانس از تأسیسات هسته‌ای ایرانه.
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/15618" target="_blank">📅 18:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15617">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نتانیاهو: تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهیم ماند
@withyashar</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/15617" target="_blank">📅 17:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15616">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وزارت خزانه‌داری ایالات متحده رسماً معافیت تحریم ۶۰ روزه‌ای برای نفت، محصولات پتروشیمی و گاز ایران صادر کرده است
این معافیت اکنون تا ۲۱ اوت معتبر است و ممکن است تا زمانی که مذاکرات ادامه دارد و توافق نهایی حاصل شود، تمدید شود.
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/15616" target="_blank">📅 17:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15615">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeSfT3sfRgUOk8y4wPYmNdTlNcedUDx2QSaSsFIKOTW7vaC5g_0f7Zz8z7gkB_wxoBt9LlHYUcXXVqICSmp72J2ix-bwSD40ldddm_UjfOM6xSW2USy801_7Pp4xkictu48Vy4YkCSD-LkxEl-D5lycFnErHCWwzgpYfq6PIb5ECFjcVfv2PnSn3ouljzhE31ciVLPTkkqpkvKTv9i52dA6BCGwna5TYsYynfF7Tpt9yqNYVv6Dmui_9tW5c02kkCMNxdF26dZgMDpmmLT1RGlkz1tW4JjYaTgxCdRniGhRM9OseebjP31FAFmwL8w2CdB1L4JZyAlUXgQF42vJyYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان بمباران توپخانه اسرائیل منطقه المشعع منصوری و منطقه بیوت السیاد در جنوب لبنان را هدف قرار داده است.‌‌
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/15615" target="_blank">📅 17:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15614">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فاکس نیوز: ایران متعهد شده است که به آژانس بین المللی انرژی اتمی و بازرسانش اجازه دهد تا به ایران بازگردند تا بر روی مکان یابی و برچیدن تاسیسات هسته ای کلیدی کار کنند.
معاون رئیس جمهور ونس توانست به چارچوبی دست یابد که از بودجه مسدود شده ایران برای خرید محصولات کشاورزی آمریکا برای ایران استفاده کند و این محصولات شامل سویا، ذرت و گندم آمریکایی است.
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/15614" target="_blank">📅 17:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15613">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">العربیه:وزارت خزانه‌داری آمریکا مجوز عمومی‌ای صادر کرد که اجازه می‌دهد واردات نفت خام ایران به مدت دو ماه انجام شود
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/15613" target="_blank">📅 16:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15612">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">طوفان در راه تهران
سازمان مدیریت بحران: مناطق نیمهٔ جنوبی، غربی، مرکزی و ارتفاعات تهران در معرض وزش بادهای شدید و گاهی بسیار شدید قرار دارند و احتمال وقوع طوفان در این مناطق از اواخر امروز تا روز پنجشنبه بسیار زیاد است.
@withyashar</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/15612" target="_blank">📅 16:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15611">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72fc6efcdb.mp4?token=GwjxZiR-hayLehjzgqS19QsdYweWIY6uRXNsAk58LLYUWKFqEIXc-1QxfBoU6GVju_l1dHmcQVxLSSz5hw0eIpvGbzu1Y_bQSrU7d17HPNL32QJIa3rzBlD8DrhrFGuaYMqI8Mm-XuapOX0mSJ22dfNYTE3PlwQSqeOB1m0-imahodJlbG5uzasydTbYSsWrtOpVczUvHdIt1-Nb0BVqiewpm6xBCPJUreYxWIKgRCCvCdykS0_szRFxFGF7wPYSlmpJnkXB3iN7JdZo1XvrzSla0o60ZAhyuyNdWoMjUsuQMr2PqGht7iDCFhHiSbXgDjJkDn1GGxQ4UCEelXTbIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72fc6efcdb.mp4?token=GwjxZiR-hayLehjzgqS19QsdYweWIY6uRXNsAk58LLYUWKFqEIXc-1QxfBoU6GVju_l1dHmcQVxLSSz5hw0eIpvGbzu1Y_bQSrU7d17HPNL32QJIa3rzBlD8DrhrFGuaYMqI8Mm-XuapOX0mSJ22dfNYTE3PlwQSqeOB1m0-imahodJlbG5uzasydTbYSsWrtOpVczUvHdIt1-Nb0BVqiewpm6xBCPJUreYxWIKgRCCvCdykS0_szRFxFGF7wPYSlmpJnkXB3iN7JdZo1XvrzSla0o60ZAhyuyNdWoMjUsuQMr2PqGht7iDCFhHiSbXgDjJkDn1GGxQ4UCEelXTbIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترافیک قابل مشاهده در تنگه هرمز نشان می‌دهد که حداقل ۲۴ کشتی در ۲۴ ساعت گذشته عبور کرده‌اند که همه آنها به جز یک کشتی با استفاده از طرح تفکیک ترافیک ایران قابل مشاهده بودند. به احتمال زیاد تعداد عبور و مرورها بیشتر از آنچه نشان داده شده است ، زیرا بعضی کشتی‌ها سیستم شناسایی خودکار خود را برای عبور خاموش  می کنند
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/15611" target="_blank">📅 16:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15610">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">معاون رئیس جمهور آمریکا ونس: ایران با ورود بازرسان هسته‌ای در این هفته موافقت کرد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/15610" target="_blank">📅 16:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15609">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1OSuVj52V9oIvcFUd7NTMViPr-Gj6qY1oyVyOxYgMutvEsbvhCWzjkzFysPSthBkx9WWy2V8lsvenrjutHCKqpfnoPUAwdoLcXDnUd5C6qNqeYge9oDR8rLCxpgOebBAxp76goSsHK_VuPJ_UU7FeJwAlq-Fmjy5eleWbaYg_d7i7TNAcDgJ7S6AxCN2wQdM2cBwEs38tSlvWCplINFZXg-RJ0alaQtj_Hb2TuWAGJwiP_kFcSn5bPUXWm0wLQuujFIZYliGxD95Ea9_Swfyzdbm7ruibfh4A6kXZM35pSfYtAPqQTwl3qjdRcSMMnV5LOWASUorJCZnIFmKIno1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : یا هر روز به جون هم میفتیم و به هم فحش میدیم و جونیمون میره یا همه باهم متحد میشیم و این وضعیت رو تموم میکنیم
@withyashar</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/withyashar/15609" target="_blank">📅 15:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15608">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47d6b1d15d.mp4?token=h7KaIyAS81f0EtkdQlSU2LHDilemDHy313KlyqjZu_QDJR4PT0Jp7F5SDsXvGH0dT1jLDSyea9u_zr-nSbrE13ct1Cxl0NtwbXTUkXuZtGyDNfv8rcn4bWVeyDCSclVEuSUBPHxUehgzWFU9sQUhG1Nujwp9TP9VSliA5zD4Hl6ncLDUvzNKnGNqZFvkhohkca7UkYRNT13QcSQ2JnTaHG6gaz-VlBRn3xSVgvxOc9dFC5C3AbIxCiAcIb9k0x9bNCFn4XqVP9x4_HgzVwVvoICygsIiorxBOZfF-HKLLVL1KF1lHHhWdS4MZGbFidSBdM_5xhyNIZNQe3onvcbTNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47d6b1d15d.mp4?token=h7KaIyAS81f0EtkdQlSU2LHDilemDHy313KlyqjZu_QDJR4PT0Jp7F5SDsXvGH0dT1jLDSyea9u_zr-nSbrE13ct1Cxl0NtwbXTUkXuZtGyDNfv8rcn4bWVeyDCSclVEuSUBPHxUehgzWFU9sQUhG1Nujwp9TP9VSliA5zD4Hl6ncLDUvzNKnGNqZFvkhohkca7UkYRNT13QcSQ2JnTaHG6gaz-VlBRn3xSVgvxOc9dFC5C3AbIxCiAcIb9k0x9bNCFn4XqVP9x4_HgzVwVvoICygsIiorxBOZfF-HKLLVL1KF1lHHhWdS4MZGbFidSBdM_5xhyNIZNQe3onvcbTNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسایی : یا در مجلس را باز می کنند یا جلوی مجلس جلسه برگزار می کنیم مردمم ببینند
@withyashar
🤣</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/15608" target="_blank">📅 15:37 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
