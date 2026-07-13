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
<img src="https://cdn4.telesco.pe/file/q7btbIWmJNxPbtsN00J1Zi4cY88SLk0JgU9gtsLuXRYDwwFk70wZuIGYEgyrpU9vpA_FCzMyi9qCVlXIHJzuKj8hTg9qZR4FkvR4maYaRdBEZQnbRtA9arG80gXUDj53vasPCUtLUU2ApBzXfnYvH9AyMUKaikeGFwyIFB2lv1QAMmC_23flN-xjvYaExg9ASNsThwCVom0bY8xChVdNU31d9HoMdM3jme67LFfYwphT3CV6iUFqYlSleg9wSCiWJ0o4uAw8WN2Gv7Uz4BBYSPkRwV7tSqRNxeebqHurVgkBwJqNrbatu-Griaygm7jH-CqdCQ6JQ4vPSfphSWhVUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.39M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 08:01:41</div>
<hr>

<div class="tg-post" id="msg-670409">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/369f15ca68.mp4?token=sMyh8WEcrP8xs5JlNn_XkRmvrfGbsF5icp_nUUBy6zf5nPNunbwNv--L_t4HxYIO8G72qTfC7p6oNd6jP78TByh4EDFD2RUJ1yUyHm9Q7K-O88oS-xgY3fwMM3_M8-LbR76kH3u1jb17y3fE_PA8rOE7vDbEXjU9ooiXk64936Gc5Z9fVPCvL5WvrnskbVk-j-qPHGTAbV1ZJUOZmqqtZdJJmcxJTiATvAPd6GaGeNkOruir1DnXct9wxjqBCyP2qdpB_knDEJ-aZOAbGrTB_CopVOJ_nC49m009zDqNdG4w0gXWcrPf74fuW7nfxmB08JRJKJ5vhJXbeTlVy75v0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/369f15ca68.mp4?token=sMyh8WEcrP8xs5JlNn_XkRmvrfGbsF5icp_nUUBy6zf5nPNunbwNv--L_t4HxYIO8G72qTfC7p6oNd6jP78TByh4EDFD2RUJ1yUyHm9Q7K-O88oS-xgY3fwMM3_M8-LbR76kH3u1jb17y3fE_PA8rOE7vDbEXjU9ooiXk64936Gc5Z9fVPCvL5WvrnskbVk-j-qPHGTAbV1ZJUOZmqqtZdJJmcxJTiATvAPd6GaGeNkOruir1DnXct9wxjqBCyP2qdpB_knDEJ-aZOAbGrTB_CopVOJ_nC49m009zDqNdG4w0gXWcrPf74fuW7nfxmB08JRJKJ5vhJXbeTlVy75v0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمرینات مفید برای تقویت زانو
🦵
🔹
زانو همیشه مقصر نیست؛ گاهی فقط اولین جاییه که دردش رو احساس می‌کنی. #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4 · <a href="https://t.me/akhbarefori/670409" target="_blank">📅 08:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670408">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
سپاه: پایگاه موشک‌های زمین به زمین ارتش کودک‌کش آمریکا در کویت به دست رزمندگان نیروی زمینی سپاه منهدم شد
روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
وَقَاتِلُوهُمْ حَتَّىٰ لَا تَكُونَ فِتْنَةٌ وَيَكُونَ الدِّينُ كُلُّهُ لِلَّهِ
🔹
به استحضار ملت شریف ایران می‌رسانیم؛
در چهارمین مرحله از عملیات مقابله به مثل، رزمندگان نیروی زمینی قهرمان سپاه، پایگاه موشک‌های زمین به زمین ارتش کودک‌کش آمریکا در کویت را هدف قرار دادند و دو سکوی موشکی "های مارس" و زاغه‌های مملو از موشک را به آتش کشیده و به طور کامل منهدم کردند.
إِنْ تَنْصُرُوا اللَّهَ يَنْصُرْكُمْ وَيُثَبِّتْ أَقْدَامَكُمْ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/akhbarefori/670408" target="_blank">📅 07:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670407">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هرمز؛ جایی که باید برای ایران ایستاد
🔹
بی‌تردید هیچ انسان خردمندی دل در گرو جنگ ندارد. جنگ، هر اندازه هم که در ظاهر با پیروزی همراه باشد، در عمق خود زخم‌هایی بر جای می‌گذارد که سال‌ها بر پیکر ملت‌ها باقی می‌ماند.
🔹
از همین رو، صلح همواره مطلوب‌ترین مسیر برای ملت‌هاست. صلحی پایدار و محترمانه، نه صلحی که بر پایه فشار، تحمیل و توافقات یک‌طرفه شکل گیرد.
🔹
حالا سوال اینجاست؛ وقتی آمریکا به تعهدات خود پایبند نیست و خواهان توافقی نابرابر است، آیا باید از حقوق و منافع ملی خود چشم‌پوشی کنیم؟
🔹
واقعیت آن است که یکی از اهداف راهبردی آمریکا، کاهش اهمیت ژئوپلیتیکی تنگه هرمز برای ایران است. تنگه‌ای که نه‌تنها یک گذرگاه دریایی، بلکه بخشی از هویت راهبردی و قدرت ملی ایران به شمار می‌رود.
🔹
تنگه هرمز امروز یکی از مهم‌ترین ابزارهای قدرت‌نمایی ژئوپلیتیکی ایران در منطقه است. اگر این جایگاه تضعیف شود، مسیر فشار بر ایران و محدود کردن توان چانه‌زنی کشور هموارتر خواهد شد.
🔹
از این رو، دفاع از جایگاه راهبردی تنگه هرمز صرفاً یک مسئله نظامی نیست، بلکه دفاع از امنیت، استقلال، عزت ملی و آینده ایران است.
🔹
ما مردمی هستیم که تاریخ‌مان با مقاومت، غیرت و پاسداری از سرزمین گره خورده است.
🔹
حفظ تنگه هرمز، حفظ بخشی از اقتدار ایران است، اقتداری که باید با عقلانیت، تدبیر و وحدت ملی از آن صیانت شود.
#سرمقاله
@Tv_Fori</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/akhbarefori/670407" target="_blank">📅 07:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670406">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOPdDKUYqjWVYUk_WPgqBQ4ZceaH3l2QKu3Yx4r4rOXaB_SVdZ6ElC0beS2rf8eU77oqrSubbge94BMMlukNu2eGVOwM2jQBCdgP67EJtXNDxh0YDmjKdY6I4OR-eqW4qgf5qVUYsUmHJqidBefcaDRwg4iqYc_FFIVW5YXi3WIllqC15kSYADN-KwcwfaFRfLzMcsJKWpB64AwIgX1aBT6Xio59dHv3c126lWnqARzEiDs5i8EHN1vaKT51oHMxCvexOoclO6LbyLQddLp1ZuMHTAx4eLh5NCEcCMYuR4is8d-ShL8eX2Z_79ZXKIOh10eeDm4whhfHaJQiSH2lyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رفتار آمریکا در برابر ایران چطور تغییر می‌کند؟
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/akhbarefori/670406" target="_blank">📅 07:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670405">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
گرما فعلا ماندگار است
هواشناسی:
🔹
از امروز دوشنبه تا چهارشنبه در اکثر نقاط کشور جوی آرام پیش‌بینی می‌شود و تا پایان هفته ماندگاری هوای گرم ادامه داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/akhbarefori/670405" target="_blank">📅 07:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670404">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
توزیع کارت آزمون کارشناسی ارشد ۱۴۰۵ از امروز آغاز شد
🔹
داوطلبان در صورت مشاهده مغایرت در کارت ورود به جلسه خود می توانند از امروز تا ۲۶ تیر از طریق درگاه اطلاع‌رسانی سازمان سنجش ویرایش کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/670404" target="_blank">📅 07:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670403">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIIZMoeG-RqQTONPy8ZyC1htiJA3KmbVnPEF9SVm9108u_aCcmgKcbovn1PIdeSezwBfhTV9mLYVe9kPmenAmUXcrboHuCH5JGqEhBInY19Lkh2e486vXIDyu0MTQ8dH3LeTQdpO_WpoEYtICi36ZvTWysLoPv9C5WwqJHveegeRzgddwhz8y1etk1x-80KSTY_SLPEy7ArZv7lSZdYRiBBGW4dVWRA7Gw32T6_krZyCHT0rk5nERDLC16C-GcbUsDkmrDNHtS3diBjKmKxlnGZfnJUVDFh0WkEAFLLnYxG1qKwUBPiGKBD25Mtjqb1NbWGc9X7OfYGiZk606Uxfow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۲۲ تیر ماه
۲۸ محرم ‌‌۱۴۴۸
۱۳ جولای ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/670403" target="_blank">📅 07:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670402">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
صدای مجدد انفجار در کویت
🔹
منابع خبری از شنیده شدن صدای انفجارهای شدید در پایگاه نظامیان ارتش تروریستی آمریکا در کویت خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/670402" target="_blank">📅 07:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670401">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c79f83d14.mp4?token=UJcwRJvd1PS0mdqbQBlv7TJ1g5XXyqrvAMHpYZnppqUJWpehKy-nZz4cE2NnGMkhtX1GVoXcim6Wdm_kJCeq6JgMsPh21qji3struvN1TGzEueLkQznbvyUCCQEey2nXEiMzKr18a1fpDwhNmJpB6JH9gGRFaDbOAtxT0D3C0WNgUA-Er7MZ3Lt7kC6YWnRUODg09FqYPbNYpDulYpFAkl24BfqbY4SjYCi2FiAbmvoOiErEIzKrzWS9VH4cpULOMA917XvbJM7Zjm1_MnedEG_Z5gZ1tgDK8LILaTOXfFfWYAvYEae2vHmidlqU0EP7FLp1UgUvNaTfH5NQyixWKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c79f83d14.mp4?token=UJcwRJvd1PS0mdqbQBlv7TJ1g5XXyqrvAMHpYZnppqUJWpehKy-nZz4cE2NnGMkhtX1GVoXcim6Wdm_kJCeq6JgMsPh21qji3struvN1TGzEueLkQznbvyUCCQEey2nXEiMzKr18a1fpDwhNmJpB6JH9gGRFaDbOAtxT0D3C0WNgUA-Er7MZ3Lt7kC6YWnRUODg09FqYPbNYpDulYpFAkl24BfqbY4SjYCi2FiAbmvoOiErEIzKrzWS9VH4cpULOMA917XvbJM7Zjm1_MnedEG_Z5gZ1tgDK8LILaTOXfFfWYAvYEae2vHmidlqU0EP7FLp1UgUvNaTfH5NQyixWKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو مربوط به آتش‌سوزی در پایگاه دریایی امریکا در بحرین پس از حمله موشکی پهپادی ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/670401" target="_blank">📅 07:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670400">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
گزارش‌های رسانه‌ای حاکی است که مقر یکی از شرکت‌های تجاری آمریکایی در بحرین هدف قرار گرفت و در آتش می‌سوزد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/670400" target="_blank">📅 07:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670399">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
صدای مجدد انفجار در کویت
🔹
منابع خبری از شنیده شدن صدای انفجارهای شدید در پایگاه نظامیان ارتش تروریستی آمریکا در کویت خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/670399" target="_blank">📅 07:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670398">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/524db81262.mp4?token=LQvkLulY4KQPklUU8tYmaveYMXM-JxkkqBv6v9t1FQsFrQ77KCdiJeXDJ9GVYuaYh0TNVYVJoZCnghGaPUaFBsXzhcwMlUom4lFKNlnP3gxN4mxw6P7kjOleldckmwVTG0Joa0cyxBR6iajnX2FM2NySsZFY0VYVdB3_sw8MwXDbYiLf47QQwo8HaKOu8H53dtwG8JM6hk6ykjGXH-6JDeft1Zi1hlbZVZxMeZHNzaU_pLQhlJrBaIxmYGWAUx5wUElh5cMo2LP-ac6BCiKil1k1ZKtd3RhPhguisL7RUkehmeaJn_81xTSTVtuupUCAMdo1wqGdZjVawGnFgtmtWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/524db81262.mp4?token=LQvkLulY4KQPklUU8tYmaveYMXM-JxkkqBv6v9t1FQsFrQ77KCdiJeXDJ9GVYuaYh0TNVYVJoZCnghGaPUaFBsXzhcwMlUom4lFKNlnP3gxN4mxw6P7kjOleldckmwVTG0Joa0cyxBR6iajnX2FM2NySsZFY0VYVdB3_sw8MwXDbYiLf47QQwo8HaKOu8H53dtwG8JM6hk6ykjGXH-6JDeft1Zi1hlbZVZxMeZHNzaU_pLQhlJrBaIxmYGWAUx5wUElh5cMo2LP-ac6BCiKil1k1ZKtd3RhPhguisL7RUkehmeaJn_81xTSTVtuupUCAMdo1wqGdZjVawGnFgtmtWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کنایۀ خبرنگار آمریکایی به وداع با سناتور جنگ‌طلب فقط با یک گل!
🔹
یک خبرنگار آمریکایی در مقایسه مراسم باشکوه تشییع پیکر مطهر رهبر شهید با مرگ سناتور جنگ‌طلب آمریکایی، با انتشار فیلمی از خانۀ او نوشت: آمریکا ۳۵۰ میلیون نفر جمعیت دارد، اما تنها چیزی که نصیب این فرد شد یک دسته گل کوچک مقابل خانه‌اش بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/670398" target="_blank">📅 07:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670397">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ادعای سنتکام: حملات جدید به ایران تکمیل شد
ادعای سنتکام یکشنبه شب به وقت محلی برابر با صبح دوشنبه به وقت تهران: نیروهای
🔹
آمریکایی با استفاده از مهمات دقیق، ده‌ها هدف را در چندین نقطه هدف قرار دادند تا توانایی ایران برای ادامه حمله به کشتی‌های بین‌المللی در حال عبور از تنگه هرمز را کاهش دهند.
🔹
در این حملات، سامانه‌های پدافند هوایی، سایت‌های راداری ساحلی، توانایی‌های موشکی و پهپادی و همچنین شناورهای کوچک نظامی ایران با استفاده از جنگنده‌های آمریکایی، شناورهای نیروی دریایی، پهپادهای یک‌طرفه هوایی هدف قرار گرفتند.
🔹
نیروهای آمریکایی برای نخستین بار از شناورهای بدون سرنشین یک‌طرفه دریایی استفاده کردند./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/670397" target="_blank">📅 07:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670396">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e107caf93.mp4?token=mOxB_sjit0fbIsyyZmCQdWAYdIKp53jc0Vml4Ml3Sy5yvAN5bivassKDdnkpilQ1i0fOeWToq7EkByhDDrWTOQruDqoTA3jXLb8yP1gX3IXwNSR9yEW36FKcC1Ejao4S3hHv8p6qfCgB8O88jYLVRlDKGX7c_MVZLnVJrhvU89Y_EG7eV3AGRzq628Vccj8Kgu6rlc0FoB5iKJN_K98PpkdPOJVV6BsL1e7bDYbqu-nXswv1IyHKjZfov7PMHk6WDthM3jym1goxgtmc0OJJ2xsZtNGFxsH50CNHVQkN-0AwKhp24NJ_XDi2bDKQ7EbVj4FHrezasDGiOvRt4y-e0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e107caf93.mp4?token=mOxB_sjit0fbIsyyZmCQdWAYdIKp53jc0Vml4Ml3Sy5yvAN5bivassKDdnkpilQ1i0fOeWToq7EkByhDDrWTOQruDqoTA3jXLb8yP1gX3IXwNSR9yEW36FKcC1Ejao4S3hHv8p6qfCgB8O88jYLVRlDKGX7c_MVZLnVJrhvU89Y_EG7eV3AGRzq628Vccj8Kgu6rlc0FoB5iKJN_K98PpkdPOJVV6BsL1e7bDYbqu-nXswv1IyHKjZfov7PMHk6WDthM3jym1goxgtmc0OJJ2xsZtNGFxsH50CNHVQkN-0AwKhp24NJ_XDi2bDKQ7EbVj4FHrezasDGiOvRt4y-e0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دود و آتش در پایگاه‌های آمریکایی در بحرین
🔹
در پی حمله به اهداف نظامی آمریکا در بحرین دود آسمان مناطق این کشور فرا گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/670396" target="_blank">📅 07:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670395">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
وزارت کشور بحرین: آژیرهای خطر برای دومین بار در کشور به صدا درآمدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/670395" target="_blank">📅 07:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670394">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
روایت متفاوت جواد موگویی از تشییع رهبر شهید انقلاب در عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/670394" target="_blank">📅 06:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670393">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
صدای دوباره آژير خطر و انفجار در بحرین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/670393" target="_blank">📅 06:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670392">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/997573ae21.mp4?token=ZgVlfS5QVGIusFyhbFXKcgKoWW5f9_s5bVg8Hx7LQ_jlWJMnTqwFeN5h2ExnL1KkQJWlnMgEUqpelSxWa_zsYXJvtgXcTCG6T-LYIzlietxwh6LDD7DzLi8LPE8b_M5yK4qcAS5c5FKRhwUQDYun6OGQR3oxcLX1UYrq_VYgzf9bYwQGqrQCzQ-1MPUOR1piNN94_iHiUUHlnrlrXZL3Yz6LnMbTbIT9JcSefKfVGpkfB3dSbxKxBKIl5pIrvj1y5dsrsHMt3DyZH53VXVSEDEs_pmqzWMe4fDJ6jzkcBFxHHlc_DU8V-DIhP_RhhCVoZJuYyKFvfFB4EGnQEohKvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/997573ae21.mp4?token=ZgVlfS5QVGIusFyhbFXKcgKoWW5f9_s5bVg8Hx7LQ_jlWJMnTqwFeN5h2ExnL1KkQJWlnMgEUqpelSxWa_zsYXJvtgXcTCG6T-LYIzlietxwh6LDD7DzLi8LPE8b_M5yK4qcAS5c5FKRhwUQDYun6OGQR3oxcLX1UYrq_VYgzf9bYwQGqrQCzQ-1MPUOR1piNN94_iHiUUHlnrlrXZL3Yz6LnMbTbIT9JcSefKfVGpkfB3dSbxKxBKIl5pIrvj1y5dsrsHMt3DyZH53VXVSEDEs_pmqzWMe4fDJ6jzkcBFxHHlc_DU8V-DIhP_RhhCVoZJuYyKFvfFB4EGnQEohKvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادامه حملات پهپادی ارتش به پایگاه‌های آمریکا در منطقه
روابط عمومی ارتش:
🔹
در پاسخ به تکرار حملات غیرقانونی آمریکا علیه کشورمان، ساعاتی قبل و در دور جدید حملات پهپادی ارتش جمهوری اسلامی ایران، محل استقرار نیروهای آمریکایی، سامانه های پدافندی و موشکی، جان پناه و سوله‌های پشتیبانی ارتش تروریستی آمریکا  در کویت هدف حملات پهپادهای انهدامی ارتش قرار گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/670392" target="_blank">📅 06:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670391">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
سپاه: مخازن سوخت و زاغه مهمات پایگاه هوایی پرنس حسن در اردن به آتش کشیده شد
🔹
شب گذشته به‌دنبال عملیات نیروی دریایی سپاه در متوقف کردن دو کشتی متخلف که با خاموش کردن سامانه‌ها و حرکت در مسیر غیرقانونی، کشتیرانی در تنگۀ هرمز را به مخاطره انداخته بودند، ارتش کودک‌کش آمریکا که خود محرک این حرکات غیرقانونی و خطرناک بود، بار دیگر با تجاوز به پایگاه‌های ساحلی نیروهای مسلح جمهوری اسلامی ایران خوی وحشی‌گری خود را آشکار ساخت.
🔹
رزمندگان غیرتمند اسلام در اولین مرحله از پاسخ به این تجاوزات، چندین زاغۀ بزرگ موشکی و مخازن سوخت پایگاه هوایی پرنس حسن در اردن را با شلیک موشک و پهپاد به آتش کشیدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/670391" target="_blank">📅 06:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670390">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
صدای دوباره آژير خطر و انفجار در بحرین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/670390" target="_blank">📅 06:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670389">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
سپاه: مخازن سوخت، سامانه‌های پاتریوت و FPS در کویت به‌طور کامل منهدم شدند
🔹
به استحضار مردم شریف ایران می‌رسانیم، رزمندگان پرافتخار نیروی هوافضای سپاه، در سومین مرحله از عملیات مقابله به‌مثل و پاسخ به تجاوزات رژیم مستکبر و متجاوز آمریکا، مخازن سوخت و سامانۀ پدافند هوایی پاتریوت در پایگاه آمریکایی در علی السالم کویت و همچنین یک سامانۀ راداری راهبردی FPS در پایگاه احمد الجابر را به‌طور کامل منهدم کردند.
🔹
تنگه هرمز سرزمین ماست و اجازه نخواهیم داد یک ارتش یاغی و کودک‌کش از آن سوی دنیا به دخالت‌های غیرقانونی خود در آن ادامه دهد.
🔹
عملیات مقابله به‌مثل فرزندان غیور شما ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/670389" target="_blank">📅 06:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670388">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
برخی منابع از وقوع انفجارها در پایگاه هوایی «موفق السلطی» در اردن گزارش می‌دهند
/ مهر
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/670388" target="_blank">📅 04:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670387">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
یک شهید و چهار مجروح در پی حمله دشمن به ماهشهر
🔹
ولی‌الله حیاتی، معاون امنیتی و انتظامی استاندار خوزستان گفت: در پی تهاجم بامداد دوشنبه دشمن آمریکایی و اصابت یک پرتابه به ایستگاه پمپاژ آب کشاورزی در شهرستان ماهشهر، یک نفر به شهادت رسید و چهار نفر دیگر مجروح شدند.
🔹
فردی که در این حمله شهید شده نگهبان این مجموعه بوده است.
🔹
وضعیت مجروحان توسط دستگاه‌های امدادی و درمانی در حال پیگیری است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/670387" target="_blank">📅 04:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670386">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ادعای قطع برق در سراسر اهواز صحت ندارد
🔹
بررسی‌ها نشان می‌دهد ادعای منتشرشده در فضای مجازی مبنی بر «قطع برق در سراسر شهر اهواز» صحت ندارد و شهر در وضعیت عادی قرار دارد..
🔹
از شهروندان درخواست می‌شود اخبار مربوط به وضعیت شبکه برق را تنها از منابع رسمی دنبال و از بازنشر شایعات و اخبار تاییدنشده در فضای مجازی خودداری کنند./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/670386" target="_blank">📅 03:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670385">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
رسانه های عربی خبر حمله به گذرگاه مرزی چذابه را تأیید نمی‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/670385" target="_blank">📅 03:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670384">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20bcbbefa0.mp4?token=qDtBWOm1Q1-se3DvHYtOVEqbpwqNuaq1voSSsBa1ty0kC_94XapWgErOOD9SQZenAYOCBReYeD-ZYWUMxKrkMdA_xJ_wd0sloXdTuQu5s0k1hMjOtmqt6VK1AIVRh3rit6-9NFvDLxKsoYuo9bkWz7Bj__gRX4THfbA89r__jXVLkBbMLrjb3-rrjAg1gN4WCajEIwQsg7kWfpahQBNvm0wT3_BnQ5BEYrMZ2hMkWbDj1TRy1nm3mAqXrV5RSARbBYJHNhIOSX1IpZ27SQ2jXOrgdtFlyJLdGuWLXt_mc2O8Uh6NNyx77QzOtzfIjEL2kqh9kBMYEtHs04sCOAj9fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20bcbbefa0.mp4?token=qDtBWOm1Q1-se3DvHYtOVEqbpwqNuaq1voSSsBa1ty0kC_94XapWgErOOD9SQZenAYOCBReYeD-ZYWUMxKrkMdA_xJ_wd0sloXdTuQu5s0k1hMjOtmqt6VK1AIVRh3rit6-9NFvDLxKsoYuo9bkWz7Bj__gRX4THfbA89r__jXVLkBbMLrjb3-rrjAg1gN4WCajEIwQsg7kWfpahQBNvm0wT3_BnQ5BEYrMZ2hMkWbDj1TRy1nm3mAqXrV5RSARbBYJHNhIOSX1IpZ27SQ2jXOrgdtFlyJLdGuWLXt_mc2O8Uh6NNyx77QzOtzfIjEL2kqh9kBMYEtHs04sCOAj9fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امشب، یک پهپاد اوکراینی به یک انبار نفت در شهر میخایلوفسک روسیه حمله کرد...
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/670384" target="_blank">📅 03:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670383">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3018e7f48d.mp4?token=PwhcQLGCzCvP5-7x8d6wy5bwUzwBCxldq-uYDL6VwSqtEzggw7rGzpoAJ9JA1zOdQWjq3xHF8UgMHNWzzbu2yenf2Vv7nBQB1IaNEfxyRNT3XC--9VIwisYSRDP2nAnZqzhI0vt68wPCz9tUiYyDBlWoStk-LD3gjYcQXgheVikSaWqyre0NpbFPdGxe7-tTm14Jrc4jOsthin1tsWlR-6rVSKntaE_-qXio8Ykanto3-0ntAqRx0HMTIJTq_mZjqAIfof03JB5jj5kzmSCW4XYAlNfCIWsL-uFi3Ae-mL_6THmkwNHJQm73fTvIW1dQkaC8yxrVmMMKwlPMmqbLvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3018e7f48d.mp4?token=PwhcQLGCzCvP5-7x8d6wy5bwUzwBCxldq-uYDL6VwSqtEzggw7rGzpoAJ9JA1zOdQWjq3xHF8UgMHNWzzbu2yenf2Vv7nBQB1IaNEfxyRNT3XC--9VIwisYSRDP2nAnZqzhI0vt68wPCz9tUiYyDBlWoStk-LD3gjYcQXgheVikSaWqyre0NpbFPdGxe7-tTm14Jrc4jOsthin1tsWlR-6rVSKntaE_-qXio8Ykanto3-0ntAqRx0HMTIJTq_mZjqAIfof03JB5jj5kzmSCW4XYAlNfCIWsL-uFi3Ae-mL_6THmkwNHJQm73fTvIW1dQkaC8yxrVmMMKwlPMmqbLvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دارالذکر در نیمه‌شب‌های حرم امام رضا(ع)
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/670383" target="_blank">📅 03:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670382">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpQgXO9juC0oeQUG4J4HVMeYdAh1-665K-rUcfW2Yf5-QB3SpabaMvlsLi0lYd_yeTyrUUfgXcD81oF0mJy_ENP1BIgNi58dJpG6h4P7Kwsp4PMAKtBTYqiP6iCFyBa3xN4-tZg-1r8RYutj1MASVHXLnqD3WdZWhp3If1pMdRILut1DZfPKRP2O8MMI78SMe8ldgKUJxINwkCaSpdcnJa17hQT_lTL6yHh1ZmRb_Ex0ZYfsf-ZSKswMFWS6QegM5I-d7-8RC0iX5OAYbs2PP2HCGzytjO0ZaQTweciaONr_EJk4R1YJWcWrUush6Lhf-hSn87QS3JkEmli5SbSuoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهرهایی که مورد حمله آمریکا قرار گرفته‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/670382" target="_blank">📅 02:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670381">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
الجزیره: حرف‌های ترامپ درباره تنگه هرمز با واقعیت زمینی تفاوت زیادی دارد
🔹
تناقض در این است: رئیس‌جمهور آمریکا مدام از چیزی می‌گوید که آرزویش را دارد، اما واقعیت در میدان کاملاً فرق می‌کند.
🔹
واقعیت این است که ترامپ گرفتار شده است. او سعی دارد القا کند که تنگه باز است و این موضوع بر بازارهای مالی جهانی تأثیری ندارد، اما ایران به‌وضوح بر موضع خود پافشاری می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/670381" target="_blank">📅 02:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670379">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
استانداری هرمزگان: تاکنون اصابتی در بندر خمیر گزارش نشده و صداهای شنیده‌شدۀ احتمالی ممکن است از سمت دریا باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/670379" target="_blank">📅 02:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670378">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: یک مقام آمریکایی گفت انتظار می‌رود موج بزرگ‌تری از حملات آمریکا علیه اهداف نظامی ایران در شامگاه یکشنبه انجام شود؛ حملاتی که از نظر گستردگی بیشتر از حملات اوایل همان روز خواهد بود./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/670378" target="_blank">📅 02:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670377">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tfJdy6UBlC2p880OTPKSNLGlT5rpH2uzipif3k_ShMiwKP-dGDLHI0QVi2kQ_XWrYAye_diwHOrQ_MoviO2h9AgvHRWM0EEN15AcEMSIgkE7C7lmTbNZxXBFEAk7g-rtGavdrm9R5sLJ3pn-w9bLMvP_63lGGxb8r263GGExNqgI5Kq-0hwShi9RqfItJwHY-c8v_E5WwTWUlDO8NxK-b2myiJBFKL8xt26jrNKdE6ETFTXftNS7OcVlOEPNBKB0e8XtRLumyahgX4kSwULcpFle_5UTc-Bxt-aXuYhyBxaB8K-MT_rhtUArPwLU-Cb2swtQfX3Qlkjk1Jlh0xWb4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همزمان با شدت‌گرفتن درگیری‌ها، قیمت نفت برنت به ۷۳.۶۹ دلار رسید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/670377" target="_blank">📅 02:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670376">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
نقاطی در آبادان و اطراف شادگان مورد اصابت پرتابۀ دشمن قرار گرفت
معاون استانداری خوزستان:
🔹
در ساعت ۲ و ۲۰ دقیقه بامداد امروز نقاطی در شهرستان‌های آبادان و شادگان مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/670376" target="_blank">📅 02:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670375">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
معاون استاندار خوزستان هرگونه اصابت به فرودگاه اهواز را رد کرد
حیاتی:
🔹
دو نطقه مورد اصابت اطراف محدوده شهر بوده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/670375" target="_blank">📅 02:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670374">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
چهار نقطه در امیدیه و ماهشهر مورد تهاجم هوایی دشمنان آمریکایی قرار گرفت  حیاتی معاون استاندار خوزستان:
🔹
در ساعت یک و ۴۵ دقیقه بامداد امروز دوشنبه ۲۲ تیرماه ۴ نقطه در شهرستان های امیدیه و ماهشهر مورد اصایت پرتابه های دشمن قرار گرفت.
🔹
دستگاه های مربوطه در…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/670374" target="_blank">📅 02:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670373">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
برخی منابع خبری مدعی شدند، برخی از موشک‌های آمریکایی از کویت به سمت ایران شلیک شدند
🔹
طبق این گزارشها، موشک‌های آمریکایی از کویت شلیک می‌شوند، وارد حریم هوایی عراق می‌شوند و به سمت ایران حرکت می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/670373" target="_blank">📅 02:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670372">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
ایرنا: شنیده شدن چندین صدای انفجار در قشم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/670372" target="_blank">📅 02:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670371">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
چهار نقطه در امیدیه و ماهشهر مورد تهاجم هوایی دشمنان آمریکایی قرار گرفت
حیاتی معاون استاندار خوزستان:
🔹
در ساعت یک و ۴۵ دقیقه بامداد امروز دوشنبه ۲۲ تیرماه ۴ نقطه در شهرستان های امیدیه و ماهشهر مورد اصایت پرتابه های دشمن قرار گرفت.
🔹
دستگاه های مربوطه در حال ارزیابی خسارات احتمالی هستند که گزارش های تکمیلی متعاقبا اعلام خواهد شد./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/670371" target="_blank">📅 02:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670370">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
معاون امنیتی و انتظامی استاندار خوزستان: در ساعت یک و ۳۵ دقیقه بامداد امروز دوشنبه دو نقطه در اطراف اهواز مورد تهاجم پرتابه های دشمن آمریکایی قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/670370" target="_blank">📅 02:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670369">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
مهر: معاون استاندار مرکزی حمله دشمن به مناطقی خارج از شهر خنداب را تایید کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/670369" target="_blank">📅 01:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670368">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
معاون امنیتی و انتظامی استاندار خوزستان: در ساعت یک و ۳۵ دقیقه بامداد امروز دوشنبه دو نقطه در اطراف اهواز مورد تهاجم پرتابه های دشمن آمریکایی قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/670368" target="_blank">📅 01:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670367">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
فاجعه در بانکوک؛ ۲۷ کشته در آتش‌سوزی یک رستوران
🔹
شعله‌های آتش نیمه‌شب، یک رستوران شلوغ در بانکوک را به صحنه‌ای از وحشت تبدیل کرد. در حالی که مردم برای نجات جان خود فرار می‌کردند، آمار قربانیان لحظه‌به‌لحظه افزایش یافت و علت این حادثه همچنان در هاله‌ای از ابهام قرار دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/670367" target="_blank">📅 01:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670366">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
مهر: ساعت ۱:۳۰ بامداد امروز دوشنبه صدای دو انفجار شدید در اهواز و ماهشهر به گوش رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/670366" target="_blank">📅 01:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670365">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
حمله دوباره آمریکا به دکل مخابرات اطراف روستای طاهرویی سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/670365" target="_blank">📅 01:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670363">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nCRrqA5XMyexG-7G4AEK4J4gJ3yNasWXkGIKNS18HODwrCiylegrb4BtPfmEoR_BcW28IAEO4qHJ84P7ywn_LP2qVZCp7JlASUWIQonxoWHalyNv8Ez1UNgZll-Pddfged4ZBbd1ROVZd5aLE5JQuws__EU43o-RklrvGnjAjXJxYrIp1BlcJMMeriisaawavVvD8Tv0izhxE8pR1-CMOWvY6u70nDRa2IhYmcwP-vDRq-rXt_frot9HMv_Qk6hmmI9ayJa1HfMSS8QSfvFbYmrcAKA0FHbFlY0leNcUt8oNgl7pPxYPkEI60gs4E0LbZgTnRvZviU_27T1-bEv03w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pz4X81mvX7gNB43Y0zJ_eUUEO0cxfAkHxFjMBU35IZIjPy-UCJ_Sicbo3mSiJ7kYcou4tsjh5oPMjc3cW8cdKYkvxqLwNfpxa7FbyqYcC4h7E_xZnfhNoLtBmCS4uI_9MAyPGnhVIYacPzbrxrAgVZ6VR4QP8_EqjAQW4xtpt3V0mZKhYBgRCg--UG0GgRaIyDT9GstBB6y57N-f8M2FjISn0KyTEwyd0_pvOoFXQpR3wXx2CWvGR_9ZwQ8LcGYM661IVdVp9xPH_GhJbB0eKRtMscEfdOM5jxyFGT63QoX-jR33LsTunSREHTwmEaXM7Q-DVWGQZQuHQSQZPotoJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصویری
کم‌تر دیده‌شده از لحظه ورود پیکر رهبر شهید انقلاب به کنار ضریح مطهر حرم مطهر سیدالشهدا علیه‌السلام در کربلا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/670363" target="_blank">📅 01:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670362">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-3wxMDooGvLRi12ZLIkCGz5zuvwGMkHtN2bVuzLYUQdGK5vI_1hAEcJqqqYf86HgaCSqizPJ-ktxke1oQO7pGZe6FdTz21jucT4L-M-bPLrnTT2mUlAhMC3gTLNjqlcUR-LpDXQZFg1UfmxOZsiofPsm4xj5iavRm3Tl_iAxwd7qXMulgE7YCUX09HdpisYdKJTSrU19cJlt7u-LeUUKkdECDcjBPe16tQ9-btBJ6bzNsjmDySoPoHdaTUwxJy5L67hUMqz7GJATRbbpcStMWENXyRPFRd2awVZNuxAP4Z7qZrUhS1F7DO0uKt6c9YguhDNcj_AXwRh3ZbEcUMcvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیت‌الله اراکی: ریختن خون ترامپ و نتانیاهو و شرکای آن‌ها «واجب» است
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/670362" target="_blank">📅 01:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670361">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ah3hfvglhfzYNW4RrpZdNjV8CzHrJE5PAneXhU4-yHK3hOtzFvZ8dmTHvbucp0GmIy4phuM2Qn_5lao7MtBfelj3bPREAXCd61Cj2IGGLA0He1BDHu-SS2yxiWuqQY2QqJ8KYtUjI2qInWBrBuKtk21kjx0c3vmL7H7i0ZPfMepj_QaN8SX8npi_uj87dMk0y9e4yIwzKr0e1SEbUv60Yx1baCU7LptV_GF0v2qT8r9e1mANbWgSYhC3sFFDSCItrQw41qAKNfxKewNO-OPZC3N2pLlEcZsStWV8V6AwGcnHW3VBDJHYWL1faevs5LLd57kkm2ehDg2xDpcnkFIHrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازار نفت با افزایش قیمت شروع کرد
🔹
نفت با ۷۸ دلار بازگشایی شد که رشد ۲.۵ درصدی را نشان می‌دهد و در ادامه رشد آن به ۳.۵ درصد هم رسیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/670361" target="_blank">📅 01:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670360">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
سخنگوی فرماندهی مرکزی ایالات متحده در گفتگو با سی ان ان مدعی شده که سپاه پاسداران انقلاب اسلامی ایران به تازگی به سوی شناورهای در حال عبور از تنگه هرمز آتش گشود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/670360" target="_blank">📅 01:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670359">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
برخلاف ادعاهای مطرح شده در فضای مجازی مبنی بر تهاجم دشمن به اهدافی در این استان، تا این لحظه اصابت در مرکز استان از سوی فرماندار شهرستان بوشهر و نیز در کنگان توسط منابع محلی تایید نشده است
./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/670359" target="_blank">📅 01:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670358">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
پرس‌تی‌وی: صدای انفجار در کنگان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/670358" target="_blank">📅 01:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670357">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
مهر: گزارش‌های اولیه از شنیده‌شدن صداهای انفجار در جنوب شرق کشور؛ جزئیات رسمی در انتظار اعلام مراجع مسئول
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/670357" target="_blank">📅 01:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670356">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
صدای ۶ انفجار در اطراف روستای طاهرویی سیریک (هرمزگان ) /باشگاه خبرنگاران
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/670356" target="_blank">📅 01:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670355">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
رسانه‌های پاکستانی از چند انفجار در چابهار نوشتند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/670355" target="_blank">📅 01:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670354">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
مهر: گزارش‌های اولیه از شنیده‌شدن صداهای انفجار در برخی نقاط استان بوشهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/670354" target="_blank">📅 01:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670353">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">زیارت-عاشورا-pdf.pdf</div>
  <div class="tg-doc-extra">115.8 KB</div>
</div>
<a href="https://t.me/akhbarefori/670353" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
فایل pdf
#متن_زیارت_عاشورا
همراه با ترجمه
@Heyate_gharar</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/670353" target="_blank">📅 01:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670352">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">-زیــارت‌عاشـــورا</div>
  <div class="tg-doc-extra">علی فانی</div>
</div>
<a href="https://t.me/akhbarefori/670352" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
صوت
#زیارت_عاشورا
🎙
#علی_فانی
@Heyate_gharar</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/670352" target="_blank">📅 01:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670351">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3SUUMfTS1B5KhgLSunq_WKKUxphJa_JNzYB2OnCDBIrIBKpHwMkpEQxNf-KEHZLDI8VPVNmDsb81xdpCVwrLFYdBqbwetGhGDYRqwl6oupPhsqh8AAHyeEm3dXg6Io0J2JRbidoP0hzotURpLoXfmDUTuKT8VtlFmGeLp9YUt0IOmM7xsYp2jn6ZYlz9r_DmV9Y-ilU-s6_GWSd0T3HUP8pR1f497S2VvcfPrJdYqi5SceM5LO4OqzqgAYL-Y44L-CHCvPcyPlg6uhQIeVpPOQTFEs3yabiXD359IKER-wf0dfP3A-pnb_Fvvjc5rb5zzWowIz31RmuiQ8AeEKvbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
به تو از دور سلام
چله زیارت عاشورا تا اربعین حسینی
#روز_هفدهم
▫️
امروز با خواندن زیارت عاشورا به نیت شهید دکتر مصباح الهدی باقری کنی  ، دل‌هایمان را به سوی امام حسین (ع) میبریم. امیدواریم که ایشان ما را پیش اربابمان شفاعت کنند
@Heyate_gharar</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/670351" target="_blank">📅 01:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670350">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
صداوسیما: صدای سه انفجار در جاسک شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/670350" target="_blank">📅 01:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670349">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
استانداری هرمزگان: در حملات جدید آمریکا به برخی نقاط استان هنوز مصدومی غیر نظامی یا خسارت به زیر ساختهای مسکونی و تجاری  گزارش نشده است/مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/670349" target="_blank">📅 01:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670348">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svJAYS4RNua-vYBn_a1Stb2gNrAo4IS-w5RH5RQorUJh2tKJs8MUbu07B6l22di0t2_yGnqNLGEPbLgDIGZw0R1poIYWqkx2W2bnxFtSMwnegfwVcmb0T0qu7d2P2Teu33Hsgwa2CQyf0_DC9-y8HYRnJdfXPXpP8wfhNCBqxeXErlTnjhiICvmUEe0a33ErBmchKrIq1FKrFapiwtFFb44Gyh35YMP_BkyJEdC9HPO6bKPsaTZYfTGQWA2fmfAV2RqKUIX2cge_bDbZ09i_icFGwtk7Ii2zbp0VylaLQbvHEV-LZGEBtmRhJt9gcx7-Yh-Fw-CNaQxvpXe709TbaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه حملاتی که تاکنون علیه ایران انجام شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/670348" target="_blank">📅 01:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670347">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONn5CTW5TE9wDf_OO3L0o6c13sAzkE8UIGncmJSA6CeE9JqceE_VZwWUsfxMVtDgeJJqAuTriCemsp9m6mFb8lF08EiX7M_KVkJg7yDQI13OIfpPFfa-0WFLS0PKHzWTUp5mT35IEOxARi5l703_QG1mBw45L-vJcHUwqKA7s2RbVurBA4r5iTUohrDHRWb17rDjDasOTsoqUMe1DCwRNCLIG-iqbqlvNe4jmyAnsp4Y_daPfi5ukDdOjqjkeTLcEaZQn9u6Ef86z1YzLsYmb1yl85kgs58H69U2MQGR2zL7x1NSimqT1u9bi-IhCkpLgv6igqgOrfzSv_5l5dwOBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/670347" target="_blank">📅 01:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670346">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjNxCx8zRjtVB2lvJ1FDk1km0DFSciCKl9ad0RortXTAZ2htFAX0HgPl45iZDAHAQZvFCC4Ww47E0OSp09HvqopcxgQfFjJ5TKoBiITF_oPk120MgfAePOAa66pEfH_YK9ugj4Xt1uFiuKGVod4Gu8oVu3fxFrelLrMsA2Q76HmHYLqu9-tF3p90bfY4Kk7CEsJc4Bu2f1FpnFWp8iiQQioRlPmfborT7JyxTws4PqZlGHuJVRcYBTV5Agc3oq8bJPiF4HXUPCLHdnqh70_uktBk-FSUDsEOP9k84tJdfGMVFfteg-nfXwN93VlAUuSKfHFmdasxsNEgc5qBQoVAUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زینب سلیمانی: مرگ راحت برایتان آرزو خواهد شد
🔹
زینب سلیمانی در پیامی در صفحه شخصی خود با تأکید بر حتمی بودن انتقام نوشت: خواب راحت از چشمان‌تان رخت برمی‌بندد و مرگ راحت برای‌تان آرزو خواهد شد. این پیش‌بینی تحقق یک وعده صادق است؛ به اذن‌الله.
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/670346" target="_blank">📅 00:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670345">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
پزشکی قانونی واشینگتن علت مرگ لیندزی گراهام را پارگی آئورت اعلام کرد
🔹
بررسی‌های اولیه دفتر پزشکی قانونی واشینگتن نشان می‌دهد که سناتور لیندزی گراهام (جمهوری‌خواه از کارولینای جنوبی) بر اثر پارگی آئورت ناشی از بیماری قلبی-عروقی آرتریواسکلروتیک (سخت و باریک شدن شریان‌ها) درگذشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/670345" target="_blank">📅 00:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670344">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Shabaye Jang</div>
  <div class="tg-doc-extra">Reza Sharifi</div>
</div>
<a href="https://t.me/akhbarefori/670344" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
بین بردگی و جنگ
انتخاب من تفنگ
🎼
شبای جنگ
🎙
رضا شریفی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/670344" target="_blank">📅 00:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670343">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8dW5Qx5xnf1MJS4BcpHxZTv9BRdqC2TcdM5vOohHKNwkmj7UUZYtDu9ZNbN-tsr1SBxrZXbpwOvJotGmtiyUH-Jf8ei4RM1Ba7ridyrdDHMfGNq8NENcYzZqPlMpSjHAL5p45cN4xi8svkmTsQ4EQUKbmqHcsDjjNYyxqlgdFiNIoACHMWs1I9iFKczyJ9s67EqDl3q2FIA9yD6lEIw5Epq2TxX-F3_XODc7aklqv5mDDuBZtnBL2qxh-sw9BIiwnwCJiacpk7mcYrocpiMgwOHed9j5yX3z2VrsAGamUt3WDcAKrSVyi4tXFpIkEoRlMlM5vVZNmunMSC0hTC9JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سنتکام از حمله ارتش آمریکا به خاک ایران خبر داد
فرماندهی مرکزی ایالات متحده:
🔹
ما حملات بیشتری را علیه ایران آغاز کرده‌ایم تا به تضعیف توانایی آن در حمله به کشتی‌های تجاری در تنگه هرمز ادامه دهیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/670343" target="_blank">📅 00:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670342">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
صداوسیما: صدای سه انفجار در جاسک شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/670342" target="_blank">📅 00:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670341">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFc1ZaS6DuUoFV9oukxafdZrodU-2X4Z4OYswJs5sfnBp3IEcbDW40cWSTe8V4Y_m0sEEGSaLYqrfJ7aU9tDSFe1YQWQx_4TY1u6tIfTvimDE8lUXxPbbSVEEdDAtBHwQedOZm_dBEYPUBRXPNjNjffWbJG-IXARKVk_THCLt25ap9sv_HT6D2ikcO656J4agtNMMlwzWSwgJpcNkM-PR2DlZOadDYbxl1iB-kTko-B2zRllFI4AelVG85TC0jHWJF2guxNITQo4JFGnU_Bx815_c6_tB7Zx3qn9w0TvpCh5V6oFN0LDfJNEcexJ3IS9M_3QGOm1Rm_XBsWBGLQawg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاکید غریب آبادی بر تعیین واکنش به هر سوقصدی علیه رهبری و دیگر مقامات از سوی شعام و مجلس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/670341" target="_blank">📅 00:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670340">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
صداوسیما: صدای سه انفجار در جاسک شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/670340" target="_blank">📅 00:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670339">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
صدای ۶ انفجار در اطراف روستای طاهرویی سیریک (هرمزگان ) /باشگاه خبرنگاران
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/670339" target="_blank">📅 00:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670338">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJ-lD-5DyiK2QF1pQvTcI_2UmfXyv8GbiAbjhGNHo_GrE5qjDTF4jOTWS-I2JgiHN6ZPTKyOA33W8T1lbbAZMdtS3Tk8hctuppZv8xdm9gtXl_aevm5hk1YK7p4BKg1HSr5gX4pt7iIXTFrlJRpppY4RnItEpBUujv66rvazeYoxjEV3utJkoIJDkyJ5CY0z0dCpr_HSHlBgejzNubuBjuc0OnUEkrGEMyrQBIamy-t45q9VvR9tXKgtFiP6vNwoU5XKvNSDOenzQ4d7qykyEItIs1OjLqiSeDNV6ZEEdf6NYak3Yk2XvCGxyD28csD2hYBcqm6PjLo42c7ZcA4aTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه درباره تجاوز نظامی آمریکا علیه ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/670338" target="_blank">📅 00:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670337">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
صدای ۶ انفجار در اطراف روستای طاهرویی سیریک (هرمزگان ) /باشگاه خبرنگاران
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/670337" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670336">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
منابع اطلاعاتی آمریکایی مدعی شدند: آمادگی‌هایی از سوی ایران برای انجام یک حمله گسترده علیه امارات و کویت مشاهده شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/670336" target="_blank">📅 00:31 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670335">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6800058819.mp4?token=pSGn8hBdeOo9Ai56JXJOQeDeln7sfdO0HvQJfE3cHuIkcKUlmc7RS-BxCab0kb6Zhe6QxTnKPjVrwJPuY0Rafwi6q-kcdKBNzfkMvv6EFH0Do5e6-TYqJdXbU6tyHkYY3EhAxwmCAoWt1X9E-KmoiKJGQc2-iB0hSDKqc0Y0L2E2CcfD9tYMPclRuvx29zem3AqAdvhcXISiFFhhHQGNE_F57lrM8NIrgPU_jozbOrf76R0ge8qcvYt2LyBlmhdCfm9rohIE_EeLs7ebJm8AKum0Vl41a6tP4x_HD6KEaFCyU6cyCIUZEmdaXSnWKqAI07CMw3-3gta5Fd8ma3s_NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6800058819.mp4?token=pSGn8hBdeOo9Ai56JXJOQeDeln7sfdO0HvQJfE3cHuIkcKUlmc7RS-BxCab0kb6Zhe6QxTnKPjVrwJPuY0Rafwi6q-kcdKBNzfkMvv6EFH0Do5e6-TYqJdXbU6tyHkYY3EhAxwmCAoWt1X9E-KmoiKJGQc2-iB0hSDKqc0Y0L2E2CcfD9tYMPclRuvx29zem3AqAdvhcXISiFFhhHQGNE_F57lrM8NIrgPU_jozbOrf76R0ge8qcvYt2LyBlmhdCfm9rohIE_EeLs7ebJm8AKum0Vl41a6tP4x_HD6KEaFCyU6cyCIUZEmdaXSnWKqAI07CMw3-3gta5Fd8ma3s_NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دقت راننده پیک در پرتاب روزنامه در هند به سرعت وایرال شده است: او می‌تواند برنده المپیک شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/670335" target="_blank">📅 00:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670334">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
هلاکت ۳ نظامی آمریکایی در حملات موشکی به کویت
🔹
برخی منابع گزارش دادند علاوه بر این سه نفر، چند نظامی آمریکایی دیگر هم در جریان این حملات، زخمی شده‌اند.
🔹
هنوز منابع رسمی، این خبر را تأیید نکرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/670334" target="_blank">📅 00:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670333">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yc2i07eMcSiLqDnpnTQk7-sEMCNQc1nng8SXZLRBnWO2yN_JK1b_BMPyzag7dYCUp-U02ipzg363HN20JlAGMe2yYrHIrALoJ5-T7NaL2fjc2urjO6firBDOBWInuXboC9Mq5M0wuNR39dG_-ec5Y7dbFnWL5u26bRqU7UBlIbPF-U8rbAnWIkzucJsO1El7xdJ-lJxaDnD_oR0pswcdtanEoysTCEuD6XQL2oxBecrPamOtb4uXfvvrr7tiMsWn7uYOtY2Y9Mx9txI8c2P6HTsE5OErcNq2PYxHyplGAKHxEm39ApX06Ocho5dijwcC78AA9-8u3fK3jis9Lb6AxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ناسا دنبال داوطلب‌هایی می‌گرده که یک سال در انزوای کامل، در محیط شبیه‌سازی‌شده مریخ زندگی کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/670333" target="_blank">📅 00:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670332">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: شماتت کردن ایران به‌خاطر دفاع از خود در برابر تجاوز، غیرمسئولانه و ناروا است
🔹
این وضعیت، «برخورد نظامی» نيست بلکه ادامه تجاوز آشکار نظامی است که از ۲۸ فوریه توسط آمریکا و رژیم صهیونیستی علیه ایران آغاز گردید.
🔹
ایران به جایی حمله نکرده است؛ ضربات ایران علیه پایگاه‌ها و دارایی‌های نظامی متعلق به آمریکا، مستقر در کرانه جنوبی خلیج فارس، اعمال حق ذاتی دفاع مشروع طبق حقوق بین‌الملل است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/670332" target="_blank">📅 00:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670331">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phIkcitfKGxS_KPMYf2ZeecnL2Xt64rkOYHJ0YQfkVWI4x4PvXVKhXnN2QIEyWgySbkSIDoZciT5jiX8EktTM5Vge7YDZEU9If8jsXfkAxkAHzs14CkqhjqGT14pV3MnFyKze7VE6YeMeCvRh_ByX4QAtsq2l_rF1o1WT7LOxXK8qdge2mX0oe4kcVN2qoZihE3f4AHmk_-q4BsxkC_i2rfUrhoILudC01437zEJ2dhMpBzkTMUWVMmuo4yaTO5qoUJbw0VFpFvLhbF5gNa0Yw4Oup4lsi0ttfjEmSnUA4Jn2E46OIrho8UDhhBpKb7rjF1lzHHEcG9oL2ua3csyGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آرزوی خواب راحت و مرگ طبیعی در بستر را به گور خواهید برد
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/670331" target="_blank">📅 00:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670330">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
وزیر امور خارجه عربستان سعودی با همتایان خود در قطر، بحرین، عمان و اردن درباره آخرین تحولات اوضاع منطقه گفت‌وگو کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/670330" target="_blank">📅 00:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670329">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gx93LoAQijaEcXjukECts6fkW84vVLAaj0QzFf0JNg3R5payyR0zoVjPJQQJ_sZ6p-yG-Z6omEmbTluBEnD-93Tjlz8oVLLZNNqVjerHIPOCbkIm8dM0MoFYiYczk-q-ft1V0qaSssxE8tDO4908a8UUfq8UfM5N_jPLgSIHYMcgBeJsp2ANONcNnytr961T5NTodrNdF4ofz7YrwSQI00if697mgh4yQxW5DYQtOHFsUnc5ARbxF2Jcs3F8QpYpNU9-sIRqk3h6lZyJPLJ-Cx-C61tp0G60LZAwQa39cvOwfPcTxbr228b48ZOxOqCH06AYWnrWUYLnimeljCdO2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اوکراین پهپادهایی را به کریمه و غرب روسیه پرتاب کرده است
🔹
منابع نظارتی حاکی از آن است که تاکنون ۴۵۰ پهپاد پرتاب شده است.‌‌
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/670329" target="_blank">📅 00:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670328">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fN7npBPeS3HTB1IrgMGhBeH_sEysV7Xf6iS3mlLwuMmiwJsbNH7uu-UrL1TbLeiFvOndd6Aryq3lDTg08i2vyAIXEKGvX8ueTkLyTeLT4SaOVGBoTXq89GBeQ9Vlb_7EPumW_aMXBRH2ucDAB4RELvLkscU4sTGhcTqSKhO4P2BMBnD8HwVfpYb6uSgtBOOKKXq6cLxzsn1WtDSdLXkm5WpjiuLRLSVRRLYNzFFkbUDLBQg9CqnaWNRgUMyaWF08EHivLDLo99z0Kck_x1dNsQMHXoZ6GAUPgHbM8nqSaekl7UqDbwGL8wE_L584t8onzGsJAgUXx9uhkU3smHi-LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/670328" target="_blank">📅 00:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670327">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
باغی که سنگ‌هایش موسیقی می‌نوازند
🔹
باغ صدا، موزه‌ای روباز در شهر سن اسپراته ایتالیاست که «پینوچو شیولا» با تراش سنگ‌های عظیم، آن‌ها را به سازهایی طبیعی تبدیل کرده است؛ کافی است دست بر سنگ‌ها بکشید تا صدای موسیقی از دل آن‌ها برخیزد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/670327" target="_blank">📅 23:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670326">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
نیروهای نظامی ایران با هشداری از شهروندان کشورهای امارات، بحرین و کویت خواستند از مراکز نظامی دوری کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/670326" target="_blank">📅 23:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670324">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RCRLUpSTxQm7NjDrF81yt-VV9mGZ3O1YEIZLRVUKuhyca1vY_n-NuR_gfOqB4-fUwxlow28oYIMALgJ0tEJ5vwykVXtxyjrk2Z4CRMlz4qjPi2cjxWUHNuClyZTwidSlVMD9ApxKQYnJAgLPUeYFddlsLlLh0BSMS8I-47t5Etz7I6VZD7yAsEmm2nNaHypdAfDLmxtFCZJ8OhqoPUhgBLYwvsw5pMnne_rg_nec-Qsib3TorHCoqNddixJIYveD0hH6mgfnfpoNyls0F8di9_aKpu-8PxVlD3pYTiNm6aNAhmBqJ1Ya-6oq0uOJl6Ihk10VR3UF4AXn0wWJhZ9wpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sU536tVcl7YZKPqe81rd30fMTn2BYMGKgTAc1eYF61sQ2KsdMv9kOap8JbM98JLLgnhr1QZmU_HjyayaWSrgNYHCd0nioRpsUbO6JVyIeZcXbo7fD1K5ZkDDYoWVr-IaAa1kHUcIKfllVr-gB-M4z-yjiKZy9P8I5ch6oU_g2rMs5tS7VHGMmx-7uhAw3A15hCmI2pbQLDhVn0TYxTEaAb4LhKXCQg9Jn70_bwAda7yNLGtd5OXb627Rujo_9fUBYah07OFQW3T7-225ML6fcXRuNx07wj5yN97PEQdUfFRE5WLfqf5937RLf-TSkkvPBDnlN9_biikWg86sFklSrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دو پست جدید دیگر خوک هار که دقایقی پیش منتشر کرد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/670324" target="_blank">📅 23:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670323">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnt77Pqz1EJZVde0w_yCLLpBAnT3wgfpfn7t3c9MQL24IdzKP2HKWU1tKJd42RsYYQt_8fFKtPa8ywkrmLKWcsDmjh8Y4AVDG82LHNJXW_mSFtLJP95v71i-hLjVwJpNczLVhW30mNk-dNyQJ55LcrGOLqYWNOnNc1UE04B1RN0g-OoLJfGq1r679bOxaT9_54p0BZyJzlQC7vWtzXH7kmAAOWdCJBFg34JQ4L2ZKXgIYzzg8hFoCnE85-mcUwX8fxZ4NsP2hMneHUy43zCGWAH0t97iAT0hB15qi9CyCLFf2lQLcLksOTmD4bfyfh9ozgV0Ow3N1KFpI7zaYoVGVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت جدید خوک زرد: من به ترامپ باختم!
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/670323" target="_blank">📅 23:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670322">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5422faa93.mp4?token=MeVdX3n1yIKWEFTfL7eM20SZqeg6PEj43Ky2iKjLfqcC-rgx6a85DL1Hmy15mFTCUY7Erz_yLW41rAz_JI6NKItzJvGMx3JwyJkVQLXpc3yjDy1icEnBaSPl869mLlv2q_ntHJWLHdkSGogmwmWInrqxny7TxGy6buRCHxT9hPlTnW47ZkJrfQMs4Gpb5vDEY0OTOB1MJZDE8nrpIvIyXaTCKEOONPU2wDSlg8doChLJcTyLpmyMY_TYSPJrUOQ584JYWFBAa9w-lKg8KPfOMrvOq28LriMYZ6MeVwpbJXpAkMdTqgXhNmgOr-hwf41QLfNV-bjVULQnyAglUci32m0RyXHOy8mzWos8bs4N-IR9CSw95BrLEQyZ71qPm3MtLvPnn_3wUxeBueNb22y4aaIBt6C8jozZzp0idkAzEtraaRvQREu0BaDBfhkAqRqo9s5ZNStvHxM4P_OXXCBfYnm8pyudM88POoCDGdYnAEmQvFQ8iLILUq5bL2lWe0jU6b4ZiLL47TiUxYndh51P-wxnJmL0TKlafQFjY1var2lEApmE9A1smx9j_TkcIFDkSQ4U7NTBebEO22CRN6dIO-spcpgpIw6_tqa3qsoHLNeptDrEPbgodtU6WlgNMcb0wTa376QfnZYjtJ6Y3CrV1QMme6l-e9B3bQEnbwMtR64" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5422faa93.mp4?token=MeVdX3n1yIKWEFTfL7eM20SZqeg6PEj43Ky2iKjLfqcC-rgx6a85DL1Hmy15mFTCUY7Erz_yLW41rAz_JI6NKItzJvGMx3JwyJkVQLXpc3yjDy1icEnBaSPl869mLlv2q_ntHJWLHdkSGogmwmWInrqxny7TxGy6buRCHxT9hPlTnW47ZkJrfQMs4Gpb5vDEY0OTOB1MJZDE8nrpIvIyXaTCKEOONPU2wDSlg8doChLJcTyLpmyMY_TYSPJrUOQ584JYWFBAa9w-lKg8KPfOMrvOq28LriMYZ6MeVwpbJXpAkMdTqgXhNmgOr-hwf41QLfNV-bjVULQnyAglUci32m0RyXHOy8mzWos8bs4N-IR9CSw95BrLEQyZ71qPm3MtLvPnn_3wUxeBueNb22y4aaIBt6C8jozZzp0idkAzEtraaRvQREu0BaDBfhkAqRqo9s5ZNStvHxM4P_OXXCBfYnm8pyudM88POoCDGdYnAEmQvFQ8iLILUq5bL2lWe0jU6b4ZiLL47TiUxYndh51P-wxnJmL0TKlafQFjY1var2lEApmE9A1smx9j_TkcIFDkSQ4U7NTBebEO22CRN6dIO-spcpgpIw6_tqa3qsoHLNeptDrEPbgodtU6WlgNMcb0wTa376QfnZYjtJ6Y3CrV1QMme6l-e9B3bQEnbwMtR64" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امیر سابق قطر درگذشت
🔹
دیوان قطری اعلام کرد که شیخ حمد بن خلیفه آل ثانی، امیر سابق، درگذشته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/670322" target="_blank">📅 23:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670321">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXMRq5_hHzX-Qv287aeOHwPryaT1NLsQr1HNOh4A_R8jjebJVf5PEOJ2E1WAoy7fL59AEfuFu96RTTF-6iz1kOQcZ2XyTg_iP_ChFeeRBfPHOKXHMJM4M6JIlo7hB1nWAjUO8WE5D6lXrCdNekvtr-b5vnl4GdGleufjx-f_iM09As27wHZ1M1BFzdv1XJB30F50bi-rPlziZ8-bFaJhTR2Ab5S0KVNrgKzv1AdvHC4WrX6ubAFesb1fbCvcFZiHX1jcaVpL6Wu0LWHS0nIF2e040OWNUbjc2RUO_EfAMyCbnyRrcuUzM5tt50e7NZy7fU8D0PWPc4L3SbicIYPJgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام مهم مقاومت عراق به دولت الزیدی در آستانه سفر به آمریکا
🔹
مقاومت اسلامی عراق در بیانیه‌ای ۹ بندی ضمن اعلام مخالفت خود با سفر هیاتی از بغداد به واشنگتن، تصریح کرد که دولت الزیدی باید ضمن پایان دادن به حضور نظامیان بیگانه، برای رهاسازی اقتصاد عراق از هیمنه آمریکا تلاش کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/670321" target="_blank">📅 23:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670320">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkMDWItFvUgtDmaxeN_bvMVAM9lbfLwaVoVBqj3H9R-2OkVpo9MPO6WPiS9lN66SoLrsBFkms7Yx6lLuKbDImTRjujhowO4FbF9yAzukgBNwfh9WnpsAsHxiENIemh2lEcl_hTDlW49YIO-RIBGMLJB06TS46g9IalsXSn9EHXvyQdSDkv2Us7pURRc-ibW2a8HXAtctdqcqs7x_8ZgEKrQ1ZzyQILpIBDelM7qW5wedi002wlvBHwB9UCVyQSxRFXLzzsuu9wrzBwn9qS65-nTw9ifSIvlQl4psYIY5WXCGZAjNfA9T43e2olCRhN6Y8f7_G3t-RkpGB6C-fTVTew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوستر فیفا در فاصله یک هفته تا فینال جام جهانی ۲٠۲۶
🔹
ساعت ۲۲:۳٠ (به وقت ایران)
🔹
استادیوم مت‌لایف
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/670320" target="_blank">📅 23:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670319">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نتانیاهو، درباره مرگ لیندسی گراهام: در اسرائیل اندوه است و در ایران جشن
🔹
مقاومت اسلامی عراق: سفر هیئت دولت به واشنگتن قابل قبول نیست.
🔹
آژانس بین‌المللی انرژی: عرضه ال‌ان‌جی قطر و امارات به شدت کاهش یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/670319" target="_blank">📅 23:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670318">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b76bad9173.mp4?token=eawDMyPK09lm6mUEUJR5GbJizFb8SfQqisdiXckH1crV-LIVBzS5ZTb9i786suUOAqdLW5ClLfcKBDTROujS2hMjUgJjbbYPlAICXrSJAoC0jM2fwVOwbV9e5Ep-hi3qPt9O1WkGGMBQNInLCQDQC-qb85ySzz9M9CaXm0fMP0Sdg0kbyUmi6jaAmNTGnOuwUbYw0N3s53e6wIeYbPaIGgx89WhEgyex3SnLSyK6Q9eEh9FNjY1VMtI0dYUAADjIC7HyZuDi0_KkpkZGKrwayURJ7hDgHKfC_WxWU9Yb28-NAWQg3HTXnDCr8y1ygve6YFf0lcg7h2XDseoyNopY0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b76bad9173.mp4?token=eawDMyPK09lm6mUEUJR5GbJizFb8SfQqisdiXckH1crV-LIVBzS5ZTb9i786suUOAqdLW5ClLfcKBDTROujS2hMjUgJjbbYPlAICXrSJAoC0jM2fwVOwbV9e5Ep-hi3qPt9O1WkGGMBQNInLCQDQC-qb85ySzz9M9CaXm0fMP0Sdg0kbyUmi6jaAmNTGnOuwUbYw0N3s53e6wIeYbPaIGgx89WhEgyex3SnLSyK6Q9eEh9FNjY1VMtI0dYUAADjIC7HyZuDi0_KkpkZGKrwayURJ7hDgHKfC_WxWU9Yb28-NAWQg3HTXnDCr8y1ygve6YFf0lcg7h2XDseoyNopY0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طفره رفتن خوک هار از سوالی دربارۀ تنگه هرمز
🔹
مجری: ایران اعلام کرده که تنگه هرمز را بسته است؛ آیا این درست است، آقای رئیس‌جمهور؟
🔹
ترامپ: از نظر ما، این تنگه باز است؛ درباره این موضوع سوال نکنید. درباره دلیلی که از من خواستید صحبت کنم، صحبت کنید.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/670318" target="_blank">📅 23:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670317">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O349jRR06Vzl5LPlBI6k_9ackrc44BgEjpQY4cXiZTMp2w_lD0U5CNUh1rjL-ynTppnhfdtyv7nPikunCPlfAoWSfUEfs4UaGHLDMdHA_ILLGQITXFf4RMQzNIA-NdRt9kIZgHhW8DbyRK6466kTddqNZMhW6IOrpeW4JGwMLsPegXXGAkk_AvxuDk50dnGq0E7GVlNFgLcWsvb6UABWDvSt5L9uWx6-PDUXtdu86yfzAwNHIcBJN7d-Voi4B-nfrim50YP0oJ4ksWfHg7LAfRH_0uSwO4NvSD_8NAiOIG6E6xLYk1vVQp3tUfMBh0LbDDotqAqJz-s8jHI9Tgixwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاپ لئو چهاردهم: متأسفانه، بادهای جنگ بار دیگر در خاورمیانه، در اوکراین و در بسیاری از نقاط دیگر جهان می‌وزد و خشونت، ترور و مرگ را می‌کارد و بار دیگر بر بسیاری از مردم بی گناه تأثیر می‌گذارد
🔹
اجازه ندهیم این بادها شعله امید و آرامش را خاموش کنند، حتی اگر شکننده و سوسوزن به نظر برسد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/670317" target="_blank">📅 23:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670316">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBO8UaiR0hpjv8Z5NiSaeDhbuUy9C4-CS1UQUipmo09tgm3JX0_EZmtdCspxuD8JnYtC-ad3TiPQtz0WMB0hCkkjt3qTq3ewg_rb8t5RMy-Us3fr5XxBy83EUIRNfGXN6eOvyKGyI1Fxs6de4zv0Jh74aY50zSJsUAZADMUigGugXgjrk11Bd3Vxn1Sr0hPLP7hfDnRV5SFBSUNKQLu3LsumlHa7S1zD89BtUdMC4ocu5SK-K1bgsSVvrMGdkCFJJdiiXRcCYB9P2ifpjDAWePHK4UaDmHd6flrDvnB5Dw6ezqqsEubCABLNcK8KJhP6W0WvF7Zq8IDgIjt9c2WQiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیشتازی حزب آیزنکوت از لیکودِ نتانیاهو در نظرسنجی جدید
🔹
براساس تازه‌ترین نظرسنجی شبکه ۱۱ اسرائیل، حزب «یاشار» به رهبری گادی آیزنکوت با کسب ۲۴ کرسی، از حزب لیکود به رهبری بنیامین نتانیاهو با ۲۳ کرسی پیشی گرفته است./ جماران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/670316" target="_blank">📅 23:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670315">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9054413b86.mp4?token=JY6WZ59_4109rNC56QvbWfKBkHVRIMS_r7wEkxp70GaQnDL2-uSfBx4G3F_RIPfVS3f9JIPhMDpbBPaCL4MYdkY0f78S1pO5ryLxhFLaAWh1ad25jIkcH7d6NuArvmQE-8JYN0rqyB8eQSEnc3XA_4QNEiH0ZwNWw9UnPnKMvvjWk1VgyE6dZFjeW1Pje4IaJHFtuiyNRtZ-thx9ytnPNuUv-SM8wjmfteimKvt8yaW9BZIPyq_29kFCKDJQdQZneiHbxlAVv-XqpW92pJ3BFlCfOx52cHnvcpNdHrof7hUdPS7smw4bft1I-aV8arCG3kd4IP3boTfe8SUX_1XjcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9054413b86.mp4?token=JY6WZ59_4109rNC56QvbWfKBkHVRIMS_r7wEkxp70GaQnDL2-uSfBx4G3F_RIPfVS3f9JIPhMDpbBPaCL4MYdkY0f78S1pO5ryLxhFLaAWh1ad25jIkcH7d6NuArvmQE-8JYN0rqyB8eQSEnc3XA_4QNEiH0ZwNWw9UnPnKMvvjWk1VgyE6dZFjeW1Pje4IaJHFtuiyNRtZ-thx9ytnPNuUv-SM8wjmfteimKvt8yaW9BZIPyq_29kFCKDJQdQZneiHbxlAVv-XqpW92pJ3BFlCfOx52cHnvcpNdHrof7hUdPS7smw4bft1I-aV8arCG3kd4IP3boTfe8SUX_1XjcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین ویدئو از سردار عظمایی، فرمانده نیروی دریایی سپاه: هیچ کشتی خارجی بدون شناسایی ایران از تنگه هرمز نمی‌گذرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/670315" target="_blank">📅 22:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670314">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
عبور نفتکش چینی از تنگه هرمز در مسیر تعیین‌شده ایران
🔹
بر اساس گزارش‌های منتشرشده، یک نفتکش چینی تحت مدیریت سپاه پاسداران از مسیر دریایی تعیین‌شده از سوی ایران در تنگه هرمز عبور کرده است.
🔹
طبق این گزارش، مسیر جنوبی نزدیک به سواحل عمان همچنان بسته اعلام شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/670314" target="_blank">📅 22:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670310">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jCM3AvkMcxOuoe7449FLqi7e73Hqu0-J3V7bjbQilQ8PcAFZqpNlmuJu_MEVQlj_t7PGQBjQYKY4tJeY85rm2X1d-CLD5y4tJuzYTgT-V8PKsIXE5iBJ3DINIsJen7-SoNMKgO3u0C-GePx8S1oB9cc6K6z55XEXbc8ERBwPWjn-SfNn_GKTs0gzej6EnX-LNPZZ-cIsOC5qFOJaZTTrWrzQYMHiWjlcDH8jPqgiZVBRyDPjyNEvBea5h5d1VdcNMST1691v0hvVrG5J4zl2zMz1LBcOGCcnZxQy_jztHg2lbaG1lPvx_hM9W-LmUfZmGjS-q1nDsBN6cMRD4CdHNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_0xB2QU0lc1bV4P01v4ZT8A2o-lI7SeloOjJ6wpViZZGNlv6XGzQqknpJ0zVwIGzd4yZvK9q5tQvkAr3s1zL8CA3A7W5I0EfnS_-DswScOKgjaep0ASZbCLFcZw-XravyEgEIss1BtGstslDby1a0VShhz_QAJjoDMK139Ss7AH513axDsLAhOmw3QnTn9QoYoMuB6BihXXSPdl_gwPSn4pQqxctovIwgVokr4LMMd2IEvEPOydFBBasHjVdlz5HGTlAlxYUxhBcx3SbJw2lz12TJ7Qo1gUla88skNLAgSP5WLK_qAMOQxjUGRMnDBDIiQXrrhEBv29Fc-vHP9HGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ndSH-PNKzcK-wRRFw3zB9of9qrhbaudMAePRXFxpDXX418fAgGzDGyzGKYaxRELb-N4FsLpr8Btmu9OHvs7lDIn8q56J62ldgBZui4lpVtTqALPslp3gyg6pLzxuILGDmgQifP1fgvwY51bd9JJ3o4DL2J9mfdFq22wkcKwT5KERZP3YtvKMiYXLz2IHDzfN9G1mBT-sAuDGbU8yVYW-EXSHmJU_nkc8wYzaYKrUWPRFvtWmADTpimSRMDSHUHQE21gDb0NULmV4jg6gL9a6119-IlwDEiYzHS50ZIwH_RO39QVHxKXo5mb8KARrE6f5Qp8VLspbzIr9gYjtMpeDkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJQU_ciDhG-ajx32mueoCbborZWxUu4oolWOPgVBrKLpuNjWGZAgGte-Dmd72dsGv7i_AeicRctaRRecFTSG43_OEKORA363jh2l58B6DZTvAIugUHG9xlE_zYP01E-WHBeBIrN257x4qz0nBmLhKefBxhF1nmUS7YRvcu2EzQ2y4-aRaVlafjMij0acn2ICyOd3-DWUD7Bgxuxunbgf17Oy4nrl4NOgFUpvzaM5IwSImZ3cNUjPTPqcS_kKRGYCX88HJ9JoZrrMeSJi83li8QzYZGeKJdn328AJmMGPi7D2DkK50MuRJGgkFscOGH3JYJK7E00M9oMKc6VhhgJbNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از حملات ایران به تأسیسات آمریکایی در خلیج فارس، که در تصاویر ماهواره‌ای دیده می‌شود
🔹
آشیانه پهپاد MQ-4C تریتون در پایگاه هوایی شاهزاده حسن در اردن ویران شد.
🔹
آشیانه‌ای در پایگاه هوایی العدید در قطر آسیب دید.
🔹
به یک تأسیسات انبار در مقر ناوگان پنجم ایالات متحده در بحرین اصابت شد.
🔹
آتش‌سوزی در یک پایگاه در کویت، که ایران می‌گوید ایالات متحده از آن برای حملات هایمارس استفاده کرده است./ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/akhbarefori/670310" target="_blank">📅 22:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670309">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5aab71909.mp4?token=QljBvg9qaJQk0jvOrR6HQLX93HR_6ZI6OPgtZOi5ufjCD1IQ8F6PWcfpMaN5BfYkMO5-LLaPzRvSFkjqx-oPypH3tr4VOFoH0aF2OS3nJrkafCwjy8Zmki93yScZG0WTRoVl-BfJGB5a6G_EScs0YE3kb6gagCOyBRlMHhqR_hHi4lmaMXd0CqbK0j6xFq6k1YdE5zlE41Q5st1waYjdbxnJP36LBEai03QaPSiBsjYIWkAD6_xF3BZRqSUwoTydArSwIHlXGT_vig-OKeJGWkOcPep0CdWWYEMD3o4aEXIEnFqF_17Nl2rrZHt0K3_ylhdivB-yHyE6HxQOVuAyxZS_Tz2ZYCQL-TQ2fK45y8m5Lz9URxv76xMDTstIHZKdhTASVD1d5Q1XCxiTM-je3cHLvpnWaPkHSqCLPNDDOcPlctQK9fAqET5_Wm2oHHLZSAvEqCF1rrQNQT6Jt_oDoqspcj3R8mTQSX7vgRO3pACyPbxZ28QB3f2Tfcck00BuBc_gt4hk1sOIj4e_Y2rSoJJrQnhUQERDjOF7Q1oW9ptUpZSy-7Or1whf-ybUiy_dmNsbsdXqw2uDr3Agr7IDs4YCG4NnfLPuH3jeeCllIlqMSX3pOtl6elQp2goifMRD-2OBLQnlt63W4iKaC54peGomJ47ecncoEjC5GThMofo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5aab71909.mp4?token=QljBvg9qaJQk0jvOrR6HQLX93HR_6ZI6OPgtZOi5ufjCD1IQ8F6PWcfpMaN5BfYkMO5-LLaPzRvSFkjqx-oPypH3tr4VOFoH0aF2OS3nJrkafCwjy8Zmki93yScZG0WTRoVl-BfJGB5a6G_EScs0YE3kb6gagCOyBRlMHhqR_hHi4lmaMXd0CqbK0j6xFq6k1YdE5zlE41Q5st1waYjdbxnJP36LBEai03QaPSiBsjYIWkAD6_xF3BZRqSUwoTydArSwIHlXGT_vig-OKeJGWkOcPep0CdWWYEMD3o4aEXIEnFqF_17Nl2rrZHt0K3_ylhdivB-yHyE6HxQOVuAyxZS_Tz2ZYCQL-TQ2fK45y8m5Lz9URxv76xMDTstIHZKdhTASVD1d5Q1XCxiTM-je3cHLvpnWaPkHSqCLPNDDOcPlctQK9fAqET5_Wm2oHHLZSAvEqCF1rrQNQT6Jt_oDoqspcj3R8mTQSX7vgRO3pACyPbxZ28QB3f2Tfcck00BuBc_gt4hk1sOIj4e_Y2rSoJJrQnhUQERDjOF7Q1oW9ptUpZSy-7Or1whf-ybUiy_dmNsbsdXqw2uDr3Agr7IDs4YCG4NnfLPuH3jeeCllIlqMSX3pOtl6elQp2goifMRD-2OBLQnlt63W4iKaC54peGomJ47ecncoEjC5GThMofo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدجواد لاریجانی، کارشناس ارشد مسائل بین‌الملل: از دیپلمات‌ها و دیپلماسی انتظار داریم که سایه جنگ را دور کند و علاوه بر آن باید سایه ترور را نیز دور کند
🔹
اگر انتقام نگیریم، سایه ترور همیشه وجود دارد.
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/670309" target="_blank">📅 22:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670308">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CW9fP4TFE8CxQ75gMmDdPVdysCfoO48lsSzpIEaM1KOs2QqzJxn2tshLL_65uaLTCeCykBT0D-9lV6JauK42F_KD4C49WlcdyRVNpInkQsd3U4ItUUA867m_Q5idTgaW5sZ1uhL_NhWrxpQrAMsalyPOFNUjOrzSf_xLcpQQQTYV83V4ue2YC3q8MmpjNRpeOj97RNLMEnC92h_8nwgFTnNV2PgE9dW8LCADSZjG3GdmW6OQKH7uDobEzc2GyvAxxVaH_Cir6my3bWWxBpCFiBbW3X4vEu0z4eqkKu1Vhw01R_ujA-qmbcXPowdodSELZ4tY0i1hQP81UnVnDctf0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حقیقت وجود هر آدمی در طوفان‌ها شناخته می‌شوند
🔹
آدم‌ها در روزهای آرام کمتر شناخته می‌شوند؛ این فراز و فرود زندگی است که گوهر واقعی‌شان را آشکار می‌کند. ثروت، قدرت، سختی و دگرگونی‌های اجتماعی، نقاب‌ها را کنار می‌زند. بعضی در غرور،  دنیاطلبی و سختی‌ها سقوط…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/670308" target="_blank">📅 22:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670307">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
کانال ۱۲ اسرائیل: نتانیاهو با اشاره به مرگ گراهام که امروز مرد، گفت: «او به من گفته بود: باید به تأسیسات هسته‌ای ایران حمله کنید.»
/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/akhbarefori/670307" target="_blank">📅 22:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670306">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bad85807b.mp4?token=rKVTuo976iFIuBnJk4tvqUyb61wx8aVWKCgaAQSmD_zwtDuqbURUZwyI5MoHaUnz-l-2gx7p_-T2GvD0Rl7Ic5YMjE5kl-4WS7_3sXZ9ydFO8DaSAMI_cH13HknTW65CjsUuTuUYdpmi-Am_BFEawDxnCvXoCUZTB3emP-2XUzVAmW1nwBtF_IV3PP42AtCHAgGQc0e1Q4Bo_iryAkP3JHVnhYPXB5UhOWlNEBfOMTDMU6qT3dx4Xx43R8VUeFifrBHnE8fPXmlsLcOC1aaLJZLWsfHND5c2A7My22FBZERl3U2KjCyZX-l_ihSGAVG--k0BHrhzXqujyD8TwTdLsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bad85807b.mp4?token=rKVTuo976iFIuBnJk4tvqUyb61wx8aVWKCgaAQSmD_zwtDuqbURUZwyI5MoHaUnz-l-2gx7p_-T2GvD0Rl7Ic5YMjE5kl-4WS7_3sXZ9ydFO8DaSAMI_cH13HknTW65CjsUuTuUYdpmi-Am_BFEawDxnCvXoCUZTB3emP-2XUzVAmW1nwBtF_IV3PP42AtCHAgGQc0e1Q4Bo_iryAkP3JHVnhYPXB5UhOWlNEBfOMTDMU6qT3dx4Xx43R8VUeFifrBHnE8fPXmlsLcOC1aaLJZLWsfHND5c2A7My22FBZERl3U2KjCyZX-l_ihSGAVG--k0BHrhzXqujyD8TwTdLsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بستنی میوه‌ای، پادشاه فصل تابستان
🍦
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/akhbarefori/670306" target="_blank">📅 22:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670305">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBank Maskan | بانک مسکن</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68c4e1f16a.mp4?token=vVrX1ULMRH44AK3MdiPaPaFoOcuJUO6WqsoEvNzQIqet2GrwoxjvZtmeUMQkvL4r1yD2USm6BmvRcZidiky4DaB-BQXMZmTRXux_pTNkXcqicY7hZJmNl1XQ2XAvdnsS5unZeQg-KyL7mflTdvpamE1My5axV1WjmGf22voKlErc3uOqNJ4I51tUYJOVx-Slrt_gZZQJXwk6WFj37fWZDp7_6zpHzq_42sSY43vNkEdJa7ZIISgFxA9BQWRE9yr3_CKmd_zYAY9oq9aJ6AV-sevRwpiDCdU4j8Kqmy_S3vFF59UBvdpKL5we4BeW6b0pjQIVFyJV1SvJ0s6-ZcyA4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68c4e1f16a.mp4?token=vVrX1ULMRH44AK3MdiPaPaFoOcuJUO6WqsoEvNzQIqet2GrwoxjvZtmeUMQkvL4r1yD2USm6BmvRcZidiky4DaB-BQXMZmTRXux_pTNkXcqicY7hZJmNl1XQ2XAvdnsS5unZeQg-KyL7mflTdvpamE1My5axV1WjmGf22voKlErc3uOqNJ4I51tUYJOVx-Slrt_gZZQJXwk6WFj37fWZDp7_6zpHzq_42sSY43vNkEdJa7ZIISgFxA9BQWRE9yr3_CKmd_zYAY9oq9aJ6AV-sevRwpiDCdU4j8Kqmy_S3vFF59UBvdpKL5we4BeW6b0pjQIVFyJV1SvJ0s6-ZcyA4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
چهل و ششمین مرحله
#قرعه_کشی
حساب های
#قرض_الحسنه
پس انداز بانک مسکن
#زندگی_در_دستان_ماست
🔹
۶۰۰ کمک هزینه
#خرید
یا
#نوسازی
واحد مسکونی به ارزش ۲/۵ میلیارد ریال
🔹
۳۰۰ کمک هزینه خرید
#وسیله_نقلیه
دوستدار محیط زیست به ارزش ۵۰۰ میلیون ریال
🔹
۳۰۰ کمک هزینه خرید
#لوازم_خانگی
تولید داخل و صنایع دستی به ارزش ۲۰۰ میلیون ریال
و صدها هزار فقره جوایز نقدی دیگر
🗓
#مهلت
#افتتاح
حساب و یا
#تکمیل
موجودی تا پایان تیرماه ۱۴۰۵
◀
#حداقل_موجودی
جهت شرکت در قرعه کشی ۱ میلیون ریال
🏆
هر یک میلیون ریال در هر روز یک امتیاز
🔗
جهت کسب اطلاعات بیشتر به لینک زیر مراجعه نمایید.
👇
👇
https://bank-maskan.ir/g1405
@bankmaskan</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/670305" target="_blank">📅 22:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670304">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIa2wxeGe8JJTvKLH5e28dRAI-Uhdrak97DozGxmdNPaAJx5r2kuIgUmt5BGzzLN0oxvk7IvVvYEtny2YvRc-5mZrDVw4iPjGqp03o28HlyzBs6HKuursS_pgQETOUz-OCmw4h1YJIpj6Xrn9UpqNiu8eiYNK5suBGEY3b8o4fdchKouy2elseTK27KAbW5eGrsAVyNwqjolWiKBzk68KGcH7PL_ysJZcenWFyKS8O-K1-Ib6NqccyaIQlWQN9U7-bkqQOIwVeJEAf4Irfz9TSpC69EsKzyeDpdbRt668m3XHRK_c0QBAxdFqwRz-ORNY0ZNwbElL6o2WLeYLXxmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الکساندر دوگین، از مقامات نزدیک به پوتین: احتمالا موساد، گراهام را ترور کرده و به ترامپ پیام می‌دهد: «نفر بعدی تویی»
🔹
محتمل‌ترین سناریو این است که موساد گراهام را ترور کرده تا ترامپ را به جنگ تمام‌ عیار علیه ایران تحریک کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/akhbarefori/670304" target="_blank">📅 21:58 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
