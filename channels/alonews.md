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
<img src="https://cdn4.telesco.pe/file/SCNDJvpLe9ryw6ZYHRC0G8-arji2s-I_48XobwpVxRZzDzjW8RmIIHtsYH1CozwxvER-GNVtP5C9uUO4JUBoomHneXtD7ilh-UTw0nxwpXnav-YBn7xTtwxzCrbLAF8n_8FfDMhjrz7XmGGosLG8Z41KV4iEwIEhOd7zpb7SVlUxYZyCKJmhq2AhzW2go2Wc0Bhr1RieNNz24xL60wrxl8tjiq9BITvcpyJQQAjBsou88LF0ktPzN9k15lBtOxfCYNW65W7KqNSfI2m9F4j307IsOuId6p7r7celpO3Q1NPzbqrp6816p3jzWKUcR6aRkoMF8Opk_q7hdEhIWxeoqg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 939K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 22:23:10</div>
<hr>

<div class="tg-post" id="msg-135752">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
خبرگزاری عراق: نخست‌وزیر عراق در پایان هفته از تهران بازدید خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/alonews/135752" target="_blank">📅 22:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135749">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A8rKz6nawNYrkvjiEjK1Th2hHrsBoKACd0908jfA3ACQS-k-JCteFCYUOTApj0ICfl4GhNEt5QbDTpRMMLNeGTBtxIW9swaFw0ariJffFmaaK04CzOF6Q1A8JPCsOC-4tY4izGXI_bhhRYjwmc1HGyrzckyxZJ5OvwcWytY8MQuQMb0wZJcDWJgZZxZEeq7GY5qwLoq2RcThgmAgDOPWoxd0dJNQJL8nnJlnfX1ENFhFbVJ6shf4B0CLVT15KXLTgn-vT1N50F_1rhWjqrMmL0TwXWGqX2MN-I_eg6vAcezqbxxXdUKkCv20K7evOshXEHLkupFMWNTJELTsvEDUpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mvp2Of2lhq4nSf7KbI9H_xjbhjDaKqBmaiauCPKrCUd3nDpVnaAtsvZ8taRv6Rv0yh_d3_zhfPGQ3H8bETe4hKUstqwFmojAzNzQeePffm8FOjApFOTGlYxBsYfQxoCGW0XOfcrZ_E9izZH-29wx6FddI4uSYexfSRhHGThtxp4eOjsOBvhagT8_IqN5nhLzN_Vt9eGjrCLxz_9tWQft5JNcsmV_Hpgl2-P-VfiJe0Qmkl_oJY6swZF6gJQHPxNn6zX3aGkY4Fpwyqm4b-KEmNjf5l31lSEaepvme3P7GcQ7ql5gB_zOwarmpB_Z_IY-Sbe2Whxq0Vyfp0xuyCo9-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q-q6_ezigMdcXLN_XAuBf_5XqJqf2gI_yAMk40KKCWXR-8Ir0Eorf-OUbQke_wsoZXsJBRJlTZ9ApfJpmpa8pqBaBn7teZKXWvm9YE64mkizW37JW4SzUYGxHJcBVH-5GM5C8BNs_n_fgWMv0fUO7QJTyLL1jN3Afgsnnf_Il9IuHsDQNpD9i64WUPt3NIFksGlbK4Kj8XNSPe1vlxPcQ5lLcp95TQLbD1IVF6FWVROUbtpdGKs1HasbEy6WcNBJOJboGcdk-N_-SN4d2GZvEk9kPCiRwCAtFNeD7WwQ0kJ7Msh4cHbRtsDtlP4lW8D1akWoB0rqeXUnCFxSQpRcuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ در Truth Social:
کاشت درختان زیبا در کاخ سفید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/135749" target="_blank">📅 22:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135748">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
کانال ۱۳: ترامپ به میانجی‌ها گفته اگر تا پایان هفته آتش‌بس نشود، باید خود را برای تشدید تنش آماده کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/135748" target="_blank">📅 22:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135747">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
بر اساس اعلام مقامات آمریکایی، ایالات متحده جنگندههای اف-۱۶ و اف-۳۵ بیشتری را به همراه هواپیماهای سوخترسان به خاورمیانه اعزام میکند.
🔴
این اقدام که پیش از حمله اخیر ایران در اردن که به کشته شدن دو سرباز آمریکایی انجامید، دستور داده شده است، همزمان با افزایش تنشها با ایران صورت میگیرد.
🔴
به گفته یک مقام نظامی اسرائیلی، ممکن است برخی از این هواپیماهای اضافی در پایگاههای هوایی نیروی هوایی اسرائیل مستقر شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/135747" target="_blank">📅 22:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135746">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
استدلال این هم وطن کاملا درسته که میگه سرباز آمریکایی سگش شرف دارد به کل جمهوری اسلامی و طرفداراش
🤔
هرچی از حرام زاده بودن طرفدارهای جمهوری اسلامی بگیم کم گفتیم.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/135746" target="_blank">📅 22:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135744">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N9J2o-n4bdZaHgj4F562i3OoWq-relBgq0P2T5SzmJ90ZoyNXtlJ0OdLt1VmaLTJyjOnqydOL402jvBwy0AFJR6T3eprtnNEO_opEBNvbaDfL5YYaiuXxolqSLozgTtJzQpUW1A6PNG68fK4URdsj1Wx2qvqKOo28Gp1UTOYBjk7VBPfOHXM7kdEyAxN3bquhfohjI-KawEWktIFwaY86TS_8YWDSHb8mv8r9miFwFETb4hkuXHNOlTNHbFhdkjPBl9-5D6_qNicmUs6IE4-fG0i-eO2sjEHim6J4CUuxbMP-ERM6W_ipUviVNa7rwyFDYym-FU2uBqpiiIISaKWuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fUa80J9WwaafcLAnyg3fTFHNd1C_C0dgVvh6JPDLQrhbngeJcClRFVej1YB5Zzp3Az2wfRh8_Sg2VL11x9uTivB-xa7HuW9kuDDGlDAi_RR91PxCZZbdmf-qTjMFao9O6POE9-N4r01MUHQySlUV--L78lE7uybLbvbx-AQne1eOexKmIQYcwguEO2KWmDDnf2Aa917intRywGu3IIzh2ZBN0_IUFcJhI47QBNdAvkuazHe8N7bHYTFSy6F4imvt4_g3UQtfyBbit-l2yqMNX5ZdBRiXqNfGm4eYqPj2ukkDm15UGUCXm5mjpl2uLmVgQImJhPUeUjFMfc9RTDANMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای منتشرشده، آسیب به پست برق یک مرکز داده بتلکو (Batelco) در بحرین را نشان می‌دهد.
🔴
این تاسیسات به عنوان یک مرکز فرماندهی و کنترل نظامی ایالات متحده و هاب پردازش داده‌های هوش مصنوعی عمل می‌کند. تصاویر به نظر می‌رسد آسیب به پست برق را نشان می‌دهند، در حالی که خود ساختمان مرکز داده ظاهراً سالم مانده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/135744" target="_blank">📅 22:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135743">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نیویورک‌تایمز:  دسته جدیدی از جنگنده‌های F-16 و F-35 از پایگاه‌های اروپا در راه خاورمیانه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/135743" target="_blank">📅 21:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135742">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
وقوع انفجار در اربیل عراق
🔴
هنوز جزئیات بیشتری درباره علت انفجار یا تلفات احتمالی منتشر نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/135742" target="_blank">📅 21:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135741">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
شبکه کان اسرائیل:  در حال حاضر، ایالات متحده می‌خواهد اسرائیل را از دور جدید تشدید تنش‌ها دور نگه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/135741" target="_blank">📅 21:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135740">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb133ceefe.mp4?token=cWS-sBaiZAeg56ShTRbpwPYzMzC1-i5QSLJvGV2q3INTu2IUxv3174YSxiwuhAivxb1fMqv74eWU4JH6xBJ6joYXJHeTkLOQTigK9iGF2-QGTd-Xx_JWrojW98jtlukLlKwhdYa-KTwuPpGtU9SnCPE5X6jhNoEYIRrsKaPhFXsY3BpkZI_WPE4oMfeVO8krRaT69CGrtXNxhMaixIcrGvamLupHvgRsKz64w7g4yV46Hq4IVlPHBd-LE32upvU8f4bzVUb094WarL-lXyoL-W9jcyNBE1yUh3w3PHTZl_feL30yZjQdpknf8y5RaJHbMVATuFjCEbxO2bhgozxrwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb133ceefe.mp4?token=cWS-sBaiZAeg56ShTRbpwPYzMzC1-i5QSLJvGV2q3INTu2IUxv3174YSxiwuhAivxb1fMqv74eWU4JH6xBJ6joYXJHeTkLOQTigK9iGF2-QGTd-Xx_JWrojW98jtlukLlKwhdYa-KTwuPpGtU9SnCPE5X6jhNoEYIRrsKaPhFXsY3BpkZI_WPE4oMfeVO8krRaT69CGrtXNxhMaixIcrGvamLupHvgRsKz64w7g4yV46Hq4IVlPHBd-LE32upvU8f4bzVUb094WarL-lXyoL-W9jcyNBE1yUh3w3PHTZl_feL30yZjQdpknf8y5RaJHbMVATuFjCEbxO2bhgozxrwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شبکه کان به نقل از مقامات ارشد اسرائیلی: ترکیه تهدید کرده بود که در صورت حمله نیروهای کرد«گروهک های تروریستی» به خاک ایران به عنوان بخشی از عملیات زمینی به رهبری موساد با هدف سرنگونی رژیم، از ایران پشتیبانی هوایی خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/135740" target="_blank">📅 21:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135739">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
منابع الحدث:وزیر کشور ایران فردا در اسلام‌آباد با مقام‌های ارشد و رهبران پاکستان دیدار خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/135739" target="_blank">📅 21:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135738">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
انفجارهای مهیب کویت را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/135738" target="_blank">📅 21:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135737">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
کان نیوز به نقل از دو مقام اسرائیلی مدعی شد اسرائیل ممکن است تحت سه سناریو به حملات علیه ایران بپیوندد:
اگر ایران به اسرائیل حمله کند، اگر اطلاعات اسرائیل تشخیص دهد که ایران در حال آماده شدن برای پرتاب موشک یا پهپاد به سمت اسرائیل است، یا اگر ترامپ رسماً از اسرائیل درخواست مشارکت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/135737" target="_blank">📅 21:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135736">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
نیویورک‌تایمز به نقل از یک مقام اسرائیلی: واشنگتن تصمیم گرفته است هواپیماهای سوخت‌رسان بیشتری را در پایگاه‌های اسرائیل مستقر کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/135736" target="_blank">📅 21:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135735">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
کانال ۱۳ عبری : پیام ترامپ به کشورهای حاشیه خلیج فارس: اگر ظرف این هفته آتش بس حاصل نشد، برای تشدید تنش با ایران آماده باشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/135735" target="_blank">📅 21:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135734">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
فوری/وزارت خارجه قطر: پیشنهاد جدید آتش‌بس را برای ایران و آمریکا فرستادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/135734" target="_blank">📅 21:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135733">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
الجزیره مدعی شد: خبرگزاری رسمی اسرائیل به نقل از منابع اسرائیلی و آمریکایی گفته که واشنگتن به اسرائیل اطلاع داده است که قصد دارد حملات علیه ایران را در روزهای آینده تشدید کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/135733" target="_blank">📅 21:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135732">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvxUFBwJaNRjtSDlX4mGUErXg4LC0SubmOuSxfsl5pW_wyUiPQ-5vwSODedbuLBOP72pKZzDqatvFBF_8S695-H0WJzbhfQ8wAJZTy946x6HYNMvhjQZE0i5i4zoPS24oP7pZyHfMa1Szq2d5Oxjd8WMvTH9NZ-w4oSOS0f6DG8zsfBhMMao5pPqFnh_Sh_zMaCYNkZ-jlxwA-paEm3s3LmrMg2wuIwiUFcg5_Iqudf__rUJvIph4gj3YY9Sd1CbB3rb0LytjctdU7X8LMP-PP04OJMHgf3IonHPakUdHFbIhzPFdiwVoH-RLlfRVSq9SuavKwqxtXSbfcyvDQhfYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیژن مرتضوی و تام کروز قبل از شروع فینال جام‌جهانی در ورزشگاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/135732" target="_blank">📅 21:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135731">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
خبرگزاری وای نت: انتظار می‌رود تعداد هواپیماهای سوخت رسان آمریکایی که این هفته وارد اسرائیل می‌شوند از دوران جنگ پیشین نیز بیشتر باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/135731" target="_blank">📅 20:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135730">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: ممکن است آمریکا از اسرائیل بخواهد به کارزار نظامی بپیوندد
🔴
برآورد اسرائیل این است که ایران طی روزهای اخیر در حال بررسی و بحث درباره این موضوع بوده که آیا به اسرائیل حمله کند یا نه، اما تاکنون هیچ تصمیمی در این‌باره گرفته نشده است.
🔴
ارزیابی دیگری نیز حاکی از آن است که ممکن است آمریکا از اسرائیل بخواهد حتی در صورت عدم حمله ایران، به کارزار نظامی بپیوندد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/135730" target="_blank">📅 20:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135729">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
فوری /
شبکه 14 اسرائیل
:
ایران به دنبال یک حمله زمینی به پایگاه‌های آمریکایی در کویت است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/135729" target="_blank">📅 20:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135728">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
نیویورک پست: ترامپ در دفاع از جنگ با ایران به کشته‌های ویتنام اشاره کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/135728" target="_blank">📅 20:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135727">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
تسنیم: گزارش‌ها از شنیده شدن صدای انفجار در استان سلیمانیه اقلیم کردستان عراق حکایت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/135727" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135726">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری/وزارت خارجه قطر: پیشنهاد جدید آتش‌بس را برای ایران و آمریکا فرستادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/135726" target="_blank">📅 20:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135725">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
وزارت خارجه اردن اعلام کرد کاردار سفارت ایران در امان را احضار و پیام اعتراضی این کشور در خصوص حملات موشکی را به او ابلاغ کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/135725" target="_blank">📅 20:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135724">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
وزیران امور خارجه عمان و اردن نسبت به احتمال تشدید درگیری‌ها و وخیم‌تر شدن اوضاع در منطقه هشدار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/135724" target="_blank">📅 20:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135723">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rptLhJn_GHwKElnwuBRTwlnfcYUkNNMBW1RtOdRRntkncA0wjSCtxM44C4UUXBl1TOxMWJ204bhJSpBSm3g-CxTCB1Mf_3MWfTdlPnXv41AszM6F8FwOOWbp0W60pfb_j7yLZmtN_83F0ye-duMsWjY5bY53xOnjEryhRhlGlcVsiNhsTB_LEzX1nrzM5f3pQRPCUSIWFWCViPo8j5eNvh2MAVIRvXPR_aYOsInTBmUWdcZClS0sL8nwy9VHXSuw5iWgQ84m96EUaFdLKEp7g4FSqPwVJmQjwCU2qz6cxfEhcHegAjDnbSdV11hBp-f2TPykncZ76GewdNp-kPrczQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کویت اعلام کرد که نیروگاه برق الصبیعه برای دومین بار در دو روز توسط سپاه پاسداران انقلاب اسلامی هدف قرار گرفته است که منجر به آتش‌سوزی و اختلال در چندین واحد تولیدی شده است.
🔴
تیم‌های امدادی در حال تلاش برای بازگرداندن عملیات هستند، در حالی که مقامات می‌گویند شبکه ملی برق همچنان پایدار است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/135723" target="_blank">📅 20:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135722">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه آمریکا و جوزف عون، رئیس جمهوری لبنان درباره اجرای توافق موسوم به «چارچوب» بین بیروت و تل آویو که در فضای داخلی لبنان مورد انتقاد است، دیدار و گفت و گو کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/135722" target="_blank">📅 20:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135721">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f004577c.mp4?token=HTho3PVvSs3MRgmZcFqh-IFlwizU12S1YarGng_SSGEgbnZ4AY2NnDOef53eFeTjmyPf9f4o0rzBrq-pI1dSFkPFiyCFbg6qRpl3-yYB7kQKTx9WbJrBQrCCQ4jW06wl-iAKM8s8GtPNee5QqH-xfLyF_Fmpu7bivJSxuQaDRui3owtfTUz5SBQSzLTJQZp3azT84Yt3mXrKyPQaCH-Rvs0xBH78Uehk8NdUG7bZij-jRKgWn2rjZeAeHF-721Ji5hh7gKhErwKOqjp3lyRyRpTUcVqUIY002n5of0230PoW3gHY8cuZjXMTYKMVegp98uDnMtc3Oso7htFvIw9ycA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f004577c.mp4?token=HTho3PVvSs3MRgmZcFqh-IFlwizU12S1YarGng_SSGEgbnZ4AY2NnDOef53eFeTjmyPf9f4o0rzBrq-pI1dSFkPFiyCFbg6qRpl3-yYB7kQKTx9WbJrBQrCCQ4jW06wl-iAKM8s8GtPNee5QqH-xfLyF_Fmpu7bivJSxuQaDRui3owtfTUz5SBQSzLTJQZp3azT84Yt3mXrKyPQaCH-Rvs0xBH78Uehk8NdUG7bZij-jRKgWn2rjZeAeHF-721Ji5hh7gKhErwKOqjp3lyRyRpTUcVqUIY002n5of0230PoW3gHY8cuZjXMTYKMVegp98uDnMtc3Oso7htFvIw9ycA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کد عجبب عراقچی
‼️
🔴
مجری: آتش بس با نظر آقا مجتبی هست؟
🔴
عراقچی: این چایی
دکوره
یا برا خوردن؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/135721" target="_blank">📅 20:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135720">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
اتحادیه عرب تحت کنترل عربستان خواستار تنش زدایی فوری میان واشنگتن و تهران است و از هر دو طرف می خواهد به مذاکرات بازگردند و از تشدید بیشتر در منطقه جلوگیری کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/135720" target="_blank">📅 20:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135719">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkwgKebO1nxo4DDT7AVUPbdadVk26ECSavZzgpdS2YJObR0SpNX0SsFWLw7YBuCcLOlsu7A0Nz0AJCHYxL8td2FTxya3cEk5_ZuzkB5mENUj0KbJV8mtggAKxT7V5MAd8mlBA-A0JazgaynQ_V4Buy5o6K-xzynycNrVaU-rNmkIjDsk_RIR3PcPYgie-Ku_wsNn4a9DV5rOwi058bbI6eAWCOOiG1fuAwbY1i42P0IstduLWl9T7FwsH6SyQB5Rivon7ltcornej9CKzfNBuHpOF_FZ2WL05vjeV7rEcypLqFMGMrXLi-b3nPWZw4tISUIMmgM5DwDaamvM6tfC8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امشب ترامپ جام رو به تیم قهرمان اهدا میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/135719" target="_blank">📅 20:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135718">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83cb4f4b3b.mp4?token=JzIBNMNuKJgjPxowB8EUOWUgufy6N7Gps8ApfWNqAYUgBv098PsjTpFHG7HfsqjD28tmUJ3Ck3hqIb0ob_Xo-kW37PKy2Ijhi3HbNhuXZgC37gPv1s_HMAoPX_Pxk09SZCrYLL1cSSwomArjDjzOt_wdIr9u-Gcr-oUaxC9or9BJJSiki5-HG8vTJu2t_lsbk6oCUOVgvQnFX7dTpvc3s16ihmFxs9FAGv6OKxPfXm4T7JQJNkepEa32VyJRK45_k7gN8cIx-rczWiYG41vZh09EHmw19YBeMa90rfMt3_C8EDz4lYDrhSY4JA6M6V87Hp6WFeEqG13bsMsizxvJ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83cb4f4b3b.mp4?token=JzIBNMNuKJgjPxowB8EUOWUgufy6N7Gps8ApfWNqAYUgBv098PsjTpFHG7HfsqjD28tmUJ3Ck3hqIb0ob_Xo-kW37PKy2Ijhi3HbNhuXZgC37gPv1s_HMAoPX_Pxk09SZCrYLL1cSSwomArjDjzOt_wdIr9u-Gcr-oUaxC9or9BJJSiki5-HG8vTJu2t_lsbk6oCUOVgvQnFX7dTpvc3s16ihmFxs9FAGv6OKxPfXm4T7JQJNkepEa32VyJRK45_k7gN8cIx-rczWiYG41vZh09EHmw19YBeMa90rfMt3_C8EDz4lYDrhSY4JA6M6V87Hp6WFeEqG13bsMsizxvJ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف حق جواد کاظمیان: من الان زن بگیرم که چی بشه؟
به بچه‌‌ای رو به دنیا بیارم که چیکار کنه؟
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/135718" target="_blank">📅 20:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135717">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d827bf4609.mp4?token=JQfuJ64VZM2kPqvhzrj1vsP1s4ebWW4qVazCFgvQ0JzbzQ3n48HfkML7Ac2dcfUib5r9-ZgWYTWM5k6FCiFOhX_AS8FQKHotfippAlmkptjQpUNvlesKctZz_WMWIkQC76ffpclCSeJIP8dBQAUQz8bDrH5_RnsEpDpHCtZxPzoA99zs9NVwrlO9jwU5KvLZLwvf9eCNaAtd2k8y2iIzaqzcow3sS8kDk0fMzNik0h9Opzq-H2e4Y0Bpmd1NPLJq5RCWCNuaPRb3ekRgZGmaf11jTqXftH3oK7e_KmLHV7FUPt3sjbJpfSSh8qEaG6PVnFCLhKKAh1qU5bu8Vf3yqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d827bf4609.mp4?token=JQfuJ64VZM2kPqvhzrj1vsP1s4ebWW4qVazCFgvQ0JzbzQ3n48HfkML7Ac2dcfUib5r9-ZgWYTWM5k6FCiFOhX_AS8FQKHotfippAlmkptjQpUNvlesKctZz_WMWIkQC76ffpclCSeJIP8dBQAUQz8bDrH5_RnsEpDpHCtZxPzoA99zs9NVwrlO9jwU5KvLZLwvf9eCNaAtd2k8y2iIzaqzcow3sS8kDk0fMzNik0h9Opzq-H2e4Y0Bpmd1NPLJq5RCWCNuaPRb3ekRgZGmaf11jTqXftH3oK7e_KmLHV7FUPt3sjbJpfSSh8qEaG6PVnFCLhKKAh1qU5bu8Vf3yqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
استدلال این هم وطن کاملا درسته که میگه سرباز آمریکایی سگش شرف دارد به کل جمهوری اسلامی و طرفداراش
🤔
هرچی از حرام زاده بودن طرفدارهای جمهوری اسلامی بگیم کم گفتیم.</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/135717" target="_blank">📅 20:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135716">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل به نقل از ایلی کوهن، وزیر اسرائیلی، گزارش داد نشست‌هایی میان اسرائیل و شماری از کشورهای خلیج فارس برای تقویت مسیری جایگزین تنگه هرمز برگزار شده است.
🔴
کوهن مدعی شد با ایجاد این مسیر، ایران دیگر نخواهد توانست از تهدید بستن تنگه هرمز به‌عنوان ابزار فشار استفاده کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/135716" target="_blank">📅 20:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135715">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-8HeoAfzvBspuEk0VaFapLM2N4NClRv1p0VuFJGFqpgLG8ev0YC_Ph-JmNh9XotQl4Kg70xzpcb5fKPL_BkwHFtBIo7Fn_MJt7_VCXLSoiqggdHLG4Jc-Xl7iywZJRLZTTSK5z3CJacks1jLxOP4HLZy8_X3IbRL3lMrd2j7PY0FO9W9Gi721C8f_HDLXF_lXKWvFuBM5-joJe06M967b-_R_FzbtfDoD88xC0TGtw7W91vap5OajHa5HwKlonFT4JQzlANi9TasnskiUNWbHkAzTuW7SLDcsfXEhQQR4TEpZm7Vtw2nwoz85ACwbnDxnTmgNsvwl4sk7-w5BNw0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیافه پزشکیان قبل ریاست جمهوری و دوسال بعدش
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/135715" target="_blank">📅 20:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135714">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
رسانه عبری: تا نهم مرداد تخریب صدها ساختمان در دو منطقه لبنان تکمیل می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/135714" target="_blank">📅 20:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135713">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF): کمی پیش، نیروی هوایی اسرائیل یک پهپاد را در منطقه مرز اسرائیل-سوریه رهگیری کرد.
منشأ پرتاب در حال بررسی است.
🔴
سیگنال‌های هشدار طبق پروتکل صادر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/135713" target="_blank">📅 19:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135712">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
فرمانده ستاد کل ارتش اسرائیل :
اوضاع ایران رو لحظه‌به‌لحظه زیر نظر داریم
🔴
سطح آمادگی‌مون بالاست و هر لحظه لازم باشه، آماده‌ایم دوباره وارد جنگ بشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/135712" target="_blank">📅 19:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135711">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff128e3610.mp4?token=aeEx5oU4yaR68FAh_JmyzrV7HOOwQeEs0T_P0JR2Hing6ZYNXGPU2wJL-DM18WXQYh2WHnhcbooxoKKoI6r8M1InSHo3f3Tn1-EznlmtHuxZ5CRAGDX4inbSXYxn8LT5QIrM9pbztnSEkv4ccNXPwqPjLfAkvYCFexAsZuTsPsfzWw_XOfTlaMP2-FNHZGqmzdlpdYAQmeIJRJ2wu_HP0UBJZgMAufDIJ9VX3UJwFLVtrkdchFrHjprt2DAfKR9k7FXpNmjOmyHQ6wyTnuTz755sdpddEzD8o5c93tph0OuBs_dfvRUZZ9FyIkRW8YHt5eOCzyS2SOXMMsNU7tjZwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff128e3610.mp4?token=aeEx5oU4yaR68FAh_JmyzrV7HOOwQeEs0T_P0JR2Hing6ZYNXGPU2wJL-DM18WXQYh2WHnhcbooxoKKoI6r8M1InSHo3f3Tn1-EznlmtHuxZ5CRAGDX4inbSXYxn8LT5QIrM9pbztnSEkv4ccNXPwqPjLfAkvYCFexAsZuTsPsfzWw_XOfTlaMP2-FNHZGqmzdlpdYAQmeIJRJ2wu_HP0UBJZgMAufDIJ9VX3UJwFLVtrkdchFrHjprt2DAfKR9k7FXpNmjOmyHQ6wyTnuTz755sdpddEzD8o5c93tph0OuBs_dfvRUZZ9FyIkRW8YHt5eOCzyS2SOXMMsNU7tjZwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کره شمالی: در کنار روسیه تا پیروزی نهایی ایستاده‌ایم
🔴
چوی سون هوی، وزیر خارجه کره شمالی در دیدار با ولادیمیر پوتین در کاخ کرملین، بر حمایت قاطع و بدون تزلزل پیونگ‌یانگ از روسیه در جریان عملیات نظامی ویژه تأکید کرد.
🔴
وزیر خارجه کره شمالی رسماً اعلام کرد که کشورش تا دستیابی روسیه به پیروزی نهایی، با تمام قوا در کنار مسکو باقی خواهد ماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/135711" target="_blank">📅 19:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135710">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
حمله ایران به نیروگاه برق حطین در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/135710" target="_blank">📅 19:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135709">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
فرماندار جاسک: آب‌شیرین‌کن بونجی که در پی حمله موشکی آمریکا و اسراییل آسیب دیده بود، کمتر از ۴۸ ساعت پس از حادثه، امروز وارد مدار می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/135709" target="_blank">📅 19:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135708">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
فوری / رسانه‌های عبری: ارزیابی‌های امنیتی اسرائیل نشان می‌دهد فرماندهی ایران دستور حمله به اسرائیل را صادر خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/135708" target="_blank">📅 19:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135707">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
رئیس هلال احمر:  در تشییع میلیونی نه تنها یک فوتی هم نداشتیم بلکه شاهد چندین تولد نوزاد نیز بودیم :/
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/135707" target="_blank">📅 19:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135705">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uNMZOLJ9WO2S0uVSL0F4eRs44vhR3EDKemhGLsXTxsPWFqt3z22uZ6yPA5vuzFNjvReNzecvehhm_Ck5RqF7FUoDrVIDZK2WoRs0OTTFUE4cwREHo8lXVQmQA8qgFWfYMiHsS8xfDkLCiAMqj0Z6in-rKxxu8cqb8iX54L9MAllr24oVlTKZiHyfxwS8WqU938gQAkxawLCsBOrAsa91y814UbMlAfOIOHhCN324TMEVtF_kN6z0LLjXsEirNfKp26Znz77Z1ZFOrpFC6q4C29bhWFqNMnUf60SkzmeRbLCnF7qSn6601j8ItWdvY3h0uhZCOTkKXZnb3T5jXEounQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/grWmE24n9SVeErMreeU9IHERupqdJxXTbVKCb5WIyeFLLkBrCWcP5eKBHQZLPwf-Vkjk3srxjoh0ih7MT1LfRlQVBoe6ICt40hJDZ3CGcgIA1hxVJ7G5c_GuRJ4qblQncoQJ2N3m_rYsCHyD5zcZsvHXHQcUHClp03wUb-iiunGLevJNeCbm0vHqjeHZPBCsbpHm9dAmNGFRCAuFtuAQfhWy3EDxr1F690z08X4A0D3sXiGYt7MpHhYI-oCZh1rdJNOtw3ojEW3OKNAt2IZcWB91xRjjElQFGsqb1n_4jMBiBTDTg0rg5czmQKO7Xw7FXGZbiGbcywqHfDDHqN1YUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از انهدام انبار مرکزی قطعات لجستیکی نیروی هوایی آمریکا در پایگاه هوایی العدید قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/135705" target="_blank">📅 19:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135704">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7091c7c4c.mp4?token=TeIz9GfpZmFKnC7tfJH0ZbyGxzxC4WE4LIj6b5ARltYOskN3sja-g8urEKz2_GE8AjpIDNMapX5nvFI95A1Vnxrq2x5FH0fYnZzqoxobIQHBt-__6IrSFKiNxwiVQfNnL42Jmqiufi3VUpVZtY3oIWf5jBQlgEOKQNfV0PraxY88pyUDUUp-LKGjWdPVf0-q8uLIEpsGr8DPOmpDbqr9rOTZj2qnytL2vWBW-VJOXsUK3tav3Y0HuKZR-gvOt6qznMeb6Nz8oU3soq2O2vxKBXd_qFHblHviqf05KsBdym2LgOBcGnLoI5-0Gm_rIa58EUM8ONM7roFykl4vh4z4ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7091c7c4c.mp4?token=TeIz9GfpZmFKnC7tfJH0ZbyGxzxC4WE4LIj6b5ARltYOskN3sja-g8urEKz2_GE8AjpIDNMapX5nvFI95A1Vnxrq2x5FH0fYnZzqoxobIQHBt-__6IrSFKiNxwiVQfNnL42Jmqiufi3VUpVZtY3oIWf5jBQlgEOKQNfV0PraxY88pyUDUUp-LKGjWdPVf0-q8uLIEpsGr8DPOmpDbqr9rOTZj2qnytL2vWBW-VJOXsUK3tav3Y0HuKZR-gvOt6qznMeb6Nz8oU3soq2O2vxKBXd_qFHblHviqf05KsBdym2LgOBcGnLoI5-0Gm_rIa58EUM8ONM7roFykl4vh4z4ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: آرژانتین امشب قهرمان جام‌جهانی میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/135704" target="_blank">📅 19:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135703">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa71ce2aae.mp4?token=lXI3OnHz5jYEXJvIOXoQjV9La5jivLRfNjYnVYnR7HtYHFlfyeul0P9Z79DNrgvrp6MqiumlsAqM416thckTtr_qF1B2ommv-c3Rs0rfF63XQvUTmBVIpqYHb4gIV38APm5XnefME-LV0j3K1nrOTk1ya13e8zysihAFFmkOz5RIYDWHL2A1B3Tg4sjHv3h3CcsWjIwn8VssS5Wnd4J-Mgo00FogUYKk1zIDvuhnTZ9SRf4xEqjRVJepCbLyd02YRg6v5u7jHNLqtLa3HSD-nOCjg-21rcvsRR46oR9X4XRN9hmuU-kl7NgScpRJ6ZahFudgQfZLux96y62B3cS30g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa71ce2aae.mp4?token=lXI3OnHz5jYEXJvIOXoQjV9La5jivLRfNjYnVYnR7HtYHFlfyeul0P9Z79DNrgvrp6MqiumlsAqM416thckTtr_qF1B2ommv-c3Rs0rfF63XQvUTmBVIpqYHb4gIV38APm5XnefME-LV0j3K1nrOTk1ya13e8zysihAFFmkOz5RIYDWHL2A1B3Tg4sjHv3h3CcsWjIwn8VssS5Wnd4J-Mgo00FogUYKk1zIDvuhnTZ9SRf4xEqjRVJepCbLyd02YRg6v5u7jHNLqtLa3HSD-nOCjg-21rcvsRR46oR9X4XRN9hmuU-kl7NgScpRJ6ZahFudgQfZLux96y62B3cS30g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آبادان پس از برخورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/135703" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135702">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4557e032e.mp4?token=pjq4pQguuUh2iWfHpVhYON7ECONjDdQBNfxWtro1lZib-you52IvdVn5yqXFFfI15DJMhd6nvft14zb3HsHM_eyITGMUSjILEaHdSxCM9hR7BFxGHwLEy-RutYXZsxC2lNy2iZ4atuJPgkdzcE15Pkt4DULDAAOvoreiKa72G-6cG-4I7b-uEhDT1KcEYs3SZELBc8Ud-sj-WyPASfSutxWI5PDGBaf2NHS2lcsosdinSTA_VO6MySiVgOeHcMNdLRpVTGJL5OGsoLCTf0O0-saG7Yii_LGOsBi3ox1GsDzOUlxuaEcQaNV0IiMOkkyWJ1OXr0QPy4asOF3k4Ym4sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4557e032e.mp4?token=pjq4pQguuUh2iWfHpVhYON7ECONjDdQBNfxWtro1lZib-you52IvdVn5yqXFFfI15DJMhd6nvft14zb3HsHM_eyITGMUSjILEaHdSxCM9hR7BFxGHwLEy-RutYXZsxC2lNy2iZ4atuJPgkdzcE15Pkt4DULDAAOvoreiKa72G-6cG-4I7b-uEhDT1KcEYs3SZELBc8Ud-sj-WyPASfSutxWI5PDGBaf2NHS2lcsosdinSTA_VO6MySiVgOeHcMNdLRpVTGJL5OGsoLCTf0O0-saG7Yii_LGOsBi3ox1GsDzOUlxuaEcQaNV0IiMOkkyWJ1OXr0QPy4asOF3k4Ym4sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مربی بی سواد: از نظام عزیزمون میخوام با عادل برخورد کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/135702" target="_blank">📅 19:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135701">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/853ed69eaf.mp4?token=hhFa1wN4B4kKszi9s9ig-i2AnRfiTej1qcNnEnLPXDZj_4-xrEAbrOnE_A6fTifblZVCFagGQaAMSvcS1kU75acLfpiDyRoX9bsjj8js4uLWlEkh0IgQBSLosZfhcx9Pzetl5jznAP8hZh4HIL73FI4Hu23m4UEfIKyv3HXZm6U_gMd8hpYehEmCUl1pKGCOOpojGYX0v4xHgddASsLe-MD1GddbfKmg78O3bL8zCgr8dnd8QcY70mZxiAvhB03tvbimGevUZj8bYLywPxCq2pbYALdfRqeGCYSbmgKsnWMdKv94Qqi8m4SgZ-eQ_jucsz1yqK_MH_ZEJoA_C-V64A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/853ed69eaf.mp4?token=hhFa1wN4B4kKszi9s9ig-i2AnRfiTej1qcNnEnLPXDZj_4-xrEAbrOnE_A6fTifblZVCFagGQaAMSvcS1kU75acLfpiDyRoX9bsjj8js4uLWlEkh0IgQBSLosZfhcx9Pzetl5jznAP8hZh4HIL73FI4Hu23m4UEfIKyv3HXZm6U_gMd8hpYehEmCUl1pKGCOOpojGYX0v4xHgddASsLe-MD1GddbfKmg78O3bL8zCgr8dnd8QcY70mZxiAvhB03tvbimGevUZj8bYLywPxCq2pbYALdfRqeGCYSbmgKsnWMdKv94Qqi8m4SgZ-eQ_jucsz1yqK_MH_ZEJoA_C-V64A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جواد موگویی و عراقچی: تو ۱۸ و ۱۹ دی هیچکس فکر نمیکرد اون سیل عظیم جمعیت معترض به خیابون بیاد و چند هزار نفر کشته شدن
🔴
مشهد تو ۳ساعت سقوط کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/135701" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135700">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/135700" target="_blank">📅 19:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135699">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
موشک سپاه به نیروگاه برق در کویت خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/135699" target="_blank">📅 18:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135698">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94279117e7.mp4?token=rQB6fXWl8qZXpW17drYT9YEjMARdgIpS_ddHAsohyk5pFysbh9PNdDyhJq-XAcIEznoSxWK7c_mX7B0MrwUj5_N5X4sMJ5h4Qn91n2ufvpLtTvJsihtgOItFwX7T8HxuSDx3rRPt9itxLXFtOxOR5bXXP5-X181FlJIiXv4_Z5Qk1_aWZ31XughmBJK4Pexwv6i6d6EaET03hC-Y6Iqa60i8lo4UXNEp4-v1SQ2iDQm2dFrxYyDqw8tZlbuDrICe6dC8z4YBUtkCgCnh2v7_VIgO5yBrjyTT0WrhbTQJdUi9Czg1Q7HhbVfS9l-ZirF6BhWIOnNFXpnTVTCaT79zpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94279117e7.mp4?token=rQB6fXWl8qZXpW17drYT9YEjMARdgIpS_ddHAsohyk5pFysbh9PNdDyhJq-XAcIEznoSxWK7c_mX7B0MrwUj5_N5X4sMJ5h4Qn91n2ufvpLtTvJsihtgOItFwX7T8HxuSDx3rRPt9itxLXFtOxOR5bXXP5-X181FlJIiXv4_Z5Qk1_aWZ31XughmBJK4Pexwv6i6d6EaET03hC-Y6Iqa60i8lo4UXNEp4-v1SQ2iDQm2dFrxYyDqw8tZlbuDrICe6dC8z4YBUtkCgCnh2v7_VIgO5yBrjyTT0WrhbTQJdUi9Czg1Q7HhbVfS9l-ZirF6BhWIOnNFXpnTVTCaT79zpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک سپاه به
نیروگاه برق در کویت
خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/135698" target="_blank">📅 18:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135697">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0a2a1085e.mp4?token=AHflkUlb5Bs135J80HbHWWadUnrV09XrVfPrH-jRwmieulhvXUpPG_bexZmUCY5JSzY3P_njd9e9McVVz8tURA5Q8MgXh9ybRLlTYbPMRKZN01tSzOs5jfniz1TYVsNFXUhat7FSJzTAnKTntyJKzGBC-2wDLWSJzX-ecSTmCSeRmdTwVcQ8BBZdHih1wPMmjdxzwt4SCOdAt_Z7RDij2aHqb-J7kvSG0KUKUD_KMDOyT8XMDPxXrttHyU_b-G2GV3NFczU2wHLZqhPKT0HGl_XhhsuJplXbHZZiFZepiWSUKkbQDc5NALgYud6Cq8upk3h27E5YQq6qTBPCvCpO3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0a2a1085e.mp4?token=AHflkUlb5Bs135J80HbHWWadUnrV09XrVfPrH-jRwmieulhvXUpPG_bexZmUCY5JSzY3P_njd9e9McVVz8tURA5Q8MgXh9ybRLlTYbPMRKZN01tSzOs5jfniz1TYVsNFXUhat7FSJzTAnKTntyJKzGBC-2wDLWSJzX-ecSTmCSeRmdTwVcQ8BBZdHih1wPMmjdxzwt4SCOdAt_Z7RDij2aHqb-J7kvSG0KUKUD_KMDOyT8XMDPxXrttHyU_b-G2GV3NFczU2wHLZqhPKT0HGl_XhhsuJplXbHZZiFZepiWSUKkbQDc5NALgYud6Cq8upk3h27E5YQq6qTBPCvCpO3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند حامی حکومت:
آقا مجتبی رو اول امام زمان انتخاب کرده و بعد مجلس خبرگان رفتن ببینن امام زمان کی رو به عنوان نایبش انتخاب کرده. دیدن آقا مجتبی رو انتخاب کرده. اونام اقا مجتبی رو به عنوان رهبر معرفی کردن.
#دروغ
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/135697" target="_blank">📅 18:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135696">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
قلعه‌نویی:
میگن مردم این تیم ملی رو دوست نداشتند ولی همه رستوران‌ها و سینماها با بازی‌های ما پر می‌شد و ۶ میلیارد نفر اخبار ما را پیگیری می‌کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/135696" target="_blank">📅 18:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135695">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNsisjYDofhKdPFJx16BvFk5sHKq7CmEyGnFPpdPZi52rH5Fq-GY2xSH6Cxk0yms5OBtmafs7DLmMF30NHnB_sg2ObHqiM4OH57rtJP6dR3_eNxVgUlVfoBd-Wlx6RtKwq7anfaBbdkBcWLfNRJDk-UJxmOt1KhZMj3rXpcDAKqxiN5q6gjjShEOPtidPzxp1aKjfZLLBjY-zZCVQFsvp8Rqt5mbZACfU5XoowEUqR8pB9kJDRZBsouzFgPTzqlXmh5yEX7J8KqS-O0ghxu6IelrNqHQD_saXZq1j1TJF4SKRlO5MscH5vn5DbirPXvXJbsmusMK4wz5JR0h1lH97Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهاجری: بعضیا الکی الکی کشور رو سر تنگه هرمز به جنگ کشیدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/135695" target="_blank">📅 18:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135694">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tX70GNRhx2qnP4cjkfG7mLhY24R_JnBuu_lQExJOEJ50aHy3tcgFzlkNcD55CEj-AsJGfLS02pJaXrcHxLnlRJilUqzQCkEaRdFNiFDbQySNDPjMuRE6qA4hsJdHifOwdRn3dCcH11IX7QdybZM7wo5lNSWzh56WkoZ6P8UgIXFRORr9Pv4TQ_8cIESZCGNK2UGCVRES7AkDdp0KdhVMeF1Wk3THZOPBn2FbXzlS8sc38GGwQJF4h0X2sOkfzlUXY9EpJ1DCItoWgGA6peIWs-Eo2MgfW_5ShDlFKL0_-FOk8_TzDkLstttyJreUp6MK6kW4zww2galL9qobpTttqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکونومیست: عراق به‌دنبال نزدیکی بیشتر به آمریکا در برابر ایران
🔴
اکونومیست نوشت نخست‌وزیر جدید عراق انگیزه شخصی برای حفظ روابط نزدیک با دونالد ترامپ دارد؛ در عین حال، جانبداری قاطع‌تر بغداد از آمریکا در برابر ایران می‌تواند مزایای اقتصادی گسترده‌تری نیز برای عراق به همراه داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/135694" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135693">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
تندروهای جنگ طلب تا ایران رو به غزه تبدیل نکنن بیخیال نمیشن، یه مشت عقب افتاده ترسو عصر حجری
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/135693" target="_blank">📅 18:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135692">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
گزارش‌ها از ورشکستی هتل‌های کیش
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/135692" target="_blank">📅 18:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135691">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
کریس رایت، وزیر انرژی آمریکا:
ما در حال حاضر روی تضمین عبور نفت و گاز از طریق تنگه هرمز کار می‌کنیم
🔴
ترامپ همواره به دنبال راه‌حلی دیپلماتیک است و می‌خواهد این موضوع را با توافق به پایان برساند.
🔴
اگر ایران برای راه‌حل دیپلماتیک آماده باشد، همین راه‌حل خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/135691" target="_blank">📅 18:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135690">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HryV1gyKoZo6g7-5ydwG2MjeYy5s7YSjmmZlH36UMioaw0ky-Od6nTueSRq8I9TBsmy224LcWfG2iMCNOaBOHrSQTSgGBBYZ24iuTBIOOuo4xluXiIElM1Mz4joOhhQ8LmeCNmTCmMmdHQLFo0xbuWF7x-jePCVKUcAcmqhy4zIA7YN5s_Opq5nyBZG-dIwRg0_fehDjLaCBIj-FQ83IBULEBy8yUxZ-I5w6Ci27Z3vV87jdTrVvEryjzK2b5PtqP-CQtP7eD94qT1R_K3Wy8Wy3XjE2urAysVAEyQ0ufv_KruIVGzSjVQWqssmj0qBs6Q6HllcHw3lyvkNwM7qjEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بهای تحمل جنگ به جنوبی‌ها داده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/135690" target="_blank">📅 17:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135689">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e70751a.mp4?token=u94fZ38TygZpGzEsKA6I4woAwwWM_c45-DwKr10ws0EjD3jP4qKPokUu1ZLJuCzAhH0Ks7wvGpd4OTCftKyja_kbTSjTG63iTVInQ1VpDfx_cBafpEfD0-QVlBJXTYa3zHyhoxFIsO5PY9W8gQmJ36si-MU78i3XV9ncT9PimWpqXKvJIc9qZqHhFn24hQFV_4CJaC-Lh1wsMmrJntOIFp2f3hTVEhX-c-aXgC2erVvIN8Fq0gJvcci4cESdpSYRiKsdAz0Hh6fAbB_1O5QiXO-kT-C8stuSalp1Tfspiq38blLJ5kZOhtAg0Ozy8qFmIbMWbA4U9jcKiTQj6DL4QlUcrpQJjUg18RLuiwiScMZgvBXdDhcRKRSRjGyXuWHTCL7KWze7Igx2hOQiPNlU-SCXMz_XD3-wt4L5U44ms-SFAi1-EE_dvFr1ucG6tQHreaQfDlEfqRsd5olYY89nveBMBPeQeiB--PmE7r9yhpFanI35RDenugHwYs-iKrDAqZZd6oo1UVE86yB40FUI4DWzfTqc0HyqCyqMARsJJSL2tKmUFmuRHK3VPkAgIsxBqPh40KE866ax6Fdjf2n_NhmGI8avAVFVsYTP8tv6AJdezm6OM9hIxNeRHgdRgfYBMT7Q5sEniRGAQcLt_CCJVfxHEZAhbcjzXXeHiidJuvE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e70751a.mp4?token=u94fZ38TygZpGzEsKA6I4woAwwWM_c45-DwKr10ws0EjD3jP4qKPokUu1ZLJuCzAhH0Ks7wvGpd4OTCftKyja_kbTSjTG63iTVInQ1VpDfx_cBafpEfD0-QVlBJXTYa3zHyhoxFIsO5PY9W8gQmJ36si-MU78i3XV9ncT9PimWpqXKvJIc9qZqHhFn24hQFV_4CJaC-Lh1wsMmrJntOIFp2f3hTVEhX-c-aXgC2erVvIN8Fq0gJvcci4cESdpSYRiKsdAz0Hh6fAbB_1O5QiXO-kT-C8stuSalp1Tfspiq38blLJ5kZOhtAg0Ozy8qFmIbMWbA4U9jcKiTQj6DL4QlUcrpQJjUg18RLuiwiScMZgvBXdDhcRKRSRjGyXuWHTCL7KWze7Igx2hOQiPNlU-SCXMz_XD3-wt4L5U44ms-SFAi1-EE_dvFr1ucG6tQHreaQfDlEfqRsd5olYY89nveBMBPeQeiB--PmE7r9yhpFanI35RDenugHwYs-iKrDAqZZd6oo1UVE86yB40FUI4DWzfTqc0HyqCyqMARsJJSL2tKmUFmuRHK3VPkAgIsxBqPh40KE866ax6Fdjf2n_NhmGI8avAVFVsYTP8tv6AJdezm6OM9hIxNeRHgdRgfYBMT7Q5sEniRGAQcLt_CCJVfxHEZAhbcjzXXeHiidJuvE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهدی مطهرنیا:
تجزیه ایران به هیچ وجه شدنی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/135689" target="_blank">📅 17:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135688">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
انفجار مجدد در آبادان
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/135688" target="_blank">📅 17:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135687">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
تحلیل آینده طلا و دلار
اینجارو داشته باش و سود کن</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/135687" target="_blank">📅 17:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135686">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
فوری/رویترز: حملات حوثی‌ها و ایران به عربستان، پاکستان را به شدت از تهران خشمگین کرده و ممکن است پاکستان به درگیری عربستان و یمن کشیده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/135686" target="_blank">📅 17:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135685">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSFxKgdYZWuaIZUM-kR_7trYjVAbrZ45OF1Elx2G7FT0iDQ-VosqwVy0YMrR5g4FmFc4TKsEnapdVVi-ZQW50leiwO8eAFulIixs4sahcNqH_Q1rKQxHJE1ap3HlkpY_rRbn8kOLViWwJtJBdvsUCCgtz4pjChpFLiJQC1NzsfgaIXiv1IxcWHmHzY99SMwDS_bov3vo3nbsmBWnm0YDGe3QoNQI9FF9ushUwJdUEPnv5hWDUGi7R7QqL-UGTZre1d26vZuJ54fDTLkv1DwEIONAgH1Hxo9aRTYhcaDZBQRoxwVYsiL8WoJJ0rqTv9KSRgY3L21LVS6A1XOwhYeM-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر دفاع اسرائیل کاتز:
اگر جمهوری اسلامی به اسرائیل موشک شلیک کند، ما با قدرت و بدون هیچ وابستگی یا شرایطی به آن ضربه خواهیم زد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/135685" target="_blank">📅 17:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135684">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0fb2383c1.mp4?token=GwUSfEQvfZsvrW-F9dslcGxF5P-CLfQs819WYKH47J9CVmqt2rFhnB-rM4vh0wvs5T53PCEI7II6yXNPphYqfQ46warSWYP6oKJJeO0C5OhP18J99V5nZIHvskLmQxyYn0WrufRFa9QdMuXAkRpXDm4E0vMBfY2YISkXu4IJxB3aaWPyB3Sp0LRsOetMZjR3DplCeRH4QaZ3N3EseDEleM1odJGHkIiEJxxXG9ciPtiV_Tgfoq-qHjD0M9d7sNDaXGR-Cffi_my617nAfzm8FpXNfHMOyxZK-TR4xCjq1-dxzHHmWLCTUpVQ-ZgvHY9tVcHaVs79HlBrA6_eNgagWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0fb2383c1.mp4?token=GwUSfEQvfZsvrW-F9dslcGxF5P-CLfQs819WYKH47J9CVmqt2rFhnB-rM4vh0wvs5T53PCEI7II6yXNPphYqfQ46warSWYP6oKJJeO0C5OhP18J99V5nZIHvskLmQxyYn0WrufRFa9QdMuXAkRpXDm4E0vMBfY2YISkXu4IJxB3aaWPyB3Sp0LRsOetMZjR3DplCeRH4QaZ3N3EseDEleM1odJGHkIiEJxxXG9ciPtiV_Tgfoq-qHjD0M9d7sNDaXGR-Cffi_my617nAfzm8FpXNfHMOyxZK-TR4xCjq1-dxzHHmWLCTUpVQ-ZgvHY9tVcHaVs79HlBrA6_eNgagWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله قلعه نویی به علی دایی
‼️
🔴
قلعه‌نویی درباره ساعت معروفش :
وقتی میام ساعت میندازم و کت‌شلوار می‌پوشم، شما باید بگی به به چه مربی خوش‌تیپی ولی شروع کردید به مسخره کردن!
🔴
حتما باید یقه باز بذارم و زنجیر طلا بندازم؟ (کنایه به علی دایی)
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135684" target="_blank">📅 17:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135683">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9286ee216.mp4?token=BL3X-8-us9uToD8pHQqSyHDuLHr4rQ9qwi0AjZq5xZL7pEnBlOmKFLgTL6NKRSEb8O5EPUxg9UCGpCJ0FJga_PSp5q92sywkvEg_TXbFt1GEGkM70WfeLkX4JgtOFWP3JC9P89jEHtqx-3ViMY11kZDAGtAPcZbjvjBrQf7EtimdwEf3H7WnuwUfYkGrdMvBQ-kmX4uYJCrrVfGtSkrvyYV92EmFznieVBDgtheOhQa3A6ZtucUctL5BKaOLBQpB2r1_ii2mDuDzM3oaYRxynPTlkn79J2yrcGZTAZ2ekQCP0pZrD0ppIw_jiXLvSkdRY0UNHkjbEEBAJ3LuqhuVEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9286ee216.mp4?token=BL3X-8-us9uToD8pHQqSyHDuLHr4rQ9qwi0AjZq5xZL7pEnBlOmKFLgTL6NKRSEb8O5EPUxg9UCGpCJ0FJga_PSp5q92sywkvEg_TXbFt1GEGkM70WfeLkX4JgtOFWP3JC9P89jEHtqx-3ViMY11kZDAGtAPcZbjvjBrQf7EtimdwEf3H7WnuwUfYkGrdMvBQ-kmX4uYJCrrVfGtSkrvyYV92EmFznieVBDgtheOhQa3A6ZtucUctL5BKaOLBQpB2r1_ii2mDuDzM3oaYRxynPTlkn79J2yrcGZTAZ2ekQCP0pZrD0ppIw_jiXLvSkdRY0UNHkjbEEBAJ3LuqhuVEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اعلام کرد که یک پهپاد انتحاری لاکاس متعلق به ایالات متحده را در جنوب ایران سرنگون کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/135683" target="_blank">📅 17:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135682">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f376bb044e.mp4?token=crJ9-NnHXmt4xcrBvxVX8IjYfGNXFCzwpKjpMNuCkLz1j_xs6gqoBvczz-EGWnz-9XyIOR7Q4wtcWOozOD_28cM270AHdY5MwbfG65aT4ewwLLCv52tFlhPHZxaMmpz3_gvywlE9CkfiAbJr9XUAZaIoL3nFx8JaleDYknPEA7sYYdU9uuqFOZO5AsYPXJuLbZl9w9vnf1Z0G2jhxR7_mZ-IJXG9VYEQWA2Tr7Mo6z2OQQqPSJS7Ywfwi7KbmEMZp1ISKrJp0lIcIG9a0au-PktShsZstA2zo50euhHfHYHpK6Q6fwaYPWdefKMrUkVB_3EUA2fAt8L779IXJCO9VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f376bb044e.mp4?token=crJ9-NnHXmt4xcrBvxVX8IjYfGNXFCzwpKjpMNuCkLz1j_xs6gqoBvczz-EGWnz-9XyIOR7Q4wtcWOozOD_28cM270AHdY5MwbfG65aT4ewwLLCv52tFlhPHZxaMmpz3_gvywlE9CkfiAbJr9XUAZaIoL3nFx8JaleDYknPEA7sYYdU9uuqFOZO5AsYPXJuLbZl9w9vnf1Z0G2jhxR7_mZ-IJXG9VYEQWA2Tr7Mo6z2OQQqPSJS7Ywfwi7KbmEMZp1ISKrJp0lIcIG9a0au-PktShsZstA2zo50euhHfHYHpK6Q6fwaYPWdefKMrUkVB_3EUA2fAt8L779IXJCO9VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روایت عراقچی از لحظه اصابت موشک به بیت رهبری در ۹ اسفند: به آقای حجازی گفتم آقا اینجان، گفت نمی‌دانم
🔴
با آقای حجازی در بیت جلسه داشتم که ۳موشک اصابت کرد و از زیر آوار خودمان را بیرون کشیدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/135682" target="_blank">📅 17:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135681">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">علی خامنه‌ای رهبر پیشین جمهوری اسلامی، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/135681" target="_blank">📅 17:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135680">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
پرس‌تی‌وی: گزارش‌های غیررسمی حاکی از آن است که صدای انفجارها مجدداً در کویت شنیده شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135680" target="_blank">📅 17:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135679">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b003e9e7d1.mp4?token=YlyLANyIEitWjZJkrYirQZDDgHYnVrqL6bC-5uopK3gMrfRhnKHr26UI-jozpZ9ldT2DEFCLPaGDrok4YENmgnp1mZqrBZJ8rOL2pHFfveu3bikrsAysq-M5NAMrohRkGUVkwz57FOZkfQjm7qisnHFaJpVGNz0nIpPrA2_1g42UD3ocoFApNIVmLUtbwKweCB0xh9KlILWDt3uZnKBemrD9N7Sw-MQN1bZyewAvbPGSnL_qoDHk-IjlozcIEjo9tCIjsSDeqUDe67MHlrrBCUbfoaW1J_lBQDK_AP1Ho_16FBKNxB2yH0R88Qe6AP7jP0HpYYyN9DshA1_NsjsTcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b003e9e7d1.mp4?token=YlyLANyIEitWjZJkrYirQZDDgHYnVrqL6bC-5uopK3gMrfRhnKHr26UI-jozpZ9ldT2DEFCLPaGDrok4YENmgnp1mZqrBZJ8rOL2pHFfveu3bikrsAysq-M5NAMrohRkGUVkwz57FOZkfQjm7qisnHFaJpVGNz0nIpPrA2_1g42UD3ocoFApNIVmLUtbwKweCB0xh9KlILWDt3uZnKBemrD9N7Sw-MQN1bZyewAvbPGSnL_qoDHk-IjlozcIEjo9tCIjsSDeqUDe67MHlrrBCUbfoaW1J_lBQDK_AP1Ho_16FBKNxB2yH0R88Qe6AP7jP0HpYYyN9DshA1_NsjsTcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از ایلات خروج یک زیردریایی موشک‌انداز ارتش اسرائیل (IDF) را نشان می دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/135679" target="_blank">📅 16:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135678">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوری / چندین انفجار در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135678" target="_blank">📅 16:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135677">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
فوری / گزارش ها از شنیده شدن صدای انفجار در بندر عباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135677" target="_blank">📅 16:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135676">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
منابع خبری محلی در جنوب لبنان از حملات نظامی جدید اسرائیل در مناطق مرزی خبر دادند.
🔴
ارتش اسرائیل دقایقی پیش اقدام به یک انفجار مهیب در اطراف شهرک «کفرتبنیت» واقع در جنوب لبنان کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135676" target="_blank">📅 16:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135675">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ارتش: فردا قراره تو شرق تهران بمب های عمل نکرده رو منهدم کنیم پس اگه صدا اومد نگران نباشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135675" target="_blank">📅 16:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135674">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‌
👈
پلیس راهور فراجا: تمام مسیرهای آسیب‌دیدهٔ هرمزگان بازگشایی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135674" target="_blank">📅 16:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135673">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
فوری / چندین انفجار در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135673" target="_blank">📅 16:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135672">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ارتش اردن: 3 فروند موشک بالستیک ایران که به سمت جنوب شهر عقبه شلیک شده بود، در حالی که موشک چهارم به منطقه باز اصابت کرد، رهگیری شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135672" target="_blank">📅 16:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135671">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
منابع عبری
: اسرائیل ممکن است در 24 تا 48 ساعت آینده،ارتباطات رادیویی خود را به دلیل تنش قریب‌الوقوع با ایران قطع کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135671" target="_blank">📅 16:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135670">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cV9aJdJtkCw97rb4xt2e1DuDT3betRQ-m-2nK-KhjZ4rlj2Jw7DwcQCdmtcYDnY3dwaJZV9QTNCP-BfP6az0jIWAvReZGBTlBZm4O3p1dNZgASlq826mpisAwYYaq9LRTq9ymk5jSkrh8pl0nW_iucLriZRhMVey5DKwW6j3nxEZDOkNLsaux5jJgpyl3akBU6yZE3RTAG6A81Ex8Y6jSyjJNH7ATO3odlY4RUzAZomSGF1zuk8ZQSLU3s71L0V1l495FDkzgAemHQWx_byn8S8flO31HkdPb5cSm_7t8sDkqTKOY0dhmhSpMGGbp-xUlJfOIn_MGYUc0RZXcHk7mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منتسب به کرمانشاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/135670" target="_blank">📅 16:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135669">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
گزارش‌هایی از شلیک جدید از ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/135669" target="_blank">📅 16:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135668">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
گزارش انفجار در کرمانشاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/135668" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135667">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
معاون سیاسی سپاه : حمله به پایگاه‌های آمریکا تو اردن، کویت و عمان ادامه داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/135667" target="_blank">📅 16:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135666">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
فکت تاریخی
🔴
در طول تاریخ هیچ نیروی نظامی خارجی‌ای با دسته گل وارد یک کشور نشده.......
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/135666" target="_blank">📅 16:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135665">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c7Nr6JzP0Jj64K3OPB6W2CZ3FZPol7mP3c_q0RwzWGynu8Br2VPZuIejMKLBPTypwaENGFlVYIkM0wK1a4-ko9YQHTqsOMsoIDDUvGo1K8j_62I-quALUOODr5hcvJzEhS70wpFGnI7zWr66DKhItmnWikw5QIPbnFBg_JJz4nQdpvhjVeaBHv8wEHadD6zbOW2P3FzcpOlVNXVcVLJcz-O2uBz_F-magQV7oGeCufkO88WgqQlQb1LCknxlbVI6H2bTK1--vSzlM9edAtKBiAsaGRp0lDE1ct5a3pRgPUUjM_eKvd8RvWhIdd1Js-gDhNC5Anvlc8l7ZyC08BGdEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت آمریکا در امان، پایتخت اردن، هشدار داد که به دلیل «تهدید امنیتی موثق»، فرودگاه بین‌المللی عقبه و بندر دریایی اردن تخلیه شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/135665" target="_blank">📅 16:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135663">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
بر اساس گزارش الجزیره، موج شدید گرما و حملات مجدد نظامی ایالات متحده به ایران، باعث شده است که قطعی‌های برق که قبلاً پراکنده بودند، به یک پدیده روزانه در سراسر کشور تبدیل شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/135663" target="_blank">📅 16:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135662">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فوری / هم اکنون 14 هواپیمای سوخت رسان آمریکایی از اروپا به سمت اسرائیل اعزام شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/135662" target="_blank">📅 16:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135661">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری / هم اکنون 14 هواپیمای سوخت رسان آمریکایی از اروپا به سمت اسرائیل اعزام شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/135661" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135660">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
شبکه الجزیره به نقل از رسانه‌های اردنی: صدای چندین پهپاد در آسمان عقبه شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/135660" target="_blank">📅 16:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135659">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: سیستم‌های دفاعی آمریکایی دو موشک ایرانی را در منطقه العقبه رهگیری کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/135659" target="_blank">📅 16:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135658">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
رسانه عبری والا: نیروهای اسرائیلی با همکاری اردن موشک های ایرانی را که به سمت عقبه، اردن در حرکت بودند، رهگیری کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/135658" target="_blank">📅 16:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135657">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
سازمان هواپیمایی کشوری، سقف نرخ بلیت پروازهای نجف و بغداد را ۱۲ و ۱۴ میلیون تومان اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/135657" target="_blank">📅 16:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135656">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
رسانه عبری: نیروهای اسرائیلی و اردنی موشک های ایرانی را که به سمت عقبه، اردن در حرکت بودند، رهگیری کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/135656" target="_blank">📅 16:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135654">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eG_MEsxZjfQXqcRCv8uOhwU85ZlmNODx5NtaBtrK14tgFkUyepkJkkvTL0FkLi2rPPDLm7Cm4fGpPKJOTr3rZgd7Qvn6Mat24xktWAsauoYPA8ifJ6QNXZz6luJEym0quWAoOJhohMdVGJ2LU5eWBkrhG9u7ph7tlhkmQDxZNGeF1URSopVo7aYVRRQ7uB3weWmNqJvvLE_8aS5yQLEluOPgqbRvlpUAXlTperj_RE95oArwof9SMXAl6VQr6yoCRC1-vRyzjInWFXHGMgIAsExaS7nEARIrBuq7KCct-SizPotEx7FkkhSfHeD_Ug0x5vZa-CJgfbWkZa_1xeUCyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af3ea64d0.mp4?token=Y6TfdPb4ObZUck7ZvXmhr0X8IlJyfH7oEYnmKPtjnmQFAg-j059R8fb_HYNiPINANhXS-UNGm6Rgb9JYgj8L1Sr5CtiWr_jN5FHoUfxp245y4hUKckLOia4T5IMKU8xLPstV_sqSGDoz6WXy0NOvNPpMntLeIcPjHx5hoB9g_Ww_OhEMp7NeEmCyPdWQUp4WS9Wx-0MikO8VHvHSr4664g8tQKET0oHTMDfBLEFFZnh5_s3so0ahTCUKzlvbs9jw-6Ivysj2zMFaLA1pFr5EmUas73QDFWRP5ZaCzocdGnNOOLascYdMp0-Wisug7N_p42M-bNCik907FTe1vS8MHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af3ea64d0.mp4?token=Y6TfdPb4ObZUck7ZvXmhr0X8IlJyfH7oEYnmKPtjnmQFAg-j059R8fb_HYNiPINANhXS-UNGm6Rgb9JYgj8L1Sr5CtiWr_jN5FHoUfxp245y4hUKckLOia4T5IMKU8xLPstV_sqSGDoz6WXy0NOvNPpMntLeIcPjHx5hoB9g_Ww_OhEMp7NeEmCyPdWQUp4WS9Wx-0MikO8VHvHSr4664g8tQKET0oHTMDfBLEFFZnh5_s3so0ahTCUKzlvbs9jw-6Ivysj2zMFaLA1pFr5EmUas73QDFWRP5ZaCzocdGnNOOLascYdMp0-Wisug7N_p42M-bNCik907FTe1vS8MHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یکی از قطعات موشک در نزدیکی فرودگاه پادشاه حسین در شهر العقبه سقوط کرده است
🔴
تمامی موشک ها رهگیری و هیچ خسارتی وارد نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/135654" target="_blank">📅 16:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135653">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b870f451.mp4?token=S4XFKlUQW3LRsCkA9qh7S_cqHLrLsuY9U6Ib4u2GN_qOf1p3G-gvXyHftb2kWE2koMIfSs67yuw3yoNWMTWprtDcsfNEMTbMGGrtURFymNOO0i27bwLFSCmYlvX1kQbNI_0SB6xSrPV__Zn2JauQPhTkXMWb-mhwaUTyn692MkjiNfoEEHMphId7SV0HOAxdTJG9le9TX4z8klpM7FNvtt8rfVbJH4VT_kiP8UCSQ491D-r_esZsnVZVsvqGQsUGeYGERL-fndvwXvww4faxnpuoqs5tP3eppBfACfNIGlPmCVNCKQWpDL4kGcxam9ZhW_K4M27wyxt8zWw4cuSGl2ODZfXHEiQ2eaOrCzh0OqsyK2gL1jLEMFp8SsCUZyKbE-taxal-BNDC2A-AwitLTu3yq6yqFQPbMyCBLGzLUed38a-POjf-imaf2d7BtpoHsdbNpqNNc0tZohLGSf_x-V_w1Es322-k532e2g-90o_67l4YnFZFCfWyO-q9JK4wTxJZTk08101dT6_1JBBy9nNfjvNBHPVhqHp69j8Tz0CP1dvbNlVseeXny3VSvrX0o66bD5C7YaqsrbAOybpl4Pu-QKIJPv6P6XtMGBirYscQvdkeicuD-DlCxKgLa5jg-5TOds01D6SOsdoRMJ6gDhJB7QiY5za6-azsMmOOEqE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b870f451.mp4?token=S4XFKlUQW3LRsCkA9qh7S_cqHLrLsuY9U6Ib4u2GN_qOf1p3G-gvXyHftb2kWE2koMIfSs67yuw3yoNWMTWprtDcsfNEMTbMGGrtURFymNOO0i27bwLFSCmYlvX1kQbNI_0SB6xSrPV__Zn2JauQPhTkXMWb-mhwaUTyn692MkjiNfoEEHMphId7SV0HOAxdTJG9le9TX4z8klpM7FNvtt8rfVbJH4VT_kiP8UCSQ491D-r_esZsnVZVsvqGQsUGeYGERL-fndvwXvww4faxnpuoqs5tP3eppBfACfNIGlPmCVNCKQWpDL4kGcxam9ZhW_K4M27wyxt8zWw4cuSGl2ODZfXHEiQ2eaOrCzh0OqsyK2gL1jLEMFp8SsCUZyKbE-taxal-BNDC2A-AwitLTu3yq6yqFQPbMyCBLGzLUed38a-POjf-imaf2d7BtpoHsdbNpqNNc0tZohLGSf_x-V_w1Es322-k532e2g-90o_67l4YnFZFCfWyO-q9JK4wTxJZTk08101dT6_1JBBy9nNfjvNBHPVhqHp69j8Tz0CP1dvbNlVseeXny3VSvrX0o66bD5C7YaqsrbAOybpl4Pu-QKIJPv6P6XtMGBirYscQvdkeicuD-DlCxKgLa5jg-5TOds01D6SOsdoRMJ6gDhJB7QiY5za6-azsMmOOEqE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بهترین راه برای پیدا کردن شغل، راه‌اندازی کسب‌وکار و گرفتن پست‌های مهم مخصوصاً در صداوسیما، مجلس و نهادهای مختلف این است که از دیوار سفارتخانه‌ها بالا بروید، آنجا را آتش بزنید و غارت کنید، بعد هم نماز جماعت بخوانید!
🔴
بعد از آن، خیلی شیک و مجلسی تبدیل می‌شوید به «کارشناس مسائل بین‌الملل، جنگ، اقتصاد، سیاست خارجی و...» و در همه‌چیز هم صاحب‌نظر خواهید بود!
🤔
همین حروم زاده میدونین چند نفر از هم وطن های مارو تو 18، 19 دی کشته؟!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/135653" target="_blank">📅 16:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135651">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lN2JV5U8XupeI7I8YaFMt20TU5ldSzT8gs_SvxtKNM-pC0KC5g4hKSZibN_nLR42SeRU6uFmS4JWDAcJ9eW3c_DucsAp-cbVMpMEsH_6lbLItmfL_Oxwf3k9IqAec6dPb4udOjbXlq2OWEKfdON1xZ1crhVJ-ipbZeRjHWBKInJNPSApCgq-A_GDwkGTO-780WwlHLeSg3qzrj4KXwP435gn4GC6NdvBhCAM_iEa_ZwS8gjsr4zztiig7dkCydyvVqH-xnTkcmKfdJLijr4QIPfsbjv9kh-BpJ-M2TgKgUMpdv4fav4L-LMCYgTSZvmlUjJ6ybTlLfsZ819552ySKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af3ea64d0.mp4?token=tANC-ZGi-pbdcrSA100AjGIhZOc1Dv0hA27UkWQlQhI3qR10o90gN-o0CMsK3nJInSyHAjiNFUD4iujroGJC1Gj1laBsY1pl8dfW3cS-0AwPWETriFIjc5ATjtzmdGhKUNipcOqYPnpGxDBuYFS7CtpHBqQ2I7GWnfwhM2j_KMriOdOkLZUUWWr5p5yYgkmaaL-SKCl00tDCwwZUzYeymRZ39sb7vnzT0Ij2Uw6d8b9tYtZNTDwwDy6yl3SwiQQsnPvcYO_DoN6fsvRcBt9qD_wHBtCo1sKZ-kTdu_t3A90iPiIey1Qqq3CmWC1Hdt0Y1ixUg2S4EPP9zWe1OdmhWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af3ea64d0.mp4?token=tANC-ZGi-pbdcrSA100AjGIhZOc1Dv0hA27UkWQlQhI3qR10o90gN-o0CMsK3nJInSyHAjiNFUD4iujroGJC1Gj1laBsY1pl8dfW3cS-0AwPWETriFIjc5ATjtzmdGhKUNipcOqYPnpGxDBuYFS7CtpHBqQ2I7GWnfwhM2j_KMriOdOkLZUUWWr5p5yYgkmaaL-SKCl00tDCwwZUzYeymRZ39sb7vnzT0Ij2Uw6d8b9tYtZNTDwwDy6yl3SwiQQsnPvcYO_DoN6fsvRcBt9qD_wHBtCo1sKZ-kTdu_t3A90iPiIey1Qqq3CmWC1Hdt0Y1ixUg2S4EPP9zWe1OdmhWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یکی از قطعات موشک در نزدیکی فرودگاه پادشاه حسین در شهر العقبه سقوط کرده است
🔴
تمامی موشک ها رهگیری و هیچ خسارتی وارد نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/135651" target="_blank">📅 16:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135650">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tm9TVIl0IJMK8Rl4Qgn4KlNmuoQt4CQzykpj7lw0NC1gXozdMFzVtC4Db_PVwfibyJTwpXwIUXz1iAeB4a89Z1Il_rh6-7csz_FgKfvwbI0VZrLhv1uD52JuLDmWP5mltVaswaF6tdNXaNAlZx9G1DKqg8JLjxo6cD0A32rzJLfddBktXPgO43sI5jQmOZVfkyu0nFmFeWab21Vpq0FYzbURhGhWeBrFNojVkP1TEp3Q1y1639tHdm1eKx9-vOMp6WVd-9qpGSfNPKMQpmhI6RGvlwrMFNBwOM1F-Jra8Kv_TqZLtNg01EpTrK9mdjOuK14fASHVQ3XyFyAExngL1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک پرواز از دبی به تل‌آویو به دلیل شلیک‌ها به سمت اردن، مدتی در هوا معلق ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/135650" target="_blank">📅 16:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135649">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
رسانه‌های عبری: حمله ایران به عقبه، به عنوان یک هشدار به اسرائیل طراحی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/135649" target="_blank">📅 16:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135648">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424131ea7c.mp4?token=YU64nrLOYJ_KFNEOXkzG-Ikwyyrh7URst1FF8kwk5UU_VajOmuJXSUhfHW_ZuM0TExAomtoCd2ax9Ov5pUjWfLSzYeKA6kK6r5Dqw6Ajrs-ah_ulkHNzAuWhGUg7GI-5zVchvxCkMUIOlvWMU3kz0h9nIvtGHKPioHrYlzD6-KEmqma1EJh2aX9tHZrKLD1ggaflvc0TQtvnn9DWF72YntbLpaaMljlUkOSBwWDuEyK_mO-LgWjdrp0ZRAV1oovFz8PdGWEkKQTFHCxb56vcnEluGDl7yS_LWmccDaWtryw7L-ZeL8UTAXBGnnlFDPhauIQqDiZRHSs-1tcoHkh4jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424131ea7c.mp4?token=YU64nrLOYJ_KFNEOXkzG-Ikwyyrh7URst1FF8kwk5UU_VajOmuJXSUhfHW_ZuM0TExAomtoCd2ax9Ov5pUjWfLSzYeKA6kK6r5Dqw6Ajrs-ah_ulkHNzAuWhGUg7GI-5zVchvxCkMUIOlvWMU3kz0h9nIvtGHKPioHrYlzD6-KEmqma1EJh2aX9tHZrKLD1ggaflvc0TQtvnn9DWF72YntbLpaaMljlUkOSBwWDuEyK_mO-LgWjdrp0ZRAV1oovFz8PdGWEkKQTFHCxb56vcnEluGDl7yS_LWmccDaWtryw7L-ZeL8UTAXBGnnlFDPhauIQqDiZRHSs-1tcoHkh4jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ستون‌های دود از فرودگاه ملک حسین در عقبه اردن به هوا برخاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/135648" target="_blank">📅 16:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135647">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ستون‌های دود از فرودگاه ملک حسین در عقبه اردن به هوا برخاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/135647" target="_blank">📅 16:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135646">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
آژیر ها در اردن دوباره فعال شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/135646" target="_blank">📅 15:59 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
