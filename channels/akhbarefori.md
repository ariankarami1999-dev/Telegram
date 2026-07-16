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
<img src="https://cdn4.telesco.pe/file/Zeyo_gw63NrJL-D2cnB-jjsLj0E_jYIiqwWYjV1n2lYABGDW4rHIMGYl9qsKaEcqQ_25sGlbMBvx0oVl5lpN70s3vg4bJrW2XNS4vk5wOYYo28qhH9mPx8JqkKchdvmZiF82rL1QzTpnDB-ISjmLBWEklv-DTHowhV-boUEo9VoDV6gq9n_ONI15HgudInbpRALQT3Aa9W8RV0hu3cUx8alCePVOphzIcPCMVK42ppU4Rss0V-MD5MCCFRu-lg2fYiOTbHnbTZS5MZAxHs6yuL2NFk-Ab7mysuOHa7dejp0NFyWjJxC2CzsEgzmljgxNGLN35Q0R1VYiWyORMqNVEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.34M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 00:59:52</div>
<hr>

<div class="tg-post" id="msg-671913">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
وضعیت پل کهورستان، محور اتصال بندرعباس به شیراز  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/671913" target="_blank">📅 00:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671912">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4GjHCJzNsolHAUN7_DxvH0VuCf7T7U29iTzJzd9fS8oFdvbtS6QxgGo_nkUhPfRNFKMnw6boCQ_j8qYMhuvgPBiGtnaa55Y33t11F2OdxlxT8cWJPMq-hoc5o8OXo0XBC4jNhEkwgGl-LWIdPofJ1LBFu9ZDvBOAqpOldFnQ45TXjm82ZJe0nzctBo3h0da583qAWxhYOX_matAbDV6ZMmxCPByp1u3dUQHi5Z1Q07Md1k-zzDovHvQRaG5d3O4fdK4txzSCj4FAgBBM8enJyuKpfFuO_uqsTFAndASdBUnleJ7xM5r12dS085B2sqQaKqYjUBWGm_zsfW55QtlzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین تصاویر منتشر شده توسط منابع محلی از حمله دشمن آمریکایی به محور بندرعباس–لار  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/671912" target="_blank">📅 00:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671911">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
حملات آمریکا به زیرساخت‌های جنوب ایران: پُل، راه‌آهن، تاسیسات برق بندرعباس و فرودگاه ایرانشهر هدف قرار داده شد
👇
khabarfoori.com/fa/tiny/news-3230849
🔹
ایران امروز به کدام کشورها حمله کرد؟
👇
khabarfoori.com/fa/tiny/news-3230734
🔹
ایران با این روش جنگی بزرگترین دشمنانش را شکست داد
👇
khabarfoori.com/fa/tiny/news-3230840
🔹
علیرضا فغانی؛ روایت صعود به قله داوری جهان | از قضاوت فینال المپیک تا سوت بزرگ‌ترین بازی فوتبال
👇
khabarfoori.com/fa/tiny/news-3230845
🔹
همه‌چیز درباره قطع بی‌برنامه برق و جدول خاموشی
👇
khabarfoori.com/fa/tiny/news-3230774
🔹
خبرها را لحظه به لحظه در اپلیکیشن خبرفوری دنبال کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/671911" target="_blank">📅 00:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671910">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c11af7931.mp4?token=M16C8wbbUt29vThvbGclPiJPUPqbdGhtRWqAISfDWPrlZxqSUQ5zjtZVrVQR2fVRTolI_AEagpj-098B3QVjApkeoNDzu3FY_Sn3MljfID29oLiJeTktIsWMd0uq2rIWTFbMbxYKOpuG1Vpm8mrLhrRfC5kNwKkj3IC6WE3MWAhcLCucFD1gPIsrCNqOjvpzYG62hzmRGu7C_I5AKVvnN8YvVn6IwxyNqZGrZXLuYVxhStmkZrgoTarcusrXmx51tj96LSyUBHVVO47VhTGel4PjHWiYOFdrls8oto0qu5ZmcsWQJYzzpQ66aL65kKJGeR8YscMw_B2cyU1WYy6ubw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c11af7931.mp4?token=M16C8wbbUt29vThvbGclPiJPUPqbdGhtRWqAISfDWPrlZxqSUQ5zjtZVrVQR2fVRTolI_AEagpj-098B3QVjApkeoNDzu3FY_Sn3MljfID29oLiJeTktIsWMd0uq2rIWTFbMbxYKOpuG1Vpm8mrLhrRfC5kNwKkj3IC6WE3MWAhcLCucFD1gPIsrCNqOjvpzYG62hzmRGu7C_I5AKVvnN8YvVn6IwxyNqZGrZXLuYVxhStmkZrgoTarcusrXmx51tj96LSyUBHVVO47VhTGel4PjHWiYOFdrls8oto0qu5ZmcsWQJYzzpQ66aL65kKJGeR8YscMw_B2cyU1WYy6ubw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های عراقی از شنیده شدن صدای انفجارهای بسیار قوی در کویت و شنیده شدن آن از بصره خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/671910" target="_blank">📅 00:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671909">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند./  باشگاه خبرنگاران جوان   #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/671909" target="_blank">📅 00:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671908">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rth3pAvzy62x2fi5tV5Ff8ytRzA1JSR1IXPXlaZAzdsGU95MlIz46uqLc57czBgGofaCgkHnehd8ShBoeKqczEjAN1oaxLTz9oIrxde25mQ5o1E7tVdotKcutUmiuIC8K13dWInTvwq4RhKLSk7K0qD96yevK2OSyi1RSCV_2jfaprGZq-G2ZLIxmABnFgkup0IG2oSvTpRz8JhwvM9N8-Y-Le11Yvbb2JuKNVjxa2JK31cHL7jW-cxDD0rVnu2gaXHwdtIB8K0kMzC-6ELNgygGXwALdky9qkURpLGOMWPqgxLVL8VYG956FbvAtUN6a3oJoRTI3_Jjz_TFV5D44Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعلام کد اضطراری اف-۳۵ بر فراز امارات
🔹
‏یک جت جنگنده اف-۳۵ متعلق به نیروی هوایی آمریکا چند دقیقه پیش، یک سیگنال اضطراری عمومی (۷۷۰۰) را در حریم هوایی امارات ارسال کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/671908" target="_blank">📅 00:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671907">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
شنیده شدن چند انفجار در حوالی حمیدیه
🔹
بر اساس گزارش‌های رسیده، دقایقی پیش صدای چند انفجار در اطراف شهرستان حمیدیه شنیده شده است./مهر  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/671907" target="_blank">📅 00:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671905">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab33920f95.mp4?token=YFiu1GPQzUJKAjg21M5YNAp_G48nU9BsxOzIeiru2RWm4QU-rp5_Mncj67Z8_16n6wvK5FcFGDBcdhjGqwQPd61QocCz40DbeYN_DTTnKH5s400P3rQ5IT-yelpN6igcU70jzGroKZPpbjbGPi4kJwvuXlYYr27rU0YNXnWjqYmAWMywdfHPma8Gswvmi1HrGhvcsBYbv2M_hOxr1X53YCp6Zt3dwH9VxIqQaGcVXCBtNunI4jtrj_gIv40TiIKwL-rwlvSqHzsT2YoXHNRUkexRmz4XuRcXDvcRWtI2ChyDNyHGjUBl5JBmlLW261qkiGg-YmV22EYnfifBsCPKoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab33920f95.mp4?token=YFiu1GPQzUJKAjg21M5YNAp_G48nU9BsxOzIeiru2RWm4QU-rp5_Mncj67Z8_16n6wvK5FcFGDBcdhjGqwQPd61QocCz40DbeYN_DTTnKH5s400P3rQ5IT-yelpN6igcU70jzGroKZPpbjbGPi4kJwvuXlYYr27rU0YNXnWjqYmAWMywdfHPma8Gswvmi1HrGhvcsBYbv2M_hOxr1X53YCp6Zt3dwH9VxIqQaGcVXCBtNunI4jtrj_gIv40TiIKwL-rwlvSqHzsT2YoXHNRUkexRmz4XuRcXDvcRWtI2ChyDNyHGjUBl5JBmlLW261qkiGg-YmV22EYnfifBsCPKoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله هوایی آمریکا به دو پل در بندر خمیر
🔹
به گفته شاهدان عینی دو  پل حوالی روستای کهورستان و رودخانه شور شهرستان بندرخمیر مورد اصابت قرار گرفته است.
🔹
راننده یک خودرو شخصی، روی یکی از پل‌ها شهید شده است/ صداوسیما  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/671905" target="_blank">📅 00:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671904">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند
./  باشگاه خبرنگاران جوان
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/671904" target="_blank">📅 00:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671903">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
اصابت موشک‌های دشمن آمریکایی در حوالی سیریک
استانداری هرمزگان:
🔹
ساعت ۲۳:۳۴ نقاطی در حوالی سیریک مورد اصابت موشک‌های آمریکایی قرار گرفت./ فارس
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/671903" target="_blank">📅 00:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671902">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
پل محور کهورستان هدف حمله دشمن آمریکایی قرار گرفت محور رفت و برگشت بندرعباس به لار مسدود شد
🔹
برخی منابع اعلام کرده‌اند در هنگام اصابت موشک به پل، خودروهای عبوری نیز بر روی پل بوده‌اند، از میزان خسارت جانی هنوز اطلاعاتی در دست نیست.  #اخبار_هرمزگان در فضای…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/671902" target="_blank">📅 00:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671901">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
صدای ۴ انفجار در محدوده ساحل جنوبی قشم شنیده شد
./ صداوسیما
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/671901" target="_blank">📅 00:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671900">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
رسانه‌های عراقی از شنیده شدن صدای انفجارهای بسیار قوی در کویت و شنیده شدن آن از بصره خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/671900" target="_blank">📅 00:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671899">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
انفجار و حمله جنگنده‌های آمریکایی به زاهدان صحت ندارد
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/671899" target="_blank">📅 00:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671898">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vW-VRV-iRf6Dn6Pq3kH-35o3FOsJGLpf05If5ih7y-Alh-MJKTzmYDL1Q5cACz2lImRA4fUb0XCS9tQwMz8-fBGFzgQoR1oyVqSpQ5Z_pPhmpGFHhY6lBArYVvfe8hGw3NJUQhSqPUA4EID9zzCA1y3xw2DdhSurt87yGJ-1hRsdW4d5_Zu1XlY9Foqq2xD02XXmJhfJM3htnb3kXJySSF5LNeGjwkJoY3yiuSxJfePij5nqebCsPTh8PsOn3-lFVxJYkRwaNXJmFYK1oS7MX8UhiKUQlLbxoqpRFkI8ZC4OR5dYRjDlXWKLA7mncmpXrVpHdsbCm1FnPhUzIgTErg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/671898" target="_blank">📅 00:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671897">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
تعیین جایزه ۱۰ میلیون دلاری مقاومت اسلامی عراق برای کشتن دونالد ترامپ
🔹
مقاومت اسلامی عراق در پاسخ به آنچه گستاخی و وقاحت دونالد ترامپ در ترور فرماندهان پیروزی شهیدان قاسم سلیمانی و ابومهدی المهندس خواند، جایزه ۱۰ میلیون دلاری (از محل کمک‌های مردمی) برای کشتن رئیس‌جمهور آمریکا تعیین کرده و پرداخت آن را به هر فرد یا گروهی که این کار را انجام دهد، وعده داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/671897" target="_blank">📅 23:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671896">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVqFNVU24hNdTsZiZlTrUfroEk5Ui9OmcolnPskR6OegOooUGKU5KmPBeeNrmSu96h95zuA9AZ-vGkk6WfAGeSgzmp05zgNjsqOlNvBOGefUJ8kjMtGTs_tpBJ3xxhyoatzDMjmxq2OOiFYnq2K31UpeCwLTIdPvMJ-5b6hKmATEqC_dZGbjsFrpmowDCGz5n2URiBCAsP5bx3JaxQXcbi4sEI-FJX8LgI-7BgPwq88K-eOyUHG7bqRBm5VsbXKNA6yXPVewWqlC57mQFDn4JXouXRGyYcpk-y1VXOwuDJOHnN5aTbpQc5ouTmLq0Xb777ueoe0rAfe2t16EMeBgOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از تهی سرشار
قرارگاه مرکزی خاتم‌الانبیا خطاب به آمریکا:
🔹
«زیرساخت بزنید، هرچه زیرساخت در منطقه باقی‌مانده است را می‌زنیم.» در این هشدار، واکنش سخنگوی قرارگاه به تهدیدهای رئیس‌جمهور آمریکا نیز جلب توجه کرد و از تعبیر «رئیس‌جمهورِ از تهی سرشارِ آمریکا» برای ترامپ استفاده کرد. این موضع‌گیری، پیامی صریح به واشنگتن بود که هرگونه تعرض به زیرساخت‌های ایران، با پاسخی متقابل و فراتر از مرزهای ایران همراه خواهد شد.
🔹
هشتصدویازدهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/671896" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671895">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
بحرین از محدودیت‌های جدید برای تردد شناورها در خلیج فارس خبر داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/671895" target="_blank">📅 23:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671894">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
شنیده شدن چند انفجار در حوالی حمیدیه
🔹
بر اساس گزارش‌های رسیده، دقایقی پیش صدای چند انفجار در اطراف شهرستان حمیدیه شنیده شده است./مهر
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/671894" target="_blank">📅 23:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671893">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
حمله به زیرساخت‌ها توسط دشمن تروریست آمریکایی؛ حمله به پل بندرخمیر
🔹
گزارش‌ها حاکی از آن است که لحظاتی قبل دشمن آمریکایی به شهرستان بندرخمیر و بخش کهورستان حمله کرد و صدای چند انفجار شنیده شد.
🔹
اطلاعات رسیده و پیگیری ها حاکی از ان است که در این حملات پل…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/671893" target="_blank">📅 23:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671892">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
حمله به زیرساخت‌ها توسط دشمن تروریست آمریکایی؛ حمله به پل بندرخمیر
🔹
گزارش‌ها حاکی از آن است که لحظاتی قبل دشمن آمریکایی به شهرستان بندرخمیر و بخش کهورستان حمله کرد و صدای چند انفجار شنیده شد.
🔹
اطلاعات رسیده و پیگیری ها حاکی از ان است که در این حملات پل ارتباطی بندرعباس به شیراز و معروف به پل بندرعباس - کهورستان - لار مورد اصابت قرار گرفته است.
🔹
برق مناطقی از کهورستان نیز در حال حاضر قطع می باشد./ تسنیم
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/671892" target="_blank">📅 23:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671891">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
حمله موشکی جنگنده‌های آمریکایی به فرودگاه ایرانشهر
🔹
براساس این گزارش، مردم منطقه سه انفجار شدید را از حوالی فرودگاه ایرانشهر شنیدند و گزارش‌های اهالی نیز حکایت از حمله سنگین به این فرودگاه دارد.
🔹
هنوز از میزان خسارات این حملات اطلاعاتی در دست نیست اما مسئولان عملیاتی نیروهای مسلح مستقر در منطقه هم اکنون در محل فرودگاه حضور دارند./ تسنیم
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/671891" target="_blank">📅 23:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671890">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
۸ انفجار دیگر در محدوده روستای مسن قشم، در پی تجاوز هوایی دشمن آمریکایی گزارش شده است
🔹
پنجشنبه، حوالی ساعت ۲۳/ صداوسیما #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/671890" target="_blank">📅 23:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671889">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d41c69856e.mp4?token=IMx5uZncwhwxm48E1dd_u2K7qxFbX3VtOM8TYLnzBKAh5J15LWe5GXdQrNoNrCzRtnV0BxXPC1EjuFA0327W6KBcaFYEHja0ti2J5EsAZNPHYPXLkueZF99fQMVZDF8FXLsqJco2LWsZIyxpSxXBN3L83g2w10omROxSg44dhqqReuvl-EA5zfW6Drkpd0R1BXTHEOOLm43sav04FwOb8mbAK_JKMhBD-pcRY3Yf58SAWuCncxxriP76KFh0DWXs2GM2CVgW3bv4T3zQa7YVUQdnA1vKDy7exMfPDWXcfHhfJbo1hud2tFyiVM_3ydkxfy4mtZv2hk97vS4i4o-1ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d41c69856e.mp4?token=IMx5uZncwhwxm48E1dd_u2K7qxFbX3VtOM8TYLnzBKAh5J15LWe5GXdQrNoNrCzRtnV0BxXPC1EjuFA0327W6KBcaFYEHja0ti2J5EsAZNPHYPXLkueZF99fQMVZDF8FXLsqJco2LWsZIyxpSxXBN3L83g2w10omROxSg44dhqqReuvl-EA5zfW6Drkpd0R1BXTHEOOLm43sav04FwOb8mbAK_JKMhBD-pcRY3Yf58SAWuCncxxriP76KFh0DWXs2GM2CVgW3bv4T3zQa7YVUQdnA1vKDy7exMfPDWXcfHhfJbo1hud2tFyiVM_3ydkxfy4mtZv2hk97vS4i4o-1ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایان ست پنجم| ایران در لیگ ملت‌ها ماند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/671889" target="_blank">📅 23:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671888">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
افزایش دوباره قیمت بنزین درآمریکا در پی حملات به ایران؛ کاخ سفید: موقت است!
🔹
در پی از سرگیری حملات تجاوزکارانه ایالات متحده آمریکا به ایران، بار دیگر بهای بنزین در این کشور افزایش یافته است اما کاخ سفید آن را «اختلالی موقت» و کم اهمیت جلوه می‌دهد./ ایرنا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/671888" target="_blank">📅 23:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671887">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
تجاوز دشمن آمریکایی در تپه الله اکبر بندرعباس/ ۷ نفر مجروح شدند
🔹
دقایقی پیش تپه الله اکبر بندرعباس مجددا مورد حمله دشمن قرار گرفت.
🔹
حجم این اتفاق به حدی بود که برق این منطقه در بندرعباس در حال حاضر قطع شده است، هدف مورد اصابت در این حمله یک دکل مخابراتی…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/671887" target="_blank">📅 23:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671886">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5QtcCD3NPvZUwXpgl6WInuHIp2Wup7X91fEmeLc2QbHxmMrSRZpMdcHCSuf_53woe6sYjk5kCn7GgnSk3X1EufphxW0SWHTD9XbSyIFyy2Je4vSBFuBE8cP4S8P8QTYigB2xbioRlJ_OxE2SA9z95dGAarOVENmzpunZfBVnxjTvhhH5TTfRg9ezsWoj94eQZjzpx0OzTKlo-rr90x6ivJYIwmzcbBwM0cMCheEpkIiUNdKX5yZx3vVr4-SpLz35P6KENFpdiK5cav5mE8cNA8G4recRDaFRefjBTULBSi4RALJWyei62K7Pfntb9ogB6r7l_2iSQMhz2Z9pBWoBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاریخ‌سازی دختر جودوکار ایران در آسیا/ طلسم شکست
🔹
مهسا شکیبایی در رقابت‌های جودوی قهرمانی آسیا نوجوانان و جوانان با عملکردی درخشان بر سکوی نخست وزن منفی ۵۲ کیلوگرم نوجوانان ایستاد و برگ زرین دیگری به تاریخ جودوی بانوان ایران افزود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/671886" target="_blank">📅 23:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671885">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در بندرعباس و قشم و اهواز
🔹
هنوز منشا این صدا مشخص نیست./مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/671885" target="_blank">📅 23:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671884">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
صدای ۲ انفجار در شهر بوشهر شنیده شد
فرماندار بوشهر:
🔹
در ادامه تجاوز دشمن آمریکایی، دقایقی پیش در شهر بوشهر صدای ۲ انفجار شنیده شد./ ایرنا
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/671884" target="_blank">📅 23:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671883">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jywwzbYuXNsgvBFTGNyc74Y22KS3FVguDb1V3ZKxnXyJR2eR6y4yWRbehxp1ykU59WuEbRFtbcAMHrNgyqBEt4tyBwykr75h21JYqN2UFTypwN_uCqAbmVntwYHahlbXeu7AFF88uvxNXldqeLErlVcjWrHkux2sPGmyLI_8LGEaTE4jrEK8hGqDfs2GabcMhOfFXLcSgqh4GPJ866qgAl6MMCC586Cvgp585yOAtVWb9-_MjxhQ9pcQTX9WA2vIQZt_QcUufjvz3hzztViLKVnmnGAbERb7ZPteqMr38paYqbwLDxECc2i15CNP5UABU1fTWnIBTy1A6TT7l67VVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازتاب جهانی و توجه رسانه‌های بین‌المللی به بنر تهدید‌آمیز دیوارنگاره میدان انقلاب درباره کشتن ترامپ
🔹
دیوارنگاره جدید میدان انقلاب تهران با تصویری از ترامپ در تابوت، طی چند ساعت گذشته به سوژه رسانه‌های بین‌المللی بخصوص رسانه های امریکایی تبدیل شد.
🔹
رسانه‌هایی از جمله نیویورک تایمز، نیویورک پست، الجزیره، فرانس۲۴، فوربس، یورونیوز، فارن پالیسی، دیلی تلگراف ، فاکس نیوز و ... در گزارش‌ها و خبرهای خود به این دیوارنگاره و محتوای آن پرداخته‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/671883" target="_blank">📅 23:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671882">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
شایعه انفجار در چابهار و کنارک تکذیب شد
🔹
در پی انتشار برخی اخبار در فضای مجازی درباره وقوع انفجار در شهرستان‌های چابهار و کنارک، پیگیری‌ها نشان می‌دهد تاکنون هیچ گزارش رسمی مبنی بر وقوع انفجار در این دو شهرستان منتشر نشده است.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/671882" target="_blank">📅 22:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671881">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a746355b27.mp4?token=nSGtb81D83PATfTvCwwRgGGmiM9qfxQJbPJ_4Y8YMqsK992rdepws2JmhoOZkwGYfJpip1luT62-CAYXyBVySSbXQ1sIsqKEy-dJQ6mHiZoAH4b8QQGtqtB_G0XSkoCFE8k31QxRbDAeEz0y8msDGlh-w9G61DWaer6e3SZ_mfvXvCSoYnHfSDEXnxT67vC7pde3bv5Zl4xcq3gz1wlbPVcyEBXAqS15j5wgNm4h2Tb9ad3xwZN2KekC_e4682RzrLWHjkQ-ITsZYMbjKJb5wYpOmdmF-y4R1eOIQIe5URXfd35nF89RU9OXYUtmlw8gCULmT98uoiEQw61I_oQh7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a746355b27.mp4?token=nSGtb81D83PATfTvCwwRgGGmiM9qfxQJbPJ_4Y8YMqsK992rdepws2JmhoOZkwGYfJpip1luT62-CAYXyBVySSbXQ1sIsqKEy-dJQ6mHiZoAH4b8QQGtqtB_G0XSkoCFE8k31QxRbDAeEz0y8msDGlh-w9G61DWaer6e3SZ_mfvXvCSoYnHfSDEXnxT67vC7pde3bv5Zl4xcq3gz1wlbPVcyEBXAqS15j5wgNm4h2Tb9ad3xwZN2KekC_e4682RzrLWHjkQ-ITsZYMbjKJb5wYpOmdmF-y4R1eOIQIe5URXfd35nF89RU9OXYUtmlw8gCULmT98uoiEQw61I_oQh7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی ارشد نیروهای مسلح: شک نداریم که نمی‌توانند در میدان جنگ کار را به جایی برسانند
🔹
راه نجاتشان این است که از منطقه بروند و در دنیا مثل آدم زندگی کنند.
🔹
یال‌وکپال آمریکایی‌ها در این جنگ ریخت و هر چه ادامه بدهند بیشتر می‌ریزد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/671881" target="_blank">📅 22:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671880">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/659ee464a9.mp4?token=qOfMEBbFtRiB_5ImbRo-sU1qGe3bY8KZQWY87zkuYyb9vz12IKsckTU3UNvaE5ECsKevDrRvlClGhHzAugOIcMHn8oqxfsprWXxBbHrWfTEoSYMLNNdzKLqBBaA5k5SXjkGfts1Q264ueGnodEoWOk06P68Zp4fUnFjNcKpzzQQADq_BFYNeIloHK5ODno-V-oSL0edekvZgpCg3jBeQngBXU6srJo3f5rfQE-NX_EhrSIFedhx9XybtqCUnEV2I2ivsHK4yHduHGC_JvprF55GiFbdypNEit3rU6sMjm9t_EocjfMwg1IhhPTDo82dLFaVmvuhEISdV7CcGSV5Hpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/659ee464a9.mp4?token=qOfMEBbFtRiB_5ImbRo-sU1qGe3bY8KZQWY87zkuYyb9vz12IKsckTU3UNvaE5ECsKevDrRvlClGhHzAugOIcMHn8oqxfsprWXxBbHrWfTEoSYMLNNdzKLqBBaA5k5SXjkGfts1Q264ueGnodEoWOk06P68Zp4fUnFjNcKpzzQQADq_BFYNeIloHK5ODno-V-oSL0edekvZgpCg3jBeQngBXU6srJo3f5rfQE-NX_EhrSIFedhx9XybtqCUnEV2I2ivsHK4yHduHGC_JvprF55GiFbdypNEit3rU6sMjm9t_EocjfMwg1IhhPTDo82dLFaVmvuhEISdV7CcGSV5Hpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در بندرعباس و قشم و اهواز
🔹
هنوز منشا این صدا مشخص نیست./مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/671880" target="_blank">📅 22:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671879">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در بندرعباس و قشم و اهواز
🔹
هنوز منشا این صدا مشخص نیست./مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/671879" target="_blank">📅 22:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671876">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در بندرعباس و قشم و اهواز
🔹
هنوز منشا این صدا مشخص نیست./مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/671876" target="_blank">📅 22:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671875">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
سخنگوی ارشد نیروهای مسلح: شک نداریم که نمی‌توانند در میدان جنگ کار را به جایی برسانند
🔹
راه نجاتشان این است که از منطقه بروند و در دنیا مثل آدم زندگی کنند.
🔹
یال‌وکپال آمریکایی‌ها در این جنگ ریخت و هر چه ادامه بدهند بیشتر می‌ریزد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/671875" target="_blank">📅 22:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671874">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0VshsvvdqnQmMmatQBKtamInDLP265wVJjOd0OcNzEfECHofjo8Bgiv_ozT1jfbX_-ZcQmBW5w75cxqQS7Zke9qHSqWKtNmfS76SAypFQd5TpF6fA4dYqhd2HBXu_N24kB8QluFPrATzlsHiAFnxjSnOUuZYUlzpNue6nL6kZ_BvZXixcQaHdB7_WZCY96IZ3v0Ht3RkImwpoApuoqUYevZuhmlk-7WZk6xjyw-UDLaH0xzKDk2dEyn4OYFkJlZjWajsBNZCgMjmhVc6X-HkhrXy9jiW5wP7J6zEe_QbstxNQRKzz1omKh9XEJ-8IhPSeUTzgUCJDnLkHHeeE6FEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هلال ماه صفر
🌙
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/671874" target="_blank">📅 22:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671873">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrXbwL4f-b2qtLdgHkyC5Sf6B8v6aOf33i_EaPdN32C7qIbXdhSRkvMepOblVASLPF1yaTT5OZzrvFKrZjiqCO0JlnFVz3LwxF0lo4kBgkibE4zZKT8K-nFBd1OiFqyD8tMjU-R0vEEeKxeZ-yoK64TYXqJiQfkr5E-t64Qf1OQoZV9aXrbuS9ADPYIrzKHkYC_PhboP-hwOFQ4HW1DcQKoozI3ykotl8xkwDBSqsaGCEvJYbdGFi5ZQUlQhypROIsC-BO_UzJ4MD21Taz8qWzVyEVhpKOEuVPgTh9d9WFyt6ptTPnp5kElh032lEEtlkqiCagfFCSISjpWjxnC25g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/671873" target="_blank">📅 22:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671872">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c56e6a741.mp4?token=HlkBVGUTdXaAy0oaUYkc85SFFsiriQG1nU1Il8QBCVSy5ErPwvWq9P1vdp_NHZ6clA5dcRfa2pJhlXPLaUU4YHUkJLOBN_UpjzcUZGi-K9fY0I1TBK4AbKsZSDVqZDTmDZx5Ci-CAdJpZjz2jmfkAbW-9Zu4cbqaNIARI8Az8uX15WvrQcarVQlpznabvnFZ-zWpBLzZCjqA7gjOB9my-I9V3v-BjmJRiUfmZPz4-5WQZUBf99SFcKcVBauMcBeNEdvCI9FMHrhRB6JgQnWt0XMy2pfptArI3KgLhPNI4k7p93H8YoJyhtYAXZ3OLUhc2QRPXnGt5qh7XRb_esLJpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c56e6a741.mp4?token=HlkBVGUTdXaAy0oaUYkc85SFFsiriQG1nU1Il8QBCVSy5ErPwvWq9P1vdp_NHZ6clA5dcRfa2pJhlXPLaUU4YHUkJLOBN_UpjzcUZGi-K9fY0I1TBK4AbKsZSDVqZDTmDZx5Ci-CAdJpZjz2jmfkAbW-9Zu4cbqaNIARI8Az8uX15WvrQcarVQlpznabvnFZ-zWpBLzZCjqA7gjOB9my-I9V3v-BjmJRiUfmZPz4-5WQZUBf99SFcKcVBauMcBeNEdvCI9FMHrhRB6JgQnWt0XMy2pfptArI3KgLhPNI4k7p93H8YoJyhtYAXZ3OLUhc2QRPXnGt5qh7XRb_esLJpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صفار هرندی: رهبر شهید در برابر گزارش‌ها علیه شمخانی، از شمخانی دفاع کردند
🔹
فرمودند چند تا مثل شمخانی داریم؟
🔹
رهبر شهید؛ لاریجانی را برای انتصاب در دبیری شعام وادار کردند
🔹
در دعوای لاریجانی و احمدی نژاد، اشتباه کردیم که سمت لاریجانی را نگرفتیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/671872" target="_blank">📅 22:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671870">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
سردار شکارچی: اگر به زیرساخت‌های ما آسیبی برسد همه‌ زیرساخت‌های منطقه هدف ما است
🔹
این خواسته‌ خودخواهانه‌ ما نیست، بلکه با آمریکا مشکل داریم که از آن سوی زمین آمده‌اند.
🔹
اگر آمریکا نباشد کسی در منطقه با دیگران بد صحبت نمی‌کند. به دشمن پاسخ دندان‌شکن دادیم…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/671870" target="_blank">📅 22:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671869">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
سردار شکارچی: اگر به زیرساخت‌های ما آسیبی برسد همه‌ زیرساخت‌های منطقه هدف ما است
🔹
این خواسته‌ خودخواهانه‌ ما نیست، بلکه با آمریکا مشکل داریم که از آن سوی زمین آمده‌اند.
🔹
اگر آمریکا نباشد کسی در منطقه با دیگران بد صحبت نمی‌کند. به دشمن پاسخ دندان‌شکن دادیم و در ادامه هم می‌دهیم، آن‌ها ضربات محکمی خوردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/671869" target="_blank">📅 22:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671865">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PozoqTFPjKQe0isL7KkZ74O-EJUghmNfi01kvYGMvuoiXBuM7uAIYknpMq_3ZpcxVIQRwgZvQiAnLkbqRZj29MFp7y2mMDj2swxcTkctmn3PYGoFzuNFnDPwrYqmR0L04ZnSKLEI0k8_ubaA0XDo7ZUeb6qhEsE_VIUGC_T1RkyURVUtLX-SluPye9QMpcPdw6eqMp6H_ad9YmmpTKEIbtRrPmgscS8M2NKhhEhSYpekrapvzT28BFHqepqcETY8jT5BynFuRTR0u6XYvnMKUExnKkEdst5GDh33TBiMxM9SiWlpIfzSTHHNM5rrJceu1UFmicUUzKMK9usGIkbAQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صبر از منظر امام علی (ع) چگونه است؟
🔹
مى‌فرمايد: صبر  بر چهار شعبه استوار است؛ اشتياق، ترس، زهد وانتظار. «شوق» به معناى علاقه و اشتياق به چيزى و «شفق» در اصل به معناى آميخته شدن روشنايى روز به تاريكى شب است، سپس به ترس آميخته با علاقه به كسى يا چيزى به…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/671865" target="_blank">📅 22:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671864">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ادعای خوک نجس در مورد آزادی شهروند آمریکایی توسط ایران
🔹
ایران به یک شهروند آمریکایی که در دسامبر ۲۰۲۴ در زمان ریاست جمهوری جو بایدن به ناحق بازداشت شده بود، اجازه خروج از کشور را داد. او اکنون در خارج از ایران و در وضعیت خوبی به سر می‌برد.
🔹
ایالات متحده…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/671864" target="_blank">📅 22:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671863">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9S0duzz-DKhyuDnc2f5MDtjhaXj_egDl6iVjoaveYPmuSqR8MqgAmAyd9kGfNQjB9vA8sbY6BqA91vAnro_QcfM202fz3CqPN9dgy_J29AO6ngg294jdSDYKzwp3Zrwy2U8Em5Nmoj7LhDWOwV_ZXrGKVjRgTDfaoH8JSQ1Ix7Fu9gHwWLJARHZt2SYwTyA9neiA65_t6ciifwFTlvvxiex_26g8fIJuwjTDCFPJmrHaK5f47orz9CrbxX6jCSAZs70vTtUp0GjWSSih5zeWSrk2gZBB3J7H5oyi-piaJhlGg3K7QWu8mNEmskzkj1FndUZOUxbjwoFc1dNS43SKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان ترویستی سنتکام دور تازه تجاوز به ایران را تایید کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/671863" target="_blank">📅 21:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671861">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
اصابت پرتابه دشمن آمریکایی در بندرعباس
استانداری هرمزگان:
🔹
در ساعت ۲۱:۳۵ نقاطی در بندرعباس مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیل پس از ارزیابی‌های اولیه متعاقبا اعلام خواهد شد./ مهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/671861" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671860">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKMEabP--54Ojk43j6iwuHcoVj2rRQ-De0jab9odCSOMWDDTW226xKCZf05d4ehdSjNrWR7naNHIwRmPwjRyJ8wAqsyeD5BCYDViHzn6HHVFYV-lBD5JU4k55duBg1otlNK1Sw2-bym5hXFzCfy8ZDhCAkAZa7rdR-bQOJ3syyHV3fzvjLMtCBA6dFkEq-gCHaTMYOitPDzUrXb7pjQggME3OLK7t46TkgXyTngn3VxoQDQpDpsdZKk7necX3Ia8KVDGSpCicpbJuQnNznZFMZ8mPgexJR40qNc6u5ptKVkCynymureEo4FGMKePQBZv6NROoI0GUqQmaI58H-Ey6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درخواست علیرضا دبیر از مسئولین کشور: جنوب یعنی همه ایران، پس به کل مواضع دشمن حمله کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/671860" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671859">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مقتدایی، نماینده مجلس: آژانس انرژی اتمی تا مرز جاسوسی برای متجاوزان به ایران پیش رفت
عباس مقتدایی، نائب رئیس کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
اقدامات اخیر آمریکا جنایت جنگی و نقض قوانین بین‌المللی و تمامی تفاهمات پیشین با ایران بوده و از این رو، ایران خود را محق به پاسخ و تنبیه متجاوز می‌داند.
🔹
با برنامه‌ریزی قرارگاه خاتم‌الانبیا و همکاری سایر نهادها، اقدامات برای عقب راندن نیروهای آمریکایی از منطقه در حال اجراست.
🔹
عملکرد نهادهای بین‌المللی، منفعلانه و در مواردی هم که مداخله‌ای انجام شده، به نفع متجاوز بوده؛ نمونه آن آژانس بین‌المللی انرژی اتمی که تا مرز جاسوسی برای متجاوزان به ایران پیش رفت.
@TV_Fori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/671859" target="_blank">📅 21:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671858">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewCsKrYFGlhUiIOJ-ACs9F4VpDr_Z7Ze4brbxG6925-DAZmWE7tq43BaM_9zpGH4LmtcIwXFUbupzYAg9V6ikiJNXdl87DF55OpcdEyaQKDlNyp8k_BTkzGVrmxVh8M8Za4obGB7jVJt2elxzPoPsBKsFCI74TDVWg1nYFp_wG_w7LTqgwiqGw5OUcT19KA-7PhyeFzGc1w133UmwERWjoxlgea7DjzoAAI1_otE5dOArOTGrOzguGXbjL5pbZNezQzY-uV320ZEePfAasaMMbXvhwQvVXRfTF19aZ7dJaghpNDXsysBLyQAHj9qDn6dtE59EAQJSHTvWCFB91_fkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران با این روش جنگی بزرگترین دشمنانش را شکست داد
🔹
دکترین نظامی ایرانی ها را می توان در یک کلام «پویایی پدافندی» نامید. طبق این دکترین، نیروی نظامی با بهره گیری از سرعت فراوان و بر اساس راهبرد عکس العملی، شروع به برخورد با دشمن می کند. در این اصل و دکترین، اساس نیروهای نظامی «سواره نظام» است و مهم ترین سلاح نیز تیر و کمان به حساب می آید.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3230840</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/671858" target="_blank">📅 21:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671857">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BauoMgq4leEvtoDq5iWVmtH91n-xv9Ul6Yc2L6NPxfYqc8v1oCO3K66b-sxJELKdI6sGLc7CAwiX65uwcL63_2ABnUDsmENQ93FB-cegwfsKzrWDh_opiTL0xG8uDpMQ8h18nviR4MCaYFbDpTFvHSvblCk7EH0RQm7fn-TDrcvV4AfXLRSSuyvLMTWFBt3u_p9nvhuS1losDwtX8RBsDJsWEyQeKlOGMrddOPv9rX12zQCFzFnjKcsFzlVX2SvhdaW2YgtryTLptiN4oeRmpfNt9JzBUnqNGPv3tq-UclsBHr19t88Gpia9JpXp61YhG0cz5zVyGK9QLA7zK6as_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعداد حضور آرژانتین و اسپانیا در فینال جام‌جهانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/671857" target="_blank">📅 21:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671856">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
گستاخی سخنگوی کاخ سفید درباره ایران: ترامپ ثابت کرده است که ما می‌توانیم هر زمان و هر کجا به ایران ضربه بزنیم و توانایی آنها برای دفاع از خود اساساً از بین رفته است  سخنگوی کاخ سفید:
🔹
ترامپ و جی‌دی ونس در حال حاضر دقیقاً درباره ایران هم‌نظر هستند.
🔹
تنگه…</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/671856" target="_blank">📅 21:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671855">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
گستاخی سخنگوی کاخ سفید درباره ایران: ترامپ ثابت کرده است که ما می‌توانیم هر زمان و هر کجا به ایران ضربه بزنیم و توانایی آنها برای دفاع از خود اساساً از بین رفته است
سخنگوی کاخ سفید:
🔹
ترامپ و جی‌دی ونس در حال حاضر دقیقاً درباره ایران هم‌نظر هستند.
🔹
تنگه هرمز به روی کشتی‌هایی که به مقصد ایران نیستند و از آن خارج نمی‌شوند، باز است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/671855" target="_blank">📅 21:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671854">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ادعای وزیر خارجه اردن: هیچ پایگاه آمریکایی در اردن وجود ندارد!
وزیر امور خارجه اردن:
🔹
روایت ایران مبنی بر وجود پایگاه‌های نظامی آمریکا در اردن نادرست است.  هیچ پایگاه آمریکایی در اردن وجود ندارد، فقط سربازان آمریکایی به عنوان بخشی از همکاری نظامی بین ما و واشنگتن حضور دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/671854" target="_blank">📅 21:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671853">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
کاخ سفید مدعی ادامه مذاکرات ایران و آمریکا شد
سخنگوی کاخ سفید:
🔹
ایران به مذاکرات با ایالات متحده ادامه می‌دهد و خواهان دستیابی به توافق است. حملات اخیر به ایران به دلیل نقض یادداشت تفاهم بود.
🔹
ایران به مذاکرات با ایالات متحده ادامه می‌دهد و خواهان دستیابی به توافق است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/671853" target="_blank">📅 21:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671852">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22723d50a1.mp4?token=ody20qtGnSGBMbwr6DbgW7K_J5J5ShLNnDED0pMlauBx9CnOymu4aZwD_wyJnuYVT0o7m201k5sCceC8Wt1v0HkUgThdsXQp9LZG75mjSTVNqG9XyH1EiTyc71ChEiYZ-Yt4oCgaWgI4m7Isc3Cmyo-wV1_H2bB6Xo9uHK_qudwwGjGFP8uHHKY3MT3u7iFx3rMIC2GYOaKnFqa-yQVa2VH4kW7E4kMEnqISWX5b-JpDMkoQNNTMvIXUT_xrEuR5FGrKvtuxEaNHrXcAvu15CWbvCGN8ViBpGUNI-5ieqxvytaWoMBS5pb_kSw_f4bai5mig6jRyp1XsUbeAr-tRsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22723d50a1.mp4?token=ody20qtGnSGBMbwr6DbgW7K_J5J5ShLNnDED0pMlauBx9CnOymu4aZwD_wyJnuYVT0o7m201k5sCceC8Wt1v0HkUgThdsXQp9LZG75mjSTVNqG9XyH1EiTyc71ChEiYZ-Yt4oCgaWgI4m7Isc3Cmyo-wV1_H2bB6Xo9uHK_qudwwGjGFP8uHHKY3MT3u7iFx3rMIC2GYOaKnFqa-yQVa2VH4kW7E4kMEnqISWX5b-JpDMkoQNNTMvIXUT_xrEuR5FGrKvtuxEaNHrXcAvu15CWbvCGN8ViBpGUNI-5ieqxvytaWoMBS5pb_kSw_f4bai5mig6jRyp1XsUbeAr-tRsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای نشان می‌دهند که ایران به هتل کراون پلازا در شهر دقم عمان حمله کرده است
🔹
این هتل به طور انحصاری محل اقامت نیروهای آمریکایی است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/671852" target="_blank">📅 21:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671851">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU_yYlPPIKxbLiTFCBnBfrHRYuCoPZzo3BoOm1oP1LntamvnaaS8vCfvCFv3ILHy-gX_w_JGNwc-FTirWEgsTAjdYlYQan3qVAsD4GMEPjg_4u9nj3J0jPS3dvIfv_uzlQzotjJoyBy_6L6FDLdenvZ1g0Wq18Blfr0ppyEjwG1PSXlJzJjMrEHmUfTqvNZ2T3bhl4MXar4L7QW_wsg-D52ieXm9WXmtYN1k2JPeq3tOaLjuYkM8L3t_kzVOHrVzOQUCAhi_7qbDMdfXlXpDQ49KKCzXQ0_si2T0yOVFWHB9eIIkImtP0yRzNdCHRutL43WAyu7Vj8tEzI3X0lKKmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی فیلم: علفزار (۱۴۰۰)
🔹
ژانر: درام اجتماعی، جنایی، معمایی
🔹
خلاصه: اگر به فیلم‌های اجتماعیِ پرتعلیق علاقه دارید، «علفزار» را از دست ندهید. این فیلم به کارگردانی کاظم دانشی، داستان بازپرسی را روایت می‌کند که در جریان رسیدگی به پرونده‌ای پیچیده، میان…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/671851" target="_blank">📅 21:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671850">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
حضور یک تروریست در فینال جام‌جهانی
🔹
کاخ سفید دقایقی پیش با انتشار اطلاعیه‌ای اعلام کرد ترامپ، رئیس دولت تروریستی آمریکا در فینال جام جهانی فوتبال شرکت خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/671850" target="_blank">📅 21:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671849">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGkJOWD3zPOxNnzBHzG9YdxmV1nLEjO-nH7skel9ZPIt3_yXISl9L-n2HTadzay6VWbXekFUyda48OHT17Y6FaMMrjSVG5QdPi4ny7x_gyRL9wu2iFZZVRurPjovkGjDypb3L2K4lonC24OTgIvZmgZ8_xlmNp9SlndgEmvzkXNicXnEM1Q4LpWkyCxAxJgBP-U2clDsgC17rcxbO2htDTJ-kUwgceTxJRw58G-RTkDpiK506ajsW9YppegCUlY76ENU-5TKkviswuc4vyoYvXtM9YABmT3mMUaDuM0SJpu8s3wbVAqTu6Af6cAq-ztS_zGL9H-LMRGEMyXnAa55WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
متن زیبایی که بالای سر یک کودک سرطانی در بیمارستان بقایی اهواز نصب شده
🔹
علی معرف
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/671849" target="_blank">📅 21:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671847">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f0f88d2e.mp4?token=XXge4Jk6wzQBaTV2AUJ8PGYy-lh8CqokkvtxPlJFGLX0TrpiClDZg3OGSMvhbRtLop6oFH0bwPDdxajJ2qyE9DkISTCPeLBvAcziuQCiLUTxxz2nmdh3jt4UlVjaTTNgVgWG18Cx2eRqrzeUPFGsCB-JA1ZDlusCJRlpQbq79V7xZ--Gteg6r5YHn_3twnTVG6nS4j7uXIYaLCOXCAb56l7hTxH0VDDKkzRlCkHC7FfEf95B3cCA9k0eouq-C1MZX9YAy80dVi2tPRMWTQqKPXu18Lpm7S7Kjwag_nkRyTGVtaCbRa8EWE7g842SOfYGjRxjn7xjNUwFj6Te7TjmLZcxqU60HoDmBzNsoNA-fnGCE05yZKkkQ9YJG4Ggh9F4SSdTlkZUGmJtZbLaQckZ-MboWrJBGaiYYS3hr4J2hAIIN2G4vELUukYw8AQxk_gDRMfPA0ADjFw5zFsogdj-QSIfJq8gN0wEB5M-nin-oYpZR2V2Q4V42gmnDk9iN1Eg2vLXKlXOz44-t4Y8e9CC5g6CF73wnebJaQxLbkjWPvCtC_XPHCa6uzVK-iaULKtDwp-ytOOHPmT90Aq54SIV6b8JSB20k9UT2jR2YNkmxANoeEiIuAIh7ni6C4eyorSH9YF4ssM6eDQTL-ISjjj_ofrBER_GVMmypxtaa0qRUig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f0f88d2e.mp4?token=XXge4Jk6wzQBaTV2AUJ8PGYy-lh8CqokkvtxPlJFGLX0TrpiClDZg3OGSMvhbRtLop6oFH0bwPDdxajJ2qyE9DkISTCPeLBvAcziuQCiLUTxxz2nmdh3jt4UlVjaTTNgVgWG18Cx2eRqrzeUPFGsCB-JA1ZDlusCJRlpQbq79V7xZ--Gteg6r5YHn_3twnTVG6nS4j7uXIYaLCOXCAb56l7hTxH0VDDKkzRlCkHC7FfEf95B3cCA9k0eouq-C1MZX9YAy80dVi2tPRMWTQqKPXu18Lpm7S7Kjwag_nkRyTGVtaCbRa8EWE7g842SOfYGjRxjn7xjNUwFj6Te7TjmLZcxqU60HoDmBzNsoNA-fnGCE05yZKkkQ9YJG4Ggh9F4SSdTlkZUGmJtZbLaQckZ-MboWrJBGaiYYS3hr4J2hAIIN2G4vELUukYw8AQxk_gDRMfPA0ADjFw5zFsogdj-QSIfJq8gN0wEB5M-nin-oYpZR2V2Q4V42gmnDk9iN1Eg2vLXKlXOz44-t4Y8e9CC5g6CF73wnebJaQxLbkjWPvCtC_XPHCa6uzVK-iaULKtDwp-ytOOHPmT90Aq54SIV6b8JSB20k9UT2jR2YNkmxANoeEiIuAIh7ni6C4eyorSH9YF4ssM6eDQTL-ISjjj_ofrBER_GVMmypxtaa0qRUig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حاوی تصاویر تقریبا دلخراش
‼️
♦️
امروز ظهر در خیابان ولیعصر تهران، یک اتوبوس تندرو BRT بدون راننده و مسافر به دلایل نامعلومی شروع به حرکت کرد
🔹
این اتوبوس در مسیر سرپایینی قرار میگیره و با ۶ موتور سیکلت و ۲ ماشین سواری تصادف میکنه که نهایتا ۶ نفر مصدوم میشن...
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/671847" target="_blank">📅 20:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671846">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
حمله به بهبهان تکذیب شد
فرماندار بهبهان:
🔹
ستون دود سیاه مشاهده شده در آسمان  بهبهان مربوط به سوزاندن ضایعات لاستیک و زباله در اطراف شهر است. مورد امنیتی یا اصابت صورت نگرفته است. شهروندان اخبار را تنها از مراجع رسمی دنبال کنند و به شایعات توجهی نداشته باشند.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/671846" target="_blank">📅 20:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671845">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون آموزش: اگر تهدیدی صورت گیرد، امتحانات نهایی آن استان یا کل کشور لغو می‌شود
وحید کنعانی‌کلور، عضو کمیسیون آموزش، تحقیقات و فناوری مجلس در
#گفتگو
با خبرفوری:
🔹
تا الان هیچ تصمیمی برای لغو امتحانات نهایی سایر استان‌ها گرفته نشده و امکان آن خیلی کم است، مگر اینکه تهدیدی صورت بگیرد که امتحانات آن استان یا کل کشور لغو شود. برای جایگزینی امتحانات لغو شده استان‌های جنوبی بعد از بحران حملات، تصمیم‌گیری می‌شود.
🔹
بخش زیادی از بحث مثبت شدن معدل یازدهم در کنکور ۱۴۰۶ حل شده و مورد خاصی وجود ندارد و اجرا می‌شود.
@TV_Fori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/671845" target="_blank">📅 20:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671844">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
سفارت آمریکا در عراق هشدار آماده باش صادر کرد
🔹
سفارت آمریکا در عراق در پی حملات پهپادی در اربیل، به شهروندان آمریکایی مقیم عراق توصیه شده است که در وضعیت آماده‌باش کامل و هوشیاری بالا قرار داشته باشند.
🔹
در این بیانیه هشدار داده شده است که احتمال ایجاد اختلال ناگهانی در سفرهای هوایی و بسته‌شدن موقت حریم هوایی منطقه وجود دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/671844" target="_blank">📅 20:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671843">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGySAFH5IWc8xNfaHwbmJrqUzjhSunA-uiQYChwV_bDF4Zz09ltHpA2i1kzldk321bAGRJsxUZFnCnH5jWq2iWMP14oLkTzkvheCmRS21Y7k7q1ClWK7fJqxq4Xvrm5IbOWH1M22sDYnSqsHljHfF3JN4zvevxpaueyRiHJcCWfcoLJlJ_EzfLPsUM0zHIyZZYwbVYHPZS27KaPRv6Z9C8DhVtadfsRRl0VteJC596ndB1ipezF1MXxGI5oTViknEUIwndwRUIZaDtI7pUQoFWR4uWt_0up1x4Y3k6XSOJRjtSDmVURfaOskcsRkcV5LHH2pfJaZ3T2_aKdsZvZY9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سایپا محصولاتش را گران کرد!
🔹
شرکت سایپا امروز به صورت رسمی قیمت محصولاتش را ۲۱ درصد گران کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/671843" target="_blank">📅 20:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671842">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96a114eacf.mp4?token=c-cre-P_msnD4V1MhYXrBT_jHICQGy0n2d2L7frRGi23Q-VTz_DymxTBLv7tvqi0FsppqEK2Qd2-b8uY1DRMxpI3Rrw1w9B1uSZi94yahzuc8WAYltECuRaXa2KN1Y91FFXJDzf6w-wVoS6JqATCoYAvUhel0SDu-clQdwdH64TBg_l1AfDvgSXDiu3BheRyia8XCktTNS6MGvyvUalAY_-eOG4usBJypxMSa-K8kySc4oj6fQZGhIN2XYsmzl7N3a0Kos9Yl6S4lTtbXhHWrSRN542hTZKGHioRkubA8HvyX8CyDHN4HSBP7S-qhoRL2wTOC0wvm3d-QvMMfiO8aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96a114eacf.mp4?token=c-cre-P_msnD4V1MhYXrBT_jHICQGy0n2d2L7frRGi23Q-VTz_DymxTBLv7tvqi0FsppqEK2Qd2-b8uY1DRMxpI3Rrw1w9B1uSZi94yahzuc8WAYltECuRaXa2KN1Y91FFXJDzf6w-wVoS6JqATCoYAvUhel0SDu-clQdwdH64TBg_l1AfDvgSXDiu3BheRyia8XCktTNS6MGvyvUalAY_-eOG4usBJypxMSa-K8kySc4oj6fQZGhIN2XYsmzl7N3a0Kos9Yl6S4lTtbXhHWrSRN542hTZKGHioRkubA8HvyX8CyDHN4HSBP7S-qhoRL2wTOC0wvm3d-QvMMfiO8aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شواهد جدید از کمک امارات و کویت در حملات به ایران
🔹
انتشار ویدئویی از یک حملهٔ پهپادی در بندرعباس، بار دیگر نقش امارات در تجاوز نظامی علیه ایران را آشکار کرد.
🔹
در این تصاویر، یک فروند پهپاد از خانوادهٔ Yabhon ساخت امارات در حال پرواز بر فراز منطقه دیده می‌شود که نیروهای مستقر در محل با سلاح‌های سبک به سمت آن تیراندازی می‌کنند.
🔹
این تصاویر در حالی منتشر شده که بررسی‌ها، هویت پهپاد را تأیید کرده و نشان می‌دهد ابوظبی، برخلاف ادعاهای بی‌طرفی، در حملات علیه ایران نقش عملیاتی داشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/671842" target="_blank">📅 20:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671841">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WH6jo7whl4S1O6953RPHWfO8b_VGqjRAVTm03YDfT3DqubwGigftohyeQZXMLTKk-XOANQP5l4TjClHyhE_W1Glu4LI5kx0vuUoKBHbpHW12KIATMkhikzAYEHEg5ewI-hdpnE8loGAiowXSTIEOY2MvoJWAV7D8R1R6izlBt8TWJuQKma7O52szy4xzjiqCvx0Jf7bBqwalysegsRtS8pvVHcK-zRZZhC8zVjY9wY3lPpuG2reBEWvKzxbni_irjZeK7ht9m8JJNZKPpenuMRUHPGZNNfLssBlSyqOEpaZ4GhAevXagSe8fvGmVtoeGVwkveSp8woASU9xUsZ2D6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قطر: ما گزارش‌های رسانه‌ای اسرائیلی را که ادعا می‌کنند ما با مشارکت در یک عملیات نظامی علیه ایران موافقت کرده‌ایم، رد می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/671841" target="_blank">📅 20:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671840">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DslhzoPQQw36zUGnNwFoP8S3DgsPO_iVMISuLL9xrUaC6sNResiNvr_UQNIOxwbrtRzWJXO3J65HawBSisDM1jOueMtzZquasQAeLngKrC1ciEmp-5z-GzAiobrFzJ8vDe4ohYQ3pbDRT4mtXm-gMPEeXLuWypIu98zsRvYsbdG9uzX7hI4O0DglKJevHuPKTcneL8R3k4FQzZckPQspiT4neRq0IDoJK7MtsDsUezvaeo9HFHITsHIdlPpoF2CmjEQ3f7Bnj5GntMKL9SSYQ-h2doJwHZIqoKpAKjfXkvme-fzsSDbBNwxWWlqwDcgaidUSuGgIEuMfFYhuGr92MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشاور محسن رضایی: تصمیم مهمی در تهران اتخاذ شده است؛ اگر حکومت جولانی بنا به درخواست ترامپ و فشار آمریکا دست به اقدام علیه حزب‌الله بزند، با حملات موشکی و پهپادی مستقیم ایران مواجه خواهد شد. این هشدار به جولانی داده شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/671840" target="_blank">📅 20:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671839">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
وال استریت ژورنال: آمریکا در پیامی رادیویی برای کشتی‌ها اعلام کرد «مسیر جنوبی تنگه باز است»؛ یک ملوان از طریق بی‌سیم گفت «گمشو»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/671839" target="_blank">📅 20:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671838">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddQykGpyjBJoLiAo7lrGZHLpLg0qLfvIPzzCzPUWtFt8dzvjNw9ybbWmPh6q--flut0Usc7s01RSuGC2CR38HmVi5ooqNyB75ygLyICwZhPz9uEb42H6q4tv44byEhyNHlCPL4ha7xANEyKZLU7AU2ATBVnBNc4s3ZRHdGVSewvz9l0voDibvC50N2BXdJWSvsjEBRL6ea9SDXTuR4N9ycvaxvxGsQ6RxLaoIlEckoS3sv_3mLPApQnFF9w40eWhRA6OXHehBbN-n2ep9pMhI_r4kQh3hcqjJ6R1qWBfvB-e04telAf7yS28kWLOVdN4mxLZoeSKTq7IryZtMPU09A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای نشان می‌دهند که ایران به هتل کراون پلازا در شهر دقم عمان حمله کرده است
🔹
این هتل به طور انحصاری محل اقامت نیروهای آمریکایی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/671838" target="_blank">📅 20:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671837">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WO8dpAI9yHEDuLBCoXkYVqJr9IyfwacrKMfQJkYm4FB3rMugnhXpbn7TzH2YwwOKKN8cMFYlz6nMmdhn-j2JpWSuc_1r2d9kT4eOGMEs3gvb_lXE2ZkFAmtJRfQUmZWjgPtSIbZXPspRrQmS-UqdJrVJjzj5uGlOvUi071JbYqL_6IrIHMRT_fw3JDcAW6LWNihr2oha_30KuemzF-r-b0z7du7SprTHewUIA0SSgOCTJDgOOCORjtdl3muqJyEJa7WhT5XkWMgN2jVkwnggvxYiVBB84NCfvVcB2hczw7tStsozmfx5X1f63G_ePqndYW6IS42MAHaQhpNofYwvxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان ست پنجم| ایران در لیگ ملت‌ها ماند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/671837" target="_blank">📅 20:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671836">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
روایت تکان‌دهنده مردی که پس از مرگ، فرصت دوباره از خدا خواست
🔹
00:09:00 توانایی ادراک همه‌ جانبه افراد پیش رو و پشت سر در صف انتظار
🔹
00:15:50 سفر به سه فصل مهم از تاریخ بشریت
🔹
00:28:20 خواندن خداوند با چهار اسم اعظم، برای طلبِ نجات
🔹
00:37:35 بازگشت به دنیای زمینی با حالت سجده اجباری
🔹
00:50:30 تغییرات رفتاری تجربه‌گر بعد از تجربه
🔹
00:56:20 علت تبدیل خیاط‌خانه‌ کوچک به قصری باشکوه و عبادتگاهی والا
🔹
00:59:20 به میزان دوری از نفسانیت به روحانیت نزدیک می‌شویم
🔹
01:05:10 کوچکی دنیا نسبت به عظمت آسمان اول
🔹
قسمت سوم (صبح غیرت)، فصل پنجم
🔹
#تجربه‌گر
: فرهاد یزدان‌ستا
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/671836" target="_blank">📅 20:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671835">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae6595c4c.mp4?token=BGKCL5Xipg3bj5aXmBrpyZ70JuiTdrdYI1a43QuoL6B-1Mebbtbiy8L9XJPfVycDdWHy6ZOlhGmeLY1VB1zx6vxWzkPlGw-TrYZM8XXVHZ9EuYZhh8uFq0-y7AZOT9-XXunuU4_5AmO7KSHGgP3NxjbQr-wqCXRhb-KhwsFqQ3FCh4VxMRdaaefap6ZGNlnvEZBJEw2aK7LPx7QrMKe2Os5JtGrR-T6NCnM_3sNSOR7w-ciceNbRDkq0-d1b0ORr4ov4_xtfjlSF_HW1DbJ-GNnoxsoK8S2BKhEjnE3Oi1Y7AV5wEklWiscYgM09Np40Xf-eVs5kvNFW5V0PzGEing" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae6595c4c.mp4?token=BGKCL5Xipg3bj5aXmBrpyZ70JuiTdrdYI1a43QuoL6B-1Mebbtbiy8L9XJPfVycDdWHy6ZOlhGmeLY1VB1zx6vxWzkPlGw-TrYZM8XXVHZ9EuYZhh8uFq0-y7AZOT9-XXunuU4_5AmO7KSHGgP3NxjbQr-wqCXRhb-KhwsFqQ3FCh4VxMRdaaefap6ZGNlnvEZBJEw2aK7LPx7QrMKe2Os5JtGrR-T6NCnM_3sNSOR7w-ciceNbRDkq0-d1b0ORr4ov4_xtfjlSF_HW1DbJ-GNnoxsoK8S2BKhEjnE3Oi1Y7AV5wEklWiscYgM09Np40Xf-eVs5kvNFW5V0PzGEing" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جام‌جهانی زیر چتری از دود
🔹
در فاصلهٔ چند روز تا فینال جام جهانی، آلودگی هوای ناشی از دود آتش‌سوزی‌های کانادا نگرانی‌هایی ایجاد کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/671835" target="_blank">📅 20:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671834">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hx0gloHCQsrcIaCVoPIMxNsy0Bbdl2OZWKMkCYVtNzp5PEZ9XUkL5-bFq-Xt4aifEJVzcxiPQE51PnEu0dMoqQQSvn1Z82pPnlQXckFhCiKGUvPOEh9Y10oF1BP7x8cFy2sWza6E9QifhIPvZJUr5FfebbV9RFmzzAmlrm7j15UC6uEb3W150yfcy1xHFpYQSOW_4Qv2iD_ohLeZn2-Cb5zxzGpwLyZeTNI3cY5z1UlcNCI-5doDsd8d7uETgHGhSyCkmooLejtb8NQrRlIsFhSuurBrqNXInaH170s0id8HFWa0oDfzpAu4bDzkwGiwRt6VLJYe5-gjTlv-LNmMcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای دولت دبی: گزارش رویترز درباره وقوع انفجار صحت ندارد  دفتر رسانه‌ای دولت دبی:
🔹
هیچ‌گونه انفجاری در مرکز این شهر رخ نداده و اوضاع کاملاً عادی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/671834" target="_blank">📅 20:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671833">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ادعای دولت دبی: گزارش رویترز درباره وقوع انفجار صحت ندارد
دفتر رسانه‌ای دولت دبی:
🔹
هیچ‌گونه انفجاری در مرکز این شهر رخ نداده و اوضاع کاملاً عادی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/671833" target="_blank">📅 20:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671831">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ma8vsR_9Fv1LHjPNM5muTuwAqI8l4fXJqzjEJIVL81S6gWbeQC8pfMZlU66YMGFgDQFzMmT2lW-LVsXp9-KRsN0N2Iz2YKsx6fDWtCuc7IFw5tx0u1vW8mGxn_lZ0c5H1wNoBxHo3G1gd-T0D2zt7hCPvss2oBIGGPw0oBMapK_u0EuYsJRynxuJ8H51l7rJGMGxJ6mmXlaRQx6RjXQeUhf_DGlOLDXrAAyyUIivUHJ9xJqlESCRHk97IQuoOKndii4JTKjB9AfFziBoGXkSiCscrwy754YsShYQboJVaFeEIGhg5fgenQaMIZ9tvvor-LZ355oOysInyyM-QCHWgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه‌های اجتماعی در حفاظت از کودکان و نوجوانان شکست خوردند
🔹
شبکه‌های اجتماعی برای محافظت از کودکان و نوجوانان، ابزارهایی مانند محدودیت پیام، کنترل محتوا و تنظیمات ایمنی ارائه کرده‌اند؛ اما بررسی‌ها نشان می‌دهد بیش از نیمی از این قابلیت‌ها در عمل مطابق وعده‌ها عمل نمی‌کنند.
🔹
از ۸۶ قابلیت ایمنی بررسی‌شده در تیک‌تاک، اینستاگرام، یوتیوب و اسنپ‌چت، فقط ۳۵ قابلیت موفق بوده‌اند.
🔹
اسنپ‌چت با نرخ شکست ۷۳٪ ضعیف‌ترین عملکرد را داشته و پس از آن اینستاگرام (۶۶٪)، یوتیوب (۵۵٪) و تیک‌تاک (۵۰٪) قرار گرفته‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/671831" target="_blank">📅 20:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671830">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مقام نظامی یمن: اسرائیل برای رهگیری حملات تلافی‌جویانه یمن به کمک عربستان آمد
🔹
نیروگاه تبریز هفته آینده به مدار بازمی‌گردد
🔹
آیت‌الله جوادی آملی: وظیفه همگان، حفظ وحدت، حمایت از رهبری و صیانت از نظام اسلامی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/671830" target="_blank">📅 20:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671829">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
برخی منابع رسانه‌ای از صدای انفجارهای شدید در پایگاه هوایی الظفره‌ در ابوظبی خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/671829" target="_blank">📅 20:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671827">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ER_OJjx50U9ORXO3bDb9FXBmwIeG8UmJlFRduHso635pPbaJmDI9uZU3GWvGekMFy052qOpT9un8y0VoxZ6oZgHifcn1JW9xbHgH_lvFm4SgjMAG0nPG_FMTgYyYDSDgBZRQl79j75NNdxOkzEAS29Q9EQPK4joOGg2TXvrs-KGhsSDSu5RPVhbiBB66x6sdF-zb9iSQvDPqaUfMA14IUUsEL6s1pX8HZH6_80MylBkhYcV7zEZu2SNMKjs_QlCUhliOVipjRZtuLjqmId97B_dgQeCnJ2wXl3kEjFb6SM6j38gYPJu_lSuP5i-iVmiYhF-H_s7LIOkXPZ9vx92qsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MUXQ601AT8mkixGj0DXkBIAyudy_nx2KSpbSdUHJABt4AB2kDbYZC0TI-luEsWlPXXJwq_HUwq_x6tc-BgSWan95sCYLnrqwP53qzIzXMTswPn-q-GeKugBfxQnrnEAGR10nMCaCpnh_jqZIZULaK0UV10Aw-YF3XdFzZSSByLiBhCNTHDkFgigSGUp5FE6A07Lh9YmYpKw6AD92uKQX0RZ1E9itZEsnX_bqoQKLg35zeHFnYjprtVC6aI8OW78V2lYwjiKDyTz6udRtarKSYXQXjDVHEXnI-WhCfNXszQCHkEJYph5H9MI8uWB_FI5FcOJmn8E0Pq2D8oUEi2Pfww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
از تلاش کردن و نرسیدن خسته‌ای؟ «موش‌ها و آدم‌ها» رو بخون!
🔹
«موش‌ها و آدم‌ها» شاهکار جان اشتاین‌بک، داستان دوستی عمیق دو کارگر فقیر است که با رؤیای داشتن خانه‌ای کوچک در دل زندگی سخت آمریکا پیش می‌روند. روایتی کوتاه؛ اما تکان‌دهنده از امید، تنهایی، انسانیت و سرنوشتی که نشان می‌دهد گاهی زیباترین آرزوها، تلخ‌ترین پایان‌ها را دارند.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/671827" target="_blank">📅 20:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671825">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WO2jYEpBhT0KgzWf4jNelZqtEUygBb__ICappL3nK1P9ydBK-oXBHnY6HTbxN52QoVmEjIL-Nb6v8ff3nGJr7xDR5Pt2ao-LKeWKWpPUlzigEvx6wYgM-W7fjadBqAv4Jx18-hGi06lRgUSV5zmQqa2WLzcWOUOGHktUPG2rDk9zYHt5OwegbaiLR56pOHCSNxYK6anMhp40GI6WEh2paT8frDQs1kGZJJGQI7GzVimYH22YF-DvIOP0jZU234YfFZCngRuQq2zP3tvLPX7N56ow0yKqjAcI25KytirUZ9wfQZG8d9LM55PhWbNx3WfZXpibk0BrdqYepaI7YLA_TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/671825" target="_blank">📅 20:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671816">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uv8kDUg0bgzvlZEyH6pfipYmFSI3xM0chFpX0uxG8oykpdqV4TS9utFzwqgo5V-keZv4E-pyEyq-8Pa2MrMl0tuFLTLwgMT860c5nbO0TmiHDWAeaTsvj1BDjhaE_FSzkFq3geCG5-lgJhRAgNPXV2N374kasMjFDASafBPpaE1BUoo1vCEBniUEgTD0_K7q2zOOi_iW78hfQ93037CkhFVQStVI3n2Q318CPt3Lk0IYxBxRZfCwVIq6d0xT5ztIUW7ErPAOYHe6cWHPD7D3U9RR7QQ4xcThpbRMJ7kN8XXbNv0mwDq6E4nJSqZ-Vmrs35m7mEdfgcP2xtM16x1sSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GKoPNjO5JWQ-R7g4wAQSv9yyTboMISYwVkD_iXZkcOdndf4aWjRrTViyTaWtB0so3aZX2p26T7pBqJMgKk7WJkBB7LG00kVp0PTOSgJrAnq87zAwrAWsMVM8nYRDSPhWrueOC3nvvjm2dlo2n9AEf8_uVCl_pFMv9nrouw0S46_vDwV46koS65sw5Gm35NIKFWLfXi3vF41cLr5T3SlFTkiqOGJoK3kxkHFhPJ_a2AVJ2enPUTW2KgWfhK2Vc_BxPA5axpLuq0YvMsqPN4nRnuDi3T-FqYv9M-BBpag7TO4PJe5stk4SIXoNIvlBMqVFA0i1Zb0hdy01ol7DbULYqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DflpwvQc9ijOpLNLPa9sjfDuF_tq2kuZD_czgahhFZjtUiJ4LueFVVtjIIcp0Wx20fsDSWCUZVwoT6SJPSlmzhIfDtVxmRAWEpWyFVh3YfVKB18i-jfvWzFeHXwdbHNCe-ORSbzkaeRvkPs87j2A_7fGhWIolKsfLBb38oyvLlRNwPzxXWkloRUztRK9dOUJu7xn6QUR9tUxNX_5t7HYVkXjjan6W-Mmolpq2znQPvlyHLreFbDGbSiRV0Iata6E6z3Qpo71aqkUo9P1R_hv9L8qQeezo7u36hmmw3c88hfiFtSlp8M6JuezNEG-guB-hJjiLj3TRHJULVRGIZ4aNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/neCza6yIZ2vDoJ7mIoi7o_o7LPFFuaeMB-VI7ypuf-PQFLCW45e1zm5-MM5vXGs6NpYe4GsApAmNSlvsJn-SOpwStQ7XoN1mxL6YWr7nBXKUd06pA4-zG4tEYD2JI0zcl7v_fMSaeMe1OfOspF6EqC2XMydBH2Uopiu07mq29W6oH3Pur3-oNWFoF9fs_18V44gJaEXKwAO2W9UBguFpZ6Ek64FcXCmzDxotefusNVAtzCUxkZP4I-7lmXz9dcPyBSl94EiO35bhgu_Bc44AJ4xAdj_074KVjD-sAY7thnDveLIkywq0ui4ikS6PByurLduqGG-5eUs83jX_FFaB5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgPhnPCHKkLdx0-dQx5dgtyFW7zAsdhx8yqlB3U8Q15Oo-gODHxK5xYWFSGCfgLeqi1VhLC6NCXZbm44u-zApx2_fSJATJiP67Xj42ar9lq0slkRFkKHo9lNmnarG_9Jacwmg384TJLsZGWhTRLt_tb6mWNF_rtzCL2To51n34w118Stge7xIrpChJoHMGHZpTuZqjAbvzNpqft1R-xmiepbZSTHXb9ckN3F3HxbQ2hHZWVvb8afJkmIK-9h8NKSTkpnl4s-pWUDhGMtg-PrMadNie8RuTVW3Mh_gYsqcEvcrwZvtJlRR5MTtsnTXPBXWDGloAdKPGe-R3vPvFkdzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CrJouMYseQF1XcLHk9Nv21GNsUvCG-n5DED6721XN8IiYG4Ym_LvF55Zq_LPEdabQo5MckEph4Z9ZjkIB19wjFQpyaF6AenWs5_eLhOx7LlB1XHZoqVXDvhSDRhaWsYcfW2Ef9ALh_6w1XnI1jY3d9rXGV5h6R2e05Qw_aB7SpIZQxdVgu-4NVsIHg0dfQei_lzsde0GFhgQdz8h7-RyAxKVbg2rnOszn3Mc_4pK-FTBVdnbt66lOH_7utWOokp-kHkjXPaThTic8K9bEDrOlS0gABmVuNpvvIFveSP5O8y5Hioi0Y1oAgFpwqficpK4WwHmhNV5pEDXuxwF1I6AIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y-paU13PjKfNOUhvrpzy1tY0v-V2HaTum3n1xOm9Z6LKnEouIq56tNb5p3hN-JS-tLf3X7_f0ATMj9FbKGZIowGr81u5RX0cyiXJu7XeojT-r67tV2pPp_hZreMHeoRE7P7QLVu-AQcWaH2vFPEkzeujuNFzzL0FCFK13qWMl1uIxYlo2qxby57HhWDa8Cd2W9WKelgTgNDa92tVZtEhwrfJEYHN1zunJcjkwhWW0nIMPx-5M0ItBpHDWlz5oP8f7r_mBPU7UXSbVrJmHzPakaqBaqI4ot40cOEovANh_aYaYuMxjhcGsiigb_4U_bL0M8Vu37HMsBKQjX9xZKoJCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkWOgng8n-nPPYmIVA9GH0ofV5yZqSra86HtecwmuEzfWF783w-ATPmXca000gZ7GwDHtNRuNzXl4cNLnMe35oNlx1GgDhSl2AZXoZj4cX-Nr5bDAu5yGXSjf-dXEfjsCdGtv7HfDHjw1W3HXgcQaSd1RJVOAfJcXwSIE2wfoaIyHlxB9MnL7SEY-v1fVWkXynhnO-4S5iY_Utb_Y9aXUiJHL6U-PZSNw0QGuc21iHxHHJTJd6Hgq3QfZP51HbCkrgnrVoNLPwWYlGxviKUAvtTfr6N0REUppDnu1M1Vvz8v_8bvnieKumwDIZikRF1LVBsHQJzFkWiI2m2Y16VOmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h7PGKpj8cmdM7oOtWAuwZnQoCI-pQTGgB1FQyp2G9TMl7JK2y7mq86fjnFHTHzgjIxcwF_J3kBKdscF8lNPASyzuNK147QWi0t0mt8veX_I0moYfx6zdfHap2uKmMol6LPJ9jtIOr5Qw9MdbExz4cdiFNAGEsKAtmDRK3-EqjDFeLn4rjAE8mhWXZxjoHwTWS982sewMptluhEELM0jQqlXNTwXCdYIQwgrz6rPfANWNq4Qi2-d7RQTdqtOuYj7W0mqnoXteQ0M20HOiz3JCFpo-gnK5uRuiOmKaIoFFPRj2UD9XJcDeqVjWJVsa_u5jBPVK-I0b1jcYlVJJW8RC4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گزارش‌های ارسالی مخاطبان خبرفوری در خصوص قطعی برق خارج از زمان مقرر
🔸
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/671816" target="_blank">📅 20:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671815">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToXI24VLPIcqW5wuuWj-FX4kmdpaez0Qw1H8l4EEqxbrB_5Y56pxdI8gGFnFDt4-3wC7BTDsocjOwhwzqiRjpiU5cSuSiILHTmyoJ1thqVPhETJosWTdgZ1jRwEFVpOvBsdxViHkiMozq-MCBwEMa7kpuS5ImYlge4hBd1P-kdmO1isEF1-X15Qi2Nw4CnnAZRMOn3d2JaSaeOYBOLkhF-VApHEIphVai2LZVIONwg7zyFmO6zjG_Jr-NA0_xf52lJy7yQcjbS84cuNKsahYzonliyYixw1dXZrU1dBnOgnU9q940T4rxJZDoY9TDVvZ-u3T7WacQASgwZE0OX9p3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخبر: دوست دارید کل زنجیره تامین انرژی منطقه را نابود کنید؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/671815" target="_blank">📅 20:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671814">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mStYD4vhp7XL2VeHEVFUxtKK1-DRcWKb3pN0r8XbklJxKjaa5dD2jWLCu5J2BR3sbGW5H6m72m6irWn8bnVu3FNn8SS7qd2rHFNvS2A4JCayUucYN52Oyos6F6u_TCpJgTH0ruCGaSSDYrPv_pBd-vudHGa_a72GmAXodN7jYszYG8z-RHkQJRLSFBrmzzjNXfgbpfGPanmm0Vt5WXK9kZYhPGnwvKxbFDLzPidFk-uG2DenS63GpUXxL8ihwlehVJM1ULkEnfjYNJmUwZFXRvQf9bWkW5tbBwmDNOUzXmjYlmKO9xNzUiSQTFnSlYtXqb_twRHoMx9B24j-_LkBSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور سردار قاآنی در مراسم بزرگداشت شهادت رهبر آزادگان جهان در چیذر
🔹
این چندمین حضور عمومی سردار قاآنی پس از آغاز جنگ تحمیلی آمریکا با ایران است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/671814" target="_blank">📅 20:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671813">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogb6uzat6oeowi1462T8f1qlVyBvgG_BEST0n9170-YTmi961YGyQQFgvludGIN2l5RgwI0QD8YzFN3G077X5FE7-0pqOFqk9UBb-mFOPkHGW5N_7M7wuE27FeU9SzPs7v_3vpO-BTqGJoxX9sPfTGvcstDyvPS5Glekk0pa6oPNhwy8ZVL2_xGUv2kmc4p8oAtTH5IrBcIix3-uNkeP9UwH1FIGyKVe5KK4wevIo5SPvHQEb_7jp4TiiBTx2TaezlxOeuJteT8hOdcOP187tsD7LfUADvhLqj4cZfJJBHnXnUkQy1y_XWvL_Q_DdPhE3bDCU8R3pL5vWmrtxnETyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز خیلی‌ها فقط یک جمله گفتن...
«کاش زودتر اقدام کرده بودم»
💎
اجرت از ۳٪
🏦
خرید مرحله‌ای طلا از ۵ میلیون تومان
🔄
طرح تعویض با عیار ۷۵۰
👰
سرویس عروس از ۱۰ تا ۶۰ گرم
📲
مشاهده مدل‌ها
https://t.me/haghgo_gold
ادمین :
@haghgogold
_
__
آدرس شعبه ۱: ستارخان بین فلکه اول و دوم صادقیه پاساژ زرناب طبقه همکف پلاک ۳۲
شعبه ۲: فلکه اول صادقیه زیما مال طبقه B1 واحد۴
برای اطلاع از موجودی تماس بگیرید :
09924100036  ---  09924100039</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/671813" target="_blank">📅 20:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671810">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
اصابت پرتابه‌های دشمن در حوالی بندرعباس
🔹
حوالی ساعت های ۱۹ و ۱۹:۲۰ نقاطی در حوالی بندر عباس مورد اصابت پرتابه‌های دشمن قرار گرفت.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/671810" target="_blank">📅 19:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671809">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ti1s7tGFYaYXOAxVWgEcjliGxGx8fP70BC0us50Wyk7CQDNDColLqhHKxqEPz_rbQmZMNQ5WmouE6o4jVDxYaCKZKRr94ShZdBryX6WCbhGXSWLovF2ddGzosmlBlWa_U4GrdDVHhxPyvWdcoD03LnBW3YJftEwdY_YjHJcnPBM_BkTq3PtW94RIjIMiAMy8D7vMEqEZeeqP6i9hnd3nbvrgIkE7PjtNu-kU2rgAGPCk38ElJybnfqIhK7O9C8DuCR8iqH-V68zdLBsg0zlJInzR31EVQp1OJb8ZWILXtjyyLiodx6gGRmxFp5FzCzVpJDpSyXmBnvB4jyJma7B9aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مردِ آرام در مهم‌ترین شب فوتبال | علیرضا فغانی؛ روایت صعود به قله داوری جهان | از قضاوت فینال المپیک تا سوت بزرگ‌ترین بازی فوتبال
🔹
علیرضا فغانی، داور پرافتخار ایرانی که حالا با پرچم استرالیا در رقابت‌های فیفا قضاوت می‌کند، با انتخاب به عنوان داور فینال جام جهانی ۲۰۲۶، به یکی از معدود داوران تاریخ فوتبال تبدیل شد که مهم‌ترین مسابقه جهان را قضاوت می‌کنند.
اینجا بیشتر بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3230845</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/671809" target="_blank">📅 19:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671807">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
صدا‌های احتمالی امشب در نوشهر مربوط به تست شبکه گاز خواهد بود
روابط عمومی شرکت ملی گاز مازندران:
🔹
صدای مهیب احتمالی امشب در نوشهر، مربوط به تست و هواگیری گاز خواهد بود.
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/671807" target="_blank">📅 19:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671806">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVK6r2TiX1EIeoMkIIPqHfqK3IC7BWj2gRKF37_xZ5H2ALZIi9Hm1j0xYANiP67A6vYiBSSwKDbu-d8YywPGBvbA7sdpueZ1Xb1zu93lxP11N6wjeWBAS-V2e-t2I-UV22sDn2OAs_RFx5F_Bx6IJA2ShQVi_XWTOsSijLwlTxHkD4IOePPig6Nquu7dLyeW7vYC4XGArZQulyL1h4AkHgvVIr_o-82nCZtlDTgtncVSPEDy-b42_rMqRgSeJKs5o-_v88ZuctOeE-BlYT-GGFW4Dm6oWEAZLaAKQStlG1YgPmZMtH1A5XR_5WonkT-uHnQ9JEL5zmuzLvm-0b99Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فهرست جدیدی از ترور مسئولین آمریکایی اسرائیلی در رسانه‌ها منتشر شد
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/671806" target="_blank">📅 19:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671804">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
استانداری هرمزگان: در ساعت ۱۸:۲۰ و ۱۸:۴۰ نقاطی در حوالی بندر عباس مورد اصابت موشکهای دشمن آمریکایی قرار گرفت
🔹
بنابر اعلام استانداری هرمزگان، در حملات جدید آمریکا به استان هیچ مصدوم و یا خسارت به زیر ساخت های مسکونی و تجاری گزارش نشده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/671804" target="_blank">📅 19:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671801">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f50a9527e.mp4?token=Y2BuZLtjcD59eDR8zoGNNAu3FaZKwPBeC87Oqt8WDd1pbimHQAMBzq2IZWDYWBtuHwVFqNylCOIdjtvN25O-ezfh1InweKliwM7pdqp6-24X6XJYqlPQVGLsQ3w2YP9oBP-vvHGs4ySqr053cuoROD4UYop87GqmGSI-TucMSwAgs4iFRTxZvBAt92GqtSyKzyFMCntkQbs7gt9Ei5yKzBr95s93hbs8E6Q-fjhj9wUoitKUjHLcO1GJDSyvA_rEJ5H1fKJ9fGsVv5WJLeDUaVxxeFoOgVW2eAam_gtmzSHX37H-qpDVyGIUcvbdpGEzBHaXIzRHWlrdw3o7E3JyRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f50a9527e.mp4?token=Y2BuZLtjcD59eDR8zoGNNAu3FaZKwPBeC87Oqt8WDd1pbimHQAMBzq2IZWDYWBtuHwVFqNylCOIdjtvN25O-ezfh1InweKliwM7pdqp6-24X6XJYqlPQVGLsQ3w2YP9oBP-vvHGs4ySqr053cuoROD4UYop87GqmGSI-TucMSwAgs4iFRTxZvBAt92GqtSyKzyFMCntkQbs7gt9Ei5yKzBr95s93hbs8E6Q-fjhj9wUoitKUjHLcO1GJDSyvA_rEJ5H1fKJ9fGsVv5WJLeDUaVxxeFoOgVW2eAam_gtmzSHX37H-qpDVyGIUcvbdpGEzBHaXIzRHWlrdw3o7E3JyRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بر اساس تصاویر ماهواره تجاری سنتینل طی حمله پهپادی شب گذشته ایران به فرودگاه اربیل، آتش سوزی و رد دود در محل استقرار سامانه پاتریوت امریکایی دیده می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/671801" target="_blank">📅 19:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671799">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3G_Cotjoqrg1Ckbpn3UN7beakybEmqnZ0bJuivOP2aGgQRBWmjYFd0AmUJbYQeYFSSEoYxmsVagh5hnXSn89u-Zt6_yZ9JE5pG6FsRnGPAV_b798LYH8erOBQnTQ7n-qaMaoUA-7orFJ2HwI5l5KXi6U_SmLz6EO2O-6L-ANbaQJRVBhzHNuJ1Aa6GwuazRqHhogvau0G42fSf8L9_aT0w6cnIrgAIyPxv5_Frc07b6WCzEpSWP3toPdxcpifc6cptfuK_Rf05r3c7LqFwfsvPhkngBFFp3tZ_mDJhvwWbaws3qj2rOaDLsBTPf800j1qsd43Yhg7HOnH2GIHwrXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین عکس از آلوین در سری جدید "آلوین و سنجاب‌ها" که ساختش شروع شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/671799" target="_blank">📅 19:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671798">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qca3mpXB2bFP5imyH3NEFxCP1q0cCLpElNHp9d_O_T1307s9nsD5T_0oro6f3uh8zap2xC9OldxfDzWVumvfUhJJ1d8Eydl27FETEOC_RtCdwAncsxShId8R1NrasJ0hbciIe3lfvTA3TE2xvWMla10SoWwlrDfUze1JuPU79jXiQ4JuHYq-Sllu9v0Yw6IlLFPCNHIPTDyxuc5D9ZxWJ8AMp4HBCAviu0_8Djh5S2ueH5hV_eWWqO8ASI0KoZUm6OIrRTQbFp3mRKSH3WbNa9cX6JxW3BYS3gjtYC1D2Vb_mkv2XYuepzauWFFP-jnTIfGPRrKTAWVm1-rX6WttXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/671798" target="_blank">📅 19:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671796">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUv8dUV2mw5Re2SG9Qr202l3ZXxJyGWkT3ckT9NthxvqvkzAUEzKvSAyMOyGSX9KIms73RPnCqmIsjvY7JDsB4GjLS60JAgJW9x00s6kFVWP4EEYTv1Ddm9QTn8YF3Xp5aaJQJx1Nfcfe37AdpjsFNAQsdSNmDAodMLA6ocgK5Y7bEgclB7h7NqH4gzSfrDXZrMnGynuBzEO0GP_93ufJ08ZdjgCnio8-iHS5LJUMese37p75RFUFZ__Sywbbk3bWyntkWWimEiJ016tUB4xVQIHCrbBkFcfAIV0xE75FAanR6HQHLGLFob_8RI1HF72bu5l0Ja27Ah_c8bDsdV5BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بدهکاران بزرگ پای ثابت بانک‌ها را بشناسید
🔹
بررسی آمارهای بانک مرکزی نشان می‌دهد نام برخی شرکت‌ها و گروه‌های اقتصادی طی ۵ سال گذشته به‌طور مداوم در فهرست بزرگ‌ترین بدهکاران کلان بانک‌ها تکرار شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/671796" target="_blank">📅 18:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671791">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/251b490de0.mp4?token=o3hikr4WKuTtofPDTx2TGLsfIicgMiid61Q7WQ0uvgorS4gVSOdQ8GV9QofiIj1U7E3rzftXTH8hdWfFZtTItim9_Tv5EH5OPplMYuqbJkxyjHQdlcUeFo38N8AS44Ea6gLbjb2PihiZcg3yC6Jl_GMn0pngMJimULWXYljtEK6NFyp5K0gsW9_oPqNsK2kfmlKqkrDBN1ybu-Xgtf0igMJUfeykV2ze1kqHRL8-C7tMkBEGAHCHpT_2CIDkqKvASkXNnAbb_si8gDc7OzcfseWjtnuzYPkRrQX14mVeLAA_Bu6rG2pX75gUn-8bxbrvVF8VDVH-gdUPaeAhE1lllQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/251b490de0.mp4?token=o3hikr4WKuTtofPDTx2TGLsfIicgMiid61Q7WQ0uvgorS4gVSOdQ8GV9QofiIj1U7E3rzftXTH8hdWfFZtTItim9_Tv5EH5OPplMYuqbJkxyjHQdlcUeFo38N8AS44Ea6gLbjb2PihiZcg3yC6Jl_GMn0pngMJimULWXYljtEK6NFyp5K0gsW9_oPqNsK2kfmlKqkrDBN1ybu-Xgtf0igMJUfeykV2ze1kqHRL8-C7tMkBEGAHCHpT_2CIDkqKvASkXNnAbb_si8gDc7OzcfseWjtnuzYPkRrQX14mVeLAA_Bu6rG2pX75gUn-8bxbrvVF8VDVH-gdUPaeAhE1lllQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسپانیا فقط با فرانسه و پرتغال هم‌مرز نیست؛ از جزیره‌ای با مالکیت شش‌ماهه تا کوتاه‌ترین مرز زمینی دنیا، مرزهای این کشور پر از شگفتیه!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/671791" target="_blank">📅 18:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671790">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
افزایش ۲۵ درصدی مشترکین خوش‌مصرف آب/ سخنگوی آبفا تهران: آب مشترکان پرمصرف قطع موقت خواهد شد
بهنام بخشی، سخنگوی آب و فاضلاب استان تهران در
#گفتگو
با خبرفوری:
🔹
وضعیت منابع آب سدهای تهران نسبت به سال گذشته بهتر شده، اما هنوز با شرایط ایده‌آل فاصله دارد. مصرف آب در تهران بهبود یافته؛ سهم مشترکان خوش‌مصرف ۲۵ درصد افزایش یافته و سهم پرمصرف‌ها از ۸ درصد به ۲ درصد کاهش پیدا کرده است.
🔹
مشترکان پرمصرف در صورت اصلاح نکردن مصرف، پس از اخطار با قطع موقت ۱۲ تا ۲۴ ساعته آب مواجه خواهند شد. سرانه مصرف آب در تهران ۱۹۵ لیتر است؛ ۶۵ لیتر بیشتر از الگوی استاندارد و نسبت به سال گذشته، ۲۵ لیتر کاهش یافته‌است.
@TV_Fori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/671790" target="_blank">📅 18:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671788">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVjguHimMcARc9pOs3mNt0LxBcTgI3hb1M2cW__HkAo7wF9iDd3o9U4KJ4yXSiYFdteR8nHCgB5dYcESkLxrqtAQue0y2QUdzBkszHfrERZ16vHnhlTIZjs7pYBso7uvBNUWS27FxpWhT7am8LmFaVOBfy9uOXyXF58Yb7UtBlV2e4aq9k4KfR-kISHvE7BIpBCZEKo9P63pkAl5st5azoDjMzWqZj4NWDmAAxCPagmapOeb0HkymrRuIm9JWVgjVe41PRyIyZSTZgPfjHODzeUZ7Co5V4-5csg6PCE6nHpNhFxyiMmQqH-kuqS8iZ_iO-08lF7uOnkQnMSZIQn0qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مه‌لقا ملاح؛ مادر محیط زیست ایران
🔹
مه‌لقا ملاح، ۱۰۴ سال زندگی کرد و بیش از ۶۰ سال برای نجات طبیعت ایران جنگید. او آن‌قدر به باورهایش پایبند بود که گفته می‌شود در شش دهه فعالیتش حتی یک گرم زباله از خانه‌اش بیرون نگذاشت و از بطری‌های پلاستیکی یک‌بارمصرف…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/671788" target="_blank">📅 18:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671787">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a5942b565.mp4?token=eTP1geWcFpPZ0Tdo4uM3772TvUc_tzUx_9cg9BWI3vO7LlqU2olWF3R2Ic8V4TKNf8m-uWSko6dXMFYX_LT7G-b4yYSGSmmY7kE8s5sqGORExTeNzcohMGuUA97QzFgU0RueKZEe37JHmx8ISqEjcuOir_WlHEaMCIvvpVuD0M5RFiKqr9KP6gd_zKJqDbh7JKcYmLNVxkrTvyxehHVnpKiWq6xGmIsyDWrAqUBocJSbDyOMNs4hXPDeftoEd8WLq06tfpp5lmISacYZV0wMkDdsFE3NJeey4ABpC5M-xWcjc-TIZhLTogNfnVqilIAJMblQuldHmbmeifUXCzEcqwfQi1203z5fIuQ1Z4G0bW3dr1jtKt6RqEGpw3YNyXluytedYlWuRPdQOi3SM_loeeFKlWN0OXWXyf7huDO_yezAttrL9EstJtSqiw9RiRhkn8Gi1SxNYEG_L5hTz8zkz3ZGI5X849UmYZmovuf8wd1WG6SXywqhlX5grK4IW7IWzFZqKdjT0Sda6pmj_MXLzSdvDRhm6bUu4gPZtkECiB38GCw2WkAEbtaEw9njaEG7YRfaz_7KpKx3_NOkHdLUrIVEOk_tu4lJRRjKzievtFZL5AwL-tG3-lOY-3-bDlKzbE590fxAw1qzBKxkVRc11G7OF5vtjXuylhdZ4nVgPTE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a5942b565.mp4?token=eTP1geWcFpPZ0Tdo4uM3772TvUc_tzUx_9cg9BWI3vO7LlqU2olWF3R2Ic8V4TKNf8m-uWSko6dXMFYX_LT7G-b4yYSGSmmY7kE8s5sqGORExTeNzcohMGuUA97QzFgU0RueKZEe37JHmx8ISqEjcuOir_WlHEaMCIvvpVuD0M5RFiKqr9KP6gd_zKJqDbh7JKcYmLNVxkrTvyxehHVnpKiWq6xGmIsyDWrAqUBocJSbDyOMNs4hXPDeftoEd8WLq06tfpp5lmISacYZV0wMkDdsFE3NJeey4ABpC5M-xWcjc-TIZhLTogNfnVqilIAJMblQuldHmbmeifUXCzEcqwfQi1203z5fIuQ1Z4G0bW3dr1jtKt6RqEGpw3YNyXluytedYlWuRPdQOi3SM_loeeFKlWN0OXWXyf7huDO_yezAttrL9EstJtSqiw9RiRhkn8Gi1SxNYEG_L5hTz8zkz3ZGI5X849UmYZmovuf8wd1WG6SXywqhlX5grK4IW7IWzFZqKdjT0Sda6pmj_MXLzSdvDRhm6bUu4gPZtkECiB38GCw2WkAEbtaEw9njaEG7YRfaz_7KpKx3_NOkHdLUrIVEOk_tu4lJRRjKzievtFZL5AwL-tG3-lOY-3-bDlKzbE590fxAw1qzBKxkVRc11G7OF5vtjXuylhdZ4nVgPTE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
این روزها با قطعی‌های برق، داشتن یک چراغ‌قوه معمولی کافی نیست!
🔦
چراغ قوه دستی ۸ کاره LED Torch
هم چراغ‌قوه است، هم پاوربانک، هم ابزار نجات!
✅
نور LED پرقدرت
🔋
قابلیت شارژ با USB + استفاده به‌عنوان پاوربانک
🧲
مگنت قوی برای اتصال به سطوح فلزی
🔨
چکش شیشه‌شکن اضطراری
🔪
تیغ برش کمربند ایمنی
🚨
چراغ هشدار برای مواقع اضطراری
🏕
مناسب قطعی برق، خودرو، سفر، کمپینگ و نگهداری در منزل
❌
قیمت قبل: ۱,۴۹۸,۰۰۰ تومان
🔥
قیمت ویژه: فقط ۹۹۸,۰۰۰ تومان
🚚
ارسال به سراسر کشور
💳
پرداخت درب منزل
👇
قبل از قطعی بعدی برق، این ابزار کاربردی را تهیه کنید.
https://memarket24.ir/product/brief/30291/180124/</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/671787" target="_blank">📅 17:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671786">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a755c6a7f.mp4?token=i6r4hN32hMbw7m6cjItq13CFx8qH5BwHTteMnspliRuO8b3XUr9TDFc7n1kLHN-UmNffNJabaf6ZD4fsf0qX81_SehGfq6T9raqETrNFUCNzdRTjmSGOrzKWp7BvObEAzREesw_hJIMoEovFZVc35IAnrtVvsip8JcRFDp2jmSMF_McDfjKZMyXWacZSKPuiBX6ZHtVX46_0SBe_Z75uBzk7wlUT5JSEjnzmNb2Dqbylf-pTv47rqKrETDWTrSpIAmi6FCzHQnwLad46idvR_gyfaa7P0hE2YeI81BbZiAO_CxmGU87FXh858yZd_eW1boybeoyeMqlqhz23vhtsQFbGSn8ygczf31eBQEdW331_YFX8MAtoN5MLP3t9AiD36we291yFNG4shd7VJpeFt9jKEEku2bvnbwmJnw_EhNRaVkGl615XhScN4Yr3fS6RRuF4pcRwQD8fQBGkLTCc7i98HMpuE2P-OIvltU3pkt5uVamazeKjIvMl6CRHW8BgJ-hH6KWUc1A_e90weTGQP8MQkNguFXUHabJOunKNOPeVUO_UGhh9RErI1P1d0Jr3XCIPF38lE7Qq9mtjrkK49vVFaXjkIpL0Sbt4qX0vBa8o0pRP9YOktnmgniufeuXfnouD62HzeITDcwQLNGft85i9xr2q8g6gJDSp9zzOhYk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a755c6a7f.mp4?token=i6r4hN32hMbw7m6cjItq13CFx8qH5BwHTteMnspliRuO8b3XUr9TDFc7n1kLHN-UmNffNJabaf6ZD4fsf0qX81_SehGfq6T9raqETrNFUCNzdRTjmSGOrzKWp7BvObEAzREesw_hJIMoEovFZVc35IAnrtVvsip8JcRFDp2jmSMF_McDfjKZMyXWacZSKPuiBX6ZHtVX46_0SBe_Z75uBzk7wlUT5JSEjnzmNb2Dqbylf-pTv47rqKrETDWTrSpIAmi6FCzHQnwLad46idvR_gyfaa7P0hE2YeI81BbZiAO_CxmGU87FXh858yZd_eW1boybeoyeMqlqhz23vhtsQFbGSn8ygczf31eBQEdW331_YFX8MAtoN5MLP3t9AiD36we291yFNG4shd7VJpeFt9jKEEku2bvnbwmJnw_EhNRaVkGl615XhScN4Yr3fS6RRuF4pcRwQD8fQBGkLTCc7i98HMpuE2P-OIvltU3pkt5uVamazeKjIvMl6CRHW8BgJ-hH6KWUc1A_e90weTGQP8MQkNguFXUHabJOunKNOPeVUO_UGhh9RErI1P1d0Jr3XCIPF38lE7Qq9mtjrkK49vVFaXjkIpL0Sbt4qX0vBa8o0pRP9YOktnmgniufeuXfnouD62HzeITDcwQLNGft85i9xr2q8g6gJDSp9zzOhYk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ببینید؛ انیمیشن ترامپ و عربستان!
🔹
رویترز: عربستان سعودی به ایالات متحده اجازه داده است از یک پایگاه هوایی در فاصله حدود ۷۰ کیلومتری مکه در جنگ علیه ایران استفاده کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/671786" target="_blank">📅 17:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671785">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
حفاظت امنیتی نتانیاهو به دلیل وحشت از ایران  مادام‌العمر شد!
🔹
کابینه امنیتی رژیم صهیونیستی در پی ارزیابی‌های نهادهای امنیتی، با طرح ویژه‌ای برای تأمین امنیت خانواده نخست‌وزیر این رژیم موافقت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/671785" target="_blank">📅 17:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671783">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
صدور کارت ورود به جلسه برای ۵۶۱ هزار داوطلب کارشناسی‌ارشد
🔹
تاکنون بیش از ۵۶۱ هزار داوطلب آزمون کارشناسی ارشد سال ۱۴۰۵ کارت ورود به جلسه خود را گرفتند.
🔹
از بیش از ۶۵۱ هزار متقاضی شرکت‌کننده در آزمون کارشناسی ارشد سال ۱۴۰۵، ۲۴۹۷ نفر از داوطلبان توان‌خواه هستند که برای آن‌ها تمهیدات ویژه‌ای همچون منشی، وقت اضافی و دفترچه بریل یا درشت‌خط در نظر گرفته شده است.
🔹
طبق تأیید سازمان بهزیستی، برای داوطلبان واجد شرایط استفاده از وقت اضافی، زمان آزمون به میزان ۱.۳ برابر داوطلبان عادی در نظر گرفته می‌شود. این زمان اضافی صرفاً به افرادی اختصاص می‌یابد که وضعیت معلولیت و بهره‌مندی از وقت اضافی آن‌ها به تأیید سازمان بهزیستی رسیده باشد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/671783" target="_blank">📅 17:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671782">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5784417b.mp4?token=bk9OmrZlN68QiVQEOCClzEWId6GM2oDKPWFUv1B9W_twPRrV3Zzac_YwTwBQ_KV72CPLrEMtwAVsBuz_XTYdxQQJzO_bH0_pm_FIjKd1N77zk0tocvyvEoQIHUxXCrJzc_BszNtVbpd4ml6ly2U3Sdi6FsG2OusB6FuNl9jLSsC9Rzu4Qf6sGxZ0cuEN3wS3dagbEb0S9EFw3nrvID0XiCiyyglcgLrdYM9oiRH2jPIjZi-osS92DdZ51FLFjHOwsjJDiBbDBvQhfKs13TlAGZYcZNOEoZCkvC7OqmtHug4ok1oTys3mxf0w3MM8zI5rWBTplh981hTDXOsWUXvIpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5784417b.mp4?token=bk9OmrZlN68QiVQEOCClzEWId6GM2oDKPWFUv1B9W_twPRrV3Zzac_YwTwBQ_KV72CPLrEMtwAVsBuz_XTYdxQQJzO_bH0_pm_FIjKd1N77zk0tocvyvEoQIHUxXCrJzc_BszNtVbpd4ml6ly2U3Sdi6FsG2OusB6FuNl9jLSsC9Rzu4Qf6sGxZ0cuEN3wS3dagbEb0S9EFw3nrvID0XiCiyyglcgLrdYM9oiRH2jPIjZi-osS92DdZ51FLFjHOwsjJDiBbDBvQhfKs13TlAGZYcZNOEoZCkvC7OqmtHug4ok1oTys3mxf0w3MM8zI5rWBTplh981hTDXOsWUXvIpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک خوراکی خنک و دلچسب برای این روزها؛ با طالبی و انبه هم عالیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/671782" target="_blank">📅 17:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671779">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
توهین بی شرمانه ونس به ایرانیان : اگر نظام ایران سرنگون شود، ۹۴ میلیون درمانده تروریست به اروپا و آمریکا سرازیر می‌شوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/671779" target="_blank">📅 17:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671778">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_48phjmJfMSIQczm6rdvj0_2AG3Hw6VkahrsUgrHmxsR1y9ehQ1zxQn5C0plgkNKXKF-6SmX2En4R87LkQuQ3Gfw7UCO-XFEElspgOohH6U2QQ7qPy8qNUvinbF8gCTrr2pUZKmPZWvq49DUiFUPnfEv7A0rjIlf_smLJbyS6YkpzIYHNQIthezLZtMrFD8f72iAuRrtuWGXkM-enXNkbyFaZhq6tIpRpv0y1jMC1O0fTpvwFaemumyW-fTKqStk9Fr1rZtbBOypAnE_vj0rXLXgnVUcs69POk7NKQ-bCb7FUOb1Gr-6jETjvszau1CFW5hY29tVMwCjL_0FmRP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت داری؟
پس مدرکش هم باید باشه.
با آزمون تخصصی آریاداناک، مهارتت رو به گواهی معتبر تبدیل کن و برای استخدام و رزومه یک قدم جلوتر باش.
✨
آزمون تخصصی | مدرک معتبر | رزومه درخشان
🎁
کدتخفیف: aria25
🔗
ariadanak.com/ariaacademy
📞
مشاوره و راهنمایی:
۰۲۱۲۸۴۲۴۵۴۳
۰۹۹۲۶۶۶۸۴۲۴</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/671778" target="_blank">📅 17:02 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
