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
<img src="https://cdn4.telesco.pe/file/QNOjOX7QBytQ6vWu5Rzw5o-_PndxbAStToeN7ermZG4r5YuZTcs2mJRwDkYz2m30htpwX4f4NoTU7uLSbh_-vUFBHc9WsHZ_zhZh8cHwTmECSPbzoE3FyVmUFklxmCo3MzeJX7MmXHYtT-aHCKBHZ3JB3OtrGHJhJDlrEa5ukKmRBaqOBMOqaa9YrUrvuEeHX4Fzzcdj9rJVTrGXVUi59g3eRRQ8-UDEQreZ8VZQe2Ib4xjDCYmzYjpcpsVK2r-cm7hZzQ9GpzIVZfT4XI4qwFz2Apk9dcNIEJZvYgyVw_0Nq3gmFBqmChceX7Z1onFN4SLmKTXF_TIXqUutcEl7JA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.27M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 23:42:46</div>
<hr>

<div class="tg-post" id="msg-683514">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
بلومبرگ: ایران راه‌های زیادی برای تلافیِ تحریم‌های آمریکا دارد
🔹
رسانه آمریکایی روز شنبه تأکید کرد که ایران در طول جنگ نشان داده که می‌تواند در برابر اقدامات نظامی و اقتصادی آمریکا مقاومت کند و به آن پاسخ دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/683514" target="_blank">📅 23:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683513">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
واشنگتن‌پست: ایران در پی یک غافلگیری اکتبری برای آمریکاست
واشنگتن‌پست مدعی شد:
🔹
تهران هنوز قدرت آتش‌بار و انگیزه کافی برای حمله پیش از انتخابات نوامبر را دارد.
ایران در حال برنامه‌ریزی برای یک غافلگیری اکتبری یا شگفتی‌سازی انتخاباتی‌ پیش از انتخابات میان‌دوره‌ای است.
🔹
یکی از دلایلی که ترامپ در ازسرگیری درگیری‌های بزرگ تردید داشته، نگرانی اعلامی او از این بوده که ایران ممکن است با پرتاب حملات به اهداف انرژی در عربستان، قطر و دیگر کشورهای حاشیه خلیج فارس تلافی کند.
🔹
این موضوع بخش زیادی از نفت آنها را از بازار جهانی خارج کرده و باعث یک رکود جهانی می‌شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/akhbarefori/683513" target="_blank">📅 23:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683512">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
رائفی‌پور در اجتماع بزرگ بیعت مردم مشهد با امام زمان (عج): هر روز زمانی را به گفت‌وگو با امام زمان اختصاص دهید و محبت خود را به حضرت آشکار کنید / اشتیاق به امام زمان، یعنی با او حرف بزنیم و رابطه‌ای از جنس محبت و دلبستگی داشته باشیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/akhbarefori/683512" target="_blank">📅 23:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683511">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کلثوم اکبری هَستٍمه.....
بازخوانی پرونده ای که هنوز باز است
🔹
زنی که با ازدواج، سراغ مردان تنها و سالمند می‌رفت... و کمتر از چند ماه بعد، همسرش دیگر زنده نبود!
🔹
پرونده کلثوم اکبری، یکی از عجیب‌ترین پرونده‌های جنایی ایران، حالا وارد مرحله نهایی شده. حکم قصاص صادر شده، اما هنوز قطعی نیست./ خبرفوری
@Tv_Fori</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/akhbarefori/683511" target="_blank">📅 23:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683510">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb9b1dcca0.mp4?token=B-VCNWpHELTVLqNPJOEv4a1apRGB5dsjE3oiUQ2QIJSGMuuxvsdgehBnpnMMmfLJ0TMSS4wrGWwvAGiI-7H03pS53OSRj_5RWD9YuqIpCjz2c8o6vilm9J76GehDh6m6twFG1xXXsh0NsWC1inISiw2vp7CrHgRcsWqbFNCFtj4itH5yqZSrIiUBgJJO3Pp1WxH7TR7nyDBkdEFyOarFZ-8D2vyacZF0CoUmBQnepitl17j4SV-E9t8dYc5AcTHtZGcgyjEWfxA92xD-pBo3yr2pSAeP8-6CizDz7XBSeLdVFLxS3SliESLjig5PnMWRkLi9ImSD-RW7UOB_NXlL0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb9b1dcca0.mp4?token=B-VCNWpHELTVLqNPJOEv4a1apRGB5dsjE3oiUQ2QIJSGMuuxvsdgehBnpnMMmfLJ0TMSS4wrGWwvAGiI-7H03pS53OSRj_5RWD9YuqIpCjz2c8o6vilm9J76GehDh6m6twFG1xXXsh0NsWC1inISiw2vp7CrHgRcsWqbFNCFtj4itH5yqZSrIiUBgJJO3Pp1WxH7TR7nyDBkdEFyOarFZ-8D2vyacZF0CoUmBQnepitl17j4SV-E9t8dYc5AcTHtZGcgyjEWfxA92xD-pBo3yr2pSAeP8-6CizDz7XBSeLdVFLxS3SliESLjig5PnMWRkLi9ImSD-RW7UOB_NXlL0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: باید جهاد اقتصادی راه‌اندازی کنیم
🔹
دولت باید از اقتصاد دولتی بیرون بیاید و مردم را کمک کند که وارد جهاد اقتصادی شوند. هر محله‌ای می‌تواند تبدیل به پایگاه موشکی جنگ اقتصادی شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/akhbarefori/683510" target="_blank">📅 23:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683509">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fbc4c891c.mp4?token=FhM-6vljI23LPecwedeIBHdlt5zNsHKmtrEEsxsaj1ajXvDHKac73yRe8Kmh9pZuJFN3Wy9_OKosdEHBAFAB6mgVfwSwk9Fyz3Y7cFs_VTDf65HHEWdj9f3TXRqHtavn4AsyoEREYwbpLbtw-t9MF02KRsvrmS9jzsywgPvBRNPFOeWN-Ewf_0-4Zl-3JcmBwoCmuDctVbdJnYv5ORsOjQ_Z-2NltLfBfFBLnpAkvrWtSkHyF6ZyqhrF6mkv7vLX60_YXLqEfLvIO7FLGyL6k81R70lyOBRu_wjT_IdnnnaMEINNheCnhOUNN9VEFdt2zRmvDNcry-9MqvJdABM0_4E2t5lZlBTCmaC7S3GEDJ1jlc3vtWLohvJdNbYXX9Qk1XNEmTbcFRjg4oFrWiwqYwcFjE1BP2eRKgd_jfw3MUYgL0Z5DiF0VBp9ZzK22d8P785C7UQLqSTzt-9FHMDjTaiOWb_UIW9PuC_5GtX-m9yt2vcR-4niuItPDb8khVQgG0fmyy1aXwNCXjq9ON6nzWV5X_-SbBpVyWybfBs6sWgPa9d9Tyu-McziTqiaj3pINpR2w9eZHTesVxkA9EjIf8VQ8a-sWnz2hNic0WudfVshLnjdYLAt5man98UsEHYpYZECfM57VDaf1AdJaZ1LcImDI90wZNeMw_NeAmseMdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fbc4c891c.mp4?token=FhM-6vljI23LPecwedeIBHdlt5zNsHKmtrEEsxsaj1ajXvDHKac73yRe8Kmh9pZuJFN3Wy9_OKosdEHBAFAB6mgVfwSwk9Fyz3Y7cFs_VTDf65HHEWdj9f3TXRqHtavn4AsyoEREYwbpLbtw-t9MF02KRsvrmS9jzsywgPvBRNPFOeWN-Ewf_0-4Zl-3JcmBwoCmuDctVbdJnYv5ORsOjQ_Z-2NltLfBfFBLnpAkvrWtSkHyF6ZyqhrF6mkv7vLX60_YXLqEfLvIO7FLGyL6k81R70lyOBRu_wjT_IdnnnaMEINNheCnhOUNN9VEFdt2zRmvDNcry-9MqvJdABM0_4E2t5lZlBTCmaC7S3GEDJ1jlc3vtWLohvJdNbYXX9Qk1XNEmTbcFRjg4oFrWiwqYwcFjE1BP2eRKgd_jfw3MUYgL0Z5DiF0VBp9ZzK22d8P785C7UQLqSTzt-9FHMDjTaiOWb_UIW9PuC_5GtX-m9yt2vcR-4niuItPDb8khVQgG0fmyy1aXwNCXjq9ON6nzWV5X_-SbBpVyWybfBs6sWgPa9d9Tyu-McziTqiaj3pINpR2w9eZHTesVxkA9EjIf8VQ8a-sWnz2hNic0WudfVshLnjdYLAt5man98UsEHYpYZECfM57VDaf1AdJaZ1LcImDI90wZNeMw_NeAmseMdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رکورد شکنی شهروند روس با پرش از لایه‌های بالایی جَو
🔹
سرگئی بویتسوف، شهروند روس پیش از پرش و رکوردشکنی‌اش از بالون هوای گرم، پرچم کشورش را با افتخار به اهتزاز درآورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/akhbarefori/683509" target="_blank">📅 23:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683508">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: حملات ما الان هدفمند است و جنگ اقتصادی را هم می‌زنیم خنثی می‌کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/akhbarefori/683508" target="_blank">📅 23:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683507">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8ecdab1b.mp4?token=Uw3_1VdKYiG55yWUXPhFlzoIVwKpkNcReRbXOkjWcPfHO0WAY9T3zmnxp1vMIHVsa94meQcZX3tgC3Utln2Hk5g_Hyaipzmb7DCLJqhdWoX2mrDCnlJGyp2dZLZDJwKzlkIbh8oEz68q4LLv8fCAXEGq4XXCvx_JoZB7gz1168Ks9QV3DahdgfqgidjeFgAcICdDXdSrzJyg2ShIBNnkiLMslLbJFX1oGg0Nu4UBN9TmpdNzWzfifSLffROCD4xqx1XUaFdZb2n_XZZzumjoWbBG7XYNkf0XYX68O1S1JjgZ8xer6y_kVr7FXABbDaVNFEoeia_6-N-aeHje9xauRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8ecdab1b.mp4?token=Uw3_1VdKYiG55yWUXPhFlzoIVwKpkNcReRbXOkjWcPfHO0WAY9T3zmnxp1vMIHVsa94meQcZX3tgC3Utln2Hk5g_Hyaipzmb7DCLJqhdWoX2mrDCnlJGyp2dZLZDJwKzlkIbh8oEz68q4LLv8fCAXEGq4XXCvx_JoZB7gz1168Ks9QV3DahdgfqgidjeFgAcICdDXdSrzJyg2ShIBNnkiLMslLbJFX1oGg0Nu4UBN9TmpdNzWzfifSLffROCD4xqx1XUaFdZb2n_XZZzumjoWbBG7XYNkf0XYX68O1S1JjgZ8xer6y_kVr7FXABbDaVNFEoeia_6-N-aeHje9xauRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار در تایوان
🔹
انفجار در منطقه تاینان درتایوان، ۱۳ نفر را مجروح و ۱۱ خانه را تخریب کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/akhbarefori/683507" target="_blank">📅 23:22 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683506">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: به‌هیچ‌وجه تسلیم نخواهیم شد و جانانه تا آخرین قطرۀ خون از ایران دفاع می‌کنیم؛ اجازه نمی‌دهیم پای دشمن به خاک ایران باز شود
🔹
ما نیروهای مسلح تا آخرین قطرۀ خون‌مان را به ملت ایران هدیه می‌کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/akhbarefori/683506" target="_blank">📅 23:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683505">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: ما تاکنون به هیچکدام از منافع اقتصادی آمریکا حمله نکرده‌ایم
🔹
تاکنون ما فقط پایگاه‌های نظامی را هدف قرار داده‌ایم اما اگر قرار باشد جنگ اقتصادی را جلو ببرند آمادۀ هدف‌قراردادن همۀ شرکت‌های نفتی و اقتصادی آمریکا در منطقه هستیم.…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/683505" target="_blank">📅 23:14 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683504">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35b1e3ebd8.mp4?token=ZUFd0GxPGXOMZYT-7LS0LNPXiqN6neJ-CTjLV451_waHjnQZGcoTqWKrUJkwaCU4QuIm-WpHPPnPvr0ARaqaGaOr25kAo8p9cjmP-ClAV5MV7Ynvf2jr5huQGv0JL6u0iYBFfmMPU8UYkamGFBnImvMtEfoLOtJNtVsc3d3LXR4WumljO8xN-8vXRIOe7xCLViGEfzzMlw1ivYL5-EcW5NBZg5EaYfFDkopq6uhFgkpkxrh8uisn5LDThzboo8l276Vfvm5YJIIrb906Xr4V-JZCbN7UHrIsO_LbCGe1NFWUBgRydCZ6J44_zd8pkvLuVfTCkc4OXAkKyV5uGob8sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35b1e3ebd8.mp4?token=ZUFd0GxPGXOMZYT-7LS0LNPXiqN6neJ-CTjLV451_waHjnQZGcoTqWKrUJkwaCU4QuIm-WpHPPnPvr0ARaqaGaOr25kAo8p9cjmP-ClAV5MV7Ynvf2jr5huQGv0JL6u0iYBFfmMPU8UYkamGFBnImvMtEfoLOtJNtVsc3d3LXR4WumljO8xN-8vXRIOe7xCLViGEfzzMlw1ivYL5-EcW5NBZg5EaYfFDkopq6uhFgkpkxrh8uisn5LDThzboo8l276Vfvm5YJIIrb906Xr4V-JZCbN7UHrIsO_LbCGe1NFWUBgRydCZ6J44_zd8pkvLuVfTCkc4OXAkKyV5uGob8sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مبارزه ابرهواپیمای روسی با آتش‌سوزی‌ها در صربستان
🔹
رئیس‌جمهور روسیه هواپیمای غول‌پیکر و معروف EMERCOM Il-76 را برای کمک به صربستان در مبارزه با آتش‌سوزی‌ها فرستاد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/683504" target="_blank">📅 23:11 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683503">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c69RIpa9Ziwgp6A5Fyzcecq6Tl2Dv3fAkme8LYMhffq9kLu0UpW3zQCQodKRsai_Z-Ly_OgENlS1F0t0_qDQm7NcQBah-_Jce1-Pen9RDtTj4CKbLkzRrzvT1ADo_1Z0EJ_wvUs2KLIQLjwY9fznbzUMgxQYlSa-fEH_SrQJ6vRMCbSIVW1SjTU88PCvpr_igOR1JiSY6ZB2OiV7Or7t19CI3_daOPSnrqH4yEV6UcXq7DvG6tVVcPN1G57NdNvq-KVyD0xnKzq3VFNZ2S-NryTmUEbN_4PMvyyUDvM1xvNvAthoznLxEvkbUKwVlo06woHNn1thp0hkaSqMZ2hXSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اندیشه و دانش؛ چراغ‌های راهِ جان
🔹
امام علی(ع) در حکمت ۵ نهج‌البلاغه، یادآوری می‌کند که «دانش»، میراثی ماندگار است، «آداب» نیکو، زیور همیشگی شخصیت انسان است و «تفکر»، آیینه‌ای شفاف که واقعیت‌ها را آن‌گونه که هستند به ما نشان می‌دهد.  #نهج_البلاغه_بخوانیم…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/683503" target="_blank">📅 23:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683502">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bf0c45907.mp4?token=HLAeKrmJKFR9Sd6hqKLcNXwdd_5tzYPHpIxLng-dxpFfmw5PR5Y7P3h-97VaykzVhY5zcjMg7inEkOqfsz6XGkmldR7foLNtlmEtbcq6psAvtZq003Qx6wTYn_NWmCyVKqjsJnqwV8q6gwXYMaFSwyG2t3YuiF48ZqOAm6cYIBSoLxlJ8HClk5VyNHjaNkr6O8UiRI-qcGXKdkLKlBJwwGTQasVVvHNXk2HK3sRV__9atWvZI8FLojVHk1Kn43wPtCG242KQoXbCvU7N1QSCW9cozhpwSfrYRTRFW4FA7rsSJsyGSP9QwOOcFjj6oPZJEP3GQZB3Eo9qvasAiIpbZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bf0c45907.mp4?token=HLAeKrmJKFR9Sd6hqKLcNXwdd_5tzYPHpIxLng-dxpFfmw5PR5Y7P3h-97VaykzVhY5zcjMg7inEkOqfsz6XGkmldR7foLNtlmEtbcq6psAvtZq003Qx6wTYn_NWmCyVKqjsJnqwV8q6gwXYMaFSwyG2t3YuiF48ZqOAm6cYIBSoLxlJ8HClk5VyNHjaNkr6O8UiRI-qcGXKdkLKlBJwwGTQasVVvHNXk2HK3sRV__9atWvZI8FLojVHk1Kn43wPtCG242KQoXbCvU7N1QSCW9cozhpwSfrYRTRFW4FA7rsSJsyGSP9QwOOcFjj6oPZJEP3GQZB3Eo9qvasAiIpbZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدیرعامل بزرگترین مجتمع پالایش بنزین کشور اعلام کرد:
در بنزین تولیدی این پالایشگاه از ترکیب ۳ درصد متانول و بنزین استفاده می شود!
@Titretejarat</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/683502" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683501">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a780ac014.mp4?token=tbJQZZG10mGT-dmn8OlKbV7ATXL-Ow6jWhzaLPynAzPepW_mvbjXd506s19ArjjdVE-aXHTBFW4vfy7eR-R0Nm8y03RGoPjfRhCBjmCyupi_YR1ZKzrhjlxEdxIiQdnXOuBUPGOzs4cpxnUKvdaTUufStCXVgr5PIg8Dhx_5WaAAl8BobOIWw3v55brbPAokFbL4UUlzx8JIT_KP7ksLItjig6GoR-uM1qkrpyU7RWZG9hz0lPW-0VekrbVrC_AZjrLWhJh3KjxpsVKoa9lkJfZCnwxpWWCXGI4qt8aVFO_WoTaZ72LuJjcO8mOvQBttJvlI8CUcZZNNKobrwHFj2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a780ac014.mp4?token=tbJQZZG10mGT-dmn8OlKbV7ATXL-Ow6jWhzaLPynAzPepW_mvbjXd506s19ArjjdVE-aXHTBFW4vfy7eR-R0Nm8y03RGoPjfRhCBjmCyupi_YR1ZKzrhjlxEdxIiQdnXOuBUPGOzs4cpxnUKvdaTUufStCXVgr5PIg8Dhx_5WaAAl8BobOIWw3v55brbPAokFbL4UUlzx8JIT_KP7ksLItjig6GoR-uM1qkrpyU7RWZG9hz0lPW-0VekrbVrC_AZjrLWhJh3KjxpsVKoa9lkJfZCnwxpWWCXGI4qt8aVFO_WoTaZ72LuJjcO8mOvQBttJvlI8CUcZZNNKobrwHFj2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: ما تاکنون به هیچکدام از منافع اقتصادی آمریکا حمله نکرده‌ایم
🔹
تاکنون ما فقط پایگاه‌های نظامی را هدف قرار داده‌ایم اما اگر قرار باشد جنگ اقتصادی را جلو ببرند آمادۀ هدف‌قراردادن همۀ شرکت‌های نفتی و اقتصادی آمریکا در منطقه هستیم.…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/683501" target="_blank">📅 22:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683500">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">✨
اشک های الهام چرخنده وقتی که از مردم مبعوث شده می‌گفت
@Heyate_gharar</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/683500" target="_blank">📅 22:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683499">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: در صورت ادامه محاصره اقتصادی شرکت های اقتصادی آمریکا را در منطقه خواهیم زد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/683499" target="_blank">📅 22:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683498">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
محسن رضایی: هر خانه میتواند یک لانچر جنگ اقتصادی باشد  دبیر شورای عالی امنیت ملی:
🔹
جوانان ایرانی وارد اقتصاد شوند. هر محله میتواند پایگاه موشکی جنگ اقتصادی باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/683498" target="_blank">📅 22:52 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683497">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: ما با عمان روی مسیر تنگۀ هرمز توافق کردیم که یک مسیر میانی است اما این موضوع روی کاغذ است و تنگۀ هرمز زمانی باز می‌شود که آمریکایی‌ها به تعهداتشان عمل کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/683497" target="_blank">📅 22:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683496">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38655f3126.mp4?token=cw8fSVo-HpVbc3NhZ3r50jhZ76IACFcnHwpogUJ7J-6RKoDR_x3OFb-Agxl56fksWf9iSA9HtVQMCKXtFhNEijrzdsF5VBYMq8sJbk4KBriiF3J0Kqk7wdLvEoyqBvzcs6InMHj6-obe42_0brQvX12a6FXTvPGHOH9iOPoRPxDOHhlrhwxbIR1kgICKiRrHg0LbO_tev5SuU7bGbR4KES_nMaudKfWWuC8rirGlsZK3IhRVEFab5dJzStBawRByx2fFlHsEiEL0DFblVkJH1zFNoWFewTHcXoR9LI5gxAnLfhMMfolLHU8UAONOvDSelP6_8vQY6LnZ7uchHzgL0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38655f3126.mp4?token=cw8fSVo-HpVbc3NhZ3r50jhZ76IACFcnHwpogUJ7J-6RKoDR_x3OFb-Agxl56fksWf9iSA9HtVQMCKXtFhNEijrzdsF5VBYMq8sJbk4KBriiF3J0Kqk7wdLvEoyqBvzcs6InMHj6-obe42_0brQvX12a6FXTvPGHOH9iOPoRPxDOHhlrhwxbIR1kgICKiRrHg0LbO_tev5SuU7bGbR4KES_nMaudKfWWuC8rirGlsZK3IhRVEFab5dJzStBawRByx2fFlHsEiEL0DFblVkJH1zFNoWFewTHcXoR9LI5gxAnLfhMMfolLHU8UAONOvDSelP6_8vQY6LnZ7uchHzgL0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: ما فعلا فقط جریان نفت در تنگه هرمز را محدود کرده‌ایم اما درصورت جنگ اقتصادی اجازه نمی‌دهیم نفتی از خلیج‌فارس حتی به روش‌های دیگر خارج شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/683496" target="_blank">📅 22:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683495">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80537027b.mp4?token=gZTZGv3giYIEMJKr2_tBeatFirSKuDaSfyobSJ2oPa2-HizmFU88Ls46-7Ogal5quq4AgXUlcYutlX9babzwjfhCudSgNGcsbQMl9FRStWK2Ch8WyMVhhcLwQTTaj8GmU4GMdEj_6AUQIk5LK66m8zFfDmcgtfNBU_F8qgMplXxLnc9UYSds6heFOoS-Z3L-_3R3HCWBjEsy0OReCNNsCI-k0WmTjMw08fJ9urRb9kh3ArxxZN-u3lvqxjbPYsgbgODZJ-cZ7TSA3ljn2UtnLxPAcT1zJJxUq7fQs4aGb4tT4OP7yG9MTr9n4yyt-jUOVIBpCMzPy8n_iVkvCxoJFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80537027b.mp4?token=gZTZGv3giYIEMJKr2_tBeatFirSKuDaSfyobSJ2oPa2-HizmFU88Ls46-7Ogal5quq4AgXUlcYutlX9babzwjfhCudSgNGcsbQMl9FRStWK2Ch8WyMVhhcLwQTTaj8GmU4GMdEj_6AUQIk5LK66m8zFfDmcgtfNBU_F8qgMplXxLnc9UYSds6heFOoS-Z3L-_3R3HCWBjEsy0OReCNNsCI-k0WmTjMw08fJ9urRb9kh3ArxxZN-u3lvqxjbPYsgbgODZJ-cZ7TSA3ljn2UtnLxPAcT1zJJxUq7fQs4aGb4tT4OP7yG9MTr9n4yyt-jUOVIBpCMzPy8n_iVkvCxoJFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: جانانه از ایران دفاع می‌کنیم و نمی‌گذاریم پای آمریکایی‌ها به ایران باز شود
🔹
به آمریکایی‌ها توصیه می‌کنم هیچ نیرویی اضافه نکنند چرا که آن‌ها را خواهیم زد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/683495" target="_blank">📅 22:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683494">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKMC</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmW73KrlCoVy7HQft4kY0RfALHCQpxVUOx0qcx5ZTGS2iDrdT7muee1uL03wd7DKb1o4lb3R7bwU-9i8o3UQxorV6BHW7pUq7-uadv-lyj_4O3CEqwelO_7pAc3OxjFEo-UEFcIUSTcezcKEWfL1cEdmaoNo9i8ITDVGhM2499_jMtmyxEpD7uQiudTFBblAyqd13IfHpxqaGqPGGzdIhLDFKSjTSL2iX9e8Ni2hxJwGtw99UZAt9lM1Fin3l9IbjxfmUi4BQxxR1SihdK8PpvigLkvW7tsSLGyB08RL7Lr3bJAymYYZK4FNwU0PcIwleLduhyHP__i_igNUAVxAjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
شرایط فروش کی ام سی  ایگل(KMC EAGLE )
▫️
قیمت: ۲،۴۸۲،۵۰۰،۰۰۰ تومان
▫️
پیش پرداخت: ۱،۵۰۰،۰۰۰،۰۰۰ تومان
مشاهده شرایط فروش
#کرمان_موتور</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/683494" target="_blank">📅 22:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683493">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
الهام چرخنده در اجتماع بزرگ بیعت مردم مشهد با امام زمان (عج): رهبر شهید ما، یک ایرانی به تمام معنا بود/ دشمن تصور می‌کرد با شهادت رهبری، چراغ خیمه‌گاه حسینی خاموش می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/683493" target="_blank">📅 22:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683492">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef25218d8a.mp4?token=Sm7A_fY_sLjA6935cxmz95Vl-DlohPcWqcz7RLg9xUx-9u8ksH8vZRTaeYT4zKc6wBuAn2jVyx-GCCs0iMoaNxNmG-1RkTIGb8J25JOxFXRAB_hWAm6-pyJmlAxCvXo3_I1cjT5uNAA5csL_l63-k8pxBwdjytnYmkVESWNss8-kowb-pzHNNmdjwL2-70urt2hacJzVyel8jq5-5Zd8IAPovfMdMz0-qInRPa8uN-saiZMl9m1W12Xnhmv1OoIEeL_VYCUiofinN9st884l8SHqmS-L5T1ndqpD3TmElJwxQlXqbd4PkPqb3G1Y_EuNA4p1HMH4cUw56QV1je3bYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef25218d8a.mp4?token=Sm7A_fY_sLjA6935cxmz95Vl-DlohPcWqcz7RLg9xUx-9u8ksH8vZRTaeYT4zKc6wBuAn2jVyx-GCCs0iMoaNxNmG-1RkTIGb8J25JOxFXRAB_hWAm6-pyJmlAxCvXo3_I1cjT5uNAA5csL_l63-k8pxBwdjytnYmkVESWNss8-kowb-pzHNNmdjwL2-70urt2hacJzVyel8jq5-5Zd8IAPovfMdMz0-qInRPa8uN-saiZMl9m1W12Xnhmv1OoIEeL_VYCUiofinN9st884l8SHqmS-L5T1ndqpD3TmElJwxQlXqbd4PkPqb3G1Y_EuNA4p1HMH4cUw56QV1je3bYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
مشهد، ستاره‌بارانِ حضور مردم در مراسم تجدید بیعت با امام زمان(عج)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/683492" target="_blank">📅 22:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683491">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
روایت دبیر شورای‌عالی امنیت ملی از پیشنهاد جدید نتانیاهو به ترامپ
🔹
نتانیاهو در واشنگتن به ترامپ گفته ایران را ۶ ماه محاصرۀ اقتصادی کن من به تو قول می‌دهم ایران تسلیم می‌شود. ترامپ گفته در این مورد اشتباه می‌کنی. نتانیاهو گفته ۲-۳ ماه این موضوع را امتحان…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/683491" target="_blank">📅 22:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683490">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5300c5e24.mp4?token=t_52v_X3ujBdF8Pjx0bjij065iwd17ACjF8AlLhvP_dUIZn2Tp4az6UoiiIkjIjSBnYDtpfuuTBA7g-btK6HjonZmuvpsVFsfs6BI2K-SlhndS5eh3CWlFcZ7hjDIcdb4p_s8MLumUtbCxfibUnkXH92hUffM-vRjrsc7kbLTnSlKFQBdCpRKi1h26jV0m_avieq1Za867poQXP4l0V60DQcUvcU3G45r6INR-vLlVcAazsRWbqAAZZUfg_xJdS6c3xCKM5OMkP8aym1fx4s_kbptuJtmVLX5KoGHw6p_sWiuZ5fhnHJTqMeIxh5_UdBOP3Dp4svt51m5wR9v4CAloi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5300c5e24.mp4?token=t_52v_X3ujBdF8Pjx0bjij065iwd17ACjF8AlLhvP_dUIZn2Tp4az6UoiiIkjIjSBnYDtpfuuTBA7g-btK6HjonZmuvpsVFsfs6BI2K-SlhndS5eh3CWlFcZ7hjDIcdb4p_s8MLumUtbCxfibUnkXH92hUffM-vRjrsc7kbLTnSlKFQBdCpRKi1h26jV0m_avieq1Za867poQXP4l0V60DQcUvcU3G45r6INR-vLlVcAazsRWbqAAZZUfg_xJdS6c3xCKM5OMkP8aym1fx4s_kbptuJtmVLX5KoGHw6p_sWiuZ5fhnHJTqMeIxh5_UdBOP3Dp4svt51m5wR9v4CAloi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت دبیر شورای‌عالی امنیت ملی از پیشنهاد جدید نتانیاهو به ترامپ
🔹
نتانیاهو در واشنگتن به ترامپ گفته ایران را ۶ ماه محاصرۀ اقتصادی کن من به تو قول می‌دهم ایران تسلیم می‌شود. ترامپ گفته در این مورد اشتباه می‌کنی. نتانیاهو گفته ۲-۳ ماه این موضوع را امتحان…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/683490" target="_blank">📅 22:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683489">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e563bffa09.mp4?token=TuU37SgvHcCMz8NacEH3IYCFXl4r-1D5KARTeiTS6qdmJcdvT9uSPipglyDYHPtFiSFeKQ7N-_2aV9qeZ-TOv2qNRRoaeXuYw54XWwEMVKVxzHDadRPZdNTJu5UU-lEcoYl1wuA-MpEOfCvHbT4iuHC4bhzCAcrylDZpSHcwzA5ysgqehWd7O5Z_kXXdEUnMailnnylIBlncxMtGyi3-nfJ0T7I9wgh-TeS6MLknBM16IiHv6XZ0JgKYojIlNM-RLGHl2_R7ZeHRZtwj6zqV_87Pdv73nuwvQxIXvXy9VuUWPuFRLURZdZIgLibnNclImLroe3mAjnScDVqM866IZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e563bffa09.mp4?token=TuU37SgvHcCMz8NacEH3IYCFXl4r-1D5KARTeiTS6qdmJcdvT9uSPipglyDYHPtFiSFeKQ7N-_2aV9qeZ-TOv2qNRRoaeXuYw54XWwEMVKVxzHDadRPZdNTJu5UU-lEcoYl1wuA-MpEOfCvHbT4iuHC4bhzCAcrylDZpSHcwzA5ysgqehWd7O5Z_kXXdEUnMailnnylIBlncxMtGyi3-nfJ0T7I9wgh-TeS6MLknBM16IiHv6XZ0JgKYojIlNM-RLGHl2_R7ZeHRZtwj6zqV_87Pdv73nuwvQxIXvXy9VuUWPuFRLURZdZIgLibnNclImLroe3mAjnScDVqM866IZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: برادران ما آماده عملیات هستند اما ما با یک شیب عاقلانه و منطقی حرکت می‌کنیم، امیدواریم آمریکایی‌ها شرارت را تمام کنند و ما به مرحله بعدی نرسیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/683489" target="_blank">📅 22:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683488">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
محسن رضایی: اگر ترامپ بخواهد کارهایی بکند زلزله‌وار مقابله به مثل می‌کنیم  دبیر شورای عالی امنیت ملی:
🔹
به همه کشورهای اطراف می‌گوییم در جنگ اقتصادی با آمریکا شریک نشود وگرنه او را دشمن تلقی می‌کنیم.
🔹
دنبال توسعه جنگ نیستیم اما اگر کشورهای اطراف ایران در…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/683488" target="_blank">📅 22:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683487">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
محسن رضایی: اگر ترامپ بخواهد کارهایی بکند زلزله‌وار مقابله به مثل می‌کنیم
دبیر شورای عالی امنیت ملی:
🔹
به همه کشورهای اطراف می‌گوییم در جنگ اقتصادی با آمریکا شریک نشود وگرنه او را دشمن تلقی می‌کنیم.
🔹
دنبال توسعه جنگ نیستیم اما اگر کشورهای اطراف ایران در جنگ اقتصادی با آمریکایی‌ها همراهی کنند منافعشان را می‌زنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/683487" target="_blank">📅 22:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683486">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e563bffa09.mp4?token=W4FrdItWR9pYxZnfoivH2JE-ehjYwFmH4bM3RjWbISWVpZx82pIBcV2yTJ8XkOKuMaIRQiN_QvnC9lNs9kS_7gL8zIu80IMf7Hve286zw7qqj0VbKapumet5kRwCVcSMeMBgUIyx5VTkB4eqZhpXsB22mvWBybGHKdU4OsBNxaCL3JhV9QBEXnvXeUS412kgxeOPRwgvs_aNTIkOlmDocerzP6mWzz4_EJN5CfkTnTYWfI68V9BEbxs9IX8lDuBGV77u8YOMoAvO9bDnX0TO-C4nH5kZ0WSR4KaYZ0b21Ifih9XWTUjxlzjlqvYK4m--PVrnQqG93NRuTyYxhs2sGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e563bffa09.mp4?token=W4FrdItWR9pYxZnfoivH2JE-ehjYwFmH4bM3RjWbISWVpZx82pIBcV2yTJ8XkOKuMaIRQiN_QvnC9lNs9kS_7gL8zIu80IMf7Hve286zw7qqj0VbKapumet5kRwCVcSMeMBgUIyx5VTkB4eqZhpXsB22mvWBybGHKdU4OsBNxaCL3JhV9QBEXnvXeUS412kgxeOPRwgvs_aNTIkOlmDocerzP6mWzz4_EJN5CfkTnTYWfI68V9BEbxs9IX8lDuBGV77u8YOMoAvO9bDnX0TO-C4nH5kZ0WSR4KaYZ0b21Ifih9XWTUjxlzjlqvYK4m--PVrnQqG93NRuTyYxhs2sGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: حماقت ترامپ دنیا را به سمت دستیابی به بمب اتم سوق داده
🔹
حماقت ترامپ با حمله به ایران اشتیاق مردم جهان به بمب اتم را بیشتر کرد زیرا همۀ دنیا دیدند عضویت در سازمان انرژی اتمی و NPT برای جلوگیری از حمله آمریکا اثری ندارد.
🔹
ترامپ…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/683486" target="_blank">📅 22:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683485">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: امروز ملت ۵ هزار سالۀ ایران با دولت ۲۵۰ سالۀ آمریکا در تقابل است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/683485" target="_blank">📅 22:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683483">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04bbe9cc53.mp4?token=s-094HXsxI3viB2cGPEMnw5BthzHtRhBPO9p_Ey4cP7FFsMgltGmZLc9wxCVsd7LX_4kP7a5TqxN_FOS9sEFuKStBxtmsCFntb5parnBTmZaVggzA07KDhIMl__YwsWB9JyFshu3s4Yeij3XVdMdITTnQWgQnU9QMSfLycqSo78VN7PzhGRKaeAFIH1H9wArRpWiz-eL36KRJxaCQ7kiYOZbtMTLKVQObZeLh0IT6RDFzN1Y6zUaq7QA4ezSuPRjBRzZ-reCqYpeo_SzswsM6mc7LpAd_WjRlyWfQmqfY0DIfVixgIkbUcKie5V3uO1NYgQvyVHbiDPb07jTEkquLmrV3jaA4HHIOxddQaMjTdxfxm7Cuw_YPYHtJV_fmZvfRbwcI72IpONJ0DvSI3QH5wFTDPwMmNqRTQS_S30g84Pth6tQ5x8OfhF6X27iYIwuBoUBrtZk6if3I7MXcypLHDli3_lcq0DB3prAbqXf8nGwWg6Bu4NC4CpoNTJpReTgG06tIsVLmWdXQw6d5FnZ6iu5LOyZJxtkSnZnYqOQHCwWeRXRUlomWlRJ85Mwi1EOm2rsnkHhtA7dKreFXGZz6KV0oowVrj5Zy1zLZoTxkHeE35nNnSyKKfEM1rD2DLtqYGORYhvOD8AdcNDjFk5bUlcjtFAYfYNWvCD-S4YKXwM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04bbe9cc53.mp4?token=s-094HXsxI3viB2cGPEMnw5BthzHtRhBPO9p_Ey4cP7FFsMgltGmZLc9wxCVsd7LX_4kP7a5TqxN_FOS9sEFuKStBxtmsCFntb5parnBTmZaVggzA07KDhIMl__YwsWB9JyFshu3s4Yeij3XVdMdITTnQWgQnU9QMSfLycqSo78VN7PzhGRKaeAFIH1H9wArRpWiz-eL36KRJxaCQ7kiYOZbtMTLKVQObZeLh0IT6RDFzN1Y6zUaq7QA4ezSuPRjBRzZ-reCqYpeo_SzswsM6mc7LpAd_WjRlyWfQmqfY0DIfVixgIkbUcKie5V3uO1NYgQvyVHbiDPb07jTEkquLmrV3jaA4HHIOxddQaMjTdxfxm7Cuw_YPYHtJV_fmZvfRbwcI72IpONJ0DvSI3QH5wFTDPwMmNqRTQS_S30g84Pth6tQ5x8OfhF6X27iYIwuBoUBrtZk6if3I7MXcypLHDli3_lcq0DB3prAbqXf8nGwWg6Bu4NC4CpoNTJpReTgG06tIsVLmWdXQw6d5FnZ6iu5LOyZJxtkSnZnYqOQHCwWeRXRUlomWlRJ85Mwi1EOm2rsnkHhtA7dKreFXGZz6KV0oowVrj5Zy1zLZoTxkHeE35nNnSyKKfEM1rD2DLtqYGORYhvOD8AdcNDjFk5bUlcjtFAYfYNWvCD-S4YKXwM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آثار و برکات دعا برای فرج امام زمان از زبان حجت‌الاسلام حیدری کاشانی در اجتماع بزرگ بیعت مردم مشهد با امام زمان (عج)
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/683483" target="_blank">📅 22:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683482">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d73a84331a.mp4?token=CdZZuHJ1B1H0l0e-1DCQPWbmTR3jpbZYuAuhjwGTQVKR_FXlCNjZmyEC6z4cXwVRSzxcEvAiXZ_RoUjHED_lhTrEb3KTyzqQNQsblIQj3hEn9efcaqVVYkdhWZsT6bW7ZxIu5ryishczg-j_WkXlNnS0cbv1rGwfISwridfeaDluLzyRnWZIkDaQmu1UpjpMmaj8wrdEhEfAED7ZbqtZ9cngudUDFj94_Ly6a-LI0bMPSnWTpCsQ6HIv7DQaf2bXIcd3im-feoohPcDxqe6UKc4VrmmqKEW01OerpvhzcL7df0B8HeMW4wHEBogt1fqJUFfniOze7_OGE3rXrgZjsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d73a84331a.mp4?token=CdZZuHJ1B1H0l0e-1DCQPWbmTR3jpbZYuAuhjwGTQVKR_FXlCNjZmyEC6z4cXwVRSzxcEvAiXZ_RoUjHED_lhTrEb3KTyzqQNQsblIQj3hEn9efcaqVVYkdhWZsT6bW7ZxIu5ryishczg-j_WkXlNnS0cbv1rGwfISwridfeaDluLzyRnWZIkDaQmu1UpjpMmaj8wrdEhEfAED7ZbqtZ9cngudUDFj94_Ly6a-LI0bMPSnWTpCsQ6HIv7DQaf2bXIcd3im-feoohPcDxqe6UKc4VrmmqKEW01OerpvhzcL7df0B8HeMW4wHEBogt1fqJUFfniOze7_OGE3rXrgZjsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: تصمیم رهبر انقلاب برای آمدن فرماندهان باتجربه معنایش این است که تجارب یک‌سال گذشته حتما در نبرد آینده استفاده می‌شود و جنگ آینده متفاوت‌تر از جنگ ۴۰ روزه خواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/683482" target="_blank">📅 22:22 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683481">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
نیوزویک: تهران در کوتاه مدت تسلیم فشار نمی‌شود
نیوزویک:
🔹
مهم‌ترین سناریوی فعلی این است که تهران در کوتاه‌مدت تسلیم فشار نمی‌شود. ایران با تکیه بر شبکه پیچیده‌ای از کانال‌های تجاری غیررسمی، فروش نفت به چین و اقتصاد داخلی نسبتاً متنوع، به نوعی «صبر راهبردی» روی آورده است.
🔹
در مقابل، واشنگتن با تشدید تحریم‌ها و تهدید به محاصره دریایی، به دنبال فروپاشی اقتصادی ایران است. بار بحران اما تنها بر دوش ایران نیست؛ استراتژی آمریکا با چالش‌های داخلی ملموسی روبرو است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/683481" target="_blank">📅 22:22 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683480">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46a51b803f.mp4?token=RknuDvCDACTZ4PiLhOqi_S0rJqo4dJxT76dr2eHLL1QPivSr7qTtpMp8g1tjl2w4azKPKtxpcPxTF_qdnjE2NJlaGTXNZfyxmh1fzALSuG0EgN4xOpva7EoS5j1wJfxRlx_tcAybeGsRPAKa5i9jgGMKUqyfm3nYALiZMW_SRBdPSMUbBytP9d07osJfPd2Ej7DcaGAjjE62KsQj5gAh2ywO3tBhtL_ocbNGhVt0WXJtm-bBUkA94kH-Jn82jxzn0HkF7LrMJfoUDUScZO9pwFhSewxa-e7InbdrxueCRxaaP4y7-O_Ey6Cft_oko9Wb8tmzkbtDJJ8jPrY-7iaGwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46a51b803f.mp4?token=RknuDvCDACTZ4PiLhOqi_S0rJqo4dJxT76dr2eHLL1QPivSr7qTtpMp8g1tjl2w4azKPKtxpcPxTF_qdnjE2NJlaGTXNZfyxmh1fzALSuG0EgN4xOpva7EoS5j1wJfxRlx_tcAybeGsRPAKa5i9jgGMKUqyfm3nYALiZMW_SRBdPSMUbBytP9d07osJfPd2Ej7DcaGAjjE62KsQj5gAh2ywO3tBhtL_ocbNGhVt0WXJtm-bBUkA94kH-Jn82jxzn0HkF7LrMJfoUDUScZO9pwFhSewxa-e7InbdrxueCRxaaP4y7-O_Ey6Cft_oko9Wb8tmzkbtDJJ8jPrY-7iaGwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر رضایی: دشمن روی تفرقه حساب کرده است؛ وحدت ما کمتر از قدرت نظامی نیست  دبیر شورای عالی امنیت ملی:
🔹
از ملت عزیز ایران می‌خواهیم در این رویارویی بزرگ، وحدت و انسجام خود را حفظ کنند و اجازه ایجاد تفرقه داده نشود.
🔹
امام خمینی(ره) و امام شهید ما، همواره…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/683480" target="_blank">📅 22:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683479">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a7026789.mp4?token=Wlo3eC9azqhXYAtOQKdJo8NpZflfQD8DkxN46bsVDsT5ptw061-_v23r5Rghf3sHtuCe-X_ivV3QAsXjJwmu05YXA0nZjlJJJUmz60e9jtQKKWFH_xpnvBI-lsozvVspVZ_soljZYOvvDT3RlH_3mMtXFeOyS2_qahi0mdMkaX0gGm2qmg0xFi_xttrG_6THO_Usgc50TV2SPTQyc3E84i6luKj-Ifc8YfypBt-rGkjo-PFn71bFN6ZKamY1DNfoLFkpFW8hYEh5cf_an_E8U7kgR-5k5AlUqrMUx_FvHE1m8iIKzP1tdWGHJ3oFAKQ-7_cgaWYLPaOfkv8lILJFm2qKjW-6En8lj4ofs4VfzvjYH-ihaLeqbphO7dlGnxUNJ-KbWHegZijIibo7rYg49TPGFGETzlZQ1C1zYb8FEUMNE4hweYIZEdPFNP_QaqavSFETuVWREyGh62tLhJLmvFQhMI-4nwBEzUpuxQhg7VagGAWledJtu7cy-KaHQGlEVKn2M8IMXpa9LzPZfE3Oy66EgDkCU-v56S739jlEZfXx37uaKK5YKSZbRuk4iC2xHzt0zeADGvCYDYT2EAVXmeX_82j0yWZseXOcFGJbN6dYihhQYReh7D6GVaMwD-IM1uEGtnidMiO76CXLYG7co-0NPyrxNKiTAx9b7NiWvjo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a7026789.mp4?token=Wlo3eC9azqhXYAtOQKdJo8NpZflfQD8DkxN46bsVDsT5ptw061-_v23r5Rghf3sHtuCe-X_ivV3QAsXjJwmu05YXA0nZjlJJJUmz60e9jtQKKWFH_xpnvBI-lsozvVspVZ_soljZYOvvDT3RlH_3mMtXFeOyS2_qahi0mdMkaX0gGm2qmg0xFi_xttrG_6THO_Usgc50TV2SPTQyc3E84i6luKj-Ifc8YfypBt-rGkjo-PFn71bFN6ZKamY1DNfoLFkpFW8hYEh5cf_an_E8U7kgR-5k5AlUqrMUx_FvHE1m8iIKzP1tdWGHJ3oFAKQ-7_cgaWYLPaOfkv8lILJFm2qKjW-6En8lj4ofs4VfzvjYH-ihaLeqbphO7dlGnxUNJ-KbWHegZijIibo7rYg49TPGFGETzlZQ1C1zYb8FEUMNE4hweYIZEdPFNP_QaqavSFETuVWREyGh62tLhJLmvFQhMI-4nwBEzUpuxQhg7VagGAWledJtu7cy-KaHQGlEVKn2M8IMXpa9LzPZfE3Oy66EgDkCU-v56S739jlEZfXx37uaKK5YKSZbRuk4iC2xHzt0zeADGvCYDYT2EAVXmeX_82j0yWZseXOcFGJbN6dYihhQYReh7D6GVaMwD-IM1uEGtnidMiO76CXLYG7co-0NPyrxNKiTAx9b7NiWvjo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام حیدری کاشانی در اجتماع بزرگ بیعت مردم مشهد با امام زمان (عج): اجرای قوانین اسلامی و زمینه‌سازی ظهور باید دغدغه اصلی مسئولان جمهوری اسلامی باشد؛ مسئولی که در این مسیر کوتاهی کند، به تعبیر امام، خائن و خطرساز است / حجاب به‌عنوان یک حکم قطعی اسلامی، باید در جمهوری اسلامی مطالبه عمومی باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/683479" target="_blank">📅 22:18 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683478">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnxL1y-KR7r17mnqYVcpVcsKQT-YANg8lEbU4kMSIdwQpRf3dy7k75VeTgbMtWXqViZIzQbarGJyI-5qU9ck2IcoLqbxEcQkA6PH1ApTFtQuRZJQpsGL4mfUK3k6mliG9vOLK2JYR0K2rbrinTfLBcSFjsFUIaDbUq7Vs5e-WIdI4tUtE8nbGSsGoYH87GArogczfOiqTrxPuftYEWMUQvtfSURysLX266MBqfd5mDA3Q_hrsfeylgXMg2mAa79WLuHmhXREkaLgYHBs7u6XHAapWji_RPvaXbrlOlewnCx9nShc5l7xMos6kIQkkux1-31Ysrb4rPGQ26pZkk8urA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در قعر خلیج فارس
فرمانده کل قوا:
🔹
بیگانگانی که از هزاران کیلومتر دورتر، طمع‌کارانه در خلیج فارس شرارت می‌کنند، جایی در آن ندارند مگر در قعرِ آب‌هایش.
🔹
بخشی از پیام رهبر معظّم انقلاب به مناسبت روز ملی خلیج فارس | ۱۰/اردیبهشت/۱۴۰۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/683478" target="_blank">📅 22:18 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683477">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
محسن رضایی: در شیوه جنگ و مسائل اجتماعی حتما تحول خواهیم داشت  دبیر شورای عالی امنیت ملی:
🔹
همه تجارب یکسال گذشته را حتما در نبرد آینده به کار خواهیم گرفت و حتما جنگ آینده متفاوت از جنگ تحمیلی سوم خواهد شد.
🔹
حتما در مسئله اداره شیوه جنگ تغییراتی خواهیم داد.…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/683477" target="_blank">📅 22:16 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683476">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c48885d423.mp4?token=WD6Ya2qNjmCjFUiW7WQoPPXpU34SwjIV71VWYZtm5_XDaKwBf2XT3PfoGWtE9jI1KmzJFF_eoVvenDnE16Qj9GlkkQIUI-NXyeOWepvcYSm7GOU9FSBCVPS6jiXMPZyxSLg7DWbgcxO-apF1H2rorZ9Weurpddy5WrrS1rg9ZZsMYQIcb1DiDAkYk9r71NvZCYBm-wMjbduKJZp4PxrQ2CZxuzeXBeLAFvch0Neph3olST7QYFm7fptPW6QOY75mQhvAoBAT0k4ICebbnKYx4EReod3Fne9KIsSS2f7d4gzuk7OnzrdBY5LJS8UN4rAeOMevGyU-TOMH-VnKL_KpCG1EbAcFi8oeuab4y1t4btU7YssBPD-b_LvZo8Plc3GuelyLwq_5Cm0H7pMdfH6azuPPhDB85m24xbDBjxu0DJMlgVTdZl6XOlsmXM4NYjU61DRMBEdvUXl0ebEPtbLRU7rFZ8OfAtrQvKIgV40YjKX8GkEEMwS_KNuMzSUJ_sgsojBRGZNhFoUPtuVAXVykNCXUUgJR6lLGy8lSz0sfI-Bsbjb6EFkakC6xO9CsNyEweeWJkxED3iYpxXUaeI472_YIqYy2HmjgzuWQJWrOwMpTu9RhHz1TTqwxgRPTaF2tLInzOnfHaRkUFOfZMLTvFP6-9VR1xUDQfeC6LImD1LI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c48885d423.mp4?token=WD6Ya2qNjmCjFUiW7WQoPPXpU34SwjIV71VWYZtm5_XDaKwBf2XT3PfoGWtE9jI1KmzJFF_eoVvenDnE16Qj9GlkkQIUI-NXyeOWepvcYSm7GOU9FSBCVPS6jiXMPZyxSLg7DWbgcxO-apF1H2rorZ9Weurpddy5WrrS1rg9ZZsMYQIcb1DiDAkYk9r71NvZCYBm-wMjbduKJZp4PxrQ2CZxuzeXBeLAFvch0Neph3olST7QYFm7fptPW6QOY75mQhvAoBAT0k4ICebbnKYx4EReod3Fne9KIsSS2f7d4gzuk7OnzrdBY5LJS8UN4rAeOMevGyU-TOMH-VnKL_KpCG1EbAcFi8oeuab4y1t4btU7YssBPD-b_LvZo8Plc3GuelyLwq_5Cm0H7pMdfH6azuPPhDB85m24xbDBjxu0DJMlgVTdZl6XOlsmXM4NYjU61DRMBEdvUXl0ebEPtbLRU7rFZ8OfAtrQvKIgV40YjKX8GkEEMwS_KNuMzSUJ_sgsojBRGZNhFoUPtuVAXVykNCXUUgJR6lLGy8lSz0sfI-Bsbjb6EFkakC6xO9CsNyEweeWJkxED3iYpxXUaeI472_YIqYy2HmjgzuWQJWrOwMpTu9RhHz1TTqwxgRPTaF2tLInzOnfHaRkUFOfZMLTvFP6-9VR1xUDQfeC6LImD1LI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
«قیام کن، دنیا احترام کن؛ به جمهوری اسلامی ایران سلام کن»
🇮🇷
▫️
حال‌وهوای بی‌نظیر مراسم «تجدید بیعت با امام زمان (عج)»
@Heyate_gharar</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/683476" target="_blank">📅 22:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683475">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2085dd4e0.mp4?token=XSF6PcEZ8d764vbwrn5GbU3sSDT4KqXMEhv6vwlTU5fqoM76fl4z1IuAoNr2mRMtZdhOemvarb5hFDSEOHV2t8IDR0SFgUXxufv79qK2vsbGxCsSO-QuYYucLeP0qwaKRGGoM0LRyPzu6_nWZ62-k0xdBMJb0EkLIIuJsSEW48MXPyd0XM8woC7hiLI8qHMW6Arhe5jhEHb9mwSIIi4AFIFThrSthDpMlXzHsWH9qW7-S5XPpiZlkTkGvPnttIiaTBB8XjRYjhvBJkDrb2by1Lo2XKNtxciRo3NI_8rz03tzxOIBsPNLX_lHBuNGC37l0KmDV8CG5hCy4YUSm5xx4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2085dd4e0.mp4?token=XSF6PcEZ8d764vbwrn5GbU3sSDT4KqXMEhv6vwlTU5fqoM76fl4z1IuAoNr2mRMtZdhOemvarb5hFDSEOHV2t8IDR0SFgUXxufv79qK2vsbGxCsSO-QuYYucLeP0qwaKRGGoM0LRyPzu6_nWZ62-k0xdBMJb0EkLIIuJsSEW48MXPyd0XM8woC7hiLI8qHMW6Arhe5jhEHb9mwSIIi4AFIFThrSthDpMlXzHsWH9qW7-S5XPpiZlkTkGvPnttIiaTBB8XjRYjhvBJkDrb2by1Lo2XKNtxciRo3NI_8rz03tzxOIBsPNLX_lHBuNGC37l0KmDV8CG5hCy4YUSm5xx4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: در شیوه جنگ و مسائل اجتماعی حتما تحول خواهیم داشت
دبیر شورای عالی امنیت ملی:
🔹
همه تجارب یکسال گذشته را حتما در نبرد آینده به کار خواهیم گرفت و حتما جنگ آینده متفاوت از جنگ تحمیلی سوم خواهد شد.
🔹
حتما در مسئله اداره شیوه جنگ تغییراتی خواهیم داد.
🔹
آمریکایی‌ها به مذاکرات، دیپلماسی و امضایشان خیانت کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/683475" target="_blank">📅 22:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683474">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d89fa5dda.mp4?token=vOV8s0Z3vYrdp-EYGvMsEETnG4MTrXUR_xJ8elX49vd1bbblKP4AFGJtchrih7Bm-sDPj1xzbQOCLa1mBNPbaVCuJzVzpggv39jcfuU9zG9KRhOw5KV5iBYw0YMBvogVoaJEH9Cl0ROEYEJGtdOG_YuL2zzFQltSlLtdiyCAdCQCM9NYvL68Vg6eOhv8Cag6kxC8h9Ub2UmJAqcugYAhp2-fH_99jvFem4xTca77fiYegF3LzJhdilYQwKNaDZRHkaJjmsIycesIxHYtE3pfo_0tjnhyiNAMRIXdwayp_ucKmBZdrfktJ4ADvi1PpLLcqHz_U6LWHMD7d8NHMwyPTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d89fa5dda.mp4?token=vOV8s0Z3vYrdp-EYGvMsEETnG4MTrXUR_xJ8elX49vd1bbblKP4AFGJtchrih7Bm-sDPj1xzbQOCLa1mBNPbaVCuJzVzpggv39jcfuU9zG9KRhOw5KV5iBYw0YMBvogVoaJEH9Cl0ROEYEJGtdOG_YuL2zzFQltSlLtdiyCAdCQCM9NYvL68Vg6eOhv8Cag6kxC8h9Ub2UmJAqcugYAhp2-fH_99jvFem4xTca77fiYegF3LzJhdilYQwKNaDZRHkaJjmsIycesIxHYtE3pfo_0tjnhyiNAMRIXdwayp_ucKmBZdrfktJ4ADvi1PpLLcqHz_U6LWHMD7d8NHMwyPTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: باید در رفتار دیپلماتیک ایران اصلاحاتی انجام شود
دبیر شورای عالی امنیت ملی:
🔹
در راهبردهای دفاعی ایران تکامل رخ داده و از جنگ تحمیلی دوم دائما درحال تکامل دفاعی - سیاسی است.
🔹
ایران امروز ایران قبل از جنگ نیست؛ این قضیه درباره آمریکای پرمدعا هم صدق می‌کند و تصویر آمریکای صلح خواه و بزک کرده، در ذهن جوانان ایرانی عوض شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/683474" target="_blank">📅 22:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683473">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/567f74a1d9.mp4?token=h8hAwwRmF6NtK4lQ3h9rGXIcskA5ir7zYfpohoNFqf0ObtM43RRPJNBmKCMGSqEK0Tr0Pl_AiW8Pan12_7OHJMnTbAS2zoYVoBRzceiMKiAAjs6j_Q6mP-UCj_n14eTGTsiwEz5Xznf8AJKmb-m0m40wLyt3it7IO84fkN42K90ZyhdoBVyRdDlEXk3musXjgXufKHKi_1LrsFe-SmuMFtPpiMLGRrF-5p0cjSbZYEyyYwMrEcCKHFgd15yvOORydPcwNHBBGZcEeEXM9qaNpf_1xS4yZb03FsZsaNLs7abhs-VpCopjgBnTR0dr_uXiZKxM4S_odNJWP5zrpg2uVUEhbTpASBKDxi6MHujQ9Wj5WPgTexKsWbV2aBYdfN-_5uv2upPaqhKmu-ZEZ_xTq9YjmHamTJJWms0b1yQppDHkJpSavqNycN9h20fMNy3hOiJzhiqGk65zeYV0bi1L1DrgUW8evc2LezcKx7XP_QoU3z41eCQCUhVai9vySab2V27yPXFB2EDvqrdfqK4pOVYo2h5r4YkDclLHU2ZnlIa0_0qwk_o9rO-XD5N7fAc6NI4nK-AWFWwkyV6McEPX-QID_7ITi5c70Hagz4cUwLvEj-37aBAkoyEIjaEhM-5-EG4OdO4xV7qC9QD5IwpoG-VJ5EJI-s1FkeJSJra0YBo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/567f74a1d9.mp4?token=h8hAwwRmF6NtK4lQ3h9rGXIcskA5ir7zYfpohoNFqf0ObtM43RRPJNBmKCMGSqEK0Tr0Pl_AiW8Pan12_7OHJMnTbAS2zoYVoBRzceiMKiAAjs6j_Q6mP-UCj_n14eTGTsiwEz5Xznf8AJKmb-m0m40wLyt3it7IO84fkN42K90ZyhdoBVyRdDlEXk3musXjgXufKHKi_1LrsFe-SmuMFtPpiMLGRrF-5p0cjSbZYEyyYwMrEcCKHFgd15yvOORydPcwNHBBGZcEeEXM9qaNpf_1xS4yZb03FsZsaNLs7abhs-VpCopjgBnTR0dr_uXiZKxM4S_odNJWP5zrpg2uVUEhbTpASBKDxi6MHujQ9Wj5WPgTexKsWbV2aBYdfN-_5uv2upPaqhKmu-ZEZ_xTq9YjmHamTJJWms0b1yQppDHkJpSavqNycN9h20fMNy3hOiJzhiqGk65zeYV0bi1L1DrgUW8evc2LezcKx7XP_QoU3z41eCQCUhVai9vySab2V27yPXFB2EDvqrdfqK4pOVYo2h5r4YkDclLHU2ZnlIa0_0qwk_o9rO-XD5N7fAc6NI4nK-AWFWwkyV6McEPX-QID_7ITi5c70Hagz4cUwLvEj-37aBAkoyEIjaEhM-5-EG4OdO4xV7qC9QD5IwpoG-VJ5EJI-s1FkeJSJra0YBo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام حیدری کاشانی در اجتماع بزرگ بیعت مردم مشهد با امام زمان (عج): دشمن پس از ناکامی در جنگ نظامی، جنگ اقتصادی و فرهنگی را در پیش گرفته و به‌دنبال ترویج بی‌حجابی و بی‌عفتی است / مطالبه از مسئولان، اجرای قانون اسلامی و مقابله با این روند است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/683473" target="_blank">📅 22:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683472">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی ایران: شکرگذاریم که خدا رهبری شبیه رهبر شهیدمان به ما دادند
محسن رضایی:
🔹
شکرگذاریم که خدا رهبری شبیه رهبر شهیدمان به ما دادند. با وجود اینکه خودشان دارای حزن بزرگی هستند و خانواده خودشان را از دست دادند ولی خیلی قدرتمند ایران را اداره کردند و در مقابل جنگ از ایران دفاع کردند. با شجاعت در صحنه دیپلماسی و جنگ حاضر شدند و سربلند بیرون آمدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/683472" target="_blank">📅 22:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683471">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgr_PTdFudVDyOVx9X5ecnQVUa1r6elIZDwkGXtgHN8RZfbagq0c0WMKqxaNXBGoEjlef9jYFgjqOgvd6QmGbBfGnhLFeI-A-zu7y29SJFAy0oowyIEEDTktQb6yemeUb99xlysXVuGN6JylPJ6G8PjVkmzuHOeolDUeoDyDPrPx97XSZuwrArV8Wa1tV1jPCEgTWJPDZP3b_MXfim3EOTF2lgaQmPAYqYhxikRyvwfyVGbyr-KqsSV3Ry7htKPSnwZWhLORqRC1i7Gzm1Pq8KmXvmmVKLEiE8KuKvpppf5nNanpD3oey1lDHtjaKZK0gWPTvBEKAXVnlyKVN1bGzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شما خنگ نیستید، شما فقط به اندازه کافی پول ندارید! | رتبه کنکور را حساب بانکی والدین تعیین می‌کند | پشت رتبه‌های برتر کنکور چه می‌گذرد؟
🔹
«آموزش رایگان» حداقل به صورت آنچه ما از آن به یاد داریم حالا به یک شوخی بدل شده، یک شوخی که راستش خیلی هم خنده‌دار نیست. وقتی هزینه‌های یک کنکور معمولی برای ورود به دانشگاه‌هایی که پر از صندلی‌های خالیست به رقم چهارصدمیلیون تومان رسیده شما نباید چندان نگران این باشید که عدم قبولی شما در دانشگاه‌های برتر به معنای این است که شما از بهره هوشی کمی برخوردارید، خیر! شما فقط به اندازه کافی پول ندارید!
گزارش میثم اسماعیلی را در وبسایت خبرفوری بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3239632</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/683471" target="_blank">📅 22:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683470">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
یک اشتباه رایج در بازار طلا؛ حباب منفی همیشه فرصت نیست
🔹
طلا هفته گذشته یک نشانه مهم به معامله‌گران داد و هر گرم طلا حدود ۶۵۰ هزار تومان زیر ارزش ذاتی معامله شد. در نگاه اول، این فاصله می‌تواند یک فرصت خرید به نظر برسد، اما رفتار یک سال اخیر بازار هشدار دیگری می‌دهد.
🔹
بررسی دو تجربه قبلی نشان می‌دهد حباب منفی الزاماً مقدمه رشد قیمت نبوده و حتی در کوتاه‌مدت با افت طلا همراه شده است. به نظر می‌رسد بازار گاهی کاهش احتمالی دلار یا اونس جهانی را پیش از وقوع، در قیمت طلا لحاظ می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/683470" target="_blank">📅 22:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683468">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ed41d78d.mp4?token=Che7KMlNYhtSdcZbRsksKNviDS8yh0lkgO373OjozgsYu-YFc_eYGvapSU_O7JgfMUg9OHB4PTAzZ08QYN4jc05jfrQ1_vXMmxkn9-oD7uji4xVvpPWFfZWWp3oFNYaJxW_LagT2flD_xCYBkUz1uWrA1wK7ddMoivVUmpHd-HUjzzHUZngoGEsb634Jq9hhWkLWjZPbxS-NDVX7Rfq9Ker03XAhpduytJLJTkp6bSj6SQNmwyc6vXyMFf_zUrQprQ_tZ-ky31u5CtPm5_c-de7ejVVWXM4_2PeK0PFA2-aZjJLqB5DL0vR69-pbYhzVgWk9yJ3sUPCNO0VQHYZ5iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ed41d78d.mp4?token=Che7KMlNYhtSdcZbRsksKNviDS8yh0lkgO373OjozgsYu-YFc_eYGvapSU_O7JgfMUg9OHB4PTAzZ08QYN4jc05jfrQ1_vXMmxkn9-oD7uji4xVvpPWFfZWWp3oFNYaJxW_LagT2flD_xCYBkUz1uWrA1wK7ddMoivVUmpHd-HUjzzHUZngoGEsb634Jq9hhWkLWjZPbxS-NDVX7Rfq9Ker03XAhpduytJLJTkp6bSj6SQNmwyc6vXyMFf_zUrQprQ_tZ-ky31u5CtPm5_c-de7ejVVWXM4_2PeK0PFA2-aZjJLqB5DL0vR69-pbYhzVgWk9yJ3sUPCNO0VQHYZ5iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
ای خسرو مه وش بیا
ای خوشتر از صد خوش بیا
ای آب و ای آتش بیا
ای در و ای دریا بیا
▫️
شعرخوانی حسین حقیقی در جشن «تجدید بیعت با امام زمان(عج)»
@Heyate_gharar</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/683468" target="_blank">📅 22:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683467">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
پزشکیان: آن هایی که دستی بر آتش داشتند، در شورای عالی امنیت ملی معتقد بودند این تفاهم‌نامه، بهترین تفاهم‌نامه است  رئیس جمهور:
🔹
در تمام تفاهم‌نامه یک بند پیدا نمی‌کنید که ما، وا داده باشیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/683467" target="_blank">📅 21:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683466">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEg17CHWCnWQ63r4W8R5pz9u0L0wV1ATCf8HZsR7RmAiNz1EPtwOk2vz39wSjoQ9mgxiVVKTi1qhf3jOlaFs6LoV8v2PC7B5zvTaAYugnyiUTdbSvf-ZV27gMsfl1tN-bMllEye3tuPjGBCByNwnJr0uZIcc1pXIodk3Lt6KNHxsHh1dE2vK9ptkRezVs0AHp4VZW5L-4Bp0EzJkZWWv9vWHc6TT43rqa4I4ZAe8kp_sFSPhfFev4EtcSXwPgIMvG_CgYvh6Kg2mb-iCcMzwMKB4QzlyiIb_5pLV_wJ7laMARJHkqHuSAIXTFtIvoWqeDNOO0DHZ_gKuJCCs3d7O0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمی از بزرگسالان ایرانی تحرک کافی ندارند!
🔹
در ایران، ۴۶.۳٪ از افراد بالای ۱۸ سال فعالیت بدنی ناکافی دارند؛ یعنی تقریباً نیمی از بزرگسالان ایرانی کمتر از میزان توصیه‌شده فعالیت فیزیکی انجام می‌دهند.
🔹
میانگین جهانی فعالیت بدنی ناکافی ۳۱.۳٪ بوده است؛ یعنی حدود یک‌سوم بزرگسالان جهان تحرک کافی ندارند.
🔹
گسترش سبک زندگی کم‌تحرک، افزایش شهرنشینی و کاهش فعالیت‌های روزمره باعث شده کمبود تحرک به یکی از چالش‌های مهم سلامت عمومی در جهان تبدیل شود.
@amarfact</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/683466" target="_blank">📅 21:57 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683465">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
۲ سوخت‌رسان نیروی هوایی آمریکا، بلغارستان را ترک کردند
🔹
رویترز به نقل از وزیر دفاع بلغارستان اعلام کرد؛ ۲ فروند سوخت‌رسان آمریکا پایگاه هوایی بزمر در این کشور را ترک کردند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/683465" target="_blank">📅 21:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683464">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
پزشکیان: مصمم هستیم بستر را برای آموزش همه آماده کنیم  رئیس جمهور:
🔹
با نگاه سلامت در تبلیغات شرکت کردیم. همه کسانی که سوادشان و علمشان کم است، از نظر سلامت در خطر هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/683464" target="_blank">📅 21:52 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683463">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1923648b7c.mp4?token=jGEGUeXF6dEoJUZwWNfQUkfymE0I2a4K9DoXFezNLVauL6Vf6W_Iby5HWT4ZEGxzcZMJ3qtKxXM1iVwQ-1_f6DhxO5uQ5OZJVQplUQjCfl0QxG0OoSZ9eZ329DFudiWtP5QgZ2LcNvzk68-hxl2UHMmRDx0oY6astl8qs54NvoC53xs3N5yJsL3GBD8atHg5asKyCWxIlP47PIs8Ek-9VuEnlQz7nlANT4E5yS2OxaMkvB_qEeVN4KDAeEOMebNKBlAz9a5za8PHfpHvMJbOgPmXlQraDcz-sqB60rpdktf5Q2B_KvVi0bGnbK5udxLG76vWCuTXnoUNhGUPrc_dHgHXFwruJ1Fr0qBKAF81PTEghK1kK3W8U7LsJpZJqMf5Qqo-A1boJWnLA2ums5Vos4TbfOIdaa6gtYSV2m9b2njNz3GtDSxZxJF34nRjCckOEtJrmrMbreSA8bWMxtTd0cL5MvnMgAGeEub_Fp8R9TgVNh8YW6Z9DMHinfjxfnfirMxtbgFHsralXFEhf7BnQe5Kwyu-z5p3lj3fY7z7uYS7GNMxUamPwV_8fM7OSVEnVSUHs1B0P_nziV22HM0_QJBgdqQ2oqOV5FYCTG4QQ8GkYyqwonCMNzwBqdFW3NeJ7o4BB-p4UuRh-EoZL9mELSHE1dxkZCCZSm1ns6ifW10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1923648b7c.mp4?token=jGEGUeXF6dEoJUZwWNfQUkfymE0I2a4K9DoXFezNLVauL6Vf6W_Iby5HWT4ZEGxzcZMJ3qtKxXM1iVwQ-1_f6DhxO5uQ5OZJVQplUQjCfl0QxG0OoSZ9eZ329DFudiWtP5QgZ2LcNvzk68-hxl2UHMmRDx0oY6astl8qs54NvoC53xs3N5yJsL3GBD8atHg5asKyCWxIlP47PIs8Ek-9VuEnlQz7nlANT4E5yS2OxaMkvB_qEeVN4KDAeEOMebNKBlAz9a5za8PHfpHvMJbOgPmXlQraDcz-sqB60rpdktf5Q2B_KvVi0bGnbK5udxLG76vWCuTXnoUNhGUPrc_dHgHXFwruJ1Fr0qBKAF81PTEghK1kK3W8U7LsJpZJqMf5Qqo-A1boJWnLA2ums5Vos4TbfOIdaa6gtYSV2m9b2njNz3GtDSxZxJF34nRjCckOEtJrmrMbreSA8bWMxtTd0cL5MvnMgAGeEub_Fp8R9TgVNh8YW6Z9DMHinfjxfnfirMxtbgFHsralXFEhf7BnQe5Kwyu-z5p3lj3fY7z7uYS7GNMxUamPwV_8fM7OSVEnVSUHs1B0P_nziV22HM0_QJBgdqQ2oqOV5FYCTG4QQ8GkYyqwonCMNzwBqdFW3NeJ7o4BB-p4UuRh-EoZL9mELSHE1dxkZCCZSm1ns6ifW10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
برای حضرت مهدی (عج) که دعا می‌کنیم، نوری از قلب او به قلب ما می‌تابد؛ شاید دعای ما، پیش از آنکه برای او باشد، مرهمی برای دل خودمان باشد…
▫️
بخشی از سخنان حجت‌الاسلام‌والمسلمین حیدری کاشانی
@Heyate_gharar</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/683463" target="_blank">📅 21:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683458">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s495bPe4mRMB6-C-sh8cN7lSuJUDDEamJsJrLhpFhqywJ6CBbxkq6ycOTfQkfE5suDyKNEHl_8XeDcs471SFT7ALiK2mbwjrt8vsHgWC1633P_gYqQRPkjnj-pdJxIa1Vfv-6PgWiA1UnvT3cdDn1Gx8hskXeWu641d9uub1i5qSLKUFES8QHCktUm7kJna5EH6w1nYTaTqgVePNSvCwiAQZADeE8t0NVZWQbRQT8l38Weqf-lOH70Y4msdQxtDS3cAWTv2bDNGkTIWdYrqWTEl4ctqiI7AOenXmlMoZS4yW-kttaYiXa1vcHdgjyqQVrCvfsPxAvHr3o8JU4yN0Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HRA3Gq3JcFTHU6uDet01vKj8d2-Wzya1yEODAlOWNHBpab2fsoL3JO7Z2nAEvHXmturNU7YyN30l3PdxXy1Fmho9NS-t-qlgO7tUW-YbE127tFlEYmBccxBe03wrBsleZzWF4tFAngFpOg5ddS2IjQeP_NsmOVSi5SgcgPw5_-c2v2xCY7DNMBhhrr6Ljhh8w6vbf6nOwRiNTSfB4IMs5mgWQfZKhV7Ki1NWEH3aE7z2YZlBveyilEWQ0TEdKXzP46aapHnJvIdZU2mnG6BV0klE5pboY-QSbmVeIqTDCP5m5TM_p8u5X_bbqbmYnfWrpw68__GKaUd7mQgehikwCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bck1LxMR_q54nqKNiUJk5srisNMImKOHycasS0mjSSzJuxB4OoWpGR7TdcQfnz3OkEC1cT1lFbizlhW874UK-IeAWED0QM5hf3K7hiZWZJJz7rkPGV_7d9DYNXwtwAZizdVhIiwC2g4EuWohgn_hXBlTniJHl9ap7l6KzwNOGlTYwTcq9jXkgcze5gIO2g7B8euQ47iX2FBMrhwHtENS5xeoFTqYxNW06kIinQ0dHxTxXLnL9RGfDAqiY8_PTzo__zs-H1CwmfCI5YCVX-f1kfEnsUNXg2jafP8zDjxkZshNGr32ulB_JXBmmkby__Fas7PtodrQCJj2h-0jLMI36g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IevKxaion_p4CHpD1Pl7tig0a5g9Vimsy9rFWQVa_HLOxEHg0pGcDvfvsQfw6pWe1DhgI4WqNLSPjsLYP7O3IMMa9A8Xt72TSO0Qhk8ENLixScfgq2DHW9pAvL-lzRF_6GiP_bdiridsym_CqVLykTfhsn2exlVNrmIguidNcFiLTJfOIpEb74sqWTe_Qvwq-gkA-L8AKHqjAerkIu9_4WsuDygIyaDwTAyXE2K8huxaTZtPGXn32inhljKO56ateLCYzcVDu3qRqCOWmqzvfiNzbazc2vBHJL8NUa4Ok7kBbOfdoGSNfgEEI8J-Ib2mYnkaDCg2Zf6xHMrNOGHywQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iigu49P2L1Ry4YnpFPdVwlkGAeMyClqKkEUMJjeDZycAUkgQyN0-I2TzRTe5R3LPuMJmvJ9WPLwvEli6jYcPsFx9CAk9nn_MIukzedNHHPVAXD09sgTIFnz02fLTlt4BNmb00b27aAmoqsO6SCVz9WsZuJtFpaemELdSU07mXggtSqYB4o-biKtfPvcpvj_EFOxi4b3XStLd_QMM9enjcwFWHwCDQB8eS8U1LsIapRJIzP_yo-FRNbgatukX5mnoy01pWClalJBYky4OtGSVriC9i4HkUrBpwRuIysV9DCtijKPkJhY70MjHhEWpXF6EejmK8l0A-YIc3HgqtN_8xQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کدهای مخفی که خروجی بهتر از چت جی‌پی‌تی بهت میده
#هوش_فوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/683458" target="_blank">📅 21:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683457">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
۸۸ درصد درخواست پول بانک‌ها رد شد
🔹
تازه‌ترین داده‌های عملیات بازار باز، شدت گرفتن کمبود نقدینگی در شبکه بانکی را نشان می‌دهد.
🔹
تقاضای بانک‌ها برای منابع در یک هفته از حدود ۳۴۸ هزار میلیارد تومان به ۴۸۳ هزار میلیارد تومان رسیده، افزایشی بیش از ۱۳۰ همت.
🔹
در مقابل، پاسخ بانک مرکزی همچنان حوالی ۶۰ همت باقی مانده است؛ یعنی تنها حدود ۱۲ درصد از تقاضا تأمین شده و نزدیک به ۸۸ درصد بی‌پاسخ مانده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/683457" target="_blank">📅 21:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683451">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P8dgmjpYj0WADlr47goQ12cb5W9_iVsOLw0-i-FLkCk-_c4KSWnWoUB5yOUvKYbQVRzfB1t9hkkUkCpzgnKGpcnVvkkbGHuw_HLKkAsvLzZ2Sq3Y4yjZrRafcIttxvYDu9n7DiSC2dmF8LlzpVScCxFbCc3SHg-kUne5-jHq6hjrOSgcKbhuQlDpLKcTZNq736aLZZnCdDPg3yHw1Eo0QXvDHnJ0GhrrGXGtL0mLxYWnCak2iqkmveqspFtguILqBz0mpFIfMAjOVlQfxyh3j0-C06OyOr5zR51A9xrrZalNXtbCn9yOU9V04pt79MGmjdbGzQSRUAoFcMA1XNf8-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fAsFCn_SAhgj_scOV9VDsvvYqAo5jyTQnLz4wThhjJr18tJU7jtLyhn_D3RMhCWewzEHVz7bnEOPmo0PCTJH8CkxMWdVS6pxLS22uT8pVLs4KidYqAiiMsbRs24_1LsMqZuEanBUHrujSr_ies8rjVCwG3kgBKD57GiYQApN0D3SmeXntA3qlB6n45Z7AS1ZXb63SKruWyTe7xKiov76IYARaXlxrQcK6SDgncOCNLm2xPVVeM4LAF0nBQnBoUE1b5UbfBR7cwrJtQBYM8SOAoJF0-cuRBoIlFUAZFv2xkED22lKu5sMcnxfWQDvOFnsDSos2IXW_bsu-ybtRqdMag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZP4LhmqDtPaS52716-4sN1szydrWAtOpvOOUw6QKGmc1FMoK8Ysyyj00UgVQzWF7jim_FlNW_QunmyTAg-t0tK2dNk3FFw8b6Pvvnjr-NmX527AU7afKoslUn8TqQuoM2vp8oulkVJAPCAPqBmd0qe3O8StNnrTbIFkGGXSUZLmQCMaWvpnvM6emZRaznBjgenV4kSOwJkfw3fnhELkScfi42tMon8FhXgEcoxJFy8sH_93X-UJU0J_Bx0ZS4h7qZXsWLtbeUr0fVn-SBEZGxrGk-sOnd1bLP_2Jhln5lGmmqbWbksTykDLmV2PTf-9prtUl4vU0rEUWwSXL316XgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y86J4glYhbAUQB8yBS2RsstAyUo1LGvuKM4-lYOf-JZ-P9rb_MBo8SrZ_Tuwz4qrySRgle1Tvwu7pfaljoGAaS6SAMkSBy-mpv3PZ2rOBezUuZ5t4P6vxUbL3rbjshshCt8BUKg-XLL5wi4hoWNp2grbSA5wvJ72kvMGM_lf-nAzw8BtJ3rdCZtQiPtFX8BpbLuzvmbdHuz5eBtfVOcLt0uGNvhavZU_4Yn9GLL2l4_2rXJQfgq6FZrOdtJUWkT4VtB6akDkng_J7PHKZ7Iap3M3aCRXugTJJDhe7bGI8mkpVRjjdfHaAR2eMGD8ycmnpIlwV7eiqLC73_sTAELLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mq8wn4EK-xEied_5f0NRHtgMC7hYVVAy2q8wqSzFe4WSnW9IA_tnZP58bNMcrYFlQPh-uw41OKYrnmMynsIHJD6ExM9sdNSRy4clbDPEc0wRtecCvZTzD-eCkPmvoWqnIVhUsJ0pG29OJ-5TIJKjHYqw3kpUg9a52a4wOGnvz4gLgmS7-lTbdRewQD4quSvNhbLwHWgACtIJbNzbv-QAR-qXS0vxHDX7BHdxBpYoX58os82gSEq2BY8nhH4kE0T1-fy1g-kl9sk1KmilI7LwM98swD1BYrCGuDcKb-A3QkwvzOfBLDvAp7qcDqdE4IHJHAA1rtinIQd-HowEY4nRmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
یا مهدی، نامت شده حرزِ وطنمان؛ به عهدت می‌مانیم، برای ایرانمان
🇮🇷
▫️
مراسم جشن تجدید بیعت با امام زمان(عج) با حضور عاشقان ولایت
@Heyate_gharar</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/683451" target="_blank">📅 21:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683450">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
یمن: تحریم‌های آمریکا علیه حزب‌الله مشارکت در جنایات اسرائیل است
🔹
وزارت خارجه یمن اظهار داشت آمریکا در تقسیم کاری آشکار علیه مهم‌ترین مؤلفه لبنانی یعنی حزب‌الله تحریم‌هایی اعمال کرد و این حمایت آشکار از دشمن اسرائیلی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/683450" target="_blank">📅 21:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683449">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
پزشکیان: اختلاف‌نظرها هست، اما پای وطن که می‌رسد همه کنار هم هستیم  رئیس جمهور در  مراسم گرامیداشت روز پزشک:
🔹
دشمنان تصور می‌کردند اگر حمله کنند و در یکی دو روز بزرگان ما را به شهادت برسانند، می‌توانند کشور را قطعه‌قطعه کرده و از هم بپاشند.
🔹
اما هرچه زمان…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/683449" target="_blank">📅 21:36 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683448">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d124afbd.mp4?token=dKqxk8ca9wDY_uoMpGALXWVS9vIt_JgNvKufRYnOB7x45JRa5oeQzrSAeGdbfc1aMY3nplcuepARucbiseri77ploKiLYTAHZJn_C_hR2aYPry3e6gjBSCCNVn_tLya3v-k1gI8DFPRP3hva0GJuhoYl6kA0d9QvIx6SrIb1SA7NVHQiACsnMDziIk5FwQKqdlPR-XUEMie8P9vA73xknTsunJzSqhc-W6qPy4ShAPn6GRgPLL8d5MwPqYwSlurS2vHwfAAF55OlYVDOhNoABur1cbwwYomp86w0zicuAEgmZ2UvNrOfaGof5iMkby6NKBFpFeA3fmLxnZ3DgmQ0oVeECQjEgyQUEkQQoIWqW8p_nxwnVdhE914F1r5kAMAbdJ0oxL7p66dCe3PzkZf8zuhqhlQH2oJ6rqsiEL8Hifnu6SHi9WJKCaiD8hY6f7MOCvporDV6jcp6fPXukrV3GcWTLf3Fil0RKFUEo5s6Nn24cbyVlXg0zAhOlsbudAcLlAvVPF56JUpJFbHHfgKV3TnNgenLbJt53hnaUqG_o9RB33JT7TZwrf7l5Y5p2EBpntKgvIO5VK7oeG2vturY3U2c1flijiL1YZzk-rF53O34vJ_Awr92pBTmiB_ibilNtPsoIqu0IZbWwN6GtUQzJj2XYkAcYQBdcSBguELly5c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d124afbd.mp4?token=dKqxk8ca9wDY_uoMpGALXWVS9vIt_JgNvKufRYnOB7x45JRa5oeQzrSAeGdbfc1aMY3nplcuepARucbiseri77ploKiLYTAHZJn_C_hR2aYPry3e6gjBSCCNVn_tLya3v-k1gI8DFPRP3hva0GJuhoYl6kA0d9QvIx6SrIb1SA7NVHQiACsnMDziIk5FwQKqdlPR-XUEMie8P9vA73xknTsunJzSqhc-W6qPy4ShAPn6GRgPLL8d5MwPqYwSlurS2vHwfAAF55OlYVDOhNoABur1cbwwYomp86w0zicuAEgmZ2UvNrOfaGof5iMkby6NKBFpFeA3fmLxnZ3DgmQ0oVeECQjEgyQUEkQQoIWqW8p_nxwnVdhE914F1r5kAMAbdJ0oxL7p66dCe3PzkZf8zuhqhlQH2oJ6rqsiEL8Hifnu6SHi9WJKCaiD8hY6f7MOCvporDV6jcp6fPXukrV3GcWTLf3Fil0RKFUEo5s6Nn24cbyVlXg0zAhOlsbudAcLlAvVPF56JUpJFbHHfgKV3TnNgenLbJt53hnaUqG_o9RB33JT7TZwrf7l5Y5p2EBpntKgvIO5VK7oeG2vturY3U2c1flijiL1YZzk-rF53O34vJ_Awr92pBTmiB_ibilNtPsoIqu0IZbWwN6GtUQzJj2XYkAcYQBdcSBguELly5c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
شعرخوانیِ احمد بابایی؛ در جشن تجدید بیعت با امام زمان (عج) از «قرار» برای صاحبِ قرار…
@Heyate_gharar</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/683448" target="_blank">📅 21:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683447">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تمدید مهلت ثبت‌نام دانشگاه امام صادق (ع) تا ۶ شهریور
برای نخستین‌بار، کدرشته‌های دانشگاه امام صادق (ع) در فرم انتخاب رشته آزمون سراسری قرار گرفته است؛ اما درج کدرشته به‌تنهایی کافی نیست و داوطلبان باید ثبت‌نام اختصاصی خود را نیز در سامانه جذب دانشگاه تکمیل کنند.
🔹
مهلت ثبت‌نام تا ۶ شهریور تمدید شده است.
🔹
حتی داوطلبانی که هنگام ثبت‌نام کنکور گزینه علاقه‌مندی به دانشگاه امام صادق (ع) را انتخاب نکرده‌اند، می‌توانند ثبت‌نام کنند.
🔹
پذیرش بر اساس رتبه کنکور، سوابق تحصیلی و مصاحبه انجام می‌شود.
🔹
داوطلبان گروه‌های انسانی، ریاضی و تجربی امکان ثبت‌نام دارند.
🔹
تحصیل، خوابگاه و امکانات رفاهی برای دانشجویان رایگان است.
ثبت‌نام و تکمیل اطلاعات:
https://gzn1.isu.ac.ir/landing/info
ارزیابی و دعوت به مصاحبه به‌ترتیب تکمیل پرونده‌ها انجام می‌شود — هرچه زودتر ثبت‌نام کنید، زودتر در نوبت قرار می‌گیرید.
#انتخاب_رشته
#کنکور_۱۴۰۵
#دانشگاه_امام_صادق
#ثبت_نام
#ارشد_پیوسته</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/683447" target="_blank">📅 21:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683446">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e705d04a6.mp4?token=ghMyLn8VaWFYCIk9QhM0kOFDIXHs_AZ-wxTpBGgtRo6KCg-FK0v3XrsGCQoCuQG_bVZz6W9VUaAq90CucBZGnUlMCG8UV2u7yS6KMi1O4a8z81Ureg4zJ4kpek7BVTI75aKOX8w7amU-mdXuC1KKsX6e37Q97u_0mqjBuo031nTT0q4C2zvQo1ca0s3_u0z1p-MbCoA48BZXZL4Lu4qKFSknKpi8M2936jX67NO7ULCJU1a2QJ5jSt_DT04u-dr8fQkomU4SIm5aDdONANgPu2j0keMSZ3-AVa4aFFwvUIZMsJzRsWRokShFyC9RHCmpGvASbR-HjyDfO4443VYEoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e705d04a6.mp4?token=ghMyLn8VaWFYCIk9QhM0kOFDIXHs_AZ-wxTpBGgtRo6KCg-FK0v3XrsGCQoCuQG_bVZz6W9VUaAq90CucBZGnUlMCG8UV2u7yS6KMi1O4a8z81Ureg4zJ4kpek7BVTI75aKOX8w7amU-mdXuC1KKsX6e37Q97u_0mqjBuo031nTT0q4C2zvQo1ca0s3_u0z1p-MbCoA48BZXZL4Lu4qKFSknKpi8M2936jX67NO7ULCJU1a2QJ5jSt_DT04u-dr8fQkomU4SIm5aDdONANgPu2j0keMSZ3-AVa4aFFwvUIZMsJzRsWRokShFyC9RHCmpGvASbR-HjyDfO4443VYEoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: اختلاف‌نظرها هست، اما پای وطن که می‌رسد همه کنار هم هستیم
رئیس جمهور در  مراسم گرامیداشت روز پزشک:
🔹
دشمنان تصور می‌کردند اگر حمله کنند و در یکی دو روز بزرگان ما را به شهادت برسانند، می‌توانند کشور را قطعه‌قطعه کرده و از هم بپاشند.
🔹
اما هرچه زمان گذشت، برایشان ثابت شد ملتی که به آب و خاک خود پایبند است، به این راحتی زمین‌گیر نمی‌شود و تسلیم نخواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/683446" target="_blank">📅 21:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683445">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Stak_Ju4503Yb7c5Q3AQ1e0MeMBkmWzdo6TNf7ym-kLaD4oGIwS2UBG5Os35MC7vRQmnRAeOYMfs4NSwAN1WpcLVTGR5YuHtXBjMUaQUabqDY4EMer5lyuOiQEW0VJlMvnCY-93xX4QLjKLUn0zf_r4dsnRsh2V6yJYSpskPCbVSQF0MMi4P2UakLVuC5Ee5lfaNE1qWI6Wb9ZzfyCq_Z22qf2qQ6LH728Wz8lScahvyyPgowv9Ye1BdrhvTvVJuavZn2NtEFpBUrx2ojnyDsetCIP1J1wpGaUPnM9hbP9oEC7Z72Uy54Gu5NWzc_hAQsJhB5ywC2hKyUNf6cgtZfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نشست سران قوا با محوریت معیشت و تحولات منطقه برگزار شد
🔹
نشست سران سه قوه به میزبانی رئیس‌جمهور و با حضور رؤسای مجلس و قوه قضائیه برگزار شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/683445" target="_blank">📅 21:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683444">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
سیدعلی خامنه‌ای، پس از تو هر خبری جز قصاص بی معناست
به خصم، زندگی خوش حرام می‌خواهیم
علی‌اصول، فقط انتقام می‌خواهیم
🔹
شعرخوانی حماسی احمد بابایی، شاعر آیینی در اجتماع بزرگ بیعت مردم مشهد با امام زمان (عج)
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/683444" target="_blank">📅 21:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683443">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
الجزیره: در ایران بیش از ۹۰۰۰ شرکت در تولید سلاح نقش دارند
ادعای الجزیره:
🔹
ایران در حال بررسی چگونگی واکنش به اجرای برنامه‌های اقتصادی آمریکا است. مقامات نظامی گفته‌اند که بیش از ۹۳۰۰ شرکت در ایران در تولید سلاح نقش دارند که به این معنی است که حملات آمریکا و اسرائیل قادر به نابودی این بخش نخواهد بود.
🔹
تولید برخی از «محصولات راهبردی و اولویت‌دار» در ایران از زمان آغاز جنگ بیش از سه برابر شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/683443" target="_blank">📅 21:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683442">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ابهام در پرونده کشف جمجمه ۴۱ آهو در چاهی در شاهین‌شهر
فرمانده یگان حفاظت محیط‌زیست استان اصفهان:
🔹
شواهد اولیۀ ماجرای کشف ۴۱ جمجمۀ آهو حاکی از شکار غیرمجاز است؛ با این حال، تعیین دقیق تعداد تلفات و بازۀ زمانی دقیق این شکارها، نیازمند بررسی‌های کارشناسی توسط متخصصین حیات‌وحش است.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/683442" target="_blank">📅 21:24 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683441">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ناشران و کتابفروشان، وام کم‌بهره می‌گیرند
شهاب دارابیان، مدیر روابط عمومی معاونت فرهنگی وزارت ارشاد در
#گفتگو
با خبرفوری:
🔹
ثبت‌نام تسهیلات کم‌بهره ناشران غیردولتی و کتابفروشان سراسر کشور از شنبه ۳۱ مردادماه آغاز می‌شود.
🔹
این تسهیلات پس از بررسی کارگروه تخصصی و در چهار سطح، از ۲۰۰ میلیون تا یک میلیارد و ۵۰۰ میلیون تومان، ارائه می‌شود.
🔹
ناشران متقاضی درصورت داشتن پروانه نشر معتبر و قانونی، فعالیت مستمر و اصولی در سه سال اخیر،تولید و انتشار کتاب حداقل ۱۰ عنوان کتاب بزرگسال یا ۲۰ عنوان کتاب کودک و نوجوان در هرسال، از جمله شرایط دریافت این وام می‌باشد.
🔹
همچنین کتابفروشان سراسر کشور در صورت داشتن سه سال سابقه فعالیت مستمر فروش کتاب در واحد دارای مجوز، فعال بودن کد بیمه و پرونده مالیاتی و همچنین تایید صنفی و اجرایی از سوی کارگروه ارزیابی می‌توانند برای دریافت وام اقدام کنند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/683441" target="_blank">📅 21:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683439">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
حرمتش واجب است در دو جهان
هر که در فکر احترام علیست
از یمن تا به شام معلوم است
هر چه دعواست پای نام علیست
🔹
شعرخوانی حماسی احمد بابایی در اجتماع بزرگ بیعت مردم مشهد با امام زمان (عج)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/683439" target="_blank">📅 21:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683429">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d9p-LFTdFnVsPDhIZt2KugjurSbOlOCsgTitvWm5ebx7bwewwIEWMxYY-9KIBtMZt-Kk43A_HUAO6JzmgRPoQsEjEz7e_4sDyDNbPm_vMPaf19Sb-anlLBQrrAwO94snOdatXwRsz8VAkQkAB52u8dYDhA2z0fUCwUrMVgra-JYhwT9-PnFykk158fv213fbufR8LN3OwhT1y_qbpcY_SoZDr5h9nrPF8y_bSg83ANk6_-XLGn8s-PMZ0r6VTX1D8lniG0duPSbN2bSay5YmnVWc_yWljQ-plng29fwl1XNzmGfj-FK0mEdz5mVrUYPXyPfs3aJqKdqKMcaHJzRc4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qd1Bf5nl0KhDZea7xyC2LIUfpeFFPwkzVLW8RFD77QUpK7aA_zvIj48_Mc3XbGmx_r1oTn4vKdqnbvS_SiyYGYUFlcS5Yv4BiDoJTh_RE1u2Otum88HViBj-Lrq89_-LeXPb0qAw2qq63W0iaPMjp2Ft9NZGxEP2puIHGniayG5yabEeo6wUTeBJpfEePTIKppAtCmS864AE91j9MHTx2ZosNi9lj2gG-8hxio21VbWKlbFRwbvLZzRtmn81ISF7VHiEuoq82QAXYoirjnK6fX7tS_tEz7VBa6tV8INOg-IeVUY-SvL968PxgfFEL_pJyTZG7Wzth43mCJXYfQ3P_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l1OQ3YVXTkeFi8HAcBKtioBh-BxuhlZiLTzOI-InryUdrRnI-ijH1KHeB0DZr9pz3TVXLWXsx9xVnATNh-cKWY95ee4aJtkNzCD-ALDU85BTeaAMBr1CHJ40oGvrqsLNdVKUp7_k62nekWoFXoQXRK27IQh8KcfGlQTLX2DWDCVo3Fn6roE2Wk1Gw_wF_fi-POiW0gO304njKjRYu5OuMHWDU6iQY9RbKepxYBY2UJjDGGZqFCBA9cqupqYElwGHk0Df1YbmAzY3OAqXQ-BnixZXdUglHnNfXzvCKyxD4VynOaVT4X96_pOpIEoI4XmwsHJrxiRrvclvYL9MdhwGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jh1ovXk8Y5zG20bPhxRjglg-G4-vQMpVdtcpqTpgyarKV2uOlDCZh8KYMvn12PH1U_F7uPLqlM8K1FmZVfHl_NOzey4ER95yCucvqrRWyd4UHXfmcdK0LixWwCoH7hheA_whAwqflPPbKZcg9oxKT6xFZWubUOUkyZNgkEAOGjOX8W2qyzK6yh6K8fQE0Pc7xLjgKktSuR_Ri2_nMJcu5X9D3cEiRDeMEuQ8YFO_UtnkNxiWP2VVfaKSI5CQuKclpWYYfi2yks7tTWRoMYLUD56LkD55w7BPgYi6sDI1_vwIxFsYsQ4xsow0ALhE4DGhvquPKH0MJjEj3VPwqpYqPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DW8uREUUrWs5drNyt_BQY0Wo76kVpNo6yURrSTmUgSeyIUosKphgTKeM92ojTbPxw8pb4sbLT4NIOrNAFuo2DRM5eOi1xaWtRN7-5kyURsIlOhK-Po0zc-gS7xwwEGCFFhxiYkMHs-YAedabQ8qTDKl3T15KpjOpamjCavRyz4xu1jmLcepTpQtq0lLXNmve2NYKmdEJBTDA1oREy4AO3MLzVgluaOB1HuLvqTJniokXuSHzFCQnqJTwgMBN6aZfAJ990mUmKN_xgD_m4s2p8L3s3yR4NGfDPXQyEtbm5ZpVZtybuBw39OElTZVNqIQwvlpxgzBS074MgF0dP6IIVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
گزارش تصویری از برگزاری باشکوه تجدید بیعت با امام زمان(هم) به میزبانی هیات قرار
@Heyate_gharar</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/683429" target="_blank">📅 21:16 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683428">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
مرداد، بازارها را بالا کشید
🔹
پنجمین ماه سال با رشد خیره‌کننده ۲۴ درصدی بورس، افزایش ۷ درصدی طلا و افت حدود ۳ درصدی دلار به پایان رسید. در آخرین روز مرداد همه این بازارها افزایشی بودند.
🔹
البته صعود شدید انس جهانی در افزایش قیمت طلای زرد در ایران بی‌تاثیر نبوده است. توجه به فشار تحریمی و محدودیت‌های هرمز، ریسک تداوم فشار بر بازار انرژی بالاست/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/683428" target="_blank">📅 21:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683426">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
نتانیاهو: تا زمانی که من نخست‌وزیر هستم اجازه نمی‌دهم هیچ کشور فلسطینی تحت کنترل ایران تشکیل شود
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/683426" target="_blank">📅 21:11 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683425">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94ec87207f.mp4?token=kz2CUmZVO2WXqOHbfb-BPH35naKvWcJOBosqxmpRObUvHuwqwwQPrHRN-d6xN58swkpW41Jw2-eGpDtoDtdUQZioInO2KvsOPSCYN5_7-cih8-PPJ1tLNdR2_KoYZMR9yolfUma4yghl_ezG2otwG3X7Rq89gNu-6wyiGqb6qfscZ75_o8-FOY4kXG5CTGyVM5SzcX2AIK8EU0shREEwAU8CVLW76S-ibVS0OSebjp5br15Vrn-PRJ9AsIN9FepwJ6KKrjiBtdNvhJ1aMfQkCJskRsIz80jDgAuRRUhDrubDpboKtqZOrHi3shfNsc-fCy5kofnzMm2LdqxxSzu6Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94ec87207f.mp4?token=kz2CUmZVO2WXqOHbfb-BPH35naKvWcJOBosqxmpRObUvHuwqwwQPrHRN-d6xN58swkpW41Jw2-eGpDtoDtdUQZioInO2KvsOPSCYN5_7-cih8-PPJ1tLNdR2_KoYZMR9yolfUma4yghl_ezG2otwG3X7Rq89gNu-6wyiGqb6qfscZ75_o8-FOY4kXG5CTGyVM5SzcX2AIK8EU0shREEwAU8CVLW76S-ibVS0OSebjp5br15Vrn-PRJ9AsIN9FepwJ6KKrjiBtdNvhJ1aMfQkCJskRsIz80jDgAuRRUhDrubDpboKtqZOrHi3shfNsc-fCy5kofnzMm2LdqxxSzu6Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه پخش سرود ملی در اجتماع بزرگ بیعت با امام زمان (عج) که هم‌اکنون در مشهد در حال برگزاری است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/683425" target="_blank">📅 21:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683423">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac30e14d45.mp4?token=Ki4u5nkZ8mH-La3G2ql6xAa79YGT_kVjjoNKNhg0MXSGglmvQNPIpOj4yjoLW9OApml_ObgD6CCZiGDv-fJ54n7kopnkhuuzufkv0WGDuhZPiJRXCU3fFuyNde-_xHp2cosMkesJlRe3zfxg8rrCPNl_ZouNHamrWsxJaWOZe7XHoG9hClvWtpbbEyESrYoXFwQD03hXhEScrON0K0ejLqhjxX3m75OH-vtvEfUtD_gYXwCzujA5fb4cJuQyo4mkSSM8vyqYrGV45zOv-qAUTh8DjVq7ACdsptFWI1wtSN6SiAA9IGrMscKluxVPoscuCRjYGJFECiK6kNKLMKi3yizN0vxaajQ_ZYDWbqadXcZdsTooqcUxW6pMpmcWLOQHD3lq8xlZQ2-lqZEfws1kyOChkfEze75VLm3L9qVWSEOX8G4D1gFAJsWbTDp5j0PS8CxDk96cwZnkivzPcX9WBZSFk-VS7aC8y-UQh1nb7bizK2aD01vOStnglotWwW2CWgWO4_c2I1RZttDFNL0lJotSwp5zNZpC-WwjuU1aLcMQjoQFAJkYWD5z8_CSbLL4o-D_6AYu65yTj_ngdeWQGSXYWzJhDZIvLcR6QdK3mX-Ig9QWhpa5-Ed7FpAOuT3o0JDCX_8VmJr4E-9xJT5M9qZoW37H8GO7Z5nwitYkTtI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac30e14d45.mp4?token=Ki4u5nkZ8mH-La3G2ql6xAa79YGT_kVjjoNKNhg0MXSGglmvQNPIpOj4yjoLW9OApml_ObgD6CCZiGDv-fJ54n7kopnkhuuzufkv0WGDuhZPiJRXCU3fFuyNde-_xHp2cosMkesJlRe3zfxg8rrCPNl_ZouNHamrWsxJaWOZe7XHoG9hClvWtpbbEyESrYoXFwQD03hXhEScrON0K0ejLqhjxX3m75OH-vtvEfUtD_gYXwCzujA5fb4cJuQyo4mkSSM8vyqYrGV45zOv-qAUTh8DjVq7ACdsptFWI1wtSN6SiAA9IGrMscKluxVPoscuCRjYGJFECiK6kNKLMKi3yizN0vxaajQ_ZYDWbqadXcZdsTooqcUxW6pMpmcWLOQHD3lq8xlZQ2-lqZEfws1kyOChkfEze75VLm3L9qVWSEOX8G4D1gFAJsWbTDp5j0PS8CxDk96cwZnkivzPcX9WBZSFk-VS7aC8y-UQh1nb7bizK2aD01vOStnglotWwW2CWgWO4_c2I1RZttDFNL0lJotSwp5zNZpC-WwjuU1aLcMQjoQFAJkYWD5z8_CSbLL4o-D_6AYu65yTj_ngdeWQGSXYWzJhDZIvLcR6QdK3mX-Ig9QWhpa5-Ed7FpAOuT3o0JDCX_8VmJr4E-9xJT5M9qZoW37H8GO7Z5nwitYkTtI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
اى وارث ذوالفقار مولا برگــــــــــــــرد!
◽️
اجرای ویژه موسیقی توسط گروه سرود دختران در مراسم تجدید بیعت با امام زمان(ع)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/683423" target="_blank">📅 21:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683421">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس مرکز امور زنان و خانواده وزارت کشور: قانون مهریه باعث شد زنان مهریه خود را به اجرا بگذارند
پروین داد اندیش، مشاور وزیر و رییس مرکز امور زنان و خانواده وزارت کشور در
#گفتگو
با خبرفوری:
🔹
یکی از بانوان نماینده می‌گفت موبایلم را که باز می‌کنم زنان زیادی هستند که مهریه خود را به اجرا گذاشته‌اند که تا این قانون نیامده است، مهریه خود را بگیرند.
🔹
بنابراین به آقایان گفته‌ام که ما یک جنگ داریم و شما هم دارید یک جنگ خانوادگی راه می‌اندازید.
🔹
در بسیاری از موارد این قوانین از محتوای واقعی شرعی خود که به نفع زنان بوده، خارج شده است.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/683421" target="_blank">📅 21:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683420">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb137f4e5.mp4?token=ii7IcTJ-bWzQzyNQfkvh8D5GVLho9nrX3J1kc0PoBo61oxJupg4s2zOemItzuWLy4Ji9aG_SQQdSjTqKnVafCGW1OCOC7SCMDfd6VWMG6MHp2ACqK8b2sh8WBQaWVS0hUrhoj61ubZQVJ7C1HfupdTG1yl00VimgKNCkkqwYcCUoKoTRNQbk2lUbdZNNy9mvhwlJBQP0ylZDePt0pojRC1OM3O9xEWLcxAkmh-jbQUTp7UdJRoP9heoTVfqD12SSuKsOFLSAz1XoMydorar6xN7c-gAnSGwPLIYAydmiLZpMBXLvKmDEUHYcrlQ8MfuoKucU8epU_yjMm4MLaYM19buShFUBXT8kEwOdfQn-JpIZ0BxEaDo8JI2pXXxHbyHKP6ZWrZbZLzppFtIqhUwZM3trgzncHt__EQTzwBIpIv3JRL-gKg5c9irDhDX7E7RPO9Faybpr8vspa03QOyGoeT9JOrrlWOKlFhwz3nOT_rsEiyYqS14EDlHo4tbrLPul5u_fBHh4A6fsaCORwiFAlaI8sj9sQtJDHWdnloWLS_8wWamyPUCO8fRCP996y5SO2fSdfMX7DxJRsX-Kz_KK5gzbkfnrmdBbrVSmxcDGRLGlS90ftVHLEBHOAZpPs1TpyXtstFRUlybFaaIdR5hJg6EMKqv95GD6BdYTyhsRUGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb137f4e5.mp4?token=ii7IcTJ-bWzQzyNQfkvh8D5GVLho9nrX3J1kc0PoBo61oxJupg4s2zOemItzuWLy4Ji9aG_SQQdSjTqKnVafCGW1OCOC7SCMDfd6VWMG6MHp2ACqK8b2sh8WBQaWVS0hUrhoj61ubZQVJ7C1HfupdTG1yl00VimgKNCkkqwYcCUoKoTRNQbk2lUbdZNNy9mvhwlJBQP0ylZDePt0pojRC1OM3O9xEWLcxAkmh-jbQUTp7UdJRoP9heoTVfqD12SSuKsOFLSAz1XoMydorar6xN7c-gAnSGwPLIYAydmiLZpMBXLvKmDEUHYcrlQ8MfuoKucU8epU_yjMm4MLaYM19buShFUBXT8kEwOdfQn-JpIZ0BxEaDo8JI2pXXxHbyHKP6ZWrZbZLzppFtIqhUwZM3trgzncHt__EQTzwBIpIv3JRL-gKg5c9irDhDX7E7RPO9Faybpr8vspa03QOyGoeT9JOrrlWOKlFhwz3nOT_rsEiyYqS14EDlHo4tbrLPul5u_fBHh4A6fsaCORwiFAlaI8sj9sQtJDHWdnloWLS_8wWamyPUCO8fRCP996y5SO2fSdfMX7DxJRsX-Kz_KK5gzbkfnrmdBbrVSmxcDGRLGlS90ftVHLEBHOAZpPs1TpyXtstFRUlybFaaIdR5hJg6EMKqv95GD6BdYTyhsRUGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
شروع رسمی «مراسم تجدید بیعت با امام زمان (عج) و رهبر معظم انقلاب اسلامی» با اجرای امیرمهدی باقری
@Heyate_gharar</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/683420" target="_blank">📅 21:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683419">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ادامه جنایات اسرائیل در منفجر کردن و تخریب زیرساخت‌های جنوب لبنان
🔹
صهیونیست ها، ساختمانهای دیگری را در اطراف شهرک میس الجبل و منطقه المشاع در اطراف شهرک المنصوری در جنوب لبنان منفجر و ویران کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/683419" target="_blank">📅 20:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683413">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qExBhYiNqHoXTipgCzDorf63pMELK3YGhOiWGjzy3cYS2KzaPS-5ZqDAZMc5X3Euaianmp8rVy74D2rPt8Ogy6wzjle9ktjnj3iU3kAG_dQmifPHzjtQQz7omdhL3g2-B5kYSpczeiGyTg6FNLy_68QVkNYEQM6qvVz_XabZTzZox-2JpDIgtnzx1vw0sH7WO4Q5sGLNjMQNMKCVlHFfyggeXBBhQdP_k618yLH6iJeuQsiDdtH6sGyGaq8cvn-3r788XY0fdguXd5vHLHSR71HWyGp6xvNOsvNCKud9GLzWwigR_HnPulnwqnWEHDK-wh5MkdZU86uB1NlGTShTsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pxevp3SJkt0Dzq7i5eBPYS9eHW003H2gEu7X1YQ6B-dz50Vp7ME6qTB2XGTonCkD7SEWz9itnGnBeVxH4KUSbgp157eFwZ-oIPz3RAvjK-ZGD7qVwlAdqtRw8G_2j4_igWJslEEgY8jCTCwppt_gWSHp1yFbussVH28kXTmbw1GjPGn2QFtHOvxXEAD7ZfrvXddWG70W35SHfAO3_9J-FeTwIekX09OhLIzocEgRpo9AsO5v3vO39ZzHaRvQRDbzSebjH3aSWII6136eDDmkSzO-xJbp6OKKs5Bn3AlLeaW8937T9VUgfAov-5YiFF5iWaCsfR--ZnGPLyCyM8fmfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SNvb8eG40uJc2hsQFiVHQAqE_kl0BOqxAOASaDIute5q0NdafJAgSgGi9KPSSzXOZfd9XVUGBSYFKtteOK_qSfGcp8kWT0atTs8gMBkZOuRkwoznGdxxnZ56tWqXXtRS5SWj9y6X7wW4zb8gQy4rd4u9xkEr63gIeSnJcdJ7rwZYvTsqMw3IMb-80g9Z3uvJ-E_r7gJIrg7bZA4-5Ur5TNLLA20gcTz7pJQY9sUzHxhRmCEQektTazun2l-RwjH8ovWSlsBLwheGma71Fwgy7yRwmX6H0ePUF9g0G4uB4Sb5SiICy0u2RnSWezUUI737FjQZ4ci7sloMkCsFUfdwUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I9tUTto42hmNWa1B4VqMMKPJFH7eafyUsumXzHO0pcvxF28MAo9CXLHsZZaYVDws-T-Zi5JxE3GRRQBT-2UiCiIZ8CSigbh17gkr6QYzBwlsVBPoARksFDdsLaYmlIcy_NTformv0DouJxZOxqbLAimIWIJQVjLFeORsHAvfFIdfqYGvh3DILt0ojRC1ABUfrt_eg1kz2I943ODeJAIgoPc0mU0rq0eeJrEpgr6sjbCfTjNKSY2CNgVqEZ0EYpqNIl8vIfp_W_BPa2JRJvQ0KSBK7lV5vHONboRZBRTV8aq9fzo2ubg7Ap473TCCZgqy1yPL2VE0VLLc7cG0NYp9tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/leq6LjhNpUhfRdmnH1VQXvfXCjj8HWLxuWHUCLDajXTkagoDEHrFENMJHKCGuzxz_GsQHsKO7rpXQkKHx_4v6aauM4Sq3bZGUcUU3M4dzykO7eoD8gh81MyxZDrBpb5TCdgDt0uTZzgHnLlHfMOsc0SZu-o2LeZgk_IjMbtxQRL4wn7IcBcrHyMLFpi0tAAfnX6sG9k4cxq8dosdx4WxDKshQDjQMco5urE0sLwhFnACzGyKSrTDk5jboD2YfqUWw9msbjcP1QUt7MlgyLtRwUpSHf41DN9AtJKmUDOU-ObtT7BadGlPtma_fJqNkTRMezT4McTA7Kaxvgs0rTDONw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BdnvXVo8NSnqZVPy8pFlm_WhKARv6CNoPrk7z6AZzgR5La_DYAII7Np9FgZXRMEQ6PBL9blOSSoEop30Lshi2qHzqTAsE8NwOd2StasnwKJo9dE3leZRwDzCeCh5GVSuSYyuXwZmsDF3tHZwfjwlnjxQMz9PeWCdkEgqGhBJdEvPdDBJDJhMXa5SwUMjW11L5ajFjUOF-47PR83_KuJSE30ln_AC_5iLR-2MfHWFsFDS-ZQovylKjtvHkencjcQrwQvYrIZpZ3GLorl_z0aQ3nlo1IIvVgHqeu3szw3pjJYCsU6b4AZE-YwHWcRXVG94Dfo7ui0KSqJsX5qbgxqPew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هم‌اکنون اجتماع بیعت با امام زمان(عج) در میدان شهدای مشهد
@Heyate_gharar</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/683413" target="_blank">📅 20:57 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683412">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f75df1eb4.mp4?token=rIcpJO_WvDvhVKvD6tiSychm0W8QtdY9P09CToR31_NGtiXikNHuBJNcbnU5eCpNul_KX1JONPheFBRgcMR_Diz_XAWQCpVlaaTUyqUbAEUeGkcBCgv5gj8xTmgkDrIaasDossSsRhQoi4Njrql8l7DLyszM1ASHgcdxFWA0EkrsuiRmEgwpgGQGyFzIl2XZH2qkkViaHVDuWayy0G5rGiJmoTmsx_UWs2jc8VDxZKfg4o6go3o9jpBXzSOP9MHHTl-D0H4zJ1eN3YIDtgY8oXQ_rqyMrKn4pECMwm1inr9AHe_M-oB18BkPEvhx8Zxc-S3_sfPC3KdN3b-3rE1G8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f75df1eb4.mp4?token=rIcpJO_WvDvhVKvD6tiSychm0W8QtdY9P09CToR31_NGtiXikNHuBJNcbnU5eCpNul_KX1JONPheFBRgcMR_Diz_XAWQCpVlaaTUyqUbAEUeGkcBCgv5gj8xTmgkDrIaasDossSsRhQoi4Njrql8l7DLyszM1ASHgcdxFWA0EkrsuiRmEgwpgGQGyFzIl2XZH2qkkViaHVDuWayy0G5rGiJmoTmsx_UWs2jc8VDxZKfg4o6go3o9jpBXzSOP9MHHTl-D0H4zJ1eN3YIDtgY8oXQ_rqyMrKn4pECMwm1inr9AHe_M-oB18BkPEvhx8Zxc-S3_sfPC3KdN3b-3rE1G8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیگر لازم نیست برای قطع برق وسایل، هر بار دوشاخه را از پریز بکشید
🔹
پریزها و چندراهی‌های هوشمند امکان قطع و وصل برق دستگاه‌ها را با یک دکمه یا به‌صورت خودکار فراهم می‌کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/683412" target="_blank">📅 20:52 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683411">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKz00XXOUINoSBdKXypAIhXgM_zRViGzg8qexLkP5AlqKyrqQZxAN1PbJME9OG8oLAWhCqf_cnWbTye7k_RuUFAUkoVQOHg3jcoRYBpwJmajzAsCeLPSbWaxHTx-q-MdOPRYEnE_nIwMWeOdC1Rw4HYXMm0VDKHlzdXA2Jivm84rwiOkKNMfOcwkGBHV5hfGfYZ2xA9hn-NBuTiBsqtO4JgN0by-njK5LWiZRHJ5f-nzg_TQUGRVxzROWrtcESFXkhEREDBbg-sKgmiEHyKrNMgMApr7bMiBL612BDIeMwGpS02zk0FSQdqVOEWEzsbqgGz91r6FdSBZOYzrZ7Dhbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معشوقه افشا شده ترامپ، خبر اول شبکه‌های اجتماعی آمریکا/ چرا ناتالی هارپ برای ما ایرانی‌ها باید بسیار مهم باشد؟
🔹
ناتالی هارپ، دستیار اجرایی ۳۴ ساله دونالد ترامپ، این روزها به یکی از داغ‌ترین سوژه‌های شبکه‌های اجتماعی تبدیل شده است.   در خبرفوری بخوانید و…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/683411" target="_blank">📅 20:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683410">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
آسوشیتدپرس: مصر در تلاش برای احیای مذاکرات ایران و آمریکا است
ادعای آسوشیتدپرس:
🔹
وزارت امور خارجه مصر اعلام کرد که مقامات ارشد دیپلماتیک مصر و ایران درباره تلاش‌ها برای بازگرداندن تهران و واشنگتن به میز مذاکره به منظور حل و فصل جنگ، گفت‌وگو کرده‌اند.
🔹
گویا عراقچی، وزیر خارجه مصر را در جریان «دیدگاه ایران درباره تحولات جاری، روند مذاکرات و چالش‌های پیش رو» قرار داد، اما جزئیات بیشتری ارائه نشد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/683410" target="_blank">📅 20:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683409">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bi1ne7Dur_v6FXTih1ufcgjaIIeiPEprslacV10kqzLceY3L3sPOCYZTv11MUHBxS73_zjR4ZGnUJcKVzK2Bgq_mLIFoEboWQZ6rK0DBG1894P283wS-10fzKkVAmLnpcizCPQ7idLkNin__WDuqaeNikzvq4nI76JVmfc441idjDrVJlV9Ktk6a6dm_TdxThc44IaoPAIfh2Et8LDNNXa5SwDp2DE3rVLIuzsTblYDJnRmYwV_HRDAkBMO7I8l53yqxIN0LOVAG-osJVTCUAspyqtvfex6nWb9JgVnHiuFoDFO9QYh0dIx9NHK2Zq2tbPQlb4xXFj9OLJKrc6DQvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند کاهش ذخایر راهبردی نفت آمریکا
🔹
این نمودار، نشان‌دهنده ذخایر راهبردی نفت آمریکا (SPR) برای مدیریت بحران‌ها است.
🔹
کاهش این ذخایر واکنش در برابر شوک‌های نفتی را با اخلال مواجه می‌کند.
🔹
این افت ذخایر راهبردی، نگرانی‌ها درباره امنیت انرژی و آمادگی بازار جهانی نفت را افزایش داده است.
@amarfact</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/683409" target="_blank">📅 20:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683404">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tmezccDhJX3BBWnUVWRFFjXungteixPs1cYKnEyLBupNj3NUyngOtuaV5gPztLUGhCAT3wONLmWl_f9_oSL1e9a_SSX5EXq1q8Jk0uc5X5-UTY2QVIjP55x34r3ONxAiqTDyCdJh-1tEvLI5BbzZFvd1no7QFrHlTKPtFyM1OxDTE94-f3bY3XRHXpLNerp6gyTOaZ9nJAL7va55hP5_iwnrlib7KUQayxo7PYCvbEqnJZ_rSnvyN0nqxOxKA6H1J1eNA-QxZ5QzkebQUz6xoKoAc38vxi7VI53AvegHbYsa1e1Ym3eN3olphYDwzQnOzwvMrGeKiAxd83bTJLQ5lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ixR87TQ-V69QlYruLOCerTD0x7SVV7F6n2FRI1B0yyxUgSaLoCl5fTcBm0KPgCU6AuAR5X57fZOhU_Gy4PRI9bkIVTHtNBlouxhPifRbX8Vu_anGC2qtmfmM4f8YLH8_0Bigg1cEVqCK1AKRTswe66EQXi5Jgts6ZpGYUY3Dw1q15vmL2sI6g7iyvU1w4azJMRlHV_Rnhmh_DWDatjRDzh4fw_13AX_PvA4GWIek5heipIywH9KqNLyMq7LNaVyuH_EmnWGnbb4Sh2aLPn2q2j7PIs9dbTJ6jBi2uAPEfIAhHA1yURY7QIzupOhNTy9GGAZjEHekKA4BK21TDFgVAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7880d59626.mp4?token=jTx9bd3-VcVmJy6hxAPQf2mRU-_9e-BfeWpBQR1oLzRQx2trGvBNKQ9HT6AUrN21Tejs1FONcuTnGHFzglVDBV_rE0FWX_c8J6ZAgmyow1zRVNIbF8yMbT2sXDrXxTnYjMEUEorjwnDfp0sZyCeiRqDusHuz-kqKFoneDpRRjJ2MshCt0h6PWCXyrQsHt8HL7oOJn29BjaF81IK91Q0E8CqmTGXJpADrEc1IvHDBuQ5dtwLh44rN9oLq_KFyZr1yIsKbmpLP5VNl51JC4gfDQMXL45x1VvPsnSGyV7Kau7wglcVRVSzszXYhYo1s54coNiu1b8QY6_mdpgAJXLs0nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7880d59626.mp4?token=jTx9bd3-VcVmJy6hxAPQf2mRU-_9e-BfeWpBQR1oLzRQx2trGvBNKQ9HT6AUrN21Tejs1FONcuTnGHFzglVDBV_rE0FWX_c8J6ZAgmyow1zRVNIbF8yMbT2sXDrXxTnYjMEUEorjwnDfp0sZyCeiRqDusHuz-kqKFoneDpRRjJ2MshCt0h6PWCXyrQsHt8HL7oOJn29BjaF81IK91Q0E8CqmTGXJpADrEc1IvHDBuQ5dtwLh44rN9oLq_KFyZr1yIsKbmpLP5VNl51JC4gfDQMXL45x1VvPsnSGyV7Kau7wglcVRVSzszXYhYo1s54coNiu1b8QY6_mdpgAJXLs0nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطوری با حقوق ۳۰ میلیون پس‌انداز کنیم؟ #جیب_من #چرخ_زندگی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/683404" target="_blank">📅 20:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683402">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsxC1qHy3tSR1d-Ht7HfJ2dZNz4_kLpxMwxl0OtcphLj6tsQMCSJR11r8GopIgRbkivmfQ4ZvYF2ExNKamlHGuDGOJkBUl65cPucaJKcAbdhsBsQgaqJJ25Z3cDHyxmn0rmbHBaH6Zms-LUOvtZr4TusGk2Kw2N9dSZFt3Hol8ZjMKGiV4722pJsd1YV41c9d5x25JeRmeLZgKCvJeFg9NqS4RHk6aiQi9oKqI1xzREqp6kTxWC1Kq-MKWEclmcIf-Lt6cO0G9IVfFb7HXCY8-I1Yq51YM9W9RKfgRhN2JkWR1nDp-xO76W9LJYYAUZucgvQGAuEiIEVZ1Vlb1lZbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویرانی اقتصاد قطر درپی جنگ علیه ایران
فایننشال تایمز:
🔹
درپی جنگ ایران بودجه دولتی قطر ۳۰ درصد کاهش یافته است.
🔹
بسته‌شدن تنگه هرمز نیز صادرات این کشور را فلج کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/683402" target="_blank">📅 20:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683398">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9139b50d1b.mp4?token=qH2lwqlWFNMoQSe_ypF7MamWpAyzKve_nYVkAmQUlOLLxyWLyX8lYD6NCYPKQvA4ba5zw4_OL1Z1ETw_3cPv2SlBVYFy-kALb5c3h7SJjgztxAOJo5Obb7S4_l9hGaSKHROMuOKJXOpojR1KRZPiNTRexK6ogStoMvMvUqBJ7I_V34cQPrc-IDNBEAaiFAWDqiWyCNmzS9W4_YvImO6LVglBqETctdhCysJ-OxOyRuRCsPMiOb9S0oXh7379pkYA5xh_alXuQbuIxPO5B6Z7SU0I0gffy8I9h9RCYMyMzB4VCgSlvMAV9EiFViVyuUPeG7tBOQUejuDNB0LmlBj7EpLwUIjBbAz8bJR1BVRyfrxtLsyy1tMB6q2ZcXN3haQC71OVRuccIcB-nH91qBRiBN4Xu5tNKE7wUybGYa8Y9dpW_jz4eoFSZRhZN1jCcZFLERNSax9XNiTGJwqBNC19kmiZyNArfKA8atvE9eG_6rtgae3B_fXPutIFN-whEzhDytVVOPDvG27FcHcR7JyDvCayrAKVHRQgHoptX8vYvcaauQvZNzIMx2ml4Fhu3arXw2mBXLZD5uTOx_6ZfRYI1a0SPvt4f7gZTM_PtucFmRb-bNokJu1niE1jfSp9u_AGHnOpQiCVoZmlvLqnt9tJQow22_pA8Qw-XEqtvAT5PGo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9139b50d1b.mp4?token=qH2lwqlWFNMoQSe_ypF7MamWpAyzKve_nYVkAmQUlOLLxyWLyX8lYD6NCYPKQvA4ba5zw4_OL1Z1ETw_3cPv2SlBVYFy-kALb5c3h7SJjgztxAOJo5Obb7S4_l9hGaSKHROMuOKJXOpojR1KRZPiNTRexK6ogStoMvMvUqBJ7I_V34cQPrc-IDNBEAaiFAWDqiWyCNmzS9W4_YvImO6LVglBqETctdhCysJ-OxOyRuRCsPMiOb9S0oXh7379pkYA5xh_alXuQbuIxPO5B6Z7SU0I0gffy8I9h9RCYMyMzB4VCgSlvMAV9EiFViVyuUPeG7tBOQUejuDNB0LmlBj7EpLwUIjBbAz8bJR1BVRyfrxtLsyy1tMB6q2ZcXN3haQC71OVRuccIcB-nH91qBRiBN4Xu5tNKE7wUybGYa8Y9dpW_jz4eoFSZRhZN1jCcZFLERNSax9XNiTGJwqBNC19kmiZyNArfKA8atvE9eG_6rtgae3B_fXPutIFN-whEzhDytVVOPDvG27FcHcR7JyDvCayrAKVHRQgHoptX8vYvcaauQvZNzIMx2ml4Fhu3arXw2mBXLZD5uTOx_6ZfRYI1a0SPvt4f7gZTM_PtucFmRb-bNokJu1niE1jfSp9u_AGHnOpQiCVoZmlvLqnt9tJQow22_pA8Qw-XEqtvAT5PGo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با قابلیت جدید هوش مصنوعی می‌توان از یک تصویر یا توضیحِ متنی، یک محیطِ سه‌بعدیِ قابل‌کاوش بسازه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/683398" target="_blank">📅 20:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683388">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PvIXIqzbyTC9lrfW3KrLvEyS7aY9W6tvAgZCzshWVK8-Sstma_hwL5n_UqiSnPDtWVpQ70xRIqsF2IpsraLckqA3MGMUFf5T73buXJZH9oT-M7cllqdGl2J-epPAcs3U4KEQXI_Wbg1tGlDniemUTCZyMI0Wn_To3779uCUy6R7myEaaZcXoaihBGSvWs0HDYOdLsPilsrDaGJPE30gbnS-cVQzTp4v0Co6cMQG9fWmRucQH-PXjDywPN6B6rTFFsJRrM3PAycPRBTZA0KQFr6ajYvE1sp2_-7QGEAw0nR4sDvDHBe1abe-9ngrABF3G8w2WadgQIMsPPNledOkrGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTc9ENveGVy0uCf7OJcsYVHdcWy1Jx1P29aiozYG8TgMk6kCp02Zg_HtUTC1L29DbTZF62Cnkl7cY9Dj9dc4O8ZWNQ7tYV6pJgWWIJc7QohYlJXvjpO40Pd9FNrul-8Non0OV0KnftJQCNW1xrw3D0xwWx5_PiyPpeWc3G6ynu0nnW_HNJbwGWPwfK4rxTqbTwV5h-HcmCH7DgyyFTqY23tGQ0Uzkr_L4OcIrYbZVTeAFsXc4EPRdX_DdQCwDx-jy6iekqV1hrnfPuTlLvxnRy7bv9owyGpgjJMs9OlsiS5eYyFZWimUhv9Ur1s_nER7Egj1FbZD1-_UOoFj94oCFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bb2RZRSW0L034IXCMm1Mkn_fGSTWvhJFcV881AQYMZiLIIjYDWEaw8AP6LG9DGjihvt1l2XsoMM0gWXCuc-lkyruZZxNQ3jDMCWWTWOGosDJQAVHY9K48QGMhOIbDeMfhgtur4nBLjwWkxTYJ0gDBTsodUJ8jGdiajcCrO8mmb3enbtekre9OAiDd62fYE2hTNTw11YZ8bIHDJgTgyM7BuowbE0kByt9OkOZ-R1iUM88ZPARU6CEXNGoWzi9YQlK2PSLoC9U-tOhba17aJqPYf0tMmvlrks34Wsq7MvWoB5Wr429Hb25CKb_bzhOO8G8v-eWQDecSxAEiNVNRdYukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/teiFxsHxZ-8cRWKnrFYhD2HmPxRV7vEzxSls-cuorxp1Lu3KYaKYfoGAPRSiJJWBLuM66tH-6j4Np6XDIwIbMbe4IiPFNjTOVE64n6E2dJ4uIPlgh6lRXwZWSMgclbq18eJ8SH6senHwTRwZQugRuaYGEvpJeH3le5pgGp0yy1RsAKtBJjja_hFXXu8tBEBOfphmkNvvQEdzs3qhxJBVPzjSn_7hhe0gTlwJjNen9yqwytAeGMMCTXnjgYUCEHnhPUf85ykEuQvppFS9b-R7i662Iybh2xM09T-g0CgBWhOsMd_TL1gcMPsQrNJCYJmLy3YlDAWasTmb7O0sbvfjgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pwVcYLpnAWy4_UcqS_kdZ1a1IUTtg85axELhNSmR1D68YU8CF1mvH8LiyH902a6z2AlIdN-0QNbPgyAfiKZvuhqZNUeEHxa95JC-xVrU69GIpsYN34HMR5X3QB6hcah9T1PuvrHpmVFxpgY3hH1_HJ2y3mfIRPRfYvEk3fxk5jy-hmnBq4Bp_du63cpysrCwo4w94pY1sy_NuTbLhtkpvoEwVSFG0EBrJGSkZPaUHGaOeY41Xw6wldkoe_SS-SLLThyy4spp4M91BsoGUyO-2CeQ1f17aUuV8NNBJbYuheb-rEAq8n8hkQ5M-dpYyYBZWkzdGk-LThF2gx_M--7oKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KlkfBAkR81YsyJsTcxvNyw2dCA279wzDfPD4EX-YB8WnZaJFyxYmyqpixNfpty_e3UVg86TEy33JGIfkL2OyMHPixBZpG7lUhlK94lXe-Hikr7bROfg2dzpRJxrHQU6EPyyV8rD5eS5h2omjzNEsfsleYAtB--VSZOJGasQUPBApJfFBpr9KtC1ble6NhgUVEqrYLE3c6rT5T9oxp9cFBvKc2hY5MJYQilgG7dOdvmnp3lmK8reBQQlNQMUChA5p-F2l_omKVjCHNWb60w0ocQUMARJTsKcFT-uSgZmcn0UQ-lygJYx1mUjJmijegvB7A3_iPJhiEeieZX7ZZchDiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SM_oWxYSBnFMc63blyxkxZXu4aQ069R0z6cEOp_atCvajptIVNTxbXHHZCw23CBGj8I8lGq6gEW60xKNlgOGPw93nYFqRzrC99w9CoY46zue6-6COfda4cJjxYT2Zf2VgowYKcRvfF--YK0PErQuy0hfi4qCAEFe9uuEPvhclqcBMdmINsiWvH1qlwZUyHgR5Ho5D9NeUaAtqeyZiNA7fuUld9eLB4LwEZM-pS61PMK5bV6INYBKwyMlxgsGGFADKIWSGw23wTJ8YferYUELprZ5ppONrNm3dmCWq2RkiClvNQw1WU9RchwO4ISI9PY52cEd2ZsrSW_f7ZRabmoKDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VU0XitwIBMUmQAen31omy5T6ayRiG5e5Ci7qNQ-24FdRkLYDId7ndVtCuxxAnDDlJjhpPDUVujiYeVuniKCwVAUirANrblZeY0VZAo5fwbtHvfs1asEeIgXKZLLutf6NBWcAzDucz-R-nBvGoC997Fl-uthdecEAhzz6711pqsonBx9vQ3Z_PJZZoJXhUoguqgoMsT-AGAl_gZ975myc87OIxifJwJGqIk7UXs2MctKSGAf8Xxtc28BeJIKHSAWnMR9OgcObXtbnEXb765oIg8zj3ifU8qEWzkMk1dLqZulEk15_KmdzCabvZyhL5ZqyCG2GLESPxUHMhJSor48eYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OC6EobjJp0ZlGX7ZMl6UgZ2z3C4EsRGNgU5F330msEWwCo5igSZVYMjn636zCLa44D_YCxA44ru3qVsFRJw8lEZSfUOduDZvJ4cv1O2YXhptsJtnNkR8mLhArFkwPInPSY-X8PZ15LR8-cHHzyacTUf04kvgkxl4LcVEQtyKBQZdLWDCixgze1xlOy9Vv10-h1jmJDvCx5L2Dt0iBlwz5wBJA_1mM4MtnAWCGW4jN6yPcVPgw-3bwIwnrJZszLw-7D7xs5ChSkBSyNn82_HfD17FmswLZS1gbKRtCPV66htfL2ONid0PD5_lb7sfS-PtZPFOXmTRBmSQ_2xKU9IHyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sDuFfxjhd97JTEzWE098gDiSNkjHZuaRTXpWupCRduwg5U4N_bw-ChHhRhmQb0HykZvYg8rg2nGTDQ8Dtjrug8US3syKmjt0XNfNLXykluJRgRjlmIP2s-QWCKJhqMgznZtsGMpOxvisAJpcTm5hpIebvPILp8NR4edLcdf6nWmVdtmeiw1aa-E2Ih_z7lEYJFjjJQbea9uncULBLc88a52cg5mV-fyvqHCXSfI1-LgvR88W-zwSR-8szEoctYOFYQBTRNIKhMYRn24tD5JyEJ3X1tJwReaGo2FV8NRuF70Y_sK58IVkx78y3oFh1PsT6UrjgQnTMJxdG52D2YChgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
اگر آن ماه نمونه
رخ خود را بنمونه
همه بت های جهان را
سر جاشون مینشونه
▫️
حال و هوای میدان شهدای مشهد در فاصله نیم ساعت مانده تا آغاز جشن بزرگ بیعت با امام زمان (عج)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/683388" target="_blank">📅 20:18 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683387">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeoxmO-PV-ojMOkQOOB8i09sXXZm0C1qLigRC3EUdmjecN8MmrzD4t2QazaIbPspV63PW5q58Vl2Mp5nd7TTLA1JwIoel0bQ47K6smVF-YM1ea4ugCEusGR7m5jco5GXUBI-lhzOaJUDVSbVDNPS0WxXtpPo8vRnVJUmFYRT4vQlBcphlG-qWrbx1yCkk0N1LH43GyIGfNDrTzNr2IWfI6TWQ3XtFQUV5xAcgpBcZBVxpOLoiCWKdd4OYBBMUala6HUABu4eh8pYBoQfrxJoO_4X1xhUPABdaCCOEtzexCLOAanHqg69RjvA_J73ht2kH0iP90YDsqTA6nt_gV8LMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک سری ترفند که کاش زودتر می‌فهمیدیم #ترفند_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/683387" target="_blank">📅 20:16 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683386">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4370e0903f.mp4?token=gpwZg5fc49-ucLWMZyYiC-KlxMnQoO1Z_Pkups6NkHYoTPvRYYva349-6hGSliYjaqAhoiejIW06V932ahXGEX8EasqQQTxk_Kk2INhpXlmM08a4NiFE8BjxSbW-vm1BBdMFXlD5g6yZScIu2vYLgLmSrNUv1SHvAVVZMYRDW7pPwwwyRsKBCwoZkiE4rNto_un5BvNsC0JijIGrkO-nXqfSnbwLbA_zAyaD61ouhVfXwYC6o3szxeR53UTuwj2DOiJWti4fvZlBW91q0eLSd2Wgy0NotaSpBe_FTH70NgBXGh2AwP-_8oJArAAgjGqSTmZRUz5fcZQmqkjFtqcTaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4370e0903f.mp4?token=gpwZg5fc49-ucLWMZyYiC-KlxMnQoO1Z_Pkups6NkHYoTPvRYYva349-6hGSliYjaqAhoiejIW06V932ahXGEX8EasqQQTxk_Kk2INhpXlmM08a4NiFE8BjxSbW-vm1BBdMFXlD5g6yZScIu2vYLgLmSrNUv1SHvAVVZMYRDW7pPwwwyRsKBCwoZkiE4rNto_un5BvNsC0JijIGrkO-nXqfSnbwLbA_zAyaD61ouhVfXwYC6o3szxeR53UTuwj2DOiJWti4fvZlBW91q0eLSd2Wgy0NotaSpBe_FTH70NgBXGh2AwP-_8oJArAAgjGqSTmZRUz5fcZQmqkjFtqcTaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس مسائل بین‌الملل: با قبول کنوانسیون «رژیم حقوقی خزر» توسط ایران، تکلیف قسمت بزرگی از آب‌های سرزمینی کشور به کسب رضایت کشورهایی مانند جمهوری آذربایجان گره می‌خورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/683386" target="_blank">📅 20:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683385">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">01 Ane Manaee (1403-07-12) Marghade Sheikh Sadoogh</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/683385" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه اول
حجت‌الاسلام امینی‌خواه:
🔹
تقابل حق و باطل در سوره محمد(ص) [09:15]
🔹
آثار قرائت سوره محمد(ص) [10:20]
🔹
بررسی اوصاف مؤمنین و کفار در این سوره [13:15]
🔹
رهبر معظم انقلاب: شرایط امروز هر دو جبهه حق و باطل، شرایط مرگ و زندگیست. [14:30]
🔹
مقایسه شرایط امروز با شرایط قوم بنی‌اسرائیل [16:00]
🔹
اگر بترسیم محکوم به شکست هستیم. [20:40]
🔹
بررسی آیه اول سوره محمد(ص) [24:00]
🔹
نصرت الهی و صداقت در عهد [30:10]
🔹
خدا از ادعا، امتحان می‌گیرد. [38:28]
🔹
امتحان‌هایی که خدا از شهید سیدحسن نصرالله گرفت... [40:40]
🔹
وقتی انبیاء هم به یأس می‌رسند... [49:00]
🔹
لحظه‌‌ای که از همه منقطع می‌شوی؛ آنِ مانایی است. [57:00]
🔹
نقش رهبری(مدظله‌العالی) در حفظ ثبات و انسجام جامعه [01:01:29]
🔹
بصیرت زینب کبری در دل سختی‌ها [01:05:45]
🔹
نقش رهبران و مؤمنان در جلب نصرت الهی [01:11:10]
🔹
روضه اباعبدالله الحسین [01:14:55]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/683385" target="_blank">📅 20:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683384">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
اعتصاب و کمبود شدید نیروی انسانی در فرودگاه بن گویورن
روزنامه یدیعوت آحارانوت:
🔹
کمیتهٔ کارگران اداره فرودگاه بن گوریون در فلسطین اشغالی  پس از اعتصاب روز پنجشنبه که هرج‌ومرج ایجاد کرد، نامه‌ای در مورد کمبود نیروی انسانی در این اداره منتشر کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/683384" target="_blank">📅 20:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683383">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
کانادا تعرفه‌های تلافی‌جویانه بر آمریکا اعمال می‌کند
مارک کارنی، نخست‌وزیر کانادا، پس از آنکه مذاکرات تجاری برای جلوگیری از تعرفه‌های جدید آمریکا شکست خورد:
🔹
تعرفه‌های تلافی‌جویانه کانادا بر کالاهای آمریکایی از ۸ سپتامبر اجرا خواهد شد.
🔹
در روزهای آینده جزئیات این اقدامات تعرفه‌ای جدید را منتشر خواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/683383" target="_blank">📅 20:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683382">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGpPLGCUMmWX0K6bbpiDGMTslMmev0QLhQwYAafmSl5sWjhzdB3i-PW7wuZZLnNQqLyI-3i_8zGWzMt3Z8DHcJ0Gd18diUjSLjbjypEpumZdRsKL6meiHzTnOxJz_TwkN2kYIWL_qBLrryLOH1IgzY8nIumQ9qvqNiLstL56eiu4lSXj48zGl7vWx6YWA04ErKBBT_WeFghm53PpnaL0mkkLKIrxm2soJ3_KyPTibDv_p2WU_vTmIF0pFJ4ZeDgZiEhFlNYtp1vR3eMBRQsmKyIlaWmuw3HaTJJMWIMoOeW_yXs8CzFKFm5j9sr6SQcjwHaRYz5CZICMHZLfd-Rvng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عضو کمیسیون امنیت ملی ابراهیم رضایی: گزارش‌هایی منتشر شده است که نشان می‌دهد هواپیماهای جنگی و تانکرهای سوخت آمریکا در فرودگاه‌های قطر، کویت، امارات  حضور دارند
🔹
آنها خانه‌های خود را به پناهگاه‌های دشمن تبدیل کرده‌اند. نباید بعداً از این موضوع شکایت کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/683382" target="_blank">📅 19:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683381">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
اسرائیل به آمریکا: از اقدامات ترکیه در سوریه نگران هستیم
رسانه های رژیم صهیونیستی:
🔹
اسرائیل به واشنگتن اعلام کرد که از اقدام ترکیه در استقرار سامانه های دفاع هوایی در فرودگاه ابوالظهور سوریه نگران است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/683381" target="_blank">📅 19:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683378">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b6c72dc61.mp4?token=kkDmE5yZdsJC1jozPRaIOzEYIAy6Rn1iY00mmjAoz1_POmEyQZuoKx2ILaKaFOJnAAKXf5NqEyy6MGcKrjeISoqLaH3m-Ib7xDrJR5LC6wuRYXSEkzz0bXaPQiSisrn4w4bU249Grq5CWrCGqO1w-xkkogDkn5fii6Z9U-nsOtMzxEa3RRpBJttzFKR41CS-A_pg7PIvaN_t8mJvx_z_nBjjTmQjxDHMYEksUTg0AUc_JISqWCV4HeM5aTvXJy3nf9zOqCBYoEwpu3GZ5KqG1GOzIIv-BIKsg3uYijhxo6kCw6mUSQNMzlOJddwbFguZxmLARTI4oeDQEAxN9Lchqx_VftbhYqxsmC6tsac86MF4cKnPfUvCj00zZ2XXwbkhY5IBO4B307gq5qYgHNQKLL8yAPbBvAkRewT59ijpWBU2YgosQZseC5V4QNou_3wBjNHzQhu2log1txAW54vbvhVzwafZC6uIGqSGXcTtLT_e4tugegKqZ3XjRZfy4CvazSVb-0LYvdu4VG2UystkdbFWIerWuS4kNh0UqB5cuZqDDkl_BNUaNp7SHgcc30Sh0mbELw7TGsalJFEz0H_v37XGM35eBNS_PNa2E_EqKErpZiQSx57qwH-OiRFuWcbe5ZRWUMqNxi_YCsFTzd4Py8BLUGwz_BUMjdxXeMw6xco" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6c72dc61.mp4?token=kkDmE5yZdsJC1jozPRaIOzEYIAy6Rn1iY00mmjAoz1_POmEyQZuoKx2ILaKaFOJnAAKXf5NqEyy6MGcKrjeISoqLaH3m-Ib7xDrJR5LC6wuRYXSEkzz0bXaPQiSisrn4w4bU249Grq5CWrCGqO1w-xkkogDkn5fii6Z9U-nsOtMzxEa3RRpBJttzFKR41CS-A_pg7PIvaN_t8mJvx_z_nBjjTmQjxDHMYEksUTg0AUc_JISqWCV4HeM5aTvXJy3nf9zOqCBYoEwpu3GZ5KqG1GOzIIv-BIKsg3uYijhxo6kCw6mUSQNMzlOJddwbFguZxmLARTI4oeDQEAxN9Lchqx_VftbhYqxsmC6tsac86MF4cKnPfUvCj00zZ2XXwbkhY5IBO4B307gq5qYgHNQKLL8yAPbBvAkRewT59ijpWBU2YgosQZseC5V4QNou_3wBjNHzQhu2log1txAW54vbvhVzwafZC6uIGqSGXcTtLT_e4tugegKqZ3XjRZfy4CvazSVb-0LYvdu4VG2UystkdbFWIerWuS4kNh0UqB5cuZqDDkl_BNUaNp7SHgcc30Sh0mbELw7TGsalJFEz0H_v37XGM35eBNS_PNa2E_EqKErpZiQSx57qwH-OiRFuWcbe5ZRWUMqNxi_YCsFTzd4Py8BLUGwz_BUMjdxXeMw6xco" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعرخوانی و حال و هوای متفاوت آبادانی در برنامه «سرآشپز»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/683378" target="_blank">📅 19:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683377">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
وقوع انفجار در خودروی حامل عناصر «الجولانی» در حومه دمشق
🔹
منابع خبری گزارش دادند یک خودرو که حامل نیروهای امنیتی دولت شورشیان سوری بوده، منفجر شده است.
🔹
منابع محلی گفتند یک بسته انفجاری در این خودرو منفجر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/683377" target="_blank">📅 19:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683376">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d63d9af8fe.mp4?token=BYGpJLuT_F7ZXIBipZiOcrS0BSa5bAfk29paItlgPafjPBIUKQjaZn5RhcBUJrnFoqro4HK-fYpjOWKE7qtYIFYC-XGJpIGwqIOVqIX3LaR2x_cFseWyo0xI_gA7YHzSCd9YlYVTJcI1NG64udFu489-PIWoBXlcrmdWbNnEZwkjczLOdCYXhJsn43c78glgsAbEy4p4eB8sd9DvwWD8wA6M4fk3YHnyFANdA5RlhaS5FuXA2WhMDHU7owYk13nB5rkA6xmjv7soXsW4lrNdqaTmKX_Gys_279BJ_AaFCRgvihAre9m3ZBRG1BMgGok9O2zp40zEG59hYuuAFcmIig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d63d9af8fe.mp4?token=BYGpJLuT_F7ZXIBipZiOcrS0BSa5bAfk29paItlgPafjPBIUKQjaZn5RhcBUJrnFoqro4HK-fYpjOWKE7qtYIFYC-XGJpIGwqIOVqIX3LaR2x_cFseWyo0xI_gA7YHzSCd9YlYVTJcI1NG64udFu489-PIWoBXlcrmdWbNnEZwkjczLOdCYXhJsn43c78glgsAbEy4p4eB8sd9DvwWD8wA6M4fk3YHnyFANdA5RlhaS5FuXA2WhMDHU7owYk13nB5rkA6xmjv7soXsW4lrNdqaTmKX_Gys_279BJ_AaFCRgvihAre9m3ZBRG1BMgGok9O2zp40zEG59hYuuAFcmIig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طناب‌کشی تابوت‌های نمادین ترامپ و نتانیاهو در خیابان؛ حرکت متفاوت دو خانم که وایرال شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/683376" target="_blank">📅 19:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683375">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpa5ejujFOIvZPsWgyPH322JF5qPvJMyzwtR8M1Sm8czbBKGPGiuLmYR0RWujE5BfZktv0Eq94Q5YuyzyBAILqAm4prSqBsld8yyoic4ZSzDsM0EM2Uav4iO5MH0iSIwc9i_OnbXcW5ZMqJCGGZuPCoy-j_KK-vEIEuDpPnXxZsnQKWQOrlylQRPID3aqRz8XtUVHWWB0O4_xlvNiDXk5XKViYZrHizYTPZQCjJrnQoO3Aa5JCCNetnU7ISswcGCxr8KgT3XR8SSbGwJGIRVMYzrTy9gfwHb027wk22FY47sZJEhWBvDctdIpvJ4kIiovCvlLtWyrC-aqKv2soE1uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
مراسم تجدید بیعت با امام زمان (عج)
✨
🤍
به مناسبت سالروز آغاز امامت حضرت ولی‌عصر (عج)، در اجتماع بزرگ «مراسم تجدید بیعت با امام زمان (عج) و رهبر معظم انقلاب اسلامی»
▫️
با کلام: حجت‌الاسلام و المسلمین حیدری کاشانی و علی‌اکبر رائفی‌پور
▫️
با شعر خوانی : احمد بابایی
▫️
با حضور:  سرکار خانم الهام چرخنده
و حسین حقیقی
▫️
با اجرای : امیر مهدی باقری
📍
وعده ما: شنبه ۳۱ مردادماه، ساعت ۲۰
میدان شهدا، مشهد مقدس
🤍
بیایید در این شب عهد و انتظار، دست در دست هم، بیعتی دوباره با امام زمان (عج) کنیم...
@Heyate_gharar</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/683375" target="_blank">📅 19:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683374">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOem-FgVZIU_7SOnEGOjLmJeI8kz9IA1kSZlPmpsaWo9u-TzQ-UPITw9HnUqH6UCF38frSKAP552BV7DPWCM7rtka5rQrol5z_6GJM0BYfiZMob8j3kG6e9Z5QZoXfNd7xg8ZNwI-MKFPvi7-c19CZ-YyPJDKaEFzm-pPk6NTfGkDc5rZZPUFtjP9ZAGnZhw8qxjM4s2X_T14EgkjLBYHKNGd7RxgGXSD7K-MziSs4HAHS3Ur2x4ptNmqqYzqryAeDOIqzmhbdjW6-_6A6ZyvOxADZCHHk9OT5NoAWAp6f6nobk5MaOfLw2DBpIM3OBqFr4q_7xXl2cWd-2FicQhWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عارف: دولت اجازه نخواهد داد تروریسم اقتصادی آمریکا، ثبات اقتصادی و معیشت مردم را هدف قرار دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/683374" target="_blank">📅 19:16 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683373">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8as7cU8fgVa3qWBng3ODqDAlcPNRM6hIfk5ImUb5j5lb08rFXlU3lnZpJ5eTw3LMQC9W4HXJuNr9MNacTmaRNXPx-_WNpTDUR6uHXr5612qb2vq9G7pkWr2PmpjYcbm-fVJdj8d1vSrQcZEYNRB0e1XLZjy4v1zi2gc2YQ-zG02rRVDwJbLIAcBXaWzfCti78I-iIDdzBF-8M2saEw63TafYodXTnrVhLpxARw-GALu2XCowiuSOARTXAwIdlQ9qGlEL_SncTKl7r9Pts1TSFqmeggK-rEbl9Lu0UB6347ZIHE70cdV9YT7P1rLCDtdp0pP8-y6Nz8EgG7QTnb_VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدهای دستوری برای استعلام امور اقتصادی خانوار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/683373" target="_blank">📅 19:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683372">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ag4YVmZYZzXoDHMbzs3kpGcXosVRryINXZPpX904J-GrAeXVQHsJrDqjcP3nPCF_XO6TuOrrY_6cfx2aD225i8ssk2h4c7mGpvCz66X4MUKI_LPtRmCE7F_ovu5DoEwAq6YjEUuYzpEeADQUEv80pOWz_eI4IyRxrornDDsMn5EJKyXz6UEpChL55Qkjxw2fbNCb_5WF0QSwS94c1STOlZxMtkdiZcAJ4xuB5fM9mif4NbNrT2GxMWc7-Ypwr6dnKOHj1iWrUxMDgTCsTv5_zSkXsi4bPFXsfPO80aVAVMXIDrK8FXShcSi9UfGKwvsc6HPpAmb_Y80wDwqVuAVA2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منابع غربی مدعی عبور ده‌ها نفتکش‌ و میلیون‌ها بشکه نفت از تنگه هرمز شدند  ادعای باراک راوید خبرنگار اکسیوس:
🔹
جمعه شب حدود ۴۰ نفتکش از طریق کانال عمیق جنوبی تنگه هرمز به آن وارد و از آن خارج شدند. سه مقام آمریکایی به من گفتند که جمعه شب حدود ۱۶ میلیون بشکه…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/683372" target="_blank">📅 19:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683371">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbHp2jTK3OcJ5ywi1XJ5tOIWnC9rYLIJPr9Vm4Ur4tQeZNojlgwcDivZr6PhWLVvQdiri-2G71sW4G_OcPF2YZJ4dM-lFYvVV_rfWdKe-tN2eQUiXIQ85H01bVqnRcjdjZkeecUYI8xqBRs0LlXWbtumemEP-_TndEHgeURAu36UC-NGaH0U25qniu_X57Afxhk-2n4gO12k7ycakZguK9K4h6nKO48lSKxr6PL3VS4pvcRcA9fAomx-IbFqVhZlN3nrxzEeYARdX0VP4f6IyKOau2VGXS_RcLFfJa6yOdoOmjKcTZ956KBwUEtZGUvF8GxZHKAUgn81dDo1u6HN2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرپرست وزارت دفاع: میدان جای خوبی برای آزمون سامانه‌های جدید خواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/683371" target="_blank">📅 18:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683370">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
نایب‌رئیس شورای سیاسی حزب‌الله: انصارالله آماده است در صورت محاصره حزب‌الله و لبنان، باب‌المندب را ببندد و «کلید» این تنگه را در اختیار مقاومت قرار دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/683370" target="_blank">📅 18:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683369">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9de26de11a.mp4?token=CTwtaf6tUayBxHJl5pjQx3gCE8zTMtvFX7CrDH1i395t4dPrVFzdQwyFpuLgoFefvH4DIMguATno8XPvNEsPQPZXHROhCI7cRfCGu0LdMI6ZGZpWHnvE7gn1wuvZBZDPfztFq8CgMYHebSESgS5JRx3yRKNuxcUs4lXAQeGLoGOV95oEAq0xu-lJqFqIhMJxbgmSe5Ne90W-59XNNGr-onxji4H4OqeC7kcjxtrNLPnkER8Du9CULH8LpyXIuHIWaK1MPVWkKPUkpfGMLWmIbf-p_qjhX1y629XhHwwQq44LLxYFuWpA72RHpe7fBsfUyoKel05oP1jrYYvCm1T7DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9de26de11a.mp4?token=CTwtaf6tUayBxHJl5pjQx3gCE8zTMtvFX7CrDH1i395t4dPrVFzdQwyFpuLgoFefvH4DIMguATno8XPvNEsPQPZXHROhCI7cRfCGu0LdMI6ZGZpWHnvE7gn1wuvZBZDPfztFq8CgMYHebSESgS5JRx3yRKNuxcUs4lXAQeGLoGOV95oEAq0xu-lJqFqIhMJxbgmSe5Ne90W-59XNNGr-onxji4H4OqeC7kcjxtrNLPnkER8Du9CULH8LpyXIuHIWaK1MPVWkKPUkpfGMLWmIbf-p_qjhX1y629XhHwwQq44LLxYFuWpA72RHpe7fBsfUyoKel05oP1jrYYvCm1T7DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش باران تابستانی در بخش احمدیِ هرمزگان
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/683369" target="_blank">📅 18:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683368">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
نخستین تصاویر از پشت صحنه تمرین «سیاوش»
🔹
همزمان با ادامه تمرین‌های کنسرت‌ نمایش «سیاوش»، نخستین تصاویر از پشت صحنه این پروژه منتشر شد؛ روایتی تازه از یکی از ماندگارترین داستان‌های شاهنامه.
🔹
«سیاوش» به کارگردانی حسین پارسایی، تهیه‌کنندگی سید محمود شبیری و جلیل کیا و بر اساس طرحی از متین ایزدی، با سرمایه بخش خصوصی در حال آماده‌سازی است.
🔹
زمان و مکان اجرا و سایت رسمی بلیت‌فروشی، به‌زودی اعلام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/683368" target="_blank">📅 18:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683367">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: عبورهای شبانه و «چراغ‌ خاموش» از تنگه هرمز با اسکورت
🔹
شرکت‌های نفتی عربستان، کویت، قطر و امارات، فرستنده‌های نفتکش‌ها را خاموش و نفت را از تنگه به دریای عمان منتقل می‌کنند؛ آنجا نفت خام خود را به نفتکش‌های مشتریان تحویل می‌دهند./ انتخاب…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/683367" target="_blank">📅 18:28 · 31 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
