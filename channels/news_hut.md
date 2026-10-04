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
<img src="https://cdn4.telesco.pe/file/LP84syQkixBjY2HgrjZmL23Lf9f_T2CL_5XYZ2pi2UwzHAnG1YmR3exAiZ2g-4YA8BmhPaTbrr7IuOh2M_MLR1xWvg9BicYjp9dZ76VQ0jatZIGpfxdj-0-b7VXjTaUAu-GT3yZ3C55NgtgbkOBq7V5XGLjzfjm7RR8aB9igjTpMPzRI8jLJazoleiMlX7oeqtobxE_hDP2pKfz75F1T6Bnwh4MYm0yz0cDcvnDibXw0lEmFh-dFhq7i5aqtbX5TXAyM7R9HXvNqT48mlBKYB1N3yfRSII8ruHZ8tSDyco0GBPEphfU6CRwwF4TkW3w6jJyGrWG0UnrDzV1t3bt0Hg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 20:42:00</div>
<hr>

<div class="tg-post" id="msg-72736">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1dad032a8.mp4?token=gQcY2gMmK3zxiae8akzNTB2MzcIGsHW4v5lbppgtwkD7FixVu1HaVBcmlo76z21U26gWr79wfdtzIBm-TNnF48UbVtdb0hOc1hsqeNZ-DvfVnh1d3421nah00zgEUTjca69LeNxE8iCOa6GM_E48PovZF7Eq6DkJPKmhPhTvwnFD3pJtyZ4Ni8EWaSKX9dzyCmBstuoMRXeOyy_lUgR4VjA0xcljJ8cKgoDvJNAMcs0CtiZJUznKXgcoRfoWcecZ7nyrHHeancnxvearWpaPlEgPfe6l7M_lVn_UQlhTovppsCTnIlnm65jv0OhaMY6mdJggocjPB8Wk0b9sBPthmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1dad032a8.mp4?token=gQcY2gMmK3zxiae8akzNTB2MzcIGsHW4v5lbppgtwkD7FixVu1HaVBcmlo76z21U26gWr79wfdtzIBm-TNnF48UbVtdb0hOc1hsqeNZ-DvfVnh1d3421nah00zgEUTjca69LeNxE8iCOa6GM_E48PovZF7Eq6DkJPKmhPhTvwnFD3pJtyZ4Ni8EWaSKX9dzyCmBstuoMRXeOyy_lUgR4VjA0xcljJ8cKgoDvJNAMcs0CtiZJUznKXgcoRfoWcecZ7nyrHHeancnxvearWpaPlEgPfe6l7M_lVn_UQlhTovppsCTnIlnm65jv0OhaMY6mdJggocjPB8Wk0b9sBPthmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رتبه یک کنکور تجربی همین‌جوری داره بین موسسه‌های کنکوری دست به دست میشه و تو همشون میگه که من از بچگی اینجا بودم.
@News_Hut</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/news_hut/72736" target="_blank">📅 20:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72735">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/112f06092b.mp4?token=aLSq3-monHuHXEztNh02HYJiOBQF4kXe_zEhwH_DGCB9Rx7b1rLKEapE1omAhuCTDC0zQe9N2ILg5klWwtnC-3bQfw3SlmIMTMrV0cBK1V9XTmz4_mjWnIh9mM9Ratc2c2GR5dGHLLAnfJ-eIKXVvnWfYmnzpp6tbzz8zkkg191vg_Th0LRLQjzMpXjLW1HgYNIlkoui9ygSHgWKq_7ev7YtwUIZ53lu8Z31QTkjpPMPNmI7kZCv5bkXb3_s70N8EQGwnbo18mWxttLG2Kkf6gBjrU9GlHt52R1S1qzEfulZFsTh-TznTQJMxLqSkeHQqOQlsmLFkzpWtYf-4eOK82Zm4Aw7PJxZf-Zy2dhdpb6ZRkV3eZG4zS19v7gMRwRK8F_7K6Xpw8ZbCpWUugCNQUAzhwXyGU34Ky278-QJ7nvCEDodvw09Er-JJTqxIxbxoeMnwdeWyak6IQtOLSmfqlHh32GjYeuKseT6RQAeOo95c0C_gMy1cD0SvOb3shqdLtmmt8qNbvRHWqTz03qRxbqFIT7AIqM-dYOFWixFFTTFX25wBwfHqkXzqp9iepC8tJQrqjsCmpDJMhL63s0AmF-F8mehskvNhe1DsIkwHgBVQPOn9kF9Yta3iVYXJly4SJwFyV8m6MKKbVjudp9Qeo5au3cExOQtjwpE8LENCM8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/112f06092b.mp4?token=aLSq3-monHuHXEztNh02HYJiOBQF4kXe_zEhwH_DGCB9Rx7b1rLKEapE1omAhuCTDC0zQe9N2ILg5klWwtnC-3bQfw3SlmIMTMrV0cBK1V9XTmz4_mjWnIh9mM9Ratc2c2GR5dGHLLAnfJ-eIKXVvnWfYmnzpp6tbzz8zkkg191vg_Th0LRLQjzMpXjLW1HgYNIlkoui9ygSHgWKq_7ev7YtwUIZ53lu8Z31QTkjpPMPNmI7kZCv5bkXb3_s70N8EQGwnbo18mWxttLG2Kkf6gBjrU9GlHt52R1S1qzEfulZFsTh-TznTQJMxLqSkeHQqOQlsmLFkzpWtYf-4eOK82Zm4Aw7PJxZf-Zy2dhdpb6ZRkV3eZG4zS19v7gMRwRK8F_7K6Xpw8ZbCpWUugCNQUAzhwXyGU34Ky278-QJ7nvCEDodvw09Er-JJTqxIxbxoeMnwdeWyak6IQtOLSmfqlHh32GjYeuKseT6RQAeOo95c0C_gMy1cD0SvOb3shqdLtmmt8qNbvRHWqTz03qRxbqFIT7AIqM-dYOFWixFFTTFX25wBwfHqkXzqp9iepC8tJQrqjsCmpDJMhL63s0AmF-F8mehskvNhe1DsIkwHgBVQPOn9kF9Yta3iVYXJly4SJwFyV8m6MKKbVjudp9Qeo5au3cExOQtjwpE8LENCM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهنشاه محمدرضا پهلوی:
"همیشه تلاش میشود ایرانِ دوران من با بهترین دموکراسی‌های جهان مقایسه شود، ایرادی هم به آن ندارم.
اما درباره اینها (ج.ا) که چنین قتل‌عام میکنند همه می‌گویند بگذارید درک‌شان کنیم، بالاخره اسلام وضع ویژه‌ای دارد، در حالیکه آنچه اینها (ج.ا) می‌کنند، در تناقض با اسلام است.
حتی در لیبرال‌ترین محافل، دوران من با بی‌نقص‌ترین دموکراسی‌ها قیاس می‌شود اما به اینها که می‌رسد می‌گویند بگذارید درک‌شان کنیم، اجازه دهید با آنها دیالوگ برقرار کنیم.
این چیزی است که برای من قابل درک نیست."
@News_Hut</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/news_hut/72735" target="_blank">📅 19:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72734">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe642fca6.mp4?token=T_EZOQrK8EPoHdi4a5vMfS-Td-XP6vvSswlExloHfigm3D8tWxV7kfZkLmlkI424OlalJHkpSpMXVwPL9dAZJdE2mR8RxjV2H4RNoctm5dxMXbRV7Xpbm99ht2fNIp-XuoRVmGA5UnR5jQglVHfYfBek4QHu9_F9AaGDH6slvQK_TtIbH1OaOv4woUcZi_QWTvLRtE3NFigkBl5nwu5dJ0ifI4sNBvjJXx5XNgL0nJ8_NegxjLYnaiszrnOulXGxTn1PkJawG8IP8IYefN8181QMkRVz6owpsUA6Wfv_9Ldp8wFLQYAZo-gewQyuksZhqcrSpGEJ46Fpvod4qJrqvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe642fca6.mp4?token=T_EZOQrK8EPoHdi4a5vMfS-Td-XP6vvSswlExloHfigm3D8tWxV7kfZkLmlkI424OlalJHkpSpMXVwPL9dAZJdE2mR8RxjV2H4RNoctm5dxMXbRV7Xpbm99ht2fNIp-XuoRVmGA5UnR5jQglVHfYfBek4QHu9_F9AaGDH6slvQK_TtIbH1OaOv4woUcZi_QWTvLRtE3NFigkBl5nwu5dJ0ifI4sNBvjJXx5XNgL0nJ8_NegxjLYnaiszrnOulXGxTn1PkJawG8IP8IYefN8181QMkRVz6owpsUA6Wfv_9Ldp8wFLQYAZo-gewQyuksZhqcrSpGEJ46Fpvod4qJrqvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگنده های عربستان سعودی مقر نیروهای خودی را بعد از اینکه به تصرف حوثی ها درآمد، در تعز یمن بمباران کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/news_hut/72734" target="_blank">📅 18:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72733">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMaIiBKSTuxI_lkeE_IMPfwdYsrXkMj24jsOTJGUQnFLhLZJHtvxLCldLSV1lGFAVOzJLizRJj1zv2TaSbDDSpfHO6TRosyFudDpCI-XQuqUkE2ZYXSC2BeiXSOAxLmq5C2xQ4qT-ammhEETs-UgieSDE4_XVtZthYULp7MUHWcCFVVcORiQR5oaM5qftE9QnOLDgzfNp8Sy7BqbKt2hE174Uo3kLfHZdKVq6Jug7NZ6jKzuyWTJNNicJa6q9V0nK4Bu8NskLdAZ55oQGO8q5x0H8OK_A5i7JU2w96fEUkUB2bSqzOaxLkGmkIKPRwEDDWyT29ERcHkcgK-QyGA0kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده با ارائه کمک‌های اطلاعاتی و پشتیبانی در تعیین اهداف، از عملیات تهاجمی تحت حمایت عربستان علیه حوثی‌ها پشتیبانی می‌کند، اما به‌طور مستقیم در نبرد مشارکت ندارد.
شاهزاده خالد بن سلمان، وزیر دفاع عربستان، از پیت هگسث، وزیر دفاع آمریکا، درخواست انجام حملات هوایی کرد؛ اما مقامات آمریکایی اعلام کردند که واشنگتن فعلاً قصد انجام «اقدام نظامی مستقیم» (عملیات کینتیک) را ندارد.
گزارش‌ها حاکی از آن است که فرماندهی مرکزی ایالات متحده (سنتکام) با انجام این حملات مخالف بوده و یمن را عاملی می‌داند که تمرکز آمریکا بر ایران را منحرف می‌کند.
@News_Hut
| Axios</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/72733" target="_blank">📅 18:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72732">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9ee58a69b.mp4?token=ky5W8chamQ-L3pISWdRfsq0e6SFx5sRijDftivE5szc5UWB8RU6VmqgMj9PDhQopP9O7rxmrGXsE_6WOllqG6MBRta9qRtsVgeHVU1Jl8q9i-7cX19s6hF6oHqs_B5wO_2FtoIVV9Dvou5wIP-TzCkzzTBiE_O6VucgsbKiIINPbIs0XiNl1SNK5YO0V1uv9iQdgPu7cMNsbVlQ6e35D5t5J___ClMBjsOsVXl1s5GuSRQdbqeYFFKeKCBKlx0ggZ_X7rH8Sl-DpP7xLrsOsr7MorQRgcrnyhaOsiH8Mr2vldwdJ0i-VGRTIm1G6oLp_fSMxM9Vodfdcwk2bQh35Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9ee58a69b.mp4?token=ky5W8chamQ-L3pISWdRfsq0e6SFx5sRijDftivE5szc5UWB8RU6VmqgMj9PDhQopP9O7rxmrGXsE_6WOllqG6MBRta9qRtsVgeHVU1Jl8q9i-7cX19s6hF6oHqs_B5wO_2FtoIVV9Dvou5wIP-TzCkzzTBiE_O6VucgsbKiIINPbIs0XiNl1SNK5YO0V1uv9iQdgPu7cMNsbVlQ6e35D5t5J___ClMBjsOsVXl1s5GuSRQdbqeYFFKeKCBKlx0ggZ_X7rH8Sl-DpP7xLrsOsr7MorQRgcrnyhaOsiH8Mr2vldwdJ0i-VGRTIm1G6oLp_fSMxM9Vodfdcwk2bQh35Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش:
در جریان این جنگ به این نتیجه رسیدیم که قطعاً باید برد موشک‌های خود را به ۱۰۰۰ کیلومتر افزایش دهیم، زیرا دشمن در حال حاضر در فاصله‌ای دورتر از سواحل ما مستقر است.
اکنون در این مسیر گام برداشته‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/72732" target="_blank">📅 18:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72731">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72731" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/72731" target="_blank">📅 18:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72730">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmfhAOvNZ3y4hgDmuhzVNQGHuVtE0F1BzgNLEyT9B88KX9C4Lne-a1Pau_UR8ZgTwhMrtsl4GNDbPDMQJSjq4R7n6QN_Pn4On6fmRSefeuXJIOEC-5KU5cKRrqMHmwTVGhnwqSATyLXY5F65ChDTxzSbgoecqWj2DAgTAKE5JydIYuaybLpzKJiG066JO9jGoUV9XIOTgcv53kqQP8g5nYR4RW60tm4VCCXX8tkbdpMvKz4DRr5cO9pl5V76TVjViNzYmpCX7sDAaitsskQ8hCt9X7h10KTmtxWKPRIOPWPDNJdKmHP5FzZBzjWFFVnZs2kVukEZKQyoibHVkoy4YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز نروژ
🆚
پرتغال را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
نروژ: ۲ برد، ۳ شکست و ۸ گل زده
پرتغال: ۴ برد، ۱ شکست و ۹ گل زده
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
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/72730" target="_blank">📅 18:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72727">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKiY6TT2IDJd8flplMrcJ4tke_55_VYhDJyhAJiv9EGM6uHRC6tAcEil6vvWvti2gHjmKpT9f4U-gDVH98QIeew76AIuqWTImPwe4cupCrbIZCEa9DpqgFk9t1gTkGxYvFSqVf7FKvwo39PuTn58h7DqQ4nzp0ZzEEFE5tbL_iqxLp2EJv76sadlFQ2kIXEEaPR2WjQ7kQnylgXHiNDiN2XKZBYTWDvzS0X9RAWg-tTUuV7a4nLPbySVyrtYRADbXP6g8eJibKvIl4dUjIts9x4aSFt7lchP1gjpqHIqFp3Vt0cMWHuN_5WVASwKHcqK7WhlUs93ittqvYgW_n87qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0214da517f.mp4?token=g4OiLDJslw_z6Jh563mniWL6Y2jVGZrkNeKJGocK96RPjJFW6wQBdoh5sQhkuwgvi_hpZbBhq1vWHIFccqece32BoV3CUjldGOlGYtYDQp2Z2R5JcXbbIDF5bI4C2XZWUbf7UycrQsPSFA49b-9oc1FGQdgztW5elTnX6Yd8eXOHKeBRhgAjWMb6MfBvYmRlNQGC3R-Ny2mGAtw_SDmusiklwEoVG32aufw442qBQMZw5tBOycba49GuFyR8hl6AiGqQA9UGyy2_OFqr6u-GDL8WuICFpDagFdc-UTp8ClHYENTa2mBNYVluzxXol5zPklTk-x4vx_yfSBsS_8OY9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0214da517f.mp4?token=g4OiLDJslw_z6Jh563mniWL6Y2jVGZrkNeKJGocK96RPjJFW6wQBdoh5sQhkuwgvi_hpZbBhq1vWHIFccqece32BoV3CUjldGOlGYtYDQp2Z2R5JcXbbIDF5bI4C2XZWUbf7UycrQsPSFA49b-9oc1FGQdgztW5elTnX6Yd8eXOHKeBRhgAjWMb6MfBvYmRlNQGC3R-Ny2mGAtw_SDmusiklwEoVG32aufw442qBQMZw5tBOycba49GuFyR8hl6AiGqQA9UGyy2_OFqr6u-GDL8WuICFpDagFdc-UTp8ClHYENTa2mBNYVluzxXol5zPklTk-x4vx_yfSBsS_8OY9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به نظر می‌رسد نیروهای انصارالله موفق شده‌اند کنترل منطقه «البرقانی» در شمال «الصفیه» و در محور جنوبی تعز را به دست بگیرند.
در ویدئویی که منتشر شده، نیروهای حوثی هنگام ورود به خانه «سلطان البرکانی»، رئیس پارلمان شورای رهبری ریاست‌جمهوری یمن (PLC)، و تصرف آن دیده می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/72727" target="_blank">📅 17:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72726">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad9e96757a.mp4?token=RA0GFBiKm1R5n6Jv096LESY0XC71hFcWh2OXvptBlB9AU-K2D_d2_qH5Y3b9EW-uk7NFCSBPr5sWe-peKCnIQMUWucJNE32Yv44jmx2GjpSAy457pBaZxEGOecQ5_c4hvGMEYpQPJ-XTk_-4SF9XoOliRXBquEkJh8FSTXATM7AtZhh-sv6DUn-LoPKBA5ilvm6JX-upLgA72KUtJaFv87G15aUxj1AljDsilXtP5eosWhODQxNJcRMuMoSDsXgPy5GoUW_aiNk-66EeSFDdTJao75kjRiMCP7kNYfD9dwFCjyFEOEHsXNJws-_SNFuwiqWYRcpxvyhVpqJIbM4d1iu-1Q1SEWn3qsYBXrm6dJso5yQudljS6qk-UJJWzGg2auTta9-2wixwLTU_zmPh0lAq0WUIideMFQzZjxjMnQ3sjNMulWCyznfOVmQsh49ubIq01uQgHb9xrCXa1c-WDZ0vYwxvmpxxyn0n14EHIoLWfb5t5s9tGa9sbXunEA84uLgXY35Av931G7_r0nqOZHxR89bZ4tRf1DKX9C--pL_dAU82ZsvZsLizFdLZBHDIVNE3z0tIHXq2Vw0FflMrdmdnz7gY8rUnPbPPp6r9wMOqD98CLACqycrEADoYU7LHFjsgfLEuXPcakBxZqhZiQlHXQaUaNEegsM9Ry4_nqbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad9e96757a.mp4?token=RA0GFBiKm1R5n6Jv096LESY0XC71hFcWh2OXvptBlB9AU-K2D_d2_qH5Y3b9EW-uk7NFCSBPr5sWe-peKCnIQMUWucJNE32Yv44jmx2GjpSAy457pBaZxEGOecQ5_c4hvGMEYpQPJ-XTk_-4SF9XoOliRXBquEkJh8FSTXATM7AtZhh-sv6DUn-LoPKBA5ilvm6JX-upLgA72KUtJaFv87G15aUxj1AljDsilXtP5eosWhODQxNJcRMuMoSDsXgPy5GoUW_aiNk-66EeSFDdTJao75kjRiMCP7kNYfD9dwFCjyFEOEHsXNJws-_SNFuwiqWYRcpxvyhVpqJIbM4d1iu-1Q1SEWn3qsYBXrm6dJso5yQudljS6qk-UJJWzGg2auTta9-2wixwLTU_zmPh0lAq0WUIideMFQzZjxjMnQ3sjNMulWCyznfOVmQsh49ubIq01uQgHb9xrCXa1c-WDZ0vYwxvmpxxyn0n14EHIoLWfb5t5s9tGa9sbXunEA84uLgXY35Av931G7_r0nqOZHxR89bZ4tRf1DKX9C--pL_dAU82ZsvZsLizFdLZBHDIVNE3z0tIHXq2Vw0FflMrdmdnz7gY8rUnPbPPp6r9wMOqD98CLACqycrEADoYU7LHFjsgfLEuXPcakBxZqhZiQlHXQaUaNEegsM9Ry4_nqbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛رشاد العلیمی، رئیس «شورای رهبری ریاست‌جمهوری» (PLC) یمن که مورد حمایت عربستان سعودی است، از آغاز عملیات نظامی تمام‌عیار در تمامی جبهه‌ها برای بازپس‌گیری مناطق تحت کنترل حوثی‌ها (انصارالله) و احیای حاکمیت این شورا در سراسر کشور خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/72726" target="_blank">📅 17:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72725">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05733ed2f5.mp4?token=dSKijXYBdh_L-nvdaCfNu8jkQGPKLi_GJJR3dxeVVQQK7C3VlPYEaos6Hl4fpomGEFlbjZjuAvhu2OgwpqXTV_vQFUspDOeBTeMNUgySUgSf80JBFLLUmX1oB9Hrg2EDSCHCG6e9KB2JkRucM_Wk1mvIp2H5ZmdmGhjCCXZHffJw_OV_T7IFsWcbGA3CNIUuRWG4Ik6b0dMI4MrbBceYVrLFzc6CCng1oz0q5AR8vE4Ve2XBuMcN6he0A1xcdQF_iUaqT6W5hkoUNzytHQybdkiR8NTxDdonSL0LpEZX8WHeWco-qE9xTvwrAsnPVqWR6mMwk8ZN52Y28P5q3-Z6_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05733ed2f5.mp4?token=dSKijXYBdh_L-nvdaCfNu8jkQGPKLi_GJJR3dxeVVQQK7C3VlPYEaos6Hl4fpomGEFlbjZjuAvhu2OgwpqXTV_vQFUspDOeBTeMNUgySUgSf80JBFLLUmX1oB9Hrg2EDSCHCG6e9KB2JkRucM_Wk1mvIp2H5ZmdmGhjCCXZHffJw_OV_T7IFsWcbGA3CNIUuRWG4Ik6b0dMI4MrbBceYVrLFzc6CCng1oz0q5AR8vE4Ve2XBuMcN6he0A1xcdQF_iUaqT6W5hkoUNzytHQybdkiR8NTxDdonSL0LpEZX8WHeWco-qE9xTvwrAsnPVqWR6mMwk8ZN52Y28P5q3-Z6_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پای رپر ها هم به تجمعات شبانه باز شده:
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/72725" target="_blank">📅 17:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72724">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f15ab8539d.mp4?token=uY-3tprnI7JUBmcqCnEmoIRvnrhWR_GBSrhFd6vH8vUNxqlWLO7GgJLTxdJvQPQGrXkl_Cge9CLGz9B6K3kW6cDa73zVorKqdFRYTTCwithhdz-794qF8848Bzdcr72xpCKbuldL7zGrHatZ1hb-ztBn20R6taJ2-LXitgZJQJ5UwXUx8CZrF7Ie2faZqPxptURfyetHmqqXqkTMm9a-hYTics9S9tXLMa-ys8cLHFzKVE9xTMm0agJCASm_b3U_iBNXxVrBG0wVBc91O0KA-TJ_4P27KfuCKTbK1qkojunUMMZQ59psgHQULX0A5K8uIEeJ-bUEVybtXwxcLlZwmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f15ab8539d.mp4?token=uY-3tprnI7JUBmcqCnEmoIRvnrhWR_GBSrhFd6vH8vUNxqlWLO7GgJLTxdJvQPQGrXkl_Cge9CLGz9B6K3kW6cDa73zVorKqdFRYTTCwithhdz-794qF8848Bzdcr72xpCKbuldL7zGrHatZ1hb-ztBn20R6taJ2-LXitgZJQJ5UwXUx8CZrF7Ie2faZqPxptURfyetHmqqXqkTMm9a-hYTics9S9tXLMa-ys8cLHFzKVE9xTMm0agJCASm_b3U_iBNXxVrBG0wVBc91O0KA-TJ_4P27KfuCKTbK1qkojunUMMZQ59psgHQULX0A5K8uIEeJ-bUEVybtXwxcLlZwmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه زنه داشت از حس و حالِ ناراحت پسرش تو روز اول مهر فیلم می‌گرفت که یهو یه مرده اومد و این شاهکار رو گفت:
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/72724" target="_blank">📅 16:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72723">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5caffe71ff.mp4?token=fnY9zOGGkZf9830vlpLP5iUr78mWOhQ-6b8vAZUBrdDVeLkM_b-DiTF8fZdYZNDE6TiFvuOKYvx-z9srnpyAO7Q9DCopS7nQizWO6AKBXUvhRz_e-E8W38r4RqqC5Gfn5a8E0Z7Ql9B3GX1OMqaXXPcHa3P13ziipZWxZH84TQASSWQy7rlirt5KBFTF-oYvqchstBrs3fRsVbvJSIe25prpcJerERGFn5IK7bHByGDYMZ5JSjA5_y4d2Knevj16i4Emdr0ZobZ7onOSVd82gW-TWu2tVxDjAMBJy3ALdys95mMyKNjgD8ibksQ9Y9LMLJ59DpcDgBfxPxt8bzP1wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5caffe71ff.mp4?token=fnY9zOGGkZf9830vlpLP5iUr78mWOhQ-6b8vAZUBrdDVeLkM_b-DiTF8fZdYZNDE6TiFvuOKYvx-z9srnpyAO7Q9DCopS7nQizWO6AKBXUvhRz_e-E8W38r4RqqC5Gfn5a8E0Z7Ql9B3GX1OMqaXXPcHa3P13ziipZWxZH84TQASSWQy7rlirt5KBFTF-oYvqchstBrs3fRsVbvJSIe25prpcJerERGFn5IK7bHByGDYMZ5JSjA5_y4d2Knevj16i4Emdr0ZobZ7onOSVd82gW-TWu2tVxDjAMBJy3ALdys95mMyKNjgD8ibksQ9Y9LMLJ59DpcDgBfxPxt8bzP1wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو مکزیک  یه گزارشگر داشت از وضعیت خرابیِ کنار جاده گزارش تهیه میکرد که همون لحظه یه ماشین لیز میخوره و تصمیم میگیره گزارشگر و فیلمبردار رو با دیوار یکی کنه :
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/72723" target="_blank">📅 15:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72722">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf8cf90e0c.mp4?token=FULAkLCUhMDIGOJXqoNXTEmABlDHsieOyyX0H4XTlCRnHs6YSNX01ZN0Ugrne2lWZnzlNFAWj9m8j442hXfV2WrpiawBWYCxl3786tMhdRqgLvYLvZOs0GVsInRpZmnIQLpSASMEEuPV1qAMVrehdSOZm7vhCPJBZD00476q39aabETZ5k-WtxIQuyY9_JsV-b1o8VAUh5emk8Sfr8KOBz2PMdS_to6oM7rTBh0QQ7Po1S2YoRiTV5ZuWs8mbB9-eU3I8LdPMpypZUSHimSD7jjla8QtxTLwoQ8WrHfYz3RxPOr1LanNyTWTil5guK4Gt-Y4Nw6OguEmfBV5LfRMKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf8cf90e0c.mp4?token=FULAkLCUhMDIGOJXqoNXTEmABlDHsieOyyX0H4XTlCRnHs6YSNX01ZN0Ugrne2lWZnzlNFAWj9m8j442hXfV2WrpiawBWYCxl3786tMhdRqgLvYLvZOs0GVsInRpZmnIQLpSASMEEuPV1qAMVrehdSOZm7vhCPJBZD00476q39aabETZ5k-WtxIQuyY9_JsV-b1o8VAUh5emk8Sfr8KOBz2PMdS_to6oM7rTBh0QQ7Po1S2YoRiTV5ZuWs8mbB9-eU3I8LdPMpypZUSHimSD7jjla8QtxTLwoQ8WrHfYz3RxPOr1LanNyTWTil5guK4Gt-Y4Nw6OguEmfBV5LfRMKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فریادهای مهدی کوچک‌زاده نماینده مجلس بر سر همتی رئیس بانک مرکزی؛
کوچک‌زاده:
مملکت را دارند به آمریکا میفروشند.
«به خدا اگر از جهنم به خاطر کوتاهی‌هایی که در حق شما مردم کردم نمی‌ترسیدم، امروز خودم را جلوی بانک مرکزی آتش می‌زدم.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/72722" target="_blank">📅 15:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72721">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d26538e463.mp4?token=MolsRkj3v7pg0Mi8kVxtJHfkBvPi3aYvSnj1DYigUur3iKTlze-b9-CZY8JTlPfrVgmY5gxZZYTqRsEfPKQ0un_NORYFlR-WPbALjYV58obXcTrffkfhvYO2yZm-ayaqjU9CLlq1ApBGKen9Zk6quEDuMasbqRqWn4bjtxE-jlN5CkdbJ0D7pZh_E9VYyzXO0Fk38-2-NzFiBTN2ioWHC-Ax-MNe1yKGsuKa1fptuif-7SSSNvX_46A5wozDmXxOLaLi44H1_7B53RFJRn70c3MSFPhulFIubhPke1H4-3Xmhv6dsyQaZOdp_gnuOPV5jwVdITbAzHbqT8LE9fsoYAHHrIUWVMmKnswQSqp8LiuIgUDDnH-B8vEklUNvbvDRJJlUjLwx-f4mmMmD0UfLKkzbOAFBFq5SAURrDbQPC0sI8uEUtUR6kyH79afkSJmDMszi8ynE0CwKs1xDvtsD92WA9OyfqnfDBtkN4uN9NiCI7Iey7xRSPHXn-cEpJkIahFFdBGDBEPO8ETAn9jzg0kwqkApbY3rf8IvLG4ViDNktkdb13J6TRLw-RIJ6yxh17e_lD48aEMMF3dVcSduNyBh3dPAHYudPgwncjTol26t8oYYy2a-FZ4SZ6YUXdZwEl7ykRgPotKMvWkDFqDmrb4aE3PBy-RYP2tnMRBSHifU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d26538e463.mp4?token=MolsRkj3v7pg0Mi8kVxtJHfkBvPi3aYvSnj1DYigUur3iKTlze-b9-CZY8JTlPfrVgmY5gxZZYTqRsEfPKQ0un_NORYFlR-WPbALjYV58obXcTrffkfhvYO2yZm-ayaqjU9CLlq1ApBGKen9Zk6quEDuMasbqRqWn4bjtxE-jlN5CkdbJ0D7pZh_E9VYyzXO0Fk38-2-NzFiBTN2ioWHC-Ax-MNe1yKGsuKa1fptuif-7SSSNvX_46A5wozDmXxOLaLi44H1_7B53RFJRn70c3MSFPhulFIubhPke1H4-3Xmhv6dsyQaZOdp_gnuOPV5jwVdITbAzHbqT8LE9fsoYAHHrIUWVMmKnswQSqp8LiuIgUDDnH-B8vEklUNvbvDRJJlUjLwx-f4mmMmD0UfLKkzbOAFBFq5SAURrDbQPC0sI8uEUtUR6kyH79afkSJmDMszi8ynE0CwKs1xDvtsD92WA9OyfqnfDBtkN4uN9NiCI7Iey7xRSPHXn-cEpJkIahFFdBGDBEPO8ETAn9jzg0kwqkApbY3rf8IvLG4ViDNktkdb13J6TRLw-RIJ6yxh17e_lD48aEMMF3dVcSduNyBh3dPAHYudPgwncjTol26t8oYYy2a-FZ4SZ6YUXdZwEl7ykRgPotKMvWkDFqDmrb4aE3PBy-RYP2tnMRBSHifU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
من با کیم جونگ‌اون، رهبر کره شمالی، رابطه بسیار خوبی دارم.
وقتی طرف مقابل ۱۱۲ موشک هسته‌ای در اختیار دارد، خوب است که با هم کنار بیاییم.
اما تفاوت اینجاست: ایران هرگز موشک هسته‌ای نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/72721" target="_blank">📅 14:56 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72720">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe93c3478.mp4?token=CW-RmmqPxbb6b3Hc-N1NyKPdh59uzJgvWtfhvb57W-sUMBcBZ3If9rePAk5ZDKnjqRWKSq4VspBjBHFmki_Wj9LcyHmm4sLl5br316NSM4Ck_4Ae719X4x7tr8EzzkFL0uJYZNxLVA6C0ZmngZoe2wLr6D1MYM7g-LfgmEkTFyiwqMLNcDNUMvPejDcdIt5Q_7r3Kw9nd68GWsQCbFSShB-u9iNh5mkIIz_lhz69AX7JETtaxKDLZdxbhWYH7vibhSHyOLR7KGfPh_ltOpnD6v84T8ec4pRAovHKEhCpkdS7-guWnd62gPj4Ws60JUpKCbW1NPeJiKrTt6ePWBOdpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe93c3478.mp4?token=CW-RmmqPxbb6b3Hc-N1NyKPdh59uzJgvWtfhvb57W-sUMBcBZ3If9rePAk5ZDKnjqRWKSq4VspBjBHFmki_Wj9LcyHmm4sLl5br316NSM4Ck_4Ae719X4x7tr8EzzkFL0uJYZNxLVA6C0ZmngZoe2wLr6D1MYM7g-LfgmEkTFyiwqMLNcDNUMvPejDcdIt5Q_7r3Kw9nd68GWsQCbFSShB-u9iNh5mkIIz_lhz69AX7JETtaxKDLZdxbhWYH7vibhSHyOLR7KGfPh_ltOpnD6v84T8ec4pRAovHKEhCpkdS7-guWnd62gPj4Ws60JUpKCbW1NPeJiKrTt6ePWBOdpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل بقایی سخنگوی وزارت خارجه جمهوری اسلامی :
بحث‌ها پیرامون خروج از پیمان منع گسترش سلاح‌های هسته‌ای (NPT) در محافل سیاسی ایران بسیار جدی است و وزارت امور خارجه به تصمیم مراجع ذی‌صلاح پایبند است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/72720" target="_blank">📅 14:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72719">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7872ea066a.mp4?token=pSGY8VwZxR9-GroUZ4kTxk-KkFHiQh-iFZL-aNnl21J5HWQWmvyM1Z61gPm777GDwkNQe-gnGQ3jzJyldsMHlaxMAZn4JgNwtOPdmhkYfGIgkjUtQNzl1WeJVf1S-s7YLv6Yr1920zAvceTzELi7WiIhtFLy1fwJr3IrR8lwSjc1n2dswJjMzgt5zF8dItapTI3QekSxS0HxGwcWNxgPAIa3BGsnzKeSD9JAtSWV1ZnvWxS88ykJBCG2ZzC_XGP9BDhFArEU_13fPZjpasEXuFNpv58JpDOqObuEdbqR3SArRQOLA0UR8BINoN7C7ElvhenOx8iL2JYfWQk2wmFgVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7872ea066a.mp4?token=pSGY8VwZxR9-GroUZ4kTxk-KkFHiQh-iFZL-aNnl21J5HWQWmvyM1Z61gPm777GDwkNQe-gnGQ3jzJyldsMHlaxMAZn4JgNwtOPdmhkYfGIgkjUtQNzl1WeJVf1S-s7YLv6Yr1920zAvceTzELi7WiIhtFLy1fwJr3IrR8lwSjc1n2dswJjMzgt5zF8dItapTI3QekSxS0HxGwcWNxgPAIa3BGsnzKeSD9JAtSWV1ZnvWxS88ykJBCG2ZzC_XGP9BDhFArEU_13fPZjpasEXuFNpv58JpDOqObuEdbqR3SArRQOLA0UR8BINoN7C7ElvhenOx8iL2JYfWQk2wmFgVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکشنبه ۱۲مهرماه۱۴۰۵؛آتش‌سوزی در پاساژ خلیج‌فارس عسلویه به دلایلی نامعلوم:
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/72719" target="_blank">📅 14:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72718">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDesa5_kt6wJV_MUzPI7MhdjpBktGmdgvvPBRu3Qr2o1MdablP5tn0vdlB1AXTYEakF_hKt2RskZSny1i9DXOoD4TP4E4MfZ--CN4aieSelRHiRZaQ2WvDKo78l6eHEqbcJj0HxAFeFS7ygr1EBmF8SmU8G6xyHruVggjE6Y6IVn85p458DM17PoElGlA-OjKRHmPzcr4RD_XCdwQ-yUQ1mMEEkRUtFj6B-1jUAOR3hS34YFhQQZw8vCexfDCTZetR-GCHixuujK1RtAoJhXAzgtqTbGPpLXHlj-3g6fsBTVuCg0VgUnaIdGwN2zL-rP8-jHlQ9uxJtVzv6tQirSpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز تهران _ نجف که قبل از محاصره هوایی حوالی ۱۲ تا ۱۹میلیون تومان بود ، دوباره برقرار شده اما بیش از دوبرابر رفته رو قیمت و شده ۳۰ تا ۳۸ میلیون!
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72718" target="_blank">📅 13:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72717">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3330937cb2.mp4?token=BDdjLjuFIP__runP94ZVL78lEFRxkqsb3t3KE4-DZOz-Pq9lWNJEeyLvS-btlH9iSHrDFtzz54C6-cX6ciHAMUPA5V0rVn6fEJXI92aT0VYI4Eq1tqIHdYeV8bZ4nhR7VYuJ-B6KcGg-vAY5iEOg4D8ICyRUR9ArSDqpuEvrVexyVPmAL-hBl-tFSNitgIu-n5TaueI8q6pqZ5uRuOZ35yak3DIF-vdaH_nOJIoS-IqS5JDLX6YSnoPaOYOA9xyA_aUO-fmOkkZL7hX4GaRyQIOfdlCez20ULzVHULGVrZDg2UQY2nYkIi22TErHvkCa1VS47O02H7qsffjdHeW7HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3330937cb2.mp4?token=BDdjLjuFIP__runP94ZVL78lEFRxkqsb3t3KE4-DZOz-Pq9lWNJEeyLvS-btlH9iSHrDFtzz54C6-cX6ciHAMUPA5V0rVn6fEJXI92aT0VYI4Eq1tqIHdYeV8bZ4nhR7VYuJ-B6KcGg-vAY5iEOg4D8ICyRUR9ArSDqpuEvrVexyVPmAL-hBl-tFSNitgIu-n5TaueI8q6pqZ5uRuOZ35yak3DIF-vdaH_nOJIoS-IqS5JDLX6YSnoPaOYOA9xyA_aUO-fmOkkZL7hX4GaRyQIOfdlCez20ULzVHULGVrZDg2UQY2nYkIi22TErHvkCa1VS47O02H7qsffjdHeW7HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش روسیه به پل شمالی در کی‌یف حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72717" target="_blank">📅 13:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72716">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42b7e86ab7.mp4?token=oPQRo0Zu4K6kQm_n7l5nlyNUuHMrB6KcVlZcdjRJ7hNInPNXS71WqQuOgAnNjqbuAVNo_zsDvDrclDLa2mUjrsmnu5LsiNdf78B2S-fOMx3Xt2D9YxNLWD5l2NTfTafG0hMtOCwqDq1kXb8beitfIsULgczLKM5skfxFecfD2YDz43P0B4UhqIjy8vQo0kU4fetLHHL9U3ebDtSKuaR5kY8dJCFfGt70gUewriHcddyPWRNewjEm6pYfQydK_mJ5jeIbuqT4vJ8bqSSdM39yQyg_SyQxoviz9mg5dRWaTh-OPFMWL7cTx5P7sm7OQ8dRof8Wpozb4yO_y0P1qewsEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42b7e86ab7.mp4?token=oPQRo0Zu4K6kQm_n7l5nlyNUuHMrB6KcVlZcdjRJ7hNInPNXS71WqQuOgAnNjqbuAVNo_zsDvDrclDLa2mUjrsmnu5LsiNdf78B2S-fOMx3Xt2D9YxNLWD5l2NTfTafG0hMtOCwqDq1kXb8beitfIsULgczLKM5skfxFecfD2YDz43P0B4UhqIjy8vQo0kU4fetLHHL9U3ebDtSKuaR5kY8dJCFfGt70gUewriHcddyPWRNewjEm6pYfQydK_mJ5jeIbuqT4vJ8bqSSdM39yQyg_SyQxoviz9mg5dRWaTh-OPFMWL7cTx5P7sm7OQ8dRof8Wpozb4yO_y0P1qewsEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حرکتی شاهکار نگهبانای ی شرکت رفتن با سلاح برنو بالن هواشناسی رو زدن و بعد زنگ زدن به سپاه گفتن پهپاد آمریکایی رو زدیم بیاید همین الان جایزمونو بدید
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72716" target="_blank">📅 12:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72715">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دلار ۲۷۱.۰۰۰تومان
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72715" target="_blank">📅 12:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72714">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7da8647691.mp4?token=V5w6y75awvR-7OU7jHA63wfRwJxhkeEqClt9QmHCxyq8QlyxzEKPDu067oOPkjxWblcIII3ofgDa-l8XEIX84Kpe0zhh0jcmXpl7Svk83DXixhYItQ7YMobBp7qoXmTl6NT_ou0nbqZN2kjfibp5qIa6eYa6hCR5CQeVOfUJtw291fke7LljW1T7Hq1RLkXCoN3PQ5QgSd65EDPpMZ5H36XX15fNzEFZBYU2MJfrz6q_BcHXY7CxUyZibe9RxyUhMRKPDIO4vzhxPF9aRg_0ePoTM1w5nte-PYIShPpBeFc7WVZQpylbnVEGRi4Q9TBh8PcIZ_kguZr73My_vaHmSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7da8647691.mp4?token=V5w6y75awvR-7OU7jHA63wfRwJxhkeEqClt9QmHCxyq8QlyxzEKPDu067oOPkjxWblcIII3ofgDa-l8XEIX84Kpe0zhh0jcmXpl7Svk83DXixhYItQ7YMobBp7qoXmTl6NT_ou0nbqZN2kjfibp5qIa6eYa6hCR5CQeVOfUJtw291fke7LljW1T7Hq1RLkXCoN3PQ5QgSd65EDPpMZ5H36XX15fNzEFZBYU2MJfrz6q_BcHXY7CxUyZibe9RxyUhMRKPDIO4vzhxPF9aRg_0ePoTM1w5nte-PYIShPpBeFc7WVZQpylbnVEGRi4Q9TBh8PcIZ_kguZr73My_vaHmSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت بر سر قبر علی خامنه‌ای، علیه مسئولان نظام شعاردادند؛
«گرانی رو آوردن، سازش کنن با دشمن»
«مفسد اقتصادی، سرباز آمریکایی»
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72714" target="_blank">📅 11:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72713">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHO1JzXGD4I6tycoJYx-4ZvzYFm8UNsFevRu0VlBVErLeTc1NqnwFGaklss4S7nx10C9doQUlix0ZWWmC0fafbGju8KdYucLtjNEj6RBT_15mt_hQfZl9adru6Iavwhc8Z_6y_C0CjLx9C7rbVEbjoD8ukyvJRGz_q3-Un4hBI8BzBsbitr0JEhVweD5fElBw76cwuIQog29mR0Bt-DgyhrgDK7HLjkypm1_uXsEkxv4Vm2FKQe4EkggauPE-oyEeo7soydtjHxvKQ6MZd4mSTS3A0-iUTw1EiepLaXry1a4Rk4e0krF0CRSkUO_diWDOEkuHyJdvDD_JkXEUNiQiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش در داخل تنگه هرمز هدف یک پرتابه ناشناس قرار گرفته و موتورخانه آن آسیب دیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72713" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72712">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72712" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72711">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkhYQn94lOvssFptX8FxG8P1-G1Aex0zMC-e0R1MlIInhKn97Fioe3Fwfip33xn9BDhn_OfBZvAWPQf88-DuhLo3YqJpgEyfza9z-8sOhkgII_lSDKZYLFI3-zjJxwsUlOB5YKXXQcRKDLATsr8Lspw0cIABG39-HYexGDyoTSa8xfWbPyNHLxuSYMEiLcFAMyRo_qiY4vxLl-ELzeV4MGh8WCvc69dctWnqWz1HKfWpaynWbIeuyOEpZugKXhrUS7sGEtJPUaIAmx6xuZcqCaYPfHLufJeGHu0DdqC3C-Xfb76VkdfYGpbHUfXzslTnM0cMsSYmo33mTlMzLjQynA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آلمان
🆚
یونان
صربستان
🆚
هلند
نروژ
🆚
پرتغال
دانمارک
🆚
ولز
آفریقای جنوبی
🆚
مصر
مالی
🆚
مراکش
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72711" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72710">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50e9a4b7ef.mp4?token=E6GXW3nmyeqA4WWQ0umSal1jdAX2ufnjeZxnKKK88Yy27EFxZhlefWZ_WatrhkKh9cqQl5tLlQCNg2xY4a3rqYroeVKfThsujmknuPWp03okrVGLJ6pGZ02ujVIslVzecQeyZtqdmX6GMHGPhuvzXt7mkn_APsWcCjPKSx6dleBrYuTwcoYX7kCwdB01Fz7EhXjVSXz4OeSYrF9GRmBbyInoeJRaoaSq5B-qdX_MegdLMv-kkqtSK2YFo-_1ry5s_7dRKf0C2edK1GwxjFen6wVc3hnbVRyQrk2DVRe0Xm74nc0BHukaanVvD0VkuEeKJzTtSkcgR8YN1ZZBdlNwHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50e9a4b7ef.mp4?token=E6GXW3nmyeqA4WWQ0umSal1jdAX2ufnjeZxnKKK88Yy27EFxZhlefWZ_WatrhkKh9cqQl5tLlQCNg2xY4a3rqYroeVKfThsujmknuPWp03okrVGLJ6pGZ02ujVIslVzecQeyZtqdmX6GMHGPhuvzXt7mkn_APsWcCjPKSx6dleBrYuTwcoYX7kCwdB01Fz7EhXjVSXz4OeSYrF9GRmBbyInoeJRaoaSq5B-qdX_MegdLMv-kkqtSK2YFo-_1ry5s_7dRKf0C2edK1GwxjFen6wVc3hnbVRyQrk2DVRe0Xm74nc0BHukaanVvD0VkuEeKJzTtSkcgR8YN1ZZBdlNwHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بابایی، رئیس کمیسیون اجتماعی مجلس:
می‌خوایم حقوقِ کارمندان دولت رو 5 الی 10 میلیون تومن افزایش بدیم!
قراره «فوق‌العاده خاص کارکنان» تو کوتاه‌ترین زمان ممکن و با امتیاز 2 هزار تا 20 هزار واسه کارمندان اجرا بشه.
این افزایش از اول شهریور محاسبه میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/72710" target="_blank">📅 11:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72709">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a343c0ae1.mp4?token=EOK-_bWB9gypjB5QPj2f4fyR82yYcwRAoEbuCEDwmlpKPYltV9pCO_OITNObyW-9_aqeh8xZNTrfXUnp0_dxgtyyH8TpDbEzYpIwj0ERbIzWz-cbVf-Q95fWPC9mOvIrkKnM5U8P3eSAW_rfUlFXPYyAcWwAFy2XRGB1XXaifa4LCOaAz-6kV_8aGRGkSjmt4eB0h6xWHZC9Q2aLKw2sOZAUUR1PMDqaZWLao1fXjKVSZHE8zF9dn221HlQW68XJDDP-aPnusbzHOHmjrRpB6BfilEsX377sGYgGpam1Oc_XkggABGBKBJD57EuRpc4EQyoH943kd8WiAYrCLHG1FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a343c0ae1.mp4?token=EOK-_bWB9gypjB5QPj2f4fyR82yYcwRAoEbuCEDwmlpKPYltV9pCO_OITNObyW-9_aqeh8xZNTrfXUnp0_dxgtyyH8TpDbEzYpIwj0ERbIzWz-cbVf-Q95fWPC9mOvIrkKnM5U8P3eSAW_rfUlFXPYyAcWwAFy2XRGB1XXaifa4LCOaAz-6kV_8aGRGkSjmt4eB0h6xWHZC9Q2aLKw2sOZAUUR1PMDqaZWLao1fXjKVSZHE8zF9dn221HlQW68XJDDP-aPnusbzHOHmjrRpB6BfilEsX377sGYgGpam1Oc_XkggABGBKBJD57EuRpc4EQyoH943kd8WiAYrCLHG1FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر خانوم 15 ساله به‌خاطر اینکه هر هفته پریود میشده به دکتر مراجعه میکنه تا بفهمه مشکلش چیه؛
بعد از اینکه معاینه میشه، دکترا متوجه میشن ایشون دو تا دهانه رحم و دو تا سوراخ واژن داره.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72709" target="_blank">📅 11:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72708">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aed172c29.mp4?token=BxDZLUxGTLcHgdUYrG-NnpcJN1mos_dE4WMRLIQFtvMHjZnVOLnr1-Y2cHM70FdNuWT7o0HkwHEg2OI8BAe0L0EYq8BfbxGndbN0SHPZP2ENYIegarANKhkn2PsfvT3fZ1K6s_c0i39nWUB9lOOu4rQgydPLhOp3RUYVVZUIzudkC3vJM8iri3ODMMyoFQDz4ZmChgJxoDbVDBcMTDVVy-w8KJbOm0d5svkJivjqi2VfeisnStYFOoWjGdoMrqZ9NCeCpLeid-rqMONTLQPdTzsejkQ0gzeSCoJMip7z9lmGpDKNR2y0KGhuQlw2xpd9k-gLwUGd-RG0WCOWj7Z1aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aed172c29.mp4?token=BxDZLUxGTLcHgdUYrG-NnpcJN1mos_dE4WMRLIQFtvMHjZnVOLnr1-Y2cHM70FdNuWT7o0HkwHEg2OI8BAe0L0EYq8BfbxGndbN0SHPZP2ENYIegarANKhkn2PsfvT3fZ1K6s_c0i39nWUB9lOOu4rQgydPLhOp3RUYVVZUIzudkC3vJM8iri3ODMMyoFQDz4ZmChgJxoDbVDBcMTDVVy-w8KJbOm0d5svkJivjqi2VfeisnStYFOoWjGdoMrqZ9NCeCpLeid-rqMONTLQPdTzsejkQ0gzeSCoJMip7z9lmGpDKNR2y0KGhuQlw2xpd9k-gLwUGd-RG0WCOWj7Z1aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صداوسیما:‌ حتی اگر بمب اتم بخوریم باز هم نابود نمی‌شویم!
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72708" target="_blank">📅 10:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72707">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9499513e9a.mp4?token=NWOJYNkvWQUIX7dYY-A03ke6rQF0gwczktsqpvTOXIYcV-prejc5Wmx_R-4ZENDEFt1iu7SuJUBBjkeofGx07nWkVQwt5mawTEw05xrrcGEBvdNMcUPs9k08UFhY-YUNSjoiwmlbjY_kurSmA3QhIc5ZuSBYQ1lKlKxREhFtMlI-9pMm-zPaU9mohsSmY5n_PlBfxL2q-cwVsxgnGGIRmqLEi20s5qtSs2ntge7ef-y9LGS0XivSDKr8wOOqcpMMx6Oahhh-Xisf8FKp0Nv9zGLFPY7vekiCCxRXJUy7Hxe0xVYoT384xZKY4BM-i3dBJ_MLBJRekpTP7LjjwOTuuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9499513e9a.mp4?token=NWOJYNkvWQUIX7dYY-A03ke6rQF0gwczktsqpvTOXIYcV-prejc5Wmx_R-4ZENDEFt1iu7SuJUBBjkeofGx07nWkVQwt5mawTEw05xrrcGEBvdNMcUPs9k08UFhY-YUNSjoiwmlbjY_kurSmA3QhIc5ZuSBYQ1lKlKxREhFtMlI-9pMm-zPaU9mohsSmY5n_PlBfxL2q-cwVsxgnGGIRmqLEi20s5qtSs2ntge7ef-y9LGS0XivSDKr8wOOqcpMMx6Oahhh-Xisf8FKp0Nv9zGLFPY7vekiCCxRXJUy7Hxe0xVYoT384xZKY4BM-i3dBJ_MLBJRekpTP7LjjwOTuuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه این مدرسه اس
پس ما کجا میرفتیم؟
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72707" target="_blank">📅 10:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72706">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8589525917.mp4?token=LZYk9cJzDRIpF2mxYOY0A-bQJ2V6Z8t2GRwcc0sZoml-K-Q1gFKVqNvoTfaMIHbwqu_OmMtXvaVujo1hk1f3DFApalz2Zb_CtUTxFtoGhd_XmgldLvhUmKFsJadCU4tnOizMgxLgsVBK7Nd1x5WstYZpDZThHz0t2jiIiygxQ9Imn2P2Xsb-oC4fZgdOePo7C6T5nIdf_DpyQ5pSLwmpaBjyZit6DB_ZXAvIJJY87bhbiNXaVwuDe4fyzKLfk-HDITkU3pV-8VcysH-kIppPYHLZOruXTrWUjfNGXb8DzleOYWImWixMj8pDwtDk35pLoD05efrpXgjNw3zm7KVYwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8589525917.mp4?token=LZYk9cJzDRIpF2mxYOY0A-bQJ2V6Z8t2GRwcc0sZoml-K-Q1gFKVqNvoTfaMIHbwqu_OmMtXvaVujo1hk1f3DFApalz2Zb_CtUTxFtoGhd_XmgldLvhUmKFsJadCU4tnOizMgxLgsVBK7Nd1x5WstYZpDZThHz0t2jiIiygxQ9Imn2P2Xsb-oC4fZgdOePo7C6T5nIdf_DpyQ5pSLwmpaBjyZit6DB_ZXAvIJJY87bhbiNXaVwuDe4fyzKLfk-HDITkU3pV-8VcysH-kIppPYHLZOruXTrWUjfNGXb8DzleOYWImWixMj8pDwtDk35pLoD05efrpXgjNw3zm7KVYwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در بخش‌هایی از کرج، از جمله باغستان و جهانشهر، روز شنبه ۱۱ مهرماه ۱۴۰۵، پس از بارش شدید باران سیل جاری شد و خسارات نسبتا زیادی به شهروندان وارد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72706" target="_blank">📅 09:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72705">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c198c4452e.mp4?token=dUcBsLuAhkzsxazICZWN0M-NYXJs285V18pq2jG4o8KeIAJM-KyCly7TGK0TDLlq33O7JFnrxW5o3bRleRgkMbjYzAx7mtDh4dQfH59otktlr3UM8bJZw9hzHVOGbQbg5le3NM7RVoZhz6TMYpVdJv3hWkbAjf6CQ9inxUx-BnbbyGDstA386I-4zqDbpvG_V1yaOycy3vr-vhOjFpTi0geDU43DciFnFxQ56q-hRTWYa1l00-jDmCkxVuMoQHEEBCdg0XHBF84DQLr1nhQauMWnoz1q_B8n97IwdBO8tDpAyQvdQ9hQ-K0EBzwatW4CJtBWSEmF1Da6ip-yTB_uKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c198c4452e.mp4?token=dUcBsLuAhkzsxazICZWN0M-NYXJs285V18pq2jG4o8KeIAJM-KyCly7TGK0TDLlq33O7JFnrxW5o3bRleRgkMbjYzAx7mtDh4dQfH59otktlr3UM8bJZw9hzHVOGbQbg5le3NM7RVoZhz6TMYpVdJv3hWkbAjf6CQ9inxUx-BnbbyGDstA386I-4zqDbpvG_V1yaOycy3vr-vhOjFpTi0geDU43DciFnFxQ56q-hRTWYa1l00-jDmCkxVuMoQHEEBCdg0XHBF84DQLr1nhQauMWnoz1q_B8n97IwdBO8tDpAyQvdQ9hQ-K0EBzwatW4CJtBWSEmF1Da6ip-yTB_uKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خراتیان، کارشناس صداوسیما: چین ارسال تصاویر ماهواره‌ای به ایران را متوقف کرده است!
مجری صداوسیما: چین به ایران گفته ابتدا مشکل خود را با آمریکایی‌ها حل کنید و بعد به سراغ ما بیایید
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72705" target="_blank">📅 09:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72704">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72704" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72704" target="_blank">📅 01:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72703">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1W8b6vAdBBHqi31BbQkxRza3tJ-zDNwlR35N1njRBiYt36MBrZfQEaEpIs1vovRtQBfgVn_EV1JjoaZVZ-JZPpUnwa4xnmLOnvWhTmyxGM7sUBH6nif5ZUv-k6XAfhR2ecMt2nJXmoG7mWxAvWP3SpfPE6_VfiD2QoA59bUZ7em9h1GGAeoR4vFuLjSyMr5GtqjIiVibE1Yb4AFMlZB2wmjOsOYqIuoU_ppQeAkBuuUbKO1nGSr3quAhBME7Pzg-Boa2xv5C5xujxzJIjetWDF7d8qtPQ04DKgMkngFDjhG0H0z2KZBcYGeJDipkZDTCxqU3tqG02D4zIuVFThG4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72703" target="_blank">📅 01:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72702">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af2d851559.mp4?token=ZuDwpDqHLeSWHafZ_IASCXIdN6vLW7x1JjsQzA1NaI1FTB2q7S_taym3snN3YtOch0j4GhDIU5qb4PRqqZ4iJVyrOxTNj7K_fVtfMaYl4hDOHBq0EtDi_f7FqqCi0H1rBdn0fibxrdp7ZrY7opEtLTQR2_8W-uerbVHArKGUD-CYbNUwrPiUnAzNydpZK_wl6sR1Yq-Nzc7OHikt5vj4r5X7bhKTHham7YqQ2VKiBy22nUz7gv7rJdLiMoyT2a80L6FJ_J84aZQlZiexU6c1ZAI908oNciWcGHRqg6q_J6cfzSeV_rNE1SeDctd82k4-nxRdyEOSS21M9WfCE0sB2iDxE5s3jRsC9kqUBM3HO0A2BzL5mlTi7gWObf4p6NQF45K7Oc5D-F7b9tsu88vDN4ouY-ZnsnJCT6eEkUCGvfJO-2QkURn5-28ehD9JuRzUN4G-iIf4TCPMJjq-K035OhofJEEUYEVVyqCMzkNMLdunEGT6RAMoJS9Kh1fWopbdjqI3Vop7RTrMEvdF_zxHP2uvmfg2dAEjsdcQkzpzlhQRU41_f__uk-FOJaQ9COTj3xP8bToyA3LWXeL53NTaR5Ll8nAkNwJAcTPfeBcGAvWGuEBdNU2h6phDjAgP8iefndY-sFmC6tMf64-EYFM1KcbiJy8cVSLRghMNtGltYAM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af2d851559.mp4?token=ZuDwpDqHLeSWHafZ_IASCXIdN6vLW7x1JjsQzA1NaI1FTB2q7S_taym3snN3YtOch0j4GhDIU5qb4PRqqZ4iJVyrOxTNj7K_fVtfMaYl4hDOHBq0EtDi_f7FqqCi0H1rBdn0fibxrdp7ZrY7opEtLTQR2_8W-uerbVHArKGUD-CYbNUwrPiUnAzNydpZK_wl6sR1Yq-Nzc7OHikt5vj4r5X7bhKTHham7YqQ2VKiBy22nUz7gv7rJdLiMoyT2a80L6FJ_J84aZQlZiexU6c1ZAI908oNciWcGHRqg6q_J6cfzSeV_rNE1SeDctd82k4-nxRdyEOSS21M9WfCE0sB2iDxE5s3jRsC9kqUBM3HO0A2BzL5mlTi7gWObf4p6NQF45K7Oc5D-F7b9tsu88vDN4ouY-ZnsnJCT6eEkUCGvfJO-2QkURn5-28ehD9JuRzUN4G-iIf4TCPMJjq-K035OhofJEEUYEVVyqCMzkNMLdunEGT6RAMoJS9Kh1fWopbdjqI3Vop7RTrMEvdF_zxHP2uvmfg2dAEjsdcQkzpzlhQRU41_f__uk-FOJaQ9COTj3xP8bToyA3LWXeL53NTaR5Ll8nAkNwJAcTPfeBcGAvWGuEBdNU2h6phDjAgP8iefndY-sFmC6tMf64-EYFM1KcbiJy8cVSLRghMNtGltYAM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفنگداران دریایی ایالات متحده در حال سوخت‌رسانی به یک فروند هواگرد «ام‌وی-۲۲ آسپری» (MV-22 Osprey) در خاورمیانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72702" target="_blank">📅 01:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72701">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f216caf4ae.mp4?token=i-nZF7R8G6P3BFyIz_JDmEp8Q3b2rD9n_l3YFUJxtRMNUypV3q0YFRzBgLg6DKJYtBp4RMlmUEqYq6Pn9z_y6vEaSPjIhP0yDUtzRlwalRx_4sgl66nfUslRdAbMru-9vM0tg10lV9mOjpkClM64dKiCoo06M4leLeqA98JxeuRG2ZdXF_Nf4N3IzB0FawHobMaD74d3Jlao_Irzn0cauLBhRpQAlhBvB8104JoqPe1Xn9OVNbAjCc1sgz5NMdMZ_M4fnZnt4VKRyPxvq6GbHmRL3xhSMaZdw_SmOdj0Si-kOi6W3CeyPU5cA7RqxfWYBqxhIlfbA2piOz4siBNUVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f216caf4ae.mp4?token=i-nZF7R8G6P3BFyIz_JDmEp8Q3b2rD9n_l3YFUJxtRMNUypV3q0YFRzBgLg6DKJYtBp4RMlmUEqYq6Pn9z_y6vEaSPjIhP0yDUtzRlwalRx_4sgl66nfUslRdAbMru-9vM0tg10lV9mOjpkClM64dKiCoo06M4leLeqA98JxeuRG2ZdXF_Nf4N3IzB0FawHobMaD74d3Jlao_Irzn0cauLBhRpQAlhBvB8104JoqPe1Xn9OVNbAjCc1sgz5NMdMZ_M4fnZnt4VKRyPxvq6GbHmRL3xhSMaZdw_SmOdj0Si-kOi6W3CeyPU5cA7RqxfWYBqxhIlfbA2piOz4siBNUVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
ایران نمی‌تواند سلاح هسته‌ای داشته باشد. البته، همان‌طور که می‌دانید، ایران عملاً از هرگونه برنامه‌ای برای دستیابی به سلاح هسته‌ای دست کشیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72701" target="_blank">📅 00:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72700">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e33db7c818.mp4?token=pr_-cHk0vfN4L_U80JrRE0uT53AAOR55SEH2TiA4LqjhQ1yErdOG9qje7zoIO4iPI544r0gqTo_7I1va8Wf4ixjEyeKDde4BF0j4Aa4zah9Z5cepJQkjUNJSDIFnwO02nMVwakMXm15yCNbWe440q2KiD26bHW1YM_sLb5HRttwz4ENNt0AARgBID_3vgYDoSNB06xZROaNsGUeJQFKg4J81d7_VDN9J3dwDjUuewCHk-pxL63cyY9xU0AhQIv_hkqybWMr-So-tQTI9lq8sirq20JDewABrzymaAGvj6CPptNSgJhI-2xet0MFcMI1R19n5kV1F0yggfWnCTeNHoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e33db7c818.mp4?token=pr_-cHk0vfN4L_U80JrRE0uT53AAOR55SEH2TiA4LqjhQ1yErdOG9qje7zoIO4iPI544r0gqTo_7I1va8Wf4ixjEyeKDde4BF0j4Aa4zah9Z5cepJQkjUNJSDIFnwO02nMVwakMXm15yCNbWe440q2KiD26bHW1YM_sLb5HRttwz4ENNt0AARgBID_3vgYDoSNB06xZROaNsGUeJQFKg4J81d7_VDN9J3dwDjUuewCHk-pxL63cyY9xU0AhQIv_hkqybWMr-So-tQTI9lq8sirq20JDewABrzymaAGvj6CPptNSgJhI-2xet0MFcMI1R19n5kV1F0yggfWnCTeNHoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ترامپ: تصمیمی درباره ایران دارم که باید بگیرم. کار را یا به روشی آسان پیش می‌بریم یا به روشی دشوار.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72700" target="_blank">📅 00:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72699">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b62816af7e.mp4?token=fHafkSmHP9EFbntsOtFz3g9eZ2pLhjfPi3p1HBDJ2uQoTJsdqTkvFdjypCzCvdNpdILWnv889OmeOdpH17oKf6HBrFL4HXIH_WPMGoGq_0sPe4JJ_O32Z8tIJnXbH5n5K0YyLpQYZ-tKvnf9_FXzUOEE-ntQAMtMV3D7C7BGnCj6I5GdLSEzzLRCyY_oQs-M3iZjS_mGct3_XZtQAtDSSZFgmyNgsf5Z7JDh8EfzATbC5NgHsIKOqAThnEfokmwnpFkIQp2wUnrwd9ahyy8Jn6En-fks4Wwe__TOt4LHDvZu9V_4QgkJKArQ3qM-56Bkc1hPqyTjeTdNhNl5dfU3VSlnvWcf2AsMXDof3szgUdHNCtbZuon7iq3YOaHMmgQhM_YLf1hWAdY8vp74mmnrARXoYzwFlZuv9r4M8oqPYUNaZkZ59Qog6z4iyIiIYh3lK-rUg2yglwNyihK1ptVwRFUJx-9ZyfPBFoR5NyFFIYwh5YIzLpCAqR4pT712_BN4wFahJg89dU9gcrlS5J5nptFTLEG5XelQcjSPSSMi1SlwsBigamhiF6kY9gA59pQ4RvdwC7dROv5WQX7Gxj6RdFEm0MTBfd_K-NIrvc5IL1CbaLFvPMpvdD8u9xAi-_iVmzK1Fqe7xzYULE8L3CfafhF725_oMoOQviSofR7Np5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b62816af7e.mp4?token=fHafkSmHP9EFbntsOtFz3g9eZ2pLhjfPi3p1HBDJ2uQoTJsdqTkvFdjypCzCvdNpdILWnv889OmeOdpH17oKf6HBrFL4HXIH_WPMGoGq_0sPe4JJ_O32Z8tIJnXbH5n5K0YyLpQYZ-tKvnf9_FXzUOEE-ntQAMtMV3D7C7BGnCj6I5GdLSEzzLRCyY_oQs-M3iZjS_mGct3_XZtQAtDSSZFgmyNgsf5Z7JDh8EfzATbC5NgHsIKOqAThnEfokmwnpFkIQp2wUnrwd9ahyy8Jn6En-fks4Wwe__TOt4LHDvZu9V_4QgkJKArQ3qM-56Bkc1hPqyTjeTdNhNl5dfU3VSlnvWcf2AsMXDof3szgUdHNCtbZuon7iq3YOaHMmgQhM_YLf1hWAdY8vp74mmnrARXoYzwFlZuv9r4M8oqPYUNaZkZ59Qog6z4iyIiIYh3lK-rUg2yglwNyihK1ptVwRFUJx-9ZyfPBFoR5NyFFIYwh5YIzLpCAqR4pT712_BN4wFahJg89dU9gcrlS5J5nptFTLEG5XelQcjSPSSMi1SlwsBigamhiF6kY9gA59pQ4RvdwC7dROv5WQX7Gxj6RdFEm0MTBfd_K-NIrvc5IL1CbaLFvPMpvdD8u9xAi-_iVmzK1Fqe7xzYULE8L3CfafhF725_oMoOQviSofR7Np5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ، درباره ایران:
ما از همان ابتدا اعلام کرده‌ایم: ایران هرگز به بمب هسته‌ای دست نخواهد یافت؛ تمام. این موضوع، یک منافع حیاتی ملی برای ایالات متحده آمریکا محسوب می‌شود.
ما این مسئله را در جریان «عملیات پتک نیمه‌شب» (Midnight Hammer) به وضوح نشان دادیم و در «عملیات خشم عظیم» (Epic Fury) نیز آن را آشکار ساختیم.
ایران می‌خواهد با مسائلی همچون تنگه هرمز بازی درآورد؛ اما کنترل آن در دست آن‌ها نیست، بلکه در اختیار ماست.
آن‌ها عملاً هیچ چیزی به دست نیاورده‌اند؛ چرا که محاصره ما آهنین و نفوذناپذیر بوده است و ما هر شب تقریباً با همان ظرفیت‌های پیش از جنگ عمل می‌کنیم.
ما احساس می‌کنیم که در موضع بسیار قدرتمندی قرار داریم. ایران باید تصمیم درست را اتخاذ کند؛ در غیر این صورت، رئیس‌جمهور ترامپ تمامی گزینه‌های لازم را روی میز خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72699" target="_blank">📅 00:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72698">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6316faf3f3.mp4?token=N87fqbn7krG8_8ebuT0TQon6u9gW5dD7xoPdfmUH2rtqItCTmgFSW0L-DalcBVi5BqiJpBn9kEyUbC3Vwf0QLPJhaxEVOSJPhOQn-gNso5R61yIry0mjCJScbTp4L-V2aJQyQxr_iqrttWDV-6zpcTa0o05qFNtfBHLYJLNC6MTnEFocG8DnphzP-Ta_R5yTShf0gFCdyiaxpTjWrHIemr31peAfRnh04sPj7GGjEeh261GSAdQnd4BXt88chBQGj9JE1jGoRVvfJT4qE8m3Di1nowu95zGd4_vMy4QjAVyqQ9M-1q38yk78juNdjK3IX_zidsX7vfGccrhuowwjWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6316faf3f3.mp4?token=N87fqbn7krG8_8ebuT0TQon6u9gW5dD7xoPdfmUH2rtqItCTmgFSW0L-DalcBVi5BqiJpBn9kEyUbC3Vwf0QLPJhaxEVOSJPhOQn-gNso5R61yIry0mjCJScbTp4L-V2aJQyQxr_iqrttWDV-6zpcTa0o05qFNtfBHLYJLNC6MTnEFocG8DnphzP-Ta_R5yTShf0gFCdyiaxpTjWrHIemr31peAfRnh04sPj7GGjEeh261GSAdQnd4BXt88chBQGj9JE1jGoRVvfJT4qE8m3Di1nowu95zGd4_vMy4QjAVyqQ9M-1q38yk78juNdjK3IX_zidsX7vfGccrhuowwjWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدت زمان حضور رهبری تو جنگ:
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72698" target="_blank">📅 23:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72697">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e8309253.mp4?token=J8ZE3YBTa4MIORTsGE4i6vRstcJGsYKPpGFza-kzBPHbnABMqliveYgozMphLpgkU7Jr40ZdTikZGVd-aSXKADbKQKczlJ3Sl6cQjnJpSs8R6gd5B8sVpEfkMLD3vRVIb2FIFjSROtIWKv0kdAjHDNaadaV5Veae0QqnhOzhBjImhNdBveuQdydVhV1TTAbsuwgecw-ivjKy5WpXj_DcMM0lqDqLlKz1PJNi--cwaw76LhWMhYADCHhQKT5sfq4WVU-q04BSSHgVlDG9OruysPcJDLb2wHyio-_1lwB4BAHXUzZjqo8z5a46CBue-H77LCX5Bon2xoB5O1LT-SfaIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e8309253.mp4?token=J8ZE3YBTa4MIORTsGE4i6vRstcJGsYKPpGFza-kzBPHbnABMqliveYgozMphLpgkU7Jr40ZdTikZGVd-aSXKADbKQKczlJ3Sl6cQjnJpSs8R6gd5B8sVpEfkMLD3vRVIb2FIFjSROtIWKv0kdAjHDNaadaV5Veae0QqnhOzhBjImhNdBveuQdydVhV1TTAbsuwgecw-ivjKy5WpXj_DcMM0lqDqLlKz1PJNi--cwaw76LhWMhYADCHhQKT5sfq4WVU-q04BSSHgVlDG9OruysPcJDLb2wHyio-_1lwB4BAHXUzZjqo8z5a46CBue-H77LCX5Bon2xoB5O1LT-SfaIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#مهم
؛
سؤال: آیا ناو «یو‌اس‌اس روزولت» قرار است جایگزین یکی از دو ناوی شود که هم‌اکنون در آنجا حضور دارند، یا اینکه قرار است سه ناو در منطقه مستقر باشند؟
هگ‌ست: سؤال بجایی است، اما من هرگز به آن پاسخ نخواهم داد.
ترامپ گزینه‌هایی در اختیار خواهد داشت؛ بگذارید این‌طور بگویم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72697" target="_blank">📅 23:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72696">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e6961bcdd.mp4?token=A30QHnr2hnJJkY7fMCYd1ecvG5gEQFWZOnd-1vr9MTRaWIY1wgdR3vKHbLOq3YPEcfmpOl5V3Ci4IRph3JJ-EM8hRSuXPXR06VhOMZIC9kfrNmi1t4HyadeU7n0qI3E0zzOppj-W4JZc_ROPz3udV2Quc9bRzdgep7ZpUZeiNPiiUrIe0M19pyvj0LtB5tQhT-AiBH1mlFlb-WU1q7TmzclZOuaKMXWhJ46Ag2zmIJzvb8lvo8MhKCVvfKNCZb_1pxg38uB_xrbv-iGpNcMa8U_71DV-AAr4hXARHQFZlGeod2Hsd350pg-nY4KHUkALnUEAez8UjTsdGAqATTpjfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e6961bcdd.mp4?token=A30QHnr2hnJJkY7fMCYd1ecvG5gEQFWZOnd-1vr9MTRaWIY1wgdR3vKHbLOq3YPEcfmpOl5V3Ci4IRph3JJ-EM8hRSuXPXR06VhOMZIC9kfrNmi1t4HyadeU7n0qI3E0zzOppj-W4JZc_ROPz3udV2Quc9bRzdgep7ZpUZeiNPiiUrIe0M19pyvj0LtB5tQhT-AiBH1mlFlb-WU1q7TmzclZOuaKMXWhJ46Ag2zmIJzvb8lvo8MhKCVvfKNCZb_1pxg38uB_xrbv-iGpNcMa8U_71DV-AAr4hXARHQFZlGeod2Hsd350pg-nY4KHUkALnUEAez8UjTsdGAqATTpjfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روز قبل تیک تاکرها باهم دعواشون میشه؛
چندتا دختر ریختن روی سر یه تیک تاکر به اسم ستایش و اینجوری همو کتک زدن:
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72696" target="_blank">📅 22:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72695">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4df7e241a.mp4?token=au6z7WHubejXRoroQhQ9xzZD_6N92oyeXGPMGl0jLDa0iJ7EJrwUENtAfckXzpqkcEO-xpPv3t0onvje-zBZxQViFNb-FDhuBz7tAGBp39-ddOWR4kppR-ghAENw5vXiaOJBDZVw5bodgsJBOSSgezlo9YLZiJJBBeGcPMfukgFTt7ieImebYjxebmZDYlG5J-CVJHfsbMNtQK8NuQhp8vyqmJtDW52CN6USJYdskRvy-hppJ7xZEnTLrz-yAotv0lu9sLOFJjbBfMs6EeRS1s-bOHPbdmXBV8JxUj2CFEB1hLbZ6-uQ_hx5Pel-Mi_Fxdb5XJCrW-DxzHt4GAFyJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4df7e241a.mp4?token=au6z7WHubejXRoroQhQ9xzZD_6N92oyeXGPMGl0jLDa0iJ7EJrwUENtAfckXzpqkcEO-xpPv3t0onvje-zBZxQViFNb-FDhuBz7tAGBp39-ddOWR4kppR-ghAENw5vXiaOJBDZVw5bodgsJBOSSgezlo9YLZiJJBBeGcPMfukgFTt7ieImebYjxebmZDYlG5J-CVJHfsbMNtQK8NuQhp8vyqmJtDW52CN6USJYdskRvy-hppJ7xZEnTLrz-yAotv0lu9sLOFJjbBfMs6EeRS1s-bOHPbdmXBV8JxUj2CFEB1hLbZ6-uQ_hx5Pel-Mi_Fxdb5XJCrW-DxzHt4GAFyJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه اخوند تو تجمعات شبانه: در پیروزی ما توی جنگ و ابرقدرتی ایران تو کل عالم شکی نیست؛ الان دعوا فقط سر میزان ابرقدرتی ماست!
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72695" target="_blank">📅 21:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72694">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7af7d5f80.mp4?token=r8CEXsC_5InrHtifAtQ-gnHwM9Sspk0CeI64bFyFCrXCmyFya1M5-Xf2tUNtP-Vx9BWcqIESLstZ2jXnf7gv8TIAqHSEcGAbxhPqCDnO0R6FR42RmUnZ601zIV-GA1dQK2BlPtiwHBfoH9Zz_TpQtAdfDu4XdaSK2cnNNBeOAOpovyhEJuAUYpE0RQYXker8My1356GWo8GZpvG4E-ltSWhLv1YVyZdwBJVwD4mVOqig1P_rUP3pnXOgr6jjTe1v_MbQWu9BG8bvQF6oPNdJZOU8XzGxUAPJnki4QL8inHOZuJ3RfXKzYzCLkW3xPGygHrwmB7yePhNUDt59AQfhfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7af7d5f80.mp4?token=r8CEXsC_5InrHtifAtQ-gnHwM9Sspk0CeI64bFyFCrXCmyFya1M5-Xf2tUNtP-Vx9BWcqIESLstZ2jXnf7gv8TIAqHSEcGAbxhPqCDnO0R6FR42RmUnZ601zIV-GA1dQK2BlPtiwHBfoH9Zz_TpQtAdfDu4XdaSK2cnNNBeOAOpovyhEJuAUYpE0RQYXker8My1356GWo8GZpvG4E-ltSWhLv1YVyZdwBJVwD4mVOqig1P_rUP3pnXOgr6jjTe1v_MbQWu9BG8bvQF6oPNdJZOU8XzGxUAPJnki4QL8inHOZuJ3RfXKzYzCLkW3xPGygHrwmB7yePhNUDt59AQfhfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو بمب‌افکن راهبردی رادارگریز B-2 Spirit نیروی هوایی ایالات متحده بر فراز محل برگزاری مسابقه تیم‌های نیروی دریایی و نیروی هوایی در «کلرادو اسپرینگز» پرواز کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72694" target="_blank">📅 21:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72693">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/24bef6628d.mp4?token=eMvlXUjWHptqodft4impt-s4LMAW9cfTd7tqI9tbfnwQoo45RxAiSgfVoARNvAYWQGPvbelMiSzhiVTGIKOr0nyinTZn6XapQTx9UoUoruYFNRmTmzonIpHu3FWBuKY1MwuZ8jnf0A1EH_LL8CFLACAZnHQa8bhCTZYjpALX4fBd68LwXYAhT9Wtstq0XYrsy2_YuQYpRQwEkDoypjeAi9bqsceuwBHMx9iftmXZDxOKF5mAyrFx2T3wYD3v_9_lCLYCCzujda4DcIhrttsJnaO4ourHL9P8MXyYfAPmVrTy3hKK2bdipIvxWdRJiboyNYOD9Ki50yqvXbR6byLMxA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/24bef6628d.mp4?token=eMvlXUjWHptqodft4impt-s4LMAW9cfTd7tqI9tbfnwQoo45RxAiSgfVoARNvAYWQGPvbelMiSzhiVTGIKOr0nyinTZn6XapQTx9UoUoruYFNRmTmzonIpHu3FWBuKY1MwuZ8jnf0A1EH_LL8CFLACAZnHQa8bhCTZYjpALX4fBd68LwXYAhT9Wtstq0XYrsy2_YuQYpRQwEkDoypjeAi9bqsceuwBHMx9iftmXZDxOKF5mAyrFx2T3wYD3v_9_lCLYCCzujda4DcIhrttsJnaO4ourHL9P8MXyYfAPmVrTy3hKK2bdipIvxWdRJiboyNYOD9Ki50yqvXbR6byLMxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از سیلاب شدید امروز عظیمیه کرج:
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/72693" target="_blank">📅 21:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72692">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">به گزارش نیویورک‌تایمز، مقامات بریتانیایی و آمریکایی معتقدند افرادی که در نزدیکی پایگاه نیروی هوایی سلطنتی «فیرفورد» (RAF Fairford) دستگیر شده‌اند، با عملیاتی تحت حمایت ایران — که یا به سپاه پاسداران و یا به یک مرکز فرماندهی نظامی دیگر در تهران مرتبط بوده…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72692" target="_blank">📅 20:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72691">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qao6kkf5wcA0mYpRaUJnDL1RY6296lUBEYq8y3TnXLMiOu28IWZeZTvvvTzs7VOcopMax6Pb_tfPu3HfhfgpLSJH4qfQ4PiCYNc9IDfb0_-2Os6bG_iIXgU_I6g87ErhJ6y6n3-yHt4HSBYPxh6kT9kxFyWUPg5gmnWxs-NltX-6VfC51zL3sBz7aO4VN-vlSUT_cxKuL7kphrRVWdZwly136tWaP_kPHoT-9Q3MORi-y7e2Sr0IIOY9ewZxF-zPS0JixwzAL5k3ydBsJZPIBOo3xqLUbTaFNbpqdZ9Y7BPjznO-1IjDSNRxj67DFevz-dOSdSVxvSKAoL7VAUcWmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش نیویورک‌تایمز، مقامات بریتانیایی و آمریکایی معتقدند افرادی که در نزدیکی پایگاه نیروی هوایی سلطنتی «فیرفورد» (RAF Fairford) دستگیر شده‌اند، با عملیاتی تحت حمایت ایران — که یا به سپاه پاسداران و یا به یک مرکز فرماندهی نظامی دیگر در تهران مرتبط بوده — در ارتباط بوده‌اند.
بازرسان در تلاش‌اند تا هویت فردی را که این افراد را به خدمت گرفته، شناسایی کنند؛ کسانی که یکی از مقامات آن‌ها را «افراد ساده‌لوح و بی‌خبر» توصیف کرده است.
با این حال، مقامات اذعان کرده‌اند که جزئیات مهمی از این توطئه ادعایی همچنان نامشخص است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72691" target="_blank">📅 20:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72690">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دونالد ترامپ به تمام شهروندان بزرگسال ایالات متحده وعده داد در صورتی که جمهوری‌خواهان در انتخابات مجلس‌نمایندگان و سنا پیروز شوند به آنها ۵۰۰۰دلار خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72690" target="_blank">📅 19:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72689">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a49047dbc.mp4?token=ahkT-ManuCFq5QfcC3BSLABI4JpOPWTpkfhFrp9s1z5NoxApNOmdE432D1DIBFremtuRB4x6k0TcQO0mOWteXy17-UQ2JcDuQxjIdzbLt0Ij3A8nLAi0f_zwmXmo85nYAZBUE04mnvuKnQmq6IDDmHceMZYLSmNDrNPiwZCFs5XGw_dvabYpEqs01WvRaOt8FDeoap5ou7rRvMoGUsVjMigqFG-2EucDv0T1ueTC8VZNw8ZeJs5ru3hXcxChpVu4vOpPnuFEU5R8ss36Z7iIQUtt7_6WOFtu0HVF-BJd5YO3gxgmcQ8RwEAeKjmRtBLgiCkERifyXnyCbZjX2TUPvRa5wnNeopR5xTwOYZ4ySMBtqFK-JjeJvVG0urE5gOqkMvo-Ft8xeBnIDjfo-5WOeFiP8X9IkFt5fi3K_FlhaeMT8EAKl917k16NA2SDPkynUOlMi1Snd2UiW7xR44qmsdShsQOLe1ZgeLD89kUgNVTMwPDqvZSC0gFT1ui23CAJckCSnSv_DPARv8F4vPGzrxB3Km1-zJKjM2FUAPx5VtAHtzE8hX9ClUDzK1DLG3SBxskIehj4Axbu7i0KLagZbmB6ynqV0-I5hdNXBByn2wjzUblOhaYLdertqt7dbNJYHdHy5Emdc8I0s-jxJRIje6NpcvGdrBpFVGC5l_LL2GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a49047dbc.mp4?token=ahkT-ManuCFq5QfcC3BSLABI4JpOPWTpkfhFrp9s1z5NoxApNOmdE432D1DIBFremtuRB4x6k0TcQO0mOWteXy17-UQ2JcDuQxjIdzbLt0Ij3A8nLAi0f_zwmXmo85nYAZBUE04mnvuKnQmq6IDDmHceMZYLSmNDrNPiwZCFs5XGw_dvabYpEqs01WvRaOt8FDeoap5ou7rRvMoGUsVjMigqFG-2EucDv0T1ueTC8VZNw8ZeJs5ru3hXcxChpVu4vOpPnuFEU5R8ss36Z7iIQUtt7_6WOFtu0HVF-BJd5YO3gxgmcQ8RwEAeKjmRtBLgiCkERifyXnyCbZjX2TUPvRa5wnNeopR5xTwOYZ4ySMBtqFK-JjeJvVG0urE5gOqkMvo-Ft8xeBnIDjfo-5WOeFiP8X9IkFt5fi3K_FlhaeMT8EAKl917k16NA2SDPkynUOlMi1Snd2UiW7xR44qmsdShsQOLe1ZgeLD89kUgNVTMwPDqvZSC0gFT1ui23CAJckCSnSv_DPARv8F4vPGzrxB3Km1-zJKjM2FUAPx5VtAHtzE8hX9ClUDzK1DLG3SBxskIehj4Axbu7i0KLagZbmB6ynqV0-I5hdNXBByn2wjzUblOhaYLdertqt7dbNJYHdHy5Emdc8I0s-jxJRIje6NpcvGdrBpFVGC5l_LL2GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ:
مرا بفرستید تا با «کت‌قرمزها» (نیروهای بریتانیا) بجنگم.
مرا بفرستید تا با کمونیست‌ها بجنگم.
مرا بفرستید تا با نازی‌ها بجنگم.
مرا بفرستید تا با اسلام‌گرایان بجنگم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72689" target="_blank">📅 19:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72688">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc7b08156.mp4?token=G9R5cKO6NMnib_blhCYT0_n6WqTTV7HnuNSycFHpO6R24-HIqyf2GcoEvRTiDPpOA0lVmPyL-hcLMxJuIXRVzwWYHUb-_qPseFf37zX5KnIk_aZyy6Jog6FdtPVDalHv-rnwsGOIVb5J40CgFHVLG0XUVm7JTez0vFZOV1sGfFKxK_LRtSqlrwZXbjf7vJuSBp3ZnBTC6xYufPaLs45bGcD0mxgYAfRIpc7006dTjmvAsEg3YUXUkTBEKed0-q1w1NMjUhFtMeXgX9ytGz-VXsaBcLW7ZJ_V392Dq18BFhaundzD1E3clbvMROiaMf50OVAKuDcmeneiHBvl83VHug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc7b08156.mp4?token=G9R5cKO6NMnib_blhCYT0_n6WqTTV7HnuNSycFHpO6R24-HIqyf2GcoEvRTiDPpOA0lVmPyL-hcLMxJuIXRVzwWYHUb-_qPseFf37zX5KnIk_aZyy6Jog6FdtPVDalHv-rnwsGOIVb5J40CgFHVLG0XUVm7JTez0vFZOV1sGfFKxK_LRtSqlrwZXbjf7vJuSBp3ZnBTC6xYufPaLs45bGcD0mxgYAfRIpc7006dTjmvAsEg3YUXUkTBEKed0-q1w1NMjUhFtMeXgX9ytGz-VXsaBcLW7ZJ_V392Dq18BFhaundzD1E3clbvMROiaMf50OVAKuDcmeneiHBvl83VHug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ:
اطلاعات نادرست، اطلاعات گمراه‌کننده و تبلیغات عامدانه‌ی بسیاری پیرامون ناو «یو‌اس‌اس آبراهام لینکلن» وجود داشت، اما ۸۰ درصد از کارکنان آن گروه ضربتِ ناو هواپیمابر، برای تمدید خدمت خود اعلام آمادگی کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72688" target="_blank">📅 19:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72687">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee4b7ed20.mp4?token=jzJTHWFaYs9Od1jX5nWaxWOy1hri0HZHcnL4I3rKuCIIaHYrFXuYGdCAZNrDUGHT5-21hS8lM_L2J4c-Kr8XeRCnKTftUwG7meBvFzbiGJYiOUvxQ3esjoK5lrkFAm2qu92zt3LlSwcyK2Q3-Ige4djOv34gBdxLfv5iAIF_OWfNys95S8QjfjCIEq-bEKcHGF8sCjByfUnKHp1EoA9Xz5TRACVflnAaEFeSAvVb9inIRtLeo89WRfQftsrHWBEliGgOYDEJk_qTPdJxKWi68TdIPt4kUAWaQyLEQtecYPcQfTPRkCzoU6GxHRXBxs_I2PymyPqd8CxyiVEJ2WusvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee4b7ed20.mp4?token=jzJTHWFaYs9Od1jX5nWaxWOy1hri0HZHcnL4I3rKuCIIaHYrFXuYGdCAZNrDUGHT5-21hS8lM_L2J4c-Kr8XeRCnKTftUwG7meBvFzbiGJYiOUvxQ3esjoK5lrkFAm2qu92zt3LlSwcyK2Q3-Ige4djOv34gBdxLfv5iAIF_OWfNys95S8QjfjCIEq-bEKcHGF8sCjByfUnKHp1EoA9Xz5TRACVflnAaEFeSAvVb9inIRtLeo89WRfQftsrHWBEliGgOYDEJk_qTPdJxKWi68TdIPt4kUAWaQyLEQtecYPcQfTPRkCzoU6GxHRXBxs_I2PymyPqd8CxyiVEJ2WusvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست لحن و رفتار ترامپ رو تقلید کرد و چیزی رو که ترامپ هنگام پیشنهاد این سمت به او گفته بود بازگو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72687" target="_blank">📅 18:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72685">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd7350ab9.mp4?token=miYu3WH5DfdN-Ha3Ktmjfhr80XccyGjyhHzXL8wPrX967OBoGkLE99-6sIf_sVPpAVCEqCEARg9NRMU4gZLjvOSMnwfWw8jJGZaO-iNsjrfUDgbKMnrCTbaPd-5oGBJKOmEKCCNQmjBub1WqPo0Kqt6tyzJGPlru59pB3WZOVEEMrSDoq0yw2F6TJQDRRwLy-pXSescN6-QDP5VAt9r-u2IpokFf8f7GpldsdaE7sKUePdGcr4uMRedf65PvLKz-lHxeYTigwqktY2-VEbtY5PDEUKjT--nAtR7YROoc7Gi8Dx_2a7L3akmM12j1AoTglMPKb1_Or391BAOr43aADw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd7350ab9.mp4?token=miYu3WH5DfdN-Ha3Ktmjfhr80XccyGjyhHzXL8wPrX967OBoGkLE99-6sIf_sVPpAVCEqCEARg9NRMU4gZLjvOSMnwfWw8jJGZaO-iNsjrfUDgbKMnrCTbaPd-5oGBJKOmEKCCNQmjBub1WqPo0Kqt6tyzJGPlru59pB3WZOVEEMrSDoq0yw2F6TJQDRRwLy-pXSescN6-QDP5VAt9r-u2IpokFf8f7GpldsdaE7sKUePdGcr4uMRedf65PvLKz-lHxeYTigwqktY2-VEbtY5PDEUKjT--nAtR7YROoc7Gi8Dx_2a7L3akmM12j1AoTglMPKb1_Or391BAOr43aADw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت آب‌و‌هوای قم رو ببینید
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72685" target="_blank">📅 18:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72682">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JByXn9VC6LC5jXqVknqNO18FOWKbY5cQaB8NRw7sCG62P3rO2mcbvNVCMrYqIJ2s4-D-Qs6EM3UZHl3eI26KgDTfQdKNMK2fEyg07qLv5qyahatnNBNRkdhooRFOlq1VBJqWdcISigaTrx6GoloRCfRSoc1nYlI64LMlKOyPXP6zn53c8ow-7NICuA68fjh_xALceOxJwGlzBEKgt9il7K6TiRMLoDe03HPoHspEvSYfLZocQgtIWdThl1Nxwnm27Qaa-rq1nW8IiyKiThycvl73YWGRVtOISvYJP8gESqjt1Dkaaexg9Hhmjf4yDteYDwk0P1xmQG7Bpzmh138A0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CWWQj8OHAk1ONywLCFScK62MAUZGdb2ZvCrHUlgn_gNQSUcKx7wgHMjDaWN0BJphEP2SKoR7iId7xsxHDCtDiNt-dep8h-_g4upER2RBqIlUN1t8zI0DTvr2lhGGZswnvKIYddTlfUQoCuthmDePMJiD6vE9XN5zVtHRWdcwW4-bEibK4e-li6pckMWizKp9is5vzduEAPP7b4KeXM2XVYpDJYN0Ioy3WuJ28esBJCF9T0NOMwebBRCNTxXOeBxbHciBp082xLTYaEKRbVH_t-yfoERAoX-Baa4jUPTLaOJn53LSbnX1OZrU_u59eIv979btJFVqrqMb4S0I3_eIwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eiP9f_HCFcwR0_NBD_a7y8WzK4aD7xkR7xq-l_UJqAXAVIWOyENE6o0sprUn3Ii8Xksg3wpYK1sGnvf0vDSXkQz-zmVASBxUsR9sfT5O-JDDYLIWmnmDHnh0oKn-Fj4GGnZH_x1dX4BjUgzfEGTuAEAfTxc4IroN5lP5eGt3Yv9vtyrM6olq1DZMkbNeKxGwg0xe71YzTPWFGnegGIoUJhlBbS-JLDwr0qAVPb2oQLZfs_VeOtmZk0pIdYsynyybjsWpgYfssjikZiAnmqow8Su9SGFagnfoKYiFZU1paUZPFdn1ZXFEayHFuj1emJlLr6U8btENPf-ESbswtTHMPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایلیا هاشمی:
ساعت ۱۶:۳۵ شنبه؛ ابتدا صدای جنگنده در قشم شنیده شد و سپس یک جسم مشابه با بدنه موشک، داخل شهرک بوستان قشم
سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72682" target="_blank">📅 17:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72681">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72681" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72681" target="_blank">📅 17:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72680">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZRghUK609J_rJjX3FAusN-wCW0h2FqF5YrAdBICG7-Qj7juFU_iGjxXDD9q41p-YM0CPghHv4XcP6Zw1qxdYbYJMJFwSWVv0n9_N9kVVoVb_Cu5x0QoAM645Rb9y_mrMsKuaoUIA8PQXemjJub8Bjebjm_jis6-VdvFuBB32PmhHSvPHLK8pxHqQOai4F4GQcsNV_n7O4DbR893Cpfn3G1q5NK6UY4UNlj7ek99IdSAxSzr6oa9UnirFLbY6mbmfjlmT5irhP4DcucWCgJ8_wq52Q6w5vU_NjarbX3ry3qS-x6R8A9RoBzz2wUcpAy8WW2Ud6e1sCjvmb0VQ7LghQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز انگلیس
🆚
کرواسی را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
انگلیس: ۳ برد، ۲ شکست و ۱۳ گل زده
کرواسی: ۳ برد، ۲ شکست و ۷ کل زده
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72680" target="_blank">📅 17:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72679">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4323337b42.mp4?token=eas0vtqBwRDWffEVSTSIRp9JTR10KLSdinyl4EV9T-GWouEak5dhu-Lmi5vXxre9tWFyfEVVxxMpPGSLUGcZLOAv-JeNWO0_w9OOnnzdb9V7Y-FnENTghuh6PX1Foek5nzE9xSQGFpvk6x0qeggUAsleE8EHGiF8Qu7EfjybaFvS1_RFwU_FOP4APVdzdyk0oDF_i7zQiLPIwfTNbTFaVbhlX6E_4nIkzOLERdgR6AKUqSyaeV7ceXuCZZg60FWnoNXcQstHGiEqhWuE2N9_eNHzSyJd_VT_aWKxQy4CWkL0c39zsGJReInEvnQjR9ICtQ6eFXnmKXRNNoEVeyLJmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4323337b42.mp4?token=eas0vtqBwRDWffEVSTSIRp9JTR10KLSdinyl4EV9T-GWouEak5dhu-Lmi5vXxre9tWFyfEVVxxMpPGSLUGcZLOAv-JeNWO0_w9OOnnzdb9V7Y-FnENTghuh6PX1Foek5nzE9xSQGFpvk6x0qeggUAsleE8EHGiF8Qu7EfjybaFvS1_RFwU_FOP4APVdzdyk0oDF_i7zQiLPIwfTNbTFaVbhlX6E_4nIkzOLERdgR6AKUqSyaeV7ceXuCZZg60FWnoNXcQstHGiEqhWuE2N9_eNHzSyJd_VT_aWKxQy4CWkL0c39zsGJReInEvnQjR9ICtQ6eFXnmKXRNNoEVeyLJmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن مرجانی، رئیس انجمن صنفی تولیدکنندگان شیرآلات ایران:
اگر این وضعیت اقتصادی دو ماه دیگ ادامه پیدا کنه
کل کارخانه‌های شیرآلات کاملا تعطیل میشن
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72679" target="_blank">📅 17:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72678">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ناو هواپیمابر USS George Washington  در حال انجام عملیات پرواز در آب‌های منطقه در خاورمیانه است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72678" target="_blank">📅 17:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72677">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c0fbd5c19.mp4?token=aBl4cFX8Li_Tg5_F3JeKshyr0ZYft3jiPuw5y4oUBDuO1eX-F7F9ZeWYdZkYKnWzeRqj7yVQFoqUZnOhqVd_Jchl_CRG2FLMLy24wXL8MJd1ctrh8LoFv6boMWZ0XFSiLeEZsr6hGxMEhClPZkzxLV4B4I2gegCh5_MK70gBGH2FATnNuPciqkn97NOr3WOVEsUI5yMrayAKa2DkY5d5hN1HuQEzY6CCwH-XZeO84mvHnRPos9YEVHuHSoZ0BVgDKRSF6TXlHgSRK3l9zq6MlArzA2pmvG8OMGW_Q_hEJvcg9ItGhMf5A_BpOgxaRZ69tJryg2qdHo9bi2cWrVJRNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c0fbd5c19.mp4?token=aBl4cFX8Li_Tg5_F3JeKshyr0ZYft3jiPuw5y4oUBDuO1eX-F7F9ZeWYdZkYKnWzeRqj7yVQFoqUZnOhqVd_Jchl_CRG2FLMLy24wXL8MJd1ctrh8LoFv6boMWZ0XFSiLeEZsr6hGxMEhClPZkzxLV4B4I2gegCh5_MK70gBGH2FATnNuPciqkn97NOr3WOVEsUI5yMrayAKa2DkY5d5hN1HuQEzY6CCwH-XZeO84mvHnRPos9YEVHuHSoZ0BVgDKRSF6TXlHgSRK3l9zq6MlArzA2pmvG8OMGW_Q_hEJvcg9ItGhMf5A_BpOgxaRZ69tJryg2qdHo9bi2cWrVJRNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛اسکات بسنت وزیر خزانه‌داری آمریکا:
برای نخستین بار در تاریخ — از زمان آغاز استخراج و صدور نفت(ایران) — آن‌ها در هفته جاری هیچ نفتی روی آب (در حال حمل‌ونقل دریایی) نخواهند داشت.
آن‌ها هیچ درآمدی نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72677" target="_blank">📅 16:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72676">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">صدای انفجاری از سمت دریا در قشم شنیده شد.  @News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72676" target="_blank">📅 16:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72674">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RqC7LtH4YdzKIf929vfVWOFLVb2-50kbdH3ckEDFwJvZg_eNZJYdXsCcWVoJGhenMz4RQ6RvbCmUNMQ-0V11_5aIMnsnWweEno-tTACaXMlDqQI8M3SCqZuhEilWbA96qsZxTcmJCCYBeBrH3Wta8R4AmDk2Qhn1YkuGFojk9Vuyp_w_YkZX1N0LNr9HY_Ih6gI6mtZAL-T89UeUF4rBozg9tK_YYGzcodr8sFaFEm111YrkfDFVi0AhAZicPZM_fnq62RcOMMwLqjs0dJjI9AJMnvQZIMCI0whpde-_WywdvzUoCFMW0oKFbSxXDCgQJzohXasd2-uR8UWRxPLTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FjPXaUpKp8LtL1k9l5lTbN1cFwZlnDclTB7wBQ6T4ElhvOEUmP8QCPioPcbwqfbVTp97j0KTsmzea7JA0wl8h-VeTJ35gHC38jyCv4eJFEzD9VwRoNm-wphmO4_7-ARKry5-0cGkVI50P8GIw83Lp_rqYQVYS25aYJT2ozRly39oIiH4lQ47aknmkTCvhD6hEMiD7hG4KflbXFWWzMqsbFMpcmMm-pw3ebuGd3OUztsczsyJJDi52VUHMPevpj4cy9hCo-h8TwUuyms4d94Sw07GC5_dbDvXQcH4DVbqKO1EAJRKdguMba5U02p2Y-OJ4m5eT2NMBbFj0P_Qk5A-Ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نمونه کار:)
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72674" target="_blank">📅 16:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72673">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noqDZLuwvftK6f6brQBiPZW28qvpeNOxDAjo1_KnnNrTXiX6k0JFxnSyLql1BxzAL1Y4aEgwxLDR1Jy80RUX8V7Q_mdl7zcN_6JFe2R17ivMrI44-dE8svPfTdWTS-Av7UF-PWk4dPl47aSf7O4ohUKubTo9FvUNRWjt1DV0kSyWbf8As8sr-2KFTgYEJLgD_-Z9DSjfaTRCoTlGsU5f0CkxLGNxx5ZMEcgBogzLbNvPgtjQfaX8sLx1NEFJU5u25PElNpwty0VUYhe_PutCPONiq3x4nEfGg4F-FYPAy5gwPxx45g2CsaiaCpzxxvN3Xr5CqmXa1XhkhJ6VpI41iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به دانشکده 05 کرمان
✌️
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72673" target="_blank">📅 16:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72672">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">#فوری
؛نتایج اولیه کنکور ۱۴۰۵ اعلام شد!
با ورود به پنل شخصی خود در سایت سنجش میتونید کارنامتون رو مشاهده کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72672" target="_blank">📅 15:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72671">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c967ea5781.mp4?token=Pr0kxTBH6y31H2YJ2g7yxM6vzUoQz13piLeSNkm2HrJXJCdtUjGyvm8g5hWg07pKMR4x2JzynPACwBxvXmVlgdKSBgNA_qQXA9E_3Iv_HdLPyJDUwPY-LO3soxUbVlxMtoXzOWO441Xjd0oGtNwZ5S10IJAuaXlgUEiWu8yR14mQWGbZG4M3pJ5OC9JeSJEO546InxJWT-v2P4EJeK3qGreIr8kpWeTKJObkRmoE4gu-BWyt7zWIPcIqqdqdmbnJx8s7RIkNau-tromEDLAUcEs8A-NF6Ob__0aIxizQjcvSHwZb1fQ2mwwoZ9JzbRpwrLY2VXVMeK9_-uyE6fzEHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c967ea5781.mp4?token=Pr0kxTBH6y31H2YJ2g7yxM6vzUoQz13piLeSNkm2HrJXJCdtUjGyvm8g5hWg07pKMR4x2JzynPACwBxvXmVlgdKSBgNA_qQXA9E_3Iv_HdLPyJDUwPY-LO3soxUbVlxMtoXzOWO441Xjd0oGtNwZ5S10IJAuaXlgUEiWu8yR14mQWGbZG4M3pJ5OC9JeSJEO546InxJWT-v2P4EJeK3qGreIr8kpWeTKJObkRmoE4gu-BWyt7zWIPcIqqdqdmbnJx8s7RIkNau-tromEDLAUcEs8A-NF6Ob__0aIxizQjcvSHwZb1fQ2mwwoZ9JzbRpwrLY2VXVMeK9_-uyE6fzEHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسنت، وزیر خزانه‌داری آمریکا:
ما از این مناقشه با ایران عبور خواهیم کرد. به گمانم عرضه نفت بهبود خواهد یافت و قیمت‌ها به‌مراتب پایین‌تر خواهند آمد.
روند افزایش دستمزدها ادامه خواهد داشت، چرا که شاهد رنسانس (احیای) بخش تولید هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72671" target="_blank">📅 15:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72670">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">صدای انفجاری از سمت دریا در قشم شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72670" target="_blank">📅 15:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72669">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2fafdeb0b.mp4?token=RuAtSkZa8it_PPIU40gXl161PnNV53YYTqSUknbEo-6GDZ5-qBSTnL0-p0SoXWdnjRR3uOhlN3-OPiSbCiYcKe3xj_EmEQpOK6cyVEnTSaJZRVhIP0z46qa3q2hGBhErsFo_Wotr_TM-PvADtZB7p9AcdxI4PiJsUrnCAk_lWIZ-63q_4dOsCVydluUj7lJBpSo7CuOcZ1fd9V8nuc8T9f3ZW7kOitwHWv9FBrKAVaCIMteAPw9OYIyIU8crtW2Qbh5aiwKIe-3hs2puLW1gxEV0XRHRLfAEFy8EPV3kwrwuiMSxtrk6709VB_xtYuie4Fh5TD6m1fXWAU05GcA7WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2fafdeb0b.mp4?token=RuAtSkZa8it_PPIU40gXl161PnNV53YYTqSUknbEo-6GDZ5-qBSTnL0-p0SoXWdnjRR3uOhlN3-OPiSbCiYcKe3xj_EmEQpOK6cyVEnTSaJZRVhIP0z46qa3q2hGBhErsFo_Wotr_TM-PvADtZB7p9AcdxI4PiJsUrnCAk_lWIZ-63q_4dOsCVydluUj7lJBpSo7CuOcZ1fd9V8nuc8T9f3ZW7kOitwHWv9FBrKAVaCIMteAPw9OYIyIU8crtW2Qbh5aiwKIe-3hs2puLW1gxEV0XRHRLfAEFy8EPV3kwrwuiMSxtrk6709VB_xtYuie4Fh5TD6m1fXWAU05GcA7WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واژگونی ترسناک کمپرسی بر اثر ترمز بریدن در کازرون
💔
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72669" target="_blank">📅 14:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72668">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پشماتون بریزه!
ایران‌اینترنشنال در گزارشی درباره مهدی نادری جهرمی، رئیس هیئت‌مدیره شرکت تهران‌اینترنت و مؤسس و مالک اپلیکیشن هف‌هشتاد، ادعاهایی جنجالی درباره ارتباط او با شبکه‌ای مرتبط با موساد مطرح کرده است.
نادری جهرمی با نمایش چهره‌ای کاملاً همسو با جمهوری اسلامی و حضور در ساختارهای اقتصادی و تجاری، به تدریج به موقعیت‌های حساس دسترسی پیدا کرده است.
ارتباطات و فعالیت‌های او در حوزه‌های بانکی و مخابراتی، در اختیار شبکه‌ای قرار گرفته که با عملیات موساد در ایران مرتبط بوده است؛ از جمله انتقال اطلاعات، شنود و نقش در برخی عملیات اسرائیل در ایران.
این گزارش بر پایه اسناد تجاری و قضایی، مکاتبات بانکی، قراردادهای شرکتی و روایت فردی با نام «کیا» تهیه شده که ایران‌اینترنشنال او را مأمور سابق موساد معرفی می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72668" target="_blank">📅 14:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72665">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7E-xT87udExeX_JQNZH1i8NdzY4nGQp9WX3BK6WXWC5n5UzYACruatZKSF70jIa7sD3nwfKXH1lKrR4cKSjZp4l42sqRr-vFzxbIjNaiHzVg2w_6IEEEMHID0RrG2Y9zxjRcOqavHCVkNIN4M8AfDcWjtw69ELl4Xf2-JfEpU_3kQ02stwAOGfR49IBie7kS1Ga4P4Ni0t4Z7EmwVHu0x95or54M8EaVVedxIUau7TbTPl8Re6E9UJye30fPfBcPqVeXNvJQdC6nj_3Ervl12fyZCOcNm72G0dciQckF27SVV1wy-zgjXs_9yx3NTXFfKCRRQZFTjXnzvnZAtp7pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1908d250d4.mp4?token=SxIIhy865q6jzWnuqV-Vkpzcme5q6RE8YTazH3SPP5n23tN37yN12Ps5sAkrlhhZrgJE6ln3cAB2eLHoxCBwJ0NkCiBH1HDATRa9yAgyW0ULeCywXiLfumgXtgTbLdAaJMlN_dEyWRIjyikT9O2WPtuLON9PkGTDm7OYsIjLSl6UzjczAV8o1cY2BslU8iGD15zRBWz09gNQemSu5pxO7_tlXLCaLdIY0jmb-sSpIg_RV4grZfjVKeJaqz_FcJZLgy84moxcjIjBrGoYZAzG5jeGmLSxFKyFy8eubFxR0pir0aWuBfotXEYkKCgYG3nAnn0rauITXD5X5Q1LjaXFlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1908d250d4.mp4?token=SxIIhy865q6jzWnuqV-Vkpzcme5q6RE8YTazH3SPP5n23tN37yN12Ps5sAkrlhhZrgJE6ln3cAB2eLHoxCBwJ0NkCiBH1HDATRa9yAgyW0ULeCywXiLfumgXtgTbLdAaJMlN_dEyWRIjyikT9O2WPtuLON9PkGTDm7OYsIjLSl6UzjczAV8o1cY2BslU8iGD15zRBWz09gNQemSu5pxO7_tlXLCaLdIY0jmb-sSpIg_RV4grZfjVKeJaqz_FcJZLgy84moxcjIjBrGoYZAzG5jeGmLSxFKyFy8eubFxR0pir0aWuBfotXEYkKCgYG3nAnn0rauITXD5X5Q1LjaXFlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هزاران دانش‌آموز دبیرستانی فرانسوی به دلیل کمبود معلم، ازدحام بیش از حد و ساختمان‌های در حال فروریختن، مدارس سراسر کشور را محاصره کردند.
@News_Hut
| Clash Report</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72665" target="_blank">📅 13:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72661">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b9ce8d805.mp4?token=CJWT24xuSobbtI1H7AqPAG04yKQiviA4vGT7xzbzXR71pQ8faz6iR8vAQUDBsP-MsHScZMRHq9GicWydn_OFGWnBR0Z8FJiumX1vndTLmGp1Prz4Spf8OZ0RJW0J8zZYyQa_jf7xTkySM5EN-F8I8Ggx2erXgfGI05IcP4Ot9AsZvPAH7I1yiyOAk3lNwN9MdtHedgaIEo9BFtCD3WKFPNPM1szMqN04QnXQNZoii1EmVPeP_jgiipCO0ljxdDt-NFf0zpmW4Zl4K0-kIrWfYRxTVck_n8fu5nf6tcRfowFLYDqsLSy6AHDXL6PXIZovAa3MhwTGvlce48oOBeinrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b9ce8d805.mp4?token=CJWT24xuSobbtI1H7AqPAG04yKQiviA4vGT7xzbzXR71pQ8faz6iR8vAQUDBsP-MsHScZMRHq9GicWydn_OFGWnBR0Z8FJiumX1vndTLmGp1Prz4Spf8OZ0RJW0J8zZYyQa_jf7xTkySM5EN-F8I8Ggx2erXgfGI05IcP4Ot9AsZvPAH7I1yiyOAk3lNwN9MdtHedgaIEo9BFtCD3WKFPNPM1szMqN04QnXQNZoii1EmVPeP_jgiipCO0ljxdDt-NFf0zpmW4Zl4K0-kIrWfYRxTVck_n8fu5nf6tcRfowFLYDqsLSy6AHDXL6PXIZovAa3MhwTGvlce48oOBeinrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از انبارهای نفتی آرامکو در ریاض که هدف حملات موشکی حوثی های یمن قرار گرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72661" target="_blank">📅 12:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72659">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LfwnYHkF26M8wxsfUQOk7PSRiNfAK9QJ5-CexAKnBvWxu1-tO1z9JB4sdGaPCSGM6wmKdfJtwD-d12liyBh8wPSCVrmeV1hWBSlucpOOFUUeCqxEPvAPAsdSlM2nS91-0zYMo-FVdEVszkI1YFhWGvsIHLzBbOX_PknnR8JUO3zQDTq9bLV1aEJJ3tdtUEUAlXwXKpCsQgBNXxrdmZlew-N1MbcB5GogBe9Z-Y8V03fiFXqk-7PMuB0fLS9ixeE9ZGeRM5TTG1CGRLJAFD8eEZUfylJmoWIkm7GVFHsB4svABdKoO1OPlYbZLUbkJTLcQ08CzQUXqUHbZFxRTrLHuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cc83c2d7b4.mp4?token=YqEU92EeelWleWkEg-RTshw5W9eqzwWECTFKSo7baYYZ2baJxaI6KtYDq2tpV78q6Y8YOeCNuM2Ox2AM1SH7Rf3Aq-JpyWV8mWqj7uW9f3vhHtzNiPIhB4GuZqLuVJHZveTagedjUot5Mp3Ew-oQ2LC1uoD-XBYHiDl9owhAs6tBLsWmTi00blMlhJHWP-DuAX8CoEhKJoCLcFXhgSbWoF0E_3RumkpAZDfCF1evdZQ-OWMEp0RtQ-8VPLXe6OWrVWmpfa4YXwzMOXdsfNKoDKayZtdb3cUbTZ3QUAjXCMUqtFAYclaomTsL4RdrvUfjNXzjOm7LXj73AltxiFeOwA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cc83c2d7b4.mp4?token=YqEU92EeelWleWkEg-RTshw5W9eqzwWECTFKSo7baYYZ2baJxaI6KtYDq2tpV78q6Y8YOeCNuM2Ox2AM1SH7Rf3Aq-JpyWV8mWqj7uW9f3vhHtzNiPIhB4GuZqLuVJHZveTagedjUot5Mp3Ew-oQ2LC1uoD-XBYHiDl9owhAs6tBLsWmTi00blMlhJHWP-DuAX8CoEhKJoCLcFXhgSbWoF0E_3RumkpAZDfCF1evdZQ-OWMEp0RtQ-8VPLXe6OWrVWmpfa4YXwzMOXdsfNKoDKayZtdb3cUbTZ3QUAjXCMUqtFAYclaomTsL4RdrvUfjNXzjOm7LXj73AltxiFeOwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی جنوبی ایالات متحده فیلمی از عملیات شناورهای جنگی آمریکایی Saronic Corsair نیروی دریایی ایالات متحده در پایگاه دریایی گوانتانامو بی، کوبا منتشر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72659" target="_blank">📅 12:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72658">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ:
باید با چه کسی طرف شوم.
کسی نیست که بتونم باهاش درباره ایران تعامل کنم. هیچ‌کس نمیخواد رئیس‌جمهور بشه.
من می‌پرسم: «در ایران با چه کسی صحبت کنم؟» تق‌تق(در میزنم)...اما کسی خونه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72658" target="_blank">📅 11:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72657">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72657" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72657" target="_blank">📅 11:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72656">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_QvEfIEqqFESvRLE6gcVHVry4qSlqjJ_GSSQaQzFNNngQ2xsv-XZkKKh5pBRQsh8g1gKSZprMPILNOOnidyKLwJkQ-tnXTGM0wzP4G3naCyoNiN837jMgiTCn6x2ykrhqmrJ3QzNJxKGFg9LUAk-9zq3uIzCNq7uliUwJZ-lXqfFG9oBr-1Eqik0SA4r7aLHaSi35CrJCkIrDUtm5P311SDGIUHoQNKziWtRWI47hzeeKGkyikL4-EuJyZ5VfO0mW0BuJhaWAeD3y9lvgnPnm1GS1jZLTX80j6R-aYhZKbfg7yC6FYCdxbM-aZOqOxJK4ebJheb6wIHVBdPw9t3nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
انگلیس
🆚
کرواسی
چک
🆚
اسپانیا
اسلوونی
🆚
سوئیس
لومتزانه
🆚
اینتر
یووه استابیا
🆚
لاتزیو
برزیل
🆚
هند
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72656" target="_blank">📅 11:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72655">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c533100ff9.mp4?token=YWoMhwPmHJu4z4pTvflhOSxjA3FrUMz712AoL2NQ_tgDYCXd5tPLPdIMm5NFGWah3e_uTCt1U3iqNNdoB3dfQ_tMOWfoCjMBDrzJfVlKD08XKUnTNHvMjIxTa8nMo4lSvGZ36fbjuLshqJBxx4O9VAUJtQONyPQXHoz7tkEirpoDRf3UfiRGHo0FOqbUKnDQpDJARSN1vxADf8C80eERR7meupYK3Oi5jrlG3QsgCj_AEAYkulotMXstSVGLuxSkHj-V9YSFvAodbW5cCQGiNkJkC7cLKUp0MXxQUOqbTEGMvGTC1snlElTrtPavlGw2gQuYr_lz_pU2gVT1-EjqoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c533100ff9.mp4?token=YWoMhwPmHJu4z4pTvflhOSxjA3FrUMz712AoL2NQ_tgDYCXd5tPLPdIMm5NFGWah3e_uTCt1U3iqNNdoB3dfQ_tMOWfoCjMBDrzJfVlKD08XKUnTNHvMjIxTa8nMo4lSvGZ36fbjuLshqJBxx4O9VAUJtQONyPQXHoz7tkEirpoDRf3UfiRGHo0FOqbUKnDQpDJARSN1vxADf8C80eERR7meupYK3Oi5jrlG3QsgCj_AEAYkulotMXstSVGLuxSkHj-V9YSFvAodbW5cCQGiNkJkC7cLKUp0MXxQUOqbTEGMvGTC1snlElTrtPavlGw2gQuYr_lz_pU2gVT1-EjqoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
گروهی از افراد را دیدم با عنوان «هم‌جنس‌گرایان حامی فلسطین». بیایید یک روز آن‌ها را برای مذاکره به آنجا بفرستیم.
دیگر هرگز آن‌ها را نخواهید دید. آنجا کارهایی با آنها می‌کنند که باورتان نمی‌شود
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72655" target="_blank">📅 11:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72654">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اسامی نفرات برتر آزمون سراسری ۱۴۰۵  @News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72654" target="_blank">📅 10:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72653">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVmdSLOIBDhz_1SyD4-s5sa0whxC5cckxQOZy1tSIQW1UEDVtRo28LYx0jJmiRrQFCDlhj-ooHZKJ2YIxs-9UWPaTHbQrX4I-ox1rr_qViCRAzh85cQ9C8HMl3Fhgi2NbMBgWXj6nHiYIBAGswkYg_6CZwSnXpL_Vs8WDwIIgj03KaJXaUQxAsuiOjEsWZEdksThxCD5_auH8_cVKNR1wIAa3vk8U_9KXcm32yH4Brv_Z7sng5myJehS0HBcVKMqXqbRic2OWHivQ3M_TR1So1u4j2BxesBGU538wxpFjLszLACkTyEgpsuhVqVSTcC0n-KbbK0wLEPE5tsJ_gNXVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسامی نفرات برتر آزمون سراسری ۱۴۰۵
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72653" target="_blank">📅 10:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72652">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نتایج کنکور سراسری برای عموم کنکوری ها فردا میاد!!
انتخاب رشته از دوشنبه ۱۳ مهر ماه تا ۱۶ مهر ماه ادامه خواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72652" target="_blank">📅 10:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72651">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIXKdBPy0kDoD6tNwzFqEVVYCDiDonvJfvhDA1SPsGloBl1i1J9AL2Z9yO_6r8kkWmWKvS4nFCrmPr5-Uuou3-0JOcjhHdZKnJ8LLKuB2nr2VUCtuyeV_hJbcr5Je-Sle_j1JBqVTZJcCnm5uZpZ4FM2rWZtwgVHbzEBdLA2Q5vTEq3eb8C2l4uAduQIQBxdfxY6lOyNj-VMCKplHDs6XuFj6X0keAoqwDQWYyWma3yTYLVEKUXvHSHr4QLZW0ImlM4GUUuHtIcA4afMa_UMTtIkf7PpwKLfSKL8AAw2YVibQKp4gp5HtyfLjeinNF3L43J4MA52cyAmBhzyr8AkAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست خبری سنجش تا دقایقی دیگر!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72651" target="_blank">📅 10:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72650">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qbe0Sxj8vn0mFPwWhwee6jWM56oa8G52KrvglFMN7qqp52PClm46cCLJeZOCnck9fVs3KQ_D2hhmBxX42PCV1LHlnN9R1-OZdavX5HvEFKXzl5cAz_-DHa7DepEJqN-TpMAlTIAMeT4RgHTSl1QsrOBalPnytqWHfTz04sj8czHJcn9FAhtzUbxTYb5LZKCn-dNnuxFsi5NGDfNYcxER_yWMarJyUEB0EZFI3NoalDf23SbO7QUjDjGc6rf1ERhRsEKtvKTbpCqGNV9t1_Nvh-VYtv-Dc57usvEBmPJHhZOhXnqo8r1VjsVcpX8ih8k-VFIDYYHePI1mtba3SgJ3Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛ اکسیوس به نقل از سه مقام آمریکایی:
مقامات ارشد کابینه ایالات متحده در «کمپ دیوید» مریلند گرد هم آمدند تا درباره گام‌های بعدی در قبال ایران و انصارالله گفتگو کنند.
یک مقام آمریکایی اظهار داشت که در این جلسه تصمیماتی اتخاذ شد یا دست‌کم بحث‌های عمیقی پیرامون این موضوعات صورت گرفت.
ریاست این نشست بر عهده «جی. دی. ونس»، معاون رئیس‌جمهور بود.
«مارکو روبیو» (وزیر امور خارجه)، «پیت هگسث» (وزیر جنگ)، ژنرال «دن کین» (رئیس ستاد مشترک ارتش)، «جان رتکلیف» (رئیس سیا) و «استیو ویتکاف» (نماینده ویژه در امور خاورمیانه) نیز در این جلسه حضور داشتند.
آخرین باری که نشستی مشابه برگزار شد، به ژوئن ۲۰۲۵ و پیش از آغاز «جنگ دوازده‌روزه» توسط اسرائیل بازمی‌گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72650" target="_blank">📅 10:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72649">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f04d52dbe.mp4?token=CdeR419k_YvQKvCD7Y5ON34ABYcqq486_NAR4YefMYY9uvtyHbJUePvAHB2OPCd9c-8yM2_DSm4p7m_6ZHm1KOqMZ42zY23MpSwMPaghu4Rao8w0_jScIyaUvUyZa17T0SG-sF8MMkOTpv230Ooto02laNZlk1KzSetpxpdVV2OYzvQmo9-REuHGpfgLs9kVziftJD8fcLvXeBWPP_qnGsxIPSUsIZSeJoiEq6tXpKCmOybPgopcgYDWCTckMvwpzHMSLRYD_8Y05qAfNG6Ug-vrgcFAY7_L9PS0UsUgSxaDnFPOt2EQKorL7SZLdDhFopWJdTnT7_aNi_aVqE7dkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f04d52dbe.mp4?token=CdeR419k_YvQKvCD7Y5ON34ABYcqq486_NAR4YefMYY9uvtyHbJUePvAHB2OPCd9c-8yM2_DSm4p7m_6ZHm1KOqMZ42zY23MpSwMPaghu4Rao8w0_jScIyaUvUyZa17T0SG-sF8MMkOTpv230Ooto02laNZlk1KzSetpxpdVV2OYzvQmo9-REuHGpfgLs9kVziftJD8fcLvXeBWPP_qnGsxIPSUsIZSeJoiEq6tXpKCmOybPgopcgYDWCTckMvwpzHMSLRYD_8Y05qAfNG6Ug-vrgcFAY7_L9PS0UsUgSxaDnFPOt2EQKorL7SZLdDhFopWJdTnT7_aNi_aVqE7dkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ربات‌های چینی با لباس‌های سنتی عربستان، برای شهردار ریاض و سفیر چین رقص محلی اجرا می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72649" target="_blank">📅 09:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72648">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBg4JUwVDfToy1kBNCL4KwYkvdV2YSqQSusaYSF5mWCmn0SVPj84KVXXgw9vaWqGI5bn-FxJCUo_NTXrhQ0vxT0EFGPNJy7khJixUk4F8lJBrvQpDakx6xfAXLhU6avhT2fno85n1h5oxk61luZO2uuJuoiJdUrgdwh_8jX8H1sityj9LUKOzyG6OYmqJVril6MAoFK5TqK69sU2Pa5LebMaf-bLxprIKTTgdPabV3X2BKFArB3vk1oH0Kd6ivDCDqBXloiAh6d_ONbjb5WK7d2bbiyQL-kz4Dug3T-pvI4BsW6ClXz9b-QfS-2CjzEUV4Shg7rG--aXdizQixpfyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «ای‌بی‌سی نیوز»، کمک‌خلبان شرکت «فلای‌دبی» که به خلبان حمله کرد و قصد داشت پرواز شماره ۱۰۷۳ این شرکت به مقصد اسرائیل را ساقط کند، «همام الحمامی»، تبعه ۲۹ ساله اهل عمان شناسایی شده است؛ او اذعان کرده که قصد داشته هواپیما را در اسرائیل سرنگون کند.
الحمامی در سال ۲۰۲۴، در دوران آموزش در شرکت «عمان‌ایر»، پس از کشف مطالب افراط‌گرایانه نزد وی، از پرواز تعلیق شده بود اما همچنان در سمتی اداری به همکاری با این شرکت هواپیمایی ادامه داد.
بازرسان در حال بررسی چگونگی صدور مجوز پرواز برای او در شرکت «فلای‌دبی» و تعیین وی برای مسیر پروازی اسرائیل هستند.
الحمامی با بازرسان در امارات متحده عربی همکاری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72648" target="_blank">📅 07:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72647">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knFjMBy-oKXJ-by947z4pFrDNps1FgVDXhuGnex890nB7eFJ2s8oQR2Q0rcuJup12oqzRqJ8COqZ94PE9K3j5z29AYxeY4FPHJ2HjuvUSWn7d-AkOnmodjyxozhMMKBHFIPv3JojSWV4EIQSmi104LSaPLm4iK3HenFqVcJW-mIzlD7WSL9OmeornO2VMrClr3tqBilCiXEMgM7tjXCLCz-xCcPNhl4mpIVeRVqtwUc2HUVWV1RWRdLSkCA8Gav-FpHe7PbC_JBe8jb-4j2A_IF_HomSui_95G8drWnQl6mWLJnddYeOizuf6-N3Tz2vaVKRWFNL0EkLzP-jLsxjUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار: گام بعدی شما در قبال ایران چیست؟  ترامپ: خب، اگر به شما بگویم، خبر بزرگی برایتان می‌شود، مگر نه؟ اما خواهید دید؛ اوضاع دارد خیلی خوب پیش می‌رود. وضعیت ایران خوب نیست.  @News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/72647" target="_blank">📅 06:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72646">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72646" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72646" target="_blank">📅 01:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72645">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DK6uDySHWzJbn_zFlOlTXHdP8RXH3rCAXwRcPeFEq7422Nc5Fww6fkTuUTANcY7x7Z4XTiUClDHnDSE32aAZ6WMvhBpBxsHJBTZs2ParIRY8HIaWwEBTD_oHPWyqdZx4R4XdoYjjzzoL-N21iXs9YXyRFnA2p59u5yuWt__WKES8b_VxrtXSFk2_xoCs7Fuvr5fsX4-tFOjeeqiPT3ndD9pHnBYNv4o2vZot744SM1FTK_rBj5srImUR87IldGA3IhCoqqwqjfwXIisHWtJvh2joG8s0XR9h3gdmh9ElfCGMX8liZvspmakyZFHaKb-U1wqDxvMCqquWl6-8zzhENg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
شماره معکوس تا رویارویی بزرگ
​
🦖
دیوسون فیگاردو در مقابل پیتون تالبوت
🦖
تجربه اسطوره یا طوفان پدیده جوان؟
​هیجان واقعی و پیش‌بینی بالاترین ضریب‌ها در
TrexBet
!
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/72645" target="_blank">📅 01:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72644">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b49a7f3128.mp4?token=PeEwjHD00PnVTxrh1fDtLvyui91bDJC5Mhe5Nt8XtNWKvrRSufgo4Igq6PqDI7Qw0HgvusUIH0CX5aLdtz3Vw0DoSbNRBA-EI0V3Uya2SeK5BstLHQvlNmw6kjUKiojegV6wICS0DTelHIwBWQYNwRLzBY9xFsAjdFaFaH-ZU8JVWrkgNGfc7gGfn3sUqBnVAJP_KEu3L_rZIPbSmmboK13ykUdMxN4HpdkUPqp5KnrY7TRpZRDLqFq2P8xqz9JUUGgpsZGPCFuyCVRgsiAmECYlV8ZOYd5-uN9Quljx2EFLcmL1NldQ-9Hh1J4_g0o_GAjZxxdvmCBKSvf_XSZMng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b49a7f3128.mp4?token=PeEwjHD00PnVTxrh1fDtLvyui91bDJC5Mhe5Nt8XtNWKvrRSufgo4Igq6PqDI7Qw0HgvusUIH0CX5aLdtz3Vw0DoSbNRBA-EI0V3Uya2SeK5BstLHQvlNmw6kjUKiojegV6wICS0DTelHIwBWQYNwRLzBY9xFsAjdFaFaH-ZU8JVWrkgNGfc7gGfn3sUqBnVAJP_KEu3L_rZIPbSmmboK13ykUdMxN4HpdkUPqp5KnrY7TRpZRDLqFq2P8xqz9JUUGgpsZGPCFuyCVRgsiAmECYlV8ZOYd5-uN9Quljx2EFLcmL1NldQ-9Hh1J4_g0o_GAjZxxdvmCBKSvf_XSZMng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: گام بعدی شما در قبال ایران چیست؟
ترامپ: خب، اگر به شما بگویم، خبر بزرگی برایتان می‌شود، مگر نه؟ اما خواهید دید؛
اوضاع دارد خیلی خوب پیش می‌رود. وضعیت ایران خوب نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/72644" target="_blank">📅 00:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72643">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ساعاتی پس از معرفی رتبه‌های برتر، کارنامه داوطلبین برروی پنل شخصی هر داوطلب در سایت سنجش قرار خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/72643" target="_blank">📅 23:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72642">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">طبق گفته حسن‌پور خبرنگار خبرگزاری فارس، فردا در نشست خبری رئیس سازمان سنجش رتبه‌های برتر کنکور ۱۴۰۵ معرفی خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/72642" target="_blank">📅 23:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72641">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d476b5a95.mp4?token=LmKVvx5bQjlpK2XNRqEdBI3qpKDojaZFpzZbuxqkTq6GelQ9si5yTGn6MC91Y7Kl5evoSEDObmJXbwfDZHFV_vknEjqrVFDObJf5-KG4qe7Ya0t2gn4WZCpGoQQt6fS5AX22rMd1Gxii7o5_Efo2Rlb1PbKT-V-wljM-aKSyzPoEVsaINniS0UPgob_bv83jNwB9mqzWAtrE3gtMsztHRUcHvVbwhyc3-Qvj8ItBnh43nrYOVftANYga8cSVnnjjv9_Z0-J6jYZAD9Ikb6Ei-aodUmxglZtoncb2WXZ6ZYHI0AOjGg2V-Zu6ulYAKpK7zcXpzx_FPe1fX66o7P6Oog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d476b5a95.mp4?token=LmKVvx5bQjlpK2XNRqEdBI3qpKDojaZFpzZbuxqkTq6GelQ9si5yTGn6MC91Y7Kl5evoSEDObmJXbwfDZHFV_vknEjqrVFDObJf5-KG4qe7Ya0t2gn4WZCpGoQQt6fS5AX22rMd1Gxii7o5_Efo2Rlb1PbKT-V-wljM-aKSyzPoEVsaINniS0UPgob_bv83jNwB9mqzWAtrE3gtMsztHRUcHvVbwhyc3-Qvj8ItBnh43nrYOVftANYga8cSVnnjjv9_Z0-J6jYZAD9Ikb6Ei-aodUmxglZtoncb2WXZ6ZYHI0AOjGg2V-Zu6ulYAKpK7zcXpzx_FPe1fX66o7P6Oog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر گوگل‌ارث با مقایسه وضعیت در ماه‌های مه ۲۰۲۲ و ۲۰۲۶، ابعاد ویرانی در اطراف مدرسه «القادسیه» در رفح (واقع در نوار غزه) را نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/72641" target="_blank">📅 23:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72640">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f0ca8354.mp4?token=njIf_hLwRiP8kMx754ZW2AZOrKYHOEPK7AlzzJa4-lIl8YiJcWVWxrtrQn3e4MkWb7yeXFukiUxyq5mOhKEUIr4iE9PH4dOQn-f4Vs3i5LeqbpJQBpeJHsT4zi88Hb-VqwLaY4JXmDxAOxNRz9NrXWPFvCa2qD0hiw9Wy5GMwzmTp1HpRepSTALmtRt7tV4IJ4GXDPWNY5Lz1qVhH_zl7AG9ySOUuFLxsj6tBHMhRwsYdJVh37ILIFGFXPGJTeeO1KJ9rPUO2s_dNKrVXCilCSXgdf_uE-4E5bV9_-2rlRRp5YzQgfaEeW_2e5IYYzX-pwkiAiMhsc-SueP2CUrSHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f0ca8354.mp4?token=njIf_hLwRiP8kMx754ZW2AZOrKYHOEPK7AlzzJa4-lIl8YiJcWVWxrtrQn3e4MkWb7yeXFukiUxyq5mOhKEUIr4iE9PH4dOQn-f4Vs3i5LeqbpJQBpeJHsT4zi88Hb-VqwLaY4JXmDxAOxNRz9NrXWPFvCa2qD0hiw9Wy5GMwzmTp1HpRepSTALmtRt7tV4IJ4GXDPWNY5Lz1qVhH_zl7AG9ySOUuFLxsj6tBHMhRwsYdJVh37ILIFGFXPGJTeeO1KJ9rPUO2s_dNKrVXCilCSXgdf_uE-4E5bV9_-2rlRRp5YzQgfaEeW_2e5IYYzX-pwkiAiMhsc-SueP2CUrSHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این خانم میخواسته بره مهمونی و لباس درست درمون نداشت؛
اومد تصمیم گرفت یکی گرون ترین لباس‌های آنلاین شاپ که بالای
۱۰ میلیون
بود رو سفارش داد.
حالا چیزی که به دستش رسیده :
میگه این چیه لامصب؛ من با این برم مهمونی میگن خرم سلطان اومده
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/72640" target="_blank">📅 22:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72639">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62412d8d06.mp4?token=OMDbMDw8swE_lzUzI7j31PErrDqTCmIwcku_UlsnNMIasJMzpP_PpKFAzf65NHkhU4F4hvhj9FDLqyUorlP0eYJCnouCMb0WIPGJ9ecnyL4ymoy7vBEmNyCl7rr95RlAFGVTEj3VgAK1kOpjCDl-ZpIFTSTikWsFx0EPoakZxptm4LEhlJxSC_g55k4r2Rdp0KGWhmB2UJCBpdkc1OtgJFsBDXkZszEaq4d4IGRtVDXZZo4QdsRJOWVJeGuAH0XZ7WOF_Pa0qNuDBaDZvq22dCaYknFMUfCD_9CQ6dBWpLfpN07JFN-98Xs8Qu3_gJqygn6dyXwm59G2UkbCO3i6bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62412d8d06.mp4?token=OMDbMDw8swE_lzUzI7j31PErrDqTCmIwcku_UlsnNMIasJMzpP_PpKFAzf65NHkhU4F4hvhj9FDLqyUorlP0eYJCnouCMb0WIPGJ9ecnyL4ymoy7vBEmNyCl7rr95RlAFGVTEj3VgAK1kOpjCDl-ZpIFTSTikWsFx0EPoakZxptm4LEhlJxSC_g55k4r2Rdp0KGWhmB2UJCBpdkc1OtgJFsBDXkZszEaq4d4IGRtVDXZZo4QdsRJOWVJeGuAH0XZ7WOF_Pa0qNuDBaDZvq22dCaYknFMUfCD_9CQ6dBWpLfpN07JFN-98Xs8Qu3_gJqygn6dyXwm59G2UkbCO3i6bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسره سر صبح رفته گوشی داداش ۱۱ سالشو چک کنه که میره تو پیامکا و با همچین شاهکاری روبرو میشه:
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/72639" target="_blank">📅 21:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72638">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ufYDJOq5zegYup03QiBen8_oEdJVtIZKFHeJYRuewdrMTnJK1redOX53x-zzArik4tceRNsASz5EXlnnKIPTzrINvmDzc9pxyPKYguFPuIkcE_k-xnVMT7hv9d6QB5JME8FFjSQAEuY54i9mkmKOsbwfzI7nNCfw_x_pnVRQoQoNC5-jOQD0t4cJlp_hpVKpxM0eSKd0QalNW9n48uFoxv99mqm4KKU9c6At5UeLIO0PGEQHpt-Um9NC4cCdG0HrkxIHaimNQcKLxhvmNyQgUV-vutqCDHvYxk-SwoLzNuDHLBXex1GSYkCvRaQXeCoHKuU621v5bTclQVi6NnnMmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد که ناخدای یک نفت‌کش گزارش داده است این شناور هنگام عبور از تنگه هرمز مورد اصابت یک پرتابه قرار گرفته است.
در پی این حادثه، آتش‌سوزی مختصری رخ داد و برق کشتی برای مدت کوتاهی قطع شد؛ با این حال، آتش خاموش شده و شناور به مسیر خود ادامه می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/72638" target="_blank">📅 20:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72637">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دلار 265
😑
#hjAly</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/72637" target="_blank">📅 20:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72636">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دلار 265
😑
#hjAly</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/72636" target="_blank">📅 20:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72635">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd07c4e807.mp4?token=n-lDhkha4lWo-OA7ChUT81nY4Ya3is4S5KqfmgPHSJ4aSGWxmYU2VwCOgUIEvrEvscwzDaabuEQQmUE0g8qcuZXpmSEniY555xbPP08Qt1JtbCEB254fiXBUZjI1XSSfi7yXqQyqOUKaJkH8A-Gp9T8fpd5gA5hdsku70tReZtfObGuWK6ArmXpMUhVupOHmPAXVny71KhB2DOSWqlkk8jZkfbxdwoyqR5epE7YwZDCgE0BYz7KeleSNRqup0ahTa-6D0xAa5ScO0oDDJYCYrAZUyUTQQeF6SR-J8By2yRbEebwlC9yv8EU5g0iYBqM_hswf4zKmke74RXgyxPU9Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd07c4e807.mp4?token=n-lDhkha4lWo-OA7ChUT81nY4Ya3is4S5KqfmgPHSJ4aSGWxmYU2VwCOgUIEvrEvscwzDaabuEQQmUE0g8qcuZXpmSEniY555xbPP08Qt1JtbCEB254fiXBUZjI1XSSfi7yXqQyqOUKaJkH8A-Gp9T8fpd5gA5hdsku70tReZtfObGuWK6ArmXpMUhVupOHmPAXVny71KhB2DOSWqlkk8jZkfbxdwoyqR5epE7YwZDCgE0BYz7KeleSNRqup0ahTa-6D0xAa5ScO0oDDJYCYrAZUyUTQQeF6SR-J8By2yRbEebwlC9yv8EU5g0iYBqM_hswf4zKmke74RXgyxPU9Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش تاییده خیالت جمع برو بگیرش.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/72635" target="_blank">📅 20:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72634">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">شبکه سه اومد بازی جودکار ایرانو تو مسابقات آسیایی رو پخش کنه که جودکار ایرانی تو ثانیه اول بازیو باخت و حذف شد و گزارشگر اومد سلام کنه خداحافظی کرد
😂
😂
😂
@HutNewsPlus</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/72634" target="_blank">📅 20:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72633">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">عراق اعلام کرد که مجوز معافیتی برای انجام روزانه ۴۰ پرواز توسط شرکت‌های هواپیمایی ایرانی (به‌جز هواپیمایی ماهان) به مقصد فرودگاه نجف و بالعکس دریافت کرده است.
هدف از این معافیت، تسهیل سفر مسافران و تأمین نیازهای بشردوستانه و پزشکی است.
نخست‌وزیر عراق از دولت آمریکا بابت موافقت با این معافیتِ درخواستی تشکر کرد.
@News_Hut
| Clash Report</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/72633" target="_blank">📅 19:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72632">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2fb6f9cd.mp4?token=lI9ug24VSIVSMHn7L23dF1rcR45_QE-UaraniWu95Pq7mjEnR6LVOQr-UspvyBC4CATedGBXSiFUF0SKHxwpeXQrOYmSGrWn11Osw-FJ11umx8X7BzCP1iCv6ab72PoPtPkd0NIU_M-wZN-gC9lrzlq36zs8jjTeFUksnTWIkQ3kKKh5251JqaVmYd2eKkSFd76EO2qaC_f4682BFbmaDXwFTvFhFr9vT9s9Y1_BLDDJe7y7CPoPpxtdVzQFRrFRrcF_1BIRbIlkDANOvj-pl7NspFFRnKU81DMA3Wo7DBVORa3Dy6vZ5bH7ysVnGGgakH-ZMj2uG_D3E0RDs-t5CFLQCX1prW_KBSrbSQQO_XecWrmFHXAVpF4JAF-VWx0D5lrfTgqXOnOh6F1OuzH8n8fl5FXgzagmjecCtk3sEYw6LUUkwHcUl0LiJJkYINy3pPG6mF2gGHNyzSC0R9g_kK_aPBI8qDTUDPPLZdXS5QluqRVkIe0YHyx7Gn3vXCB7mFtgRQpL4ipAUvkxcJT6BJjZbcwV9T-N9ZN8Bo2fKKZ4gVVKeymsXWiOOIoCCefihQaT7C7D31hSCcPkXdxBNBGSk54Adx615NVMWWJCBWUHTdazdVpBPiOTZbFda5Qo6IZOFLm9_0EtdExZVyBW-gS0w2HrkirT4Tv6aR17vHY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2fb6f9cd.mp4?token=lI9ug24VSIVSMHn7L23dF1rcR45_QE-UaraniWu95Pq7mjEnR6LVOQr-UspvyBC4CATedGBXSiFUF0SKHxwpeXQrOYmSGrWn11Osw-FJ11umx8X7BzCP1iCv6ab72PoPtPkd0NIU_M-wZN-gC9lrzlq36zs8jjTeFUksnTWIkQ3kKKh5251JqaVmYd2eKkSFd76EO2qaC_f4682BFbmaDXwFTvFhFr9vT9s9Y1_BLDDJe7y7CPoPpxtdVzQFRrFRrcF_1BIRbIlkDANOvj-pl7NspFFRnKU81DMA3Wo7DBVORa3Dy6vZ5bH7ysVnGGgakH-ZMj2uG_D3E0RDs-t5CFLQCX1prW_KBSrbSQQO_XecWrmFHXAVpF4JAF-VWx0D5lrfTgqXOnOh6F1OuzH8n8fl5FXgzagmjecCtk3sEYw6LUUkwHcUl0LiJJkYINy3pPG6mF2gGHNyzSC0R9g_kK_aPBI8qDTUDPPLZdXS5QluqRVkIe0YHyx7Gn3vXCB7mFtgRQpL4ipAUvkxcJT6BJjZbcwV9T-N9ZN8Bo2fKKZ4gVVKeymsXWiOOIoCCefihQaT7C7D31hSCcPkXdxBNBGSk54Adx615NVMWWJCBWUHTdazdVpBPiOTZbFda5Qo6IZOFLm9_0EtdExZVyBW-gS0w2HrkirT4Tv6aR17vHY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تایوان نخستین محموله شامل دو فروند از ۶۶ فروند جنگنده جدید F-16V Block 70 را که در سال ۲۰۱۹ به ایالات متحده سفارش داده بود، تحویل گرفت؛ تحویلی که پس از ماه‌ها تأخیر — که تا حدی ناشی از مشکلات نرم‌افزاری بود — صورت گرفت.
این قرارداد ۸ میلیارد دلاری، شمار ناوگان جنگنده‌های F-16 تایوان را به بیش از ۲۰۰ فروند می‌رساند.
وزیر دفاع تایوان اعلام کرد که انتظار می‌رود پیش از پایان سال ۲۰۲۶، تعداد بیشتری از این جنگنده‌های F-16V تحویل داده شوند.
@News_Hut
| Reuters</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/72632" target="_blank">📅 19:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72631">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgYlSYMPdYGUtH5TINC1wbbVTKXqr9ba1I53117L9VyoeDpZKcdL2GkheBQYLD_oeGi-umznwI2khkbFAqJ4I_nSlxgWFHb--79YuryWU8sqjs8CiaFyZVEna2R-XatCTCWCosMPdWVVJmt_r7k2A4aSFIRak6RnKfCn8gRF16nCjU3rmHnKLmEqgrhqrcQNewGJt6ZfJxLiKFBgpjVtzXwHSzyigC9MW50OHueL9xlH2FAmBnBs592sUdyVYWska8F5v8cLXVm4iGOLT7D6VRRPbTjbqnHon71m2ZeNxe_k_zoG_egq13bpZV1SJGeNrdU64bvABA4jodSKScWzTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «اکسیوس»، با وجود اینکه هم دولت ترامپ و هم تهران علناً اعلام کرده‌اند که خواهان پایان دیپلماتیک مناقشه هستند، دیپلماسی میان ایالات متحده و ایران همچنان در بن‌بست قرار دارد.
رویکرد دو طرف نسبت به مذاکرات، تفاوت‌های بنیادینی با یکدیگر دارد.
ترامپ خواهان دستیابی به توافقی سریع، پرسر و صدا و احتمالاً فراگیر است؛ در حالی که ایران مذاکرات طولانی‌مدت و غیرمستقیم با تمرکز بر ترتیبات محدودتر را ترجیح می‌دهد.
بی‌اعتمادی عمیق نیز بر پیچیدگی‌های این روند دیپلماتیک افزوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72631" target="_blank">📅 18:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72630">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ در تروث:
اروپا به‌تازگی موافقت کرده است که حجم عظیمی از ذخایر کلان گازوئیل خود را آزاد کند.
این فرایند بلافاصله آغاز خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72630" target="_blank">📅 17:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72629">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd453b2fe8.mp4?token=GT-3bV_Of39WGGdU4_lqL106cojZEydYtiKP4m9lSawCgj0fGNdC_OYRjc8clZ3v0_DLNKjalXsLgg3edjgb1tHVWpKRNpTxo440JZgwLfJH680JqheKe9adJdfOH0X1hmX9TuITgVcXfN4Lv9klPkzRCqxbGqb_eLa2ETr_UCWN4ZOVyfNC38MIsdvK3Q3e6BYbtY_ZPG4EM4OEwJqju-_S1xmlnR-i_y93GKCE5sHDJg-I8KQ3NZCcqS06IopmmLAQQRhkqBQ-dRskc_yghR6KuDMvPt2Z5bo_pIKH8ExxRcsonLykuvSyaYwWiEM0GzltGW3h4ludZ0QXU6zAlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd453b2fe8.mp4?token=GT-3bV_Of39WGGdU4_lqL106cojZEydYtiKP4m9lSawCgj0fGNdC_OYRjc8clZ3v0_DLNKjalXsLgg3edjgb1tHVWpKRNpTxo440JZgwLfJH680JqheKe9adJdfOH0X1hmX9TuITgVcXfN4Lv9klPkzRCqxbGqb_eLa2ETr_UCWN4ZOVyfNC38MIsdvK3Q3e6BYbtY_ZPG4EM4OEwJqju-_S1xmlnR-i_y93GKCE5sHDJg-I8KQ3NZCcqS06IopmmLAQQRhkqBQ-dRskc_yghR6KuDMvPt2Z5bo_pIKH8ExxRcsonLykuvSyaYwWiEM0GzltGW3h4ludZ0QXU6zAlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر لینک کلاس مجازیشو میده به دوس پسرش و پسره هم با دارودسته رفیقاش میپرن توی کلاس و همچین صحنه ای رو رقم میزنن؛
این وسط یه کاربر با نام عباس عراقچی هم دیده میشه:))
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72629" target="_blank">📅 17:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72628">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72628" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72628" target="_blank">📅 17:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72627">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzJbcVkbRBSKXtvuCTcY4VPqayQypLj1w6uHUVlYpL8HNPUpyuUv-0Y2w2FVMP8xaDDflwRcUba9rQMhU_bUSp0EBmI7tj8QdioJgnBXmRDRwcg7Ed0KjxPLtshpcoUCm0c0KdBPrQZjHewvJ4b_h1PZOoeq9vj89nz5NW-q3v8TT_V5_6_RT0xyTwgzbIVybG187vvoaVcQ8TZmpnBf_KYAaqQU79cj7AmmRETYD74Sai5hRThXlM9jJ3dKt3nxPKZTsCFsfya66HCA_LXR5dcrwwjfcjNhrpTGdkNo-AtZbtBd0uKbbPgR4SJBcZ-TsXoefCtkmtwtyybmhklHdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز ایتالیا
🆚
فرانسه
را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
ایتالیا: ۳ برد، ۱ تساوی، ۱ شکست و ۷ گل زده
فرانسه: ۳ برد، ۲ شکست و ۸ گل زده
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72627" target="_blank">📅 17:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72626">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11e067ea31.mp4?token=Rtskex9n8No_wF8MAfLmwJ2n0svRmdhs6cVhh_GRo3gMsSuIX80iDvn1cL-R0nsLPISkRegmlF2c5-Ask8_9tSqAtRK-32i_MgJ73gYvYy5fHt0RwR4CKSAA2zLYm3ouxY03XhdVyY4Ox7XfDzbnQh9xZQ3pJAG1JiKZMBWMvE9Ngpb8GY8VT2lKSg9z0IHMUsmpI6PRy-ZZva80jL5pXX3NgWsAAtP1gVj05in6RIm_hAUyN5q_7f8ra7bbnzDQGiqTM0b21jK2EndlCCxKLyY2hhPnStSECo2_5lAdKuOVEtZgNLAKgpJT7GSFp2CoVYafIqmnO9G-vcdc4AJjzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11e067ea31.mp4?token=Rtskex9n8No_wF8MAfLmwJ2n0svRmdhs6cVhh_GRo3gMsSuIX80iDvn1cL-R0nsLPISkRegmlF2c5-Ask8_9tSqAtRK-32i_MgJ73gYvYy5fHt0RwR4CKSAA2zLYm3ouxY03XhdVyY4Ox7XfDzbnQh9xZQ3pJAG1JiKZMBWMvE9Ngpb8GY8VT2lKSg9z0IHMUsmpI6PRy-ZZva80jL5pXX3NgWsAAtP1gVj05in6RIm_hAUyN5q_7f8ra7bbnzDQGiqTM0b21jK2EndlCCxKLyY2hhPnStSECo2_5lAdKuOVEtZgNLAKgpJT7GSFp2CoVYafIqmnO9G-vcdc4AJjzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احمد مجدزاده: آقای پزشکیان این اخطار آخره، اگه استعفا ندی، استعفات میدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72626" target="_blank">📅 17:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72625">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad77de0b54.mp4?token=XskCbJkqLu7rvCC7_oXta3hhAQ7Kfu9gsVxGayMse06tnootDGKAyEqfLmcpzyu9YCvi3_WifUjlkaPQYSsr6DVUp1qZNubhmzeHJpYbtqZe68_9ZIJkmEvXPePr6hwz0yVm5XN_kmBkaKyR-f_pVqJay1JXxPtDIzQeinbjWsGj_sNQe4_SpSMtbBnZIyhwm5Bs3ibNwegpjjCmr2jWM8RBh3NgF_JMchnesRRzm9mksKEYNIq3FkcJh9VcDcq0U_cyr3jHl0C-7Ua51jLAt_4-M3SLiczDdkBUm5P6-BpjIp2XAw3kU9SRVwd26_dIA2DCzJ2FFisyZYoEQQPpVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad77de0b54.mp4?token=XskCbJkqLu7rvCC7_oXta3hhAQ7Kfu9gsVxGayMse06tnootDGKAyEqfLmcpzyu9YCvi3_WifUjlkaPQYSsr6DVUp1qZNubhmzeHJpYbtqZe68_9ZIJkmEvXPePr6hwz0yVm5XN_kmBkaKyR-f_pVqJay1JXxPtDIzQeinbjWsGj_sNQe4_SpSMtbBnZIyhwm5Bs3ibNwegpjjCmr2jWM8RBh3NgF_JMchnesRRzm9mksKEYNIq3FkcJh9VcDcq0U_cyr3jHl0C-7Ua51jLAt_4-M3SLiczDdkBUm5P6-BpjIp2XAw3kU9SRVwd26_dIA2DCzJ2FFisyZYoEQQPpVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از بانوان پولدار تهرانی که میرن توی یه سری کلاس ها شرکت میکنن پول میدن تا برن اونجا گریه کنن و تخلیه بشن.
یسری انقدر پولدارن که نمیدونن پولاشونو چیکار کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72625" target="_blank">📅 16:30 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
