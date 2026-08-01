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
<img src="https://cdn4.telesco.pe/file/iBBnj6TmPR_opyBQUkrk1K27OUvrgYHEsBE8EcfElK7up-zrRZrGEORGCE8oT0_UQI_VVqVv4CkOHE7ixwpsxDkOOV7YAcOaumtR4tz2aMLuR486YVaS1uUKidGNZNfPgtvxlhZhYRT779hIMhEeag55ztyoMBN1xmexdjO26p2SfddNYJtTnYC5aMXMrU09AZynoiVbEG-WYGm3tkJnFp7-3qt1iw8J1Hm8rFKsxbFo5jOCTHpI4ZK0DlFtYXVx-wFAFde5Yfc20yrzpRyWgYCHtjZwvc2_hzjZ_NpmH4ljWOzm0SAN3xwv-SAxCxB9OIKsgGY6_owvYgAGjqe02Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.1M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 16:29:12</div>
<hr>

<div class="tg-post" id="msg-677332">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
سه گزینه نتانیاهو برای حمله نظامی به ایران
🔹
سی‌بی‌اس نیوز، به نقل از یک مقام اسرائیلی مدعی شد، بنیامین نتانیاهو در دیدار اخیر خود با رئیس جمهور فاسد آمریکا، او را در جریان سه گزینه برای جنگ با ایران قرار داد.
🔹
از جمله این گزینه‌ها حملات نظامی متمرکز بر مسیرهای زمینی تأمین تدارکات خواهد بود.
🔹
همچنین احتمالاً زیرساخت‌های انرژی از جمله نیروگاه‌ها و پالایشگاه‌ها نیز هدف قرار خواهند گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/akhbarefori/677332" target="_blank">📅 16:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677331">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
مسدودی ۳ سایت و حساب آژانس‌های متخلف فروش بلیت اربعین
🔹
دادستان تهران از مسدود شدن سه سایت و حساب آژانس‌های متخلف به دلیل عرضه بلیت پروازهای اربعین با نرخ بالاتر از قیمت مصوب خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/akhbarefori/677331" target="_blank">📅 16:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677330">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eb82625a1.mp4?token=If1TkU4xMxT8EY5Tar8M7bMkBebeu6kOTrTmc_DXudr457DuEERtGUuDYVsHBWonM4uHH8Ak7-zdi2LRIt__fm0j4bRfec0Q-k94lCpWHhVFNmEdmLYeOOeJT5TlLS-Dw0M4bS3BTl4GRskvUgRcc2SQRpENZhasv5-G2ysul-w20qCDBTa39jvbZkCw1SUkfS6381jJWj1ncXC7Vpoz_Ox940eIv3z8RVuZmEp2czJCCN9rUcrCHqprqUrydZMF8jSi1yXaYRZsS6w5Um1-gzfKgzpLGBpmPoJg9XdE1qdEjsc7c4AzF5gFCnL3UBPTtT4wECeh0I1vdF4n-2GJpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eb82625a1.mp4?token=If1TkU4xMxT8EY5Tar8M7bMkBebeu6kOTrTmc_DXudr457DuEERtGUuDYVsHBWonM4uHH8Ak7-zdi2LRIt__fm0j4bRfec0Q-k94lCpWHhVFNmEdmLYeOOeJT5TlLS-Dw0M4bS3BTl4GRskvUgRcc2SQRpENZhasv5-G2ysul-w20qCDBTa39jvbZkCw1SUkfS6381jJWj1ncXC7Vpoz_Ox940eIv3z8RVuZmEp2czJCCN9rUcrCHqprqUrydZMF8jSi1yXaYRZsS6w5Um1-gzfKgzpLGBpmPoJg9XdE1qdEjsc7c4AzF5gFCnL3UBPTtT4wECeh0I1vdF4n-2GJpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار مهیب یک کامیون سنگین در روسیه
🔹
یک کامیون باربری بزرگ در بزرگراهی نزدیکی روستای «مارچوگی» در منطقه پرم روسیه منفجر شد و شعله‌های عظیم آتش تا دقایقی به هوا برخاست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/677330" target="_blank">📅 16:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677329">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c5ec6cefca.mp4?token=g8CqCfrrP1EDCyo8caKdZCbvGZyepa_fc1dZdWLrobgeV4n5UDz0uDk-rVsgGajywW1QcdU64lKxKhMC_FzVOdmPwFw_cNyD97AhtAz6h49H3pNCS-dppKw8U2rDOg0JI65v0Ah72kXcn25z9tz_zYn2U_OG5XzXSVdBRJeF2pezQFHr1QIF7rrNkBnboantYdmAgaitdjLEvim9AKbddiAdI9qbz6_htR0_vS63_8TEFZpTgpeB3RkBvtPs4BH2fFtHUjs0KaUgBs136wq_9g396Ol8Ebq0T47Xk9xp_p82LU3XGAoxMZMGufVzM4OCp97siU214ESjJQ78yqL8xoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c5ec6cefca.mp4?token=g8CqCfrrP1EDCyo8caKdZCbvGZyepa_fc1dZdWLrobgeV4n5UDz0uDk-rVsgGajywW1QcdU64lKxKhMC_FzVOdmPwFw_cNyD97AhtAz6h49H3pNCS-dppKw8U2rDOg0JI65v0Ah72kXcn25z9tz_zYn2U_OG5XzXSVdBRJeF2pezQFHr1QIF7rrNkBnboantYdmAgaitdjLEvim9AKbddiAdI9qbz6_htR0_vS63_8TEFZpTgpeB3RkBvtPs4BH2fFtHUjs0KaUgBs136wq_9g396Ol8Ebq0T47Xk9xp_p82LU3XGAoxMZMGufVzM4OCp97siU214ESjJQ78yqL8xoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام سید عباس موسوی‌مطلق: تشییع رهبر شهید در عراق، بی‌نظیرترین بدرقه تاریخ عراق و بلکه تاریخ اسلام بود/ از مردم شریف عراق که این حماسه را آفریدند، قدردانی می‌کنیم
#
یالثارات_الحسین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/677329" target="_blank">📅 16:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677328">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
سفارت آمریکا در عراق: به شهروندان خود در عراق توصیه می‌کنیم هوشیار باشند و از دستورالعمل‌های مقامات محلی پیروی کنند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/677328" target="_blank">📅 16:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677327">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
کشف پیکر ۱۱۲ شهید از زیر آوار خانه‌های غزه
🔹
نهاد دفاع مدنی نوار غزه اعلام کرد پیکرهای ۱۱۲ شهید را پس از حدود دو هفته عملیات جست‌وجو و آواربرداری، از زیر ویرانه‌های منازل خانواده «الحساینه» در محله الصبره شهر غزه خارج کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/677327" target="_blank">📅 16:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677326">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
شایعات تخلیه نقاطی از هرمزگان بی‌اساس است
معاون استاندار:
🔹
شایعات مطرح‌شده درباره تخلیه نقاطی از هرمزگان کاملاً بی‌اساس و فاقد اعتبار است.
🔹
هیچ‌گونه تصمیم یا برنامه‌ای برای تخلیه مناطق هرمزگان وجود ندارد.
🔹
وضعیت استان کاملاً پایدار و امنیت برقرار است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/677326" target="_blank">📅 15:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677324">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U1bCNmn7nppVTPOAAsoNQP_lk5vs7FCuw-3bp74MWVv9Ch2nX1ynaxO65ebtMyfv4n-aPs4x4AY2nGNHPBWcsqYq9g4mgzRgB2aoo7w-ACzMxe4tTWRp3o2IHhlih-nCgEietWdHYiTWUkYgvkoGho63lW4r_T3rGdpOCSlpqwS4AdeDamoon0srDF_dPuejHFzUd2zfBmjBv0OSGhn6dXnoRAbNc-MUdFybB0V27nJqUJ0GKKqGaIHFYZSiPuOMvpTB2YptizYOJ5C5Yn8XC8DYERAxV68B3KsySkoPZSZjTSyexriTITXtzboku80nUN_MuDz6m4WCq-6VKy_q4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/APGehJbu-YB4H5s5AJhBwlnThrrpSi_q5RINRL1WzJ1NnU8yuTFDIpWcPq-aNtkaVGWVw3iqeLPzQBq77dveXGukzDXbGkXPhhBJ4algFuGhQRwqW3ZsheqUxhjcIPmCWJlKeQR0s5p60eFFuSx4SpsKtt2RWghWS43H5m85H3wB1nVp7C_AaVFOdDWQTpJ0ndJK5WbWTMPzKNTtP_sXZoYcIxb-C0oy1-GlJfPghj9DtRtLbDoji1LD51kaCotbpjjLhWgkR-9iob4Yte4ON-zhKcjqTbogwHEQQpha6XMbwrwm1g6s4bp5w9CYYDjnVxIcUUDZXF-0rs5H0UH5VQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
وقتی انباری جای خانه را می‌گیرد؛ «مناسب مجرد آقا» یا نادیده گرفتن کرامت انسان؟
🔹
انتشار آگهی اجاره فضایی شبیه انباری با عنوان «مناسب مجرد آقا» با انتقاد کاربران همراه شده است.
🔹
بسیاری معتقدند مجرد بودن، توجیهی برای اجاره واحدهای فاقد حداقل استانداردهای سکونت نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/677324" target="_blank">📅 15:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677323">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
عارف: افزایش نرخ ارز به سرعت در قیمت کالاها اثر می‌گذارد، اما با کاهش نرخ ارز، قیمت‌ها متناسب با آن کاهش نمی‌یابد و این روند باید اصلاح شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/677323" target="_blank">📅 15:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677322">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
منبع لبنانی به «الحدث»: دور هفتم مذاکرات بین لبنان و اسرائیل روز سه‌شنبه در رم آغاز می‌شود و به مدت ۳ روز ادامه دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/677322" target="_blank">📅 15:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677321">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
آتلانتیک: بزرگ‌ترین اشتباه ترامپ، نشناختن ایران بود.
🔹
رئیس فرماندهی اروپایی ایالات متحده: نیروی کافی برای محافظت از اسرائیل نداریم.
🔹
امام جمعه بغداد: عربستان با کشتن فرزندانمان از نخست‌وزیر استقبال کرد/ترامپ به هیچ یک از وعده‌هایی داده عمل نمی‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/677321" target="_blank">📅 15:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677320">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
رئیس کمیسیون اروپا: اکثر کسانی که به طور غیرقانونی به سئوتا رسیده بودند، به مراکش بازگشته‌اند
🔹
هیچ‌کس به سرزمین اصلی اسپانیا یا بقیه اتحادیه اروپا نرسیده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/677320" target="_blank">📅 15:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677319">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
آب دوباره گران می‌شود؟
آب و فاضلاب:
🔹
تصمیم‌گیری درباره افزایش تعرفه‌ها برعهده بدنه اقتصادی دولت و وزارت نیرو است که با هماهنگی وزیر نیرو و بر اساس الزامات موجود انجام می‌شود.
🔹
در حال حاضر هیچ پیش‌بینی و تصمیمی درباره افزایش تعرفه آب وجود ندارد و امیدواریم این اتفاق رخ ندهد و بتوانیم با همان افزایش تعرفه‌ای که در ابتدای سال ۱۴۰۵ اعمال شد، موضوع را مدیریت کنیم./باشگاه خبرنگاران جوان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/677319" target="_blank">📅 15:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677318">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a31eafcc50.mp4?token=PdaB_yUAdnAHSmui5AXjL6Gih_5IBt_Vlio5Zfy2bQDJyMaP3BqT2pYy5TP6FSyiGepZAB5td-IBmm3-0u4xniJjoWX4gsv_w3OEvXwafCtBRRt5GxKjm8MoN8CuBKabo7dLTEb38H-OZZs10gVyy7AB1M95-HVfrFYSDfWBXLyKRrgUI9u_-WBsBHBpnmuuTC6Q7zTdf-LpbYkNcLUvlcZ34nN6LwFkZoW9f8UVFpvvu9IDmzmJdCvK5npsLXO4OOn_uAfLMZbhWHLbVwDatpuahMFaW97l61QYj6De6m6v-ohd3LeRYKLvreon1dtGJd6Al5G2iRQNrvPYoQRxtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a31eafcc50.mp4?token=PdaB_yUAdnAHSmui5AXjL6Gih_5IBt_Vlio5Zfy2bQDJyMaP3BqT2pYy5TP6FSyiGepZAB5td-IBmm3-0u4xniJjoWX4gsv_w3OEvXwafCtBRRt5GxKjm8MoN8CuBKabo7dLTEb38H-OZZs10gVyy7AB1M95-HVfrFYSDfWBXLyKRrgUI9u_-WBsBHBpnmuuTC6Q7zTdf-LpbYkNcLUvlcZ34nN6LwFkZoW9f8UVFpvvu9IDmzmJdCvK5npsLXO4OOn_uAfLMZbhWHLbVwDatpuahMFaW97l61QYj6De6m6v-ohd3LeRYKLvreon1dtGJd6Al5G2iRQNrvPYoQRxtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه انحراف از باند هواپیما امبرائر ۱۴۵ از باند فرودگاه شیراز
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/677318" target="_blank">📅 15:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677317">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0e5419cb9b.mp4?token=eARVfrKF0kk9d5pQtKCvnHsA5zTWG0WxDu9rLJMhX3SxJJgHCqO33sgzsWctN_DnGd4xkS1Pc88XaOp4v9TYoiNjo295iv61gCyjJEMHkiRuEwW6tQkuD8mz0vHAzlA4YrmqXpUdpUQIaWPa79joe75cxTO-ChOBuyKFWQkYDcI8nQKHuOHKhbZUSWN5OuaJUmIYXYrFzsau9bgkD36ltGkq4TfYnfZRqRh9cO1pREX6thpq7RSc5srtumTZN4IQVz1nh5gArzsopPJkaOvOjiNTkzpJYvf-lHL_oOFko6ehYquQy6jAxKRORFXh30mbhBoGj6nl6_DmnvNaDdSa0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0e5419cb9b.mp4?token=eARVfrKF0kk9d5pQtKCvnHsA5zTWG0WxDu9rLJMhX3SxJJgHCqO33sgzsWctN_DnGd4xkS1Pc88XaOp4v9TYoiNjo295iv61gCyjJEMHkiRuEwW6tQkuD8mz0vHAzlA4YrmqXpUdpUQIaWPa79joe75cxTO-ChOBuyKFWQkYDcI8nQKHuOHKhbZUSWN5OuaJUmIYXYrFzsau9bgkD36ltGkq4TfYnfZRqRh9cO1pREX6thpq7RSc5srtumTZN4IQVz1nh5gArzsopPJkaOvOjiNTkzpJYvf-lHL_oOFko6ehYquQy6jAxKRORFXh30mbhBoGj6nl6_DmnvNaDdSa0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضربه بزرگ به کویت؛ حمله‌ای که برای همیشه خاورمیانه را تغییر می‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/677317" target="_blank">📅 15:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677316">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
عراقچی: ما به تلاش‌های خود برای پیشبرد منافع کشور در چارچوب تدابیر رهبر انقلاب و دستورالعمل‌های شورای عالی امنیت ملی ادامه می‌دهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/677316" target="_blank">📅 15:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677315">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9aeec8228.mp4?token=iGJe914PJmZltq_EErOdkL-xGpEjzrsVxpyhZSccErDb3uRPDbBIfzUqN2iIrw_a-WfXwj6Lx3UXyZRgjLgAafVuKkqyx9_7xRov7Q16d_2c3iAFq4pMpIJK-NeLsgIckwqQE8khDoRUbXTQiHWsLSwBg5sUNh6_sp7RZS4uczC1w-L6SSXVzl0O05Lkk9K7vuT87VWZJeg00JO5Vw092U-XpfvjXQq_Bmsu9cUKOOvsTRpUAdREQCpRkPg5VCOF_BjnPZ0wODH5vaCytrzq2XDyfYmMgD4I0XhxUYwGXzcb_3qv6JPxwN1S0qXKDWpuqLSHcrqpzKMoemSzYoIbrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9aeec8228.mp4?token=iGJe914PJmZltq_EErOdkL-xGpEjzrsVxpyhZSccErDb3uRPDbBIfzUqN2iIrw_a-WfXwj6Lx3UXyZRgjLgAafVuKkqyx9_7xRov7Q16d_2c3iAFq4pMpIJK-NeLsgIckwqQE8khDoRUbXTQiHWsLSwBg5sUNh6_sp7RZS4uczC1w-L6SSXVzl0O05Lkk9K7vuT87VWZJeg00JO5Vw092U-XpfvjXQq_Bmsu9cUKOOvsTRpUAdREQCpRkPg5VCOF_BjnPZ0wODH5vaCytrzq2XDyfYmMgD4I0XhxUYwGXzcb_3qv6JPxwN1S0qXKDWpuqLSHcrqpzKMoemSzYoIbrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨️
سعادتِ خدمت در این مسیر، توفیقی است که به هر کسی داده نمی‌شود
▫️
کسانی که با ایثار و سخاوت، تعریف جدیدی از انسانیت را به جهان نشان می‌دهند. خادمان اربعین، سربازانی هستند که در جبهه مهر و محبت، برای تکریم زائران امام حسین (ع) شبانه‌روز تلاش می‌کنند.
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/677315" target="_blank">📅 15:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677308">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n67-Zope01EUJ8Eu5iuPsWRF0-mttzQZukT5X1CiZcPWgQhKoVV2rY8zzStFFg-x65tcezRh1ZKysN6FhtogPpIQ0hSSEV7Jj2e2qT_BeOTL4L3U53JPOXuDupYvrGeU6htI2XFou7bSwxTmCpQKJiQTrjhs9RRGZoWYMPbY9nprR1QrNJW8_jZkPdfiw5Vm7_WD4oGVozR1gNmYKPEJPC0NNhZmOUNwWFdDefR4skha86YmH2m-h1Criunep6poNpm_aNPpvXKmqVqk65vyfcfOUa5MO6ztA2Z38RZ32emUW0wmgq0lvHz-DiVsogeelS4Y-SKEpwj1OVWtaCKvqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Td2FaeLEQN7RACJws0ovBw8VodzCLRL0IWi9_qRB32XGdPCSP6O1sEM1NRRoZ7lbIcm1MYwr-yvww8ZrVPKu9onbiVWT4fOww872V-hZnsKg8BQl8cEbFUsoi7Q4_dnX76OzvE2dn0WGNzTLZA73fgUadjh-h4L9tDlRq4jOAr9RGIfmP5E4PWCYnGpyjIZGR6IkSxLpOf5B0j-73N3erf3AIqk28XwaDU2KdzwQcmZeg9rLj6xMTTixtqBf3oIjprdhvLMaIA4shaJcljj14KPYmYNU4uKPOWiGhbb-RzzUHjrBU19gEFotk3cg48WhAZduD7QegFxQ949I8uKuBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KqZep3k2hG-IytLUPpUckKEzW-5l_d7gaYvIfIgitEahPDTUeu4ZtaTfAUnJ9DdrojWLzewqK2O7cU0ODzVYnZ8MbiNv9DtzT-Ip4nUN3y0okz32p-B9H33BN-IoTiUfO4b9cZpJxl7UIuTJjkAGG2uDdeK5Ts8fnvaeEttGQwKGIYAGMvUyFCoCLbkqP4kvU9FLlFe7jkq8b7MML_GX3H1soIP1uWzAjY6HHzDAL0NsOA0Ud3XyzsQwMc9WLqpo0s1xQsiRfI0RLE2nj8DJyNEJRVJCDiD76R4ItylnyRWM-MaOR1PT5hkBQ0oengyOCjlTS_TiXEq7G4VMR3AzXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kGFMy94t5qhm49dj8JVVCM32wBc28qD43LS1QxtnYdDrsC457AYIaCO7qddBY-XhetW0goQBAUr_N3oQYgo51GO_dcaxpWnG1CFAf-Jcnkmc6A8A7xc_fHFB5FDN8m9t4CfcYo790pJsxVLWu_P8LgpfLsgph9Y2Olt45hU9M0o3SHce7HgUqz4Ov9LAWHe1m61ezHdJNmZdsD7WeIh8-eHZWw8tpUFrQUPnfKDe51wIMLDSVnG2VTInotGxTMP_J2sUCqOqRhdEmAlAjAXKhE08S6GdOaBGVbMwL1cq_efi5tv6BK8aH1xAUXD4yR4cqnqN2vXEAmx-jZYq7ZVm-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aH6Nvq0vGCedJ0IM0jU8jvathrI0IPfpn0x1s-9ulhnmtJTKkvzo63AWDi7Lblk65yW0qEpk7ENuZUT9Dw8V3oCZAuaK0LhxLcfhjp3WwrI5CM3aNSe-dcUJNnu3Kh12GyHOrDqWIrLUbBDeI3J_lzLZJHBu40KnMGPyL_n8YF6Dmnc9hqrIexfR4uhAUeOig6uW12CqAyhJwO4Wym3HeRgi3tJjLjHmHki_DAPxXGXHdTb5X50_u6p7omsXF1u6A6yLm7LaAagK-3x__MxLG6w2ydgk4Ov8cbfkhtHtmESn_E0I6JjccoIUM9rP0L-F1gIbjv_9tobpw_LeUTJKAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t1NbuXnTy9fuzj93iHMi8iB-QvBuc0IDbLYnWHawi_7bNLYq1MlmKgNMgwCe8RjejAzofNbWK6tcMJwo_axvTm80uAAlskojkZpBee8vlbP5Cp4uyORzvzJslmQwYF1ypqbvLVXvqKukEGBBsF0iSpMBhvXH0jclqw_9B_xEjHb8HQqfjcmNU7Vbd4rkypqHI72wtGXddK2J07ttNzqcqrnJUQncWAQxUtx5Vqo_hm9ixGOGJcA9aiBkLhD8FrryKCeDXy_Pb-Pzgs56Iln3W_4ilHzy4WrH9mqV93k25emG60hv-n8T227kKNR915s8fefzwS_chP3t98eEGnlZXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y2wkzjH-_hllLpssA8meJ96PjpcblhXIoR2kOURep7V2KXd5LbSrnqGO54apYeRsenA3rvoIbQak6M00q7CbbJUOfhA-O4wkwoEBckAtQRCbicW5ntnXISeeSn9GeO_S_eQB2FD8WFyuaSPFNzQ8yzaoK3eetow1RA2Gc6qLnTg14TvQdyG7HjCFF4-be47DvZ45GwN8pwyct47G4-uH43QormE2JyIuPtgEK_4-zErmckgDv0AUA1I3I5ftJgm6w6TGaw4VgoZMIU8u2t6GqDngjL614HySEegLJBSdBcM8ozTndjXACJItLigQ7YquzX4fRufq-KV0fypzLaLQhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نمایش عشق و دلدادگی خانواده بزرگ فولاد خوزستان به مکتب عاشورا در چهارمین آیین «نذر حسینی»
🔹
در آستانه فرارسیدن اربعین حسینی، بار دیگر فضای معنوی و شورانگیز یاد و نام حضرت اباعبدالله الحسین(ع) در میان خانواده بزرگ شرکت فولاد خوزستان طنین‌انداز شد.
🔹
آیین «نذر حسینی» که طی سال‌های اخیر به یکی از برنامه‌های شاخص فرهنگی این مجموعه صنعتی تبدیل شده، امسال نیز با حضور گسترده خانواده کارکنان برگزار شد؛ رویدادی که چهارمین سال برگزاری خود را پشت سر گذاشت و توانست جلوه‌ای از همدلی، ایمان و مشارکت خانوادگی را به نمایش بگذارد.
👇
👇
akharinkhabar.ir/local/10964167/
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/677308" target="_blank">📅 15:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677307">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
پنجره متفاوتی به آخرین دیدار شهید هنیه با رهبر شهید انقلاب، در روز قبل از شهادت در مردادماه ۱۴۰۳
🔹
بازنشر به مناسبت سالگرد شهادت مجاهد بزرگ شهید اسماعیل هنیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/677307" target="_blank">📅 15:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677306">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
مدال طلای ملی‌پوش شنای ایران در قزاقستان
🔹
هومر عباسی، نماینده ایران در مسابقات شنای قهرمانی غرب آسیا در ماده ۱۰۰ متر کرال پشت (بخش Open) به مدال طلا دست یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/677306" target="_blank">📅 15:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677305">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
آغاز طرح برخورد با گران فروشی و احتکار
رئیس سازمان تعزیرات:
🔹
از امروز به منظور برخورد با هرگونه گران فروشی و احتکار بازار‌های تهران با حضور هزار بازرس زیر رصد قرار گرفت.
🔹
قرار است این طرح در تمام استان‌های کشور انجام شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/677305" target="_blank">📅 15:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677304">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7898f9c624.mp4?token=SYgyVGz05NFsUW5ZwBXcBwdJM1eG0Vx9grIQ1KGep1Y2AoDlDdj-daSRWe689fcijrpmVazTq1DrRxC-HbLje1O9-GlXZqg61-GX85RwRJeniK_eWgcZ46kjwCEYGslRPCBZxJDjMLBdGYqHprlfl09VVBt21n-MaT38IOQLFLMjnbtY5eUd5CdhrKEuSVJPgMqxMnnlUpAYMk3qNNV_tGFudTsXtEn-Hen3YaAXitA8kJZ2Yw5bECS7xJ-RbMdQsc7h1Qy2R231L_Tvq-G10y-A6qOV8ig-IbG4c57v2Ncc_F-Xs3vNHpaNjJt9dvvjP6bEM5sfUmdcRcM6GZbAvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7898f9c624.mp4?token=SYgyVGz05NFsUW5ZwBXcBwdJM1eG0Vx9grIQ1KGep1Y2AoDlDdj-daSRWe689fcijrpmVazTq1DrRxC-HbLje1O9-GlXZqg61-GX85RwRJeniK_eWgcZ46kjwCEYGslRPCBZxJDjMLBdGYqHprlfl09VVBt21n-MaT38IOQLFLMjnbtY5eUd5CdhrKEuSVJPgMqxMnnlUpAYMk3qNNV_tGFudTsXtEn-Hen3YaAXitA8kJZ2Yw5bECS7xJ-RbMdQsc7h1Qy2R231L_Tvq-G10y-A6qOV8ig-IbG4c57v2Ncc_F-Xs3vNHpaNjJt9dvvjP6bEM5sfUmdcRcM6GZbAvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت دانش آموزان در امتحانات نهایی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/677304" target="_blank">📅 15:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677303">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/037bfd86f9.mp4?token=r2uda8on3KbCi886Wfd6GFyYC39BGxdyZE5hJV3lT2xJUql9l-xaYEoyX2Ch9km5cnIPxM9CgaekC2tnocoUeUOcRCYqxprjEBxsHf5iIgMdAiXGeiPEKa4RQaStZBouU4FCmdAAmtIkbrTZ9uSbeD0MzO2DKgq_qO4QR5qz0Ijv-SBZ3O4Bmc38Zd8bvFVEV4hacUCbietSbjAq-RxwULajAB7Dpyza0_RE7AWwvEEPYT4aG63BZRkmamYQ9pb80YgEfbk3mNJf6X1j7I-p3miCV1--ujSJym20DFTD0AOaucYMr7IJCcjtHSXn56sgc56maMrQPkfaNw48IXVJAQ62U0NTIQ_BwW7aIfSg1tZUtvwAUSMenxsfPCjR0SSCaswyHHGaFWtKEl2UCAXtwdHtZjgkcVJ3YJ5cSG7KhBzojGHy-ICMK6RyGgs0LpZEQgd3HjqAoqgdw6IZSjQlbWxxaUxvT-1DDE8IF0SjYeqqB5WXI5yTlanmfqLAxib45bqUyC2fHu-EsaGAyhb8Ia4T9xG7Ljo07_SIBLKqSjTv5FByCVF4vnBaNI6mthlzhAImKb4HiglbfEKoZrj_zbpa_20xOs1uJSf4ayXfxudnvrzx23L9B9TbStFyHXBert7aADAs--ccfSF6WIEop4AJd25g0SNLjw_NQcVW1bI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/037bfd86f9.mp4?token=r2uda8on3KbCi886Wfd6GFyYC39BGxdyZE5hJV3lT2xJUql9l-xaYEoyX2Ch9km5cnIPxM9CgaekC2tnocoUeUOcRCYqxprjEBxsHf5iIgMdAiXGeiPEKa4RQaStZBouU4FCmdAAmtIkbrTZ9uSbeD0MzO2DKgq_qO4QR5qz0Ijv-SBZ3O4Bmc38Zd8bvFVEV4hacUCbietSbjAq-RxwULajAB7Dpyza0_RE7AWwvEEPYT4aG63BZRkmamYQ9pb80YgEfbk3mNJf6X1j7I-p3miCV1--ujSJym20DFTD0AOaucYMr7IJCcjtHSXn56sgc56maMrQPkfaNw48IXVJAQ62U0NTIQ_BwW7aIfSg1tZUtvwAUSMenxsfPCjR0SSCaswyHHGaFWtKEl2UCAXtwdHtZjgkcVJ3YJ5cSG7KhBzojGHy-ICMK6RyGgs0LpZEQgd3HjqAoqgdw6IZSjQlbWxxaUxvT-1DDE8IF0SjYeqqB5WXI5yTlanmfqLAxib45bqUyC2fHu-EsaGAyhb8Ia4T9xG7Ljo07_SIBLKqSjTv5FByCVF4vnBaNI6mthlzhAImKb4HiglbfEKoZrj_zbpa_20xOs1uJSf4ayXfxudnvrzx23L9B9TbStFyHXBert7aADAs--ccfSF6WIEop4AJd25g0SNLjw_NQcVW1bI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش جالب زائران ایرانی به بمباران برخی مناطق عراق و شایعه وقوع جنگ
/ تلویزیون اینترنتی مدار
برنامه‌های تلویزیون اینترنتی مدار رو در یوتیوب ببینید
👇
https://youtube.com/@madaar_tv?si=ICb2BPIkhXtjbTUS
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/677303" target="_blank">📅 15:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677302">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_XVoClew39N6GLVClTqMzo3Va45KdFgmgSeAVPy8Kd6xL7XeyAUZ9v4leAU9jfIdnQrGQ6fj5--E8GZYAJfFyfxY0vBamKnBvgO4Nivz0u7LR9J7ixXRm0Wai6M_AMkRcrVYfVpOeqs55KcAvxR-lXYJGpwG7hmqlxONsklaPGCwBUGUMW2LS9yuvjexX2GrrzKLgwfvVfZaoCSN470WbceX4LEcI42L6cXnqTk6bI2lFrygN3pASOW8FS4rcsB8Xv28wk5guiz2IjtCjJY7IvUAXlQggNLRdizMGJjW3HamTsZw-2Z2dfG7PZzx-8LboM-4J4_1n_N-nm2wMhIig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترکیبات موجود در توت‌ها، چای و کاکائو؛ دشمن پیری مغز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/677302" target="_blank">📅 15:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677301">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5b36c837c.mp4?token=khR-7X8_uleoocYw1S3_YzfYIL-M4vUmVQp3AUhMa7v8pN_HeX4U0qQptIkMXdE1ik6kGJ3sioQoNob3CKDhwDtJeqjJfAEn2MlZsaPo-F0nZwFifqI5URhZe_uz-tjvqBfE4CM4qNYBBU1XbRSXfTKptdt5eiStIXQMyHImrgF7O7bC_UwcC0vvsuh0Pt2zp4yD8pTWSI6djv-vGTX9bN3LhN-xbPFGTXIg5y14hYO3AmGhqSymSBlIa7vq0Sh7QhZmopKX88IfbIclZwH3bHhlGldph-AKDryrUm-3fuSF5RomCNFChuoEcuamV5taUlRLD95nuB7LyoPDp40PIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5b36c837c.mp4?token=khR-7X8_uleoocYw1S3_YzfYIL-M4vUmVQp3AUhMa7v8pN_HeX4U0qQptIkMXdE1ik6kGJ3sioQoNob3CKDhwDtJeqjJfAEn2MlZsaPo-F0nZwFifqI5URhZe_uz-tjvqBfE4CM4qNYBBU1XbRSXfTKptdt5eiStIXQMyHImrgF7O7bC_UwcC0vvsuh0Pt2zp4yD8pTWSI6djv-vGTX9bN3LhN-xbPFGTXIg5y14hYO3AmGhqSymSBlIa7vq0Sh7QhZmopKX88IfbIclZwH3bHhlGldph-AKDryrUm-3fuSF5RomCNFChuoEcuamV5taUlRLD95nuB7LyoPDp40PIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون وزیر اقتصاد: انتقال سهمیه سوخت از کارت سوخت به کارت بانکی آغاز شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/677301" target="_blank">📅 14:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677300">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سفارت آمریکا در اراضی اشغالی: آمریکایی‌های منطقه باید آماده باشند و در صورت تشدید تنش، خروج را در نظر بگیرند
.
🔹
بلومبرگ: ۶ نفتکش عربستان پس از تهدیدهای انصارالله، مسیر آفریقا را برای عبور انتخاب کردند.
🔹
ثبت‌نام آزمون دفتریاری از ۱۸ تا ۲۴ مرداد برگزار می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/677300" target="_blank">📅 14:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677299">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2gEo-Fz2wcsncJEEI5_ChhkEv_5guuWGw2d00gClSgRmexfa556yZgJ9216nk-fA-X6bV0TP6o61iKVHvBYW26_-dlD1D0EUeycC6FVQ-_V1BMv7T0Dotin0u30Hw5WoYOxMHnd6bAS5x4RsyDI0ZIElnTbT2-Xjcxy9-s1dyUFL9dA98hdRSZW0ghK3hZpBN50shBygSu6eX1rZckJxMlBeBDSnbzAyWgwQJRIkq3ZalbJLsop7Z1eEKnCDEe-iLQU8OBZ4ReOa50fZ7yNbvzKV-iSv2VR4af323aQIkpMHEKsdjLX8lcsdXMM5gFTue1SZPhIJ6SXTFf5piKGdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدیر سایت انگلیسی امواج: گزارش شبکه CBS مصداق جنایت جنگی خواهد بود از جمله قطع برق یک کلان‌شهر ۱۰ میلیونی بدون اینکه حتی یک کلمه درباره مشروعیت و قانونی بودن آن گفته شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/677299" target="_blank">📅 14:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677298">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bg81fqSDqoYXQhCoZKT47lxw2sjfaa_nFkX8O0-9ROykIdHIn8ltfYxZHM_eVQpx5YcUKDjuUn3znARxUI9mzcc2VYNZVo06hOo9kqO7rasOQJ-ES2OgjtnT1Bvh2LTGywY7c_4Qukq_HZUM9b7jl9e6NEPnpyXutGVfZqdaRrZr9B9UD_iR1v1lz-VHmRNYkr2mPe0YSmYbL0v2C7q7t79v2Hbng_57BzgpkKyZFB7B1mK4e0MEd9Ux5lxesc6JyY8dFeQWy2pnLtzrc6iGjfbtqEP0oaTLbwgNsmW6odV8zw-adP8fKfxnDpYCYNfmB5ePwYt8VPENbfSL6DKjtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱۰ مرداد ۱۴۰۵؛ ساعت ۱۴:۲۵
🔹
قیمت دلار در معاملات امروز با رشد قیمت، به ۱۹۴ هزار و ۳۰۰ تومان رسید.
🔹
تداوم تنش‌های سیاسی و نظامی در منطقه، مهم‌ترین عامل حفظ روند صعودی دلار و افزایش ریسک در بازار ارز عنوان می‌شود./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/677298" target="_blank">📅 14:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677297">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اسپانیا: تعداد کشته‌شدگان بحران پناهجویان سئوتا به ۶۷ نفر رسید؛ سازمان‌های قاچاقچی مسئول هستند
🔹
آنچه در سئوتا اتفاق افتاد، حمله‌ای غیرقابل قبول به حاکمیت کشورمان بود.
🔹
کسانی‌که به طور غیرقانونی وارد سئوتا شده‌اند، هرگز وضعیت قانونی دریافت نخواهند کرد.
🇮🇷
…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/677297" target="_blank">📅 14:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677296">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmjShedhMHu9RYENWoRGHwhaE14pSiCGxPIni0IDRedh6kuyO3OlrTG8xrLmKbWqhwSQzZahQ7KU3kNTA9xIpl-7l0w1b2JwvkN-6XDxYJxppu0wjjVXnWfX10gvjWvlXvaiQ8PpwvAT1gsVEVTiSRbVHzv07NuTZJAF_gcQvU8lzTxHOCIORl-raSO-nzgrHKSs67tEDDEqcLPwtn73-7rk-InILGdccEolrtz6wgpvz583GKZ8ZEGMMb9Okmko4w_hjLVdOKs3QY9FCLp5HyhOeBB4pQJLpU_89NefQGlVD2xweLc4o8lQANcNNnOQGEusvj5AotBrdJnDVzlWtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کمیسیون سلامت دیجیتال نصر تهران: پلتفرم‌های سلامت دیجیتال غیرقانونی نیستند
🔹
رئیس کمیسیون سلامت دیجیتال سازمان نظام صنفی رایانه‌ای استان تهران در واکنش به نامه مشاور اجرایی معاونت درمان وزارت بهداشت درباره فعالیت برخی پلتفرم‌های دوراپزشکی تأکید کرد:
🔹
فعالیت پلتفرم‌های سلامت دیجیتال طی بیش از ۱۰ سال گذشته در چارچوب قوانین کشور انجام شده و تلقی غیرقانونی بودن آن‌ها بدون پشتوانه حقوقی، فاقد وجاهت قانونی است.
🔹
اگر دریافت مجوز برای یک کسب‌وکار الزامی باشد، باید این مجوز بر اساس قوانین موجود تعریف و فرآیند دریافت آن به‌صورت شفاف در درگاه ملی مجوزها اعلام شده باشد. نمی‌توان فعالیت کسب‌وکارها را صرفاً به دلیل نداشتن مجوزی که مسیر قانونی تعریف آن طی نشده، غیرقانونی تلقی کرد.
🔹
پلتفرم‌های دوراپزشکی به‌ویژه در دوران کرونا و بحران‌های اخیر، نقش مهمی در حفظ دسترسی مردم به پزشکان و تداوم خدمات سلامت داشته‌اند.
🔹
سیاست‌گذاری در این حوزه باید بر پایه تنظیم‌گری هوشمند و استفاده از ظرفیت بخش خصوصی باشد، نه ایجاد محدودیت‌هایی که می‌تواند نوآوری و دسترسی مردم به خدمات سلامت را کاهش دهد.
متن کامل خبر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/677296" target="_blank">📅 14:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677295">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Czgppm7kOcSUUN-WmdPYlVaJnEF5oScfJA88O7IvEXKtOEk_P4vqvk5QPSeDEKEJoV7sQg_Tun52bEA4AijMhidnf2_qmG6pTqDFL3JX6YcZll9DUeuhvAhGgBKDQ0xz0NCczSEnSzrBKAu0JyR-wghLadrIsz3CYrs46wh91LkvrcZFZGab-F-T_lXxgsQtJN9DyvSzmbqAwSsbuf0IfmsGJZciddotkN7wxjYHt61E-uXWLOPyp3J7Wb_E08mo-VAC7LuqY_3hcFTwQrtDwtkEOABtbGTOEGu4Zpppsy-8aN3jjS7JPXGxZmc36ZBwJL1Ee8o-78J9tir01wEdcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولویت مهارتی آینده از نگاه افکار عمومی چیست؟
🔸
در این نظرسنجی بیش از ۲۷ هزار نفر شرکت کردند که سهم روبیکا حدود ۵۴ درصد، بله ۲۸ درصد و تلگرام ۱۸ درصد بوده است.
🔸
بیش از ۴۴ درصد شرکت‌کنندگان، هوش مصنوعی و کار با ابزارهای AI را مهم‌ترین مهارت برای آینده دانسته‌اند.
🔸
کارآفرینی و راه‌اندازی کسب‌وکار و مدیریت مالی و کسب‌وکار در رتبه‌های بعدی قرار دارند.
🔸
با گسترش هوش مصنوعی، اولویت‌های مهارتی از زبان انگلیسی و برنامه‌نویسی تغییر کرده و AI به یکی از اولویت‌های اصلی بازار کار تبدیل شده است.
@amarfact</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/677295" target="_blank">📅 14:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677294">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9316cef4f.mp4?token=VlxEli54Tqm-B9-s58T9YE9ZwPUCAFKcMawtajllDvSTmoTeiWLA6yFQ2pt1pYC4gznZB1JLq75yO5hgG_CaeITe1J4fNetG1Sn8xhDvisbEPsIu3Oi9ADT0SqREOSBNNZYiyw2DCH4iGAKtK22FBMiOKpfbk9-uJNDF4O6hDLrI2S3sHQggx3zV-2ywIUuHGL6IsyezwsvtL3CVry-fXvvvOiGV-73XQ4oOORn1fh0JuX07W8Z5QvuenC-aIyeupFeDfOLDRXQuu3LkI0yK4WTxQqC2usbcEr5BtCtlJxof0KoEFigPtPW07j4EJMbMH9K2a0Bg-vexX062k8PfyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9316cef4f.mp4?token=VlxEli54Tqm-B9-s58T9YE9ZwPUCAFKcMawtajllDvSTmoTeiWLA6yFQ2pt1pYC4gznZB1JLq75yO5hgG_CaeITe1J4fNetG1Sn8xhDvisbEPsIu3Oi9ADT0SqREOSBNNZYiyw2DCH4iGAKtK22FBMiOKpfbk9-uJNDF4O6hDLrI2S3sHQggx3zV-2ywIUuHGL6IsyezwsvtL3CVry-fXvvvOiGV-73XQ4oOORn1fh0JuX07W8Z5QvuenC-aIyeupFeDfOLDRXQuu3LkI0yK4WTxQqC2usbcEr5BtCtlJxof0KoEFigPtPW07j4EJMbMH9K2a0Bg-vexX062k8PfyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاهده ۲ قلاده خرس‌ قهوه‌ای در شمیرانات
🔹
مدیرکل حفاظت محیط زیست استان تهران از ثبت تصویر دو قلاده خرس قهوه ‌ای در مناطق حفاظت ‌شده شهرستان شمیرانات توسط دوستداران طبیعت خبر داد و این رخداد را نشانه ‌ای از پویایی زیستگاه‌ ها و اثربخشی اقدامات حفاظتی در این مناطق دانست.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/677294" target="_blank">📅 14:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677293">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
کلاهبرداری با عکس یادگاری
🔹
یکی از جدیدترین شگردها، ارسال پیام‌هایی با عنوان «عکس یادگاری» یا «تو هم داخل این عکس هستی، دانلودش کن» است که کاربران را به نصب فایل‌های آلوده ترغیب می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/677293" target="_blank">📅 14:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677291">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
حمله پهپادی رژیم صهیونیستی به خان یونس
🔹
شبکه المیادین از حمله پهپادی رژیم صهیونیستی به منطقه مواصی در شمال خان یونس واقع در جنوب نوار غزه و زخمی شدن چند شهروند فلسطینی خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/677291" target="_blank">📅 14:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677290">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
قتل در نازی‌آباد بر سر زنگ مکرر ساختمان!
🔹
مشاجره میان یکی از ساکنان ساختمانی در نازی‌آباد و مردی از اتباع افغانستان بر سر به صدا درآوردن مکرر زنگ ورودی، به قتل ختم شد.
🔹
متهم پس از اعتراض ساکن ساختمان، درجریان درگیری با ضربه چاقو او را به قتل رساند و از محل گریخت. پلیس آگاهی تهران تحقیقات برای شناسایی و دستگیری وی را آغاز کرده است./هفت صبح
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/677290" target="_blank">📅 14:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677289">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e251b0948.mp4?token=iGOEaB-jQj2aiExja2DOxwAItHpCot71Q9fTWD68ga06aVAOX4rcMBClwYv8qPlsCiQeKm1MJQuLk9OE91BOn2rFNCb2qXPOXzC62ZUxft8eCLuQIFCPRiW5JmVpwJC4xf0UgaTU87bZPZimgqXwuGy9K9SUj2b-JOUVaM4AUcZ57A9i9IZtHYNJQlmBAp_wwGLhshQfwOLzinOHbIUVWukhVefp2rmDRVBeeQN1xduT4PypufSJJvVny7_1iIdonHao4K_58HEyrWS6JSUxQVUtuN9hR2n7gSZiisxVmHZ6H2kM6UQQk-pcqNtGlTW8rQ9mWkvwezqx8N0zrlxrcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e251b0948.mp4?token=iGOEaB-jQj2aiExja2DOxwAItHpCot71Q9fTWD68ga06aVAOX4rcMBClwYv8qPlsCiQeKm1MJQuLk9OE91BOn2rFNCb2qXPOXzC62ZUxft8eCLuQIFCPRiW5JmVpwJC4xf0UgaTU87bZPZimgqXwuGy9K9SUj2b-JOUVaM4AUcZ57A9i9IZtHYNJQlmBAp_wwGLhshQfwOLzinOHbIUVWukhVefp2rmDRVBeeQN1xduT4PypufSJJvVny7_1iIdonHao4K_58HEyrWS6JSUxQVUtuN9hR2n7gSZiisxVmHZ6H2kM6UQQk-pcqNtGlTW8rQ9mWkvwezqx8N0zrlxrcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عارف: افزایش نرخ ارز به سرعت در قیمت کالاها اثر می‌گذارد، اما با کاهش نرخ ارز، قیمت‌ها متناسب با آن کاهش نمی‌یابد و این روند باید اصلاح شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/677289" target="_blank">📅 14:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677288">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ac437de3c.mp4?token=RH20cKLTbElyQWrnwuBjvp-4mrgXsto_WoT2pKJLIC-l1PWsOkaN0LvvDHFAvEw_25OWQLc7fEQhGmeGZsq4uQOMxPxU_1-F47WNpquWxJnBokLj5gKLoGjYLOAtsr16aMPaGUQbJ4zNiVbdd0A03-TFD4bqBB4pmPwPQgTC3fYsUKHy39f90xdfCmaGx4peUtFfGPdAa3W1EHIaLpYqK0lOfjdsDVZaNbpRYxWEnjvY_N-qwgCt_yRNq8O3O9bQTipUJO23jZ0N5ko2Wvi-VWMs3TakX2IN-9bWCSEYaRsgsLDH_MLkUcVM46zbVjaoaERqg8BbB72IoQ5jmyw-Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ac437de3c.mp4?token=RH20cKLTbElyQWrnwuBjvp-4mrgXsto_WoT2pKJLIC-l1PWsOkaN0LvvDHFAvEw_25OWQLc7fEQhGmeGZsq4uQOMxPxU_1-F47WNpquWxJnBokLj5gKLoGjYLOAtsr16aMPaGUQbJ4zNiVbdd0A03-TFD4bqBB4pmPwPQgTC3fYsUKHy39f90xdfCmaGx4peUtFfGPdAa3W1EHIaLpYqK0lOfjdsDVZaNbpRYxWEnjvY_N-qwgCt_yRNq8O3O9bQTipUJO23jZ0N5ko2Wvi-VWMs3TakX2IN-9bWCSEYaRsgsLDH_MLkUcVM46zbVjaoaERqg8BbB72IoQ5jmyw-Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رفع زگیل جوش و دست سوخته از دید هوش مصنوعی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/677288" target="_blank">📅 14:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677287">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
سفارت آمریکا در عراق: به شهروندان خود در عراق توصیه می‌کنیم هوشیار باشند
و از دستورالعمل‌های مقامات محلی پیروی کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/677287" target="_blank">📅 14:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677286">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
مالکان مکلف به اجرای مصوبه سقف اجاره بها هستند
وزیر راه و شهرسازی:
🔹
موجران باید قراردادهای سال گذشته خود برای اجاره دادن خانه شان را به مشاوران املاک تحویل دهند.
🔹
سقف افزایش اجاره بها مسکن نسبت به سال گذشته ۲۵ درصد است و همه باید آن را رعایت کنند‌.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/677286" target="_blank">📅 14:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677285">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
تصاویر جدید از آتش‌سوزی در یکی از پالایشگاه‌های استان اربیل  رویترز:
🔹
آتش‌سوزی در یک تأسیسات ذخیره‌سازی سوخت در پالایشگاهی در جنوب‌غربی اربیل.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/677285" target="_blank">📅 14:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677284">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37a7c160b8.mp4?token=tyTNSNerCmL7_KaxOpl4rQ40e7GYbBmtnBXwkm6flsJB3i4RCW7PzhTXLjqeXra7LCweKQorP4WkzT9wbQ7d_U_Oblxm5iVxbQoZoEMX4YBgaHTO8XEVvTcGsbUqswy2fNrniJ0O40f0TxluPxcXUhwu3cR8VBsfmhFqqNKZR4OuGKmRsAHbZPZfoweCoJDLIvsPM9_8Ql2SxycykAqeDXBGr1jW7ouIQ5QvRbTjNLPxN1UIdlO3lagF7lO016-awGWvLhQV7uLaJGQ8oqWdWsiJDFiwdiBArSz--wl39K2UJBHb-J9HXUsVPO2LEoMwOrSzcF8vEhl96VWLa5SelA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37a7c160b8.mp4?token=tyTNSNerCmL7_KaxOpl4rQ40e7GYbBmtnBXwkm6flsJB3i4RCW7PzhTXLjqeXra7LCweKQorP4WkzT9wbQ7d_U_Oblxm5iVxbQoZoEMX4YBgaHTO8XEVvTcGsbUqswy2fNrniJ0O40f0TxluPxcXUhwu3cR8VBsfmhFqqNKZR4OuGKmRsAHbZPZfoweCoJDLIvsPM9_8Ql2SxycykAqeDXBGr1jW7ouIQ5QvRbTjNLPxN1UIdlO3lagF7lO016-awGWvLhQV7uLaJGQ8oqWdWsiJDFiwdiBArSz--wl39K2UJBHb-J9HXUsVPO2LEoMwOrSzcF8vEhl96VWLa5SelA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از  شناور متخلفی که در آتش اعتماد به آمریکایی‌ها، در تنگه هرمز در حال سوختن است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/677284" target="_blank">📅 14:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677283">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gm-Nrwbt5X_YHoJdrhgTinzK6AZdSEHDzcbC2ycFbJ5qfpnoEs54xE3BNbS5VGEPKb0VnQzbekQ_QhcGMqvahMZ0A8Bprene0CvHcaro2FWWEvnBfzGSCX6dtGlBWeO9cq18jctUwILFP41YXJa8r74jYDHtGE6SkMNt8Tky7tOgRzpDvVJHZclw0ppfFvu6AzARWo_NXfe25zsQ_lomVKUdb-pPpoNmSHEi0iCnE5rRQTls6JYUScYQ3L3VSkvVQap2eUObqWoaDHpmwfQvSprNo_uegD23fzkG19IVsITsBbz7x6fOIYPFVwr9RQBdek0biKpo0zUQkI9HeW6ctQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨️
هزار سفر کربلا
✨️
▫️
فقط کافیه عدد «۲» رو به ۳۰۰۰۱۱۵۲ ارسال کنی و در پویش زیارت به نیابت از رهبرشهیدمان شرکتی کنی
@Heyate_gharar</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/677283" target="_blank">📅 14:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677282">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔹
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست./ فارس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/677282" target="_blank">📅 14:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677281">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf15376740.mp4?token=QEgWrQ4V9IgCodGQuG-nRhoJMq6fpQsd88MdyfIlP-o_E2o9oiygfNnu98PIVoaZs8TJpLFG18hJJysQ3kcrRgUxZzStGJoaTQU561NFLEpZII-0Gv_xQQ1kVVogEh7tB9I3opDCmdnSTe1Oamq8jzNCYP91Y3vFyAQU1IrVO-sYVtHhlQWqERmetKBK0N3ObVxORZDmxn0JwRnsh64-4z68zEUJW9S7xZDltXTwA-Hr8WyM30-sbFV1UORtvnhamHpNrvqt2G6_8V8tcZJwUhF7Wvy-AZECMjyQZHu3dvultn4CsNgYmV-VbVZ-JuymDHzb0UE3V0Ech4lIEB-PpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf15376740.mp4?token=QEgWrQ4V9IgCodGQuG-nRhoJMq6fpQsd88MdyfIlP-o_E2o9oiygfNnu98PIVoaZs8TJpLFG18hJJysQ3kcrRgUxZzStGJoaTQU561NFLEpZII-0Gv_xQQ1kVVogEh7tB9I3opDCmdnSTe1Oamq8jzNCYP91Y3vFyAQU1IrVO-sYVtHhlQWqERmetKBK0N3ObVxORZDmxn0JwRnsh64-4z68zEUJW9S7xZDltXTwA-Hr8WyM30-sbFV1UORtvnhamHpNrvqt2G6_8V8tcZJwUhF7Wvy-AZECMjyQZHu3dvultn4CsNgYmV-VbVZ-JuymDHzb0UE3V0Ech4lIEB-PpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تست قدرت گردن یک راننده فرمول یک در مقایسه با یک فرد عادی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/677281" target="_blank">📅 14:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677280">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
خبرگزاری فرانسه به نقل از وزیر خارجه ایتالیا: توافق شنگن با اسپانیا تعلیق شد/ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/677280" target="_blank">📅 14:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677279">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee349df35d.mp4?token=d5SsuCuCTLHoSx254cooVOxU_AMv9qVbDHWMeeFwucBe6iZC9CTOOLwAmPyfhnuspOm2SRGs_D_n1c364xAEhOizPC-eNYCCM6qeEtVnWM_mVKBW-2DSnHnQYycsdQrrkjeTFyPQF9sQyf7I5xQl39PBNfpf7LhfKVWvsqV7KMIWaafxDCKiOTcmP7ls0DggCGp7Fptvz0KbNSDusPk_8J4-3PIHseqIClNh86AAUEIM3o85Qxv9c_W9_nDonXtHpx3Tf5Sb5PdZSld9JyEf3SyFIC8R7FzCnxt7j0cRd9z9hhZFZc7oAEJGlhScS1d-yVD3Y6J8domXEcvQ0m6r0YSu9F8hcNIghwidcICeFTAtd7IQPKW_NC9Mt7sQGaLcBZjZd6VHRwLk_azAyWHcPb4IafnrpcaDIyv7u7g2iCBqUPoeYAf5a2SzA3CWHakJW-qPnZBM8eUavd8b95K88y4lXAvr-5FptDh-Uu5H1OoS8U9zIYaVAjl-S_Q6FFYYsruS3KxXoPNX_Skljc_nRHcV2GAWWJaSfn26CxnLnkVH4LwDx-XjeI5zzWYNk41LMZUL8J6kyUjJs2He3XO9v0bMRp7kGndDcmWaZZQ21HM6529I493TtZ45rRcxRdRpso3df9XP9BQIBmJSOl1Z9z9HQZxtAW0r0o7A2UUGuUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee349df35d.mp4?token=d5SsuCuCTLHoSx254cooVOxU_AMv9qVbDHWMeeFwucBe6iZC9CTOOLwAmPyfhnuspOm2SRGs_D_n1c364xAEhOizPC-eNYCCM6qeEtVnWM_mVKBW-2DSnHnQYycsdQrrkjeTFyPQF9sQyf7I5xQl39PBNfpf7LhfKVWvsqV7KMIWaafxDCKiOTcmP7ls0DggCGp7Fptvz0KbNSDusPk_8J4-3PIHseqIClNh86AAUEIM3o85Qxv9c_W9_nDonXtHpx3Tf5Sb5PdZSld9JyEf3SyFIC8R7FzCnxt7j0cRd9z9hhZFZc7oAEJGlhScS1d-yVD3Y6J8domXEcvQ0m6r0YSu9F8hcNIghwidcICeFTAtd7IQPKW_NC9Mt7sQGaLcBZjZd6VHRwLk_azAyWHcPb4IafnrpcaDIyv7u7g2iCBqUPoeYAf5a2SzA3CWHakJW-qPnZBM8eUavd8b95K88y4lXAvr-5FptDh-Uu5H1OoS8U9zIYaVAjl-S_Q6FFYYsruS3KxXoPNX_Skljc_nRHcV2GAWWJaSfn26CxnLnkVH4LwDx-XjeI5zzWYNk41LMZUL8J6kyUjJs2He3XO9v0bMRp7kGndDcmWaZZQ21HM6529I493TtZ45rRcxRdRpso3df9XP9BQIBmJSOl1Z9z9HQZxtAW0r0o7A2UUGuUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت عشق ملائک به غیرمسلمان‌ها/ چگونه می‌توان فرشتگان را جذب کرد؟
/ تلویزیون اینترنتی مدار
گفتگوی کامل در یوتیوب
👇
https://youtu.be/ckhhIgbCtaE?si=oXx9NgHAEAIdXDJ7
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/677279" target="_blank">📅 14:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677278">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c200977d3.mp4?token=pFpjT5p4wbfj0UzcAcL8jo1QbihUJ3b5dEA1yAKswNYAkciNAapEnfxvv3SRy7GONk5uJ547AkFTEU10dBiccszgML1C2yESfdzzuoimtkiQ3ERN1kj1YMOPfiwxY_2tL_TyEalz7Gk6k1FVZ8ufWC38rqkFRkEd6TMsDgB6JGEdXS0vbOGVnIQ9JaJsolyb9JsDqEpSyO-X00CrU5hTCwT2YoKMJb0PXW5nZewrRerC9xpUnUnjYNbZj5wtPml2E9B66uQxlGYRuzVYa99k2vaCcb11IEBo2liWWb4T3EpdSu42r4FIYZdiWUHUB1OhOernCS7ksNC3VFEI6sAakg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c200977d3.mp4?token=pFpjT5p4wbfj0UzcAcL8jo1QbihUJ3b5dEA1yAKswNYAkciNAapEnfxvv3SRy7GONk5uJ547AkFTEU10dBiccszgML1C2yESfdzzuoimtkiQ3ERN1kj1YMOPfiwxY_2tL_TyEalz7Gk6k1FVZ8ufWC38rqkFRkEd6TMsDgB6JGEdXS0vbOGVnIQ9JaJsolyb9JsDqEpSyO-X00CrU5hTCwT2YoKMJb0PXW5nZewrRerC9xpUnUnjYNbZj5wtPml2E9B66uQxlGYRuzVYa99k2vaCcb11IEBo2liWWb4T3EpdSu42r4FIYZdiWUHUB1OhOernCS7ksNC3VFEI6sAakg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عطوان، کارشناس مسائل سیاسی: حمله به بندر دمياط در مصر، توطئه‌ای از سوی اسرائیل است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/677278" target="_blank">📅 14:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677277">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159c0b99ec.mp4?token=QB4bpZmbOdu6fNqFWBpvKdeosjwEGNzaqcISXrHmgJE6FbwceUN4ZrGLIx_T-7CyqFOhd1Xlwri7soJLnm34hKlsNnU7F6vYykjDgUCeZLvelu_izXnf5imFnv86MBwituE5VOFh16rlMVWYWVPz9nOp9Jx4vg2_J0n5XTZjLsxNVgpCIBJfnEP5rxjwa7mFfSEQxqhK5YPWi8lIEWRWBP0J7R2SpC78BFOq6CGOz4YU7cDsow7tyfIKwe8ShxWha6-xjp2m-9Fi4_55Zgr7Mvzu4ElWJjO1tFcfEEN47mBEm9gv4g_a2UcYs8pH14salwobQqHC4SzEzIufBy1nDa0n60w_FNyEvpEoWKPYfZQi9v_AiqknUe77Vb-_sy9teADS0XgPXgjssj1bhTjh2Zcy1tPtMmmynKUUC4lPPSLWnIoaRoaj7rVGvyAyMaEd7cVTThaDUvQK8SX5IjaCnllpVKwin1vJAa11PVxtKyw0Y-LeuPzNFBcSgmHykg4rrjABpF8FuELxEh1hhopWyUrSR5nPD9uVN-C-RFiapB1Sv39y7GtW2FDeNYOIL3vF_1sW4kt6v-nUB9PO7tIX84xdl237eJCgk7C2sX5UenTtuoIZ1hQSN90pgR7Az-1XgsL3hHuH13JJF2xomSmIy4lLmM1YzFxLOPjpb5oFGvc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159c0b99ec.mp4?token=QB4bpZmbOdu6fNqFWBpvKdeosjwEGNzaqcISXrHmgJE6FbwceUN4ZrGLIx_T-7CyqFOhd1Xlwri7soJLnm34hKlsNnU7F6vYykjDgUCeZLvelu_izXnf5imFnv86MBwituE5VOFh16rlMVWYWVPz9nOp9Jx4vg2_J0n5XTZjLsxNVgpCIBJfnEP5rxjwa7mFfSEQxqhK5YPWi8lIEWRWBP0J7R2SpC78BFOq6CGOz4YU7cDsow7tyfIKwe8ShxWha6-xjp2m-9Fi4_55Zgr7Mvzu4ElWJjO1tFcfEEN47mBEm9gv4g_a2UcYs8pH14salwobQqHC4SzEzIufBy1nDa0n60w_FNyEvpEoWKPYfZQi9v_AiqknUe77Vb-_sy9teADS0XgPXgjssj1bhTjh2Zcy1tPtMmmynKUUC4lPPSLWnIoaRoaj7rVGvyAyMaEd7cVTThaDUvQK8SX5IjaCnllpVKwin1vJAa11PVxtKyw0Y-LeuPzNFBcSgmHykg4rrjABpF8FuELxEh1hhopWyUrSR5nPD9uVN-C-RFiapB1Sv39y7GtW2FDeNYOIL3vF_1sW4kt6v-nUB9PO7tIX84xdl237eJCgk7C2sX5UenTtuoIZ1hQSN90pgR7Az-1XgsL3hHuH13JJF2xomSmIy4lLmM1YzFxLOPjpb5oFGvc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیزر قسمت هجدهم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای حامد البرزیان که با وجود داشتن یک زندگی نسبتاً عالی، بخاطر یک تهمت که به ایشان زده می شود، ناشکری کردن را در زندگی شروع می‌کند و در شبی بر اثر سانحه تصادف به کما رفته و در برزخ روی تخت سنگی مورد عذاب قرار می‌گیرد اما با گله و شکایت از خداوند به خاطر دوره آفرینشش به دوره حضرت بنیامین برده می.شود و زندگی در آن زمان را تجربه و از کردار خویش نادم شده و توبه می کند را نظاره می کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: حامد البرزیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/677277" target="_blank">📅 14:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677275">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
اتاق تهران، حلقه اتصال دولت و بازار برای تاب‌آوری لجستیک
🔺
اتاق بازرگانی تهران به‌عنوان پل ارتباطی دولت و بخش خصوصی، با هماهنگی شبکه‌های لجستیکی، تاب‌آوری این بخش را تقویت کرده و با استفاده از داده و همکاری مشترک، به افزایش تاب‌آوری و مدیریت بهتر بحران‌ها کمک می‌کند.
⬅️
منبع: گزارش معاونت مطالعات اقتصادی و آینده‌پژوهی اتاق تهران
👈🏻
کسب اطلاعات بیشتر: ۱۸۶۶ و
www.tccim.ir</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/677275" target="_blank">📅 14:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677274">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxfTnJbCd1T0zfQf-nfgV4YyE0L7OASrlmE-mjHfhxHMPQ4RDDphcm3oPPWv0XLuwyQZRjQ3iTArdtdME91BoFkm1vWJL5Gh88lZa3ZN6KHYu1bXCC35kDGC9eMKrVfZF8DdQrkBjBLf5c8kMz4Fzk5mAz0i4ARUgyGVbmRORq2jJhNXq-O6md7Zkc_vGMFtgKLA5vN2rN5mWqejKkj-0t0SgZQooxt01I8w34peFZ_HzqmcOckFrGwicY_BzZ6MEMGdOcow6V4i2bNkPLm-Kbg7ngA2MzVnXoj44_dsJLjaaKkYVrMAL4IwwP_9SY9oz81CKqUiH5IXLzTjFgYceQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربرد و تفاوت انواع کت رو می‌دونید؟ #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/677274" target="_blank">📅 14:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677270">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e836379e.mp4?token=LEQ4R8uVdtUTn5sGmMXEFjas4E8vAIDRp1Sh-_fcopXsEuBjRDqkZwGCHvB4OZ1co9Bch8f3XNZqVOSk5GImFP6W2PjDhYoIcd-hapjend6bCHIdbpVtLxfikq27YpFACYIl7798EiiFRtLeqoCWug2tAOm8Ruq3_S5h_eAKrjPCIp1876DTEqyi2OdP0rnpQWt1kIt6HX1N9t_WogYUC3UvsY9P9zhsmDVhZAf2P9R0jpiTMA0mT92YKvLaQ5kdHymoirOegAAEVBy9a2tQza2dULHVte0Ub4t-_aCqXF8A9DJu6yVrONogq1haX5sBU3ICOxO3lfMGdVo20hOJxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e836379e.mp4?token=LEQ4R8uVdtUTn5sGmMXEFjas4E8vAIDRp1Sh-_fcopXsEuBjRDqkZwGCHvB4OZ1co9Bch8f3XNZqVOSk5GImFP6W2PjDhYoIcd-hapjend6bCHIdbpVtLxfikq27YpFACYIl7798EiiFRtLeqoCWug2tAOm8Ruq3_S5h_eAKrjPCIp1876DTEqyi2OdP0rnpQWt1kIt6HX1N9t_WogYUC3UvsY9P9zhsmDVhZAf2P9R0jpiTMA0mT92YKvLaQ5kdHymoirOegAAEVBy9a2tQza2dULHVte0Ub4t-_aCqXF8A9DJu6yVrONogq1haX5sBU3ICOxO3lfMGdVo20hOJxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان شدید آلمان را درنوردید؛ یک کشته و چند مجروح
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان آلمانی دنبال کنید
👇
@AkhbareFori_DE</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/677270" target="_blank">📅 13:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677269">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آبفای تهران: برای تابستان آب داریم
بهنام بخشی، سخنگوی سازمان آب و فاضلاب استان تهران در
#گفتگو
با خبرفوری:
🔹
با وجود شش سال خشکسالی و کاهش ۳۰ درصدی بارندگی نسبت به میانگین بلندمدت، در حال حاضر منابع آب سطحی پاسخگوی نیاز تابستان است.
🔹
در صورت تداوم مدیریت مصرف، در پاییز و زمستان نیز با تنش آبی مواجه نخواهیم شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/677269" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677268">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔹
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/677268" target="_blank">📅 13:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677267">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
طلا و سکه در مسیر صعود
رئیس اتحادیه طلا و جواهر تهران:
🔹
با وجود کاهش قیمت جهانی طلا، افزایش نرخ ارز باعث رشد قیمت طلا و سکه در بازار داخلی شده است.
🔹
قیمت هر گرم طلای ۱۸ عیار به ۱۸ میلیون و ۷۷۰ هزار تومان رسید و حباب سکه نیز افزایش یافت./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/677267" target="_blank">📅 13:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677266">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
فرمانداری جاسک شایعات تخلیه شهرستان را تکذیب کرد
فرمانداری شهرستان جاسک:
🔹
وضعیت در شهرستان جاسک کاملاً عادی است و خبرهای مربوط به تخلیه منطقه صحت ندارد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/677266" target="_blank">📅 13:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677265">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TH6hKrjQmBlgVO-iWLxZFKfXQDIolO_144c18__dYgrGykHFZs6YeuYj6-H-p4ryAHai3PUC_cjRdmGjBTSzdOzOJtX-wtZTfa_RWA6c-rGi0wLQrk822HI17vLnTAi4V1vmeIwypMOVe5P3PDuVBmwcbL2ugfpGiRq5tOuRf_c1rvxyhzVGJ7CrUbmt3zivmw3UauuxgQhby84oV2QrVayCLqDf_0pFvCHGtVSHSY1fk0TKF74GU0l_Tjr6eVoS7nbjlBDFiTsQ_23-Ae-kcfiEsNZ80twOzOOXHZiEXxFGX-u77rjaX8ZdFUfESDgOlqcq9h7WrmjWfujTb28VWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨️
یکی از زیبایی‌های اربعین، همین عشق و پذیرایی بی‌منت مردم عراق است
▫️
با رعایت چند نکته ساده، میتوانیم قدردان محبتشان باشیم
▫️
به اندازه غذا برداریم، غذا را هدر ندهیم و قدر محبت کسانی که برای پذیرایی از ما زحمت می‌کشند را بدانیم.
🤍
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/677265" target="_blank">📅 13:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677264">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20563fa6a9.mp4?token=aSpMTesbfYP02B8SLxZY60gm7WNWNuALCRc9tDo_yIh-d6b-Ztq9tbLZH2B1a0zczHRiiv6Be0Ulc1TA9N_3JuAoXJ0haaiCFxPfRTQOAMgUHxbpZYT0QxE6SXT9kQ9pqoMJ_GrTYeAlmFRzRgqB-aY23_SqZCjB7WgaToOgyf42h-cRxrT1os4nEJYkzgWPPOuFCJEL4ygp24TqJKWqKm4O-Tm0mmucZ2iN4tgYPDFmd-zaDqET46-lQ9MB2wdz7b7hiP_9voOVcHWcfsRCjFaZ7O93sHNBVjBKOITicmTjWvPSw1cOoAV5BACtMwma8qmEgYQ6L9mMdnuWvjNy-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20563fa6a9.mp4?token=aSpMTesbfYP02B8SLxZY60gm7WNWNuALCRc9tDo_yIh-d6b-Ztq9tbLZH2B1a0zczHRiiv6Be0Ulc1TA9N_3JuAoXJ0haaiCFxPfRTQOAMgUHxbpZYT0QxE6SXT9kQ9pqoMJ_GrTYeAlmFRzRgqB-aY23_SqZCjB7WgaToOgyf42h-cRxrT1os4nEJYkzgWPPOuFCJEL4ygp24TqJKWqKm4O-Tm0mmucZ2iN4tgYPDFmd-zaDqET46-lQ9MB2wdz7b7hiP_9voOVcHWcfsRCjFaZ7O93sHNBVjBKOITicmTjWvPSw1cOoAV5BACtMwma8qmEgYQ6L9mMdnuWvjNy-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروج پر دردسر علی دایی در بزرگداشت اکبر عبدی با هجوم مردم/ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/677264" target="_blank">📅 13:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677261">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
خودربایی دختر جوان برای فرار از ازدواج اجباری
🔹
دختر ۳۲ ساله‌ای که خانواده‌اش مفقودی او را گزارش کرده بودند، سناریوی آدم‌ربایی را خودش طراحی کرده بود تا با دریافت ۵ میلیارد تومان و مقداری دلار از خانواده، به پسر مورد علاقه‌اش برسد.
🔹
تحقیقات پلیس تهران نشان داد ماجرا ساختگی بوده و انگیزه او، نارضایتی از رفتار خانواده و مخالفت با ازدواج تحمیلی بوده است. پرونده پس از روشن شدن حقیقت مختومه شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/677261" target="_blank">📅 13:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677260">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b270a75bf.mp4?token=CswiYjDOrZBv_q8OSh7AgFZhwPVhwtiwD3R7mjJ-VcrBS2_ePB9Fk-MVGMDWX16PuQgqrUY-PMIfXEsnnv29tsItkaGJ2plgXydRHIwJEt3alfBLx228kDQE9MU09tsjLFGKJAyjXoYBFaEA3CubBwotjZZJUL8TaWtwa7NyFLmqfJOTgm_NQpT5QNWR3Aoyofa-QPdjwcxJlXpyhsaisiTOsBqVDGp8Tjda8c9ASU6aK36Dbeqba2nUg7nVKaOc6hFBTEXQo5ONJHB-ndF9yvvy9w5Q76Edrh58ZpeRzYzH7cRFRX097ENdqwscohnvDRZDI-F9gsKTaefYVGtIHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b270a75bf.mp4?token=CswiYjDOrZBv_q8OSh7AgFZhwPVhwtiwD3R7mjJ-VcrBS2_ePB9Fk-MVGMDWX16PuQgqrUY-PMIfXEsnnv29tsItkaGJ2plgXydRHIwJEt3alfBLx228kDQE9MU09tsjLFGKJAyjXoYBFaEA3CubBwotjZZJUL8TaWtwa7NyFLmqfJOTgm_NQpT5QNWR3Aoyofa-QPdjwcxJlXpyhsaisiTOsBqVDGp8Tjda8c9ASU6aK36Dbeqba2nUg7nVKaOc6hFBTEXQo5ONJHB-ndF9yvvy9w5Q76Edrh58ZpeRzYzH7cRFRX097ENdqwscohnvDRZDI-F9gsKTaefYVGtIHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نظامیان اسپانیا مانع ورود مهاجران مراکشی به سئوتا می‌شوند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/677260" target="_blank">📅 13:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677256">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TGfcWRYmEChx9FOiMyzlEiVsPzKSG6PBstppquJA_W25x3_xVQa0sIkg3xTF7CXAbYA1KPEJmbxQJxaEVIWu1pfEd1vt_FELflCoxOGGWkCepEom68-zjiBPKWRu8RfX8OKataQBl9I0EqijhPX4naMqxLKrUGLjOcVtUBvmjVVj5sqpZt3wZjQ5V-z3wpB6JwBJmxIOUhT1YU1cw76XJUvYULkYgBfL2Rnpx-07ESqeDvG7sasxzB69mY7kpCic44PYGHsHPckqcVi8eH_B2xtppk9BS-KyWeRj-qFauKQ0jVm8xw3xQourNUpYejgbI87zMtMMvFPP0bAKHT7OFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIbXFQ1QnyN-WS8qCdNSYWG2Hap2fvnkDOAD-0bK0gEDDGePbpRoH35FBJq485oApX5MR1-ZmjBxMv0WMLOwdt1Z2pnVRr7-i6H0SdNLYQNNu6zN_66lp2u6gHOlzPKRvTkeqjM_ZxAAUgYUJ4LNKXUAJYwJ7rfRs_5JXIDGxvgUaxAvOB0YigGeWcnkIEjBKrQph0DbtuVXTS6y_0BuYLUX4IzHC27psHqFPhgH0TXvq20TfWeKz2UQxf3j_Tx7KLW4PP6FYeXDvu2Jh18akK7INElNw8GK1pSXB1RtdG0qOD6H69qhp3TSoAaHLwriTTNq6kia99Bep_IhK4hZvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i9WU4woSD30R13p5xl268nFJQwP1EGyEsybfzFJYEC2Kve9WImx7sJ4qOdHmzLlmCgjOpXeWiIOBF7BP6nhw5D9KUFwQGtW0pqoAUPQa54CKbtxDRHKhX6IBMmn_Dti1sz1YSJ3CbNw7TyF-4KYCH-tK-S7twSFHf2YLRr9Y5KtUm_bNJTbj_ybD_bqghUZGK0GTjqXUQBz6gAr6MyNeRaTgDvvx9cb4HBQKekF8VNmajzfobYJNAgZjNjcwerIbcVkf3kzc3brw_bHQHkFPpZCy8uSE9HLs1PzHtpK1bDf1WMtAhcX9-P2fj2nAton93TWRWZXOikjhzsQ1MDnhpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZuZMFkp6S0RxBT7506AW3dzgpLd6D-5nagr7FXGBMpL50YlZ2Clnr06-USI0aWCNRqgsuM-hFIDmCI_ABwxGjAuDuy3g9W0EsEobjsYD-5xEVJUHNut2xdqkGQq5EK3iP0zG1MTVsrnV5LkIRmgHuTpWReOh50xJzwpcag_qJRhLLwI1HXpREIAWmfXwWPI0UVcsRb_iINmXfT-Z9HWQGMce2eHdI2qIoiwd92BSpG8rEA7JAcxco5grtmBQQEmO0l18-nkm8m8o93rJFbZb_SHHDpClSP9nzSPHIyIC7GhUrMKDL79e2pqkRC5UJLQaQI2KX1XSco46Y-bC08uSSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اکثر افراد نوع اضطرابی که دارن رو نمی‌شناسن‌، با این پست نوع اضطرابی که دارین رو تشخیص بدین #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/677256" target="_blank">📅 13:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677255">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
پلیس فتا: انتشار محتوای خشونت‌آمیز و تحریک‌کننده جرم است
رئیس پلیس فتا:
🔹
تولید، انتشار یا اشتراک محتوای تحریک‌کننده خشونت، تهدید، آموزش اعمال مجرمانه یا تشویش اذهان عمومی در فضای مجازی جرم بوده و با متخلفان طبق قانون برخورد خواهد شد.
🔹
شهروندان می‌توانند موارد مجرمانه را از طریق شماره
۰۹۶۳۸۰
به پلیس فتا گزارش کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/677255" target="_blank">📅 13:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677254">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdtTq3IQpVLfzRDODN6aAU8nDo2PirQw_m9eN6OCGd-eZTIwRlNRYQUgBy25PDoikjRdM7MQnpalvQLnt0TDPtpvsQkZPFxy_Rb7q_o1Q41Wq-VLZ5NYPRr92qOu7BK1dElmTqFhe71FqQ_i_91WuaYjzVTv8FR8PfFWRPlAxSLyXySe9lyb1ShVzzmLcFEn0z4GUf8tKq0cKbA-FJNo0aTlYs2SXqe-rGGVOG9fizMirkJU1haeu5sBPnkat4L5OLY0_J1qtalUD0eWdQlhPWmm3BPRaQ76y0mj0JF1aFuvoRbiFvjGu5cnSprbUhA6UdMuvGenf9XyxsDoqAhDrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه فاکس نیوز با انتشار نموداری جدید اعلام کرد که از موجودی ۲۳۳۰ موشک پاتریوت ایالات متحده پیش از جنگ با ایران، حدود دو سوم آن مصرف شده و ذخایر این سامانه پدافندی ارتش آمریکا به حدود ۸۰۰ موشک رسیده است
🔹
همچنین مطابق اطلاعات منتشر شده توسط فاکس نیوز، نیمی از ذخایر سامانه پدافندی تاد آمریکا نیز مصرف شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/677254" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677252">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fcbbd55ac.mp4?token=hwP4O_-32PVQheLmMJZWTzkwueWUIg5Vwk_jb2WMbqkBByNIfdV37MStSlmSpvwqOiEAi7wwquB2EARchClo0KJbjBq4K_-rWzjFLyAs4CpglgmZCuCUuaCnDwGj_iDPjRLCXD-8iTqxnj8n8GIAx6nLCdEC7Zi0ifCI2bXS-7ilXtyiMspTV2DDm_vWnj68Hf8OYlrdWSKZmFGYbVlvOv65Ju7FcjOFq7mNtWDvtIulzUGsRGoodavCFMMivGYCDafd5BIxM_j1UdsfAYMAFqJTtWWhzbAFZxZkJaEcBq0X52m8p-iUunKPNb-Ns7ID2dHwHwbUNUlgbw5Oofe4LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fcbbd55ac.mp4?token=hwP4O_-32PVQheLmMJZWTzkwueWUIg5Vwk_jb2WMbqkBByNIfdV37MStSlmSpvwqOiEAi7wwquB2EARchClo0KJbjBq4K_-rWzjFLyAs4CpglgmZCuCUuaCnDwGj_iDPjRLCXD-8iTqxnj8n8GIAx6nLCdEC7Zi0ifCI2bXS-7ilXtyiMspTV2DDm_vWnj68Hf8OYlrdWSKZmFGYbVlvOv65Ju7FcjOFq7mNtWDvtIulzUGsRGoodavCFMMivGYCDafd5BIxM_j1UdsfAYMAFqJTtWWhzbAFZxZkJaEcBq0X52m8p-iUunKPNb-Ns7ID2dHwHwbUNUlgbw5Oofe4LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در یکی از پالایشگاه‌های استان اربیل در اقلیم کردستان عراق
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/677252" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677251">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| نَبض تهران |</strong></div>
<div class="tg-text">🌟
وزیر نیرو از اعجاز همدلی  می‌گوید...
🌟
روایتی از اعتماد و ایثار مردم است که در سکوت خانه‌ها شکل گرفت و روشنایی‌اش در سراسر ایران ماندگار شد....
#قرار_همدلی
|
#مدیریت_مصرف
|
#پویش_۲۵درجه_قرار_همدلی
#صنعت_برق_عرصه_تلاش_خدمت
@tavanironline
روابط عمومی شرکت توزیع نیروی برق استان تهران</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/677251" target="_blank">📅 13:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677250">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/It97SkczRQ0xmpCgGFt61TZIcuWIkcJQYnvBlvZU57aF3PKqxRglC7rNTQwtOKcE1E0OX-srmHeBZWYV_pdvA_YvBk1pcOgGM60GUMX7sNdvWIebg701F1cnqM6jp9eSeK6i4pXTElMCbujIScqwhsikhbrf8FwPhjmendTOwfSqykWIsDWydBNdg9EbsZg9-Ji5Vsa45NmYPHFP73rK3ext8MCi66O77C5hlmYAhj2PXR6e5T3uGQCAZQyZjKlO4KAJ04IfPcHarAWzBs0mmci-4TB_2waJkSjM7Jvg4vG7tENJNrrYCDPijRNFUkDBnw3DSI3xQxCj6mlqg5nlJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت روز طلا در ۱۰ مرداد ماه
🔹
در بازار طلای امروز با حرکت در محدوده‌ حساس قیمتی، شاهد افزایش قیمت طلای ۱۸ عیار و سکه امامی و بهار آزادی بودیم.
🔹
قیمت‌های اعلام‌شده از اپلیکیشن میلی، به‌عنوان مرجع قیمت معاملاتی طلا استخراج شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/677250" target="_blank">📅 12:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677249">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feed9248e1.mp4?token=vdJB-gYYwJ9cQIhEnM7s1eeo4xJuT-CHrmuB2QF1viOd4fq1QQABqVou7cFcTiBv33lezl4b-6SRWrAHw27ESlRRVRDhd6pu8fdcwouO_beM34w78EyA0rqjRUq7SEhQbjy53CQpc_BT1aL6RVf__k9tNFgMwhpv-7W06VZRTCjxr3-ldVDU3vQdVZ6ckXOzo73SKi7XTi27GJhTOOfIAfrKv52IImU8HqLTp4cMTL55pkMmlRdloLVJGR_LNckkxphhgm1TwhdM43OLJr4-PMUg2Sgj6ALQGT3xRpVc3Bl1xUHbLUs70vv5cBmSL_-wSFilaYRaUNByrDjgiRJeHo9Ls8BW5qjvd4mZa3S4OMP6n3TOrab-WH9SM0fEEWJhCctyHsC1tGbqbnpcucQMV_ZpkYyQ8aU0mFAOwR16ATif_0wa1YuvyYatVv78Ha00ZrLWLVdLqFOcL3LoOqQ5sjLgWqo7AmtrLUzFPDKCaH6VgyjEzwETw_HjK2PGi5zd2NWb88gGORcOgFUvwO1mQlyktrKTOdBBz49rYqC6M_4KEBmmSv7cufVarRCOEnhIxyrwkKKuKp6azRvkbh3bczHnL2poqNrM6sKXlYPI3ZafayGo_LEyZku_QKRix9PlpKYHPMCGkzx5J5nhSmuE8J9NT89ePJ7V6Rw6XWDD1n0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feed9248e1.mp4?token=vdJB-gYYwJ9cQIhEnM7s1eeo4xJuT-CHrmuB2QF1viOd4fq1QQABqVou7cFcTiBv33lezl4b-6SRWrAHw27ESlRRVRDhd6pu8fdcwouO_beM34w78EyA0rqjRUq7SEhQbjy53CQpc_BT1aL6RVf__k9tNFgMwhpv-7W06VZRTCjxr3-ldVDU3vQdVZ6ckXOzo73SKi7XTi27GJhTOOfIAfrKv52IImU8HqLTp4cMTL55pkMmlRdloLVJGR_LNckkxphhgm1TwhdM43OLJr4-PMUg2Sgj6ALQGT3xRpVc3Bl1xUHbLUs70vv5cBmSL_-wSFilaYRaUNByrDjgiRJeHo9Ls8BW5qjvd4mZa3S4OMP6n3TOrab-WH9SM0fEEWJhCctyHsC1tGbqbnpcucQMV_ZpkYyQ8aU0mFAOwR16ATif_0wa1YuvyYatVv78Ha00ZrLWLVdLqFOcL3LoOqQ5sjLgWqo7AmtrLUzFPDKCaH6VgyjEzwETw_HjK2PGi5zd2NWb88gGORcOgFUvwO1mQlyktrKTOdBBz49rYqC6M_4KEBmmSv7cufVarRCOEnhIxyrwkKKuKp6azRvkbh3bczHnL2poqNrM6sKXlYPI3ZafayGo_LEyZku_QKRix9PlpKYHPMCGkzx5J5nhSmuE8J9NT89ePJ7V6Rw6XWDD1n0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در یکی از پالایشگاه‌های استان اربیل در اقلیم کردستان عراق
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/677249" target="_blank">📅 12:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677248">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8JFbkNmlQxc-FZwUwOU3k7Duno7bBdvtmeNtWOl4Pg_OOb6WqXr51t2wprf9X7qm25Qm_9JIviH_mQHDeojjpTMApwsMdR5cfY2weGMnqASNgD4g--tnAoKkoybmsfqKQI9inT1708FAJDjGAKr-PYvWrrnS7QahdnyyoNJYzVQUQAtJ1bUQqo4IU2Tm18ApFIV-Bb-qkdNBuAaMCzixRo2mUXhkeXeOU5QrkYFNFMrKaUfFI7TCXBBeYip96QPJPseFR_jIXPtJV-3Ns1x-xn0EzMFgr5o19yzgnQrp31Ubu1UaQx4xmv9f0lKzL2nQHXA4V9-yLROg0Mw2PFXyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابراهیم رضایی، عضو کمیسیون امنیت ملی مجلس: اگر به ایران ضربه‌ای زده بشه، کل منطقه و تاسیسات آن را به عصر حجر برمی‌گردانیم. به نفعتان هست که حماقت نکنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/677248" target="_blank">📅 12:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677247">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8jyEmA1BMFgskLB-xzZJOXp2u_RaOL2So7J7ZI0lNRZq_Qx3t0EtO0tCxRm4PqOaXzqENYc3Wr0YwY79BOP2FcYB2qTzoTIywKL9xfunFiRcRDezpkb9bAX1DiZIr1Jw2yYbuNcZbzAsCCud223ItjdpGSg8QzaJ4JovhfRwgXBUXV6QUQBMC-huzAwhJgxHhnQaOGwsJCXJR90FWAO-q4EdKAtgLYmItUeVRGyHzj7H3a3xr65g4JgHZ_V90nSqW83fRahcj6Id3cn4hgF3Tk3VQ92HP4JbMfLnR7u00T3tPYOAegXk2hgg-stZ8bBsmgAdbWg_Ez5PJkn5jK24Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین پادشاه ایران در اروپا؛ سفر پرهزینه ناصرالدین‌شاه به فرنگ
عکسى تاریخی از اولین سفر ناصرالدین شاه قاجار به اروپا سال ۱۲۵۲
🔹
ناصرالدین‌شاه آن زمان ۴۳ سال داشت و بعدها دو بار دیگر نیز راهی فرنگ شد. علاقه او به سفرهای اروپایی آن‌قدر زیاد بود که تأمین هزینه سفرهای بعدی، با مخارج سنگین و دریافت وام‌های خارجی همراه شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/677247" target="_blank">📅 12:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677246">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
پاکستان به ائتلاف دریایی عربستان پیوست
🔹
پاکستان به همراه ۱۳ کشور دیگر به ائتلاف دفاع دریایی به رهبری عربستان پیوست؛ ائتلافی با هدف تأمین امنیت دریای سرخ، باب‌المندب، خلیج عدن و حفاظت از کشتیرانی و زنجیره انرژی جهانی.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/677246" target="_blank">📅 12:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677245">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b23215cb0.mp4?token=fncrgfF0zAZJ-44NWcfb4lpTc80Q5kgJxbDzsoqX7-GP2DxL5GkHVTjM1n_seM-Q7tiJHV0J_j8_X7TOFfyKzA9R5qNq7r2_ELyHjlwLYNejySfgieF_SINujmUjHX2dpwMON2B4AU4Y0kLGBFMhLa44QxrYSPQ1PE_qHWTE8vTJJ4BlQ6hmFQg8X4o9hJ2155zXnz5CubkbpkOdUHdW6dD9LhtIYlfrTxqhEbHzgAicSQcxLjp8ePbhV_-1lBEzyJX8b1yIOS8uxvO_d6bhdPJh4YqEG9e0TNhz6Vdebd9dLpYgYYvTS7IHYcuG5CT4YOgYI26VMkmhj8qA7W5dlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b23215cb0.mp4?token=fncrgfF0zAZJ-44NWcfb4lpTc80Q5kgJxbDzsoqX7-GP2DxL5GkHVTjM1n_seM-Q7tiJHV0J_j8_X7TOFfyKzA9R5qNq7r2_ELyHjlwLYNejySfgieF_SINujmUjHX2dpwMON2B4AU4Y0kLGBFMhLa44QxrYSPQ1PE_qHWTE8vTJJ4BlQ6hmFQg8X4o9hJ2155zXnz5CubkbpkOdUHdW6dD9LhtIYlfrTxqhEbHzgAicSQcxLjp8ePbhV_-1lBEzyJX8b1yIOS8uxvO_d6bhdPJh4YqEG9e0TNhz6Vdebd9dLpYgYYvTS7IHYcuG5CT4YOgYI26VMkmhj8qA7W5dlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨️
اینجا همه یک عنوان دارند؛ «خادم حسین»
❤️
▫️
روایتی از مردمی که با عشق، خستگی راه را تحمل می‌کنند تا در بزرگ‌ترین اجتماع عاشقان حسینی، خادم باشند.
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/677245" target="_blank">📅 12:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677244">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpmtmSAuMYubfzyi1oSIZjfG0OKSE5BzcBze6HpbB9E0OfWSvADfKXIlAO9gZww-BypEboNifW37UDYfPtcvtLfDkS4W5ZZq4n-wxs-L8Xlg6dX3EgjNx2j9UsJDZNnY86BUoO7lvb-AvYe6UzTEe3nz-zElb03twc7cfSIjvPXLTruL5xy350pZxeexuPzvTZWWF3zd3kEy3hBhsyW3avPeuP51cpUx-sLz8ydHG-zgWshTFcH0E7x8ocZbkDwA28sa7mhrOsNTUEsUVJF1xLNjmK-YrNq9yNXII-UYTP2dfgO9DszViZ1798l34gCoombn1vjAd58DJmsoFRjZSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دانشمندان راز کوررنگی را کشف کردند
🔹
دانشمندان ژاپنی کشف کرده‌اند که فقط چند تفاوت بسیار کوچک در چشم، می‌تواند باعث شود بعضی افراد رنگ‌های قرمز و سبز را متفاوت ببینند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/677244" target="_blank">📅 12:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677243">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29cc88ce4b.mp4?token=cRYsPQDpHUvhLW4xi-219vp-oOGSrHo7iYDEvsDOFfUy7ypMaJnuVajGgWfcn232l9JJSbogztR8M2gr3ZCwfhuxNP5fYMofGK6vQvmwJdBTxTjjjokikt5j5fJDs8bik5UjFBz_NMh9GFLuiagKDWnBSbcoKpRBrJlzs8aEeV-O0Vzp0W1F76z-l_f-w3VH2JQdD9ohtgxGnqX2jInH5kGdAxsPA4Aw5FCBP60HLuWXjjpCxB10nP0TC7dkGslwbXkHRboojTtMLt-8LsjQ9q0mCThYQPVGmuHYNzZfKg3ZMqcn3r9L29v6nqPDcuSsSrMVDUN7d0Shjt93EdUAyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29cc88ce4b.mp4?token=cRYsPQDpHUvhLW4xi-219vp-oOGSrHo7iYDEvsDOFfUy7ypMaJnuVajGgWfcn232l9JJSbogztR8M2gr3ZCwfhuxNP5fYMofGK6vQvmwJdBTxTjjjokikt5j5fJDs8bik5UjFBz_NMh9GFLuiagKDWnBSbcoKpRBrJlzs8aEeV-O0Vzp0W1F76z-l_f-w3VH2JQdD9ohtgxGnqX2jInH5kGdAxsPA4Aw5FCBP60HLuWXjjpCxB10nP0TC7dkGslwbXkHRboojTtMLt-8LsjQ9q0mCThYQPVGmuHYNzZfKg3ZMqcn3r9L29v6nqPDcuSsSrMVDUN7d0Shjt93EdUAyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی ارتش: برد پهپاد‌های ما تا حدی است که به سرزمین‌های اشغالی هم می‌رسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/677243" target="_blank">📅 12:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677242">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huDka3T_rAoA_idcdyR1j4TEevgbkl10Vj08YFSgzINyk8z5bojW1YWZM05kGIjT-MtN6Bgm40X3E4sYEbqvLapin2Wiqt0WKzL9B5KlFITI3O9DNmtK0blk-jbzSqzn85XdPNQqCgms9fJhcGbDLlJ3PbRgUD6TAMD-ODyHqrf1I3RD2mAcqJhqXq06xUDWw3J-3BT_LRx4pwJqtgeeMgniZGMqJ6TuCLHKaiVszjvAaQq6Mzhea7UY2qjp9tRs5bgf9QX8n6uVJRLDOqjrJeZU4MDHHJ49AuvfEs6U4mQwab8TXIRoE_RPJHpZOUHxkPeMF5wTYNuRNhEsYH41Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تأکید مدیرعامل هلدینگ خلیج‌فارس بر تسریع در اجرای پروژه‌های تأمین برق شرکت‌های آسیب‌دیده با مشارکت مپنا
محمد شریعتمداری، در نشست مشترک مدیران گروه صنایع پتروشیمی خلیج‌فارس با مدیران گروه صنعتی مپنا:
🔹
از نخستین روز پس از حمله به شرکت‌های زیرمجموعه هلدینگ، مسیرهای مختلف برای تأمین برق از منابع گوناگون با جدیت دنبال شده است تا روند تولید در کوتاه‌ترین زمان ممکن به شرایط پایدار بازگردد.
🔹
حفظ پایداری انرژی مجتمع‌های پتروشیمی در صدر برنامه‌های هلدینگ قرار دارد. تدوین جدول زمان‌بندی دقیق برای طراحی، اجرا، ساخت و بهره‌برداری از پروژه‌های نیروگاهی شرکت‌های آسیب‌دیده ضرورتی راهبردی است.
خلیل بهبهانی، مدیرعامل گروه صنعتی مپنا:
🔹
این مجموعه آماده برای ارائه برنامه عملیاتی و اجرای به‌موقع پروژه‌های نیروگاهی شرکت‌های آسیب‌دیده را دارد. با توجه‌ به جایگاه راهبردی گروه صنایع پتروشیمی خلیج‌فارس در اقتصاد کشور و نقش تعیین‌کننده آن در استمرار تولید و تأمین نیازهای کشور، مپنا مشارکت در اجرای پروژه‌های این هلدینگ را رسالتی ملی می‌داند و همه ظرفیت‌های فنی و اجرایی خود را برای تحقق این هدف به کار خواهد گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/677242" target="_blank">📅 12:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677241">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ea4aea03d.mp4?token=byY3wQzSzLoumakKeXwviphVa4J8SGRQLgH1skWqorTQ9khG1aReVV2nM-n9v-SYsXgewAJ3kanyNfOhjHk0DfvZMIJtn4LShf16DgHEZMUxAm30Z9o_tbAUuEdMRidmX9hGkSKi5fghAvLJdG0AFvM2ZkX4XLUqJLcUETGLB9mvGGBdeO1GX8LguDLBWxXatSzt0sTHj8jhJGzm1ReG0GtnAUhFNYnA8aLmkoNOcfJi64G7G-byMIx5Nx8_CEISazL8lDlA7j3nRv3nxCs95f5HwJHlwP7OzmOo0cw_5T77GKA_pVI33qwLTFZ_JieDikkDgcfOs6NUmh_kpYRp-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ea4aea03d.mp4?token=byY3wQzSzLoumakKeXwviphVa4J8SGRQLgH1skWqorTQ9khG1aReVV2nM-n9v-SYsXgewAJ3kanyNfOhjHk0DfvZMIJtn4LShf16DgHEZMUxAm30Z9o_tbAUuEdMRidmX9hGkSKi5fghAvLJdG0AFvM2ZkX4XLUqJLcUETGLB9mvGGBdeO1GX8LguDLBWxXatSzt0sTHj8jhJGzm1ReG0GtnAUhFNYnA8aLmkoNOcfJi64G7G-byMIx5Nx8_CEISazL8lDlA7j3nRv3nxCs95f5HwJHlwP7OzmOo0cw_5T77GKA_pVI33qwLTFZ_JieDikkDgcfOs6NUmh_kpYRp-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نجات معجزه‌آسا؛ سپر دفاعیِ پدر زیر چرخ‌های مرگ!
لحظاتی نفس‌گیر از عبور قطار از روی پدر و فرزندی که میان ریل و سکو گیر افتاده بودند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/677241" target="_blank">📅 12:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677240">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzUQcHEQFSHkH0YllCBJJxKtYhsvnDOkXrKAQPa2bVqB1bEiQJ4NidPprHv6MgDtxwUrtvCe-rH8DXOmKoL-cTGRB3adXZnwZ9DXNw0A6KvS_lvZZCPKc79dQdmZr-mxWuNTT_P20ksbQuWyNRm15-UlwgOUQI4reJH2tPvxbE9lpSs_OTP06HgwamrtbCzI-1vKPmf2kM4giDFw4ontUFfZPLOLMD8axqicFEBzCRlUuD0PiXmKTxkLhrKOzMZDzZcD3Y9A5r90cu9_oxui2XNXSuG9nmcSR5mJzBogJetYsTikpO9F_n6QLclEDq52D_iraC12x63yHIzbaCTTSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
فروش ویژه بازنشستگان
🔺
بازنشستگان کشوری
🔺
بازنشستگان و مستمری بگیران تامین اجتماعی
بدون پیش پرداخت،بدون ضامن و بدون چک
طرح کالا پی(بایک چک دیجیتال ۲۴ ماهه)
طرح مانیسا(با یک برگ چک)
گوشی و لب تاب تا لوازم خانگی
از ۶ ماه تا ۳۶ ماه
با برترین برند های لوازم خانگی
دوو
سامسونگ
اسنوا
هایسنس
پاکشوما
دیپونت و….
قاسم آباد نبش شاهد ۳۱ لوازم خانگی ابری
@Abri_kalaa
تماس
09914835014
09152166100
@Abri_kala</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/677240" target="_blank">📅 12:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677238">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqIaAFTMXe2IWHFV_ML7ALLgLTdtAvJXMPAI7QnoTF_I5-haEYmksnvWiH2b5zUaQ7Go-wZ-PB7Qr_MtR59pzid7-35kDC3ukr0ccjn1KqUGvwQK65LPa7EmOUR4pg6HT3Mqmqskib5fb-K-obDuAyP--oypRPOzlQ1wCwMBVMk9Sq0i-6svJvE65nHMPljRhJ4lCp1IhSlPDaXKeyVTw4fXDk0sxED4qkV1LtnIQVneQhaWUPCYRgZsG6t_xdzN3_6qllbeekMkybOT3isBMC9qAh9t05HpOJsKmhbd8_ESpIQIr-8G4Puh2AeXovcbvpdCUqNWziHSmFQqKyj6qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از 30 درصد کاهش وزن
، با استفاده از
آمپول های لاغری زیر نظر پزشک
در « دکترساینا »
🔸
آمپول‌های لاغری
، بروزترین و موثرترین راه کاهش وزن هستند که با تاثیر بر گیرنده های دوگانه GLP-1 و GIP و تقلید عملکرد هورمون طبیعی سیری در بدن، باعث کاهش اشتها ، بهبود متابولیسم و در نهایت کاهش وزن می‌شوند.
🔹
با استفاده از سرویس کاهش وزن با آمپول های لاغری در دکتر ساینا کاربران می توانند علاوه بر
دریافت ویزیت رایگان درباره تزریق دارو ، از مزایایی همچون مسیر درمان اختصاصی ، ارسال رایگان دارو از داروخانه ، ضمانت اصالت و حفظ زنجیره سرد و پشتیبان 24 ساعته
سلامت برخوردار شوند.
👈
مشاوره رایگان با پزشک</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/677238" target="_blank">📅 12:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677233">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I8fh68R3GmKS8RfUXCoOFc2IUJYwT7yA3oI_a91OtwAJqhnAuLUxUk2oAbeq5wp-DVlt1weGtb-3eQlGG6CJusXNds7jlFf86jRDeP8YXyinnux3uUDCm0NXvLCnXpAcqMA5Q9bxPkdWC1XwvBXnREZtPdeNg43D9A-fXnYCby_ldG3FQFH6gqcsPf7ic80hzc4m4eeZ2bvA1Sd1kEohhy00_k7vZFURJxcUO3HFZLlDnWRWAX8j9iIGsK8ec9sfY05LP4fFD-TGjxG6W0-k27_Xa4UoULE9HJKQQpym2K_s_gl36T9hRN9QiuBuRzCAfL3gNGtM26OkKjgZGh5KYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JGgB0C4eyajQxOCd-DWjMWfasG6X8-IyyUimic_rbQc9EQx2cE5VrOhhqtnPGLsus0pL-DbBCtaqFiHCrQy98SEA1fDkIuWueQcsQQScBhNeqpLLgW4NFTtWfV3z-lXbTWXRf49rUVMuyTKzL1VWiHEgVa1N8mrtpQnJ1TSf4a3_4SOXMU2MSdsV-qY8kYN_GxAtqVRv-H689mwxqf_qEd1fHr3K7OTZL_C3psU7LHRycg3U31QQ9DHu2nHIQaNubkRYkMlbZdLqs6yYfIeEAHbEwAd8a8IuCcvc8GaDZMoErPINdYWKh6f-yqpzxyDzHM92aJ2gjtmC5MRnDeU2fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kPPMZZ3mN2qarMBKiv2F25l8fQovCdyCGuToHDBn1SY10vlCw0BXohAmWFlIii7WeP2DFSLT1D35e15-WNqRh89LIiTkYo-bdraQHrmKC0seANmv9DJHg_leRfqQG7rdz1vLeQFAMredalIb0T6wN7G-uCsOQGj3SwQzyRnBttq6xBrUGdajyj1Wz5BiG-2gt-QL1IOBbOfnRqxCu_TUaltiwo2uFxBn93z8AJU7u7A8LNdZ9YKdX9Wh1kUtQnOM3jnSRs9z1Sjrm6My8ucRkhhzkmVDjceY28YSqrzXp7I_hWzTGon1hbJo7DymcAhIbcvXsk-KHk4E9cBNm_-Ltg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ctlVNyGJoVj1ietJWa4jxxk8nMesNkHSfSwu9W2_G7i3zuYPnHtG_NRXC0OEfe6zn8HVQcqytPY1LeDI-zp2wHW5U1bbhx6Ns3apLubugkGLsEdZn0NYEPPl19T7UXrdJl9WkQpWBvDEjXwkEG-ruaFrHGa8bZP55DrTaNkxbgIOntwNTz-yWTJ1py3SM1nCkQKPa1adlbbKvqaNcoP1ssO7l1TsNwEfS7G-Do8sojNH1Q1nfeOY7AkpmMOAxISFxIrfNzlUvLqDGFhEjyr92g9GKi6h72-zf7PniTCHfzHWg-qLMbpEEUCPbjtFyt19JYcJa9OvUi5qp_r2_tcUHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کاروان های خون خواهی امام شهید با پرچم های سرخ از حرم امیر المومنین وارد پیاده روی اربعین می شوند
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/677233" target="_blank">📅 11:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677232">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
هشدار سفارت آمریکا به شهروندانش در اردن؛ برای ترک خاورمیانه آماده باشید
🔹
سفارت آمریکا در اردن از شهروندانش خواست با توجه به احتمال تشدید ناگهانی تنش‌ها، اختلال در پروازها و بسته شدن حریم هوایی، خروج از منطقه خاورمیانه را مدنظر قرار دهند و از نزدیک شدن به پایگاه‌های نظامی آمریکا خودداری کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/677232" target="_blank">📅 11:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677231">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlJXss982gY3wRv-AfLkpzSe5DWlHBJUHg7VtZvOaFC6M2rfcG5m9rIlENqLb4M-_R6HdrECZ1-QGWIPqlfvcjvT2UdlkdEf0TNwwCuX7nGRTLMS_jOVkjxuQcV7frArqAds-D6jMfq2uGuZAuzrEBVrxkzaVOcARa84QpuqwszFSwdxWyITiI-vo4d4iyh95a7eW0CLqVCTN1tu4wHSgzz-6LioHeCbICLSppVkBP65QkVaYhLYKjujyIvHn4gmtf-ZkMhBqxhYYE-iG3c53weozpCqBc1NZWeMWH9p_v6FE5yK2_v8erO7zxrIHNVvcJaYXJb0Ta4iMnYVUFN3eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دو هفته پرتعطیلی در پیش؛ فعالیت‌های اقتصادی با وقفه مواجه می‌شود
🔹
با تعطیلی روز سه‌شنبه و همچنین تعطیلی سه روز پایانی هفته آینده، عملاً بخش زیادی از فعالیت‌های اداری و اقتصادی در دو هفته پیش‌رو با وقفه روبه‌رو خواهد شد و بسیاری از امور و پرونده‌های اقتصادی تا پایان تعطیلات به تعویق می‌افتد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/677231" target="_blank">📅 11:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677230">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCO6CjsnrMZQJVaymOI9ZTsRAZd0gaWJ6JmuQvodAEsL1DgAUA4BYarVJk6oefX7sKkSt9773l9PCdel_KZVZsFsIQQjP7as-VWEdbzsb57e-KZxxe-i6vHG1UlANmBrEwIuhz0J5La4VRYq4kyc1wby1dhFAUHaBmJ5wwZkdBJoRkdBDJgz8PBj53b_Zfk4A5HLVlo5zscRkKN_46YRRBwKiAK3CIaPUeiQYNibGSIGoFAuW6ZTPDJwES66VFsVUi_MLvlx8HtmsP2RMaU8hPg6K-exML7o1WjSoMViZBy8k9Jec86eI0FhOqayNI-yRvtafIKC14JT6WcGdv7cYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت خبرنگار خبرفوری از جنایت شب گذشته ترامپ در قشم/ حضور در خانه‌ای که شب گذشته در قشم هدف حمله موشکی آمریکا قرار گرفت/برخی از اهالی که خانه‌هایشان تخریب شده در سفر کربلا هستند/ خبرفوری @AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/677230" target="_blank">📅 11:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677228">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egpvNxKepmbK08FIs0Dq9jl2UKCWP8C4Lke-A1tbOKNqILu29ZJq1L25qTj3BIOrqxFAZuubWpcZ9kSnWjHe5-4dDnZLRqRyf5awleuLJFVIiaukB8crsa_Hjc_U5V1haE6QOj2nicFI-0jjIPM5voE-7X00PnqAAOZ2u3nxidSUCFz0kBoQQ6LDA7BIUw-2uvNE_mmwe54zDv0Ol1K0eRBjav4C8NOGbedQtpEhcvXF3SpzH-dW2z1ZtMANLgQidapAo_xSiJCWqFxTs6qSxnG8SU_Ykkg-qyrgrpxa2khXQS1lk8K5vfj5Isuy85q-x5ZttxbVoeg6YcKJ2ErrHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨️
احترام به سالمندان، فقط یک ادب اجتماعی نیست؛ بخشی از فرهنگ مسیر اربعین است.
گاهی یک همراهی کوتاه، خستگی یک راه بلند را کم می‌کند
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/677228" target="_blank">📅 11:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677226">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53b26cff82.mp4?token=cuF2Twys7NhbJtvbtkKQZW2W9bf5JgfIczegKUJxrrzHf3uOEnIALEnFjRcOb_HyZRAXuYbd8kysp1KcgSROifG-YPnFmXGTu31KOkIpSjzzGff_Mgvc2ezOJQ4VyD0hBZBVAil8uM1ifNGrLs1R_iqeEr7nzQN2-Q0EIZ7gDIgt6-vU2ww81qBdWw8gIYs-2bAm1WEg0KHkBNhGFVaxZjjzSEGSRwRVJk8BVXfoZd934aPdz3Rd9Enxi1d0AEjI8OjINqAyjHKhrmIX0Ox0vwXoohqPcscyTGdjyRtwPYu_4plt7ezWLiY6seWPj_a0SyB2N7Jae3j96iSlcu_sjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53b26cff82.mp4?token=cuF2Twys7NhbJtvbtkKQZW2W9bf5JgfIczegKUJxrrzHf3uOEnIALEnFjRcOb_HyZRAXuYbd8kysp1KcgSROifG-YPnFmXGTu31KOkIpSjzzGff_Mgvc2ezOJQ4VyD0hBZBVAil8uM1ifNGrLs1R_iqeEr7nzQN2-Q0EIZ7gDIgt6-vU2ww81qBdWw8gIYs-2bAm1WEg0KHkBNhGFVaxZjjzSEGSRwRVJk8BVXfoZd934aPdz3Rd9Enxi1d0AEjI8OjINqAyjHKhrmIX0Ox0vwXoohqPcscyTGdjyRtwPYu_4plt7ezWLiY6seWPj_a0SyB2N7Jae3j96iSlcu_sjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
‏
احمد ایراندوست این ویدیو رو  پست کرده و گفته تقدیم میکنمش به روح عمو اکبر (عبدی)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/677226" target="_blank">📅 11:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677225">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e3f1f9f26.mp4?token=M11Y8WtgzvsgqSfQKawUk9YfiQCipzlfktdKE36JffPXPbknPO0WyptNkNe9g0DahjHrKXof-9rXTwtVgpxTQ2yF-krmx4ITetRVL_5VplGjTao6ymy0y7BzTD1_mWc8hhBgAad8nZPkWolGgldv8YSEB9axUdC4RVzfATtdtMPEYpCsx_GdHueVlB3NagNZ_OwFO7BEgmIXkVLL0QTmO39-m04N3vsfUq-_uJOfy2_DGpTk7osoE-Ah5yViBFTrdq_KrjIt4W6LZN0IRy7jDLN23qZBQQzOZRdubcpLJTvlpz9P0jxXBi76Tl_vvA4zhZmq5pOUPEmt80qZORZzrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e3f1f9f26.mp4?token=M11Y8WtgzvsgqSfQKawUk9YfiQCipzlfktdKE36JffPXPbknPO0WyptNkNe9g0DahjHrKXof-9rXTwtVgpxTQ2yF-krmx4ITetRVL_5VplGjTao6ymy0y7BzTD1_mWc8hhBgAad8nZPkWolGgldv8YSEB9axUdC4RVzfATtdtMPEYpCsx_GdHueVlB3NagNZ_OwFO7BEgmIXkVLL0QTmO39-m04N3vsfUq-_uJOfy2_DGpTk7osoE-Ah5yViBFTrdq_KrjIt4W6LZN0IRy7jDLN23qZBQQzOZRdubcpLJTvlpz9P0jxXBi76Tl_vvA4zhZmq5pOUPEmt80qZORZzrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هوش مصنوعی به کمک ربات‌های نظافتچی آمد!
🔹
ساعتی ۳۰ دلار میدی خونه رو برق میندازه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/677225" target="_blank">📅 11:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677223">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159deb788d.mp4?token=LTDnQahIgB9mFIuJWVopNwn1LYKeQHILtnON1D-Rx3TtWzHFyi43puPQotNqE-eJoQjY2kYqy3tvXKyKORghFx8N8Klah9yaPDt3bKfZf5zEDeh7vcwMD8CUfG_k45kvHRi7j6ze7lpty3sWkAAXMucef_PIROUsfhgQpT7kRVWwirY7hCKpm3Hf_sDZsoyc7CAB2Yyo_x9FQG4r-5la9qwKdWhhI3iULBK8T82TjFVADiF_OBACEuvt-El9VtRDCA33Rh95QK8tPC6lgewoo8DIQEaOgVH3UDak8MF9UWnDFfQ7MhqXZ36cRK4U-lKZS1AmYCEEuNfSvxtaLazGIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159deb788d.mp4?token=LTDnQahIgB9mFIuJWVopNwn1LYKeQHILtnON1D-Rx3TtWzHFyi43puPQotNqE-eJoQjY2kYqy3tvXKyKORghFx8N8Klah9yaPDt3bKfZf5zEDeh7vcwMD8CUfG_k45kvHRi7j6ze7lpty3sWkAAXMucef_PIROUsfhgQpT7kRVWwirY7hCKpm3Hf_sDZsoyc7CAB2Yyo_x9FQG4r-5la9qwKdWhhI3iULBK8T82TjFVADiF_OBACEuvt-El9VtRDCA33Rh95QK8tPC6lgewoo8DIQEaOgVH3UDak8MF9UWnDFfQ7MhqXZ36cRK4U-lKZS1AmYCEEuNfSvxtaLazGIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی قابل تأمل از دختری ۱۹ ساله که در این سن دهمین عمل زیبایی خود را انجام می‌دهد...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/677223" target="_blank">📅 11:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677218">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffd47e5f7f.mp4?token=CDsFxNyZLomLLAOzBhaSs1KAPuvXMV9mFBbKM8FUyac10ghZxK2g9RJFiIWmMCvSko6XFUQc9lq3o4zxlwL977qLMJIT_L-pwmiVWNu4oufvxFViHs2aheaG8gg1jwrf35E8w0Di27ZqpN__m3iJX_pqaPk_5SZQyWd5J4i0uebz87YVlYwT9W-yCZKKSooutnGyVPnkC68ls7icngVS9LuyBcQfWq0AZdWvSum00tgEqpy0yoH8zw_s0eJo_ifqPA45rDLf2M0c77BQ6m2iVtJAAiCi7W23XkRjnJ2gR6Qd71h2g6QGeX0mnXqC498wkyP2svq36D3eF7omXAXpFDpMRu-vEW0rQ4pheQK8q-ECcf9_Mjs5bPiDA1S7wL3z19P_DHcEVI6GrwNh2zc-fnY0ywsi7mj1Mdajhlhidyqu7JNurZDMa_GJ-jseHn_Q0PcQsePeJsdrahtQRWZ742f2u_KjOrKYWRL_e7uFnRAIePAx2W0jub-j8hPC87YzmclGkjQ_2Zbu0Ilc4UT0CKUUJ9YFv8IymDbcSAQPBWuFqRL0uZgxlBDh0Iug01D9TXMGsa_B7ZAy5LPp05y1kqhK3HychubaN3_Xm0q-OiVFwWUmwEczx0iP8QUQxXX8UJPUs_6okpXcgyXkq-FpdgdW5YfJ8es7cptWZ0Kntls" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffd47e5f7f.mp4?token=CDsFxNyZLomLLAOzBhaSs1KAPuvXMV9mFBbKM8FUyac10ghZxK2g9RJFiIWmMCvSko6XFUQc9lq3o4zxlwL977qLMJIT_L-pwmiVWNu4oufvxFViHs2aheaG8gg1jwrf35E8w0Di27ZqpN__m3iJX_pqaPk_5SZQyWd5J4i0uebz87YVlYwT9W-yCZKKSooutnGyVPnkC68ls7icngVS9LuyBcQfWq0AZdWvSum00tgEqpy0yoH8zw_s0eJo_ifqPA45rDLf2M0c77BQ6m2iVtJAAiCi7W23XkRjnJ2gR6Qd71h2g6QGeX0mnXqC498wkyP2svq36D3eF7omXAXpFDpMRu-vEW0rQ4pheQK8q-ECcf9_Mjs5bPiDA1S7wL3z19P_DHcEVI6GrwNh2zc-fnY0ywsi7mj1Mdajhlhidyqu7JNurZDMa_GJ-jseHn_Q0PcQsePeJsdrahtQRWZ742f2u_KjOrKYWRL_e7uFnRAIePAx2W0jub-j8hPC87YzmclGkjQ_2Zbu0Ilc4UT0CKUUJ9YFv8IymDbcSAQPBWuFqRL0uZgxlBDh0Iug01D9TXMGsa_B7ZAy5LPp05y1kqhK3HychubaN3_Xm0q-OiVFwWUmwEczx0iP8QUQxXX8UJPUs_6okpXcgyXkq-FpdgdW5YfJ8es7cptWZ0Kntls" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت صاحب خانه از لحظه سرقت طلاهای خود و نوه های کوچکش با شمشیر و تبر
گفت اگر طلایی پیدا کنم که مخفی کرده باشید شکمتان را سفره می کنم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/677218" target="_blank">📅 11:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677213">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29749a0fae.mp4?token=S-3NomBGwxpGpn_FJszs3ISPuZXcFjL1FghsVGtta0kskQtdu2zjbed2CvBNOSurzZG5wpL0h3PYvt5vCgvW7FaaN1q8lPdMw0fjOkH5KTw_gBWlUMG1NpKtGMIkB_h_Au3ukFfsnsj4IAy9j4RzXkyM-qAdieE0GW1P8huWgfJVLmOqQLj_9AzutTTgUc1KqltZ5aLSTBMU_zw3KbeJbnpvndh58si4iyf9jBkyAn4hi8vckerY9BcfEjzf7NfY9r1aDsgrGqDlBFdtm4H-KFdcrZ3qMjiUx2JOahOA6cpMrQ6JtaX5ykZjpQ2F9_lMKYF5Wsd2AvbzJcH9i3pXkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29749a0fae.mp4?token=S-3NomBGwxpGpn_FJszs3ISPuZXcFjL1FghsVGtta0kskQtdu2zjbed2CvBNOSurzZG5wpL0h3PYvt5vCgvW7FaaN1q8lPdMw0fjOkH5KTw_gBWlUMG1NpKtGMIkB_h_Au3ukFfsnsj4IAy9j4RzXkyM-qAdieE0GW1P8huWgfJVLmOqQLj_9AzutTTgUc1KqltZ5aLSTBMU_zw3KbeJbnpvndh58si4iyf9jBkyAn4hi8vckerY9BcfEjzf7NfY9r1aDsgrGqDlBFdtm4H-KFdcrZ3qMjiUx2JOahOA6cpMrQ6JtaX5ykZjpQ2F9_lMKYF5Wsd2AvbzJcH9i3pXkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت پرده زندگی عجیب مالک میلیاردر تلگرام
؛
پاول دوروف: نه خانه دارم، نه قایق، نه جت!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/677213" target="_blank">📅 11:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677212">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJwYxiyWQdZydmW6h2OPZA2as455EygIoQAU3iGUhfVmwt1ZxqzOOHDjSjR4tE8Kv-74hrchnlfbkod6bv5kK2hvzTfQVFVAyPOx23tBbGLl9egDC0HpfFMwfi4t1JPPL_OKnhop3FSNhL9DMYwIUH9Tsy4Je2Av6NX6rxKoAgJCrCO6E-6RIk6F8mXaBxMsboRlnNc5zE_pB7s5hSbGDxVygOggX2rVGq9kspzXUXriM0S0pzPAe8YTlBQCVsJQDQTmYKFI7m19LqlwBG1ADRtS6plW87EDHaN4LNuGCr4yO51KFP4tmwP-xxHmQxTFw6lwNYMJK0Qrs9C01W24fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش چشمگیر ذخایر دفاعی آمریکا
🔹
به گزارش فاکس‌نیوز، ذخایر موشک‌های رهگیر پاتریوت آمریکا از حدود ۲۳۰۰ فروند به کمتر از ۸۲۷ فروند کاهش یافته است.
🔹
ذخایر سامانه تاد (THAAD) نیز از ۴۵۲ به کمتر از ۲۷۸ فروند رسیده و جبران این کمبود دست‌کم ۳ سال زمان می‌برد.
@amarfact</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/677212" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677211">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a694ba76.mp4?token=ufM6GiGljgAFvHSg52Qm1eLwKQqoTEKESbpEiGszbpE-K3l3DGAPcpl7fRnLvogU5eihe3xACvbPETbanND8hF80GHbG8NUhLxn3Y9ynh-ryfFCp6IvRHt6uHmFaGQSR9nCTUtPe2dVtz1qQM7QjzawkKKaIhXZR7of8Azphwy2dVfxqlWA3GYuyE6Xpnjo9TUOUykNrAD7VV2K-QLa3TWILjFlVNKc3J4zwVt-LCV4HKTgc6Qv5yW-lA3qyXDe6uPKRj1SlWaV8AR1rqjTh3ZDrbBeLApWOUSSjSK1-hiTb-13-iIvUVHOiTePB1BW87tEb3rBZvGuy7Ly5-dbslQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a694ba76.mp4?token=ufM6GiGljgAFvHSg52Qm1eLwKQqoTEKESbpEiGszbpE-K3l3DGAPcpl7fRnLvogU5eihe3xACvbPETbanND8hF80GHbG8NUhLxn3Y9ynh-ryfFCp6IvRHt6uHmFaGQSR9nCTUtPe2dVtz1qQM7QjzawkKKaIhXZR7of8Azphwy2dVfxqlWA3GYuyE6Xpnjo9TUOUykNrAD7VV2K-QLa3TWILjFlVNKc3J4zwVt-LCV4HKTgc6Qv5yW-lA3qyXDe6uPKRj1SlWaV8AR1rqjTh3ZDrbBeLApWOUSSjSK1-hiTb-13-iIvUVHOiTePB1BW87tEb3rBZvGuy7Ly5-dbslQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاحالا نوک قله دماوند و کاسه قله دماوند رو دیده بودین؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/677211" target="_blank">📅 10:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677209">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/178ccbb251.mp4?token=iRVvr2geT3OqHzzVP5wUu0-8RYB7Sc0P6FrTByYpfvQLTl-E2btdWiE47ilhUpZH52dh5uRF2-Gy6wlMud3sye12c3f-pEQ9AxHrPD4lBbFFfrV76XwNo1vWxmfQuNZSbj1xow9xGcXDaqxybCGqlYfFZ3BAmkZ0psxX46OZx_r2HeePNAykB26Hh7SXvleWum7BGcxVtaLlYeY4a2LKPAZA_PeVBQQOKFPkmI2qy04WZPlHAlBH7Pu3o_KQ5-SN5Xig0yvmhF7eI1bOrFhwCBVP9ILt5EVvXalyVJ3ti2aTr8_Sq2aB-c9eW382x2lpen9evmCDO0owBz72lPaC6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/178ccbb251.mp4?token=iRVvr2geT3OqHzzVP5wUu0-8RYB7Sc0P6FrTByYpfvQLTl-E2btdWiE47ilhUpZH52dh5uRF2-Gy6wlMud3sye12c3f-pEQ9AxHrPD4lBbFFfrV76XwNo1vWxmfQuNZSbj1xow9xGcXDaqxybCGqlYfFZ3BAmkZ0psxX46OZx_r2HeePNAykB26Hh7SXvleWum7BGcxVtaLlYeY4a2LKPAZA_PeVBQQOKFPkmI2qy04WZPlHAlBH7Pu3o_KQ5-SN5Xig0yvmhF7eI1bOrFhwCBVP9ILt5EVvXalyVJ3ti2aTr8_Sq2aB-c9eW382x2lpen9evmCDO0owBz72lPaC6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جمهوری تا ابد اسلامی میماند
🇮🇷
به حق الله #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/677209" target="_blank">📅 10:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677206">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/549b63786a.mp4?token=KnMtT3YzHFLzk_y16CcF9fuhxkruuv5jp8zA0BjxheQvrcdoKlvn4F6uJw2ckZiGmYJOEbrBEi3wuoXcOiThsCtohqEXRn1GnrLakc_meScshzSaU7AXEm0Q0t6Gv2g4Apzwb95-ig3CpmBCFkBtyDtwWp-gM40zIg7PU97bcQUcvY3vJ-KGm94ILzQdbwRAK0VEcC4siO3FTm-xrLh4lPLDEd-FG1ONPE-Qai32AKK4cK73nghUuNSr2C_OETwp81Lu4vjFXx2I7WVx6NGM2yqBHkkxcWRm9EpmbCebzLIsRSUkuWKKmFmFhD2WbnKfipQsy8jNTDnKUh4slUtd5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/549b63786a.mp4?token=KnMtT3YzHFLzk_y16CcF9fuhxkruuv5jp8zA0BjxheQvrcdoKlvn4F6uJw2ckZiGmYJOEbrBEi3wuoXcOiThsCtohqEXRn1GnrLakc_meScshzSaU7AXEm0Q0t6Gv2g4Apzwb95-ig3CpmBCFkBtyDtwWp-gM40zIg7PU97bcQUcvY3vJ-KGm94ILzQdbwRAK0VEcC4siO3FTm-xrLh4lPLDEd-FG1ONPE-Qai32AKK4cK73nghUuNSr2C_OETwp81Lu4vjFXx2I7WVx6NGM2yqBHkkxcWRm9EpmbCebzLIsRSUkuWKKmFmFhD2WbnKfipQsy8jNTDnKUh4slUtd5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
توصیه استاد فاطمی‌نیا برای جاماندگان اربعین
@Heyate_gharar</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/677206" target="_blank">📅 10:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677204">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
همشهری: بستن تنگه هرمز کافی نیست؛ باید با ناامن کردن منطقه خزر راه نفت اسرائیل را در منطقه قفقاز و جمهوری آذربایجان بست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/677204" target="_blank">📅 10:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677203">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PspY-5DZVwI-fsu4_N6iOkd4jXFp88hiv_X6_obPXIMVVmnQr1_hzQu2bE_oYz1gL3uCLpFX91JS6uvP44ovXANgmwxj1u7OOeUQXKpFhiiOlMjZqWEl0a22LOsfKG6eksXFDTV7guKLJly_sQuNtaaGub_n2ka_3HcbOQ4P_pkzSAxyg76hVGnO1XEjZ_Yk3OQDcpnw-DII-flouQu2ZwN6A3-o8mfGyRwK7IcDYyyMAYcHl3RZg0mVpVmgWK1PqVZIt6oJDfWRlyR8nrYRYHRTO96Cq5KYKWOsWflWH7EVWkquug7zbTkyYP7TgBs0rRcwNOtWhsY8JCHX1wX6xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رفیقدوست: امام من را صدا کرد و گفت بمب اتم نسازید / تنگه هرمز آبراه بین‌المللی نیست / جنگنده هم ساخته‌ایم و در حال تکثیرش هستیم
محسن رفیقدوست:
🔹
وزارت اطلاعات حدود ۱۰۰ گروه نفوذی را شناسایی و دستگیر کرده است.
🔹
هر نقطه‌ای که از آن به ایران حمله شود، هدف مشروع محسوب می‌شود.
🔹
ایران در حوزه موشکی جزو قدرت‌های برتر جهان است و جنگنده بومی نیز ساخته شده و در حال تولید است.
🔹
در حوزه دفاعی به خودکفایی رسیده‌ایم و نیاز چندانی به خرید تسلیحات نداریم.
🔹
تنگه هرمز متعلق به ایران است و آبراه بین‌المللی نیست.
🔹
امام خمینی به من تأکید کرد بمب اتم نسازید؛ چون سلاحی غیرقابل استفاده و نابودکننده انسان‌هاست و به‌نظر من دکترین هسته‌ای ایران تغییر نخواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/677203" target="_blank">📅 10:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677199">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e46502dce.mp4?token=oR01w2krdwoRm30AuTw78m8xxchXgvKzLWU4ZVv-wLRctut5QV_-JFDwdhAwTN10j061fc5BXxa61xVCfnBHI3M8yJ8kJP0YTbk6veBtQYxDyaqc4rzFWsrjYbwn4-uPd8SBRyqpBUAyqNWynKCKp2Xni-Z8I75HtLQdBqncq37I06YmLB6LERFst0IePzTV5usNvcLfLJo1gmo2PApoRb11aVJtvcMVf5NIvo-_H5S_KxblOE-xjAR8JMasSGStvU39RPnJbPnx4bKc_ZrWSO4zimP092rHPJo9oNqYSfS57d8iFKljdOap6PO1PQ3xrXLkumie7Ox-2ptKsEaYJ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e46502dce.mp4?token=oR01w2krdwoRm30AuTw78m8xxchXgvKzLWU4ZVv-wLRctut5QV_-JFDwdhAwTN10j061fc5BXxa61xVCfnBHI3M8yJ8kJP0YTbk6veBtQYxDyaqc4rzFWsrjYbwn4-uPd8SBRyqpBUAyqNWynKCKp2Xni-Z8I75HtLQdBqncq37I06YmLB6LERFst0IePzTV5usNvcLfLJo1gmo2PApoRb11aVJtvcMVf5NIvo-_H5S_KxblOE-xjAR8JMasSGStvU39RPnJbPnx4bKc_ZrWSO4zimP092rHPJo9oNqYSfS57d8iFKljdOap6PO1PQ3xrXLkumie7Ox-2ptKsEaYJ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاج حسین یکتا: قرار نیست قصاص و خون‌خواهی را به ظهور موکول کنیم/ ما خون‌خواهی و قصاص را مقدمه ظهور می‌دانیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/677199" target="_blank">📅 10:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677197">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec63f82889.mp4?token=HOPifC_iXluhIVCQ9gcLCc8riOv0TcfG2eBwGm-8eJLUIhxYtEGIflaXWsGENUjy2JZUPwqKlEj8Eu8HVnz4vjrWILHdOFdcINKI3_Bv7Hx76rlpQp6bfYwfnpRsrE_o5rdBL3hk4YRoDHce3_8-ps9Bd6O5PQLJe4o6dHAM1nxw3wyQbchnNTtKPotg1wD2h4YCk5GWhj0kWgXfd-b_OlF-QeFidkFIhoOQzMKnt4Fm6TAngzhjbyzGMejo5UK_YsFYoO4b7iKq0xctCUrwBautacqTOQOtRBjgwFL1mfzLxtx36kABnQJzUWu9_0kxhiVOU9jWyg-25djA2mXo_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec63f82889.mp4?token=HOPifC_iXluhIVCQ9gcLCc8riOv0TcfG2eBwGm-8eJLUIhxYtEGIflaXWsGENUjy2JZUPwqKlEj8Eu8HVnz4vjrWILHdOFdcINKI3_Bv7Hx76rlpQp6bfYwfnpRsrE_o5rdBL3hk4YRoDHce3_8-ps9Bd6O5PQLJe4o6dHAM1nxw3wyQbchnNTtKPotg1wD2h4YCk5GWhj0kWgXfd-b_OlF-QeFidkFIhoOQzMKnt4Fm6TAngzhjbyzGMejo5UK_YsFYoO4b7iKq0xctCUrwBautacqTOQOtRBjgwFL1mfzLxtx36kABnQJzUWu9_0kxhiVOU9jWyg-25djA2mXo_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایتی تازه از روز حمله به محافظان احمدی‌نژاد
🔹
ابهام‌ها درباره حمله به محل اقامت محمود احمدی‌نژاد و هدف قرار گرفتن تیم حفاظتی او همچنان ادامه دارد. به‌ویژه پس از انتشار گزارش‌هایی که مدعی شدند آمریکا و اسرائیل سناریویی برای خارج کردن او از ایران و بازگرداندنش به قدرت طراحی کرده بودند.
🔹
حالا عبدالرضا داوری، مشاور پیشین احمدی‌نژاد جزئیاتی تازه از روز حمله، وضعیت محافظان و اتفاقات پس از آن روایت کرده است./ هفت‌صبح
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/677197" target="_blank">📅 10:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677195">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
آکسیوس: حملات جدید ممکن است با مشارکت اسرائیل انجام شود
آکسیوس به نقل از یک مقام آمریکایی:
🔹
ترامپ به‌طور جدی در حال بررسی آغاز حملات علیه اهداف انرژی در ایران طی روزهای آینده است، اما هنوز دستور نهایی برای انجام آن را صادر نکرده است.
🔹
این حملات همچنین ممکن است برای نخستین بار طی چندین هفته، شامل مشارکت ارتش اسرائیل نیز باشد؛ و چنین تشدیدی احتمالاً به حملات موشکی ایران علیه اسرائیل منجر خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/677195" target="_blank">📅 10:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677193">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b451f88a68.mp4?token=SOJNALZ6_Ni7en9uHaPAfK3jdCuhg0_wBB8gnEY6je4H9ZPyFvNcPjXPtbpK2l7E8-i8glmuM00F6VTztu883lRANuwOv883DMb-O280Iav_sDIgH3KQKs19OBZAqjcKpC6mLIPfqnK1jr-TA5ng3jZjgXPkKO7LdUQ_BF7iTfvDHvJ4O5HeLl1GuyJwffphqvy-HbaDBgYZ0_htY4C-_Ll_X41xjDQTr6muh87een5a9UdoVoi-fRaAGE7q7fdUDjnPRUSc2NojizeicSsYkyIbko_6SaaoDTtgEMf4XRCRNwxrLAL9LL8klig7uRca-CA4RpC4b3df8rElDwjGZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b451f88a68.mp4?token=SOJNALZ6_Ni7en9uHaPAfK3jdCuhg0_wBB8gnEY6je4H9ZPyFvNcPjXPtbpK2l7E8-i8glmuM00F6VTztu883lRANuwOv883DMb-O280Iav_sDIgH3KQKs19OBZAqjcKpC6mLIPfqnK1jr-TA5ng3jZjgXPkKO7LdUQ_BF7iTfvDHvJ4O5HeLl1GuyJwffphqvy-HbaDBgYZ0_htY4C-_Ll_X41xjDQTr6muh87een5a9UdoVoi-fRaAGE7q7fdUDjnPRUSc2NojizeicSsYkyIbko_6SaaoDTtgEMf4XRCRNwxrLAL9LL8klig7uRca-CA4RpC4b3df8rElDwjGZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تغییرات ظاهری و کیفیت خودرو برندهای بزرگ دنیا از گذشته تا امروز
👌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/677193" target="_blank">📅 10:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677191">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNeAK6bnT9kvOaD71FjvBCZlsbUnibn1gOsqXjFfzHfz6Irs9xTCSpzMLBhBpfN8vD5pZKWRb-xC_d1FFrw6s_5Iv-iPMg7v7Wl_yeqXUnNlHQRIkPV0_gDCAZO4zDCFQbI2B79Qy4RGW5Hq9lGEJcR6kUInI7sjg34DqlH565XFLKlczwyLDQfPiC-Of1hxo_zb6NsfhpjiHJdOVW6UaYo2ZB1Yj8RXpxtvWg5qMmWBir9p7YzZxrX0qlUvcykhZ-nsbtK8xyxaQNzxEtJnq0TMK9G2Zgx0YdaktZdnCjRi7iywSMUGubKDRpGlYSQJOPyBRfLkrFplnGZH42SAoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از شهید مصباح‌الهدی در کنار رهبر شهید انقلاب
🔹
این عکس متعلق به آرشیو شخصی خانم سیده هدی حسینی خامنه‌ای است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/677191" target="_blank">📅 10:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677190">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAkvDd38rDthSHG4WFwPUh2dgIRs47QOGwMhKagUCwtFx1o5GGLuxGMyGFGPe1zC3PwLyBO51nnPL3GDf_ugoALrHeaG77hgW7O7Ch4GOMBsILk-EP3YzhNPDAXQl4yOsBtaDG1MJsUlByHPCjZEtHVPsgerwbNr8xse6NOz_hrtGw2gm-jeaPj1GZjqyWNSFquiaQVy2DDyatBb3Dc2jUlLCPME5jTucJInBvRTsHPNWQfeIke5NL5pj7KatIqKch18t3Oz46RxGBHyeQ6qvk7mive7z0Z7hJ8UxxSYDhXUO_BTWolenLbdnoFabGSB5zJapEQTtnbJ4pRxVGUzxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فقط با سه قلم مواد، یک دسر فوری و کم‌کالری درست کن
😎
مواد لازم:
🔹
دو لیوان طالبی خرد شده
🔹
یک لیوان شیر (پروشیر)
🔹
یک لیوان آب گرم
🔹
یک بسته پودر ژله بدون قند #آشپزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/677190" target="_blank">📅 10:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677189">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a02884086.mp4?token=MmKazSkW76Zht2rwxl1Uzwnd0lFSjxu4Bw8V-JPFIrsbmO1N4FTFh0Dwa7m1tbIGm3SLsBaXdsXfL0-dNSRB7A9_wln4CHRq6m9rV2TZpfaeTe5DRzJ-RQ2y03cPxFFaUnHyqUgSVJ6SEBOXAmm_VonRI-2NIKEsgnkkzxu40RDDLEUUJIS8wksshiJFYUgHC6DFr6PDMz2t7aK8jBIVkbddIXG_lQmMKru2tY2gjoh9zbSRW5GzamluswcWuLRwlmpen6Ebzot2M1AHBNg5pwCWTYfWkdbSbOMDBjeEnZADtPapZczXjD6K4w9bKGtyVjSbnhvmPDpJ6a-VIOI-iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a02884086.mp4?token=MmKazSkW76Zht2rwxl1Uzwnd0lFSjxu4Bw8V-JPFIrsbmO1N4FTFh0Dwa7m1tbIGm3SLsBaXdsXfL0-dNSRB7A9_wln4CHRq6m9rV2TZpfaeTe5DRzJ-RQ2y03cPxFFaUnHyqUgSVJ6SEBOXAmm_VonRI-2NIKEsgnkkzxu40RDDLEUUJIS8wksshiJFYUgHC6DFr6PDMz2t7aK8jBIVkbddIXG_lQmMKru2tY2gjoh9zbSRW5GzamluswcWuLRwlmpen6Ebzot2M1AHBNg5pwCWTYfWkdbSbOMDBjeEnZADtPapZczXjD6K4w9bKGtyVjSbnhvmPDpJ6a-VIOI-iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاکم بحرین خطاب به ایران: حضرت محمد(ص) پس‌از قرن‌ها تاریکی در ایران به آن عمق روحی، انسانی و معرفتی بخشید، بخاطر تشکر از این کار حداقل دیگر به بحرین حمله نکنید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/677189" target="_blank">📅 09:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677188">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1047710156.mp4?token=T23ZrMT3Z7V5TQCbECa2q7Yao7QTwsEzooV16PC79AKt1dfpyVmlRAl4_6dJAsEfLqHgjZxfwoQzxN1ycDKpVt7YcU5fv6PPLzfbtxU7UQB5frKDDDBvjHrWsMlVLxnXMZb0a5YYtyO9Jr-gqkuyOoB9ga9R1PL5dfKsSh9FgAngkjbrL69yYDl4EswPvc6TFlz6f1MWQGrAgOyI6TXmq4PfYnx5mRX2Eae5bqTv7ITZjIAxVl6WSXK9BAL1oKV0KbQR_YNGpEFJhpy5NboMhBsoxt_HZFlIs3G0JbXFiCFdCSizZKFiWWHyrMoj2NCyZ1pm_GSeL3vozWGFL17AW00ep_n9nSDuQn-FhmbGVl6DA7eBeII0N2HenkqWqwsqnHMGgheu-VBQd11onXoTxPDYn7gDxStPtvy4XkUWPerzCdyGj_Be1u5-nwAwZSY0bWZs0cS_bwELGDMHnC0itVgCZyVf947rzq_TxG5w5dFt3QGB-Y7nUB3ip90oBE9drOqiv1Lc1QkxjrWC-stJ8YRFyCGRG67XvvGjvSwxEJh-Dhlp8Cawzl9A0f4OuYcAg_R8cTIo7Ei3in2dktvi479I_-R60cabv-jRX0QDfx5hepwGAcv6LpTh4FTyhyIcS9KCUjz18DG3pVKOQl-BmcdUfHP1YIE-rYGvhmc1JC0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1047710156.mp4?token=T23ZrMT3Z7V5TQCbECa2q7Yao7QTwsEzooV16PC79AKt1dfpyVmlRAl4_6dJAsEfLqHgjZxfwoQzxN1ycDKpVt7YcU5fv6PPLzfbtxU7UQB5frKDDDBvjHrWsMlVLxnXMZb0a5YYtyO9Jr-gqkuyOoB9ga9R1PL5dfKsSh9FgAngkjbrL69yYDl4EswPvc6TFlz6f1MWQGrAgOyI6TXmq4PfYnx5mRX2Eae5bqTv7ITZjIAxVl6WSXK9BAL1oKV0KbQR_YNGpEFJhpy5NboMhBsoxt_HZFlIs3G0JbXFiCFdCSizZKFiWWHyrMoj2NCyZ1pm_GSeL3vozWGFL17AW00ep_n9nSDuQn-FhmbGVl6DA7eBeII0N2HenkqWqwsqnHMGgheu-VBQd11onXoTxPDYn7gDxStPtvy4XkUWPerzCdyGj_Be1u5-nwAwZSY0bWZs0cS_bwELGDMHnC0itVgCZyVf947rzq_TxG5w5dFt3QGB-Y7nUB3ip90oBE9drOqiv1Lc1QkxjrWC-stJ8YRFyCGRG67XvvGjvSwxEJh-Dhlp8Cawzl9A0f4OuYcAg_R8cTIo7Ei3in2dktvi479I_-R60cabv-jRX0QDfx5hepwGAcv6LpTh4FTyhyIcS9KCUjz18DG3pVKOQl-BmcdUfHP1YIE-rYGvhmc1JC0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت قالیباف از چگونگی شکل گیری میدانی به نام خیابان در جنگ تحمیلی سوم
یک ساعت بعد از بمباران ما متوجه شهادت رهبری شدیم
تا زمانی که توانستیم مسئولان را جمع کنیم ساعت ۸ شب بود.
در آنجا تصمیم گرفتیم ساعت ۸ صبح فردا شهادت رهبری را اعلام کنیم.
ساعت ۱۰ شب چون نباید مسئولان در کنار هم باشند پراکنده شدیم.
ساعت ۱۲ شب شبکه‌های ماهواره‌ای شهادت را اعلام کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/677188" target="_blank">📅 09:50 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
