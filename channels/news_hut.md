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
<img src="https://cdn4.telesco.pe/file/KVJmVVMvGxE_cIvCwsou34InN-tKimzrVg4jeze_6Z3DB2NGfPLzHAPoSlndf3vfKL6zIXWCHfIPh3QFeeI_yyGC6N3jB0_gh1rVdnS3EmufVZ4K2cVCK4CSJR5mUtLGZe_Uw4rT4KqkX8WJrEr5Ol7s5drh4jAh_odA9jJnekMGlNae0q9N4euogr3yTkAlg2Q7R6ZCC5pnYjhLLHjD26WnDKwUs0jirs_l0PpWrRxCaD1imNcDsfnHcqeSbhJLjdz629xi1hgDgx7mFBzq9uxcadwrIEJnDp_m8C-3q22Td0X7lj74pwAtH-GndMkyhgcDkMwJu8UbGyJYRZpmKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 13:40:22</div>
<hr>

<div class="tg-post" id="msg-72113">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHZ0uBGVXfc4yVBymTJ9OFg8rDFslmH1mbECxWek44iGWPfL86BdKcNt5A-HN6JYMUC9DX9V-YAacIZD94KYG90LXPBzG08LPZjKlElUa6h8Rm_wM4LcWtGzKUTL3jrqqHEeolZMr5AwrXrjDVv9D-VhSrVI8crRq1ECo1eg9Gm5dxzQivguquIg--C2A63MkOF0SL46fOwQZktLrRJrAlNlxaBbh2oz6k1Rmnw2H1gfHk9fHkGpP6u94FrACgMqvYBjqpgI46aoNC7er5us1Q912tTqvZzM7LpWwoI7HIonB07H3KX_XOFma_BvtXYOtJ7EDqjj6qYsHVwDwWFCEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بازنشر کرد:«ائتلاف نتانیاهو در تازه‌ترین نظرسنجی انتخابات اسرائیل پیشتاز است.»
@News_Hut</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/news_hut/72113" target="_blank">📅 13:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72112">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/foADMWJC8ZipsZ_fhlX-ND1ald90TeqN9vObvN9QdwuRGUcQd0Tr0nV8DgToKeHp9tMNCdJVStDDXgiQMnAEYFur75N-Wf7vXkFPv_6rv5X3W9QDbGIUkrZHSayPTcdCu58WWzL0oc_rAdJx4AGz7izp20oYzpPJ27YhgfAgW2M0jSTuo4UVusUWwIMsAEF-jDasbm8TdtVAE5kXcQCge4Z7D2K3G6Gcquk2WNT9-zhZqYch198cH2Rp7kVzduIRVySXjIGm6gP1XzFtj1d82ESZ8DjsUycwsy2azOs5TfTO_W_ziFjpl4I3rPgDQy0xFDVwTjnrwt2y3jZTlbUl0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حال‌ و هوای یکی از دانش‌آموزان در جشن شروع سال تحصیلی جدید:
@News_Hut</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/news_hut/72112" target="_blank">📅 13:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72111">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb3684649a.mp4?token=eU_OFdvlc7GbDbj5wYDECjPdfC5HydsjA-Bro4FreduCu3lWajbVzY8E3m8tLwRwe9TrWjkbH8qe_TM-4VpM95Ct8YY5oqWNbFVuAWCdiVX-yBQERTahZKkY-TRUb2RgZgvFhmA_t0uzX72W236-xopBzIhiIcVOiiIHv0OPHN5oPwzgeRzEGPFF9jBCVOtQZ5T5qU_rseNe_tTLh_FW0uV2kSSn1qieXLD0JudxvJ7NMMa_ediRmWKLNaVf1HEq2MTBHTImu6Sok3htbfDtyQFGrh3RsCUuX6Xdz9PH-264XHBqbX4vepzvNXYfGQB38rKDdNiZbrKxgj86rYGCnIDEBQeNY5yasbYSZqkakRWoZpurBELgUvgPowQs_xCTrdIYPFTIuKP1TVXgcb1smZiAVtjI_paRNCST9VrI0s74P37_UI08NM666kGnnZrzLgyZKZdYZR1k058Gc9Tf8muEVOlYLNmzadfwvmN13xTzlhO5_c_Jtau0AUZGplbh6Hug_HFM6hjmAMHiG9PXJGRvuf-P-WHXWpT3n94RtmWf9DyFvzgmsN6WN62-vykNlujb7e-Jg3ndTvnNXlW2W1_tRblVHYatAdd4O08YK9hFfeKgZ4qxO5pi8OH1JkFuISmPgVbvVzpJqk7DqbzDNzMfpZp9We84hPfQHeRZyw8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb3684649a.mp4?token=eU_OFdvlc7GbDbj5wYDECjPdfC5HydsjA-Bro4FreduCu3lWajbVzY8E3m8tLwRwe9TrWjkbH8qe_TM-4VpM95Ct8YY5oqWNbFVuAWCdiVX-yBQERTahZKkY-TRUb2RgZgvFhmA_t0uzX72W236-xopBzIhiIcVOiiIHv0OPHN5oPwzgeRzEGPFF9jBCVOtQZ5T5qU_rseNe_tTLh_FW0uV2kSSn1qieXLD0JudxvJ7NMMa_ediRmWKLNaVf1HEq2MTBHTImu6Sok3htbfDtyQFGrh3RsCUuX6Xdz9PH-264XHBqbX4vepzvNXYfGQB38rKDdNiZbrKxgj86rYGCnIDEBQeNY5yasbYSZqkakRWoZpurBELgUvgPowQs_xCTrdIYPFTIuKP1TVXgcb1smZiAVtjI_paRNCST9VrI0s74P37_UI08NM666kGnnZrzLgyZKZdYZR1k058Gc9Tf8muEVOlYLNmzadfwvmN13xTzlhO5_c_Jtau0AUZGplbh6Hug_HFM6hjmAMHiG9PXJGRvuf-P-WHXWpT3n94RtmWf9DyFvzgmsN6WN62-vykNlujb7e-Jg3ndTvnNXlW2W1_tRblVHYatAdd4O08YK9hFfeKgZ4qxO5pi8OH1JkFuISmPgVbvVzpJqk7DqbzDNzMfpZp9We84hPfQHeRZyw8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دنی دانون، سفیر اسرائیل در سازمان ملل:
ما می‌دانیم رهبران ایران کجا پنهان شده‌اند. ما می‌دانیم آن‌ها چه کار می‌کنند و چه می‌گویند.
به گمانم جانشان برایشان اهمیت دارد. آن‌ها دریافته‌اند که اگر به اسرائیل حمله کنند، تنها چند روز طول می‌کشد تا سراغشان برویم.
@News_Hut</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/news_hut/72111" target="_blank">📅 12:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72110">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/402f33620e.mp4?token=iTClk7YvGGUlVsJasreJCAzsDxxuNhWnLGRcYUx688aAVMmT-AUu7BkU5VKzZAepPfJ6aNdD2_opgFA9s2mGcWqTIt9pzwtDJsh4DtkmjZE0ncYZzXgk1Lq5AXXjEM_CQPAbmauiJlBOoXLFTwNpQeY8mB4ex33JwiJzwPhJ_w_BbNi4_GkFQhvEDdJUazCkbb9zS3dujRtnUVrhNhbVt_TQNncNVvORrYClGmMCYk1gK59xNzR5iYdyyGsnnmyee_YqQZzzMSGXOmrtlie_O3Q01jjidBXnwjafjYoisH4Rks1OmoLJiW7Wm1ZhhIayU1RwrD1PP2dEZ9uzMUDlSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/402f33620e.mp4?token=iTClk7YvGGUlVsJasreJCAzsDxxuNhWnLGRcYUx688aAVMmT-AUu7BkU5VKzZAepPfJ6aNdD2_opgFA9s2mGcWqTIt9pzwtDJsh4DtkmjZE0ncYZzXgk1Lq5AXXjEM_CQPAbmauiJlBOoXLFTwNpQeY8mB4ex33JwiJzwPhJ_w_BbNi4_GkFQhvEDdJUazCkbb9zS3dujRtnUVrhNhbVt_TQNncNVvORrYClGmMCYk1gK59xNzR5iYdyyGsnnmyee_YqQZzzMSGXOmrtlie_O3Q01jjidBXnwjafjYoisH4Rks1OmoLJiW7Wm1ZhhIayU1RwrD1PP2dEZ9uzMUDlSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز یکم مهر ماه، بچه‌های میناب دیگه نیستن که برن مدرسه...
اما جاشون پیش خواهر برادرای بزرگترشون امنه
🤍
@News_Hut</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/news_hut/72110" target="_blank">📅 11:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72109">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b92a5ff67f.mp4?token=AsNjR0O5RvVyUFCg85qUE__kPsNvfMYMUNTJRr23zSbs9YD_Ab_xCfk-UtQizPNUAu32-ci61j-F18ENYoNAvmeg1m230IJKU08ZQOrdudHOqqUXAeUPMT1mqLbTHqyBe4_zMkHl98B8E3V6k7wx7wewd-ruVqXrzqzbEykAGxth8U8gFZmopxg1LGxas_idetjA5Hm7RgI82wuCmMgdfC50bK0yqiVbKjmyjHzi3VgvZ9V2A5lDNq2CNeokFc0tn3LXciomSQXSnRyllBJ1Q5TnKf7bkLMG_2V7WcRp9XW7rDO21LELuzZJLApP_huyLHBkpNr-GDFT18ZVvjXbN1iAUeK-t2VGz55es_QDG0Gv9WlXMWrPGFrjk9acLGdlIr9l_qYcRjvJdK2jtWMSI2AAwuZzIjXC9HeHtP34D1JUlk2s9mDXiw5fG_qYhFnmC3Ooh5ki5OhnoIAafGtwjAe1t_zTLjuHOG6uVEsRA_fdA7qb138USWbq3FaN-irQhdTmFjWMGPiphC9S8r026JopYyPKqDD6zzxqsMm-PW1MJjJMOlpPqu3QZFyLM1hcHf2YJenN4FTn6SYPPvyu3QTD_VO78yolHV108EcEvtSakPJ25JgVLCXjU12wgDnrNElkp78Ve-uwRWhNb-WO8TV7RfLUrYzGkZJIo3LPUpI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b92a5ff67f.mp4?token=AsNjR0O5RvVyUFCg85qUE__kPsNvfMYMUNTJRr23zSbs9YD_Ab_xCfk-UtQizPNUAu32-ci61j-F18ENYoNAvmeg1m230IJKU08ZQOrdudHOqqUXAeUPMT1mqLbTHqyBe4_zMkHl98B8E3V6k7wx7wewd-ruVqXrzqzbEykAGxth8U8gFZmopxg1LGxas_idetjA5Hm7RgI82wuCmMgdfC50bK0yqiVbKjmyjHzi3VgvZ9V2A5lDNq2CNeokFc0tn3LXciomSQXSnRyllBJ1Q5TnKf7bkLMG_2V7WcRp9XW7rDO21LELuzZJLApP_huyLHBkpNr-GDFT18ZVvjXbN1iAUeK-t2VGz55es_QDG0Gv9WlXMWrPGFrjk9acLGdlIr9l_qYcRjvJdK2jtWMSI2AAwuZzIjXC9HeHtP34D1JUlk2s9mDXiw5fG_qYhFnmC3Ooh5ki5OhnoIAafGtwjAe1t_zTLjuHOG6uVEsRA_fdA7qb138USWbq3FaN-irQhdTmFjWMGPiphC9S8r026JopYyPKqDD6zzxqsMm-PW1MJjJMOlpPqu3QZFyLM1hcHf2YJenN4FTn6SYPPvyu3QTD_VO78yolHV108EcEvtSakPJ25JgVLCXjU12wgDnrNElkp78Ve-uwRWhNb-WO8TV7RfLUrYzGkZJIo3LPUpI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات روته دبیر کل ناتو درباره ایران:
چرا برای از بین بردن توانمندی هسته‌ای ایران، حضور ایالات متحده ضروری بود؟ چرا اکنون در ماجرای حوثی‌ها در دریای سرخ، همه نگاه‌ها به ایالات متحده دوخته شده است؟
زیرا اروپایی‌ها به نوعی از توانمندی کافی برای انجام این کار به تنهایی برخوردار نبودند. آنجا حیاط خلوت اروپا محسوب می‌شود، نه حیاط خلوت ایالات متحده.
در آینده، دستاوردِ داشتنِ یک ناتوی قوی‌تر این خواهد بود که اروپایی‌ها می‌توانند خودشان به امور حیاط خلوتشان رسیدگی کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/news_hut/72109" target="_blank">📅 11:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72108">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اظهارات روته دبیر‌کل ناتو درباره ایران:
می‌توان گفت که اجرای عملیات «Epic Fury» بدون بهره‌گیری از اروپا به عنوان سکویی برای اعمال قدرت ایالات متحده، غیرممکن می‌بود.
از ۲۸ فوریه سال جاری تاکنون، ۵۰۰۰ فروند هواپیما در پشتیبانی از عملیات «Epic Fury» از پایگاه‌های اروپایی به پرواز درآمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/news_hut/72108" target="_blank">📅 11:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72107">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72107" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/news_hut/72107" target="_blank">📅 11:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72106">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMwKJtxdI5XbA3k0yXXB44o2l-8K-4y6tkIsAjaHKrI_9cZo61sOmi3H0WX8H-h9s0Wu1eAvkTQtWugNVIjrUsYt5RzzxHRAJu9J6dwFeC1tZ9MQ8NwfZOIwU00KbzQWdrtb-Gfes8hMW_z4gd32X_YZ-PYVynX1BXBt4pFuDGAEZkuwn4YRvpflrEPNYTd-mIzTcHjuHES1-nDR5vImy7OH_lBynDBzxrB7O_uFlFxOveMu7GVFiYfp4m1ji03TyTxaYnIPjqfShQMwYn8iG8dIBSooJcNWFfrr6un5N4Vhq43LTU9GG9MTW6ZJbKNJkT3RKdaA9TvREp_QBiQaHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
هیجان مسابقات DOTA 2 را زنده در
TrexBet
دنبال کنید و با پیش‌بینی دقیق نتایج برنده شوید!
🦖
پوشش کامل تمام بازی‌های محبوب Esports:
‏CS2, DOTA 2, Valorant و ده‌ها گیم جذاب دیگر...
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/news_hut/72106" target="_blank">📅 11:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72105">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شلیک چندین موشک ضد کشتی به سمت شناورها در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/news_hut/72105" target="_blank">📅 11:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72104">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4629cd7c2a.mp4?token=fm-NKwYEJYgJu-ukOa9LUg7FdvRwiyP28xAsTZKZRNOWURgNfRi-Nt--krg4UFxiHXFa_STzYQBFFsTxdrBJI9MooFyo-anZP-rcbrim5X2CvrMuoiF5ERMF6e67tlxvCO0b1R0tFgmtC7-huoy7pVXyVhvtuCCOUV-35FFUDycsOutRWr7zWCS_j7-rx-xS0WDF9UOL3nswz4rBYXzmKRCGPZINiYIPtPHg6Lk1-zSX45SQs617_8EAbo1AGcPpfXIv7j8Lugkb-fXDw6-Ol7xup3JopBddMbvt99ClujHS6205H4Lr06wqCMXGBLgEeuSiXJio4VUT4g1Lnml3MmmkVOlYw24iL6cri8H6hF_dmFnCWOFCwCSj7Kia7zDQI1ojZTawC6nmEhn7Tj5GJ55NhByILJFIqcmqrNqCL9cg_Bjb2LbIIiRIGjrphXuNn0dCS2X785SsZbxlvMCFVLJhtePU0XxZ3u91AkmysuNZmYsttvcorb_xVUUixQ8EqRmBhU4NvYpNCnTuH2LfXGPydOLle9TwKW2B84lDaaDC1OIPNQmJ71F7dPsfipGpc4EFLW195RZB8rEbBqhPn-EwqIuNQ7cP65PdN76bXwwrpYgr7Q2ExEI58YHK_LxKvdYhCZX-spTnzi696AppbcNZ-rU4Qg358k33Ca7XWNc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4629cd7c2a.mp4?token=fm-NKwYEJYgJu-ukOa9LUg7FdvRwiyP28xAsTZKZRNOWURgNfRi-Nt--krg4UFxiHXFa_STzYQBFFsTxdrBJI9MooFyo-anZP-rcbrim5X2CvrMuoiF5ERMF6e67tlxvCO0b1R0tFgmtC7-huoy7pVXyVhvtuCCOUV-35FFUDycsOutRWr7zWCS_j7-rx-xS0WDF9UOL3nswz4rBYXzmKRCGPZINiYIPtPHg6Lk1-zSX45SQs617_8EAbo1AGcPpfXIv7j8Lugkb-fXDw6-Ol7xup3JopBddMbvt99ClujHS6205H4Lr06wqCMXGBLgEeuSiXJio4VUT4g1Lnml3MmmkVOlYw24iL6cri8H6hF_dmFnCWOFCwCSj7Kia7zDQI1ojZTawC6nmEhn7Tj5GJ55NhByILJFIqcmqrNqCL9cg_Bjb2LbIIiRIGjrphXuNn0dCS2X785SsZbxlvMCFVLJhtePU0XxZ3u91AkmysuNZmYsttvcorb_xVUUixQ8EqRmBhU4NvYpNCnTuH2LfXGPydOLle9TwKW2B84lDaaDC1OIPNQmJ71F7dPsfipGpc4EFLW195RZB8rEbBqhPn-EwqIuNQ7cP65PdN76bXwwrpYgr7Q2ExEI58YHK_LxKvdYhCZX-spTnzi696AppbcNZ-rU4Qg358k33Ca7XWNc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی:
تولید ناخالص داخلی ایران در سال ۱۹۷۸ دو برابر کره جنوبی بود. امروز، تولید ناخالص داخلی کره جنوبی پنج برابر ایران است.
وضعیت اقتصاد ایران قابل تداوم نیست؛ پایدار نیست و در آستانه انفجار قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/news_hut/72104" target="_blank">📅 11:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72103">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/582ee3d494.mp4?token=pLcacgW7Eb7vi9eCX05qoTtGIzBa5Ys4PgTlAroZ1NUrpQnyWpk8hmzzYdBUI7ibeFasRvpnPTk_tynuCC7JAM7GR4tVog6hR_Gf9ASkWWDEddfaJgiaMWSdvtuwgSUZ3co7NhG45A4MdaRgr49WaDiTOP-DQ5SuyPVx9Al6WrOM33hJYYKJbuqdEaAjvF1n4hHe9otrr6v7kpgAQRONFAPYbU26YfePeDHoL2sb2XthKVZp_BNFAmvyVEbgbXsZl9BatFXX2lXon9_V49PSaW4BjoVcX57crDeTyWGfWvtgMsde8_TUdlAMlzo1iCw6njHHLxPM4hhkEuO6hUiJ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/582ee3d494.mp4?token=pLcacgW7Eb7vi9eCX05qoTtGIzBa5Ys4PgTlAroZ1NUrpQnyWpk8hmzzYdBUI7ibeFasRvpnPTk_tynuCC7JAM7GR4tVog6hR_Gf9ASkWWDEddfaJgiaMWSdvtuwgSUZ3co7NhG45A4MdaRgr49WaDiTOP-DQ5SuyPVx9Al6WrOM33hJYYKJbuqdEaAjvF1n4hHe9otrr6v7kpgAQRONFAPYbU26YfePeDHoL2sb2XthKVZp_BNFAmvyVEbgbXsZl9BatFXX2lXon9_V49PSaW4BjoVcX57crDeTyWGfWvtgMsde8_TUdlAMlzo1iCw6njHHLxPM4hhkEuO6hUiJ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناوگان هواپیماهای باری نظامی، از جمله هواپیماهای «آنتونوف ۱۲۴» در حال فعالیت از فرودگاه لایپزیگ/هاله در آلمان مشاهده شده‌اند.
فرودگاه لایپزیگ/هاله یکی از مراکز مهم لجستیکی ناتو است که برای انتقال تجهیزات نظامی و محموله‌های فوق‌سنگین مورد استفاده قرار می‌گیرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/72103" target="_blank">📅 11:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72102">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6c2bb73b79.mp4?token=VtSyj_658B3fEXxX3fVKHrPt4xJn-kEdbAUvIA5Y9aUDgu-IafHN7d9bh1Djjfrmt9zZjtR3hIv_xlVuOqNT_aVccBS_7eZqYPt_WpNsxTrOKKgTPPOeiagTJ6HNNSbaTMi-Q5e_1NHfjvv982gIr-nntC-m0fIzSxR_q978CjseJoNaCHGloRCj968h7lxLmkqqdJkMEkLkS2uLcZMGUkS2vXtrO0c_djup1EKByk6xIiTNN543l_drINcC8idy0Wzmx__SxK4WoUI_k_DDJXKVkkGWAWzSsPY86rMqjxISafzV04q2tlY0qhp2DFy2tKmk6sA6xpJOdtvoYBnnvA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6c2bb73b79.mp4?token=VtSyj_658B3fEXxX3fVKHrPt4xJn-kEdbAUvIA5Y9aUDgu-IafHN7d9bh1Djjfrmt9zZjtR3hIv_xlVuOqNT_aVccBS_7eZqYPt_WpNsxTrOKKgTPPOeiagTJ6HNNSbaTMi-Q5e_1NHfjvv982gIr-nntC-m0fIzSxR_q978CjseJoNaCHGloRCj968h7lxLmkqqdJkMEkLkS2uLcZMGUkS2vXtrO0c_djup1EKByk6xIiTNN543l_drINcC8idy0Wzmx__SxK4WoUI_k_DDJXKVkkGWAWzSsPY86rMqjxISafzV04q2tlY0qhp2DFy2tKmk6sA6xpJOdtvoYBnnvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کم‌ کم ربات‌های جای انسان‌ها رو دارن میگیرن....
برای اولین بار تو تاریخ، یه مبارزه رسمی بین انسان و ربات برگزار شد؛ که در آخرش ربات با یه لگد سنگین حریفشو انداخت رو زمین و ناک اوتش کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/72102" target="_blank">📅 10:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72101">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2331092d7.mp4?token=mJJa8bIP63VZ6R3j9wdt1z6vnNwJxHDz6dLY2rUDU9kbJe2bs6p3vs_9dl_2Cf-J4BDO8GRxaFdUGWhnei4M36t581hLQXGf2TPXX22D1U9Q12kthhMXT71j0rYCGe4sIUblmmL8Y8dU4aYbzl8mRrD5jcN1TVl1YlS6LRbWDq6wQnVTJ8epYEEkGqX-I_lhHIQdLJmtqPw1YpSp6l0-YX8YD3qCwf7sO9UGcsoES1dz2DHGtqmyCYo2jH7C3LbR7Qps8O3H_7-mJhsIBvAHJReaEZYsHJqQBe9BWPcwRqTHBWKdW4RvN2lGu2BbcZOEYFwayaapo2HTwc4zGkF8AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2331092d7.mp4?token=mJJa8bIP63VZ6R3j9wdt1z6vnNwJxHDz6dLY2rUDU9kbJe2bs6p3vs_9dl_2Cf-J4BDO8GRxaFdUGWhnei4M36t581hLQXGf2TPXX22D1U9Q12kthhMXT71j0rYCGe4sIUblmmL8Y8dU4aYbzl8mRrD5jcN1TVl1YlS6LRbWDq6wQnVTJ8epYEEkGqX-I_lhHIQdLJmtqPw1YpSp6l0-YX8YD3qCwf7sO9UGcsoES1dz2DHGtqmyCYo2jH7C3LbR7Qps8O3H_7-mJhsIBvAHJReaEZYsHJqQBe9BWPcwRqTHBWKdW4RvN2lGu2BbcZOEYFwayaapo2HTwc4zGkF8AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لمس ممه‌های دوس دخترتون واقعا زندگی شمارو نجات میده! این یه شوخی جنسی نیست، از لحاظ علمی این موضوع کاملا ثابت شده و اینکار مثل معجزه عمل می‌کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/72101" target="_blank">📅 09:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72100">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/575ce7dd12.mp4?token=k-afO3qZjkqITv35LmZhXMCRvWGsCd7mS1vtr9nvac2RlAiEIqrTInhrBH-UxKZl-FBSSA7DA1DK8eQIdnPDK8nye0ToKjT4tnDWjYua8tkev7VXm3SO6jWKKUHNd2eM1FQPKjud7KiGiR9n9nLAVILeIZg6PdcxJqSiObLW7hA9O592sIaCPTnj8sqdfhHVrA97UL6Vdcyhyo0XjrKkis80iniSteD5yryRvPhPAa5ZUs181SMP6R17IUsquwveEfGlmCLsgsU4ya8KwlH2tKnuRT1jEvxfuUhV9KQhYpYNM0xm16tmyiaA1DVTi713Jy88kDWv354UjCzppRvWsg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/575ce7dd12.mp4?token=k-afO3qZjkqITv35LmZhXMCRvWGsCd7mS1vtr9nvac2RlAiEIqrTInhrBH-UxKZl-FBSSA7DA1DK8eQIdnPDK8nye0ToKjT4tnDWjYua8tkev7VXm3SO6jWKKUHNd2eM1FQPKjud7KiGiR9n9nLAVILeIZg6PdcxJqSiObLW7hA9O592sIaCPTnj8sqdfhHVrA97UL6Vdcyhyo0XjrKkis80iniSteD5yryRvPhPAa5ZUs181SMP6R17IUsquwveEfGlmCLsgsU4ya8KwlH2tKnuRT1jEvxfuUhV9KQhYpYNM0xm16tmyiaA1DVTi713Jy88kDWv354UjCzppRvWsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی مشهد یه خانم حامی حکومت تو اتوبوس، به یه دختر بخاطر حجاب حمله‌ور شد!
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/72100" target="_blank">📅 09:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72099">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad662c895d.mp4?token=WlCmUl4pjBnlJX2Tp4TotCghqP1FRb-dPvxCyS_7xle1v58OX4_Vc6nbdBckFeqFUTQFaoqzhVTu-41TU-8a283NPLYDGsfBztDIie4xYzk8Oc6V2v4a5m_6rlC35EWq1dZgWn8xAU68k2g0LU2jwWDNomkCQbEEIHyqFUZ3-2tlIz2gOwhqozbyryehqBCIm20vWeaOZeXStZTgVDkPx4hS_vJV22H7W02F47AZfb5hwYdkV0Ws2JlCAN8jwVQla0NbDJA7-mzMnvwxtrDcSzeiXX9YYX0-KE31NKfhugxhKz_mjddy_yHT96s6PDc7G5iO9G-EvqIu9fL97nHvYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad662c895d.mp4?token=WlCmUl4pjBnlJX2Tp4TotCghqP1FRb-dPvxCyS_7xle1v58OX4_Vc6nbdBckFeqFUTQFaoqzhVTu-41TU-8a283NPLYDGsfBztDIie4xYzk8Oc6V2v4a5m_6rlC35EWq1dZgWn8xAU68k2g0LU2jwWDNomkCQbEEIHyqFUZ3-2tlIz2gOwhqozbyryehqBCIm20vWeaOZeXStZTgVDkPx4hS_vJV22H7W02F47AZfb5hwYdkV0Ws2JlCAN8jwVQla0NbDJA7-mzMnvwxtrDcSzeiXX9YYX0-KE31NKfhugxhKz_mjddy_yHT96s6PDc7G5iO9G-EvqIu9fL97nHvYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی در استودیو فاکس‌نیوز با مارتا مک‌کالوم:
«وقتی من میلیون‌ها ایرانی را در ۳۱ استان کشور به آمدن به خیابان‌ها فراخواندم، آن‌ها به صورت میلیونی حاضر شدند و ضمن اعلام حمایت، شعار پایان دادن به این رژیم را سر دادند.
آن‌ها از تمامی اقشار جامعه ایران، اقوام، ادیان و گروه‌های اجتماعی گوناگون بودند؛
این جلوه‌ای عالی از اتحاد و تنوع است.
بنابراین، هر کس که ادعا می‌کند پس از ما ایران دچار جنگ داخلی خواهد شد [باید بداند که] عامل اصلی این تفرقه و اختلاف، همین رژیم است.
همه ایرانیان می‌دانند که این رژیم بذر دشمنی و خصومت را کاشته است.
اما ایرانیان دریافته‌اند که پس از دستیابی به آزادی، قادرند دوباره برخیزند؛ درست همان‌طور که قرن‌ها فارغ از تفاوت‌های قومی یا مذهبی، در صلح و آرامش در کنار یکدیگر زندگی کرده‌اند.
و انقلاب «شیر و خورشید» در راه است.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/72099" target="_blank">📅 07:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72098">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/686ffe220e.mp4?token=BofmLe1kvbMc_bvBoMrA8X7eZ_o_Umk53KoHj_U16QjNPX-dx52NI0Jq5YfO_oBwvR1Uqg3w9NwUQYzUYg7-7V4b4EyHzbz_sTz2UCZk3Nsl-bQLI99aqY5O2AUBpRAPzKYSqp5XVe6S6sdZC6NBUBUyjMOHLRIr-NSN04WFXTs_KyX4DeWgv95dLKbeNl9L8L-3dg-4CB_WQ_P6dfhnK_Da7r2wI2tC-5Ba5jdOWKTXMbJPYi72a9g9wOFqqAA4sWfgbleL5Navjtygc1lVKXdhuU11I9jKosZXeMCQBhhDPoGJpElZe7VwlqBAjvuAcIJQHPO1SPdpdUUq-t_Ukw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/686ffe220e.mp4?token=BofmLe1kvbMc_bvBoMrA8X7eZ_o_Umk53KoHj_U16QjNPX-dx52NI0Jq5YfO_oBwvR1Uqg3w9NwUQYzUYg7-7V4b4EyHzbz_sTz2UCZk3Nsl-bQLI99aqY5O2AUBpRAPzKYSqp5XVe6S6sdZC6NBUBUyjMOHLRIr-NSN04WFXTs_KyX4DeWgv95dLKbeNl9L8L-3dg-4CB_WQ_P6dfhnK_Da7r2wI2tC-5Ba5jdOWKTXMbJPYi72a9g9wOFqqAA4sWfgbleL5Navjtygc1lVKXdhuU11I9jKosZXeMCQBhhDPoGJpElZe7VwlqBAjvuAcIJQHPO1SPdpdUUq-t_Ukw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی در اجلاس سالانه «کنکوردیا» (Concordia)، پرسشی را مطرح کرد که دهه‌هاست در سیاست بین‌الملل نادیده گرفته شده است: چرا مردم ایران در کانون گفتگوها قرار ندارند؟
جمهوری اسلامی با مذاکرات بی‌پایان یا سیاست مماشات تغییر نخواهد کرد. ایرانیانی که به دست این رژیم قتل‌عام شدند، خواهان آزادی بودند، نه توافق هسته‌ای یا کنترل تنگه هرمز.
انتخاب روشن است: یا همچنان بر روی رژیمی سرمایه‌گذاری کنیم که عامل بی‌ثباتی و تروریسم است، و یا در کنار مردم ایران بایستیم؛ کسانی که شرکای طبیعی جهان آزاد برای ساختن آینده‌ای سرشار از صلح، امنیت و فرصت‌های اقتصادی بی‌سابقه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/72098" target="_blank">📅 07:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72097">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrOY9lWAR46FQimYdFuFuN6sPH9hJSMuNdI8haVYDzgAfwHxhG3K9SukDpLf389mEZ8gJKO96_AxLXPKl4v-ehlNqbSu26qDxB0y4yq9dcNP_VdgTrX57juUL2RR5h002BuLYfCl4AUYXvWJmXgyLKcqV5Fwl0iMSN2bi_lAkB1v9C6AGvH5h-Y5_QqTRg7fiaKLsQ49RpAUZL-bUR-E6mIU6oE1BSmX9VUAz7UB-cpqk1GVPi83uL2QDZVOLUZPNCXDNFWoGn7YLOqB0kSz_xWfnT4H0sMYYJqeH5tZa-BBl1PkvmrL89uTH8TtYNTLKg8Dvnct40TNopw_GmUEMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛یک منبع آمریکایی به العربیه:
آمریکا درخواست ایران برای رفع محاصره را نپذیرفت.
فرصت‌های دست‌یابی به توافق محدود است.
اختلافات و موانع بزرگی همچنان میان دو طرف وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72097" target="_blank">📅 07:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72096">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjYjFGnGC49Hw0a8CusGDqcAoPT8AJo1Ey3th4Ej7T0pBLGXygL0nN0u5dDjF7_FABud29XvCMbx-ya0TIzGaSemdImQ_dalvVqp-pzK63_XVWbbaad3WwaMfsLStYSpffcAxK7ovkP2pDjYmtggYt35ku0tnkel7jM8rhX0ThqhsyjUTmbVzG0g0_nEFvdRNMdL2VxBBt5PGYiONDdYSSDjcouqnh98qEid-5beqfs9gglQRQF4pIWg0L7_S71-_KEaRaBR5ycRqn-l4Ylgk-DGB2RpMiUx11rQrj3DPCHGHwmbX_6cK9-YmkaayAjyAgoymC7xBqwNANkmHnfalQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استیو ویتکاف:
امروز در حاشیه مجمع عمومی سازمان ملل، از طریق میانجی‌هایی که در طول روز میان دو طرف در رفت‌وآمد بودند، گفتگوهای مفصلی با هیئت ایرانی انجام دادیم.
آن‌ها یک دور از مذاکرات را با موفقیت به پایان رساندند؛ مذاکراتی که امیدواریم سازنده و نویدبخش باشد. میانجی‌ها به کار خود ادامه خواهند داد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72096" target="_blank">📅 06:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72095">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83dc83eba1.mp4?token=Tn8AsIflYbJyNin_DihPWP1CoGyxpynEVIKT46etUaQirs9yWc1fDarZjtCF_-4gU4sgJx9RbvQSFxJvr9Q4pOWQZiolg9rf4ReVPvaDLhJoMducmWKVJ0Ps0D05MeIDq_Yedrat-plAOWTs_XwOwAXlQc0zRMpNoWkEAelmd8WL9VyPWXzGjWVphxSqrQ4EYeaeYOQ9s65WnCFkjQJWDM-r36386M8bqd1SYvIkQkWWsX1BvrgwFWuDfUEg73WHkgChYMXwKxQRYf4tk2zYtiaMkLke4lSbIg9hRQ1DEg0xl64mTMvAeb9fgo5KQo3DV63o7Rwx5ZWUc9gy2g98SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83dc83eba1.mp4?token=Tn8AsIflYbJyNin_DihPWP1CoGyxpynEVIKT46etUaQirs9yWc1fDarZjtCF_-4gU4sgJx9RbvQSFxJvr9Q4pOWQZiolg9rf4ReVPvaDLhJoMducmWKVJ0Ps0D05MeIDq_Yedrat-plAOWTs_XwOwAXlQc0zRMpNoWkEAelmd8WL9VyPWXzGjWVphxSqrQ4EYeaeYOQ9s65WnCFkjQJWDM-r36386M8bqd1SYvIkQkWWsX1BvrgwFWuDfUEg73WHkgChYMXwKxQRYf4tk2zYtiaMkLke4lSbIg9hRQ1DEg0xl64mTMvAeb9fgo5KQo3DV63o7Rwx5ZWUc9gy2g98SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود هم رسید نیویورک
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72095" target="_blank">📅 06:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72094">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+hgTgtcXHw1k4ODA8</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72094" target="_blank">📅 01:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72093">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+hgTgtcXHw1k4ODA8</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72093" target="_blank">📅 01:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72092">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">صدای دوانفجار جدید در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72092" target="_blank">📅 01:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72091">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2-m1rfZwPXJfDZ5jBwP1N76mCWCdXfy2KLov8CNYLplyEydn7uzQ9RCbgMmDI4hyPGTjDI7eZeFR6gzOuZ2OJcvYhARFVn1Q-Oc4Nav_dTta3hndyjqNAmF9f_k-LfAwLxEeutA20QO8vrsb0F7e7DKrJBK_rBRDiMjciRoM9PcD2T8evpBHrX06oybCQJowfTtqv0fs6l848DFpNA7_VKaBAcP5cM4Kkft2wWfK1Aj8TDatC4FLBRpOq8ZeUoIY5QZvwiXqedpG8aMZSKz1wo5IgsVAUuF324_RRWG6MpGkIZ1Y0cNVn7sVwReHpkf5LD1hH-L-uwp_uVmnF6Hew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای‌نت:
انتظار می‌رود سخنرانی نتانیاهو در سازمان ملل به شدت بر ایران متمرکز باشد و به گفته‌ی ایدز، این سخنرانی حاوی «غافلگیری‌های» نامشخصی خواهد بود.
هیئت نمایندگی اسرائیل همچنین خود را برای احتمال مزاحمت یا خروج هماهنگ‌شده در طول سخنرانی آماده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72091" target="_blank">📅 01:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72090">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ایرنا: صدای انفجار در حوالی جزیره قشم به گوش رسید
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72090" target="_blank">📅 01:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72089">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3046a77aed.mp4?token=OM3wLehK32NL9cH7mxvTc3OfPMZsKUvdqy8vt_5GTVddor0cwzfcavEtKZIRzVrcIQGyKb_YPOZF64kcK_k6RUJsZUOPJK4GefFd24iUeIrkU9fKmONoVPscbyfHPUX6CTI8S4AtzkOw250CJYM5PJC_CdQChZx7tcWNKZbCmvEKphCo1ZoJTM3KD62MudV1hpU2UwUK29qc2vOcgy9ezqrgu6XsIdIgxQkDnDhBLUT5SgnfIX57hVyzqb8OYU9dYPkSkBDbaAc4G7QUQ_rNn87x408gV6aPlsBcuVOwu4jjR1j1alC09qDANuvvAhYWxgxGER3FfdnHEPhunw5Llw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3046a77aed.mp4?token=OM3wLehK32NL9cH7mxvTc3OfPMZsKUvdqy8vt_5GTVddor0cwzfcavEtKZIRzVrcIQGyKb_YPOZF64kcK_k6RUJsZUOPJK4GefFd24iUeIrkU9fKmONoVPscbyfHPUX6CTI8S4AtzkOw250CJYM5PJC_CdQChZx7tcWNKZbCmvEKphCo1ZoJTM3KD62MudV1hpU2UwUK29qc2vOcgy9ezqrgu6XsIdIgxQkDnDhBLUT5SgnfIX57hVyzqb8OYU9dYPkSkBDbaAc4G7QUQ_rNn87x408gV6aPlsBcuVOwu4jjR1j1alC09qDANuvvAhYWxgxGER3FfdnHEPhunw5Llw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت
ترامپ:
یا به توافق می‌رسیم، یا کار خیلی خیلی سریع تمام خواهد شد.
آن‌قدر سریع تمام می‌شود که سرتان گیج می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72089" target="_blank">📅 01:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72088">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fAXLkpXxXHHtUOo-wyL88_Q2FEJ7DMHZTDsNgaibsXufjIsHrBtmND865ui3xaT0Xccg2DxoWXLv2SP-sdvGPr8d5p3QX_OnzaiBPQ9quep5J-VmAeU4G-2RN3IRca_lBB3zafZikXsThhbvtJzSifU9900AgPjJ0-zD6PfRhdw9OqFWvSWoJSzqSwdI08rl3PlAaKWmg38F2XMHX4dvZRgTrB1Lzb992AGcYfdNacP0AXGrZH3g8BDOIPj4FCC7VZlzrro7UiR444c08aESssJj-XLcywDKKl4h6XIlx2MI5LsSxbXNKYZH0INPnCeTfeRFDbwkIPhDkZZ_6vs3xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظاری که تندروهای جمهوری اسلامی از پزشکیان تو نشست سازمان ملل دارن:
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72088" target="_blank">📅 01:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72087">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تابستون هم تموم شد و رسما وارد پاییز شدیم...
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72087" target="_blank">📅 00:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72086">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ساعت ۰۰:۴۷ بامداد چهارشنبه؛ یک انفجار در محدوده تنگه هرمز رُخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72086" target="_blank">📅 00:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72085">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a836832d.mp4?token=qG1z0C4DLELw528v3rviRdvWpmPopzjMqKjeRZFdmjuwKtRUldrM4pUoHZKWvI1d-lhUpCCMckwI_4liw0BRCaWOyvZw0xKATvUWUAF1mkLM_mKXe22XvDAa4ZI79AV_8uSe-tTqSysIYtU-0RzrB3Gv2bK3J4VQg6iWxAkvQYCkcdmUtuHPsUvnKTiqvL2uPAFpE8BLhrzLsSCXTImoNba61gIvA_-HMzkX7EWJ3nGXoNR1w09jHJVPx4YqYe_QW5XnIq40UduySFom86V7O5vAjBRuUBf1YwsZZC5PD4puZN-mYg41cKOI2nIn9vechLTQ5S0j9ZzKOUf0iSu-cjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a836832d.mp4?token=qG1z0C4DLELw528v3rviRdvWpmPopzjMqKjeRZFdmjuwKtRUldrM4pUoHZKWvI1d-lhUpCCMckwI_4liw0BRCaWOyvZw0xKATvUWUAF1mkLM_mKXe22XvDAa4ZI79AV_8uSe-tTqSysIYtU-0RzrB3Gv2bK3J4VQg6iWxAkvQYCkcdmUtuHPsUvnKTiqvL2uPAFpE8BLhrzLsSCXTImoNba61gIvA_-HMzkX7EWJ3nGXoNR1w09jHJVPx4YqYe_QW5XnIq40UduySFom86V7O5vAjBRuUBf1YwsZZC5PD4puZN-mYg41cKOI2nIn9vechLTQ5S0j9ZzKOUf0iSu-cjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
استیو و جرد امروز جلسه بسیار پرباری با میانجی‌های ایران داشتند. باید دید در ادامه چه پیش می‌آید.
به گمانم انگیزه و شتاب زیادی برای دستیابی آن‌ها به توافق وجود دارد؛ این همان چیزی است که از همه می‌شنویم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72085" target="_blank">📅 00:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72084">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e28a4d4c0.mp4?token=uBPkQABiYy8MOXqTUhYmaymdJDAa6tTXiDVR22pzcnmhcpgu2gDLvGmoy3_ne3IPomA9uFycSMqMftdkatb-Dkp8tyd0ZokivYaZ_1B7ShmLwKdoU_nXUD5C6yw-8LiWmbWstcfE4TEO0vJW-DMnOz9agFyeRer9k1MSLtVQn-mq2BFaAWTHM33hKpawzkFWQXqmDcOZiAJ73-W9uYWA4axXeUNKCCg5jD3F2jTmykQuK9HTD8_dBQNcOO8UPQFrhiQOX3EtU8SgJ3Zg46Nmzvf7zTzLC9tuz7uVD3QyXqFCiv1c5GhVEcwSdf7WUPE1RRuNeSOHKjTbD7jiujvfwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e28a4d4c0.mp4?token=uBPkQABiYy8MOXqTUhYmaymdJDAa6tTXiDVR22pzcnmhcpgu2gDLvGmoy3_ne3IPomA9uFycSMqMftdkatb-Dkp8tyd0ZokivYaZ_1B7ShmLwKdoU_nXUD5C6yw-8LiWmbWstcfE4TEO0vJW-DMnOz9agFyeRer9k1MSLtVQn-mq2BFaAWTHM33hKpawzkFWQXqmDcOZiAJ73-W9uYWA4axXeUNKCCg5jD3F2jTmykQuK9HTD8_dBQNcOO8UPQFrhiQOX3EtU8SgJ3Zg46Nmzvf7zTzLC9tuz7uVD3QyXqFCiv1c5GhVEcwSdf7WUPE1RRuNeSOHKjTbD7jiujvfwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
امیدوارم پیش از آنکه خیلی دیر شود، هرچه سریع‌تر کار درست را انجام دهند.
می‌دانید، زمانی فرا خواهد رسید که دیگر خیلی دیر شده باشد و ما دیگر فرصتی برای اینکه اجازه دهیم آن‌ها به عنوان یک ملت باقی بمانند، نخواهیم داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72084" target="_blank">📅 00:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72083">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تسنیم:
دیدار استیو ویتکوف، نماینده آمریکا، با عباس عراقچی، وزیر امور خارجه ایران، در حاشیه مجمع عمومی سازمان ملل متحد، پس از درخواست‌های مکرر طرف آمریکایی برگزار شد.
ایران اعلام کرد که از این جلسه برای بیان شرایط خود برای بازگشایی تنگه هرمز، از جمله لغو فوری محاصره دریایی، آزادسازی دارایی‌های مسدود شده ایران و پایان جنگ در همه جبهه‌ها، استفاده کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72083" target="_blank">📅 00:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72082">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a836832d.mp4?token=qv38W8J6N36sBSWLRO224qrgDJtykUzQnAm_KuGsR5VvQxLII41IRbHwxoVuqOfm1FlK1Cwvw2rPPEq6rNIE-hsPycR-Tk9IbagVs-qBchkCjJx1KGTmKq0VJ8OxoRcKStowc6wkfX18IRIrypHIU-6F8-HBmjIFqDY8PTunV6dOOLVTDbDmNt_f9ko4YFJJBAjA2T0fKiHYGDW_u929jSIly0t9sWHeZ4A5VMXo4IhKvOrIN6JgA0YvMTBYNZyJ11sQhYdSfyCpnCOFr4em9hlVanLQCeu_hip6l1uAkx6I23pNHibJU4CGk0shjyHua5STbSxmsDyMRN_9EpY2YTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a836832d.mp4?token=qv38W8J6N36sBSWLRO224qrgDJtykUzQnAm_KuGsR5VvQxLII41IRbHwxoVuqOfm1FlK1Cwvw2rPPEq6rNIE-hsPycR-Tk9IbagVs-qBchkCjJx1KGTmKq0VJ8OxoRcKStowc6wkfX18IRIrypHIU-6F8-HBmjIFqDY8PTunV6dOOLVTDbDmNt_f9ko4YFJJBAjA2T0fKiHYGDW_u929jSIly0t9sWHeZ4A5VMXo4IhKvOrIN6JgA0YvMTBYNZyJ11sQhYdSfyCpnCOFr4em9hlVanLQCeu_hip6l1uAkx6I23pNHibJU4CGk0shjyHua5STbSxmsDyMRN_9EpY2YTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
امروز یک نشست فوق‌العاده و مثبت بین کوشنر و ویتکاف با نمایندگان ایرانی داشتیم
واقعا در مسیر خوبی حرکت می‌کنیم اونا خیلی میخان توافق کنن اینو همه میگن
شتاب قابل توجهی برای مذاکره داشتیم
اقتصاد ایران رو منزوی کردیم اقتصاد اونارو نابود کردیم این خیلی خوبه
تنگه هرمز رو از مین ها پاکسازی کردیم و نفت جریان داره همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72082" target="_blank">📅 00:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72081">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4086006d.mp4?token=Oj_P81WtOVAVy8BXdyhV4ZgQaSa-M1gt74O2suNebcfvo0JNTFUL23TXJ5vDstDiRHSHx-b0EhEmM3gXpk_J7RgHHg6wRk9mFVkmeddQLSmec-yKiLWUslAl-6EWil4U3AOAEhOvf31Qo9o0WWzdog4be5PwUcGus-Acq0fgCCiTYOgbHwrt-8mvrgk_AzSP-haVCjpTtu9TGvv0iZzGRUePY0FDzX7Aj0IALsoXW0DHlw2og92_6lntMvDSf5z49-4Zho0RVSIj7XmKuAy9isjue3reUedklL_CDn7gS67-FF1g_y4tMPnBr94XCGxcoGmxXJO-ZfrO2v7Sb4_QlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4086006d.mp4?token=Oj_P81WtOVAVy8BXdyhV4ZgQaSa-M1gt74O2suNebcfvo0JNTFUL23TXJ5vDstDiRHSHx-b0EhEmM3gXpk_J7RgHHg6wRk9mFVkmeddQLSmec-yKiLWUslAl-6EWil4U3AOAEhOvf31Qo9o0WWzdog4be5PwUcGus-Acq0fgCCiTYOgbHwrt-8mvrgk_AzSP-haVCjpTtu9TGvv0iZzGRUePY0FDzX7Aj0IALsoXW0DHlw2og92_6lntMvDSf5z49-4Zho0RVSIj7XmKuAy9isjue3reUedklL_CDn7gS67-FF1g_y4tMPnBr94XCGxcoGmxXJO-ZfrO2v7Sb4_QlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صداوسیما:
آمریکا داره آب خلیج فارس رو می‌ریزه تو امارات تا تنگه هرمز خشک بشه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72081" target="_blank">📅 23:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72080">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=jSSjzDBksvlELh3HSvXS3HheSY18Dl3FGGndeVImFY-8FN0KVxovTjrq73iHzejgVt0jR-m6rht9wQE8LQetdtW2PPRb1fpUe7SU7F8LFIcxGmDwl9q0jVsbq0NA7eEKsEt0gmRuaDNR-rA7LZcGsokio8jMLblxkzEQG3Rj4zhDR5SJ3_IWHi6xIOnUbBspQ2FeoxAA70UOTC9neIqT25YqRHJs6J1OnQ5t88S3y-YcsU3QKz3dflQL13ZMq92Wsl5P6C7RUQ9Q6xpXCpXmqkvkoWmK3RZzzydb4Fy7MDs4N2OREqcrD4Ipn2pF7xSNfPfbcYVrHkFy71UofMIPtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=jSSjzDBksvlELh3HSvXS3HheSY18Dl3FGGndeVImFY-8FN0KVxovTjrq73iHzejgVt0jR-m6rht9wQE8LQetdtW2PPRb1fpUe7SU7F8LFIcxGmDwl9q0jVsbq0NA7eEKsEt0gmRuaDNR-rA7LZcGsokio8jMLblxkzEQG3Rj4zhDR5SJ3_IWHi6xIOnUbBspQ2FeoxAA70UOTC9neIqT25YqRHJs6J1OnQ5t88S3y-YcsU3QKz3dflQL13ZMq92Wsl5P6C7RUQ9Q6xpXCpXmqkvkoWmK3RZzzydb4Fy7MDs4N2OREqcrD4Ipn2pF7xSNfPfbcYVrHkFy71UofMIPtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی آلمان یه دختر تریان (انسان‌های که فکر می‌کنن حیوانن) به یه خانم حمله می‌کنه و گازش می‌گیره، به پلیس اطلاع داده شد، هر چقدر از دختر اسم و فامیل پرسیدن فقط پارس کرد، پلیس هم اون رو برد مرکز نگهداری از حیوانات
😐
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72080" target="_blank">📅 23:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72079">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/956bc67dd9.mp4?token=Q-im6TuXoInUoYoBcfQIkM7mKOWGbduV-kr1YqDfDLj8ZVunuDLTcEAf9OWCOOYwyd3Ybz2ALhX5c6TlmhAu-P9QVrQwNjpkJ13ZbTWCyk-dUjNTRW7ICmPAw5UhyaXI_vmojDYHzQBUNvb3-ktGmpLmyL_8jY62tzH7yDHpbAN6C0tP1zBRr_9fAM77x8IXK3EsOg1ZO3Dn5sqn9HaGpgcp6mekUuta0Z0E7AEstrGojYkZ3U3Hd4uImFen-e3ssur0cbv-PxjGm8qIsC0u9t38pFLP89p5Fyr6rTgv4D8gihmwupSLE9pwaJqnBRat1sHAfLV76RDl6OitShSU4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/956bc67dd9.mp4?token=Q-im6TuXoInUoYoBcfQIkM7mKOWGbduV-kr1YqDfDLj8ZVunuDLTcEAf9OWCOOYwyd3Ybz2ALhX5c6TlmhAu-P9QVrQwNjpkJ13ZbTWCyk-dUjNTRW7ICmPAw5UhyaXI_vmojDYHzQBUNvb3-ktGmpLmyL_8jY62tzH7yDHpbAN6C0tP1zBRr_9fAM77x8IXK3EsOg1ZO3Dn5sqn9HaGpgcp6mekUuta0Z0E7AEstrGojYkZ3U3Hd4uImFen-e3ssur0cbv-PxjGm8qIsC0u9t38pFLP89p5Fyr6rTgv4D8gihmwupSLE9pwaJqnBRat1sHAfLV76RDl6OitShSU4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی فروتن، عمو فیتیله‌ای:
این روزا وقتی دختر، پسرا میخوان باهم دوست بشن، خیلی برای همدیگه لاف میزنن!
معیار انتخابم که شده پول، قیافه، خوش گذرونی و... به نظرتون گند نزدیم به عشق و عاشقی؟
یه زمانی آدما دنبال کسی بودن که نه تنها حرفشون، بلکه سکوتشون هم بفهمه. به خودت احترام بذار و با هرکسی وارد رابطه نشو.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72079" target="_blank">📅 22:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72078">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">امیر قطر در مورد غزه:  اسرائیل به نوبه خود باید به تعهدات خود به طور کامل عمل کند: توقف قطعی عملیات، خروج از نوار غزه، لغو محاصره و ارسال بی‌قید و شرط کمک‌های بشردوستانه.  @News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72078" target="_blank">📅 21:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72077">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88614b72e8.mp4?token=hjyfN_ljkiXT4SSgpohj5Yzj46IDaRuJLHy0IEzrrqJZz8XuAQdixdUi2DMsrYJAUN1H7FM5lLb0lXyXcbbvKyA7zU_Rv5i3W4W73wzM-yuFclsaOYJx3a9jCW2n05QSdMVoXM4ODhVUZblgGEvnKRxOnDQDVZ_ErHSahSn_o8bxpmuxkKhG6e8BqvuzRloYtOB2b3z8VwXPZ5QgOzZh7l1izFN4EIDPpR6fRo8IoO7lZIahBol2o-SG55tECW8cIWMw7AhU9lVi4Nwe0cy_JQCoPjOIzA_RXO5RIZn7ZxXwtqcUVUpwcjIQI4MHUUfws_pY21EVjK2i44JnF0fxOoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88614b72e8.mp4?token=hjyfN_ljkiXT4SSgpohj5Yzj46IDaRuJLHy0IEzrrqJZz8XuAQdixdUi2DMsrYJAUN1H7FM5lLb0lXyXcbbvKyA7zU_Rv5i3W4W73wzM-yuFclsaOYJx3a9jCW2n05QSdMVoXM4ODhVUZblgGEvnKRxOnDQDVZ_ErHSahSn_o8bxpmuxkKhG6e8BqvuzRloYtOB2b3z8VwXPZ5QgOzZh7l1izFN4EIDPpR6fRo8IoO7lZIahBol2o-SG55tECW8cIWMw7AhU9lVi4Nwe0cy_JQCoPjOIzA_RXO5RIZn7ZxXwtqcUVUpwcjIQI4MHUUfws_pY21EVjK2i44JnF0fxOoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر قطر در مورد غزه:
اسرائیل به نوبه خود باید به تعهدات خود به طور کامل عمل کند:
توقف قطعی عملیات، خروج از نوار غزه، لغو محاصره و ارسال بی‌قید و شرط کمک‌های بشردوستانه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72077" target="_blank">📅 21:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72076">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9803dc4ebc.mp4?token=JeUZIrpaK8vJ-zINo0gaoob2r3NQDEcHjv5-xvGEwlrioMeYlpjj4-5tPMU7QkHaNJmcACg-7-Px7tF5ml23H9GtIRat9Tvih_rP7Vy9Kt3ajqPQpNlb6ku4dUdvosohTVmdmjt8nNfNFpFnKTcHt5ISSb8lWVDzzTiW9ktBwr-rPoqfzM3Ducowcwibi90IVI8hGvbNMTETkOA8frOLotaodhmg-qayxkB8yhDEernGncc9k-R7uEzybNQ9AiyhbUElc6DGZnOfa76vhWIhD9WYlazqJRCmjuD6VQpQIDvmHuh9hOXmXmtp7VSO54njHhfqM5vHqNmLQzVoWXdatQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9803dc4ebc.mp4?token=JeUZIrpaK8vJ-zINo0gaoob2r3NQDEcHjv5-xvGEwlrioMeYlpjj4-5tPMU7QkHaNJmcACg-7-Px7tF5ml23H9GtIRat9Tvih_rP7Vy9Kt3ajqPQpNlb6ku4dUdvosohTVmdmjt8nNfNFpFnKTcHt5ISSb8lWVDzzTiW9ktBwr-rPoqfzM3Ducowcwibi90IVI8hGvbNMTETkOA8frOLotaodhmg-qayxkB8yhDEernGncc9k-R7uEzybNQ9AiyhbUElc6DGZnOfa76vhWIhD9WYlazqJRCmjuD6VQpQIDvmHuh9hOXmXmtp7VSO54njHhfqM5vHqNmLQzVoWXdatQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها دیداری بسیار خوب و سازنده داشتند. دیدار دیگری نیز برای آینده‌ای بسیار نزدیک برنامه‌ریزی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72076" target="_blank">📅 21:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72075">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c847d96020.mp4?token=DFZv5iQ78kzdLMj5nIliqDxmv9MvKNXZpSGJumy1xXpEQPuj2WRcapy2TqjnrPwzbxcP2fTZI9R0ZHvhBPojPoj4AVG79A1NEh0IQaKwH9aUp6uYh_CKwxqOHs2gna442OQspiql4pP-hLrfzU50QOI1iPVm69hZpUAoTT_SrxGHJk6z3Hxqe7whtnY1Whm5Ko0mBut0g4QjD8d7TykZ7Sm-scqVQnDEVN1DlSDt3SYknJYOxuKwloNLc93UCya9N-OVt9CLjX0srC15wIOZ89Lm-ZHK6CybB5799p4djygpGOEDtgVuBCEOY9OSqr5Bhoso7nOBC6nbKPWYH5Kd1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c847d96020.mp4?token=DFZv5iQ78kzdLMj5nIliqDxmv9MvKNXZpSGJumy1xXpEQPuj2WRcapy2TqjnrPwzbxcP2fTZI9R0ZHvhBPojPoj4AVG79A1NEh0IQaKwH9aUp6uYh_CKwxqOHs2gna442OQspiql4pP-hLrfzU50QOI1iPVm69hZpUAoTT_SrxGHJk6z3Hxqe7whtnY1Whm5Ko0mBut0g4QjD8d7TykZ7Sm-scqVQnDEVN1DlSDt3SYknJYOxuKwloNLc93UCya9N-OVt9CLjX0srC15wIOZ89Lm-ZHK6CybB5799p4djygpGOEDtgVuBCEOY9OSqr5Bhoso7nOBC6nbKPWYH5Kd1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
امروز، حدود یک ساعت پیش، گفتگویی انجام شد. گفتگو بسیار خوب پیش رفت و یک ساعت پیش به پایان رسید.
این نشستی بود که سه ساعت به طول انجامید.
مسئله، عظمت — یا عظمتِ بالقوه — و یا نابودی است.
در یک حالت، صحبت از نابودی است؛ و گزینه دیگر، عظمتِ بالقوه است. [ایران] می‌تواند کشوری بزرگ باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72075" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72074">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e59383b3.mp4?token=egX7S5DB1ExaPc2rHm4bXWHFJpFLcRLfEpTvklg06cl6_fVDx5Fh17yvN1rnvjOJYoaqIwQvWBE_WykvKcUXYTHVQdWl9MpdmfHHf28HMDTxN0Z_ojMssgwQrfW3UnC5wafcmTMEpAFL6DxK_uLq6wFEOylvtQH2LtsdXZqUp-CvAV4bdI2DKvQftPbwFFAhX85P4F84SH4iDry-9V3QceranflAlFd7Pk8i946Q4aHxD1H-kFJBOiTI2xRWe3vAplLYZK60bvExWSuaIZ5_7VoJ2oNXNPbQV72ssq3Foi_YQEV4mdu7KrHOxPyhDANsKEasTWdty7s2xPmYtFeWWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e59383b3.mp4?token=egX7S5DB1ExaPc2rHm4bXWHFJpFLcRLfEpTvklg06cl6_fVDx5Fh17yvN1rnvjOJYoaqIwQvWBE_WykvKcUXYTHVQdWl9MpdmfHHf28HMDTxN0Z_ojMssgwQrfW3UnC5wafcmTMEpAFL6DxK_uLq6wFEOylvtQH2LtsdXZqUp-CvAV4bdI2DKvQftPbwFFAhX85P4F84SH4iDry-9V3QceranflAlFd7Pk8i946Q4aHxD1H-kFJBOiTI2xRWe3vAplLYZK60bvExWSuaIZ5_7VoJ2oNXNPbQV72ssq3Foi_YQEV4mdu7KrHOxPyhDANsKEasTWdty7s2xPmYtFeWWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به گفته خانم دکتر؛
مردهایی که به‌طور مداوم رابطه جنسی دارن، طول عمرشون تا 50 درصد افزایش پیدا می‌کنه و همچنین خطر ابتلا به بیماری‌های قلبی هم تا 45 درصد کاهش پیدا می‌کنه.
-در زنان هم باعث میشه سرطان سینه و کیست تخمدان نگیرین.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72074" target="_blank">📅 21:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72073">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc4e3a7b84.mp4?token=SBbSLJI8rKS-2TCaTjvu_DN_poMfhgHFj8t4di9WpxW9LEsfuAlvaiYgTyYHNQfOKFtr-5CCJ53jX4KQ9cNJBtqCwPkAHP--rZLmkR3yV7RuqDOOxUEdOb8OVH8vGg1yNLJJIF-uMQ6gnkWCxmYlJl9uGKNupIq2Wx7R-CdvssoC-BQpIeU6EzYikJ3Ns8fIN7kUV-5G75RDltOb3T8sxZoGjU-ezEx6bCkdAEP84al9mhmcD0XFLGKSUvoNlQNTTKeqOTYw6qfgjbLaissnZNLhu_3tAOMi4tsqz9YD1hn2xFZeaawPP9XIaA3NgUmnMGv5uFig0q7lVaTqkhzb9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc4e3a7b84.mp4?token=SBbSLJI8rKS-2TCaTjvu_DN_poMfhgHFj8t4di9WpxW9LEsfuAlvaiYgTyYHNQfOKFtr-5CCJ53jX4KQ9cNJBtqCwPkAHP--rZLmkR3yV7RuqDOOxUEdOb8OVH8vGg1yNLJJIF-uMQ6gnkWCxmYlJl9uGKNupIq2Wx7R-CdvssoC-BQpIeU6EzYikJ3Ns8fIN7kUV-5G75RDltOb3T8sxZoGjU-ezEx6bCkdAEP84al9mhmcD0XFLGKSUvoNlQNTTKeqOTYw6qfgjbLaissnZNLhu_3tAOMi4tsqz9YD1hn2xFZeaawPP9XIaA3NgUmnMGv5uFig0q7lVaTqkhzb9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: بانوی اول ما کجاست؟ یک جایی همین اطراف است.
ملانیا:
👋
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72073" target="_blank">📅 20:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72072">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اکسیوس:
چند کشور عربی در تلاش‌اند زمینه برگزاری یک دیدار سطح‌بالا میان دونالد ترامپ و مقام‌های ایرانی را در حاشیه مجمع عمومی سازمان ملل در نیویورک فراهم کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72072" target="_blank">📅 20:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72067">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/77b06fbdcc.mp4?token=qQKuMoVss8wHA75JOhz5U9zO1We8TIkfStGXUNGdEwoqBsPDkM6K6Kb39nrj-7zEQXMWqHfT8jfVwUnHpfhRBdGO4gTzek1dTOaG44fo2yIf3Yl5s3BOa2orRTy7cIxCnhAqGSkluDY8CAEXOl6T7_HquprHHxhEKdqFrDBs2khxuk7JrrSV149HadmzxTLawcPAfJN-w5PVcLJt7rNamZvjCaUb9Ri0sIOowtUj5a0p8ALQ4IeET7iF77Sodltr44mv39KneZy5MPcCStNwdp7Hal30kE5DIbiEoNcMv9JGDUM1FKuxPwwrznpJtWFSIW3DoNcjZoauOZt0EAKDzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/77b06fbdcc.mp4?token=qQKuMoVss8wHA75JOhz5U9zO1We8TIkfStGXUNGdEwoqBsPDkM6K6Kb39nrj-7zEQXMWqHfT8jfVwUnHpfhRBdGO4gTzek1dTOaG44fo2yIf3Yl5s3BOa2orRTy7cIxCnhAqGSkluDY8CAEXOl6T7_HquprHHxhEKdqFrDBs2khxuk7JrrSV149HadmzxTLawcPAfJN-w5PVcLJt7rNamZvjCaUb9Ri0sIOowtUj5a0p8ALQ4IeET7iF77Sodltr44mv39KneZy5MPcCStNwdp7Hal30kE5DIbiEoNcMv9JGDUM1FKuxPwwrznpJtWFSIW3DoNcjZoauOZt0EAKDzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی در پایانه لجستیکی شرکت «نووا پوشتا» (Nova Poshta) در حومه روستای اوساتوو (Usatovo) در منطقه اودسا اوکراین، پس از حمله موشکی.
علاوه بر این، ممکن است انبارهای متعلق به شرکت‌های دیگر در آن نزدیکی نیز دچار حریق شده باشند؛ چرا که مجموعه‌ای کامل از انبارها در آن منطقه قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72067" target="_blank">📅 20:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72066">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMsq8NYHcmFgBd4L00ZV08IkqxVzenm5jaG_z9lO7fDHr0VEJIsS71GI26ascQ5GnchsiQhL16iqNIuppYzdWlatVsX4ynYb8LUbmwABGc3AwriXY10x4nWzOpR_4zd1NEwC5uPXIezJuZiduPiH71d4vqpN5UlvCTriaQz9Ssjtea3r-DIabFT9SXiE6jQL5wvUx5SSU-4O6aFdD95ZrH90arEV7dfX1f1w2GmamH07cZ9ybPOndkzgF3l84Pgr7nw61hHvwlrWwmqhXAw3Mkdiay-8IufvPF5FFth1vCnDsnzuEeFvwmeSgl8RpTsVVoOQ8KOSh7CRHJdaQB5UBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهزاده رضا پهلوی وارد نیویورک شده است؛ ایشان قرار است در «اجلاس کونکوردیا» سخنرانی کرده و دیدارهای خصوصی با نمایندگان دیپلماتیک کشورهای حاضر در مجمع عمومی سازمان ملل متحد داشته باشد.
با این حساب دونالد ترامپ، بنیامین نتانیاهو، مسعود پزشکیان و شاهزاده رضاپهلوی هم‌زمان توی نیویورک هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72066" target="_blank">📅 19:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72065">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فعالیت مدارس استان هرمزگان ۲ هفته مجازی شد؛
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان از مجازی شدن فعالیت آموزشی تمامی مدارس استان در همه مقاطع تحصیلی از شنبه به مدت دو هفته، با هدف صیانت از سلامت دانش‌آموزان و حفظ کیفیت فرآیند آموزشی خبر داد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72065" target="_blank">📅 19:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72064">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">در ۲۳ سپتامبر، فعالیت تمام شرکت‌های هواپیمایی ایران در سراسر جهان متوقف خواهد شد.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72064" target="_blank">📅 19:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72063">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/079b2c614f.mp4?token=K5G7kKOEMd_Ea9uqA3rzl3RbtVgGc6S-0ajuO_CPON-ZFvIXXjn8-w9uGP6_HpvsOetvTadxY78kyuO1DtmYKA1Mz5w57hxIh0zu9y1kWfGrDYq2AIpzDbi_TwYWzJzTAoS4gQBeRewkaFGEcQaonHRHeuRY5D9J6qTVP4F0_3gS6TGhIcwSEMhSwFh46nQUnAUGhU1Wmse6N7k081n39u0f2kDlcDUAnZF1aMH-HyvvmSHWYaiPoFI6sCsN0eV0A2EZyxUxbrRZ33SSuF4Jotw4trWM-1ntO2lCyQWPkNJ_idy6G7rPi3eS8xzYtAYNFyS80ZnXN7AYsYgfz2NOcnnuy0cEUgq0PR5YUSg3pz1Q1sCDCcbgl-ZI3xdYfgPFm4U-AYvQep8lYGjOmBCrI0ofCaY6GnR_lqG2KATI-Ayuo0rRHvrqrVrSfa1IeMORlhPu3M5cuzZ2VngjO__VCQjt_rD25axmvffcdj9dg2hbrC_299ytWumE0xjMW1M9zlOtd8Hcowy9tSVpBRQK2By3mwakZEVPi9ACWhNe8YUOejn_a4UgGq2OvlkpxKb_YC0Ha_6LSquv1omnpoUdlVeSzSUtkdWE4KxnMcFqvjY6-SKrw0co2y4-kYYsZVGD7NTkmznBbZf8CRld5sncPrxLDrwqPKOPmzBEmv1cxBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/079b2c614f.mp4?token=K5G7kKOEMd_Ea9uqA3rzl3RbtVgGc6S-0ajuO_CPON-ZFvIXXjn8-w9uGP6_HpvsOetvTadxY78kyuO1DtmYKA1Mz5w57hxIh0zu9y1kWfGrDYq2AIpzDbi_TwYWzJzTAoS4gQBeRewkaFGEcQaonHRHeuRY5D9J6qTVP4F0_3gS6TGhIcwSEMhSwFh46nQUnAUGhU1Wmse6N7k081n39u0f2kDlcDUAnZF1aMH-HyvvmSHWYaiPoFI6sCsN0eV0A2EZyxUxbrRZ33SSuF4Jotw4trWM-1ntO2lCyQWPkNJ_idy6G7rPi3eS8xzYtAYNFyS80ZnXN7AYsYgfz2NOcnnuy0cEUgq0PR5YUSg3pz1Q1sCDCcbgl-ZI3xdYfgPFm4U-AYvQep8lYGjOmBCrI0ofCaY6GnR_lqG2KATI-Ayuo0rRHvrqrVrSfa1IeMORlhPu3M5cuzZ2VngjO__VCQjt_rD25axmvffcdj9dg2hbrC_299ytWumE0xjMW1M9zlOtd8Hcowy9tSVpBRQK2By3mwakZEVPi9ACWhNe8YUOejn_a4UgGq2OvlkpxKb_YC0Ha_6LSquv1omnpoUdlVeSzSUtkdWE4KxnMcFqvjY6-SKrw0co2y4-kYYsZVGD7NTkmznBbZf8CRld5sncPrxLDrwqPKOPmzBEmv1cxBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر ترامپ درباره هوش مصنوعی:
هر کس در حوزه هوش مصنوعی پیروز شود — باید این نکته را به خاطر داشته باشید — و حالا می‌گویم هر کس در حوزه «هوش برتر» (SI) پیروز شود، برنده نهایی است.
آن‌ها همان گروهی هستند که پیروز می‌شوند.
و ما در حال حاضر با اختلاف زیادی نسبت به چین و سایر کشورها پیشتاز هستیم. ما این وضعیت را حفظ خواهیم کرد؛ مسیری بسیار مستقیم و موضعی بسیار قدرتمند را در پیش خواهیم گرفت.
من نمی‌خواهم مانع رشد پدیده‌ای شوم که ابعاد آن از انقلاب صنعتی هم فراتر خواهد رفت.
بسیاری می‌گویند این تحول حتی از انقلاب صنعتی یا خودِ اینترنت هم بزرگ‌تر خواهد بود. و ما بسیار محتاط عمل خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72063" target="_blank">📅 18:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72062">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36fc0e287a.mp4?token=qWPQXmV7F96_FUtuFBIDOPdyhINf5fsZYQ0zVMkaxQCzv1U_Kb24YtgJli_gkRsQCDuZmwX-rBQZg9Zz3vMc1pKSVLjapnUG9aGSWce1Tult28Ef3nl6r1Jaxr4Lj0O3JpWLjvywBy4wowF8nWo2HUB0CEmgGMLx-HhDqcgZziAWVA1hBh2Htq06AdC_lDW3Ghr6SVtlh_8h_pgHf-yto3rklUWOG0Is_xNsUesQwDzGveKt6bNev7ZhtrvgG4vI3WGyVbhibIdL8gvPQS-7-0pTdrNb0XKs7CwT9HDAby4adbcJJBuU2LeMqdgerSwtePuutB8KDiKFBVOs9SyV_pauFBxlQqaUygh5h7Qbwdxy5rpIgHV2jrbnxSXXV4iBftTGEl9v1Uyg1gYuhl_nnB1LRb7abRPsG3--g65nllxFeG511sts7jsERMMjvn9DLuDZqrbqX9OvFLyeXMgL8B4-vp2MW6IobT2Vhe5Cgn4mSruVQjEEHKPp6Dp3I2pIK2koeCc84B9YIIEB13b4XTL4wIzFpyn1ALJ4frHH1Ir7OIbnKZEQ80zTaNnZUDnAhgFwlf652gYn7tMQwuR_4w4aezwjpuCqlwMbPY7mLuJc7T4-A0izPonhXGAiQip9MmjEFSPtHwxspfFs0fXWQ_kcNzWcPigresVTFOJbZnc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36fc0e287a.mp4?token=qWPQXmV7F96_FUtuFBIDOPdyhINf5fsZYQ0zVMkaxQCzv1U_Kb24YtgJli_gkRsQCDuZmwX-rBQZg9Zz3vMc1pKSVLjapnUG9aGSWce1Tult28Ef3nl6r1Jaxr4Lj0O3JpWLjvywBy4wowF8nWo2HUB0CEmgGMLx-HhDqcgZziAWVA1hBh2Htq06AdC_lDW3Ghr6SVtlh_8h_pgHf-yto3rklUWOG0Is_xNsUesQwDzGveKt6bNev7ZhtrvgG4vI3WGyVbhibIdL8gvPQS-7-0pTdrNb0XKs7CwT9HDAby4adbcJJBuU2LeMqdgerSwtePuutB8KDiKFBVOs9SyV_pauFBxlQqaUygh5h7Qbwdxy5rpIgHV2jrbnxSXXV4iBftTGEl9v1Uyg1gYuhl_nnB1LRb7abRPsG3--g65nllxFeG511sts7jsERMMjvn9DLuDZqrbqX9OvFLyeXMgL8B4-vp2MW6IobT2Vhe5Cgn4mSruVQjEEHKPp6Dp3I2pIK2koeCc84B9YIIEB13b4XTL4wIzFpyn1ALJ4frHH1Ir7OIbnKZEQ80zTaNnZUDnAhgFwlf652gYn7tMQwuR_4w4aezwjpuCqlwMbPY7mLuJc7T4-A0izPonhXGAiQip9MmjEFSPtHwxspfFs0fXWQ_kcNzWcPigresVTFOJbZnc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر ترامپ درباره هوش مصنوعی:
از این پس، تمام اسناد ایالات متحده — و به امید خدا اسناد سراسر جهان — تغییر خواهند کرد تا به جای واژه «مصنوعی» (Artificial)، از اصطلاح بسیار دقیق‌ترِ «اَبَر» (Super) استفاده شود.
به عبارت دیگر، به دنیای جدید «اَبَر-هوش» (Superintelligence) یا همان SI خوش آمدید.
باید دید این ایده چه بازخوردی خواهد داشت؛ هرچه باشد، خیلی بهتر به نظر می‌رسد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72062" target="_blank">📅 18:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72061">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6100a5cc1d.mp4?token=OfGWYgvEuNYWf5NT4RiglzP_Y3ltqct3FMMOwo5U0zPfToEEhDBIVzVhY837vhNkDikjjXLT26jxfIRESPJvHNjQX-afB4lzSOfc2PasK9BjGdK4f2RdsSQuOt3S8TDHylzGtnPjs3hAik00lETtS2YUOerzQbTpW7_0Mcv-yAQCsQejpfc55Yze_HSWmrnBh1A6G2_Z-mSN4XE0Ply87rwIVVGuWuiZgrB3GBWvS-0KpjCHfMVGgDeq1JaeFsJuJaRhmkOz2ebFgXX1-ZrB5L398IDDazTxsm1zgvkcM0gMgiJndaUMmHVDJreOkqI0FcX445hixyiu7ODsuo4mHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6100a5cc1d.mp4?token=OfGWYgvEuNYWf5NT4RiglzP_Y3ltqct3FMMOwo5U0zPfToEEhDBIVzVhY837vhNkDikjjXLT26jxfIRESPJvHNjQX-afB4lzSOfc2PasK9BjGdK4f2RdsSQuOt3S8TDHylzGtnPjs3hAik00lETtS2YUOerzQbTpW7_0Mcv-yAQCsQejpfc55Yze_HSWmrnBh1A6G2_Z-mSN4XE0Ply87rwIVVGuWuiZgrB3GBWvS-0KpjCHfMVGgDeq1JaeFsJuJaRhmkOz2ebFgXX1-ZrB5L398IDDazTxsm1zgvkcM0gMgiJndaUMmHVDJreOkqI0FcX445hixyiu7ODsuo4mHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ نام «هوش مصنوعی» (AI) را به «اَبَر‌هوش» (SI) تغییر می‌دهد.
او می‌گوید استفاده از واژه «مصنوعی» باعث می‌شود که هوش، «ساختگی» به نظر برسد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/72061" target="_blank">📅 18:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72060">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/156037c15c.mp4?token=O0fA8Bj2CDZdLaL4O-YNOVol-hpY5MVGR2y_5PdNX9Pp9biXHCSwnUd8vYBbXwJO5zDUZu_DZg1cBZzRDaaAi0tLTvLU0y1q2wF5LRTQukU95Zi7TN-2GznGSEY8o6_VPZ2egDFxs-oz2Wz-oRzrotcuD4G33tQnSPyiZERRgyvZw1dBZYpYDwWDLN4LOEgEXx2ai8Ar1N9oPCwk6MVHY8ZTS95xXNmBYcWCpi-nK48B2o-JPPLG2a9jOxVwHRXqNi7Wp1ywN3BhTslHAIal_CSkscsES_HoNjMjc1Fwi3IfTOUC22FIGR_1f4Ec8WxBGq-TQ3zK_Qp6FNs20PI9ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/156037c15c.mp4?token=O0fA8Bj2CDZdLaL4O-YNOVol-hpY5MVGR2y_5PdNX9Pp9biXHCSwnUd8vYBbXwJO5zDUZu_DZg1cBZzRDaaAi0tLTvLU0y1q2wF5LRTQukU95Zi7TN-2GznGSEY8o6_VPZ2egDFxs-oz2Wz-oRzrotcuD4G33tQnSPyiZERRgyvZw1dBZYpYDwWDLN4LOEgEXx2ai8Ar1N9oPCwk6MVHY8ZTS95xXNmBYcWCpi-nK48B2o-JPPLG2a9jOxVwHRXqNi7Wp1ywN3BhTslHAIal_CSkscsES_HoNjMjc1Fwi3IfTOUC22FIGR_1f4Ec8WxBGq-TQ3zK_Qp6FNs20PI9ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایران:
نیروی دریایی ایالات متحده اخیراً بیش از یک میلیارد بشکه نفت را از تنگه هرمز اسکورت و عبور داده است و حجم نفت در حال عبور، بیش از هر زمان دیگری از آغاز جنگ است.
ما هر روز و هر شب، به ترتیب ۲۲، ۲۵، ۳۰، ۳۲ و ۳۷ کشتی را [از این مسیر] عبور می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/72060" target="_blank">📅 18:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72059">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=iydsxo33xitn56Gc9uXJbEUJmPa8AZNu01NSFoeq6Da99LaVJpmXDzaUo2Y2rB1uAS7BC8VionY7X3d7OMpTDXVuUHq_exqyf47flOEup2lD8HPlQWoBy9QHDWny_IOHHtsow1jCBD6QbNw9DENwun-DGSxCH3ZOGm2K0Kj-ZuxjtC6XIHRWNNci7CBiFHygDJYItW16DnKDrOE9ySHdsjRiyA5fW_GmSQnTI1Y1j8-o74l9RQ60CEs9RTr8Pek3ZJfD2tPSC14fdNGz-8fBY5kwzjnzGA2aLYH0WynlR9vvyRW1DrJq08SQYw7hj8l-WIwJnhurfwfk4ZyN_2l2fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=iydsxo33xitn56Gc9uXJbEUJmPa8AZNu01NSFoeq6Da99LaVJpmXDzaUo2Y2rB1uAS7BC8VionY7X3d7OMpTDXVuUHq_exqyf47flOEup2lD8HPlQWoBy9QHDWny_IOHHtsow1jCBD6QbNw9DENwun-DGSxCH3ZOGm2K0Kj-ZuxjtC6XIHRWNNci7CBiFHygDJYItW16DnKDrOE9ySHdsjRiyA5fW_GmSQnTI1Y1j8-o74l9RQ60CEs9RTr8Pek3ZJfD2tPSC14fdNGz-8fBY5kwzjnzGA2aLYH0WynlR9vvyRW1DrJq08SQYw7hj8l-WIwJnhurfwfk4ZyN_2l2fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ایالات متحده و ایران قطعاً این کار را به سرانجام خواهند رساند. ما به هر طریقی که شده، این کار را انجام خواهیم داد. این کار انجام خواهد شد.
این کار به‌سرعت انجام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/72059" target="_blank">📅 18:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72058">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e9a7cd318.mp4?token=OqEVHdv9fQxfERWssYTXQrdKpMMrZH2RDnW5WSQCH7VNwWqnduOqgSOHduWoDWmyRecrr54COr_cYvb7BYWRL5BJjRI2wJCRLlj2WBlWLsJuztqDb6n177bBS78BLflogri_EvhlgnBAen3uuvF08U-nIfFX5RwsE9beNOJTPBCM_iAOgIONf9qVv8zRbyVlG98bZUhgJCq5RAR3AEGvGyFc4HcXmUabE--v4u-PQzm99849tELaapy42BwfPpH6Qw9jFhA4KgbCv0COhh_Vv492k7r9D55xAs8bDjWW5wVg4mvXKCeoDOw_R7PRQgTBnCmL5AwgWGpjUSNaAWuazhtOknv6FC7el5udxyhfeqg6--PqmgGZK61mHm-gIv7jyGKzlKmJYCw43-e2ujPxWWHydQCE3aisCMBHmKWEKPRG9xantkUM_xWN2_lB9BOOrp058F3lB7DabrHoRJ4SRGftnXJvLsSsbuGmduDDTxaJJkfnuTK0OM6lUlWJHhx1dRv2ucjwNRh6mYhp3ebwluptEVFc_NNItqooMvb-CYL_VMdSfKptmAqExGuVdxff7UyHt-1p8mwA-HogYN95llN7W4GDoTX07mPF40SJyDZUeIeLfCJJQDbFlljvp7Sd_tE022BcCkhtucuothfNZLAWpnVZ3rnSbWe6VIOjC3c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e9a7cd318.mp4?token=OqEVHdv9fQxfERWssYTXQrdKpMMrZH2RDnW5WSQCH7VNwWqnduOqgSOHduWoDWmyRecrr54COr_cYvb7BYWRL5BJjRI2wJCRLlj2WBlWLsJuztqDb6n177bBS78BLflogri_EvhlgnBAen3uuvF08U-nIfFX5RwsE9beNOJTPBCM_iAOgIONf9qVv8zRbyVlG98bZUhgJCq5RAR3AEGvGyFc4HcXmUabE--v4u-PQzm99849tELaapy42BwfPpH6Qw9jFhA4KgbCv0COhh_Vv492k7r9D55xAs8bDjWW5wVg4mvXKCeoDOw_R7PRQgTBnCmL5AwgWGpjUSNaAWuazhtOknv6FC7el5udxyhfeqg6--PqmgGZK61mHm-gIv7jyGKzlKmJYCw43-e2ujPxWWHydQCE3aisCMBHmKWEKPRG9xantkUM_xWN2_lB9BOOrp058F3lB7DabrHoRJ4SRGftnXJvLsSsbuGmduDDTxaJJkfnuTK0OM6lUlWJHhx1dRv2ucjwNRh6mYhp3ebwluptEVFc_NNItqooMvb-CYL_VMdSfKptmAqExGuVdxff7UyHt-1p8mwA-HogYN95llN7W4GDoTX07mPF40SJyDZUeIeLfCJJQDbFlljvp7Sd_tE022BcCkhtucuothfNZLAWpnVZ3rnSbWe6VIOjC3c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
من از همه کشورها خواستم تا در اعمال
انزوای کامل اقتصادی ایران با ما همراه شوند؛ تا زمانی که آن‌ها حملات خود به کشتی‌های تجاری را متوقف کنند، از جاه‌طلبی‌های هسته‌ای خود دست بردارند و به حمایت از تروریسم پایان دهند.
این رژیم تروریستی نه به این دلیل که قدرتمند و با اعتمادبه‌نفس است، بلکه به این خاطر که ضعیف و درمانده است، چنین رفتار نامناسبی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72058" target="_blank">📅 18:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72057">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/415b898f05.mp4?token=APvXaXmvQAkBt3sOZraAIp3Wr5c8qq-juln8GPX6W3txCT8zpE8giGItcl899OyJrE5OJ3bphYT6qtDfoqBy1u4LOFrBIvpePr5CW9nxkiJ-7E3Q35SYI5XF2dUJy-EkEKwBKDok_vn1Ug3tg-Evle0uDECMQ6JylnbXjWVnztHPzQfkQbmIpBpMvUVrJeKa1oIwpk9pigP40E4vvnwwJBoDhprS4Rle3rMyvswtT-M9Vu_FfITLSimPUPXYIanvy86-_VndtqEg69Y8ePbM2RApTFBEGB7NFO0Xj97OjGkrrSwwbP9tv2KOalE1N7ZxBz2mnXw0BKmV11BqOcer_IfkMRiJ7Ik1gbsVI7jQLHX8-S_090X4WxkyKK-IlrbDqBkr7spq4EVSp5MtkHG-rbFXJ6vLR5ykT29we4AQCHBL5Eeaas2Se3iDGUPQ3ywVg_Bgy3hV2prFGD2UvOZ_6KZxYNXGS30iuNfTUGPCGVcjgQ-FguLfT6dBIDP0soGz1nYetEZ4jlK9Ww-JocgmX9cmicLnOXvIAdqDjfsw8QQss83rAVqbSjEN0MVp33Seh-QFCchmWuEmrbcR5kqzorXjqXYOT7W-RLxUzDI9wBgPnmdRtWf5GZiz8uvFeSDq1Ub5Clj6cCcwmWaxN9NMHOSJ40Z1o4Z2FNiOQnsN5to" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/415b898f05.mp4?token=APvXaXmvQAkBt3sOZraAIp3Wr5c8qq-juln8GPX6W3txCT8zpE8giGItcl899OyJrE5OJ3bphYT6qtDfoqBy1u4LOFrBIvpePr5CW9nxkiJ-7E3Q35SYI5XF2dUJy-EkEKwBKDok_vn1Ug3tg-Evle0uDECMQ6JylnbXjWVnztHPzQfkQbmIpBpMvUVrJeKa1oIwpk9pigP40E4vvnwwJBoDhprS4Rle3rMyvswtT-M9Vu_FfITLSimPUPXYIanvy86-_VndtqEg69Y8ePbM2RApTFBEGB7NFO0Xj97OjGkrrSwwbP9tv2KOalE1N7ZxBz2mnXw0BKmV11BqOcer_IfkMRiJ7Ik1gbsVI7jQLHX8-S_090X4WxkyKK-IlrbDqBkr7spq4EVSp5MtkHG-rbFXJ6vLR5ykT29we4AQCHBL5Eeaas2Se3iDGUPQ3ywVg_Bgy3hV2prFGD2UvOZ_6KZxYNXGS30iuNfTUGPCGVcjgQ-FguLfT6dBIDP0soGz1nYetEZ4jlK9Ww-JocgmX9cmicLnOXvIAdqDjfsw8QQss83rAVqbSjEN0MVp33Seh-QFCchmWuEmrbcR5kqzorXjqXYOT7W-RLxUzDI9wBgPnmdRtWf5GZiz8uvFeSDq1Ub5Clj6cCcwmWaxN9NMHOSJ40Z1o4Z2FNiOQnsN5to" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
بزدلان و خائنان بسیار دوست دارند بگویند که ذخایر مهمات ایالات متحده رو به اتمام است، اما این حرف صحت ندارد.
ما بیش از هر مقداری که حتی تصور استفاده از آن را داشته باشیم، مهمات در اختیار داریم و با سرعتی بی‌سابقه مشغول تولید آن‌ها هستیم. ما با سرعتی بیش از هر زمان دیگری در حال افزایش ذخایر خود هستیم؛ آن هم با تجهیزاتی که در بالاترین سطح کیفی قرار دارند.
علاوه بر این، در آینده‌ای بسیار نزدیک، کارخانه‌های عظیم تولید مهمات افتتاح خواهند شد. هم‌اکنون ۱۸ کارخانه از این دست توسط برترین شرکت‌های دفاعی جهان در حال ساخت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/72057" target="_blank">📅 18:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72056">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=gTqTBFU9KKsRNrdoBpuUVcOj6ObKJxXTxnywEWY3K9uf_RQoIMlK9aq4VcRtZrwk7pB-ouPzr3mNSRcN1I0Lb3yQZ_Iwflk1yLpDjTt9dF7QfB_bChXwdICcQCRyBeULBrZ004rLkrrQ4hTsZIm2jgZh99ezcQVFE0FGgGQKTl6cui_zYWKAHkJ6XKo9YlJp88QxKZNlnFB4YCA9KLNq3Dwnmmky3zuqze9hZu3750LOh15_kufeS5SNQ8CJAa-Y0uRp8G1iCXpOITgb1HcMl-nKutcoOQimgkm4ZKoaRYaKJGjrQuJrX1-PXj1mxFHzqkBIAh-CPC-po8xqI1AI2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=gTqTBFU9KKsRNrdoBpuUVcOj6ObKJxXTxnywEWY3K9uf_RQoIMlK9aq4VcRtZrwk7pB-ouPzr3mNSRcN1I0Lb3yQZ_Iwflk1yLpDjTt9dF7QfB_bChXwdICcQCRyBeULBrZ004rLkrrQ4hTsZIm2jgZh99ezcQVFE0FGgGQKTl6cui_zYWKAHkJ6XKo9YlJp88QxKZNlnFB4YCA9KLNq3Dwnmmky3zuqze9hZu3750LOh15_kufeS5SNQ8CJAa-Y0uRp8G1iCXpOITgb1HcMl-nKutcoOQimgkm4ZKoaRYaKJGjrQuJrX1-PXj1mxFHzqkBIAh-CPC-po8xqI1AI2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
من برای انتخابات در مورد ایران مطلقاً هیچ اعتباری قائل نبوده‌ام و نخواهم بود؛ این موضوع حتی به ذهنم هم خطور نمی‌کند.
تنها چیزی که اهمیت دارد این است که ایران هرگز به سلاح هسته‌ای دست نخواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/72056" target="_blank">📅 18:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72055">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">#فوری
؛پرزیدنت ترامپ درباره ایران:باید تصمیم بزرگی بگیرم.
آیا توافقی با ایران صورت خواهد گرفت که به آن‌ها اجازه دهد کشورشان را بازسازی کنند و کشوری بسیار بزرگ‌تر از آنچه پیش‌تر بود بسازند؛ شاید حتی یکی از بزرگ‌ترین کشورهای خاورمیانه یا حتی جهان؟
یا اینکه جمهوری اسلامی را نابود کنم—آن هم به سرعت—و هرگز به آن‌ها فرصتی ندهم که دوباره دست به کشتار و ویرانی مردم و کشورها بزنند؟
آیا آن‌ها را به جهنم بفرستم، بدون هیچ شانس بقا و بدون هیچ امیدی به عظمت در نسل‌های آینده؟
اما معتقدم که بلافاصله پس از انتخابات به توافق خواهیم رسید، چرا که تن ندادن به آن برایشان منطقی نیست.
آن‌ها منتظرند ببینند عملکرد من در انتخابات میان‌دوره‌ای چگونه خواهد بود. چیزی که متوجه نیستند این است که من اصلاً نامزد آن انتخابات نیستم. من آن کار را قبلاً انجام داده و با اکثریتی قاطع پیروز شده‌ام.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/72055" target="_blank">📅 18:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72054">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5ddeee9dd.mp4?token=fppyqnJHMbWeYeINkOfNc5dg-4j91nrNy4mKyukOmnmZMZTkUSpXUzAfWS6gtMZIIEJqNmz5bBG5cGS6Gg30h4eKXorYCXVidkgP1jwzAMxQpZDLhTWQBT3VnNygr8ESlq10DuDmMujnCFsCZ9pNMB0jp4I5LXEMeM93Oa1NoYmImoUFK98wD6l4QwSM2SHDPJ2CV24saCx0YoeBBovxJfnYXConWbjhyTl-RTg2BpD6xpwjaLzuy96ciyZZC1ratDgt7OtkxSTfNhVK0Yd7c-fl4jOdrNKs3aaAII01GNhmcZ5YcNwl8XuKBpxtqU8Am-V4F-gwknQZKreVWatqoRU-wzIKmmo4PAIlxljNMQnnpao33N8fV1NbXnkSaQxOrcWTRUGliWN4dQGKg7aTOf43qlDb59C70r3Yn3NpEM8-yfT9KllXVnNxre0JLwsMt17977Jbl1QBUEl8fLe_qiBce3o5TG-StckHY4EsiCnQvOoPYWdBC4Ec2rNGg30uUDYDc1Vk65ZPMt_I2ZacM867JI1vXwS5xwaIBpvU1rNS6nNxXLecZdM12Gj-MgFlt6QRZ_8FoBEZhLyFtS2twRlAyjwnLH2GzFv337gc_EByG1or7ayxM7E84tEuHlk46y1P0csS7Uud2XnV7w6eCbFCbBK8TpGOxos_N6gwN1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5ddeee9dd.mp4?token=fppyqnJHMbWeYeINkOfNc5dg-4j91nrNy4mKyukOmnmZMZTkUSpXUzAfWS6gtMZIIEJqNmz5bBG5cGS6Gg30h4eKXorYCXVidkgP1jwzAMxQpZDLhTWQBT3VnNygr8ESlq10DuDmMujnCFsCZ9pNMB0jp4I5LXEMeM93Oa1NoYmImoUFK98wD6l4QwSM2SHDPJ2CV24saCx0YoeBBovxJfnYXConWbjhyTl-RTg2BpD6xpwjaLzuy96ciyZZC1ratDgt7OtkxSTfNhVK0Yd7c-fl4jOdrNKs3aaAII01GNhmcZ5YcNwl8XuKBpxtqU8Am-V4F-gwknQZKreVWatqoRU-wzIKmmo4PAIlxljNMQnnpao33N8fV1NbXnkSaQxOrcWTRUGliWN4dQGKg7aTOf43qlDb59C70r3Yn3NpEM8-yfT9KllXVnNxre0JLwsMt17977Jbl1QBUEl8fLe_qiBce3o5TG-StckHY4EsiCnQvOoPYWdBC4Ec2rNGg30uUDYDc1Vk65ZPMt_I2ZacM867JI1vXwS5xwaIBpvU1rNS6nNxXLecZdM12Gj-MgFlt6QRZ_8FoBEZhLyFtS2twRlAyjwnLH2GzFv337gc_EByG1or7ayxM7E84tEuHlk46y1P0csS7Uud2XnV7w6eCbFCbBK8TpGOxos_N6gwN1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ:
ما در آمریکا به‌تازگی بیست‌ و پنجمین سالگرد بدترین حمله تروریستی تاریخ، یعنی ۱۱ سپتامبر را پشت سر گذاشتیم؛ حمله‌ای که جان سه هزار نفر را گرفت. درست در همین نزدیکی‌ها.
دو هفته دیگر، سومین سالگرد حمله ۷ اکتبر در اسرائیل را گرامی خواهیم داشت؛ حمله‌ای که در آن تروریست‌های تحت حمایت مالی ایران، ۱۲۰۰ غیرنظامی کاملاً بی‌گناه — از جمله ده‌ها آمریکایی و بسیاری از نوزادان؛ نوزادانی کوچک، ظریف و زیبا — را شکنجه کردند، مثله کردند و به قتل رساندند.
رهبر عالی ایران آن کشتار را جشن گرفت و آن را «خدمتی به بشریت» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/72054" target="_blank">📅 18:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72053">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f9289304.mp4?token=sEHbyv5U4IDTVetspkwTqzEWxpAuAOcSOLjfeKiSAR3KXAs9DTgM8KBZpehFanJfYGUlr28IQKwV1bU9oDguM0StYq98OnKi3PabUIl-tAKcmPgItOfwQT1POTbDWcOMD5XETFdI_g2Hk2k3CVPvpf99Ap_qXsjDQdMEZqXM4i0NWJpzxQFdNYhHdX-Pjs5pHX1NyHH3hYwyW8wx-Xqos_NyT_XA5n6NM7gmVxwEZXxCFdRtLTF_LKXBHxpTou4iMi6p2gRofYKaprnXuPEsUGUQqW6UQ3btM7hFvLtpy3-fS2GjAElnTee8Myw3FtPp8jDA3CiuRrmco4-9-6MIDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f9289304.mp4?token=sEHbyv5U4IDTVetspkwTqzEWxpAuAOcSOLjfeKiSAR3KXAs9DTgM8KBZpehFanJfYGUlr28IQKwV1bU9oDguM0StYq98OnKi3PabUIl-tAKcmPgItOfwQT1POTbDWcOMD5XETFdI_g2Hk2k3CVPvpf99Ap_qXsjDQdMEZqXM4i0NWJpzxQFdNYhHdX-Pjs5pHX1NyHH3hYwyW8wx-Xqos_NyT_XA5n6NM7gmVxwEZXxCFdRtLTF_LKXBHxpTou4iMi6p2gRofYKaprnXuPEsUGUQqW6UQ3btM7hFvLtpy3-fS2GjAElnTee8Myw3FtPp8jDA3CiuRrmco4-9-6MIDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
این رژیم امسال بیش از ۷۲ هزار تن از شهروندان خود را به خاک و خون کشید.
تصور کنید چنین رژیم پلیدی قدرت آن را داشته باشد که از پشتِ سپرِ هسته‌ای، دست به حملات تروریستی گسترده بزند.
این واقعیتی بود که باید با آن روبرو می‌شدیم؛ واقعیتی که بسیاری ترجیح دادند آن را نادیده بگیرند. همه آن‌ها آن را نادیده گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/72053" target="_blank">📅 18:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72052">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e271237b80.mp4?token=Lf7zAeRxcUYubMwTJJAl-SVB3KclGy4fGJ6iR0XXtzVYK4o3Hst-akUDuuqQN9MTvyyYOjOmPewhYYKg5r3uZJ2r-s1cFTEswqTGmkWtXmwqoL7FYE3CLL58XuUrI9GKzJR7QnX-ZXGugT1dbdttYxZDFOpSyHCJ9cOi7VqKfgc9DUK2cgIMr9rmA6wzMw1LGwwjJiriXc5F7Rk8J7nJyyavIoNOjfmtTaupvcoI0X5z1SABphiY9nx7eg4J4H7s2kilV0CzURTgVI_24JZ6fNRLBfM3Wg4HD7yLKkvEQmV9-STzQwHhzmeDm-Z5aW_qv8izsgiOCUnIqPm20WU0bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e271237b80.mp4?token=Lf7zAeRxcUYubMwTJJAl-SVB3KclGy4fGJ6iR0XXtzVYK4o3Hst-akUDuuqQN9MTvyyYOjOmPewhYYKg5r3uZJ2r-s1cFTEswqTGmkWtXmwqoL7FYE3CLL58XuUrI9GKzJR7QnX-ZXGugT1dbdttYxZDFOpSyHCJ9cOi7VqKfgc9DUK2cgIMr9rmA6wzMw1LGwwjJiriXc5F7Rk8J7nJyyavIoNOjfmtTaupvcoI0X5z1SABphiY9nx7eg4J4H7s2kilV0CzURTgVI_24JZ6fNRLBfM3Wg4HD7yLKkvEQmV9-STzQwHhzmeDm-Z5aW_qv8izsgiOCUnIqPm20WU0bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها موشکی ساختند که قادر به هدف قرار دادن اروپا بود و به آن بسیار افتخار می‌کردند. امیدوارم اروپایی‌ها متوجه این موضوع باشند.
هدف ایران این بود که در پناهِ سپرِ موشک‌های بالستیک متعارف، ساخت بمب هسته‌ای خود را تکمیل کند.
اگر آن‌ها موفق می‌شدند، آن رژیم شرور آزاد بود که تا ابد به گسترش وحشت و مرگ بپردازد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/72052" target="_blank">📅 18:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72051">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=kaTVLagcMvcxYJmxD_9ldnv_hz1O8PitKv4RBbp9RjaTvx9BEl4Di9LDfWgCt_oKhQobdS6c3bQSofWRLz6eY8Aa1lCvR4tY2iKhRBu6pJGEhHYDMqZSCkgTpk7-vq2dIFBBQ8ZMzaQzBwODIAlXfvJSb3qz92Ffrb2x-VIR2uX6chmiSlE3c6B1V9UjEaSbIHajwYsScGsMCJVN4168rXEZ9xFwWcmf-gO-ogm0x17xuTmCgoFv4jsN8mM6oObx16Ap_AyoIfqjFQkOH8ti6sHpaooA-f8zRSY06H9P0BGEcVwun7Gy109DscTCGLdjnDkQTqixNiB14g7DR6Rm9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=kaTVLagcMvcxYJmxD_9ldnv_hz1O8PitKv4RBbp9RjaTvx9BEl4Di9LDfWgCt_oKhQobdS6c3bQSofWRLz6eY8Aa1lCvR4tY2iKhRBu6pJGEhHYDMqZSCkgTpk7-vq2dIFBBQ8ZMzaQzBwODIAlXfvJSb3qz92Ffrb2x-VIR2uX6chmiSlE3c6B1V9UjEaSbIHajwYsScGsMCJVN4168rXEZ9xFwWcmf-gO-ogm0x17xuTmCgoFv4jsN8mM6oObx16Ap_AyoIfqjFQkOH8ti6sHpaooA-f8zRSY06H9P0BGEcVwun7Gy109DscTCGLdjnDkQTqixNiB14g7DR6Rm9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
سال گذشته، پس از آغاز به کار، مذاکراتی را با ایران آغاز کردم و به آن‌ها پیشنهاد دادم که در ازای پایان دادن به برنامه هسته‌ای و حمایتشان از تروریسم، از همکاری کامل اقتصادی برخوردار شوند.
اما آن‌ها نپذیرفتند. این اشتباه بزرگی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/72051" target="_blank">📅 18:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72050">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29ba0a501a.mp4?token=b-AZ3BHaZwSnXvi6LEpMUQf22DQCLZfiIrsS9PDNdrpDcx0IVpY53xITcsq-FpOIsgzDdeZJyCdAyd8SsoeQHtEtVLJhIsZD-wMyG2fAIa37uGXLsrGqSZ52soiZO4hRcPfvfsWk6ZNr6NK2OtIvNpfTyLeGloDBtAhRDEXhSnIwl4gBqaSpfbPMrArpg44fI1fcQyjHkFOR9rWwhEAJir_MvB1wvRljuuklen-JF9hfS2keGLexGeDlKWffl-T5SXjbbDSNuPKS_5ILriW8i-hRDvwUhL61z1VNin9q3oO9zYcq7jgK_Gr3GjEmzrJlbDr4_A07tqGr44s9oOd3iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29ba0a501a.mp4?token=b-AZ3BHaZwSnXvi6LEpMUQf22DQCLZfiIrsS9PDNdrpDcx0IVpY53xITcsq-FpOIsgzDdeZJyCdAyd8SsoeQHtEtVLJhIsZD-wMyG2fAIa37uGXLsrGqSZ52soiZO4hRcPfvfsWk6ZNr6NK2OtIvNpfTyLeGloDBtAhRDEXhSnIwl4gBqaSpfbPMrArpg44fI1fcQyjHkFOR9rWwhEAJir_MvB1wvRljuuklen-JF9hfS2keGLexGeDlKWffl-T5SXjbbDSNuPKS_5ILriW8i-hRDvwUhL61z1VNin9q3oO9zYcq7jgK_Gr3GjEmzrJlbDr4_A07tqGr44s9oOd3iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها قلدرِ خاورمیانه بودند، اما دیگر قلدر نیستند.
از همان روز نخستِ ورودم به عرصه سیاست، موضعی تزلزل‌ناپذیر داشته‌ام:
هرگز اجازه نخواهم داد  ایران به سلاح هسته‌ای دست یابد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/72050" target="_blank">📅 18:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72049">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a4eccca8.mp4?token=ksvPwJtgn2ANaxEZ8jSjPWCIZa_-MdW9SKGCxTHThSZPu0cmtDXxXXrrjBFikxRPwCPmTS-4R8S-bkNWvPKq2SQ0J08gPAegVRDfACdZY93HrMSk5mkoYtcXNltyPUHQqzWLMJOudo28RP2bCBG0ESPEGs0J8yPh4Yy4_TxAYWgXza_UjmZv8bwqBSYhc2fBBvTVGmuFcAt7ylNr_Fcgbj9XYdvlZwOtNWfUlG1eO0vPG9_lEApB80y-zXQl9Us6paC3KETh0tyO8gv17tUwlAmZr1wmj-gu_zyc2B1xRIROYzADbFRlBZhYUebxnl8yE_yZYuYC-0V2Y2Od5Ebxhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a4eccca8.mp4?token=ksvPwJtgn2ANaxEZ8jSjPWCIZa_-MdW9SKGCxTHThSZPu0cmtDXxXXrrjBFikxRPwCPmTS-4R8S-bkNWvPKq2SQ0J08gPAegVRDfACdZY93HrMSk5mkoYtcXNltyPUHQqzWLMJOudo28RP2bCBG0ESPEGs0J8yPh4Yy4_TxAYWgXza_UjmZv8bwqBSYhc2fBBvTVGmuFcAt7ylNr_Fcgbj9XYdvlZwOtNWfUlG1eO0vPG9_lEApB80y-zXQl9Us6paC3KETh0tyO8gv17tUwlAmZr1wmj-gu_zyc2B1xRIROYzADbFRlBZhYUebxnl8yE_yZYuYC-0V2Y2Od5Ebxhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ:
من هیچ تمایلی ندارم که اجازه دهم خطرات، حتی یک روز دیگر هم رشد کنند. من به اینکه بگذاریم مشکلات وخیم‌تر شوند، اعتقادی ندارم؛ چرا که حل آن‌ها دشوارتر می‌شود.
بنابراین، در حالی که دیگران حرف می‌زدند، من عمل کردم.
در حالی که دیگران از صلح سخن می‌گفتند، من صلح را محقق ساختم.
در حالی که دیگران تهدیدها را نادیده می‌گرفتند، من با آن‌ها مقابله کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/72049" target="_blank">📅 18:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72048">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd7fee3bd0.mp4?token=jJ6uWj7R_70WTn8dvgIOB4SHL7eXj_tI-TkegVACi-tjdGlLEMbwGiS2YtHYcUk7Hl_5bjQjI75PexSkSwcGtwKhq2mx30luum2ECoR4taYTShn0nfI4CQ5-BTfuXm5cdFvmBCLELLo0crl85iklo-AvqC-4AuoGszdLk9-iNsu0maG7BOHfyPJ7LveaamDqg8qOB43cUcMzo16krgc81rCPxpCzvtm-rDdfgZEUN-HhScvtah4UN1nlK-v483k_eoXWEfdDQ5r8un4YmhHp1w0yjgEOzQdHY7E8Ht2PBaJ4IJVPm9RQWFEufNxFHqYObUo07O4y2ea_xLU6WnYrBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd7fee3bd0.mp4?token=jJ6uWj7R_70WTn8dvgIOB4SHL7eXj_tI-TkegVACi-tjdGlLEMbwGiS2YtHYcUk7Hl_5bjQjI75PexSkSwcGtwKhq2mx30luum2ECoR4taYTShn0nfI4CQ5-BTfuXm5cdFvmBCLELLo0crl85iklo-AvqC-4AuoGszdLk9-iNsu0maG7BOHfyPJ7LveaamDqg8qOB43cUcMzo16krgc81rCPxpCzvtm-rDdfgZEUN-HhScvtah4UN1nlK-v483k_eoXWEfdDQ5r8un4YmhHp1w0yjgEOzQdHY7E8Ht2PBaJ4IJVPm9RQWFEufNxFHqYObUo07O4y2ea_xLU6WnYrBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ترامپ:
با افتخار به شما اعلام می‌کنم که آمریکا بازگشته است و کشور ما امروز قوی‌تر از هر زمان دیگری است.
اقتصاد ما مایه غبطه جهانیان است. ارتش ما قدرتمندترین ارتش روی زمین است.
فناوری ما بی‌همتاست و ما تقریباً در همه زمینه‌ها پیشتاز هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/72048" target="_blank">📅 18:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72047">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سخنرانی دونالد ترامپ درمجمع عمومی سازمان ملل متحد در نیویورک آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/72047" target="_blank">📅 18:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72046">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دیدم که مراد ویسی گفته احتمال اینکه پزشکیان و عراقچی رو تو آمریکا مثل مادورو دستگیر کنند غیرممکن نیست
آدم می‌مونه به این تحلیلگر چی بگه
😐
🧠
#hjAly‌</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/72046" target="_blank">📅 17:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72045">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59e4ea7a67.mp4?token=HhCBHf0La_5qe5u8uvvIhDSImATilTuID1VoeMTzoWIABZwhjufLav6PQnItobY5J7eEIw6lMnWj-eqSq8fpeXA70kA-TnbLQ-hptMQQdMIsvsXe2PCnHi-SNsjOVdNczgWhaQppvMqasF3b7AremQfcLq8hXMrLcqz5qxKUdhaKR808c51w9UKXXeLXqjKdra77Uq594uK-F1n9tvcz4F13Zc6X7Pf-p_8QCIOT6hVDq010FdxnQC98RQzWwJXLISDUXpIWuLujIB_ynzdv0Rqdrh88jCJGSTeFG-XUnHz7HETJI_bnVPOzNvza72qfDZGQETX1G5oiswbGN2S5-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59e4ea7a67.mp4?token=HhCBHf0La_5qe5u8uvvIhDSImATilTuID1VoeMTzoWIABZwhjufLav6PQnItobY5J7eEIw6lMnWj-eqSq8fpeXA70kA-TnbLQ-hptMQQdMIsvsXe2PCnHi-SNsjOVdNczgWhaQppvMqasF3b7AremQfcLq8hXMrLcqz5qxKUdhaKR808c51w9UKXXeLXqjKdra77Uq594uK-F1n9tvcz4F13Zc6X7Pf-p_8QCIOT6hVDq010FdxnQC98RQzWwJXLISDUXpIWuLujIB_ynzdv0Rqdrh88jCJGSTeFG-XUnHz7HETJI_bnVPOzNvza72qfDZGQETX1G5oiswbGN2S5-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:پیامی که می‌خواهید به پوتین منتقل کنید، چیست؟
ترامپ: این جنگ را متوقف کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72045" target="_blank">📅 17:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72044">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7aa5b4a7d.mp4?token=ukTNtU5jSDBPvr504Tw3exKaF5c97K4BQbIsonquDVuYFvbJpJs0_fZ4Mg3VK3Yyx4vVHlDcvulzwesxoIr2JxhXH7PKHkVd6rv-FhOYLyHTKAn8QtTe4llxF8bUgvOakseegj8gp5epTnf38CB5RjSkGynZ6XW1T8zh7D086h9n4PdvtFokGt0vV0JHsE0CkPS1-2I8ucBRz617RXDc6paNMKFo8qz_0GW7HdexV0BSqBtM5xfe_XeNg_62yyrh3ev7Gan3pCN1j5UM7-4qVx-8MYF0hQqb2lQYYcK1sBnnNSy5Ya8kPBo9pi52A1IUgaRu-OdCCHMzKFJkpDJv4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7aa5b4a7d.mp4?token=ukTNtU5jSDBPvr504Tw3exKaF5c97K4BQbIsonquDVuYFvbJpJs0_fZ4Mg3VK3Yyx4vVHlDcvulzwesxoIr2JxhXH7PKHkVd6rv-FhOYLyHTKAn8QtTe4llxF8bUgvOakseegj8gp5epTnf38CB5RjSkGynZ6XW1T8zh7D086h9n4PdvtFokGt0vV0JHsE0CkPS1-2I8ucBRz617RXDc6paNMKFo8qz_0GW7HdexV0BSqBtM5xfe_XeNg_62yyrh3ev7Gan3pCN1j5UM7-4qVx-8MYF0hQqb2lQYYcK1sBnnNSy5Ya8kPBo9pi52A1IUgaRu-OdCCHMzKFJkpDJv4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ هنگام ورود به مجمع عمومی سازمان ملل خطاب به سی‌ان‌ان:
تعجب می‌کنم که سی‌ان‌ان اینجاست تا اخبار مربوط به مرا پوشش دهد. شما نباید اینجا باشید.
شما گفته بودید که قرار نیست اخبار مرا پوشش دهید. نباید مرا پوشش دهید.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/72044" target="_blank">📅 17:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72043">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72043" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/72043" target="_blank">📅 17:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72042">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7UVpItpBXk1FKasBYsBxEmMUAqUltfERQWPveBZtvOf3_9MJz_XENbp-tA0SeSyVTqaR57CrnZuyKgr1jnkcsLQd9PXA1HrxJ82IR-60zdq4qM5T9NioZUHzky-C-uGZETX2t3JCjVgDyE9n1-CwVEj49VJSX8_T6hbeAnNKkTdUETTj9pL54E1QP4iBRDquoDe-zq47wSN8mj7jvF1l41ht9Zw29kX9V5FJ5HLVVmbyCOL8cl1cC6AJnY6fLo4rq4vpDouHzMBu2s4BdKIRGxspM_Y7XqYF-aRkL5TVGltmV4fN8S2o3fjHgDPWMKL-4NFPy7qMWpOD0edZY6A7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مسابقات
UFC Fight Night
شروع شد!
🦖
یک شب پر از مبارزات هیجان‌انگیز، رقابت‌های نزدیک و لحظه‌هایی که نتیجه می‌تونه در چند ثانیه تغییر کنه.
مبارزات رو زنده دنبال کن، عملکرد فایترها رو بررسی کن و پیش‌بینی خودت رو در
TrexBet
ثبت کن.
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/72042" target="_blank">📅 17:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72041">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a05f244ea4.mp4?token=Cko0xC1dyG_MgBRI9xkmqoCujJg9UFPCVxGywOUYaXuh4QVcLIBhNv403wRw8OpMnIJIobGtIFUS_XcZpc02pi7A3SwWx3ePxuqJ-EFc4XKQF1CH2W9NNr7jPLTGD3iCGB944NxyuXz5vpusm6qqfZ3P5e_-fmxEv6pO0TSp509zVQNaYG8XvsYs96k7UUjgdvTVS_rWFICe3PGhxSuNp-gtvL38ImN-72QAG7Sd_PzrZdk_a0uahl2rTRJGiIUJwlQasH33Hq_drNBXAy6MZXH3ciDb5Hnax166FlQLChDFRwHbIrZ3QU_gUI9ufy7vZ4SFdyjMoDrlKdhlG-6nmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a05f244ea4.mp4?token=Cko0xC1dyG_MgBRI9xkmqoCujJg9UFPCVxGywOUYaXuh4QVcLIBhNv403wRw8OpMnIJIobGtIFUS_XcZpc02pi7A3SwWx3ePxuqJ-EFc4XKQF1CH2W9NNr7jPLTGD3iCGB944NxyuXz5vpusm6qqfZ3P5e_-fmxEv6pO0TSp509zVQNaYG8XvsYs96k7UUjgdvTVS_rWFICe3PGhxSuNp-gtvL38ImN-72QAG7Sd_PzrZdk_a0uahl2rTRJGiIUJwlQasH33Hq_drNBXAy6MZXH3ciDb5Hnax166FlQLChDFRwHbIrZ3QU_gUI9ufy7vZ4SFdyjMoDrlKdhlG-6nmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختره چندین دوس پسر داشته ده ها بار باهاشون رابطه ی جنسی داشته حالا اومده پیش متخصص زنان تا گواهی بگیره به نامزدش نشون بده پردش ارتجاعی بوده و سر اون پسر بیچاره کلاه بذاره.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/72041" target="_blank">📅 17:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72040">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/396f2961ce.mp4?token=keG8D3JNddqV-6OLf9XtaDFATvlHc3E0_Zt5jXifZnNIW42lITMHWbx2H722EX0Rlb70K9a9nOfjhEL-J5msojntKwGV8oDNX8CtJaEH2a8X0HOi4rybCN-kzXQ-j76xoiBNNsBc-J0tdU94rGsFJxI34llFbq6N7n29w_xaO7AVTjNFCtYO8dPZkSoiytBEipNtqBECxnznZz5hFFq0TX5V5OrHXKbfl7sbqW2xF0ySOUO5yiMTXy3NSm6RqAzJ0p0PCZgud_Ptnc-d006F86be1zKN3xNZux9XLEAzovb9JBHOWi7KOxkqYxr-8qc8U9LiS-Xt6B__Lgeb4_XJpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/396f2961ce.mp4?token=keG8D3JNddqV-6OLf9XtaDFATvlHc3E0_Zt5jXifZnNIW42lITMHWbx2H722EX0Rlb70K9a9nOfjhEL-J5msojntKwGV8oDNX8CtJaEH2a8X0HOi4rybCN-kzXQ-j76xoiBNNsBc-J0tdU94rGsFJxI34llFbq6N7n29w_xaO7AVTjNFCtYO8dPZkSoiytBEipNtqBECxnznZz5hFFq0TX5V5OrHXKbfl7sbqW2xF0ySOUO5yiMTXy3NSm6RqAzJ0p0PCZgud_Ptnc-d006F86be1zKN3xNZux9XLEAzovb9JBHOWi7KOxkqYxr-8qc8U9LiS-Xt6B__Lgeb4_XJpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جان کیریاکو تحلیلگر و افسر سابق سیا؛
اسرائیل با پرداخت مبالغی در حدود ۱۰۰ دلار، هزاران شهروند افغان را در ایران برای فعالیت‌های جاسوسی به خدمت گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/72040" target="_blank">📅 17:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72039">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تو نمایشگاه خودروی تهران که تازگی تموم شد، تنها کاری که مردم نکردن بازدید از خودروها بوده ؛
جکِ ماشین رو برداشتن، با خودکار رو کاور ماشین کشیدن، با مشت زدن رو کاپوت G700، کارت استارت ولوو رو بردن، شید سقف ماشین رو خراب کردن، خار دستگیره در رو گاییدن، دوربین جلوی ماشین رو کندن، جکِ کاپوت رو کندن، با خودکار رو صندلی ماشین خط انداختن، دکمه صندلی رو شکوندن...
‌
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72039" target="_blank">📅 16:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72038">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1637ed0d1b.mp4?token=Bb_1TAgRQyM2IAVw35qgOjdCYdpLPQm0rismVgrqyMnmciwHke-d3msoV2sk61nPWl0AqjVP--6GYTRUsohqZvoKZmi6kRGTE_IiTwvAtgH3V_tSXwsCLyNMsKEroizVZ1Ff8j8UJm_1Ina83o8aGFrQknJCAODFpxkrO5P6iY3Lpue33vmH32-ygy0DpPhIFDWreOtr7D7CozaZr---cEJzeqhJVJ8srIXRIQnIqHgwxLzErupdmcfi0NYjgnlRNHCaWLCBs7PtgvTzagUgktqf9oNnxmI48xN1bOKGvWrSoM07Sn9-glMk3TiooecJw1l0LH4uDPxDmtj71eoe3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1637ed0d1b.mp4?token=Bb_1TAgRQyM2IAVw35qgOjdCYdpLPQm0rismVgrqyMnmciwHke-d3msoV2sk61nPWl0AqjVP--6GYTRUsohqZvoKZmi6kRGTE_IiTwvAtgH3V_tSXwsCLyNMsKEroizVZ1Ff8j8UJm_1Ina83o8aGFrQknJCAODFpxkrO5P6iY3Lpue33vmH32-ygy0DpPhIFDWreOtr7D7CozaZr---cEJzeqhJVJ8srIXRIQnIqHgwxLzErupdmcfi0NYjgnlRNHCaWLCBs7PtgvTzagUgktqf9oNnxmI48xN1bOKGvWrSoM07Sn9-glMk3TiooecJw1l0LH4uDPxDmtj71eoe3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل:
پیش از سخنرانی رئیس‌جمهور ایران در سازمان ملل، کانال‌های رسانه‌ای سپاه پاسداران ویدئویی مفهومی و ساخته‌شده با هوش مصنوعی منتشر کرده‌اند که تصویری از نخستین آزمایش واقعی (انفجاری) بمب هسته‌ای ایران را به نمایش می‌گذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72038" target="_blank">📅 15:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72037">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3d6eda575.mp4?token=gJmM51LNDbPnoqi4rUIwoDqtqHTSVeILnwkrVtKB7tw_uUKvAWUYf1fksWxq-55_qM_3sT1bEYYzXcF3EBuzgcxDXzPa7AuZeoPTSKrF6cJ0SmJDv3P24o3ZdTyMdLCOdmCs29QnkdsEGKrqX3RS2iO2z86Ul6WFguGRP-_hZFIZUQLtMRacVEMfHjsEyR1dIQWKdzX3NVxTQgqyqVuzWde83QJ21t9FyTL-TxAZpezj6cCKBIdOKTOj-LtXIihfzMx3iLEhx8YQznxxAuaGZ6BXeAy8lttYdEVynLbUIv-YY5dyi10_b2piQDLJzeuCyiIjj9AD6QNmnI5SQfhuJKpXpzBzTqwB1QTElmY0Fz85si1z1fvomDzjx4fqwuevkrdgj2rjrZBfPVrj_O6G0VJ1_ZdAto_ixyw0JuP2ljCbjjsk8pFkMnSpEgiWREgfcrtC6hRm8kHpuPIE2drN3zy3_LUANkgW8sv5zXOdRdT5e2QAv5IrKOIYkHlrbmDIZ_AFnIpNtlNb2NoJRhWFGgOHc9mU7wA5noa63JWllADV87gJzCJhxTeuSs70uGuVU8Jud8k-UTWFJaFW8CJyCPFab-7XOCopEapuuHVHK744bl8K5fzs9A7mffRp-UEpg966YvbB7yJtByVxj5xW68DEij21pHJTq2FrLsoNXe4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3d6eda575.mp4?token=gJmM51LNDbPnoqi4rUIwoDqtqHTSVeILnwkrVtKB7tw_uUKvAWUYf1fksWxq-55_qM_3sT1bEYYzXcF3EBuzgcxDXzPa7AuZeoPTSKrF6cJ0SmJDv3P24o3ZdTyMdLCOdmCs29QnkdsEGKrqX3RS2iO2z86Ul6WFguGRP-_hZFIZUQLtMRacVEMfHjsEyR1dIQWKdzX3NVxTQgqyqVuzWde83QJ21t9FyTL-TxAZpezj6cCKBIdOKTOj-LtXIihfzMx3iLEhx8YQznxxAuaGZ6BXeAy8lttYdEVynLbUIv-YY5dyi10_b2piQDLJzeuCyiIjj9AD6QNmnI5SQfhuJKpXpzBzTqwB1QTElmY0Fz85si1z1fvomDzjx4fqwuevkrdgj2rjrZBfPVrj_O6G0VJ1_ZdAto_ixyw0JuP2ljCbjjsk8pFkMnSpEgiWREgfcrtC6hRm8kHpuPIE2drN3zy3_LUANkgW8sv5zXOdRdT5e2QAv5IrKOIYkHlrbmDIZ_AFnIpNtlNb2NoJRhWFGgOHc9mU7wA5noa63JWllADV87gJzCJhxTeuSs70uGuVU8Jud8k-UTWFJaFW8CJyCPFab-7XOCopEapuuHVHK744bl8K5fzs9A7mffRp-UEpg966YvbB7yJtByVxj5xW68DEij21pHJTq2FrLsoNXe4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه، درباره ایران:
رئیس‌جمهور ترامپ برای دیدار با پزشکیان یا هر کس دیگری آمادگی دارد.
اما اینکه آیا نتیجه سازنده‌ای از آن حاصل خواهد شد یا خیر، دشوار می‌توان گفت؛ زیرا تصمیم‌گیرنده نهایی در ایران، «رهبر عالی» است و رهبر عالی، یک روحانی شیعه تندرو است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72037" target="_blank">📅 15:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72036">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70ab0515ff.mp4?token=ULIAqaNTPJEOyxHBqyqYv63ZAMYn4WW9ambR3mxYM_QHnflH0knCM2Ja81ET-oGSPMzclSYfcC2UWbOQymS_ew-9IRhbcA0goQKPSVzmHsG5ivIdXI636NIQG2fAw8Xs-h7DqOSyuqSx3JPEX9MlRfRI-xZTvzbcnzO5QNIbBmH9onHtC215JRVlnM3hg_wz2jSrcCRXGd0ifXeWFjlXkof-8Q6ZmkLj93zI2A4uCdvHyq6lIN04SPoM_4DTUxVbPkWviagILPaWQ3Kp0PaKh-aN1yNxXg6a-w7eiHufc_-JPloGc44DQ06z1Rq7OyHKZaTvVnqPVOXh8j6AZl7yqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70ab0515ff.mp4?token=ULIAqaNTPJEOyxHBqyqYv63ZAMYn4WW9ambR3mxYM_QHnflH0knCM2Ja81ET-oGSPMzclSYfcC2UWbOQymS_ew-9IRhbcA0goQKPSVzmHsG5ivIdXI636NIQG2fAw8Xs-h7DqOSyuqSx3JPEX9MlRfRI-xZTvzbcnzO5QNIbBmH9onHtC215JRVlnM3hg_wz2jSrcCRXGd0ifXeWFjlXkof-8Q6ZmkLj93zI2A4uCdvHyq6lIN04SPoM_4DTUxVbPkWviagILPaWQ3Kp0PaKh-aN1yNxXg6a-w7eiHufc_-JPloGc44DQ06z1Rq7OyHKZaTvVnqPVOXh8j6AZl7yqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران:
مسئله اصلی این است که ایران توسط روحانیونی دیوانه اداره می‌شود که دیدگاهی بسیار افراطی و آخرالزمانی نسبت به دین خود دارند.
این افراد هرگز نباید به سلاح هسته‌ای دست یابند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72036" target="_blank">📅 15:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72035">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeeb195e4e.mp4?token=EM8229Sn_D-w7B0HN3lZcb6d9bMSED6Gs6LwH-6dhf9XWshRdumpwc3Uw0M82VSlj2jtlIzgVt9A98nfgRJAmcj8c9Z9f5FGxTzqZcsw2pLf3sZcxvjwSa_FzNLD9cF5HXSqxRdhRXvkBXEISJMyXLovG6Htn1-buKoXUkUphQmWZTyOzrN5cl0yjq1WRBviP_gIyDdwi3v1BYsvtoIE4YPioBFn0s_4HMRAKaKZ-73u6aVmtqvQ7iZk3Lebqaxo-vKKTdDN7AUBLMBtuRKI21roTSbaYeKJ9xBT2qRYApQa2SiJVdDqIFBggOwpooNjJeirG8M3yAcn7bnyHCX_OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeeb195e4e.mp4?token=EM8229Sn_D-w7B0HN3lZcb6d9bMSED6Gs6LwH-6dhf9XWshRdumpwc3Uw0M82VSlj2jtlIzgVt9A98nfgRJAmcj8c9Z9f5FGxTzqZcsw2pLf3sZcxvjwSa_FzNLD9cF5HXSqxRdhRXvkBXEISJMyXLovG6Htn1-buKoXUkUphQmWZTyOzrN5cl0yjq1WRBviP_gIyDdwi3v1BYsvtoIE4YPioBFn0s_4HMRAKaKZ-73u6aVmtqvQ7iZk3Lebqaxo-vKKTdDN7AUBLMBtuRKI21roTSbaYeKJ9xBT2qRYApQa2SiJVdDqIFBggOwpooNjJeirG8M3yAcn7bnyHCX_OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
ترامپ برای دیدار با هر کسی در سازمان ملل آمادگی دارد.
ما نیز برای دیدار با پزشکیان آمادگی داریم.
گمان نمی‌کنم در حال حاضر برنامه‌ای برای آن تنظیم شده باشد، اما قطعاً از چنین دیداری استقبال می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72035" target="_blank">📅 14:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72034">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">شرکت‌های هواپیمایی «ترکیش ایرلاینز»، «پگاسوس» و «اِی‌جت» (AJet) تمامی پروازهای خود به مقصد ایران را از تاریخ ۲۱ سپتامبر لغو کرده‌اند و امکان رزرو بلیت نیز حداقل تا مارس ۲۰۲۷ وجود ندارد.
تحریم‌های ایالات متحده موسوم به «عملیات طرد اقتصادی» (Operation Economic Outcast) دامنه‌ی گسترده‌ای دارند و حتی هواپیماهای ایرباسِ دارای قطعات ساخت آمریکا را نیز شامل می‌شوند؛ موضوعی که شرکت‌های هواپیمایی ترکیه را ناچار به توقف این مسیرهای پروازی کرده است.
شرکت هواپیمایی «ماهان» نیز پروازهای خود به استانبول و آنکارا را به حالت تعلیق درآورده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72034" target="_blank">📅 14:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72033">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhUIwWcj1-9kRhUXCQb_WtaQoTwSiWIOW2yDY7tbneJj8j6SLnWMe3Ug81CShEMc03p5VeSujBIsst1QdOB_GXtCLI43JPy6OfB41c1XXvqPZWcNoK6lxVp1PCzpl6SypjN3vUu2dmwT3-_VLy6FVJlbKhiv8ivDmBFG_xwk7-5_w9RAU_RzZEY3zI9UXkIySjTs_pzbWbpeWHqAuwhxooXZYKKnDB-e3rKc_z7J1YNQfAbUMglEvPfgarnak6c14HO4parKih3KN1sWyhgEbIW2DAGsam_Y8WCnVKtb-r8h7ULcOSdpLJvOIMBrywm3NPWtlpWoVr1yvFo44bwq2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری ژاپنی «کیودو» و به نقل از یک مقام ایرانی که نامش فاش نشده است، ایران پیشنهاد کرده است که در صورت برداشتن گام‌های اولیه از سوی ایالات متحده برای کاهش فشارهای نظامی، تنگه هرمز را ظرف هفت روز بازگشایی کند.
این پیشنهاد که گفته می‌شود از طریق واسطه‌ها به واشنگتن ارسال شده، خواستار ازسرگیری مذاکرات با هدف پایان دائمی خصومت‌هاست.
این مقام ایرانی اظهار داشت که دستیابی به توافق همچنان امکان‌پذیر است، اما احتمال دیدار میان ترامپ و پزشکیان در حاشیه مجمع عمومی سازمان ملل را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72033" target="_blank">📅 14:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72032">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uh6Qo3TiKCyUsioapFoXdp9iFhg03Pqehv2gt1LQIpMGCGXNjhK2dW4O2fj0NK96Sg0DUZfyKNjyojiwEqG0nANg9TuEBmqQtk8Zl_ee6Gp0hKhovL6zPKFfTXC9HuFOjzmMe3z-ZrT2orhiP-HwkIqwElXrcvmLLIzA862nTMMOwQgsEjgw1TqLKPp94kaIz7SYMq9f9401YHcrKkRrFarLo9W75eRWg1VX_ZjiI-yq2kjk80FfxK2rKQWS8GEPITQMD4gzd1eJHVFgD54YpFr93O7R4cMpmnNiCbRIVd1QrIXWC0FnWDiSO-nmHkmeF8dT8nOkg6aop-WAD1pHlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان صبح امروز برای حضور در هشتادویکمین مجمع عمومی سازمان ملل متحد، تهران را به مقصد نیویورک ترک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72032" target="_blank">📅 12:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72031">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3534317cc.mp4?token=HFyM_tMXBhWLU8r2D6Sotp0Pza8mCCAa5mKFzdpmNWkEURDWW9uanLfpAv55Aqg3GNDuBwbbhhLaFjUaKnzJCzM6THZOT_DChu3sU8HOeI5JBocTzpUOwB_rRsMOVm1U7tbd1hj_IcJ_S95A4bFRGRtgPmtbz2cCk3f6fWfHt1Hhye2vVf3h20zUeqbi7-6SFWHjtTVo2zHEQ-Bm15M6X2nh-dggPiyjbH_nHmRdEcT8g7rQuqsy3gOJA4fUmS_BfIj-6o2wId2PxC0slIW4N3qBpuaqyaBxOVMy35e23ikWWfBPggYApsRpJAEA_-Pf4wTnklhd8dyj-a2-LLTntw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3534317cc.mp4?token=HFyM_tMXBhWLU8r2D6Sotp0Pza8mCCAa5mKFzdpmNWkEURDWW9uanLfpAv55Aqg3GNDuBwbbhhLaFjUaKnzJCzM6THZOT_DChu3sU8HOeI5JBocTzpUOwB_rRsMOVm1U7tbd1hj_IcJ_S95A4bFRGRtgPmtbz2cCk3f6fWfHt1Hhye2vVf3h20zUeqbi7-6SFWHjtTVo2zHEQ-Bm15M6X2nh-dggPiyjbH_nHmRdEcT8g7rQuqsy3gOJA4fUmS_BfIj-6o2wId2PxC0slIW4N3qBpuaqyaBxOVMy35e23ikWWfBPggYApsRpJAEA_-Pf4wTnklhd8dyj-a2-LLTntw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت عجیب سربازان روس که به بالای دکل ها رفتند تا با استفاده از سامانه های پدافندی دوش‌پرتاب(MANPADS)با پهباد های اوکراینی مقابله کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72031" target="_blank">📅 12:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72030">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72030" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72030" target="_blank">📅 12:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72029">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdhMCkPcuwWHZY2GK0HjklNvEGIH6Hx9X7PPgC5tUV83mfbBXfbLLkLSxatS0_OmWyWC87RZtTBQGVYHRgCDWwrwaWt7upxnsF4qKDaqm_6PwYbzW4Fy9jVKs3VeTDeJa6GCSblpr8txWAKjKI7yF19f3IOBlCDVSk6LAPywlsPUVzsdk4zOFYfj7QL22XHsU-1UNWiKn0fFANQvv0LMEtzrq2C5Rb1MDdXAc2iwWbQstY6v6auSAD_Zznp-DW1ALovhXmjwJQemBjHRWSahg2MTHjdRHSas9HLNjmiphzYK_W8HlAp1qs5ENhAIYKHIFxS-J_KMLzujeBIDwrEMQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72029" target="_blank">📅 12:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72028">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prDbO6y99cWLuTlYX56s4lJ2fPfS9NT8Y389YPlMX8IkEcpoZ0inS-sTNKHPLPwdQkomgq86p1fJ0sltsFCqbTbnNLeSp-bJO4SiuAq1X1uXgOqi9yn_lHleN-5cL8Q9ZOG1IwNgnThm0KcgV1F3cm9cDcUSb6jt778NBoA4k1Wq5eDyfONdFKMBb48WSKphSv6ytUzV74koUqsMM8N6sQXKyHbS1a8-YvxOjT_q0yc6rSNaEhkOjAxckQF7-x9fNhdKao7qshYFcOv8Crycx7WZR6bRWwBr_FVMXwfizeyA1Lc3iQcB-P6pLZzdtndF3PCsPKm_UHnW9QDHm4p4gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندی برنهام، نخست وزیر، گفت که بریتانیا پس از حملات پهپادی و موشکی حوثی‌ها، پشتیبانی «سوخت‌رسانی هوایی دفاعی» را در اختیار عربستان سعودی قرار خواهد داد.
این پشتیبانی که انتظار می‌رود در روزهای آینده آغاز شود، شامل یک فروند هواپیمای نیروی هوایی سلطنتی وویجر مستقر در پایگاه نیروی هوایی سلطنتی آکروتیری در قبرس خواهد بود.
مقامات بریتانیا گفتند که این استقرار «محدود به زمان» خواهد بود و احتمالاً «برای چند هفته» ادامه خواهد داشت.
برنهام گفت که این اقدام به دنبال درخواست عربستان سعودی برای «حمایت نظامی» و با هدف حفاظت از ثبات منطقه‌ای و منافع بریتانیا انجام شده است.
«عربستان سعودی حملاتی را تجربه کرده است، به دنبال اختلالات احتمالی بیشتر است و ما باید این مسیرها را باز نگه داریم و از این رو با این درخواست موافقت می‌کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72028" target="_blank">📅 12:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72027">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e88d60053.mp4?token=l2iru8ubXJqgWsoT2vLXO1c23LO6iaNA2mFrxZvSa6omshkRi0RqoFM--LQFp0-3DREoOwKbgwzfAxlaknl89F-V841qBn2Gm_kWLiAq9NmLpzyaHnjbz9VIBTP1j8u5gSExUDRVU8bKluMo_QNLxP_bg0NF1Fgo__UbCVmntUkrlNRAm7WyLA3f03UvYp0d25fNtU-lMAgskmkqCN9F-2hHNjA2SePlK2wYe62x4lH0Qpg-sFuNy_8D9hTt528WxCN2hTJIXC4o44qJGSjl-j9P-IlRgivZj9DfT0ZD5WgOv-yWJRZnNpqBRjumYJmCK3lEzcW_3UOKerbqjL_qLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e88d60053.mp4?token=l2iru8ubXJqgWsoT2vLXO1c23LO6iaNA2mFrxZvSa6omshkRi0RqoFM--LQFp0-3DREoOwKbgwzfAxlaknl89F-V841qBn2Gm_kWLiAq9NmLpzyaHnjbz9VIBTP1j8u5gSExUDRVU8bKluMo_QNLxP_bg0NF1Fgo__UbCVmntUkrlNRAm7WyLA3f03UvYp0d25fNtU-lMAgskmkqCN9F-2hHNjA2SePlK2wYe62x4lH0Qpg-sFuNy_8D9hTt528WxCN2hTJIXC4o44qJGSjl-j9P-IlRgivZj9DfT0ZD5WgOv-yWJRZnNpqBRjumYJmCK3lEzcW_3UOKerbqjL_qLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو صحبت کردن این پسر با یه پشه که تو اینستا خیلی وایرال شده
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72027" target="_blank">📅 11:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72026">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/72b152b531.mp4?token=hVwy0Y6a9DvcBfinl0kach48d0iY_MhBOMTf41EgGEdIPgH4F6a-ZScgp-9qiEJ6fyg-qfz6uz3ZIRrJTKeYFjIsD_fOnhBA61ZC9ff-nKb0dFB-_Jny2z7SCVFYWdRbW2HGpW1pY8aJqrcNgMdTCNVB9JTGvPgn_wWhlyTe1NQPVVc_9D4LiOgzmalmw-zWDEdTM-SQYGziy8KLv0f28aGhZG73bKYRpTZsVQmfuoC1ZBI37Vc049C302hwXnYPUqWwVE4LsOrX9y_WSeHWsl4Za5dhStw0g0-VRkvRuM7s8qJpreDUqIUSm9qNuPwORNfkyuhzKE-f1YXv3xA-Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/72b152b531.mp4?token=hVwy0Y6a9DvcBfinl0kach48d0iY_MhBOMTf41EgGEdIPgH4F6a-ZScgp-9qiEJ6fyg-qfz6uz3ZIRrJTKeYFjIsD_fOnhBA61ZC9ff-nKb0dFB-_Jny2z7SCVFYWdRbW2HGpW1pY8aJqrcNgMdTCNVB9JTGvPgn_wWhlyTe1NQPVVc_9D4LiOgzmalmw-zWDEdTM-SQYGziy8KLv0f28aGhZG73bKYRpTZsVQmfuoC1ZBI37Vc049C302hwXnYPUqWwVE4LsOrX9y_WSeHWsl4Za5dhStw0g0-VRkvRuM7s8qJpreDUqIUSm9qNuPwORNfkyuhzKE-f1YXv3xA-Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی عظیم در دنیپروپتروفسک؛ صحنه‌ای آخرالزمانی؛
پیش‌تر، وزارت دفاع روسیه اعلام کرده بود که نیروهای مسلح اوکراین از تأسیسات غیرنظامی برای اهداف نظامی استفاده می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72026" target="_blank">📅 11:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72025">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6404ec7a8.mp4?token=ptlyTBsUI0AcVEnnBjkbGmk-TCjzu2Mhi96xb2nr7abdnSCyr1cdWIRKf1ninkn32IX_1pXISliIfntY0Uyk1CYLI7MGfFTggCQeGpck76p0zKqBNBkdRn_M4dwDRBt6wW1vswQ_CypyehCRj5x_iOw_S0cmcw9gAsyoBYQV20GrCAVxkHisj2CSXgYKfy8KxNM5LD6-o9JxKEr3hsamngDE8W9gZ6_QPxjPCKjzdHDEsxYm_5RmySvHpSEtKRXXwimnp9heP-PlRfExlxlI8Jo-w3k_kZIKGZXMDti8Xv6yLF3FNCymQZwLqvMK82dBDlANWUNSqvot_giyff36iiov7glLAAQZIkygpPCL3DU6FWmE39Jx8mw8tX76eO-qK_TJwKdIehjZaLGUNcv_aT8GQQZoUFDMVV3fl5pQeKuTBADKI_4NmGU7SGCmYULY5fNh_-p8bBivTNTa5KUb78QUVpKHZ17QSFE9X2xZmccJ7fmI_d_foueJA8jHeYjZ4033Hr_rEjsVSA1pxG7sFumjGrNZA0mz09a6GBlwKEGgTeVnVviBvGfAj6KxWat0B19MGSPzzhljOCnvDm4d4y3bAB18qgWJQMWaOYNvvBQWivtyGsPlcWI79dwjqUoZdrwnIBkdPtIhWzTP_WMWDVDW6r_WrZUqLHXookdiWWI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6404ec7a8.mp4?token=ptlyTBsUI0AcVEnnBjkbGmk-TCjzu2Mhi96xb2nr7abdnSCyr1cdWIRKf1ninkn32IX_1pXISliIfntY0Uyk1CYLI7MGfFTggCQeGpck76p0zKqBNBkdRn_M4dwDRBt6wW1vswQ_CypyehCRj5x_iOw_S0cmcw9gAsyoBYQV20GrCAVxkHisj2CSXgYKfy8KxNM5LD6-o9JxKEr3hsamngDE8W9gZ6_QPxjPCKjzdHDEsxYm_5RmySvHpSEtKRXXwimnp9heP-PlRfExlxlI8Jo-w3k_kZIKGZXMDti8Xv6yLF3FNCymQZwLqvMK82dBDlANWUNSqvot_giyff36iiov7glLAAQZIkygpPCL3DU6FWmE39Jx8mw8tX76eO-qK_TJwKdIehjZaLGUNcv_aT8GQQZoUFDMVV3fl5pQeKuTBADKI_4NmGU7SGCmYULY5fNh_-p8bBivTNTa5KUb78QUVpKHZ17QSFE9X2xZmccJ7fmI_d_foueJA8jHeYjZ4033Hr_rEjsVSA1pxG7sFumjGrNZA0mz09a6GBlwKEGgTeVnVviBvGfAj6KxWat0B19MGSPzzhljOCnvDm4d4y3bAB18qgWJQMWaOYNvvBQWivtyGsPlcWI79dwjqUoZdrwnIBkdPtIhWzTP_WMWDVDW6r_WrZUqLHXookdiWWI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این اخوند توضیح میده چقدر رژیم جمهوری  اسلامی پول خرج اینا میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72025" target="_blank">📅 10:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72024">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d71cb9ab.mp4?token=nHETzDvBkkE4l8IQI-JY1Mes3sdBNrQB7vZz8r5kp1VkqmYiuihAhK0GOQ_NwJK5bZ1KMw9yOnTsnFuczrYq1U2P7il5wfzmdWlX0WOqCyIKPg2T0llrBwyqUrhFGldurGCaikDIOUptJRQ660-9bL3XiUDAJZiZM07G_wLcHW4jymamsYhHNjJwzkpr4INL0pahbMLJH9WKJXzbTV9Gt8r35ba8iht-MdPPw3qERFHvD89wmesqj0OzHDj42CtezrTGiLWAW_br73X62MCdcJm3R0Ao-KDyFyabSlgDEY9YndBQZyZNSA7-r2o4uOgC_PfBZX8a5H2vaUW8mGc19g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d71cb9ab.mp4?token=nHETzDvBkkE4l8IQI-JY1Mes3sdBNrQB7vZz8r5kp1VkqmYiuihAhK0GOQ_NwJK5bZ1KMw9yOnTsnFuczrYq1U2P7il5wfzmdWlX0WOqCyIKPg2T0llrBwyqUrhFGldurGCaikDIOUptJRQ660-9bL3XiUDAJZiZM07G_wLcHW4jymamsYhHNjJwzkpr4INL0pahbMLJH9WKJXzbTV9Gt8r35ba8iht-MdPPw3qERFHvD89wmesqj0OzHDj42CtezrTGiLWAW_br73X62MCdcJm3R0Ao-KDyFyabSlgDEY9YndBQZyZNSA7-r2o4uOgC_PfBZX8a5H2vaUW8mGc19g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سال گذشته مردی در حال قدم‌زدن با سگش در کامچاتکای روسیه بود که متوجه نزدیک شدن سونامی شد و با تلفن همراهش از آن فیلم گرفت.  لحظه‌ای هولناک و در عین حال شگفت‌انگیز از قدرت طبیعت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72024" target="_blank">📅 10:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72023">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpoKoTyiXv0jcXKCIR3c4SP59_tvW4k-08R4NZYxvGuMluVENjPmUSG_2Axy7l7jUBORdIjms4nKknnJcXugnyURgLfYMRLensF_Ea1J9oWaYIVMcmv6ab8EBtOxnyAf3G-nAa-9QP1-Pc8jp9sN5LxBfZJnRzYhrhiTFlaHNdKsKIssOtbnTGRcwX4JE0U8JDIuo1-u7P9PXyk3_OBiHCkrDPiyJYCdHMmSPZkDxg8NeG_P4-UGMQk-MVzOk9EcW-Eapb3uCUqq25GuNMKzHeMgte8j5LbnuBQjzQTrLTVq_j5dvlQW-o9N8tuhGjw_dcMvnT9VF1mlc9CuTNxI1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در پی درخواست مجدد عربستان سعودی برای اقدام نظامی، در تعطیلات آخر هفته احتمال صدور فرمان حمله به حوثی‌ها (انصارالله) در یمن را بررسی کرد، اما در نهایت تصمیم گرفت از انجام آن خودداری کند.
دریاسالار برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، پیش‌تر تمامی گزینه‌های مربوط به حملات هوایی را آماده کرده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72023" target="_blank">📅 09:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72022">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8969619843.mp4?token=aBLa8kf7zl3Ho-0bCk-WwX_KtmqCBZTBwKse1A0q1_BYOJagu_yblRslug-hjKBfM_fQ_ImHbAfelOsALHDngO9kwkpbeLt-cZM224pJ9ik7YUzMAOhUbR-dpV2WpleLfJrQogqlM1mlzNs-fJ6I1PUC4wB0iS1CGpVhfJXXJ-C3ksEwAvB040sQ16dGP7wz4liIS20MhLB6X58kia5QXFJKwpEoGgHhlsm-geyRy3zYt8RsTiUIBlLXO5gVAbYIaXW-EkowBLiT9pdJhX1IgBuHRMSRfKsQ93TvzP1M-OZ2KtwMiGIdUPW7foXGdn8ImkS8EMKpF8tJsyTKco4g_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8969619843.mp4?token=aBLa8kf7zl3Ho-0bCk-WwX_KtmqCBZTBwKse1A0q1_BYOJagu_yblRslug-hjKBfM_fQ_ImHbAfelOsALHDngO9kwkpbeLt-cZM224pJ9ik7YUzMAOhUbR-dpV2WpleLfJrQogqlM1mlzNs-fJ6I1PUC4wB0iS1CGpVhfJXXJ-C3ksEwAvB040sQ16dGP7wz4liIS20MhLB6X58kia5QXFJKwpEoGgHhlsm-geyRy3zYt8RsTiUIBlLXO5gVAbYIaXW-EkowBLiT9pdJhX1IgBuHRMSRfKsQ93TvzP1M-OZ2KtwMiGIdUPW7foXGdn8ImkS8EMKpF8tJsyTKco4g_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود: ‌دونید شماها گوهرید یا نمی‌دونید؟
دخترها : بله می‌دونیم نه نمی‌دونیم
مسعود: می‌دونید من اینجا الان اسمم رئیس‌جمهوره؟
دخترها : بله
مسعود:  می‌دونید من از یه خانواده معمولی به اينجا رسیدم؟
دخترها : بله
مسعود: یجور این مملکت رو درست بکنید هیچ بیگانه ای نتونه بیاد اینجا شماها بخواید میتونین دیگه من تونستم شماها هم میتونید دیگه
خنده های وزیر آموزش پرورش فقط
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72022" target="_blank">📅 09:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72021">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f75dfbec.mp4?token=s4gwPXN5J2kdWKq0ziVF2KrVr50_erbgg1nU62rcmrmpLJPrRKdn2RgCuFjDRVJ02OK-oxiOt_Am83kkNQduL3nfM4S9eJ5LQ_SO_0qcBpNzjKtqByy-gSQQCxxGc5dv_GvO9DdSzJL_N9Wh6DV9GAJ_WbvOU5zpS2zbYA8xxCQr2cD6LfmTQHeoSb2bFI6AkxDAsGtirsWjmEZsKyfntIhlSySyr1HJbvJA9O1bJzymuL7JjTHSgiT-IKeFH7wQyEgqb-tnY-h92ycExMqTaHpM7q-bPITXrLdHF4PldkpK6DmYNbYp-VtsvuH29IEpcTKExnWBbvnVpPd6Q23p0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f75dfbec.mp4?token=s4gwPXN5J2kdWKq0ziVF2KrVr50_erbgg1nU62rcmrmpLJPrRKdn2RgCuFjDRVJ02OK-oxiOt_Am83kkNQduL3nfM4S9eJ5LQ_SO_0qcBpNzjKtqByy-gSQQCxxGc5dv_GvO9DdSzJL_N9Wh6DV9GAJ_WbvOU5zpS2zbYA8xxCQr2cD6LfmTQHeoSb2bFI6AkxDAsGtirsWjmEZsKyfntIhlSySyr1HJbvJA9O1bJzymuL7JjTHSgiT-IKeFH7wQyEgqb-tnY-h92ycExMqTaHpM7q-bPITXrLdHF4PldkpK6DmYNbYp-VtsvuH29IEpcTKExnWBbvnVpPd6Q23p0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ سی‌ان‌ان، ام‌اس‌ناو و پولیتیکو رو به خاطر «فیک‌نیوز» از کاخ سفید ممنوع کرد.
فاکس‌نیوز + ABC، CBS و NBC در اعتراض، پوشش تلویزیونی مشترک (TV Pool) رویدادهای ترامپ رو متوقف کردن.
نتیجه: مراسم‌ها بدون صدای زنده پخش شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72021" target="_blank">📅 07:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72020">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72020" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72020" target="_blank">📅 01:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72019">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbfdXB3DUfGkDaqZnYdrGQ6TnoB3iJVuAx0FJs6hvQhViEqISIwC0LLEpWmULSGwd5md-hYrGtevjE7TvcFM6wzZhfC1a4IptfCpTd5qW-CHzV0AmEQyF5MO4O-exSb-bPVFzn3DJIIfDFTI75v9cB8Z8q68ScHM0fSCcqtx4g3pnA9XrG1CVCtY7p6kq4csjrYc9LoSNe8so_x3YHPrzAOTsoanYZz3sBBdLpTklCOKcX6px_wvcdLCFxvfPsNCwvxMaUvaiwM-b4VaSxwE78NJbhTpCHJzdpZphRYUwn9ZoDRqbot8BUgIMKUuT-qjUsqDZj7leVxUGki1jvKWBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72019" target="_blank">📅 01:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72018">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d99b0ae83d.mp4?token=hoonbJJw9tN4gOHhb6chU097hVajNZA5J34N5tGlW8vnNggrQ6vGgYU9kFPPqTP7pvSzoz29fYLxyVxRE725UHVoq6MBDQy8qNjdZvhGUsSeXM4pbQT2EPvPe5ADIZX9YuwlAk8aHnXJIdB0RrPeOCaWn4YuIRDXK4kOhX3Yghjf8-_g_B25P75xifpjvIMCjYUa9jqQD9i2c2W9Ywi47WENzs2BFR4AtbhhFJDa58xMziCQPI3DvnpQYlURdDwumJn5iE7ttS8-f6Sd6CPxijD4ki6kGEBOKphvCOP7fCS-6NePHx0-1XNyqVO-aFKPB1Xg5F9TOn--9ttYLdrr3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d99b0ae83d.mp4?token=hoonbJJw9tN4gOHhb6chU097hVajNZA5J34N5tGlW8vnNggrQ6vGgYU9kFPPqTP7pvSzoz29fYLxyVxRE725UHVoq6MBDQy8qNjdZvhGUsSeXM4pbQT2EPvPe5ADIZX9YuwlAk8aHnXJIdB0RrPeOCaWn4YuIRDXK4kOhX3Yghjf8-_g_B25P75xifpjvIMCjYUa9jqQD9i2c2W9Ywi47WENzs2BFR4AtbhhFJDa58xMziCQPI3DvnpQYlURdDwumJn5iE7ttS8-f6Sd6CPxijD4ki6kGEBOKphvCOP7fCS-6NePHx0-1XNyqVO-aFKPB1Xg5F9TOn--9ttYLdrr3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، برای شرکت در مجمع عمومی سازمان ملل وارد نیویورک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72018" target="_blank">📅 01:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72017">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e2686a0e6.mp4?token=japXbHE4KBLcRGCm2j7-waFEEMlkR_k6R8zAT5wOQvzIsHkA4LrdXF3QZhtRY235SyXkNb3_vq2U25QK2igifXnmipB4HXq0TMy-Zn-uq7UR-rJbhvbeakNsfJghKbTiHUSX-R3p00EGiv3mr4HQxXqMA1Bn7dz3nH3fb9ojWHyI6NG0Wwmj_upV99xSnL0vzEDnmFB3tGtHJkDY3nKJ5n-jRVRk-wYslLaDmUbAf3-8oZTB-lShNiXCZ70jlONQ4AsdODi_IdVo8cH94RiCx-Uxm1uRLcyuU68Lvs-_s1d1adXzItXz0IQo7pl02iJIN2SEXcspPmVsX3hyfKajdXrR0R8BaWcWAHU_VcuPgb0jBRamQs9m5QiSY0E7kORFiymNqvgX3COVFjDrmdEGlpEumyNiJQ513ToDjr0_nVNrml3mgLgbkm9NaAI8EWzmAvtrgC0Lmy533fT7ls2-XjUo_iIvZrcZSLRQie0LRYpsgxCX7-gX7HG4exf3W8EoBKrB8hB9_oSTbQZszVt-_LkL1EArH_hEOd0YbY0_JE_lLpPmjBH36ujbyCkj7v4IwlpcoZ-AARsJqKVqnM4e3wN2qb1nfbVA2ujKkNlqXnO0GwbJTZ13rTz4ucg356ICnJL8FoIKbaPrRfuGGhbfn_APy1wbwesxUYz2rib9X6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e2686a0e6.mp4?token=japXbHE4KBLcRGCm2j7-waFEEMlkR_k6R8zAT5wOQvzIsHkA4LrdXF3QZhtRY235SyXkNb3_vq2U25QK2igifXnmipB4HXq0TMy-Zn-uq7UR-rJbhvbeakNsfJghKbTiHUSX-R3p00EGiv3mr4HQxXqMA1Bn7dz3nH3fb9ojWHyI6NG0Wwmj_upV99xSnL0vzEDnmFB3tGtHJkDY3nKJ5n-jRVRk-wYslLaDmUbAf3-8oZTB-lShNiXCZ70jlONQ4AsdODi_IdVo8cH94RiCx-Uxm1uRLcyuU68Lvs-_s1d1adXzItXz0IQo7pl02iJIN2SEXcspPmVsX3hyfKajdXrR0R8BaWcWAHU_VcuPgb0jBRamQs9m5QiSY0E7kORFiymNqvgX3COVFjDrmdEGlpEumyNiJQ513ToDjr0_nVNrml3mgLgbkm9NaAI8EWzmAvtrgC0Lmy533fT7ls2-XjUo_iIvZrcZSLRQie0LRYpsgxCX7-gX7HG4exf3W8EoBKrB8hB9_oSTbQZszVt-_LkL1EArH_hEOd0YbY0_JE_lLpPmjBH36ujbyCkj7v4IwlpcoZ-AARsJqKVqnM4e3wN2qb1nfbVA2ujKkNlqXnO0GwbJTZ13rTz4ucg356ICnJL8FoIKbaPrRfuGGhbfn_APy1wbwesxUYz2rib9X6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش خبری فاکس نیوز به نقل از ترامپ:
«در حال تصمیم‌گیری هستم.»
اریک شان، خبرنگار ارشد فاکس‌نیوز، گزارش می‌دهد که دونالد ترامپ، رئیس‌جمهور، در حال بررسی گام بعدی خود در قبال ایران است؛ آن هم در شرایطی که برای دیدار با رهبران کشورهای حوزه خلیج فارس در حاشیه مجمع عمومی سازمان ملل در روز سه‌شنبه آماده می‌شود.
ترامپ در حالی که گزینه‌هایی همچون اقدام نظامی، تداوم فشار اقتصادی یا تلاشی دیگر برای دستیابی به توافق را سبک‌سنگین می‌کند، به فاکس‌نیوز می‌گوید: «سؤال من این است که آیا و چه زمانی کل کشور [ایران] را نابود کنم؟ بهتر است آن‌ها درست رفتار کنند.»
این هشدار هم‌زمان با تشدید تنش‌ها در منطقه مطرح می‌شود. ایران تهدید کرده است که در صورت انجام حملات جدید از سوی واشنگتن، علیه منافع آمریکا دست به تلافی خواهد زد؛ این در حالی است که حوثی‌های مورد حمایت ایران نیز به سمت عربستان سعودی موشک شلیک کرده‌اند.
ترامپ همچنین می‌گوید که برای دیدار با مسعود پزشکیان، رئیس‌جمهور ایران، در هفته جاری آمادگی دارد، اما در حال حاضر هیچ دیداری میان این دو رهبر در برنامه گنجانده نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72017" target="_blank">📅 01:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72016">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612f18036a.mp4?token=p6GSFfogLP3NeenpYagUSLNLCxCf8T9p97GWmxK9pxpgnUi80O13q4Ft5JXFiHdY_jBOjW-Afhej9n_R7-OEDg_-A0nmE5_4cKqIMmahsCUC5jEqt2uwG1t6F8QdLGoDxDny7hYrDW9mg_yu6-cbceLTcacDyK0_fpJvsnGAWLUm0zrM5zdQgUdpntp2hTC2JIjuiuqU_vFxyP44--K0v3uqlfFJ6ZEhBoD5eMyg1v1hcXqNsj_Zqeby8p6qyUKSmZ9ajvMeLBfT-H8JUgTUOfAY2rN203d5D4_E6FfBcuP7oZmKdYuYKLvaB_X_d6tRsBY7HRTC8LM_G943mllEpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612f18036a.mp4?token=p6GSFfogLP3NeenpYagUSLNLCxCf8T9p97GWmxK9pxpgnUi80O13q4Ft5JXFiHdY_jBOjW-Afhej9n_R7-OEDg_-A0nmE5_4cKqIMmahsCUC5jEqt2uwG1t6F8QdLGoDxDny7hYrDW9mg_yu6-cbceLTcacDyK0_fpJvsnGAWLUm0zrM5zdQgUdpntp2hTC2JIjuiuqU_vFxyP44--K0v3uqlfFJ6ZEhBoD5eMyg1v1hcXqNsj_Zqeby8p6qyUKSmZ9ajvMeLBfT-H8JUgTUOfAY2rN203d5D4_E6FfBcuP7oZmKdYuYKLvaB_X_d6tRsBY7HRTC8LM_G943mllEpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ درباره ایران:
وضعیتشان خوب نیست. در واقع، امروز جلساتی در این باره دارم. عملکردشان بسیار ضعیف است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72016" target="_blank">📅 01:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72015">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ti814KJr2mjt2s-QLVkT3_VIvV4z83IDGHyjDU18DtGPuhsr4D1UCBDXJoTCR8_84A_vN-c9Vuqx4EzG09dVoJxeNnbu2g3egJi0HjlWNNqIX6zFwG1r4jEYg3JvS4JjdSQqxDNMs9rBHi8UQG-remcA_NWHq20WGiAPtslzhu4qLahMuudLMYojihnzbHBpcedSbPriJLujiybdP_X4xuc59yftA9_cMMAwzcjlhJLpk6C1rE6NW-ibZqPHYsK3KWqlFdHDxpSSxYZWOSqmMJ-ydTwSsudYwxGZ4zZlZ5nOwk7_OD5IV9wdnbzWWS-IbnWDrrCQqy3Lm9OcnIB-_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امجد طاها، روزنامه‌نگار و تحلیلگر اماراتی، با انتشار پیامی کوتاه نوشت:
«اتفاقی عظیم در راه است؛ حرکتی تاریخی و بی‌سابقه. آماده باشید.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72015" target="_blank">📅 00:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72014">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترکیش ایرلاینز پروازهای ایران را تا مارس ۲۰۲۷ متوقف کرد؛
یک نماینده شرکت هواپیمایی ترکیش ایرلاینز اعلام کرد تمامی پروازهای این شرکت به ایران دست‌کم تا مارس ۲۰۲۷ در برنامه پروازی قرار ندارند.
این شرکت همچنین اعلام کرده بازگشت پروازها پس از این تاریخ نیز تضمین نشده است.
این تصمیم در پی تشدید محدودیت‌ها و فشارهای بین‌المللی بر صنعت هوانوردی ایران اتخاذ شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72014" target="_blank">📅 00:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72013">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxMVGrJDCBtFbPO6nxjNGZfZTrj_S2_KGC4X2xbs2gM0cD4fSaXD2U1_bNfvpN64vPyYVfFHeu9yGT_LOwiGVaNK3CfyrTetepLlyzMPRE9btMstUWij1C4lah3L3gI6dF1OojvIXAcmTj1isolBsdFJ46ImFRzp7psqb4jq9rbJslLMEVNla6Y_-i6XP9CyWYpTURMrlUpUO2iu-haYyPwvffaoNKO5OCEnQRjJC2_9NgDvZQTwosrr0nHb0nDOve5UqN_6W_9PeWEtWIYbLWAfN8yT33YTIe_ByQxnNhGFZCQXas-WuxP3fUl8y-PGEtHPieqL-Aeq0d5YGC2h5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛مقامات استان لوبلین لهستان در پی حمله هوایی جاری روسیه به اوکراین، هشداری مبنی بر احتمال بروز خسارات جانبی صادر کردند.
هوانوردی لهستان در حریم هوایی کشور در حال فعالیت است و وضعیت تحت نظارت قرار دارد. به ساکنان توصیه می‌شود منتظر اطلاعیه‌های بعدی باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72013" target="_blank">📅 00:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72012">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">#فوری
؛حدود ۵۰ دقیقه پیش، هشدارهایی در پی احتمال وجود تهدیدی در حریم هوایی منطقه «کراسلاوا» (Krāslava) در لتونی — که در امتداد مرز با بلاروس و در نزدیکی مرز روسیه واقع شده است — فعال شد.
جنگنده‌های ناتو به منطقه اعزام شدند. هنوز جزئیات بیشتری منتشر نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/72012" target="_blank">📅 00:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72011">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59e699259b.mp4?token=hdmdTH2-cNstkLIJh8Zo7VxVAwaHF0ffEnAHKhXNC1YhMkxJ4vHFF5sM6rU-3zE5gbVZTmUFhb-6OfWYIFZID4-gKzJTkOTzZd4NgjaFNRS6Z5-uJ04BdHVrkwRT8IOIexJ7Vhu9Hjhojn-jYYDu95C77WRuwZvxZ2mbTG3GnE-FHVU4F99O703QyyHb0Rs3eIu0pUATuHHgrX2kDfGn6-QyZjedSrSxbrNh5Uhik2miqxJQxF0J-Sdn7Lh2jDljlGHvUzztiDF8x5meSzZSDVonMMdZFCOO-tOCHbutesvkPqoJNOUEH-hQwWESIOiWcdYbbBg6dHIVi7saHJhZxpMPOBjOt8aGavkNMVhnMTJzwUDIrq62dD5EQSw7Pym5TMeahpUczhJWJ68NQwPc_ayF8VFXL3vnScCAUX9cFyw32mDFSlxK6Yfjx9BntBJV3BNpQe0nFlabTOPFWjdWW2BryqyphnsNOCwmDrrofD0f1mvbvaUDft5pPK4k-ssiDAhntMQpKxPin3f3wy1l2Hs3un3Q1xluzpIT9bGa30xT7w7rl1LdGd8WC7UUavqBb9WUv79P0FuaN3mgq9GnMrQQIb5gVv3Y9nmXx74UScA47MP_p68Q4neSOkagAlltpFmmn3nWxo1lU2kg0JNyGSb7EkATOpJRNJ4qn6ksKtc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59e699259b.mp4?token=hdmdTH2-cNstkLIJh8Zo7VxVAwaHF0ffEnAHKhXNC1YhMkxJ4vHFF5sM6rU-3zE5gbVZTmUFhb-6OfWYIFZID4-gKzJTkOTzZd4NgjaFNRS6Z5-uJ04BdHVrkwRT8IOIexJ7Vhu9Hjhojn-jYYDu95C77WRuwZvxZ2mbTG3GnE-FHVU4F99O703QyyHb0Rs3eIu0pUATuHHgrX2kDfGn6-QyZjedSrSxbrNh5Uhik2miqxJQxF0J-Sdn7Lh2jDljlGHvUzztiDF8x5meSzZSDVonMMdZFCOO-tOCHbutesvkPqoJNOUEH-hQwWESIOiWcdYbbBg6dHIVi7saHJhZxpMPOBjOt8aGavkNMVhnMTJzwUDIrq62dD5EQSw7Pym5TMeahpUczhJWJ68NQwPc_ayF8VFXL3vnScCAUX9cFyw32mDFSlxK6Yfjx9BntBJV3BNpQe0nFlabTOPFWjdWW2BryqyphnsNOCwmDrrofD0f1mvbvaUDft5pPK4k-ssiDAhntMQpKxPin3f3wy1l2Hs3un3Q1xluzpIT9bGa30xT7w7rl1LdGd8WC7UUavqBb9WUv79P0FuaN3mgq9GnMrQQIb5gVv3Y9nmXx74UScA47MP_p68Q4neSOkagAlltpFmmn3nWxo1lU2kg0JNyGSb7EkATOpJRNJ4qn6ksKtc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هلندی ها به این شکل پرچم فلسطین رو از دیوار کشیدن پایین
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/72011" target="_blank">📅 23:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72010">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39a7c63375.mp4?token=N3eDVRsiDBm4QHSmb_xltc1aVCQ43GmXDc3hjIPbev1CLd9ox-AQ7PxUJ_GhGOdDWZBo5zvbgVgkkreX3b28_fNGAVa6i6Wn-hwOureYGsVGeg0uW2K70HOOT48wWrBObRCqUhuYqGBYLunF4pOnBvxDq3QMbz8PZRCm6tn_3k2iLJWvdti7gMpEKUHmwFoTZ8fAI1FJoZQuIO3G-vj84aZwfBuwwRCcbXnpMqfAbaUkboVCq3qLTwm6RWggoSvIQILTl1VywxKarIpNiNSqDmUgj2pFjGIP2JMjlF8stxpfbI0koHlZLuDdZfOCgFJP1EUcIZ7oNRWK-acsK6EGTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39a7c63375.mp4?token=N3eDVRsiDBm4QHSmb_xltc1aVCQ43GmXDc3hjIPbev1CLd9ox-AQ7PxUJ_GhGOdDWZBo5zvbgVgkkreX3b28_fNGAVa6i6Wn-hwOureYGsVGeg0uW2K70HOOT48wWrBObRCqUhuYqGBYLunF4pOnBvxDq3QMbz8PZRCm6tn_3k2iLJWvdti7gMpEKUHmwFoTZ8fAI1FJoZQuIO3G-vj84aZwfBuwwRCcbXnpMqfAbaUkboVCq3qLTwm6RWggoSvIQILTl1VywxKarIpNiNSqDmUgj2pFjGIP2JMjlF8stxpfbI0koHlZLuDdZfOCgFJP1EUcIZ7oNRWK-acsK6EGTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدر این پسر رفته تو اتاقش سیگار پیدا کرده
و پسره هم این شاهکار رو خلق کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/72010" target="_blank">📅 22:51 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
