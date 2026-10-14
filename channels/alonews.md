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
<img src="https://cdn4.telesco.pe/file/Ppy3EHLeWhiRw0rxmolyCmCjQ8N-XykUMzUd-YWpq1hWFjvhnzKgoUEyT87hPRAKIN4cEe3_c_P0yiGdLCo6BCObs-xiI9xpHwB_FU8-z2cHb9VLWEJTHnndvED2aS3BbXwDMJy-SOr53xmW_oDzl5l7vhw3uN0IaQFnxMKcrWLNs2jNzUDQJZKqE5BBRWYrZWD1jA42HU4NRM2T_XaqB_APMoHG7LKuAKixq5BC8rYJ60HlE7dfX72t1Uc0RiMpnpQ3kk7u0_7xhFiwN7XpVHqudriRde93O5Sjph_qzr0JO9lYlUuZwJXwZ9crREuSHNq8R7HREQnsy_fn6J9Kvg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-23 01:19:55</div>
<hr>

<div class="tg-post" id="msg-152741">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZFe9dCXu_qlegC_EQDbRjOcYzbI3UckdgQz_4Vq5_dWH7OXoAw4s0MZ3fLllWUMYKjUfWkEgGubyyo0Dt5kj8mJm9L2wAanG76OBkWmUpuvGS_45q1Uccx_svshUqAWcGltm3X48un13ei8elOxuJV58jLsgZcbDSKAvXe2xcxNGLmj3gHkDkf3mtwYvGY2QGy9uSTQBEaeHLh89-_pRdQj__8Rq9ubSIZcItF4tdSjmK5qkr-BiqLmne2Gi_8bRTAMWn3v6XC_qzKi6YIRq7KiIuRY8vq70GQLheT5wDjyyzmpkI45quUUGfGt914FAs6WzIcwVhwbgkwv-H_Hsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو صحبت کاملا متضاد
🔴
سیدعلی خامنه‌ای چندسال قبل: جنگ نخواهد شد و مذاکره نخواهیم کرد
🔴
قالیباف امروز: هم مذاکره میکنیم هم جنگ میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/alonews/152741" target="_blank">📅 01:13 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152740">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
امریکا به کشورهای حاشیه خلیج فارس اعلام کرده خودتان را آماده کنید «جنگ نزدیک است».
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/alonews/152740" target="_blank">📅 01:10 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152739">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b45af26fcf.mp4?token=CUkQgfTwjcbEd5MrLu5gL1SRsRD3ZbwBNX39yZN7at_8XqNp-_HZ6VoWknn3VffugnIseR_9zVC0M4yC0apKLat65Sa5OnHAY7fpP88_VL_lXBjaN44VYuzl1bCktvKvqBlFcMjPR6hImbK5p8kKlOOOb2-RPLyiTpkXloQc3EcgdBJgqxib7Yy0Nui9W7NqTvfM07ts1-Li1xtK3ntsvButouB1j0EF_bXZDD5itdrWfsADBu2hzi_0_pnRZA4-sRtePH7tCTtgHeh4ybHDEichgG0hXv-rP0c07jWukHcNDwNs3Sk3htQ-Ikipkb8L90OGpCL4sfyitlOJnOwJ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b45af26fcf.mp4?token=CUkQgfTwjcbEd5MrLu5gL1SRsRD3ZbwBNX39yZN7at_8XqNp-_HZ6VoWknn3VffugnIseR_9zVC0M4yC0apKLat65Sa5OnHAY7fpP88_VL_lXBjaN44VYuzl1bCktvKvqBlFcMjPR6hImbK5p8kKlOOOb2-RPLyiTpkXloQc3EcgdBJgqxib7Yy0Nui9W7NqTvfM07ts1-Li1xtK3ntsvButouB1j0EF_bXZDD5itdrWfsADBu2hzi_0_pnRZA4-sRtePH7tCTtgHeh4ybHDEichgG0hXv-rP0c07jWukHcNDwNs3Sk3htQ-Ikipkb8L90OGpCL4sfyitlOJnOwJ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: «دلیل حمله ما به ایران، در واقع دفاعی بود؛ چون نمی‌خواهیم آن‌ها به سلاحی دست پیدا کنند که بتواند در یک حمله، میلیون‌ها نفر را نابود کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/152739" target="_blank">📅 00:48 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152738">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d1cf2f837.mp4?token=jbN6OyRvQghKw63onB2VqLe1rraCssXahUjr4c8e0djRc0ngxylY0RK2yIxXK8G6fBdcgAgd44MML_kWq4dIDmuzQm9_IfKthvyhIEQ9nHkE9G3J2v-Lu-Uej-fIh4qvjnACmG0lae1f8A5sixfRrr6WvVnHmd0xpys2Q5XRofKp2EBJiP7SwNmAtTdEQyyK7O1Sg-w-6KVRv1cfaLGKC_qdF80LigAyOQn9ZAEQiZ5KXqBlnkfXOSKEnTtPru53M3FeYli8FVwYnRq2UF4o4jySJ7iVJI5qV8mZvmaf5JGvP7IlHgV7h6XT3d8qrZVKJJZ8oes5pTdL-FNyYklpqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d1cf2f837.mp4?token=jbN6OyRvQghKw63onB2VqLe1rraCssXahUjr4c8e0djRc0ngxylY0RK2yIxXK8G6fBdcgAgd44MML_kWq4dIDmuzQm9_IfKthvyhIEQ9nHkE9G3J2v-Lu-Uej-fIh4qvjnACmG0lae1f8A5sixfRrr6WvVnHmd0xpys2Q5XRofKp2EBJiP7SwNmAtTdEQyyK7O1Sg-w-6KVRv1cfaLGKC_qdF80LigAyOQn9ZAEQiZ5KXqBlnkfXOSKEnTtPru53M3FeYli8FVwYnRq2UF4o4jySJ7iVJI5qV8mZvmaf5JGvP7IlHgV7h6XT3d8qrZVKJJZ8oes5pTdL-FNyYklpqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: «اگر ایران به سلاح هسته‌ای دست پیدا کند، سواحل غربی آمریکا را هدف حمله هسته‌ای قرار خواهد داد، چون رهبرانش «دیوانه» هستند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/152738" target="_blank">📅 00:47 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152737">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3afa7d4e29.mp4?token=vZn-qbd-lv_j7LFPY-uFw8e_vPwAS_kXKvkMQvXR8XWcqtsjssSjlSyiFOcBsbRAmdmk8L5NjqX-D3r5zMGdIjtytZqpuPTkgMcI7tOmgsJsOpfSqDHDCBVdlWXQdMCFNFnUTBp6ZMt_un8I7F-G_V-5t6YuSCVYviJUdeUtAp75dPpT2JeI-m2rOOBwscT9K8kR7vqPMyYEm_h1M9O4O1ARqNc9VACTXCrSyr2tL_yu86gLkg0nOU7P88WyJIG9BFi5woVD_z6RLjnwCeHVVTRTgpuDpNl6zlOEWmldwemNxqicgr8oYj11p35MKoYQunFyfApeRDPP3oyS_rR3LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3afa7d4e29.mp4?token=vZn-qbd-lv_j7LFPY-uFw8e_vPwAS_kXKvkMQvXR8XWcqtsjssSjlSyiFOcBsbRAmdmk8L5NjqX-D3r5zMGdIjtytZqpuPTkgMcI7tOmgsJsOpfSqDHDCBVdlWXQdMCFNFnUTBp6ZMt_un8I7F-G_V-5t6YuSCVYviJUdeUtAp75dPpT2JeI-m2rOOBwscT9K8kR7vqPMyYEm_h1M9O4O1ARqNc9VACTXCrSyr2tL_yu86gLkg0nOU7P88WyJIG9BFi5woVD_z6RLjnwCeHVVTRTgpuDpNl6zlOEWmldwemNxqicgr8oYj11p35MKoYQunFyfApeRDPP3oyS_rR3LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ترور رهبران ايران:
احتمالاً کمی زیاده‌روی کردم. متأسفم، چون دیگر نمی‌دانم با چه کسی طرفیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/152737" target="_blank">📅 00:46 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152736">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0f068cfa.mp4?token=XdJx0Q5XKTEkvPt0VdhygEq9RyjHWTiRgGw9Y3sZZUZzxtFgjrUinlyzcn28y0wVSDOsS_VEkRE76eubqpJeL7ka6_W1ZCHKWgAh5q0-qivFpRxPUVCqboBVxmlbxPRrSuGf9fSyRavmpAhUaJMBG89ualrcFOzr56MBh2VJi1iW44e_D5feKtg3W3XtDA-h1-j5AOzEmpl6NEP5Jgy37nNr1dVCYU23fC_v_o5OIP7uYP5x4Y2AOc6rXd69X4VWfkkn8kUCSUhoYMgxGDe-9W4RxXTpr3pSkA2hGyEGrlIH4lHN1lsMUh88gn1Z_870KKzD2kvDmU7hvVXeDvIp3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0f068cfa.mp4?token=XdJx0Q5XKTEkvPt0VdhygEq9RyjHWTiRgGw9Y3sZZUZzxtFgjrUinlyzcn28y0wVSDOsS_VEkRE76eubqpJeL7ka6_W1ZCHKWgAh5q0-qivFpRxPUVCqboBVxmlbxPRrSuGf9fSyRavmpAhUaJMBG89ualrcFOzr56MBh2VJi1iW44e_D5feKtg3W3XtDA-h1-j5AOzEmpl6NEP5Jgy37nNr1dVCYU23fC_v_o5OIP7uYP5x4Y2AOc6rXd69X4VWfkkn8kUCSUhoYMgxGDe-9W4RxXTpr3pSkA2hGyEGrlIH4lHN1lsMUh88gn1Z_870KKzD2kvDmU7hvVXeDvIp3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ درباره ایران:
آن‌ها از من قول گرفتند که دیگر هیچ‌یک از رهبران ایرانی را از میان برندارم. من به آن‌ها قول دادم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/152736" target="_blank">📅 00:45 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152735">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
طبق گفته تحلیلگران غربی؛ برنامه ای که توسط آمریکا و اسرائیل برای حمله به ایران تدارک دیده شده؛ شروعش برای بازه زمانی ۲۳ تا ۳۰ مهرماه هست. اگه برنامشون این باشه که قبل از انتخابات حمله کنن تو این بازه حمله رو شروع میکنن.
💹
@shahab_gold_trading|</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/152735" target="_blank">📅 00:41 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152734">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rv_jrtd2mdnCD31DQDqxtVxwTLwZFSwz8hhJUCfBHMRJ8xVPrEcN5mwnUSppY4wYYn1DK1kuwdVbU0D_rsiTRttnZRALokDHEKszCxyoMmh0DfcT_eT7VemyVop4tpSmsNYhy3mhpN2Gv27sWQkUJUDG3AnBaSN8QgsQvz16tUpr2Q0I7uOvGrCHbORzsxe0LzLCxUL3okVYS1LEos1N9owdRNdfZT4-Dc8GGVc1XjNNKbbPfTJ0Xt1ES5v1gU4QSCj9OW3lmjZDGFO4dp-5JxOQBvI_2up7-2fwBV3IGGVokL7wk4zXcakrN92sciweQBAqVtZDOON_x7nHl04RhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میرسلیم: حق دارم از طرف مردم حرف بزنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/152734" target="_blank">📅 00:30 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152733">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3oaG9fS8kAdxdKMXfo0H9nnW58V8wRWAdf6RMOdcNaBCq8BRqUSksJqMozqiWLx7rJuF7ckicaytMoOnUCjZCoEQXxgWD-h6GuvLM3lzh54QLtyWbDGUTcemlHXF15uUQ45OoELEbuDQRJG9wctKZ2V2sG-rSJByZ7AWelqA_w0GtV7sM3F-bsDdTXszGumBac-aK91vcUFdMK4eavPNUv4tN49b7ArHWjTubbPSy2MHCbtQTARgH1cprUuH71B0V_pKlQ2k9AHdavEB_BPGf8lFZk1qugG3p4VJIWQ8XANuBAqf-aVP_JHxqX7Amp4xuD1eJHGMcJJJDNJnUXoLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کرباسچی:
نظام حریف آمریکا نمیشه و باید تسلیم بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/152733" target="_blank">📅 00:21 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152732">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
کریم صفایی، محافظ شخصیت‌ها : عامل موساد، هاشمی رفسنجانی را در استخر غرق کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/152732" target="_blank">📅 00:13 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152731">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9972452cba.mp4?token=o9YLuax_Eo2g0GrACVBvch4vF62Yu6RUO4fIOccfWewW92YZDvpX_xvX_ncPNCbPbnnL1RNQ9kIUtbRwFxR2xa9tC7aClpYnvfgz553L_0eBNpK7042w9UCUc7enRvjp7owpWI0mEqiDm6ZrbAi7ByvEuCZjP9a_2OS5F0EeFXtW3yaKrgrScJ1UxiVoWOBshOWbbteySRwSTCQ5Q6c92q-EzGVtVMLKe3f0GfoZbF9Ky_4qsshkL6FjgcdWtrt6uTEj6P2PE2fUjrnBIk7a5qec3jQaxXXyZxHk_GObYxlycpYNyJRwm8KjE4nVObVFvmrjKnxfGkVShuOyBqle4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9972452cba.mp4?token=o9YLuax_Eo2g0GrACVBvch4vF62Yu6RUO4fIOccfWewW92YZDvpX_xvX_ncPNCbPbnnL1RNQ9kIUtbRwFxR2xa9tC7aClpYnvfgz553L_0eBNpK7042w9UCUc7enRvjp7owpWI0mEqiDm6ZrbAi7ByvEuCZjP9a_2OS5F0EeFXtW3yaKrgrScJ1UxiVoWOBshOWbbteySRwSTCQ5Q6c92q-EzGVtVMLKe3f0GfoZbF9Ky_4qsshkL6FjgcdWtrt6uTEj6P2PE2fUjrnBIk7a5qec3jQaxXXyZxHk_GObYxlycpYNyJRwm8KjE4nVObVFvmrjKnxfGkVShuOyBqle4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره ایلان ماسک:
«ایلان ۸۰ درصد یک نابغه فوق‌العاده است و ۲۰ درصد هم یک مشکل کوچکی دارد. من همیشه این را به خودش می‌گویم.
🔴
او مرد فوق‌العاده‌ای است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/152731" target="_blank">📅 00:10 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152730">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/912fcd7513.mp4?token=DCT3NlfotACFK5q4eaeoJyYfxLyT_xozuiBZql9PPdBzX2IIXfDk85bVmmamtfFBnRkNxX7jgJv8Jo5m2BJNQPPwzH2NTjVvtnotKl86bjsU665U8jOXk-hoB6RGgzdvBPL-8-M98PMxFoUrbQzdL26Z6yV3ie2yT0KtNGFoZJwXRBBx95OkII2D-1dvsoDEe3v6dK6pttCihXqhUxcJ116ESqwid5eCD9ob8V5t0s880paoy2cLbYcLF0erJJnE0PtAQYumlhyqqb-Ax84Hj0L1RdRATSV-7LAy7eaAzp-bVe_plptMImf-cKBeV-bl8QIZt64UU2ih7b6vFLNnqBrS5gJP09RHxXHQ7kv04Y2oFd2Ty0R3dxg5vno682GAb9lBLbqevvQap-CPXt6CRvPvgwLSCWCx0ji-MzkuNDHF5ij2MApXlq_pWfgDaFu6b8AC0O53SzaNFmTu2U37Ej9A8yIDaFzQ5xSpUYbhze-qaBsXYAMA7JyiknqZ_18EXr4v4Cj0OxJbKqrZg5Q5ZGP0w8haZ675EicsQQN33Okg1dph65KwxNDLo6rQ9z9KAqSqGs_rVY0haea-XBnIoIzuYVWbclcQlG-TmxE_AJNdn72zBVjc4GBmPliCATSxTzndd4C5A1FK4_lUJ4Ychv1Fr-3Yo1IBZs48PeYRZno" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/912fcd7513.mp4?token=DCT3NlfotACFK5q4eaeoJyYfxLyT_xozuiBZql9PPdBzX2IIXfDk85bVmmamtfFBnRkNxX7jgJv8Jo5m2BJNQPPwzH2NTjVvtnotKl86bjsU665U8jOXk-hoB6RGgzdvBPL-8-M98PMxFoUrbQzdL26Z6yV3ie2yT0KtNGFoZJwXRBBx95OkII2D-1dvsoDEe3v6dK6pttCihXqhUxcJ116ESqwid5eCD9ob8V5t0s880paoy2cLbYcLF0erJJnE0PtAQYumlhyqqb-Ax84Hj0L1RdRATSV-7LAy7eaAzp-bVe_plptMImf-cKBeV-bl8QIZt64UU2ih7b6vFLNnqBrS5gJP09RHxXHQ7kv04Y2oFd2Ty0R3dxg5vno682GAb9lBLbqevvQap-CPXt6CRvPvgwLSCWCx0ji-MzkuNDHF5ij2MApXlq_pWfgDaFu6b8AC0O53SzaNFmTu2U37Ej9A8yIDaFzQ5xSpUYbhze-qaBsXYAMA7JyiknqZ_18EXr4v4Cj0OxJbKqrZg5Q5ZGP0w8haZ675EicsQQN33Okg1dph65KwxNDLo6rQ9z9KAqSqGs_rVY0haea-XBnIoIzuYVWbclcQlG-TmxE_AJNdn72zBVjc4GBmPliCATSxTzndd4C5A1FK4_lUJ4Ychv1Fr-3Yo1IBZs48PeYRZno" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا:
«با رهبر بسیار محترم قطر تماس گرفتم؛ مردی جوان و خوش‌قیافه.
🔴
به او گفتم: اگر امکانش وجود دارد، خیلی دوست دارم بتوانم هواپیمای بوئینگ ۷۴۷ شما را قرض بگیرم یا از آن استفاده کنم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/152730" target="_blank">📅 00:09 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152729">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❗️
هر لحظه احتمال جنگ و قطعی اینترنت هست
🔼
اگه میخوای همیشه وصل باشی میتونی از بات زیر یه سرویس تهیه کنی
👇
@VOXNET_BOT
@VOXNET_BOT
مورد اعتماد
✔️</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/alonews/152729" target="_blank">📅 00:05 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152728">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65efcfbaa3.mp4?token=q-3QW_JW_pUfGlzAXUZXrQkOOBNzW03VR-lNSHoF3_BnigGRmQb_hGAFL_ZkqLxeVA6fwqgJsAUSJ9gP1XKqKYCeala_62pv6lQHQFwsRwf1jE-eQ3JDlJjUtogM0ARmdUync8vfydsQLBWjXxEM_1l18HvqI11rfVVg7Z0Ed0K5t8QW4ZW_kQK9QqHjlW5hg4CzOsilwp1G_qSabYWGEk9Gy_MbJxcsGsnEPPQoPpDcjzW0qzblsgI7dh5GKkwxsK8PSDr7GHNPcp9EwoyKD_CPEuidmh4Ic7Qt_KLkVTK932HxYEvRnHMn1Zwp988yxdEsgVnN7QOOwfL3StiN6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65efcfbaa3.mp4?token=q-3QW_JW_pUfGlzAXUZXrQkOOBNzW03VR-lNSHoF3_BnigGRmQb_hGAFL_ZkqLxeVA6fwqgJsAUSJ9gP1XKqKYCeala_62pv6lQHQFwsRwf1jE-eQ3JDlJjUtogM0ARmdUync8vfydsQLBWjXxEM_1l18HvqI11rfVVg7Z0Ed0K5t8QW4ZW_kQK9QqHjlW5hg4CzOsilwp1G_qSabYWGEk9Gy_MbJxcsGsnEPPQoPpDcjzW0qzblsgI7dh5GKkwxsK8PSDr7GHNPcp9EwoyKD_CPEuidmh4Ic7Qt_KLkVTK932HxYEvRnHMn1Zwp988yxdEsgVnN7QOOwfL3StiN6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آخرین وضعیت کشتی موشک خورده در تنگهٔ هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/152728" target="_blank">📅 00:02 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152727">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/482b840586.mp4?token=v-Pn49OHQUPOzW0Je_Bj09LEMlzw87Bdm__AJAuCAICfXJRQ0I0HZLF3RHTGpDRImzahxv0WqTc7SpfdG6REmQxPPBsfEkca0LUtujoKx_6G_OlfuSn-XdK5tWAAZHkxFCblDF8e1UcchQoZbnsvCm11XdD4cftvydovTP964F1cmvFFszMeZYSOrQia172hm46zcj_R-sCMB9NqfavCfYQXGsvbsVZZF04-mxv3R7narn8Qt-vKeaAuGmJ1pzcx0jOtRuAWY_JFrwWOW7JXyOdQHBT1ftfb1ogO-o9Of_xeNgSASEgjXfLQwikA0_YmBJAIgkTo7FqGfin7MYZBDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/482b840586.mp4?token=v-Pn49OHQUPOzW0Je_Bj09LEMlzw87Bdm__AJAuCAICfXJRQ0I0HZLF3RHTGpDRImzahxv0WqTc7SpfdG6REmQxPPBsfEkca0LUtujoKx_6G_OlfuSn-XdK5tWAAZHkxFCblDF8e1UcchQoZbnsvCm11XdD4cftvydovTP964F1cmvFFszMeZYSOrQia172hm46zcj_R-sCMB9NqfavCfYQXGsvbsVZZF04-mxv3R7narn8Qt-vKeaAuGmJ1pzcx0jOtRuAWY_JFrwWOW7JXyOdQHBT1ftfb1ogO-o9Of_xeNgSASEgjXfLQwikA0_YmBJAIgkTo7FqGfin7MYZBDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام، با انتشار ویدیویی اعلام کرد نیروهای آمریکایی ۱۴ مهر یک لنج مرتبط با ایران را، منهدم کردند.
🔴
سنتکام افزود خدمه پیش از انهدام لنج به‌طور ایمن از آن خارج شدند و تلاش برای بازگرداندن آنها به کشورشان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/152727" target="_blank">📅 23:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152726">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecaf11f4a6.mp4?token=edG0EW4TpyeCOyoW3EiV92QfAuUHhsZlS-0R_BrIMg0ktBUZyDqEmH-M6RvQsrBT7d-Rtz_R2t1N_Ga9Ti7t6m1pezUDDAC0-yElS3Zx6UzGLHh4MZJolYRtNb-2-6voObEdUSUdckdOTiZiiVhEYSIQ2pRDRE0iTlO7z09DVYPW6J6AktSlES5Qum6tQHl0tjRFsf4mga82gGcaLj1SSFulyUZnn_a8P5XhcMUyMhYNHMZQyGHl_6EoD10ATAq4hcCpbKwTMQAx4X2I1IbhcynQqE92iPfPIb2djheg_JyFW3K2qINFgo_FQ9aaFCORSe36d1W0JgVlaPa7Ixke5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecaf11f4a6.mp4?token=edG0EW4TpyeCOyoW3EiV92QfAuUHhsZlS-0R_BrIMg0ktBUZyDqEmH-M6RvQsrBT7d-Rtz_R2t1N_Ga9Ti7t6m1pezUDDAC0-yElS3Zx6UzGLHh4MZJolYRtNb-2-6voObEdUSUdckdOTiZiiVhEYSIQ2pRDRE0iTlO7z09DVYPW6J6AktSlES5Qum6tQHl0tjRFsf4mga82gGcaLj1SSFulyUZnn_a8P5XhcMUyMhYNHMZQyGHl_6EoD10ATAq4hcCpbKwTMQAx4X2I1IbhcynQqE92iPfPIb2djheg_JyFW3K2qINFgo_FQ9aaFCORSe36d1W0JgVlaPa7Ixke5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: «اسرائیل امروز قدرتمندترین قدرت است.
🔴
همچنین می‌توانم به شما بگویم که اقتصاد ما با چنان سرعتی در حال رشد است که باورکردنش دشوار است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/152726" target="_blank">📅 23:50 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152725">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/233a985a0b.mp4?token=ta5JA-pYRfMYMvEi3pAldXQmzv7zFhkUWHHryRMQkPU2IL7JK4W9G1YLqTklL9nuoreMcUA7K1CIs01t1z-WsHj_XIj63bU-7zwuAtKvboqPkTcua7vqF8fU6s2u3Jj6QLYvmzEcIsolJqVnMjzcZsyWQIARWE1INpqijxCKyMMMIlo5VeyVv22KW78BrDPbGj7V99649qY7dv6Bz13Z-TWe7tMjpQqs2rw2FKILyFiGxWm9WwnqAB2x7EOWtYfg-p6BUccwUF-eMnuPUgEHKzl7pY3TJosspPEYV4Q5GIZMBXmAuSEoANUouknHbhSnDPSdUhrp2VaOdFNpPqxXVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/233a985a0b.mp4?token=ta5JA-pYRfMYMvEi3pAldXQmzv7zFhkUWHHryRMQkPU2IL7JK4W9G1YLqTklL9nuoreMcUA7K1CIs01t1z-WsHj_XIj63bU-7zwuAtKvboqPkTcua7vqF8fU6s2u3Jj6QLYvmzEcIsolJqVnMjzcZsyWQIARWE1INpqijxCKyMMMIlo5VeyVv22KW78BrDPbGj7V99649qY7dv6Bz13Z-TWe7tMjpQqs2rw2FKILyFiGxWm9WwnqAB2x7EOWtYfg-p6BUccwUF-eMnuPUgEHKzl7pY3TJosspPEYV4Q5GIZMBXmAuSEoANUouknHbhSnDPSdUhrp2VaOdFNpPqxXVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«من تمام زندگی‌ام را وقف این کار کرده‌ام.
🔴
هزاران ساعت در برنامه‌های پربیننده تلویزیونی آمریکا حضور داشته‌ام.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/152725" target="_blank">📅 23:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152723">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31f85a0760.mp4?token=KOrU2KcX0TCBW1WrcB9eXUjg7KFIiSOXt-TPfBPH6l717opYdS6oAOA0lcwkCJrfWBWmrSC0RQMM1Ad7Pxc_THrXUoZvvdtybp8uIb--W4Gfwd-SlyvFLzEGjPCkGEgAdQrSit8DIPl-UAf78PnmmYr95PnOwDhV-W5FNhQ5ZpRNOLQM-6grpg5T4DVoJLn6sQ4Odm62n9Ih7GWMdg7QVg7Im5fuFcyVDwip35Dl6mReKHLuGwyLgfX-GgDNM0Sg0lFZacAGNvhyan3MwaLYdUTY0BmZe1WQOwh_PVMFKUg_k_ukzrNIKzCcB7aAaWMpMYL2xPsqxLDu4uN-p6uXkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31f85a0760.mp4?token=KOrU2KcX0TCBW1WrcB9eXUjg7KFIiSOXt-TPfBPH6l717opYdS6oAOA0lcwkCJrfWBWmrSC0RQMM1Ad7Pxc_THrXUoZvvdtybp8uIb--W4Gfwd-SlyvFLzEGjPCkGEgAdQrSit8DIPl-UAf78PnmmYr95PnOwDhV-W5FNhQ5ZpRNOLQM-6grpg5T4DVoJLn6sQ4Odm62n9Ih7GWMdg7QVg7Im5fuFcyVDwip35Dl6mReKHLuGwyLgfX-GgDNM0Sg0lFZacAGNvhyan3MwaLYdUTY0BmZe1WQOwh_PVMFKUg_k_ukzrNIKzCcB7aAaWMpMYL2xPsqxLDu4uN-p6uXkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو درباره ایران
:
«من می‌گویم که سرنگونی این رژیم ضروری است.
🔴
ما اقدامات زیادی انجام داده‌ایم؛ آن را درهم شکسته‌ایم. این رژیم اکنون در ضعیف‌ترین موقعیت خود در تمام دورانش قرار دارد.
🔴
اما باید کار را تمام کنیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/152723" target="_blank">📅 23:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152722">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ca5ec198.mp4?token=KlpNrpmDwCikXhATZbylKt1CPcZbiaQtjEgSgPCtl9tJTB9kFLhujFM-eIOkiItImdPqmqp3OT7hFnLUnsJOW8wFNezltf8zscvzSGeuGKpTSJHdtQ_E1kEIQyqsuUzdPBiNZ7Q7Jr2eLYL3dk0MNR5GPa9xzF0V4c_0eurDZylzSZpJhuSONQfgSwDbpkXFcHtAWkntRjkN2_hVkvV3FT2OzjQL8HH8vck_qD4wI7j1gEu8Jl0Q-QUP_1dHTTRQwLucVsA2waKwjNzb2Pi6GbW6Bl2Ua50QeH8VK-aXo4pLusp_NhCtztnuPHSgE2AB2_HUYDSKlNO9HVp0q_HekQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ca5ec198.mp4?token=KlpNrpmDwCikXhATZbylKt1CPcZbiaQtjEgSgPCtl9tJTB9kFLhujFM-eIOkiItImdPqmqp3OT7hFnLUnsJOW8wFNezltf8zscvzSGeuGKpTSJHdtQ_E1kEIQyqsuUzdPBiNZ7Q7Jr2eLYL3dk0MNR5GPa9xzF0V4c_0eurDZylzSZpJhuSONQfgSwDbpkXFcHtAWkntRjkN2_hVkvV3FT2OzjQL8HH8vck_qD4wI7j1gEu8Jl0Q-QUP_1dHTTRQwLucVsA2waKwjNzb2Pi6GbW6Bl2Ua50QeH8VK-aXo4pLusp_NhCtztnuPHSgE2AB2_HUYDSKlNO9HVp0q_HekQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرسش:
آیا تغییر رژیم در ایران پیش از انتخابات اسرائیل واقع‌بینانه است؟
🔴
بنیامین نتانیاهو:
«نه، فکر نمی‌کنم چنین چیزی واقع‌بینانه باشد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/152722" target="_blank">📅 23:43 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152721">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_RxbNZuUOAtGBwoFyiSGtMLj_0oB_zmM0sKFIUfnV4232cYMyaSqwOSp-rOGd5x2ksY5U6UKnGO6yI8KINkEY88ds84uHf3cwM6BUPpvatsR6z4aZbjyzYTpZuqx3qsgJP2y_denUkWPjpQo8OqTPv_cxwDWNkrpQmvlEir4aC0cZYmEc_FAcDfQsNcw1h4JVfbD7Fsg5Kly0owgPti3mcBbJdVo-MvnXqJ0qG3tbgG2Sv38Hw2ob3dPkL5zWjzJrkWNqe_FV-N4uiZUas2KKKcBhH3JCQpnCiE24xuyp_EpYLCLaunwni9xQDeLGPpzH1ZPtQZGQ4r5GbOWg7Dtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دختری که پاشو میداد پسرها بخورن و فیلمش رو منتشر میکرد توسط فتا بازداشت شد
مشاهده فیلم</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/152721" target="_blank">📅 23:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152720">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31a6e1de75.mp4?token=KxH211eyxGfX7gyLNQlbA-q56H1C9rIVop0zHUho9j-ACg2-Zx3f8slIZA4coYJmWzkYjzyIdAG7h0yExoHWCkgJmuuQ2eo0vcD1t5iRoNl-xhYWh9E4v9W8bf0r-E32jVBytRWWrtjKRPaOWVp-uyNZhV_w9JvJSbbZgzKpeUrKXx4EaUFh5dZXIaDYWc7nzD_2S2UIGz1VMs5ZCYCeLM8kyu5QV_y2EB-mwTLwaGB2-gTWMzGUEGWQ-HnTJCGY3Sliib5SdOAPdgiOH1SNyv4W_y3nH2oZ7dWsuSDoGgPveh8rVOUH5neKJq-mO8CMJPhbPYKQUdmIx_8ugOzZvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31a6e1de75.mp4?token=KxH211eyxGfX7gyLNQlbA-q56H1C9rIVop0zHUho9j-ACg2-Zx3f8slIZA4coYJmWzkYjzyIdAG7h0yExoHWCkgJmuuQ2eo0vcD1t5iRoNl-xhYWh9E4v9W8bf0r-E32jVBytRWWrtjKRPaOWVp-uyNZhV_w9JvJSbbZgzKpeUrKXx4EaUFh5dZXIaDYWc7nzD_2S2UIGz1VMs5ZCYCeLM8kyu5QV_y2EB-mwTLwaGB2-gTWMzGUEGWQ-HnTJCGY3Sliib5SdOAPdgiOH1SNyv4W_y3nH2oZ7dWsuSDoGgPveh8rVOUH5neKJq-mO8CMJPhbPYKQUdmIx_8ugOzZvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو: «گادی آیزنکوت می‌خواست جنگ غزه فوراً متوقف شود. او می‌خواست جنگ را پیش از آنکه حتی وارد رفح شده باشیم، متوقف کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/152720" target="_blank">📅 23:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152719">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ترامپ : بخشی از دلیل وقوع جنگ اوکراین این است که بایدن در سرتاسر جهان به تمسخر روسیه می‌پرداخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/152719" target="_blank">📅 23:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152718">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ترامپ درباره چرایی عدم استفاده او از واژه "دیکتاتور" برای توصیف ولادیمیر پوتین: من باید با افراد مختلف مذاکره کنم، بنابراین نمی‌توانم به این شکل به آنها توهین کنم. من یک مذاکره‌کننده هستم.
🔴
من همیشه در مذاکره بسیار موفق بوده‌ام. من به دلیل انجام معاملات، ثروتمند شدم. بنابراین، من به این شکل مردم را مسخره نمی‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/152718" target="_blank">📅 23:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152717">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33809b8f53.mp4?token=RGo85jZIH3bPBszA1ugOpO8syA1X2uOclQalxVni205xPv5RIaXg172xYzTKt0tJ3BJJ1WEM92q5oDttdEIL5JMQTnbVA__0nVwpvaa_AnSt7L2jU91QCRMBduGs07eqmuoaaO-uLu6yT13Ib9u48CFVsxzVgdhKH0qbIl2I2eWtydQzKm1s8jfjGSckxe61_0MHBR9VWdH9pGZ-v0rQ8G2AobIfxlnvIc5oB-MasE09VlWGdAjfRrTBDqy0LNaUBXJp_b6Rd7AHuRsWK_Ve5e-fkTbm0l1ZVP8m3cvjHV-vj6Anp3nXHWUfnwl53sMneeDsb-HdUHh5XEiVMHfAYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33809b8f53.mp4?token=RGo85jZIH3bPBszA1ugOpO8syA1X2uOclQalxVni205xPv5RIaXg172xYzTKt0tJ3BJJ1WEM92q5oDttdEIL5JMQTnbVA__0nVwpvaa_AnSt7L2jU91QCRMBduGs07eqmuoaaO-uLu6yT13Ib9u48CFVsxzVgdhKH0qbIl2I2eWtydQzKm1s8jfjGSckxe61_0MHBR9VWdH9pGZ-v0rQ8G2AobIfxlnvIc5oB-MasE09VlWGdAjfRrTBDqy0LNaUBXJp_b6Rd7AHuRsWK_Ve5e-fkTbm0l1ZVP8m3cvjHV-vj6Anp3nXHWUfnwl53sMneeDsb-HdUHh5XEiVMHfAYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما با چه کسی در حال تعامل هستیم؟ هیچ کس دقیقاً نمی‌داند؛ هیچ کس نمی‌خواهد رهبر باشد.
🔴
ایران به زودی شکست خواهد خورد، و زمانی که این اتفاق بیفتد، قیمت بنزین و سایر هزینه‌ها به شدت کاهش خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/152717" target="_blank">📅 23:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152716">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee99761bb.mp4?token=WJJl3Fd9F0iUtpdbYE0ufwhmjXv0aJflZeSuDmv6canB6H3YhxHY0aznAMrIbegh4h7pht_-VlI2Cn2N-D4BfaVZOW_IFs2iNDUPX9GSqQkZ0cM7D4nODEZFeEH6gxcG41Y1n5HZTx0hiz7lPrm7LUAw8KAqHFXMKRLyDlovWK9HMN2z1iXLubNtznQ--acoTKK2YVGpZNqOYXOcyD_msXCykRSdQhgvLB0AByHDQ1xxtNhLBE9sRDhaPIvW8jY0tM3uaqQlKBV6ATxV_Fv1pU7aqqut4OFnbpBP29_WwkfyPUeuk7-fnKNHx9kg77BU5Mute990KwubvaxKxUXyDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee99761bb.mp4?token=WJJl3Fd9F0iUtpdbYE0ufwhmjXv0aJflZeSuDmv6canB6H3YhxHY0aznAMrIbegh4h7pht_-VlI2Cn2N-D4BfaVZOW_IFs2iNDUPX9GSqQkZ0cM7D4nODEZFeEH6gxcG41Y1n5HZTx0hiz7lPrm7LUAw8KAqHFXMKRLyDlovWK9HMN2z1iXLubNtznQ--acoTKK2YVGpZNqOYXOcyD_msXCykRSdQhgvLB0AByHDQ1xxtNhLBE9sRDhaPIvW8jY0tM3uaqQlKBV6ATxV_Fv1pU7aqqut4OFnbpBP29_WwkfyPUeuk7-fnKNHx9kg77BU5Mute990KwubvaxKxUXyDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی خطاب به ایلان ماسک: امریکا با قطع استارلینک به ما خیانت کرده
🔴
لطفا استارلینک ما را قطع نکنید؛ این یک اشتباه بزرگ است؛ این کار را نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/152716" target="_blank">📅 23:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152715">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
زلنسکی، رئیس‌جمهور اوکراین: تحت فشار آمریکا استعفا نمی‌دهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/152715" target="_blank">📅 23:11 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152714">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سید محمد خاتمی: رئیس‌جمهور چین به من گفت از پروژه هسته‌ای در اصفهان دست بردارید
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/152714" target="_blank">📅 23:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152713">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb16ad2b7c.mp4?token=vsldOsMblZRPFJ2BH1q7FPm-SQSmBsR1HKWL86uKD5PFS37A71fAwMYnuFeIc2tc8ywSPOME6FP2r8a2KB6u8zvLZaS1BCUGI9op4tIKjWyQBoPpg4yxPrvmFlcCxHos3GhKya44w4cXXtEQ7imNxi60-Ox68I4sECh441NKFwwBj999YeIZDKSD0418k-a0UFjrn1D-YLVutIM4hWhOLOcRYFc1Fcjg7rJX0PHppUPg9bpN1cl8qyoOOCxnpcwDJgJDPdYg0jBK3AXQudG08E_XfRgdQdfpTUNH7Yx3duT8lVjdftSwrYok3Ahdk6GICFgRZgQovJp0s9I4EoOtQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb16ad2b7c.mp4?token=vsldOsMblZRPFJ2BH1q7FPm-SQSmBsR1HKWL86uKD5PFS37A71fAwMYnuFeIc2tc8ywSPOME6FP2r8a2KB6u8zvLZaS1BCUGI9op4tIKjWyQBoPpg4yxPrvmFlcCxHos3GhKya44w4cXXtEQ7imNxi60-Ox68I4sECh441NKFwwBj999YeIZDKSD0418k-a0UFjrn1D-YLVutIM4hWhOLOcRYFc1Fcjg7rJX0PHppUPg9bpN1cl8qyoOOCxnpcwDJgJDPdYg0jBK3AXQudG08E_XfRgdQdfpTUNH7Yx3duT8lVjdftSwrYok3Ahdk6GICFgRZgQovJp0s9I4EoOtQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از نشریه i24NEWS:
مقامات ارشد ایرانی در روزهای اخیر به دیپلمات‌های منطقه‌ای گفته‌اند: "ما مطمئن هستیم که آمریکا حمله خواهد کرد."
🔴
همان مقامات به دیپلمات‌ها گفته‌اند: "فضای جنگی در تهران حاکم است."
🔴
در روزهای اخیر: ایران سرعت آتش‌زنی در تنگه هرمز را افزایش داده است - چندین کشتی که مورد حمله قرار گرفتند، غرق شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/152713" target="_blank">📅 22:58 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152712">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
سخنگوی سپاه : احتمال جنگ هست! ایران کلی سلاح و مهمات از چین و روسیه خریده و آمریکا اینو فهمیده و میخواد مجدد رو چین تعرفه سنگین ببنده!
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/152712" target="_blank">📅 22:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152711">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در جده عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/152711" target="_blank">📅 22:54 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152710">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
سخنگوی نیروهای مسلح یمن(حوثی‌ها): یمن، فرودگاه بین‌المللی ملک خالد در ریاض را با یک فروند موشک بالستیک هدف قرار داده‌ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/152710" target="_blank">📅 22:49 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152709">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkG7PPcIFMam5ixQ1VUzLkfVFCCYaocsKufmcaEcQBV3kVFeoz3aJXnAQixWk3Sn5Ph1irmPH3NFuY5hQZP3lMlqnR2ev8fmA75WnkLlaQMlWf9jmBfcaWArKRzi4g3DE4ZjOBL0woc0xNq8aMUo2ncVscmd6d3AYbR4KAC8BBssFMdk2fh8lPhKcp-57AKk-pBoPCTf5WMox_-DGEE5Jkt5cYBB2_tTLbU5MtVXpxUCDdfPjVErl7hRWZcaxj9C2ZpCS2ErFzCBbBol6q1XfUGieNt8aSwuL3DVswyrfBb95ojOkVxw4cw8g5Y0JFLJMGFRYx9uHNO2-ScCh5ZpFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش فرانس 24، پاکستان یک هواپیمای بدون سرنشین حمله یک طرفه توسط طالبان را که از موتور DLE55، یک موتور تجاری 55 سانتی متر مکعبی که در علی بابا چین فروخته می شد، سرنگون کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/152709" target="_blank">📅 22:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152708">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HIktyt0JA7jK4J43JR21AC_iTwiJtzecD97folbQ7XnUGuEGElOP2KMuuTT0zgOWjP_QcSU53kJw4C_KSVJ-LN7bDIRfNf6_hFx3zyJybHBKPwveVT6xnaXwCDt4Hs4pCI2PMyvLvhEH_9BDZ42n2VZLB2_U8vsxiPXaljox81QZJtEBZqHrZk1eIASxjCwML5yeYBjjBvsxB6dvDoXvAyk9SW1CqzKcS-gF-OuVKy0SWdlKxS_S02dJqmX9ZiMUL4tKcrsTg8znvgjp7HWDcreGDGyO2GRDp6Us3tpVPCPWxK2HzqU-IYn05L_BbB9Lj7D6XUwXR8kbiZ4-laLdGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با افزایش ۱۰۰ درصدی تعرفه‌ها، قیمت هر گیگ اینترنت به ۲۵ هزار تومن میرسه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/152708" target="_blank">📅 22:37 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152707">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
قالیباف: درباره پیشنهاد آمریکا باید بگویم که آن‌ها باید تنبیه و شیرفهم شوند که خواسته‌های به‌حق ملت ایران را بپذیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/152707" target="_blank">📅 22:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152706">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYLJeASlRor5YJAvn4LZvHtQL4wNWbOqS1WY2st3MCoeOnp_rUjmHc41n7Re1nFKJbvk6FMaG88XoOa-elVOAZUYvm1zTQ2aYBz5QtclTMNleoDwpX7WhMFMeKSV80LhNhv74OOF-N1-zsBSTkjWbTJXcldRx-yvzDkUoK6krZkZDg5np4r6PCo_x-2-OKsEQPuZnmXtdkJJ7kcRxKUTa1xPcPRKU_ZR1iUgn2pqmjGElnJ0MUmoPuw65ntI6Tvm1po8BG1RbQM2xyLCrXifOuBcWXEi8Z3Gvt8Fel6h4WC58hBK5IbjSXRsrkGpGbC2eVjZ5pO7nHZXOJg7n5Q73g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکونومیست: کمتر از سه هفته مانده به انتخابات میان‌دوره‌ای آمریکا، طبق شاخص رصد نظرسنجی‌های ما، میزان محبوبیت دونالد ترامپ به پایین‌ترین سطح تاریخ خود رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/152706" target="_blank">📅 22:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152705">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd32b47709.mp4?token=Px1EWEVHJS0SUYYZP8NkhABlzsqdFgxkpCqJSjomJTdFAFJErsUnptenqDFAzEmwES8MEETTcG3C7AV9o1f9Pp0zXVwu_XYolBOsMKkthxA7KZlmcV_QUi26fUmz2j6pZYbCP-PJmq_OL45DX5qT4nbAE4Ttlm4E3--5Yf40y74DUwqmqaUSN1bWNecRiGk2THD37eDu_RFh8d4eK2atYtAr52EcSd09eugmDQu-PSaCyJctIYWIVxdvhI9z_UgwWD2LK1yWWYe_kkbio8isCBzXGnMlRhKluPdKTjGZ2MQJgpqjPi5GVnEckrRQRyp54XoFcj_i_zRAe-aeXYvpMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd32b47709.mp4?token=Px1EWEVHJS0SUYYZP8NkhABlzsqdFgxkpCqJSjomJTdFAFJErsUnptenqDFAzEmwES8MEETTcG3C7AV9o1f9Pp0zXVwu_XYolBOsMKkthxA7KZlmcV_QUi26fUmz2j6pZYbCP-PJmq_OL45DX5qT4nbAE4Ttlm4E3--5Yf40y74DUwqmqaUSN1bWNecRiGk2THD37eDu_RFh8d4eK2atYtAr52EcSd09eugmDQu-PSaCyJctIYWIVxdvhI9z_UgwWD2LK1yWWYe_kkbio8isCBzXGnMlRhKluPdKTjGZ2MQJgpqjPi5GVnEckrRQRyp54XoFcj_i_zRAe-aeXYvpMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طوفان کرباسچی در تلوزیون
‼️
🔴
کرباسچی: اکثریت مردم مشکل اقتصادی دارن و با نظام‌مخالفن!
🔴
هرکی هم میاد حرفی میزنه رو چندسال میندازید زندان
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/152705" target="_blank">📅 22:24 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152704">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
ارتش آمریکا در حال انتقال تجهیزات نظامی از قبرس به امارات است!
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/152704" target="_blank">📅 22:19 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152703">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d07aa0cfd3.mp4?token=fk1Dttn7_mkwp4Q9AGpMrcXsUL13JZj7Thy6ATdf-F6ISldgfVFnvbZNK51Jxzz76s6Tnq7m_eqyWtmLY7VlJVmEGBCl1Kyt5FkNEQ9cQ03GLU5WExILiNXA4Dd-F4Ii4LfVkW2hMUmbKnsnNRtatFSbjJZLDAb18qCytcK5bhcozS45wShm8rHFSEUOI4qsh-RZLPEZ9BfrVMHOP5N3fxKmLOv6E2j-89tPT5OyAXteGi81qb_CPLCx8gzsDizxluyU0iKCFwHxHcy1Qxza2YvV4zMSbpgl5TdE4fy_hVi1rpYUIBk6QBkQSn5EXJvY_BNbhOBjZxb_Bpo2XkuS9Avs205n-mCnlRAi70VkPZ8OOFlF18MQQqGOGmfg_Zfp6hA_eaZjwk70Z0gElVSpYIOhooGYv1J8BmxY4Dfob5JFhHVOwHMdqwbsdGFmw13D__wWRV1ykV5Y0W2HemzYuMED1fhu0i5EhGBL4xEsQZzOnoIU7mKmvH0yBu-jYTwP7GG5fU0f5xS2TvvY8CzntgRqq4cWy6aWWS0tpRmPFw2fO8PfD26Y4ydJWBICWhg6dFV9gcJC9nE2YKYhahVqr_18mbgiIXmHmDGz1fQiVxTGkMkIUrAStb-Skbqk39l0X2JfgHUq5_kMT2UWadYOBXYEsEbnYCxFFgiVqUPRAyM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d07aa0cfd3.mp4?token=fk1Dttn7_mkwp4Q9AGpMrcXsUL13JZj7Thy6ATdf-F6ISldgfVFnvbZNK51Jxzz76s6Tnq7m_eqyWtmLY7VlJVmEGBCl1Kyt5FkNEQ9cQ03GLU5WExILiNXA4Dd-F4Ii4LfVkW2hMUmbKnsnNRtatFSbjJZLDAb18qCytcK5bhcozS45wShm8rHFSEUOI4qsh-RZLPEZ9BfrVMHOP5N3fxKmLOv6E2j-89tPT5OyAXteGi81qb_CPLCx8gzsDizxluyU0iKCFwHxHcy1Qxza2YvV4zMSbpgl5TdE4fy_hVi1rpYUIBk6QBkQSn5EXJvY_BNbhOBjZxb_Bpo2XkuS9Avs205n-mCnlRAi70VkPZ8OOFlF18MQQqGOGmfg_Zfp6hA_eaZjwk70Z0gElVSpYIOhooGYv1J8BmxY4Dfob5JFhHVOwHMdqwbsdGFmw13D__wWRV1ykV5Y0W2HemzYuMED1fhu0i5EhGBL4xEsQZzOnoIU7mKmvH0yBu-jYTwP7GG5fU0f5xS2TvvY8CzntgRqq4cWy6aWWS0tpRmPFw2fO8PfD26Y4ydJWBICWhg6dFV9gcJC9nE2YKYhahVqr_18mbgiIXmHmDGz1fQiVxTGkMkIUrAStb-Skbqk39l0X2JfgHUq5_kMT2UWadYOBXYEsEbnYCxFFgiVqUPRAyM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیرس مورگان: آیا پوتین هیتلرِ دوران ماست؟
🔴
ولودیمیر زلنسکی: قطعاً؛ همین‌طور است.
🔴
مورگان: فکر می‌کنی او تا این اندازه شرور است؟
🔴
زلنسکی: او آن‌قدرها هم قدرتمند نیست که شرور است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/152703" target="_blank">📅 22:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152702">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ef3bc8036.mp4?token=sHnUW_KTCgaM92u7jvu_waGEc8ARsCU8vHzWyQ2CpMuyXdEoyag5jK6ZqTPR82b8SlSjrMvLP0-r0kUTVgLxhgqXHcqniW1hixJJSeO72OwXd0TWmsS63ryuSyXNbCLbuFlNOXmX6Hyzx88j4lSDaSF_Yw9bNIHGSFGDl4qNV-yPlJurxJig0kvhYAyghGQ3kISdURlcylJPy2K5abcunZN_rn67FitZwShonGRILxR4qNaFSSW6woaQKoHGj0W0mJ2kvzrDeJbYW03nTkaGKp5bYfgDxchSPGs767PRSAeFzr2FmcXe0txoWifxZ1L64YDe6Q7qelsWbq83agdrng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ef3bc8036.mp4?token=sHnUW_KTCgaM92u7jvu_waGEc8ARsCU8vHzWyQ2CpMuyXdEoyag5jK6ZqTPR82b8SlSjrMvLP0-r0kUTVgLxhgqXHcqniW1hixJJSeO72OwXd0TWmsS63ryuSyXNbCLbuFlNOXmX6Hyzx88j4lSDaSF_Yw9bNIHGSFGDl4qNV-yPlJurxJig0kvhYAyghGQ3kISdURlcylJPy2K5abcunZN_rn67FitZwShonGRILxR4qNaFSSW6woaQKoHGj0W0mJ2kvzrDeJbYW03nTkaGKp5bYfgDxchSPGs767PRSAeFzr2FmcXe0txoWifxZ1L64YDe6Q7qelsWbq83agdrng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ولودیمیر زلنسکی، رئیس‌جمهور اوکراین:
«تنگه هرمز دلیل واقعی افزایش قیمت‌هاست. تمام دنیا این موضوع را کاملاً روشن و بدون هیچ تردیدی درک می‌کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/152702" target="_blank">📅 22:13 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152701">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
هر سه اپراتور ایرانسل، همراه اول و رایتل با ابراز تعجب از رقم ۴۰ درصد اعلام کردند که درخواست آنها افزایش ۱۰۰ درصدی تعرفه‌ها بوده است!
🔴
‏ اپراتورها می‌گویند نوسانات ارزی، تحریم‌ها، آسیب‌های ناشی از جنگ به سایت‌های ارتباطی و رشد هزینه‌های تجهیزات و نگهداری شبکه، فشار اقتصادی سنگینی به این صنعت وارد کرده است
🔴
‏ به گفته آنها، درآمد اپراتورها ریالی است، اما بخش مهمی از هزینه‌های توسعه شبکه وابستگی ارزی دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/152701" target="_blank">📅 22:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152700">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/92e13adabf.mp4?token=eYf0RhXborp1MH1Rr4-Jdw087B4qnD5KK9t4PpbOskX-FvHp_hlWgPH8iTjAUHL3_glKVKd8xQ_trBZyjIsI25k1qy4H4SETh9BLCSHVVT0WpbFgRCQHzyzhsQushlno2EzIutSokJWsNFA0ViGjJPYm4apK8l2SjmtfN2AElzForPqWGEsqBEnWXQKpxmQC5FGhWawPkJ_fhYKGgyWucUDUPnx6NaEHJRKzrPuCkCwtOe0Y2E7eiukmo1Kr6f-tMb3BfaqDvRzuQXBR6XmYLaE-GdO25TAdD9DOne6bO4Povz7qgjth8D3xNgX3i44V6dF-yHTzGSx8Ns8viQAnew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/92e13adabf.mp4?token=eYf0RhXborp1MH1Rr4-Jdw087B4qnD5KK9t4PpbOskX-FvHp_hlWgPH8iTjAUHL3_glKVKd8xQ_trBZyjIsI25k1qy4H4SETh9BLCSHVVT0WpbFgRCQHzyzhsQushlno2EzIutSokJWsNFA0ViGjJPYm4apK8l2SjmtfN2AElzForPqWGEsqBEnWXQKpxmQC5FGhWawPkJ_fhYKGgyWucUDUPnx6NaEHJRKzrPuCkCwtOe0Y2E7eiukmo1Kr6f-tMb3BfaqDvRzuQXBR6XmYLaE-GdO25TAdD9DOne6bO4Povz7qgjth8D3xNgX3i44V6dF-yHTzGSx8Ns8viQAnew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تقلید صدای علی خامنه‌ای توسط بلاگر طنزپرداز جنجالی شد
🔴
سعید شکیبا، بلاگر طنزپردازی که صفحه اینستاگرامی‌اش بیش از یک میلیون دنبال‌کننده دارد و به تقلید صدا مشهور است، در ویدئویی صدای علی خامنه‌ای را تقلید کرد؛ ویدئویی که با واکنش تند حامیان رهبر جمهوری اسلامی روبه‌رو شد و برخی از آن‌ها خواهان برخورد با این بلاگر شدند.
🔴
شکیبا پیش‌تر نیز صدای شماری از مقام‌های جمهوری اسلامی را تقلید کرده بود. او همچنین در ویدئویی جداگانه به کشته‌شدگان اعتراضات دی‌ماه ۱۴۰۴ واکنش نشان داده و از آن‌ها حمایت کرده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/152700" target="_blank">📅 21:59 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152699">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
سی‌بی‌اس نیوز: احتمال دارد آمریکا عمداً از ارائه هشدارهای اولیه درباره حملات موشکی روسیه به اوکراین خودداری کرده باشد؛ حملاتی که ۶ کشته بر جای گذاشت و برق ۶۰۰ هزار نفر را قطع کرد
🔴
مقام‌های آمریکایی شرایط نامساعد جوی را دلیل این مسئله اعلام کردند، اما مقام‌های اوکراینی این توضیح را زیر سؤال بردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/152699" target="_blank">📅 21:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152698">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پشماممم این گردونه جدیده رو زدم 1,000,000 ارز بونک هدیه داد
😐
😂
گفتم لینکشو بذارم شما هم بیکارید یه تستی بکنید ببینید چی میده بهتون
👇
https://B2n.ir/gd6225</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/152698" target="_blank">📅 21:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152697">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1a18687a9.mp4?token=tVwWTfAJ_eNRSW9WuxLvjlAQgxxh4iucuiD-1bc98cthSU4tBpnCL9gebkqgTXpmMZSo9w9OexpZe9XsrNXRRDtFzDuyb7C2w0KCRukMIVzkIaWp7AAOCiNwD45RZ3-LjJ3CN9ZCdETq2-PrcE7mXl74N0z8moBIoZAMK4PR5WRaez_piZ82brnPCyF_zGzh21gSMxfMwKWAUfOi2AmWJsEWTASDc2-OuqGhBZJFOib76v2xn1HRYsg4C0a7yhO5rR1u-CvXZW8d0LfbSBnGcDEXLKIiqLTkMrEm4bua68tdik4iYBKiR6z9utG3d2yzxE_sxk9vHVWNaFThxThL44WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1a18687a9.mp4?token=tVwWTfAJ_eNRSW9WuxLvjlAQgxxh4iucuiD-1bc98cthSU4tBpnCL9gebkqgTXpmMZSo9w9OexpZe9XsrNXRRDtFzDuyb7C2w0KCRukMIVzkIaWp7AAOCiNwD45RZ3-LjJ3CN9ZCdETq2-PrcE7mXl74N0z8moBIoZAMK4PR5WRaez_piZ82brnPCyF_zGzh21gSMxfMwKWAUfOi2AmWJsEWTASDc2-OuqGhBZJFOib76v2xn1HRYsg4C0a7yhO5rR1u-CvXZW8d0LfbSBnGcDEXLKIiqLTkMrEm4bua68tdik4iYBKiR6z9utG3d2yzxE_sxk9vHVWNaFThxThL44WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: تفاهم علاوه بر بازدارندگی به نیروهای نظامی ما کمک کرد تا قوی‌تر شوند، تاب‌آوری اقتصادی آن‌ها بیشتر شود، حزب‌الله لبنان قوی‌تر شود
🔴
ما با این تفاهم فرصت و منابع کافی پیدا کردیم که مولفه‌های قدرت خودمان را قوی کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/152697" target="_blank">📅 21:49 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152696">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
پزشکیان: باید شرایط جنگ اقتصادی را به فرصتی برای حل مشکلات کشور تبدیل کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/152696" target="_blank">📅 21:43 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152695">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
طبق گزارش ها برای چهارمین روز متوالی، جنگنده های اسرائیلی پروازهای تمرینی را روی آسمان سوریه و عراق آغاز کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/152695" target="_blank">📅 21:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152694">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: دو هفته آینده بسیار حساس است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/152694" target="_blank">📅 21:28 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152693">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhXnAJsVKejPR_uNVAl5q4aRmlgGgxWd8dFj45YmidYXRgBqd2qcn7e7SyaXF-g2BosE5xLcwVzvN_MzFeEqb9WZvY5NJQqJGgTCFVlOAIKVCQjGi0w9uuHPJsmyVPf2CeVMI35Up6xwi0hmWQStfVOnh_6aoVIu6dDWFOnkq7re5qZV9mXW-KTqBz5pID4BUo2e68UkPD6BgPexhRqKcAANSzdJt99gEgEg97NUMAB6bQKu9bI9-V83QY7q9z6bXCBBphVgOJLN8K8PliKiaWBkju1R2w4yjsPZwsEwtbARSXKNCEekgkxnYLw9dNQDis6mbGqfI7znv6--83xw2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک اکانت اینستاگرامی، کد مخفی عکس خاتمی را رمزگشایی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/152693" target="_blank">📅 21:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152692">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWlzm5xYc7c5Lduu8ob0PdfxbMQiPAhJnc5CXz3850y5bVrHIqu_urRcBbWfkvbluT8Cc5EpHgLZK5aCvLCjO0asJxuj8b_l_N1DTqNpQL6Vtv0xrBf14Jo6I3hBHAj1Cr2PHmRfbSkhE8f-aqlp_7gNWkYY_kKbN6MqnZJ5UGJSPBI_AANeEsoR2MRl1LHrO1QZSj_L4YJoeY9rAXEzIZ3xgDLT-dLK9Mt0VnLkOTu9fyfpdU0qv4edVtJ3vPC9ZTmrdlAP4fE82gkR58dteAzMEF_JfadkMeA-iPLViGeB_0TeZtAJqGXoMhipkFf_50jwX32ZyGlmunVhuALfSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: بیایید «درصدها رو بازی کنیم». منظورم شانس نیست، بلکه درصد رشد‌هاست.
🔴
راستی، «دو هفته دیگه هیچی ندارن»، «سه روز دیگه چاه‌ها منفجر می‌شن» و «روز پیروزی اقتصادی» هم گذشت.
🔴
زمان نسبیه؛ معلوم می‌شه ممکنه اصلاً مهم هم نباشه. جایزه نوبل فیزیک کاربردی برای وزارت خزانه‌داری؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/152692" target="_blank">📅 21:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152691">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
قالیباف: هم می‌جنگیم و هم مذاکره می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/152691" target="_blank">📅 21:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152690">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
زلنسکی: ترامپ به ما خیانت کرد. او در طرف اشتباه تاریخ قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/152690" target="_blank">📅 20:54 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152689">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c7c9b362.mp4?token=vqXNpbHBP6IURQfufY16QRNDWybFVARluUroe0MgsyATTdY__gd-KbBuuUOa_iqYf1oegGeWS1Zt-25EwBkNfbhCYl9ApzUEV0b22sS-mkjpQcBPnoJM3New5IaCUbfskqpKDBvrMYAvIUpGXhndr-IsuHFLFurE1jW1OsZ3topHk5R8zw2sptDkWCkTLPodFSyJ4oMfSXwbkZqfaCYKbE1wxevmFR3hQyBu7Xw2WAc4nZDn7MZyFxn63pdUJuW5pEhDDcHE2nFsDsyQ5ljiCwmPL0fau1XwjrJ2bZnyXg4J8CtvFanAhmbRoQMOIpfWNEABUeeTPHKZfSz8eIfnYTdN-Gyfw6yJVBFXrDHwY_ScfqbAlC7DhBl6_yX2hzx8ClYUbUk1gI0AtMgiUkqm7ghCmPJn1OxuxvcF505P1ZUR2o8mHYKiiL993yMG44W1jeIBdHxDh1NjyAWWM1BOKfMnxsk-rYabmxl5vWVeN_N9mxj1bDIsB4RDX3PWz15i2Lvrp8VJgXTaJ3iNCYcUd4gKLDOk8xAQhHEKJ8_QS_zcf0eKo4X-pg4wiXKvpqlFmgov6gpB-hj_AzV9LoJ8GNo02LDy_15MdeERZLXXRIHn0gBKytwbKkmLrG3d-uJIiKfLYcfDt1u7IsLWh3s_xnDiCUDLdD_atBiUbMMCMjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c7c9b362.mp4?token=vqXNpbHBP6IURQfufY16QRNDWybFVARluUroe0MgsyATTdY__gd-KbBuuUOa_iqYf1oegGeWS1Zt-25EwBkNfbhCYl9ApzUEV0b22sS-mkjpQcBPnoJM3New5IaCUbfskqpKDBvrMYAvIUpGXhndr-IsuHFLFurE1jW1OsZ3topHk5R8zw2sptDkWCkTLPodFSyJ4oMfSXwbkZqfaCYKbE1wxevmFR3hQyBu7Xw2WAc4nZDn7MZyFxn63pdUJuW5pEhDDcHE2nFsDsyQ5ljiCwmPL0fau1XwjrJ2bZnyXg4J8CtvFanAhmbRoQMOIpfWNEABUeeTPHKZfSz8eIfnYTdN-Gyfw6yJVBFXrDHwY_ScfqbAlC7DhBl6_yX2hzx8ClYUbUk1gI0AtMgiUkqm7ghCmPJn1OxuxvcF505P1ZUR2o8mHYKiiL993yMG44W1jeIBdHxDh1NjyAWWM1BOKfMnxsk-rYabmxl5vWVeN_N9mxj1bDIsB4RDX3PWz15i2Lvrp8VJgXTaJ3iNCYcUd4gKLDOk8xAQhHEKJ8_QS_zcf0eKo4X-pg4wiXKvpqlFmgov6gpB-hj_AzV9LoJ8GNo02LDy_15MdeERZLXXRIHn0gBKytwbKkmLrG3d-uJIiKfLYcfDt1u7IsLWh3s_xnDiCUDLdD_atBiUbMMCMjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت ترابری هوایی نظامی آمریکا در دو هفته گذشته بیش از ۸۰ درصد افزایش یافته
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/152689" target="_blank">📅 20:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152688">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22ce76e630.mp4?token=AbgSOn6mO6FamgwJeODLwQV0QlqDYvUKkCTughwkbLMPALZml3Du1DhP8k-ODRALc7NtF7HD5nJkrOeWpXGy075XWHAwWWG7mzAk48KcFmCQaNyv2G8oUVEqeMp3if9bOC-WKCiFv_amf2ai62OL59OlOxXSm0VYMi7e4Dr-9SIkEplDSLGQgJ7YcaT6unZ7y_4XvIkkS1EEbgL8KxmZmzUZsoR7HcPJB_IjraAz4HbGQyd3zgvaJNBDsDIGoxkh3nBuSNUKfrvGNwUiiLTIvEGIAY7jylLfNEX3Xu-bvJ6-XsTj-cblyE7HxeSjczBWd21Ccwh9NM-UY67VdByuGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22ce76e630.mp4?token=AbgSOn6mO6FamgwJeODLwQV0QlqDYvUKkCTughwkbLMPALZml3Du1DhP8k-ODRALc7NtF7HD5nJkrOeWpXGy075XWHAwWWG7mzAk48KcFmCQaNyv2G8oUVEqeMp3if9bOC-WKCiFv_amf2ai62OL59OlOxXSm0VYMi7e4Dr-9SIkEplDSLGQgJ7YcaT6unZ7y_4XvIkkS1EEbgL8KxmZmzUZsoR7HcPJB_IjraAz4HbGQyd3zgvaJNBDsDIGoxkh3nBuSNUKfrvGNwUiiLTIvEGIAY7jylLfNEX3Xu-bvJ6-XsTj-cblyE7HxeSjczBWd21Ccwh9NM-UY67VdByuGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کرباسچی: ما نمی‌توانیم پدر آمریکا را دربیاوریم!
🔴
هر روز کارشناس بیاورید و بگویند ما داریم پدر آمریکا را درمی‌آوریم؛ اما واقعیت این است که ما نمی‌توانیم چنین کاری بکنیم.
🔴
درست است که به آمریکا آسیب زده‌ایم، اما باید دید دقیقاً چه میزان خسارت به آن‌ها وارد شده است
🔴
آسیب‌هایی که ما به آمریکا وارد کرده‌ایم، با خسارت‌هایی که کشور و مردم خودمان متحمل شده‌اند، قابل مقایسه نیست.
🔴
اساساً توان و ظرفیت ما با آمریکا قابل مقایسه نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/152688" target="_blank">📅 20:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152687">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff57fce1b.mp4?token=fOFZJQ58hZa8yd6RFjYzoxEITEjUqR29H7YJmiP97CaVWuWiYOjDV-MOJSW3ovj7uJVXk-rf9RYotBMlan7Yk3aGQP9hK7KByIWfy1nfDl8UzCtGvdosR-iQ0GyARuZa1f-9SZ63U967UkeqAn2Kxahp_8jPYgMEW4lKfkQGwLRWJRUrYfTzw6-0Owb9FxxH3k-aTutT8swXMqONdfZz2tQhaebHJ498sJ6dVzEuEHJQOo3xixPDJsxJy1Y3J4AmDZHF-9bGnpU1maUi1jPpo6nXI3g4JPJKa-kaC907rV3y3CsMZLa4HjisRV7e2DPUelOK5aN0-6QrC4Tu58tfPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff57fce1b.mp4?token=fOFZJQ58hZa8yd6RFjYzoxEITEjUqR29H7YJmiP97CaVWuWiYOjDV-MOJSW3ovj7uJVXk-rf9RYotBMlan7Yk3aGQP9hK7KByIWfy1nfDl8UzCtGvdosR-iQ0GyARuZa1f-9SZ63U967UkeqAn2Kxahp_8jPYgMEW4lKfkQGwLRWJRUrYfTzw6-0Owb9FxxH3k-aTutT8swXMqONdfZz2tQhaebHJ498sJ6dVzEuEHJQOo3xixPDJsxJy1Y3J4AmDZHF-9bGnpU1maUi1jPpo6nXI3g4JPJKa-kaC907rV3y3CsMZLa4HjisRV7e2DPUelOK5aN0-6QrC4Tu58tfPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کرباسچی:
سلاح هسته‌ای بازدارنده نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/152687" target="_blank">📅 20:32 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152685">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd776cbdcb.mp4?token=ABofCD_yISVdJRdZ1cuyNoDhg2Wgw1PCvqJn2Gl4XujzaTTVjFFgB-0sbiBSm8k9_ViPer4Od2FyPCFi_2i2sItlEwMBeU-qmzuQSv2scwmUAUtmPT33QXWCCilAIrWM_M7Ezd4SnL-BBX7OZILndkNGLb_KFtUzIMy6g69OfgiQXNnXo73PJNtCkVB1lF5QYW-n6IwQ3wn0aPSrYQJG2o_BBHxoNDXy9jpY3AEh8B5AzwCwFO_CjctmuEQA9uYRFwRMLwW6_yNlkXP_B13Qs-rqEGjGus15VNkUzO1HUWpxo_VHmB7uzWZVaLE5N7ruZx7D0oVEGLRDnM2WmqriCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd776cbdcb.mp4?token=ABofCD_yISVdJRdZ1cuyNoDhg2Wgw1PCvqJn2Gl4XujzaTTVjFFgB-0sbiBSm8k9_ViPer4Od2FyPCFi_2i2sItlEwMBeU-qmzuQSv2scwmUAUtmPT33QXWCCilAIrWM_M7Ezd4SnL-BBX7OZILndkNGLb_KFtUzIMy6g69OfgiQXNnXo73PJNtCkVB1lF5QYW-n6IwQ3wn0aPSrYQJG2o_BBHxoNDXy9jpY3AEh8B5AzwCwFO_CjctmuEQA9uYRFwRMLwW6_yNlkXP_B13Qs-rqEGjGus15VNkUzO1HUWpxo_VHmB7uzWZVaLE5N7ruZx7D0oVEGLRDnM2WmqriCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کرباسچی: زدن سه نفتکش بعد از توافق نامه اسلام آباد بهانه آمریکا برای از نقض تفاهمنامه بود همه دنیا تعجب کردند که آمریکا چگونه زیر بار این تفاهنامه رفته است
🔴
اما پزشکیان گفته من نمیدانم چه کسی کشتی‌ها را زده. هنوز هم رسمی ندیده‌ایم نهادی گردن بگیرد. اگر این سه کشتی زده نمی‌شد ایران دست برتر را داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/152685" target="_blank">📅 20:28 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152684">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhBHeg6tGo3wUHoT1JC1rbIvdQDW0UWtMh-XpbtoLug9tLV16v5dOnvQTmc6OEAXmKjseK6yzru0egPS1UMZ5a1ifKsGMb1nwGVvnIOplyo7_IQ4fbcc0-jk-wDGEOoo-EgwVQNeOJBd5C2R-BHIUm-Ro-fi5eYXZY57Tr6QQXTNs3esdQf2FUxtcYlf6WNfwpUPQfbsOzMBCFtUVRQOXFi8pHWbj_1VE8Sm3e8S27w4sdX_ZiSxZ3yHfg4Woe_-paK-2KDXbJ1FsdoiBSnuhbp7miropZ7tsN-8PVvm1SnsLrobCiN3QWdm_ZELUq6b_MfWh7dTQkGaN6C_Q4W7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کرباسچی:
باید قبول کنیم حریف ایالات متحده نمیشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/152684" target="_blank">📅 20:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152683">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
کرباسچی: باید هرچه سریعتر جنگ خاتمه یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/152683" target="_blank">📅 20:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152682">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
کرباسچی: باید هرچه سریعتر جنگ خاتمه یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/152682" target="_blank">📅 20:13 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152681">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9180b0e9.mp4?token=gx5KMg1huI6lMvAevAZzbtj34qmOfs_DB78nBKlTeuPQtngALj4DEpxoJw0jY0qRQhW05BwaAYcP23jVOW2PAY9fSp1xiM6fmjlRkWCw9kwpXiZYPGGjlUYm_HRiU5EMAmFKfbsCn6G19Vo5HdcqGDLdEKMnw6x8d6sVRTJt4l2rr0ntXpa9S5a0TrAM3lmKn4PA909DTApSiVmTsVWs49jZEKRdIyOuKAh6VvFn4iPhGZGiBxIgyKIpRUVWPEkEie4u07110_WHl66r-wSrp6zPVQ6jsO08Ts3_SnWkAzORJnjbeuwrkj5eU6HUt639jh59clCIGKIwO_Xu6o6dRqYhuwuK9hHK-CMQibDlenqcEcuXEUpUCzT7uJJqvtok3AwVZK9Et2ysKbQttps226UpUkaAL-oss2kq7SV1uJhquClUPfBKfMqXRubdKTFKLhcOYs0DORBsJTSQeSO4TQbzYMyxk6kR3MJkZzMwvdxC4pGDg-VkoJhfcpkN2mEqF57G3_TNL2MbArwS-A0bX8MA4pPZ3dtXmUyidMijsepCeNO_UyLljgD58LvuuQIUcJLYzcy2URE0pBLFbpC6CVpxJWPUqwgwArePwq99GU01OsR4PIAasjlMxv6l7L-SNvW-_HYbcvoY25k6bS__rmlx4mBBVHyr6DqnblLyZmo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9180b0e9.mp4?token=gx5KMg1huI6lMvAevAZzbtj34qmOfs_DB78nBKlTeuPQtngALj4DEpxoJw0jY0qRQhW05BwaAYcP23jVOW2PAY9fSp1xiM6fmjlRkWCw9kwpXiZYPGGjlUYm_HRiU5EMAmFKfbsCn6G19Vo5HdcqGDLdEKMnw6x8d6sVRTJt4l2rr0ntXpa9S5a0TrAM3lmKn4PA909DTApSiVmTsVWs49jZEKRdIyOuKAh6VvFn4iPhGZGiBxIgyKIpRUVWPEkEie4u07110_WHl66r-wSrp6zPVQ6jsO08Ts3_SnWkAzORJnjbeuwrkj5eU6HUt639jh59clCIGKIwO_Xu6o6dRqYhuwuK9hHK-CMQibDlenqcEcuXEUpUCzT7uJJqvtok3AwVZK9Et2ysKbQttps226UpUkaAL-oss2kq7SV1uJhquClUPfBKfMqXRubdKTFKLhcOYs0DORBsJTSQeSO4TQbzYMyxk6kR3MJkZzMwvdxC4pGDg-VkoJhfcpkN2mEqF57G3_TNL2MbArwS-A0bX8MA4pPZ3dtXmUyidMijsepCeNO_UyLljgD58LvuuQIUcJLYzcy2URE0pBLFbpC6CVpxJWPUqwgwArePwq99GU01OsR4PIAasjlMxv6l7L-SNvW-_HYbcvoY25k6bS__rmlx4mBBVHyr6DqnblLyZmo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کرباسچی: باید هرچه سریعتر جنگ خاتمه یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/152681" target="_blank">📅 20:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152680">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
فرود اضطراری پرواز تهران-استانبول در تبریز
🔴
پرواز شماره ۹۷۰۰ ایران‌ایرتور با ۱۱۶ مسافر که از تهران عازم استانبول بود، به‌دلیل نقص فنی ساعت ۱۸ امروز در فرودگاه تبریز فرود اضطراری کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/152680" target="_blank">📅 20:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152679">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
رهبر کره شمالی خودکشی کردن رو ممنوع کرده و گفته هرکی خودکشی کنه و زنده بمونه، خودمون اعدامش می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/152679" target="_blank">📅 19:59 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152678">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d51b184a4.mp4?token=snPcPxvSAuwpEUqYW4WOy3y470QNzKm6gDcwfG1tlZXZmtv6MWmPJ4jTEysQNhEyvsVXfBb05bEq7FFN3oStWzJc7yPlCKxfPrNQNYLWxV_YfU5KrtWL0GsYOhNXPUru-sJcuKQ__d8mPylTIEz-nnKYv7s1XCRHP7n2h2dxfD1tNrxlrS7Zdl2qMHzsXkWx5ytb5Z6A0k9qgnuZQwirLykiHs0dbdb3ZM031EKOjfgeGzmxGm93lVpqjts80SR9yHiJeVcLBdif9fxA9OQVvwpcZEcnUM0M5JhUWiCXhALPaaJPscBtKWjZCIkeaqMtKy1GJMNDWzx7yiQvYu7bLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d51b184a4.mp4?token=snPcPxvSAuwpEUqYW4WOy3y470QNzKm6gDcwfG1tlZXZmtv6MWmPJ4jTEysQNhEyvsVXfBb05bEq7FFN3oStWzJc7yPlCKxfPrNQNYLWxV_YfU5KrtWL0GsYOhNXPUru-sJcuKQ__d8mPylTIEz-nnKYv7s1XCRHP7n2h2dxfD1tNrxlrS7Zdl2qMHzsXkWx5ytb5Z6A0k9qgnuZQwirLykiHs0dbdb3ZM031EKOjfgeGzmxGm93lVpqjts80SR9yHiJeVcLBdif9fxA9OQVvwpcZEcnUM0M5JhUWiCXhALPaaJPscBtKWjZCIkeaqMtKy1GJMNDWzx7yiQvYu7bLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سینه‌زنی بیکارها با شعار:
🔴
«ظریف آمریکایی مایه نمگ مایی، فریدون نفوذی مفسد انگلیسی»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/152678" target="_blank">📅 19:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152677">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">dbbet.apk</div>
  <div class="tg-doc-extra">45.9 MB</div>
</div>
<a href="https://t.me/alonews/152677" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#دیبی_بت
😃
😉
🥲
🥲
🥇
اپلیکیشن رسمی دیبی بت
😉
با اپلیکیشن اندروید Dbbet بدون نیاز به فیلترشکن شرطبندی کنید
✅
#Dbbet
*️⃣
*️⃣
*️⃣
*️⃣
*️⃣
*️⃣
*️⃣
*️⃣
🎁
تا سقف 100 یورو بونوس‌ با
کد هدیه
2️⃣
🔤
2️⃣
🔤
یا همون
(
2K2K
)
👑
آدرس سایت :
👑
https://DbBet.club
☑️
کانال تلگرام
🛡
@dbbetif</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/152677" target="_blank">📅 19:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152676">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DfNteqNTVU-TnywnDQ9joI-UZ30ztA3q23_mG7rniZjcKmUgwfEkSL9Sba9ZUlrhr6-RGJ8xdTISO4VHh1rJKxhwsGrJ0YNQJKok6LhJ8tZmcsZVOI89Xt1A-VjtVoGV__0UAwI4jVm9NFjEu_b1z7ucu_IhDLO7FHP5col4RejlGP6jmmHGWooeprWrVp5aQ6XrCqe1nvXjRT6jSV6UovMXKsseoMhS7P07FZSNIjUiALfZtScc7BaSxyiHbkSkgFzTB-Xd6T9Y5QvVtwRRIj7YItO3x_P9if9v3EYalnOc_8v_uGpgpDeLHljdLs50ij7MaBM5uHh8jW6YeUGfLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
واقعا چرا دیبی بت انقدر در بین ایرانی ها محبوب شد
⁉️
➕
دیبی بت اولین سایت پیش‌بینی فوتبال ، که تمام ارزهای دیجیتال رو برای شارژ حساب پوشش میده
💳
درگاه کارت به کارت امن ریالی برای کاربران ایرانی
😉
اینجا با خیال راحت شرطبندی کن و درآمد دلاری کسب کن
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
😊
https://Dbbet.com</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/152676" target="_blank">📅 19:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152675">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwiQBxGQiLhrA1NWIitQkRBQrSxqpDw3U46M5o2eGU0wxnPyYiXXkYseLNdflUGFgjmA426d4PJvl4eufOm-CjD5-CagB9Qsl2rnvotqGqT2S7hVyfbBpBWEvBCb_iQhxi5885yXoBjSio0o8C9InUG7V2jR3rsOrRTIHOC46lXD6lv55qNOgGCT8x6qs5aUUHC44VKt7rtuRFQ7y_YQ_1lSIQ1EpzPrelipR2BTWW6okQWwqAb8rdYlsE7vNYs4yLagUPZ3dFHyTRYzhUkMCCSryhFlpPNl-m3xBtoG9oYzbdIMpyOSSTP6JwOz9O2GCyPCZu1_ZU_cpxwnQxczew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار الهام علی‌اف رئیس‌جمهور آذربایجان با رئیس‌جمهور اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/152675" target="_blank">📅 19:50 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152674">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
گزارش شلیک موشک از قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/152674" target="_blank">📅 19:41 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152673">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
اسرائیل ۱۲ بالگرد پیشرفته آپاچی از آمریکا می‌خرد
🔴
اسرائیل و آمریکا، قرارداد نظامی جدیدی را برای تقویت ناوگان هوایی ارتش اسرائیل نهایی کردند.
🔴
کابینه اسرائیل پس از چندین بار تعویق به دلیل چالش‌های بودجه‌ای، خرید ۱۲ فروند هلیکوپتر آپاچی پیشرفته مدل E ساخت شرکت بوئینگ را به تصویب رساند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/152673" target="_blank">📅 19:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152672">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac361504bf.mp4?token=a0aoQ5Gx1TRVHL3hXrVhAjPr4s0ap-rfpkKnAzusCDawcNbt8aFAjCa2bIZkQQfQYC_twFJEPv9ZdMQspy8Z1oJ8TDJ2HF3BUyJCbz0R_Dq4Q9FHhqhdtJsKWboJB4VoJ6rFY4ZfGmV6Mo84QQ8x1epRiHZwtmnyoUWGMU-IS5bgUBt_p0tpTsBz26vzdwJRC2arVQMtxDZ6wO57Apt9w6R00VXFRdR-7Y_VRzNZ8xYnLHK6026zouZzfuxvwN1TcKuYbmLlAQn6Y_atb193yZKfZaB4psD2YC13WeUiVt_x428IN-qxPgI_PxJH70a49yhVISZ_JMvwNPDOXxdYkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac361504bf.mp4?token=a0aoQ5Gx1TRVHL3hXrVhAjPr4s0ap-rfpkKnAzusCDawcNbt8aFAjCa2bIZkQQfQYC_twFJEPv9ZdMQspy8Z1oJ8TDJ2HF3BUyJCbz0R_Dq4Q9FHhqhdtJsKWboJB4VoJ6rFY4ZfGmV6Mo84QQ8x1epRiHZwtmnyoUWGMU-IS5bgUBt_p0tpTsBz26vzdwJRC2arVQMtxDZ6wO57Apt9w6R00VXFRdR-7Y_VRzNZ8xYnLHK6026zouZzfuxvwN1TcKuYbmLlAQn6Y_atb193yZKfZaB4psD2YC13WeUiVt_x428IN-qxPgI_PxJH70a49yhVISZ_JMvwNPDOXxdYkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سعید لیلاز: پیام آمریکا به ایران قبل از جنگ ۴۰ روزه: کنترل نفت ایران را به ما بدهید تا به شما حمله نکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/152672" target="_blank">📅 19:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152671">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ایرنا : خطر خاموشی در زمستان جدی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/152671" target="_blank">📅 19:11 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152670">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
نام برج میلاد تهران تغییر کرد
🔴
بر اساس حکم صادرشده از سوی علیرضا زاکانی، برج میلاد تهران به شرکت گردشگری و تفریحی میلاد تهران تغییر نام داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/152670" target="_blank">📅 19:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152669">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vz3agRBAnDV0ujAkiUyg4ikqgTArNKNhc4UgcUM7wE_92tzlcO8oXT8ceiXGn1a0h2EBmhau4shChE67chE5CJLU9aD6-UAGy3_S964jYmwt6P1W1CYVL_CTfIYAmgAaTKQLyCGaNXqpkc3I1elnFlMf4BjCZU5OzcD8x_0HhfUE83pE36yuCWK-9yeIhRd9p7lYMHS5mKEe2ZUX95uE3YpuQLldC8rU2Axp4ZfaPmyNGYBbIt0FbyRl78aH4VPpxHIoR6LAnPJZhq5j6sbLz4kDa3guQS7yHJLCoStbs1o_H7EZnFace6mfxBd7bxklQPrlnWnlGhz5Y7xAoyURFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش آمریکا در حال انتقال تجهیزات نظامی از قبرس به امارات است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/152669" target="_blank">📅 18:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152668">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: در حال حاضر، کنترل تنگه هرمز را به طور کامل در دست داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/152668" target="_blank">📅 18:49 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152667">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
سازمان دریانوردی سنگاپور: دو کشتی‌ کانتینری طی دو روز گذشته هنگام عبور از تنگه هرمز، مورد اصابت پرتابه‌های ناشناس قرار گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/152667" target="_blank">📅 18:37 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152666">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzsTzkxCtjt2OVvsqwTuYvUn7pK6xTI30d2t2bBFnx49xsMxPh5h1v_Rwb87Tg9-FQ5mdnDRHYv6h0l0LUMzeqv2ExRnyCFMJH44Cx0VdeFjJ4XHxEgA7kLF9p3EsL7-OoW7zOlxQW8naJgQnJ40RvSG74uGOag3-GIRgrv8Okus6dVf8jODKCgvt_w5aYN-OX3XSsILOQkwAE3GrcgwC1P8xj0AwiRozI4B2MpcO4VEOwIedN8DHVu82qpW3JIoyJsrguT2k3Qxz28uU-FExhwll7cV4hknm46wfBLDJWqYDKpAnF4vHw7nSZ-9Gfk_n9YYJYOfMMtJvDCPUeAZ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تورم آمریکا در سپتامبر به بالاترین حد خود در سال رسید: ۳.۷ درصد !
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/152666" target="_blank">📅 18:30 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152665">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87f461be38.mp4?token=fAMZtiXRnFWqSnz6kBTGgX-YRCUu-X5hHyed4QuNoB3QgIHkjem55MeaTdQ4nYu8-wEwclbMbezgJjfI3bjcwk0FBAwftK5rG_uaTrZKvn6j6ciGHeq79jDhoTaAyOcUAyf1e0fUj2ak1sCFF9_-U0VupyrUyETG4kFGT12o3jw0tCi2DM_oKfvLAIqhBYtrdjyEdspxkrD2yADH5Zt7TPvaawnMTrdIwDDl4LNjE-DNBmWi6UWhMXBAih5NBT2dxb6NgY3LtIbSLaKtu8gmBEMX_xbv_Msa5Bfn1Zgm_r_mv7jIXmUfsxIOi4mCA2-q_MhlQ68MI8yA0g7-Q8DlAIACyxdP50UZdQqQuskSsJL2ohwA2DAJwkQNHvXyZ7xF8hZYE1uZigNvw6bQ5cQClY5QEHg8T-co4RA5ksIfYun4gEmrjyUTJmmmjA7Fc3wbnlCjn_9vr_lqKVn5jyEGo_nQ91FGOAjdTVxQIwsH8hF0eUi4f12ETMt3RnOymy36oOeiet9xrcvC1rRatn2tFMDQ-FR5na2PS_9lDa5_Eq-peB2hNK36SndjTTgAJqrbRCQqaez0gA-ECSY6hstq2abqG2yQFBwCMcEwjA68pAwuB7EKwrsY2n4dseSqChYwSqnWCk-KEFbdp5Ow45NapgOkEXZWWzakZn6o3e8Aamw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87f461be38.mp4?token=fAMZtiXRnFWqSnz6kBTGgX-YRCUu-X5hHyed4QuNoB3QgIHkjem55MeaTdQ4nYu8-wEwclbMbezgJjfI3bjcwk0FBAwftK5rG_uaTrZKvn6j6ciGHeq79jDhoTaAyOcUAyf1e0fUj2ak1sCFF9_-U0VupyrUyETG4kFGT12o3jw0tCi2DM_oKfvLAIqhBYtrdjyEdspxkrD2yADH5Zt7TPvaawnMTrdIwDDl4LNjE-DNBmWi6UWhMXBAih5NBT2dxb6NgY3LtIbSLaKtu8gmBEMX_xbv_Msa5Bfn1Zgm_r_mv7jIXmUfsxIOi4mCA2-q_MhlQ68MI8yA0g7-Q8DlAIACyxdP50UZdQqQuskSsJL2ohwA2DAJwkQNHvXyZ7xF8hZYE1uZigNvw6bQ5cQClY5QEHg8T-co4RA5ksIfYun4gEmrjyUTJmmmjA7Fc3wbnlCjn_9vr_lqKVn5jyEGo_nQ91FGOAjdTVxQIwsH8hF0eUi4f12ETMt3RnOymy36oOeiet9xrcvC1rRatn2tFMDQ-FR5na2PS_9lDa5_Eq-peB2hNK36SndjTTgAJqrbRCQqaez0gA-ECSY6hstq2abqG2yQFBwCMcEwjA68pAwuB7EKwrsY2n4dseSqChYwSqnWCk-KEFbdp5Ow45NapgOkEXZWWzakZn6o3e8Aamw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پهپاد انتحاری اوکراینی، یک هلیکوپتر روسی مدل Mi-28NM را در حین پرواز، در منطقه‌ای از خط مقدم مورد هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/152665" target="_blank">📅 18:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152664">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
معاون وزیر امور خارجه روسیه:
مسکو آماده است در صورت لزوم تمام اورانیوم غنی شده ایران را به خاک خود منتقل کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/152664" target="_blank">📅 18:13 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152663">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
به گزارش والا نیوز، رئیس ستاد ارتش اسرائیل گفت: ارتش اسرائیل در وضعیت آمادگی بالایی برای انتقال به عملیات تهاجمی در مقیاس بزرگ قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/152663" target="_blank">📅 17:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152662">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayKrDdE7gAOFH9wKemjOxxsVsfN5P91lntFg8ZieHqU6qJVTw7S-nOR-7ZmOH6UJps1Rw5XoV6cv-MDq54G7xu2xRkCgVdSqRapcVAMJfxZ6ZbURv-y6_R_SfmsOgRVBIsUs_lAUDyp7lGNAUqJVgHiYVmIoyXiT0BIt6l5SR5rkB51PVeJIWkTAzpY6LxQWSj4I97YdRys-Z6XfwUrQqSAi4edFrFeMuKt5nlhzK949E5YGXgsIkMYl1d3urtuPRLP99EutQGvihOoeZb3KVh14fa_BCOz1nBOrTNq6RnwqWREbdRo-glMF-yBa_aBujdN0XVqe4tS1tkWzb47yuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان: وضعیت صادرات و واردات کشور و فروش نفت عالیه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/152662" target="_blank">📅 17:47 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152661">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4UqvrhIIokARl_w2LJPhw-2-SWtIwmUqX-zaJsAMk_zGEX71Ed9d6tlowfFZoPyLpqH_oA_zydjtc_g3fV_LSakl3nbp7TKt-92aeS8VYn4eeTd_JKTj78-HE-U5Tnb-mMT6OBCO0bI6YERgrFrfVs_SnpcsHsDyIH0kR2fYt4PkfQ3SjpLbkUE_FMmZ23ryJKrVwXoM5_wwF9vHlxW38qcCAcGuRbqCV5lXZbCxc5uBQPb1AeMhq7t1DYKKEKiBD-EgCAlcyjbKfDTDlglb5pqqIkgP7cz12VY8n__9e54b-xvnbPLgfgM9sML-ni-jv4UmurZRj_oA69e6f-tnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قائم‌پناه،معاون پزشکیان: هیچ مذاکره‌ای بدون تصمیم شعام و تایید رهبری شکل نمی‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/152661" target="_blank">📅 17:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152660">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
جزئیات جدید از نحوه بمب‌گذاری پیجرها از زبان سفیر ایران در لبنان
🔴
یک لایه مواد منفجره نازک ۲ در ۴ سانت در لایه‌های باتری پیجر جاساز شده بود؛
🔴
حزب الله از قبل از انفجار؛ به پیجرها شک کرده بود
🔴
حزب‌الله به پیجرها شک کرده بود و یک اسکنر کشف مواد منفجره از ایران به سمت لبنان می‌رفت که با موشک زدند.
🔴
یکی از کارشناسانی که قرار بود پیجرها را بررسی کند؛ قبل از انفجار پیجرها ترور شد!
🔴
جاسازی پیجرها در آستانه لو رفتن بود که انفجار را عملیاتی کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/152660" target="_blank">📅 17:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152659">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
جماران:
احتمال گران شدن ۴۰ درصدی اینترنت از امشب
🔴
بر اساس اطلاعات دریافتی از سوی اپراتورها، تعرفه اینترنت از بامداد پنجشنبه، ۲۳ مهرماه، ۴۰ درصد افزایش خواهد یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/152659" target="_blank">📅 17:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152657">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UDMRPijx-iFDByp16LTIKsuxQDkraLZnB5-WIWSrZpjrd_Yu-kg6ZhtZcGtR4m4lpT0BmI36nswQVcTWod8Oe18XEq1opQlmEcC2M5Mgcs8QifsbygV5FQEWWNZPA-dtI1ox1GDqgtDxlm48nIscrxNCavBDlRE-3sLUPISYSBoB4YAYTpV9yUpw5rohEUCcr9zS7U3jET_NqKuwcLuOnduYx582zIc1WRwrorVAfDahoczedPPdYXVra0jxsdkIFKBcMrARdlSF5NQsW5uLpA-kmPlactx8y1eTswgKvYF2mPZkh2u1Ur3XXmU4TrP6llIEjAES8h0gYRrrAtS18A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B8sr42Nhhxh--Pt2EYC1yrLA6tCYSGuXgI0yWpPA1D21oIgfh3VjI7lk2YdAoJlNcsnxjN-RgMvfOMBRmAQlwMs5l_U3_mSnaH5c7MOkteeuI3saVnf0D1NvOTyWgrMcgu88X2DY0EVFTzyCYUg7aPZrLtJ2OJwxlUPkQsdj3WW1_2smf5fKoPI8iftwGw3yPTs1UO_JhlpJqlAh0bP7dWik02CaYfW9UenIgxGPSTUuK87tDD-81lsgDgdmVJxRTZjrL41P9GNvL2D9oJ2scdCsx4JyT6jwt_mZsDTWd_xwciU2b8r4hG19r7Sl5YyJkQ1D7RQ9J0E4infdI4nsoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای آثار غرق شدن کشتی باری «GFS Pride» در تنگه هرمز را نشان می‌دهند که هدف حمله سپاه پاسداران قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/152657" target="_blank">📅 16:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152656">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
بیانیه دولت عراق: زیدی، حمله به فرودگاه بین‌المللی خالد در رياض و هرگونه حمله به غیرنظامیان و تاسیسات مدنی را محکوم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/152656" target="_blank">📅 16:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152654">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Sngx_hlYQqCJjzE7JN9gMwlR7_yQERX5-MTeX-DsshwCe1c_Z8SHPAXHVXIem5xwh58o6ecsSTjRIi_sb4lpCjJmcZRctbvc7AXmoZcjAIhDAoSMQgNVF5l1STuViaH_abX1M2IkN8n0oJaRVeSUF9meyQ4FeKXkWcaOAOtyQciS_GEkpXG9toXFNlWPUBUaD9lWlRf0RGEGxjoscFYlVTfyE_uj9zL5Bz6ay_hSEnSVW7Tm-B0w92C-oVVylwfHWFy7Fij8bHHmgsn1U4nEd5EZRUN93FsQHsoYxYr0U0rzoSN3rijxQU0ORFmvIOMuuCKucqW1kfulIxgtkvr8Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jrTf_f9pg3WsxxJ6Ju99GbbaE_PlCcGIBKV1MC61uJXg9mvplJcov-KB7uaf2oWNRR73nid7Fv1EWXafUjPqoxqVQM6fHauBYt1o8a77NN0Mcqw8BZLOUIuR2OihfOiZvdkdG42ZcEFnnRnzmAzduDNFE2YIgcEGGRJ-LnqhY1pETLl7VMQ9nU0ae4VniRvSXt_khzZADIg7mPNIptIG0wbXbT83nNFywOGKHsXOcxH91389K2rL3i29yYy5mCS7B8k2y_QIWac42J46T4r_ohnxyk11TwXRbNnCYxXNeWt-DokvK4GHc619LriGDEasZs5Fop_ny8DYF1cLJaCubQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر بسیار عجیب خبرگزاری مهر و ایرنا از ناو هواپیمابری که درحال قاچاق خودرو به داخل کشور است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/152654" target="_blank">📅 16:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152653">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
زلنسکی: روسیه شب گذشته با ۳۹ موشک بالستیک و بیش از ۱۲۰ پهپاد تهاجمی، به طور مشخص زیرساخت‌های انرژی ما را که شامل آتش‌بس می‌شد، هدف قرار داد
🔴
مسکو اظهارات ترامپ را قدرتمند و بازدارنده نمی‌داند
🔴
از رئیس‌جمهور آمریکا می‌خواهیم تحریم‌های شدیدی علیه روسیه اعمال کند
🔴
هیچ کشوری در جهان نباید در برابر بازیگری دیوانه مانند روسیه، تنها گذاشته شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/152653" target="_blank">📅 16:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152652">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4482fcb60.mp4?token=JD70Bo_s_a8yI9eNdw5U1_j6S7ptop-em21tHiUMR3_7kL03-Z11ZBEhjwP5eIzyK3bTC2gh-7DKz56GYSvuXX3Guikg-H1ZhFaVuXWh24SCyA--sAyHeY6_lcXuwvqXs6u-1-wDPl7-BYHpL7mhaV2YN1rmWJnOkGDzwOOScz0yypQU3dbGLoWT0EY2ltJJO00PLxyR4mrqJ3AguyIHDMjeXbFVGLQ0Q7C5nD17A2muyP5WMXi5EOe-8w69TB7TTdofFqZbQNkfkii-GGqx3rY1EtHl-aAcjjRmlDGwF21AuekDVdPPacJz1jk-ALOgJTikEttTtFfljwewayJV3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4482fcb60.mp4?token=JD70Bo_s_a8yI9eNdw5U1_j6S7ptop-em21tHiUMR3_7kL03-Z11ZBEhjwP5eIzyK3bTC2gh-7DKz56GYSvuXX3Guikg-H1ZhFaVuXWh24SCyA--sAyHeY6_lcXuwvqXs6u-1-wDPl7-BYHpL7mhaV2YN1rmWJnOkGDzwOOScz0yypQU3dbGLoWT0EY2ltJJO00PLxyR4mrqJ3AguyIHDMjeXbFVGLQ0Q7C5nD17A2muyP5WMXi5EOe-8w69TB7TTdofFqZbQNkfkii-GGqx3rY1EtHl-aAcjjRmlDGwF21AuekDVdPPacJz1jk-ALOgJTikEttTtFfljwewayJV3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: شاید بتوانیم یک کشور فلسطینی در اوگاندا تشکیل دهیم. آیا این می‌تواند راه‌حلی برای تمام این مشکلات باشد؟
🔴
نتانیاهو با خنده: «پیشنهاد شما به‌طور جدی بررسی خواهد شد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/152652" target="_blank">📅 16:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152651">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/959217c881.mp4?token=e23E2kZVJBmRBEtFYhfI1z-FZ9YfmPPIm8_Uwe-Cb6tNbBIAVj9xu5rbrx1g05BspkCp7lgTJ6a_cNPKp7bfD6QQni2FyYEl5xXp1b1USNnIN-hZx246smHganGAnYCIwnolKYSpcREt2m4yvYUybgoFXTXiBbL9IHkIIinxz4WJ1gpsDEL3WqcGIIMILqsP6BZx1hB4ZdhlwKGk08UPW0N36ylUKXlgescRY82-VOYuZ3FWdoFfZRi0lUEMvuh0_FGbcB5zbRbPI8J6jelllLf_5k-W34t8PJHwQpsaTN-406Qz-UWntnwrdeNpql9sENmz5-f__MATZhYahLsNfYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/959217c881.mp4?token=e23E2kZVJBmRBEtFYhfI1z-FZ9YfmPPIm8_Uwe-Cb6tNbBIAVj9xu5rbrx1g05BspkCp7lgTJ6a_cNPKp7bfD6QQni2FyYEl5xXp1b1USNnIN-hZx246smHganGAnYCIwnolKYSpcREt2m4yvYUybgoFXTXiBbL9IHkIIinxz4WJ1gpsDEL3WqcGIIMILqsP6BZx1hB4ZdhlwKGk08UPW0N36ylUKXlgescRY82-VOYuZ3FWdoFfZRi0lUEMvuh0_FGbcB5zbRbPI8J6jelllLf_5k-W34t8PJHwQpsaTN-406Qz-UWntnwrdeNpql9sENmz5-f__MATZhYahLsNfYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجروح حملهٔ صبح امروز به لنج صیادی سیریک: درحال صید میگو مورد اصابت قرار گرفتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/152651" target="_blank">📅 16:09 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152650">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIJL8kBsUIiZdN7zEmeVc_n4DhzaVQvq0H013pqI_GxFjKw1vNNhnbIJgAr3TeE7NEtjZ4URzeTQfpy5P7KEtEV2hVtXgUANAbF-F5PINkQhXkY3rLZ64_fGdllxrXGo5mCBKMps1KEyo8JJMWFtiqMaIJZana3DwVpZdQKBbfF9GLTz9wmocbp-kCW1_NyXc0kF2y2m_7UtHnYR99BueM41wGhJxFOBCGhDUmV8E56PSUag7SgElGYP_k53quVZhvwy_3wHT_Gy0zuo_rv_nLV42xT8EPLuyPjC_5aW2iNIXjde2M_V_r8D9PaYfOYiTdzPSGFm_cThEUYj8ol1KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: اکتشاف گسترده نفت، گاز و مواد معدنی در گرینلند آغاز می‌شود
🔴
دونالد ترامپ در شبکه تروث سوشال نوشت: «اکتشاف گسترده نفت، گاز و مواد معدنی قرار است در گرینلند زیبای ما آغاز شود!
🔴
کارشناسانی می‌گویند ذخایر نفتی که به‌راحتی قابل استخراج‌اند، از ذخایر تقریباً هر منطقه دیگری در جهان بیشتر است.
مهم‌تر از آن، گرینلند از نظر امنیتی و دفاعی، هم برای آمریکا و هم برای اروپا، موقعیتی بی‌نظیر دارد
🔴
هر حمله احتمالی آینده به آمریکا باید از مسیر گرینلند عبور کند؛ جایی که سامانه‌های دفاعی ما می‌توانند پهپادها، موشک‌ها و حتی سلاح‌هایی را که هنوز اختراع نشده‌اند، رهگیری و منهدم کنند.
🔴
گرینلند از نظر زمان هشدار، موقعیت جغرافیایی و میدان دید، شرایطی فراهم می‌کند که در هیچ جای دیگری از جهان وجود ندارد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/152650" target="_blank">📅 16:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152649">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
خبرنگار الجزیره گزارش داد که نیروهای ارتش اسرائیل در حال پیشروی در غرب روستای صیدا در منطقه جولان در حومه قنیطره در جنوب غربی سوریه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/152649" target="_blank">📅 16:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152648">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
بر اساس ردیابی اطلاعاتی منبع باز، بیش از 19 میلیون بشکه نفت خام روز دوشنبه تحت اسکورت ایالات متحده از تنگه هرمز عبور کرد. حملات ایران به کشتیرانی در طول روز ادامه داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/152648" target="_blank">📅 15:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152647">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a4914da11.mp4?token=rkyv7d1_nG4gm-I6hNflq8_obhZcNaAFa0zS9fmrhnEIsq4Q59m3qtNWOmLkqIlc6mmhzXztueJsPM2AlCAazHZTuV_t10BZbaX-_hcB9HcRXXR4S8e9ZEi-jut-NzqASZvuJtZCbk9BKpNprbREivGnZJCswNTfB7bqNUANEYTF8dwhuaTxfBvvu2qp539_DRDlxLw7BDYq_dTtIU0ixNFXFNwD0bBDP3RTZgkVz5fRi6msVRZjeBqeIwr1HIuZQcgEMIL8nzUewWx5rh6Lbb1TxMB6ZTcZm_WFmj7wCrL9IrcTMQUwGqN2UL06TjgMefhtIJi5jUCOGblLkNTCbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a4914da11.mp4?token=rkyv7d1_nG4gm-I6hNflq8_obhZcNaAFa0zS9fmrhnEIsq4Q59m3qtNWOmLkqIlc6mmhzXztueJsPM2AlCAazHZTuV_t10BZbaX-_hcB9HcRXXR4S8e9ZEi-jut-NzqASZvuJtZCbk9BKpNprbREivGnZJCswNTfB7bqNUANEYTF8dwhuaTxfBvvu2qp539_DRDlxLw7BDYq_dTtIU0ixNFXFNwD0bBDP3RTZgkVz5fRi6msVRZjeBqeIwr1HIuZQcgEMIL8nzUewWx5rh6Lbb1TxMB6ZTcZm_WFmj7wCrL9IrcTMQUwGqN2UL06TjgMefhtIJi5jUCOGblLkNTCbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواپیمای مشاهده‌شده در نظرآباد آموزشی بود
🔴
درپی مشاهدهٔ یک هواپیما در آسمان نظرآباد البرز، مشخص شد این پرنده از نوع آموزشی فوق‌سبک و متعلق به فرودگاه پیام کرج بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/152647" target="_blank">📅 15:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152646">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
مرشایمر، نظریه‌پرداز روابط بین‌الملل:
این احتمال وجود دارد که عربستان و امارات، آمریکا را برای حمله به ایران تشویق کرده باشند؛ زیرا تصور می‌کردند می‌توان ضربه‌ای «ناک‌اوت‌کننده» به تهران وارد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/152646" target="_blank">📅 15:36 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152645">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac89bffc3.mp4?token=XQN8WMkNtkNmTuXVkzY4ePPjX7eX98H_Li8Evi-021t6PpocnRW5fYjJ_pg6W0NnvK8wedxVy_YDKWTobbIxD6ZKrNt6fmLLuVHZU-XYixOO6A2U99Ge__rUwcQLT6r6SaPDoch_iK1MMWMSPIgMOK7aYRgsYpeNihGSN0f9h4KmbvIh4R8zYgUE0OGDpvs4wcJIDLEMRj_TgL8roxDdpX5CwejjNxaRATiHfbaUUnA6Sy13y-8ubjmxLbKB-jum48GTCc5my1WjBNaUKLGjURFQUKnY7GvngZeDMp8N9r-1fIL_Cm4aVnjjCo-L3CxHJTS7cpnrHsKrHRTd3XxEJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac89bffc3.mp4?token=XQN8WMkNtkNmTuXVkzY4ePPjX7eX98H_Li8Evi-021t6PpocnRW5fYjJ_pg6W0NnvK8wedxVy_YDKWTobbIxD6ZKrNt6fmLLuVHZU-XYixOO6A2U99Ge__rUwcQLT6r6SaPDoch_iK1MMWMSPIgMOK7aYRgsYpeNihGSN0f9h4KmbvIh4R8zYgUE0OGDpvs4wcJIDLEMRj_TgL8roxDdpX5CwejjNxaRATiHfbaUUnA6Sy13y-8ubjmxLbKB-jum48GTCc5my1WjBNaUKLGjURFQUKnY7GvngZeDMp8N9r-1fIL_Cm4aVnjjCo-L3CxHJTS7cpnrHsKrHRTd3XxEJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وای‌نت: انفجار و آتش‌سوزی در کارخانه اینتل در جنوب اسرائیل
🔴
در پی انفجار و آتش‌سوزی در کارخانه اینتل در جنوب اسرائیل، سه نفر زخمی شدند.
🔴
همچنین گزارش‌هایی درباره نشت مواد خطرناک منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/152645" target="_blank">📅 15:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152644">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGPMSVeRC_2ZWTeB20A3W9_WbCavcU1ytvxR4fMSYHujQhJSncVZYhkyZ3Z0Zfa9Y1KHv6AmKJkMqKbGow1VpstDHPo3nPAfwMez4O9Y14nkwzs0VdQCVPzWNgblqjjm7XDW2ajt6Kyv7Ia-aixDET2ThtNUtvajclmRULDB0YWW8qfUpk3ZdyUDYDRw8aBDSeFazxbdcM8D6blQTFAJwJvukz0yJjv7lvK8T1LvxbiMLnSYAY9ja4Kw-JRZxovp4DK_h92qpN9Fz_rEHdmegGXyo1ZwLBpytP9VcJUIolBC-aJrHKhyqvapA3OXKSchTTh3zS87VDHc0ypzkZZ-tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۳ هواپیمای ترابری نظامی آمریکایی، بریتانیایی و ایتالیایی به سمت خاورمیانه در حرکت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/152644" target="_blank">📅 15:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152643">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DL0AXsby4XFvtpqe0HauIVITekOwApxEDxyj23FyeLz7Goe0riRYr7elg8TjbITEp_ZffmCq7iHRL_MveCCc9cr3FCopldI8jHdhT_7f_S2zUWUFWhLNK7Awr5BjkRQlGRGMxApyJoSO__x879xfviU-1G9WTs6za9FGjLb7gBYJzVYVyA-jUECudt7oUCy0xUEpUcH9CwIEym1ADuJhxO1U8RFstKT3RjLBCEt-j3AnNYD2HS9kNuInj8QDmvSOCZn3EnZxDuMQW2VnPxb3eXsioyigNNhR22bYIv6rLNUxqbdYukD2flXrSJya6J_8UDiJ6bUUG1fxv2WytsHlLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان: وضعیت صادرات و واردات کشور و فروش نفت عالی است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/152643" target="_blank">📅 15:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152641">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VznUNT8PU-mQxHpOh_KhyRNC7m7qGgSLyndV5YDJtQkGreCtdfI2Z5Rr1RlyVIFM1X7MxnDSqeVE9YvJmPV8bUeUxcSHTLz_iSBzOWaedYVMwkef3gp3iqMfNp4WqZVCbk-3ANbcJHOmnjQqsZB4EDCntQuQR9ydptDtEq9oW43FQDYPBN7khZG5duXZ62VSaCCMVzqmUIXLv5qsmxmT6i0R0Xx8yvZwffkd34QosqpMNwqwtscijmtw-n7fWjv9XQcLu0IoukmKcUAIYjqaxyHCaW5UwTBnwD6l_oC5Qq0FGWnpHEZHBXyg9me2H4F3tcTZPpfbYUvsAk53coV13w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XGqAxShGndIsKyn-k8thWhhJaxzWrh5wvGYSyQbbBdBvTz-jnSJ5CaduMOvUl5pFSEr6TPAwt-dKn0Ex5xOqk1Fnrs-gp002LyH_KySn9TZJV2uNou9S17Kw48ekGixzUFlrPoJ9xLNKRcTRdk1ohJiz8w5KEzcdMWKzG-zXZ5YkS_79vCPfmH_XaK242SJIpT3mqa0RIcAitZRwWfS_EPW8Hj5yKTIUutZhRlvaTHvjrns_AQYh9GkKJ5x4jOI-ob6IVqQJ_4knDIF2Puw9WlQdW-I9_75P0-FEmItg5hDwtoaAnMzEo8kUr8hjeb-lOYmgbFlxkM8QwKPe6oYqAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر دیگر از لحظهٔ برخورد کشتی کانتینربر با مین در مسیر تنگهٔ هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/152641" target="_blank">📅 15:17 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152640">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ترامپ در حال بررسی قطع اشتراک‌گذاری اطلاعات اطلاعاتی با اوکراین است.
🔴
یک مقام دولت آمریکا به رسانه سمافور گفت: «ترامپ واقعاً عصبانی است؛ ممکن است دستور این کار را صادر کند.»
🔴
این موضوع در کاخ سفید در حال بررسی است، اما جان رتکلیف، رئیس سیا، با آن مخالفت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/152640" target="_blank">📅 15:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152639">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
کاتز وزیر جنگ اسرائیل : اگر حزب‌الله به ایران در حمله به اسرائیل بپیوندد، ضربه سختی دریافت خواهد کرد و زمین‌های بیشتری را در جنوب لبنان، به ویژه در مناطق النبطیه و لیطانی، از دست خواهد داد.
🔴
این مناطق به بخش پایدار امنیتی اسرائیل تبدیل خواهند شد. به ارتش اسرائیل دستور داده شده است تا برای یک عملیات زمینی آماده‌سازی شود
🔴
همچنین، محله الضاحیه در بیروت تخلیه خواهد شد و زیرساخت‌های آن تخریب خواهد شد. بیش از یک میلیون نفر از شیعیان به آوارگان داخلی در لبنان تبدیل خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/152639" target="_blank">📅 14:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152637">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZCR0nmBNpH9WrCPlrcnhmC6hXB9jOTOXKfbJSBVzT5vdZDs5jpw2PY22uSk0q4jNMGPC9tRuE7iw3L3S_t9bf5gZx8bMRuYndZ0u3LXnpnEGMgc4u4KK3dFAppSPW2GdR_XUPttka7r3Fu3dockyxGj5KGPtNXZavccrxr7TifR9s73vGyUZqfTkK8k6ewuxXJsM6RUHiBZNB5yx7x75C6_BZ5dXGZCwAgQy7wj5IGX_ZXSmvFRT6nooTSEh0-C025ZkqPC7meSjmsi5siY2qW2qy1x4gjqL0IMX6G85_aGQZJ2d7tjBbaog_jUoI4HDpH_KMkNoncqwudCVjQ5aow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dgHGu5aS_agIrtuY2EAXIuvp-_C8pnmjJ5oY84GzfjKdGGhQ1Et-AJcXnxBcOeouz83J4GzEOeJ46NtiO3GneqMXR0EzrSokiL2J5TtZYBC7wk6SfSkotLnqvzcU1qvKzfqdByJuYZ52AAItk7mz7_erPUHTBBPpdSRNePm_fdQ3Mp1gMfzDj48Xm9idon9Z4SVrhCT_Ly5qSzJgS9-8BhpGhD1tl8LMNiG9ThaT-N5NUeYvu9ZkqUxrC-btp5CgImY08PRN5rQLYCVyqqjnymhEbZtEfr-jv4vD25aQ4GA9aB3X6UjZPMp_jnJ46vlm7QUDyHZotBf4t0XV61Zngw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سامانه‌های پدافند هوایی فلاخن داوود در شمال اسرائیل مستقر شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/152637" target="_blank">📅 14:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152636">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رویترز: مقر شرکت آرامکو در ظهران در حمله روز گذشته خسارات شدیدی دید و آتش به چندین طبقه سرایت کرد. به کارکنان دستور داده شد از خانه کار کنند و پس از این حمله، بخشی از فعالیت‌های شرکت به دفاتر آن در خارج از کشور منتقل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/152636" target="_blank">📅 14:32 · 22 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
