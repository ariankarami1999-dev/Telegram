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
<img src="https://cdn4.telesco.pe/file/R40UbZuKXA7oHquC-G2mIX8M-XVY2G5K45mKiYWzmyM7Y8IC8aF2lKcOZKgPfQOhstpgzVBR84thxhnEadibitDgChbtUtpP0y7kzdVPWLkNL4pbosr9P5SN00hk0GFDiztVgAXU9SFR3MIM4wb8CwxTMKTnSbvWD4YfpxVIf5NU52RKCNZAYm46QpU9uTRmQn9AL6naKhUbevfmlH6QOUphOr-ChHMXJIPZPsOt5mL8yja3Isj8jFPcjw5FaIOPJrXqjqKeUX2qVogNzpFGSinYqLAe52_VYS7NoXiGTMcPsX_lP4g4se35PFVZL01yXA7KHth-kSkokaNx0LMZtA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 180K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 17:32:06</div>
<hr>

<div class="tg-post" id="msg-67905">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f43409a1c.mp4?token=osHH0o5DQ9Vb3pazSjjxaB9oOKa2Peilp1Y7yO39h9ipmLcai_0_yY8UN5h4XoDx0X10eyeq2omw9LXI5oT2jyah-bZGCp8csp4GGeL7VGETO77vgOwNR1LXeMfR0CuQsAWENwpySrhm8uwCNCQDJnpRsH6UzBZxmQLE8KH9OmmD2LDwyjFPmANjOWYUqFF_QjvyfE95pDGIt65r7QkjOukTQWAIEpN0uNOokK3arjhG9GW2PxD1x779BAS7EUBCip_ZzNpCyDC3qADcSj0IdcGq8vpknSldiEne8TepkKn58Nz9KOMPcqvnEANYNz1cPQp_-Ps8cXww1bfVMlN0LSSpLGQg_SOmOlu5rpMU0JXri8zdSXKNVQvcK2NtuvMCEbSsqPLQcyvkzGy4Uyj96tknmQNq324ACbwwTi0FoIWir3XcYWmdQ3ysCs5z_WM6bM26Z148NfPhi6h4vSq7xe2OcCbdTYfgn8Oesd_PlCiFFz0BzlvYm-4-QKQQgp8gqBFB8jDUOd97kfd5ah9RMdI2a6-HAAZq9gGGcyg1ANXqHJkTMbo0Ctl9FGH2PMRr7CW7rA79YHbiteCv0dfonBeCl1KBz1A6Zkab4O1JRvGx9wFFqPKB7x7rAsNrJPcaCcDo1W6X_CAK8ndcA2j9MHjbLOg80D4MpYQzMiaOqyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f43409a1c.mp4?token=osHH0o5DQ9Vb3pazSjjxaB9oOKa2Peilp1Y7yO39h9ipmLcai_0_yY8UN5h4XoDx0X10eyeq2omw9LXI5oT2jyah-bZGCp8csp4GGeL7VGETO77vgOwNR1LXeMfR0CuQsAWENwpySrhm8uwCNCQDJnpRsH6UzBZxmQLE8KH9OmmD2LDwyjFPmANjOWYUqFF_QjvyfE95pDGIt65r7QkjOukTQWAIEpN0uNOokK3arjhG9GW2PxD1x779BAS7EUBCip_ZzNpCyDC3qADcSj0IdcGq8vpknSldiEne8TepkKn58Nz9KOMPcqvnEANYNz1cPQp_-Ps8cXww1bfVMlN0LSSpLGQg_SOmOlu5rpMU0JXri8zdSXKNVQvcK2NtuvMCEbSsqPLQcyvkzGy4Uyj96tknmQNq324ACbwwTi0FoIWir3XcYWmdQ3ysCs5z_WM6bM26Z148NfPhi6h4vSq7xe2OcCbdTYfgn8Oesd_PlCiFFz0BzlvYm-4-QKQQgp8gqBFB8jDUOd97kfd5ah9RMdI2a6-HAAZq9gGGcyg1ANXqHJkTMbo0Ctl9FGH2PMRr7CW7rA79YHbiteCv0dfonBeCl1KBz1A6Zkab4O1JRvGx9wFFqPKB7x7rAsNrJPcaCcDo1W6X_CAK8ndcA2j9MHjbLOg80D4MpYQzMiaOqyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از  فعالیت موشک‌های رهگیر پاتریوت بر علیه موشک‌های ایرانی در پایگاه موفق السلطی اردن از دید سرباز آمریکایی طی درگیری‌های روز‌های اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/news_hut/67905" target="_blank">📅 17:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67904">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b2f989ab.mp4?token=TuxnvlKbLE_WVYhEKZXoqvufc9mgd3O8m2nx_tvnAnaV_HOI5Ej3xrdB699NPTyi3erwx1GjFJfkD2G5IGP4JtWgVhSGK36F5XPxtNfHKXOlsd9pMWA0K55yuntzqXi3HgmFuF_Anix5TF6yVIo4nARnK-DPVTNm21-QZr3Avyfdwd5es9vrHGRfTuu3HschQLFT0zkJHwwEXXvua5ZbQ_mxA-eedtwpBlOK_AwnHZrRZljj1_z4CgUcArADCileKruBB7Ib3NxKjcBSQzok0ODH83SmkRl350NscAwidza7QhlcasG4dyB_WV7sxiUwwlDxJwG1OJm1m4lRwDhqJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b2f989ab.mp4?token=TuxnvlKbLE_WVYhEKZXoqvufc9mgd3O8m2nx_tvnAnaV_HOI5Ej3xrdB699NPTyi3erwx1GjFJfkD2G5IGP4JtWgVhSGK36F5XPxtNfHKXOlsd9pMWA0K55yuntzqXi3HgmFuF_Anix5TF6yVIo4nARnK-DPVTNm21-QZr3Avyfdwd5es9vrHGRfTuu3HschQLFT0zkJHwwEXXvua5ZbQ_mxA-eedtwpBlOK_AwnHZrRZljj1_z4CgUcArADCileKruBB7Ib3NxKjcBSQzok0ODH83SmkRl350NscAwidza7QhlcasG4dyB_WV7sxiUwwlDxJwG1OJm1m4lRwDhqJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب شدن سرباز بر اثر انفجار اشتباهی در تمرین پدافند هوایی روسیه(نزدیک بود همرزمش رو هم بگا بده)
👅
👅
@News_Hut</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/news_hut/67904" target="_blank">📅 16:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67903">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdilalHrhKLhH7bidO7-k_5VSdW3re6k2CijH1dCl60pTqvMDPcfslW1wB7f5nkPDvkuaLLIf24JYRxRxo4rylUr3JPhw7YZPF5G8_55VKrDl_EX0tiVivun5cyokNcmufLVDvGFK2xvpHG6U86KZYksNENzXG9vAiT_CjEGW4o5_Nalrfx0uLa2LClFc7656qc5RPK3crpFW6XK_NY3e7K6FjEu5ScbnHlXo52tU8tZxlyN4eSaKPTGStdauU242cj3mIl0RvPuPN92izihEO8rOcHHC2zsNs6Mqh3hZVUfC_IfT4C6fElf3kNQXg1BSFFn4Zq_PXBIw8f8xJiZxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
تنگه هرمز برای تمامی کشتی‌هایی که قصد عبور قانونی از این آبراه بین‌المللی را دارند، باز است. نیروهای آمریکایی در این منطقه مستقر هستند و آماده‌اند تا از آزادی تردد دریایی اطمینان حاصل کنند، علی‌رغم اقدامات تهاجمی، آزار و اذیت، تهدیدها و اظهارات غیرمنطقی ایران. ایران کنترل این تنگه را بر عهده ندارد. ترددها به روال عادی خود ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/67903" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67901">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyeUt8Lzx7vLhRvpyLWmIqz9VkvEJDFZvX-84Rn2415lpSwoOANAxxlgUa3QzaMIlL47pS4bJPbRmuxZDpVozLCemRRltpoD5ZcH0p8tsFUapey_FzTEhitkMw7jf6McRLjkEp-dxSln5UhDbQ3k5AQWZiFDodsqo7Rlf8rDLYgZ7nxgtUAPV24n1HRdrP4lmThGMn98CMfMY3z964USVbjXy8pbhE-yJ6l0p71OxWhhNNtzWAqMUX4fRZU5aPVv-aGmh-NzBR9hLiUjrCoFFtfsVGHWJL9QbdIQGll6GgC5tQB6clpZZKAVovQbfZINpSnRZW52drrGN5cMaMGDzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaa15fb6f3.mp4?token=bbWN_PnA3EgZCCOddGwDOObZLgqk-x9uuhdexS2LGuazOOMdt7S0bM3Hob_eNj6j7TYpV3xAfSaQICfXN4iaCljzavv7jTNHEYYYSLuPU4M076q4pl11nKZ4KT_dr8Kok4yvM1QElAY38DeYW_Uusqi8dBMeAu3hAzIzclDRthog6XfFj7aYkSBGW4qZY2tjKW9iJ1DOjxKLiH09JPG7pwu6S8copQSeyVe9gUZzQWsNazxGo_JdWgg-EuJlKPPfMAysWB-AFhHynCs-4tZ6iVyW77P2-oB-Fw09XYY9MMB67TSSpS-TL4ayGriIilcB2dkJBj5RmxvK6x3NnrtrYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaa15fb6f3.mp4?token=bbWN_PnA3EgZCCOddGwDOObZLgqk-x9uuhdexS2LGuazOOMdt7S0bM3Hob_eNj6j7TYpV3xAfSaQICfXN4iaCljzavv7jTNHEYYYSLuPU4M076q4pl11nKZ4KT_dr8Kok4yvM1QElAY38DeYW_Uusqi8dBMeAu3hAzIzclDRthog6XfFj7aYkSBGW4qZY2tjKW9iJ1DOjxKLiH09JPG7pwu6S8copQSeyVe9gUZzQWsNazxGo_JdWgg-EuJlKPPfMAysWB-AFhHynCs-4tZ6iVyW77P2-oB-Fw09XYY9MMB67TSSpS-TL4ayGriIilcB2dkJBj5RmxvK6x3NnrtrYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از اینکه صداسیما رسما مرگ لیندزی گراهام رو تبریک گفت
فیلم تبریکش بشدت در رسانه های جهانی وایرال شده و گویا برخی دنبال ربط دادن مرگش به جمهوری اسلامی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/67901" target="_blank">📅 15:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67900">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFdw40W9grpatxFeJ7v_7Wm4wGAld8aIG6kV-8KWs1a2BJpaUqK_YS78QTRkmB9esGrCVTJDioEQNDivKj5urfomolVVx8LG3MEPq0dMlVL0JjriegcWL6uWnp1xJnvUChuKd5Ag6nlnI35unLcw5tGyRFmSZ1NbFhBqs8KkAk6AkY0Ffe_7d4N5I6YOH_P13-5dm0wuy56nMAyTFeh0bDErsvALsMXvaGwR60k0Ci2YzMeBHiYwkrSe8l6V87Cl9I9SgP7pTyvox3fq-aNx9USMIRR20VsbzO0AhGRrAOSyI7FPsunkjhPb_JK1fqbmKzODWLw-UTQBabT4PnpIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پس از شلیک چندین موشک بالستیک به کشور قطر در طول شب گذشته، عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، ضمن ابراز همدردی صمیمانه، به خانواده و مردم قطر تسلیت گفت و مراتب تسلیت خود را به مناسبت درگذشت امیر سابق قطر اعلام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/67900" target="_blank">📅 15:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67899">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f465c542d7.mp4?token=FY_kaN2JVs_ibE1RSt4Y7Sy12qJfj-sp5ZlS4NRiKXJZCg-q_ugEO3scJP0ZmNHLmbqtQNfn25UJuTAFZw9l-E_i6p0kVO2xIG7_M_UhOqC0I_IDM-zkTKF9_RHT2pM_9XcKt-HSb368-eh-kebT0Zf8PGFBgE-I5bBRLi33_39ts53zae75kBpCy3Jvd-h8BvCoqk43evMnQ3mSa0jRGOYR-sWACETwcTnCnDyDF27tb5XH5mWR2MraIUyvOEbRNHVqdaMiTPr4zQ8RWJ67Id6Jpuq_tuhcx6hFEQnyHJ7gvgNdQgNPNSrKtBf5NbIGlSpwr6rol8eKfdtGjc7OAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f465c542d7.mp4?token=FY_kaN2JVs_ibE1RSt4Y7Sy12qJfj-sp5ZlS4NRiKXJZCg-q_ugEO3scJP0ZmNHLmbqtQNfn25UJuTAFZw9l-E_i6p0kVO2xIG7_M_UhOqC0I_IDM-zkTKF9_RHT2pM_9XcKt-HSb368-eh-kebT0Zf8PGFBgE-I5bBRLi33_39ts53zae75kBpCy3Jvd-h8BvCoqk43evMnQ3mSa0jRGOYR-sWACETwcTnCnDyDF27tb5XH5mWR2MraIUyvOEbRNHVqdaMiTPr4zQ8RWJ67Id6Jpuq_tuhcx6hFEQnyHJ7gvgNdQgNPNSrKtBf5NbIGlSpwr6rol8eKfdtGjc7OAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش ممد سامتینگ در حالی که تندرو ها دارن شعار
«مذاکره با دشمن خیانت است به میهن»
میدن در مراسم چالسپاری خامنه‌ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67899" target="_blank">📅 14:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67898">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
نتانیاهو در حال بررسی سفر به منظور شرکت در مراسم خاکسپاری لیندی گراهام است. احتمالاً ترامپ نیز در آنجا حضور خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67898" target="_blank">📅 13:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67897">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVFtAQ86MAylaXfE7xOaqQ3mHT6fOeoOEW2DM7IobdnCoVwfo-d93goVNcNkv2b-PCYCzzNWOha40_pn_Bqu8QAKblkDrF1Xw9wxIMfhDA8oOf85yxA5fOwc-xKoNZBC3NJrIbWqxwPWPWT7hADqt5GYcKNf021KJTkesZFqaV8pn3Okb_u_RwX8l2ol-N6XYm_V5d_UczPLFxrXYR4tBN5YMO3rKTySzd15pmIM8h2VoLUR9Q8QBD944DOINdGvKDvjJBftGTQnE3XKwpDvyidhi2riQOdGyKBcEvQQjvkznX6yC4bnNMO6fqgaHgvK3Z1O1jng-WkeMYJwROWf-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حمیدرضا دهقان از اعضای پدافند ارتش در منطقه جاسک طی حمله بامداد امروز ارتش امریکا کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67897" target="_blank">📅 12:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67896">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvULATMieiLPn4GUZSNcv6Mc5K65DginSdhqU8Yk1YUM4ZpVxwm8W6KLY5_XSV--29MFEKc11Os2MQRGrKRrR3zyjXRA4-XhzLka-Vez6jVMIhmXR8dWcvkMDxJRsH3CPaL__QUxDw3R3fjpIq-GHgbfJ_HRhVYtBbyDPH3i4Mi4Qn4Eay4mlqb7G4IRo0k-TDiz4Hbzz6VczWwKqEJUfs7GNJRAxaEeFOM9IA1rz17u4Ov0j4CMPqZTjUQjBLAAjxCRybUrgk7yNgkGk7sfWSrQi3BncNq_uLnDeSV_rQKavPGsLMCXfApewE1tpLa7TChOWMiA-MAvmE2jLAem7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
واکنش مرندی عضو تیم مذاکره کننده به درگذشت سناتور لیندسی گراهام:
چقدر بد؛ من میخواستم او قبل از رفتن به جهنم قیمت بازار نفت را ببیند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67896" target="_blank">📅 12:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67895">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nF51OQyDSp1xoZijJUQBXccZOt-aQ_8tKQtdo1w47FLcLRc1pjREjqAc0qy7L6c28qLz9Ohng7wL59REulM201hrmJNfz08PNhQXCfqvVumC71iwq4Rc4uB6vEwiNCzClnsS_EjHPwl2KTKbbIAQ63ABgLXWCIZODW0L8rpe7dYvVYvTaANg3CG5_MLsOc93NNrN2Euqe0_Wj9CgOY5jCJVZw3hHk0IYDJ0JDH_8GtyUNn7ozqJLYjx_h9fiJwnE_8AytGcjIALjDgJL6CXBohhQjcAc1JwzW3idCcEvaVVYjrs5H32fjPhL93opd7Tz0nP-Vs40Uhwwp0h1pAsCPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
👑
شاهزاده رضا پهلوی:
از درگذشت ناگهانی سناتور لیندزی گراهام، دوستی ثابت‌قدم برای مردم ایران و مدافعی سرافراز برای آزادی، عمیقاً اندوهگینم.
در لحظاتی که نیاز به موضع‌گیری اخلاقیِ صریح و درست بود، سناتور گراهام در جانب حق ایستاد. آنگاه که دوستانِ واقعی کمیاب بودند، او در مبارزه علیه استبداد، در کنار مردم ایران ایستاد.
او از صدای خود بهره گرفت تا اطمینان حاصل کند که صدای مبارزانِ راه عدالت در راهروهای قدرت شنیده می‌شود.
حمایت او از «انقلاب شیر و خورشید» ایران، لقب «عمو لیندزی» را در میان ایرانیان برایش به ارمغان آورد.
یاد او همواره با سپاس و احترامی عمیق گرامی داشته خواهد شد. ما مراتب تسلیت عمیق خود را به خانواده، عزیزان و همکاران سناتور گراهام، و همچنین به مردم کارولینای جنوبی و ایالات متحده ابراز می‌داریم.
روحش شاد و یادش گرامی باد؛ و باشد که دیگران راه مبارزه برای آزادی را ادامه دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67895" target="_blank">📅 11:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67894">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTcdl1PxT_ym1lUzYmLFKk0kM-KMwTNj5WQoSEFOQqfdMnacomg4QJ6cAiSetwUFIWpNdX7w2R1o6A9RNmaS85xntGpTQ8RzYOqdEn_srUMfZxeMELP8EhkhBL4tKEmrX1_di9X2x7aYDr0Xn5UEy0OyvhXkliO-_ZBkANw60685jn-6OYCgCiSTBniY44gl3UcAezoS_ncRxJJkfp7VRDqbmXUp8g5h6RtPaCdOfX4kQh-yd1boSZ2WcePN1BMEFu7lcjeCoKntzg61adCFIJlHrHqE34ezozxLdQHL_wvLCoTw6C_-a257I3pQpS9LO5AE7nbz0W1aL8G2GG_fvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو نخست وزیر اسرائیل در سوگ مرگ لیندسی گراهام:
من و سارا با مردم آمریکا به خاطر از دست دادن دوست عزیزمان، سناتور لیندزی گراهام، غمگین هستیم.
در ملاقات اخیرمان گفتم: "لیندسی دوست بزرگ اسرائیل و دوست عزیز من است. ما هیچ دوستی بهتر از لیندسی نداریم.
لیندزی فهمید که امنیت اسرائیل و آمریکا جدایی ناپذیر هستند. او زندگی خود را وقف دفاع از آمریکا، تقویت اتحاد ما و ایستادگی برای جهان آزاد کرد.
اسرائیل یکی از بزرگترین دوستان خود را از دست داده است. آمریکا یک میهن پرست بزرگ را از دست داده است. من یک دوست عزیز را از دست داده ام
.
قلب ما با خانواده لیندزی و با مردم آمریکا در این زمان سخت است. باشد که ارزش ها و ابتکارات او همچنان ما را به سوی پیروزی و صلح رهنمون سازد و یادش همیشه پر برکت باد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67894" target="_blank">📅 11:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67893">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5JO8oj6TiPXfxFXFBEuLvRR2Bsuy94cEGAXykRSA8cSSKRZgQIMLhJshrS3Q-oyEmr8H400ayLSp9v4tC7lGeCNC9Q0DVt_n-d-OIvTPIhv1zVGCLDQTiZrCIamQYMKZSOesEEg5C2msFvjd0KXB03mtXO-M6G0Jj9BX30NKyei9Mux2LHFV_Nqojlac9BvbgVQIN89ttbiVBYk6v-gWzQIeyB3-IyFQDVXUrAxOfQltC_2YAH4Zc9glqexmN9YwJnkWLYMQwlGujeQ3dg8Wkuh0-6qxMNGUsWJ3pEQb9KwS-F3WSv1kAXtpVCjl9bpeH56Ig-XFb5fkUYGDH0kdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇺🇸
پرزیدنت ترامپ:
سناتور لیندی گراهام، یکی از بزرگترین شخصیت‌ها و سناتورهایی که تا به حال می‌شناختم، از دنیا رفت. او همیشه فعال بود و یک آمریکایی واقعی بود. ما لیندی را بسیار دلتنگ خواهیم شد. جزئیات و برنامه‌های مراسم تشییع پیکر او متعاقباً اعلام خواهد شد. چه خبر غم‌انگیزی!
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67893" target="_blank">📅 10:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67892">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDxQXll24mOFqniywF86zHqRxVkVRtLfGz6kh33rdtqOYUSN4kmNh2NkmZRKTrF8DTUISOULKLrca2BejnbnfV69vdDUqqyjNVn8NZOMjhPlOs0WW9gfhdQ0ajKovNPyRPDmQ02BCSVejSSRpx0PAYUX1E0uetnpZg8DMFetJAItkOVbGrSNeymMr4kfgmlHiVswpPch_7VDETiU_-S6ML10PN1g-iQCO2UKbISlb8cxk9Gnr3JxcxNrfVQz9n5FGPjr607dc6UQFeWCc6MhwmjNAHs2Tz-4nL3FhTE4S5XSUPgtbovAKvpbbNq-mCFKWJyGUKWB0amDAULUehCOWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ان‌بی‌سی‌ نیوز:
در حال بررسی صدای ضبط شده از بی‌سیم پلیس مربوط به واکنش نیروهای امدادی به یک مورد ایست قلبی در خانه لیندسی گراهام است.
این شبکه همچنین گزارش می‌دهد که عکس‌هایی از شخصی دریافت کرده است که به احتمال زیاد لیندسی گراهام است و او را روی برانکارد از خانه خارج میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67892" target="_blank">📅 10:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67891">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CB61_-4et-npGTWkU8NgnGhAPRZkL6pKlsoj619ZtOvrqSHNw449PhnBFTsWk4MFHyp0soElm2Cw6JWHJdzey3raaxY8UvF5QFU9kz4z-SGQevsjfgFWneJ2Opoyiy_66t0BbHYP6Av3S9F9l8ls5UuXd9A6E4qKy-q67dSyphukUokdJVt7XR8bdrIRndcnYBZrP71RhcILiBbEuN-j-p2xATpBlaJ1ft42EXMslMxTFk4RaX2XwvKReC4LP0OqILPXmJ8ZNTswX3ZfKWm9bVqIaJ4ydUD8n0fjXhb4WgYJLQhcL2BW8u-Si7X2sran_uJiYiliUySlxtQ7O-0EJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#RIP, great man
🫡
🖤
#hjAly‌</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67891" target="_blank">📅 10:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67890">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHG_1B8n8RvtXkKBE7rWeTqDsRP47F56MLCmeLzAlNbXj6NZS05ytPJeYT0HNrpuwypBAS-IbtmUyOfWRs-66qyL-A12KAAQVmKNcS0daiDN6mPl1n1yIG4XpqWjyBcTWug5dcwclj7EvKv7jhagHTfdp8z9oK_BllCFS1VU-W_vDMpBd5bODeBj2Ae80OPzfJn6RQItkAzdTSpCbkcSBbo4ye8piJ9pIAjDUtJPS5C5Fkt-1t5HiRKpHviNSYR1kh2WH8555W2PbdPjFz5EknO3F30i5AFwobZi96Gk71-rSzezGNVRUL_Ej-66qO3FifJOWvbP_o2859JOnMwvsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
بیانیه دفتر سناتور لیندسی گراهام:   دفتر لیندزی گراهام، سناتور ارشد جمهوری‌خواه، اعلام کرد که او شامگاه شنبه پس از یک بیماری کوتاه و ناگهانی درگذشت.  @News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67890" target="_blank">📅 09:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67889">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJTJxusanixgKxANJOn2Z8UqavpcDW4MrKxUrX_2sIeDHRr-KJATF76LAnp7DM0ntAzU62wbf3G7JBgZMaGsnu-qODMXxfbD9gNghxP40zC8Nqd3Zx413lHp7B76yfILIzJKi6grFO8_Z1dn7Jx_fYGvvwfYdf-xa1Cr-aibGDmHJLBRsTnXoCtBLCQ46d4HyAwIgo_XCdWtRyiUXmfWQUdmtHaUT_W10JgPOcpLdO2Fq7n3aPD0iUXC62rs5GLfqn661mp5sXJrLV8Xpdp2s2X_phA_Xa59-F7L7ooGBoWNWcJUlMcamLX37nVgwqQXSnLGQiNuODckzPyyzDwBBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
بیانیه دفتر سناتور لیندسی گراهام:
دفتر لیندزی گراهام، سناتور ارشد جمهوری‌خواه، اعلام کرد که او شامگاه شنبه پس از یک بیماری کوتاه و ناگهانی درگذشت
.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67889" target="_blank">📅 09:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67887">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVMjXNhhi-NHuR80GLac8HYbXdzZy4spU5MQTiUwUyeX_wzM8lpYXw7V_WS5BWkBnrLyiIRPkIFujiU17WCa8otAUCUWP4foQIhTbtqoN39ihmQHmFMEBXvj_6Mi4683ivFY6ajKGk1mNtPs23iThd1Ozfg14VpgLcdG2H1VTjFQon8e0u2lhsQoDPAIkg21KLl1QzEuYXTMABJTr_cD1vhkV_x39k3oCpX_OS-3QyRMhnqLCqd5EfO-0j_mvVMvM8BF3_tC31EDdYmRdzQ6GEoouxrx7NF8opaxbJOTG7pLL9lP076KeiQEqYyIzyYO2NioMsX5VkWLRpN_pBVxRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
#فوری
؛
لیندسی گراهام سناتور جمهوری‌خواه آمریکایی و از حامیان انقلاب شیر و خورشید درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67887" target="_blank">📅 09:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67886">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
تصاویری که سپاه از حمله به پایگاه های آمریکایی در منطقه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67886" target="_blank">📅 09:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67885">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/51a23206ab.mp4?token=AHAG5g2pJwwfcSRYzYvdvxbPDeusJAvZwJTWau0Wir2Q2VxNwG4S3pYe5i8bcSPkqBeg8avnIuDEa7VbHvypthz817HOyQDBGZYmTTMj9dnMHpfqLfQ2066r4jBFOMqUZtW58dNP9J9K2HsA5I3W9ZebrPBFNxQOS-Shs8DVhRwWoqzUrnZ-h6h4oXnFzNlOwpnnOs90MGeeZWgH1WGcTuETNiheyG9wsj18ACj2PGDZRQzM7bHJxIIBFU4SpIbnyzFB_y5N5Pk7eWmstYmV9drN1wwVJLPzj6RdaYqMFBXqt45p7ehvkeeq60Lr1DhImtpj-3FCmfCgNJdnZaMAxYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/51a23206ab.mp4?token=AHAG5g2pJwwfcSRYzYvdvxbPDeusJAvZwJTWau0Wir2Q2VxNwG4S3pYe5i8bcSPkqBeg8avnIuDEa7VbHvypthz817HOyQDBGZYmTTMj9dnMHpfqLfQ2066r4jBFOMqUZtW58dNP9J9K2HsA5I3W9ZebrPBFNxQOS-Shs8DVhRwWoqzUrnZ-h6h4oXnFzNlOwpnnOs90MGeeZWgH1WGcTuETNiheyG9wsj18ACj2PGDZRQzM7bHJxIIBFU4SpIbnyzFB_y5N5Pk7eWmstYmV9drN1wwVJLPzj6RdaYqMFBXqt45p7ehvkeeq60Lr1DhImtpj-3FCmfCgNJdnZaMAxYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سرباز روس خودشو به موش مردگی زده تا کوادکوپتر اوکراینی شکارش نکنه
اپراتور اوکراینی میگه: «نگاه کن لعنتی طوری نقش بازی میکنه که دی کاپریو جلوش کم میاره»
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67885" target="_blank">📅 09:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67884">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7O7-qLkfYWOHBltPeXc3djqJb35nVjJzjPYJvxVRzFqV85_lr5HvDbirnm4MdlN8IPKFxqQ2iPBJAanOVHNAgGucLeVZbnpA4oFKHRXaMGJ5bWuPU237nSPdMDEO_uT1utycWaZnph5RMQz-zWGHpdJ-MAEG9CbPk64cJIAC7AAhd1vO-n5Dm3eafE-sU-v_Tu4dKb7Vjv_DmMyoN86TK9ePKPYWy2lHCQ-c4uwvFKzJJIg_9l9zAkpw_Fp6hleY-SUSRImppCotZVm_qAiaDX3J5RA-H6esKu4zmqTAbkz9SGLTKHxXHE-vZxJUfmemkmwFQzz5_FLDi7ExgXXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
قاليباف: دوران معاملات یک‌طرفه به پایان رسیده است. به شما گفته‌ایم: به قول خود پایبند باشید، یا عواقب آن را بپذیرید. واقعیت در حال نزدیک شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67884" target="_blank">📅 07:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67883">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2431b44fb2.mp4?token=QFdu2H_R4Nk7otBKyVUIVgzkNfwPi-TSAniY273mIgOm8_Zgx1ocb8kwHCcx1_czbFAUjkXFenCneJIIa0tK6wP3jKzgtA2SGPrBUY8G3XGsR0D6A0XDoUfpOg4-X28Ispd3GJ3h5QaXGNQ7bNIy4hEwKsH1F2wvXzYzm7GkFYvVDdcDAIlVzF9MquaqKTxltohP8hBt_uAE4sng-Efc7wF_P-yDlZiTOxjwfjiEBXCl5sk9kyhB-bDLwWzf79z3gP7K1wBiBuuucdeidjiWovprrmueJIhKTJyy3oUZUwAYy6LeRTHOxz2BenXTOobp9K2A6T2kPJ6dYe_2e4BpEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2431b44fb2.mp4?token=QFdu2H_R4Nk7otBKyVUIVgzkNfwPi-TSAniY273mIgOm8_Zgx1ocb8kwHCcx1_czbFAUjkXFenCneJIIa0tK6wP3jKzgtA2SGPrBUY8G3XGsR0D6A0XDoUfpOg4-X28Ispd3GJ3h5QaXGNQ7bNIy4hEwKsH1F2wvXzYzm7GkFYvVDdcDAIlVzF9MquaqKTxltohP8hBt_uAE4sng-Efc7wF_P-yDlZiTOxjwfjiEBXCl5sk9kyhB-bDLwWzf79z3gP7K1wBiBuuucdeidjiWovprrmueJIhKTJyy3oUZUwAYy6LeRTHOxz2BenXTOobp9K2A6T2kPJ6dYe_2e4BpEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
ادامه حملات سپاه به کشور قطر
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67883" target="_blank">📅 07:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67882">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
سپاه مدعی شد: مراکز لجستیکی که به کشتی‌ها و سکوهای سوخت‌رسانی متعلق به ایالات متحده در بندر الدقم در عمان خدمات‌رسانی می‌کردند، در یک حمله شدید و غافلگیرانه منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67882" target="_blank">📅 07:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67880">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=CruRm8Q7w9QrtbmAgqSb4ETHSf_aJSXhvpYWSBm4bkT9Ye0wLsIGq0mRnc8L_y0Fb5Jb09xMDJIiAnib4mqot-08_hSINzWcAbGhUwDMz4rXR_OYatTxqpnPUl5C5jwynMCOQu6UAMmTyLpImy-xe97hiPjJGeoiuuWoMrbLOZEHRBKM7bckFPUCwhH_oGIyDctmUEIjNOUPgpPcUNPdMznpU8grcB6yvCBy5ms2isOh9A-B9K8k4gVsgZ4XHxSHZ4wamPoAUQDRtWfyg0piBXJk2eoG7L7ukxdiMYUUp-KGbzqkPBuW8XkwWu5pkbUINbNZ3BE7H2ZbEycSy6GB8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=CruRm8Q7w9QrtbmAgqSb4ETHSf_aJSXhvpYWSBm4bkT9Ye0wLsIGq0mRnc8L_y0Fb5Jb09xMDJIiAnib4mqot-08_hSINzWcAbGhUwDMz4rXR_OYatTxqpnPUl5C5jwynMCOQu6UAMmTyLpImy-xe97hiPjJGeoiuuWoMrbLOZEHRBKM7bckFPUCwhH_oGIyDctmUEIjNOUPgpPcUNPdMznpU8grcB6yvCBy5ms2isOh9A-B9K8k4gVsgZ4XHxSHZ4wamPoAUQDRtWfyg0piBXJk2eoG7L7ukxdiMYUUp-KGbzqkPBuW8XkwWu5pkbUINbNZ3BE7H2ZbEycSy6GB8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
تقابل سامانه پاتریوت در قطر با موشک‌های شلیک شده سپاه پاسداران جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67880" target="_blank">📅 07:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67879">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سوپرگل تماشایی خولیان آلوارز مقابل سوئیس</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67879" target="_blank">📅 07:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67878">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
سپاه پاسداران مدعی شلیک و نابود کردن یک کشتی تجاری دیگر در آب‌های خلیج‌فارس شد
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67878" target="_blank">📅 07:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67877">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فکت:
شما چند ساعت دیگه می‌رید امتحان بدین ولی من زیر باد کولر می‌خوابم
😎
#hjAly‌</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67877" target="_blank">📅 06:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67876">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=jzZA2ZcPk_HTxtDH1bNGK-wVAcUHu9Z4idnhJJKUr9YpB-RiLKI3z308AMafFaNRMS6FpPzDd5Jca07pdn0wVjhEQ9hBRtVnI-ZfaeqqlQ4W05uwSFUgIQfNTBVnSQt7dnqNsurcnEtHRIVywOVpZ3GRGeJPcaHLHYoeZn0mBBYL9n4QDTmE_cVnr_Rjl1nLFKIbbO4EAYlImz6v4yJn8k8INR2zWJQAtEse7pbCThJnoI2hKDeJISHnUvNkCBI_4f_-23vzUgtyLCDMYwvCKnBpHool8Sc9HWeuJfDnYCxrATfDlBn4srqbkjJ7MB9aUCGPstGTv4_oXLlsq_ZDkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=jzZA2ZcPk_HTxtDH1bNGK-wVAcUHu9Z4idnhJJKUr9YpB-RiLKI3z308AMafFaNRMS6FpPzDd5Jca07pdn0wVjhEQ9hBRtVnI-ZfaeqqlQ4W05uwSFUgIQfNTBVnSQt7dnqNsurcnEtHRIVywOVpZ3GRGeJPcaHLHYoeZn0mBBYL9n4QDTmE_cVnr_Rjl1nLFKIbbO4EAYlImz6v4yJn8k8INR2zWJQAtEse7pbCThJnoI2hKDeJISHnUvNkCBI_4f_-23vzUgtyLCDMYwvCKnBpHool8Sc9HWeuJfDnYCxrATfDlBn4srqbkjJ7MB9aUCGPstGTv4_oXLlsq_ZDkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات سپاه به بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67876" target="_blank">📅 06:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67875">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/67875" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">1میلیون شارژ کن 1.200 میلیون تحویل بگیر با پشتیبانی آنلاین ۲۴ ساعته
😍
🔵
برداشت آنی
👌🏼
⚽️
تنها سایت مورد
#
تایید
ما
✅
اپ اختصاصی با
دسترسی راحت</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67875" target="_blank">📅 06:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67874">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ak0pxzqyyYjZw8stNl0XNQrlIw1W5wAhgsGqSMZ4dBjZHUC3G-WKKQjFKifMlJ-3KDdM22PIMm-KWrSuREwQrRENdAWnjtIjL_AagyBNgGNcTS73JpUd0UrlX1v1saT_z44imvHcxDhApGtXnxlh33jzQLHKxrHG2JI_7ok1Yb8ZnTLK3PZG2w_A7HEVyK-lBt9T3349s6OoyfJFK654HoESXUAXELnizgF_Po8wJcVbwGM5spB7zXEmxwOC_0jOkhc0UtRo5hsEl1vKgpESV5gumFwhdFepYj4BBcxVaTEuMo896pKAqQO0R69JSlsK15S954T_dP_W6jtmAFGymA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
تنها سایتی که توی جام جهانی هوای مردم‌ رو‌داشته تا باخت سنگین ندن
⛔
📣
خودم بدون نگرانی از باخت شرط میبندم با کمترین استرس
🛍
از این لحظه 20% شارژ اضافی همیشگی یعنی به ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان بدون قیدو شرط میده
💰
🤩
🤩
درصد هم برگشت وجه در  صورت باخت،دیگه چی میخوای؟!
🌐
betinja.bet
🌐
betinja.bet
کانال هدایا
a20
@betinjabet</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67874" target="_blank">📅 06:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67873">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1IDSRizctgL5jm_uBooUaoi_CBHl5Lgw4mN5WifmY7nCQ2ZY8MnFenpm4w6rmtmb5DSvbK6A1kVOyCOY4o0VW6iVMnfzlQ2RusljihG3nbmDbk0ft-6vnDf6E7ftjuD0HT5FUtXOh1GMTaBuLNMcvaZJLD5iEdibf23P36z0BpS6Oh_55-PRxJN2Ta5Dr3deTK_tUmFyfY_hrZRsi6PX_IqEeifYfwAsXkY3fJvLMMNC3PPAbjW2ORxkw1QzIIU1Sf70r6SPaslC0xmao65q7kaQJSy8kfctqcJgJkwVRxTMSZdCQO8gB9cQcMOO3pdJjwzzcw6YL0-FD5zVYM2hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/news_hut/67873" target="_blank">📅 04:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67872">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نتانیاهو: تو جام جهانی طرفدار آرژانتیم،</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67872" target="_blank">📅 04:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67871">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپمپ بنزین</strong></div>
<div class="tg-text">ما که منتظریم اقا
❤️</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67871" target="_blank">📅 03:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67870">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67870" target="_blank">📅 03:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67869">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67869" target="_blank">📅 03:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67868">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
هرگونه خبری مبنی به حمله به تهران یا فعال شدن پدافند تهران کاملا فیکه
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67868" target="_blank">📅 03:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67867">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گروهمونو که دارین؟
😴
https://t.me/+5NElXlQWt_05OTlk</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67867" target="_blank">📅 03:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67866">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff21f4d079.mp4?token=E06-mHgrzQaMgTZ1Ii1wvbbathK84S5sDQ_iFEZ-uP6fF0aoBT-y2LyfqdE9lGcIp66ZcwbQkrQmMcVekaNcKSf3HUOWY18eVVfn4Pr1ZOmnw3pRML6Z2h1Ec3hBsjkeVida0zybt8CBJz15gZKLz5XzAkGzoRm4qkCHm1reLedEVAVUu8hRvVFToJ4M4jSuUTsjLtZOtMO_Jgiy3PFoBfgyjZIkZmBP5Z1UYQLC7qei_xGu5LwSyuAxoG7WP_zIDF-Zgtjap8oIsw5IsvhZGgD8oaeaP9-fPGfk9Sun5j-r44ACSOWDV4BrJX0APbXSJ_lkmGJjcJLwethvlE3O-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff21f4d079.mp4?token=E06-mHgrzQaMgTZ1Ii1wvbbathK84S5sDQ_iFEZ-uP6fF0aoBT-y2LyfqdE9lGcIp66ZcwbQkrQmMcVekaNcKSf3HUOWY18eVVfn4Pr1ZOmnw3pRML6Z2h1Ec3hBsjkeVida0zybt8CBJz15gZKLz5XzAkGzoRm4qkCHm1reLedEVAVUu8hRvVFToJ4M4jSuUTsjLtZOtMO_Jgiy3PFoBfgyjZIkZmBP5Z1UYQLC7qei_xGu5LwSyuAxoG7WP_zIDF-Zgtjap8oIsw5IsvhZGgD8oaeaP9-fPGfk9Sun5j-r44ACSOWDV4BrJX0APbXSJ_lkmGJjcJLwethvlE3O-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش نمیدونم صدات به جایی بند هست نمیدونم چی  جونه مادرت یکاری کن امتحانا تعویق بخوره</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67866" target="_blank">📅 03:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67865">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRazis</strong></div>
<div class="tg-text">داداش نمیدونم صدات به جایی بند هست نمیدونم چی
جونه مادرت یکاری کن امتحانا تعویق بخوره</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67865" target="_blank">📅 03:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67864">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فکت:
شما چند ساعت دیگه می‌رید امتحان بدین ولی من زیر باد کولر می‌خوابم
😎
#hjAly‌</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67864" target="_blank">📅 03:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67863">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑨𝒕𝒆𝒏𝒂</strong></div>
<div class="tg-text">آخرین باری که کل کشور باهم دینی خوندیم رئیس جمهور مملکتو خرس خورد
امسالم که اینجوری شد
فکرکنم سال دیگه انقلاب شه
😂</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67863" target="_blank">📅 03:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67862">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQrBI4KG7ivHFwQoKL2VTeLNKMPulbHYE4vdtDSONXxmUpZN7iSmTxmdHAH4FOmElI9a3X21TXj4Vl-U9TeG7vIhfsJFgFXn0W4AQvnXlTQEWoAQbdnnKAOORMheQYTIekEAP3a6SVYWlAmgTn2Okvemb96kq3TMz2DfCxHiZTR0MyCP1QwfzSHgEcEJBUuGvDzUZ0_fglg-BRdiA1ehYcfwoJKxadU-UcqnsITZEqKesWIw1inr_4ACz4GL9eROs2iqILPs4kR8QJ9qTnvD61_WKllyD8u9YejCrZKQMjzqn1fClt8SNYMYhqbuwkiQcfaDDRoM_OQCnHKK4BsGRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقیش اینه به تعویق بیفته حداقلِ حداقل تو جنوب کشور، ولی اینطور کل سیستم امتحانات نهایی بهم می‌ریزه و باید بخش هاییش داخلی بشه، و البته با این مسئولایی که ما داریم چنین چیزی بعیده #hjAly‌</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67862" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67861">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbSV1ZTVEvX70Ppp0YlqppPgdH1ArYMS-_vfi-aLSzZbn23JFLMajl7guqbSzTJW_D9XgAb2lUwFlFXXFscPYKWqOuuN8CM1GEM9D1HA_7-H8Egq-dMVhR3NVqRhqrv4UI-W1c139CrgTJ6jJ7eFmie_Ocon7LQGMsJEjMgMDIVVHCb9CjmbJir3kxoXXKsEV7JS3C2rsLwWZeOhc-L873dewKBUiuFsUIGIHPVmBDxw81UIN44lu-1t2OaJz4h8ItlDWTzkMgNVmsMvsCRqN_l1Gq471s4l0SEM4Aa19kHSpy-Hh6DSBQyphl6Pj70MjFByRiVVziFbAKZojE3AaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابا اونایی که نهایی دارن بخوابید توروخدا، تعوووویق نمیفته نمیفتههه #hjAly‌</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67861" target="_blank">📅 03:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67860">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLZqeUddNS9f57Tcb95827CGZE_9pGB4OHNkAlY_oH33xQ9PS9XQ15lBEykfEeQtnqOLL2Y-vsNCLzaF1Cy9cxivFkYFJds25cOHq9f3P5-D16jyXsXEtE1I_rFJEqkKA_kuwEKGLidRc8wkPscj7ieL8WTcTJv1CbFTntS1G960bQo7dS0WfKOoPwmBYiE2yn0QQuwAFXnQmBNqDSznTfxjuKYPG_HBkZEV4Uev0XeBqylbQrpBF-NlSSC1HsOZxe-RqjqebNGE8Y6MEPsvSEuLRxv6LPrJoveaaXvz2LM1HiJvzKjbyeSGVLJJXZ-j79OoQwAJ0MksZwrQPZYysg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67860" target="_blank">📅 03:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67859">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDm1oUA5c060XBx_cP_5eAT0e92w2wqwfLdSYDEbpof0VcMlluZOkmB_lRBKR_zyeA4RI60WU6Z2umBe1MIR8hSpTNbVUD1dT2HS5knhydb6MjUQl9nSgtdu3XfHsr3qtiwG9FsLR6xe3Y67IiTD24i9v_4PGJdkeM601ETWqUSqnSUTXO-qJgLbz6wnPDSLE-jHmnhfm_lHZie6JZ1B2Ds3KbRDR6RPcXU3x5WHQwU9mMtsdMwrQmwgKyCSkfNynMcNr5HaGH1TlFNjnBharZoTN6e8DJ6SLAo36mByy_Vu-NV-gf0nDq5DO4p6A6ZaITZag11MCoUtc_vJFNn0kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزیر جنگ پیت هگست:  ایران انتخاب ضعیفی داشت. حالا پرداخت می کنند.  @News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67859" target="_blank">📅 03:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67858">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
نایا:
دو انفجاری که در جزیره قشم شنیده شد، نتیجه درگیری‌هایی در آب‌های خلیج فارس بود.
نیروی دریایی سپاه پاسداران انقلاب اسلامی و ارتش ایران با ناوهای جنگی آمریکایی درگیر شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67858" target="_blank">📅 03:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67857">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
دو انفجار در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67857" target="_blank">📅 03:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67856">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=gdJFnU1Aw057d4gQycS-RsLTyVqfpPqE70HV4dh8CbdVum4SwzDCwztj9-S4S_XBdKkZSqACBpAA7ADIOVPvDOrOCkNNe2RDXxUkBFeeFZ3rZRr5RltC05KxyIOSu-HwvUUZazj8ecCEJHTu7_PM3pMRk6BjWWLXZEMbjfx8B4yFGCRrEDcZ0Ogy1AIQTCkfMdrPxQ8-pK4KF0FrTkMZd4tmQ-eC-JQYO1vWwxWSPFBB8CRorfhY-_AsQhSxZGiPwHzIVD46gno0Vnc5AnbQLgN6NPyHXzGjFH1yVMcrE3j6_wx2LJKhgbsKHgy3S9omeyshuM5qV-3igc8XZDwNSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=gdJFnU1Aw057d4gQycS-RsLTyVqfpPqE70HV4dh8CbdVum4SwzDCwztj9-S4S_XBdKkZSqACBpAA7ADIOVPvDOrOCkNNe2RDXxUkBFeeFZ3rZRr5RltC05KxyIOSu-HwvUUZazj8ecCEJHTu7_PM3pMRk6BjWWLXZEMbjfx8B4yFGCRrEDcZ0Ogy1AIQTCkfMdrPxQ8-pK4KF0FrTkMZd4tmQ-eC-JQYO1vWwxWSPFBB8CRorfhY-_AsQhSxZGiPwHzIVD46gno0Vnc5AnbQLgN6NPyHXzGjFH1yVMcrE3j6_wx2LJKhgbsKHgy3S9omeyshuM5qV-3igc8XZDwNSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فارس:
گزارش زندۀ خبرنگار صداوسیما از آخرین جزئیات حمله به جنوب ایران
تا این لحظه سه انفجار در بندرعباس، و سه انفجار در سیریک تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67856" target="_blank">📅 03:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67855">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
خبرنگار صدا و سیما در عسلویه: صدای ۴ انفجار در این منطقه شنیده شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67855" target="_blank">📅 03:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67854">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
چابهار رو زدن
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67854" target="_blank">📅 03:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67853">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
❌
شنیده شدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67853" target="_blank">📅 03:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67852">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qysAvP4z1E4LMl01yGltOhvpj3fhBNmG7yJUgACZbtNXub5v3zVSX_qsRlN9oWCjjxhBQzaAWKaHSOwW730UXZoJ7bnt9OhlT7dQPLhslQsiBxSHHpfz5RTJ9Qcff8cTElpyXTqzEHJC_yxxpRtM-RBZZ584kabsj-nUFU2E1SPXh6kcQ0mPjLmwmObPPNzCs_eEmZUN_GOTqcA4x01ZGSirkoZuYWJkigakyOQuBURqpSjr8NRKFFewsGnOyjsAG_G0-GdgJB2uxX628n1lW_3n-biW80fsPVvey1Jb4weA_NkGASqL8Nxg4dWHDdhHsU82qwJ_SGGogCe-5i7AnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزیر جنگ پیت هگست:
ایران انتخاب ضعیفی داشت. حالا پرداخت می کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67852" target="_blank">📅 03:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67851">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed7140b74.mp4?token=UsMrM7YRBTGy_1wmhdHGQ-CC00vfGNTqk5JGOLHGVwgPEkXjXODg2bipAUh3dHrZ-IHf-2EEngEBiSpC4Ab1F7dpdkYlg_GgY_yp4aOuILj2dgeayHon62oQzmdAHcQd-FHrzc0-pvpI1PFPYr69Kq9ylJhXyqPScHnrIoX-nv5QGcSxanntiy8ItJuR4WsPyUE5UMt50xfNJ0t27NBtCUiWEqv9nfaMsKPWhCOj5bYfoo7oDRXQWTamr7xRxQQRruW88cDuCKNJ3bLHUF-BMboUwXXHNHGxl2rJSIOq_65VEsjKi1JFmr5rDTAohq0_Ubn3SV_fIRf2cmRcLRSSRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed7140b74.mp4?token=UsMrM7YRBTGy_1wmhdHGQ-CC00vfGNTqk5JGOLHGVwgPEkXjXODg2bipAUh3dHrZ-IHf-2EEngEBiSpC4Ab1F7dpdkYlg_GgY_yp4aOuILj2dgeayHon62oQzmdAHcQd-FHrzc0-pvpI1PFPYr69Kq9ylJhXyqPScHnrIoX-nv5QGcSxanntiy8ItJuR4WsPyUE5UMt50xfNJ0t27NBtCUiWEqv9nfaMsKPWhCOj5bYfoo7oDRXQWTamr7xRxQQRruW88cDuCKNJ3bLHUF-BMboUwXXHNHGxl2rJSIOq_65VEsjKi1JFmr5rDTAohq0_Ubn3SV_fIRf2cmRcLRSSRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
شلیک موشک های آمریکایی از بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67851" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67850">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام):
ساعت 7:15 بعد از ظهر امروز پس از اینکه نیروهای سپاه پاسداران انقلاب اسلامی به یک کشتی کانتینری با پرچم قبرس که از تنگه هرمز عبور می کرد، M/V GFS Galaxy که در حال عبور از تنگه هرمز بود، به طور آشکار، نیروهای فرماندهی مرکزی ایالات متحده، سومین دور حملات خود را علیه ایران آغاز کردند. یکی از خدمه غیرنظامی ناپدید شده است و کشتی به دلیل آتش سوزی داخل کشتی و خسارت قابل توجه موتورخانه قادر به ادامه سفر نیست.
ایران فرصت دیگری برای نشان دادن پایبندی به یادداشت تفاهم پس از پاسخگویی به حملات قبلی به کشتی‌های تجاری در اختیار داشت، اما باز هم شکست خورد.
در پاسخ، ایالات متحده هزینه سنگینی را با ادامه کاهش توانایی ایران برای حمله به کشتی‌های دریایی غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه عبور می‌کنند، تحمیل می‌کند. این حملات به دستور فرمانده کل قوا انجام می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67850" target="_blank">📅 03:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67849">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c16f69bf83.mp4?token=rb-litR6RcgnAmOjS6BbMB51SBB5NLOCCEaRX7Bk15dqz7ykGtNLI_Jbd3n81WtlIPqVWOUWYkig-aB-fK8ebMlVXDOt4pW5FeP0b1GPDbiRyOLt9Vxz2H9o_SOHezRXdzOWhbqateNRbmhf6EQCLiiBDiVSAZ43-wWm2U8Ev4xYRKUe4E7qlVL1rniUPmN6Wbv4Hi9Ukt0T1dXiAb1jxz0tg0gzc8xEmXU4uNExcjiqXUB689-yJwWlctqywCY1DLlCd1r4GjW4EL6qjM-aDIEi54e-fC4xWWjHGTIqHLKXoZeIXcLbawNYSZGg6B6uVGJ3WHjtCF1cSyji1ImaaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c16f69bf83.mp4?token=rb-litR6RcgnAmOjS6BbMB51SBB5NLOCCEaRX7Bk15dqz7ykGtNLI_Jbd3n81WtlIPqVWOUWYkig-aB-fK8ebMlVXDOt4pW5FeP0b1GPDbiRyOLt9Vxz2H9o_SOHezRXdzOWhbqateNRbmhf6EQCLiiBDiVSAZ43-wWm2U8Ev4xYRKUe4E7qlVL1rniUPmN6Wbv4Hi9Ukt0T1dXiAb1jxz0tg0gzc8xEmXU4uNExcjiqXUB689-yJwWlctqywCY1DLlCd1r4GjW4EL6qjM-aDIEi54e-fC4xWWjHGTIqHLKXoZeIXcLbawNYSZGg6B6uVGJ3WHjtCF1cSyji1ImaaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67849" target="_blank">📅 03:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67848">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇺🇸
🇮🇷
باراک راوید به نقل از یک مقام ارشد آمریکایی:
ارتش آمریکا در پاسخ به شلیک سپاه به سمت یک کشتی تجاری، چند هدف ایرانی در منطقه تنگه هرمز رو هدف حمله قرار داده .
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67848" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67847">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67847" target="_blank">📅 03:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67846">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67846" target="_blank">📅 03:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67845">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
بوشهر رو بد زدن
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67845" target="_blank">📅 03:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67844">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
چند انفجار در اهواز و بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67844" target="_blank">📅 03:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67843">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
تصاویر بیشتری از اقدامات تهاجمی آمریکا که از بحرین آغاز شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67843" target="_blank">📅 03:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67842">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=OQOhbuTz8YjFUWUdIpv8e_SeLN6FNjS3pFykfwMMRc50xcY1UAYAOb2F2F23fG18ULKNoft5JzIkkK3ngOru5fSOVdO_HS192tDZqmHtk6uISu_nijiNoI-mdHbBpVvbVJKhrhovMA100-PT9dDUU1bHFmDP_Py5HgcbghKpSZd7YWuQjkafDFMrN2M3rQ55qEowVxbNf_fNmWeSvh6ZNjqKr2m2zZ5tog_KVbigfvlT4pzSPU-4tdnoT4XwgtZ1NvnXagDTqLDWu5ebkzG4rfUNIa6-psxLjJ7opt9o-79WJoWKXJDUhrkzRI1045mXtNx388hLXVAt7tfEE3zXJYk5Q7NwX8LgyCSs94PWkHbcpRpWczQJRcrGCmHjSVxhFF8Ev3Vxy_5lAt_l6pdfM8MIEGrxFlVILupXo1SlvLXmhA6RMxzY1geGAMz4xHmCO_NGhHrZOBcENiLPR6fq1XzJM7Y5UC0A87rg4Sw-5R_0LbXBQpUvvaRBEuULASMOUcANK-Uq1Ri3a03MeJrsunk4aBGn_HQI3GuK4v2L0TQRsoXILZ3mgn4GDGJTZGygHtmprIV981F7AjpXEC7wslE2KF1BCU4CwBNSMbRfQVgzsLU_f4RF4k2BANmgTYitwyw8Ykygfx-OVNAhfbMvN7lstqUe9YC40nhT-rgx1d4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=OQOhbuTz8YjFUWUdIpv8e_SeLN6FNjS3pFykfwMMRc50xcY1UAYAOb2F2F23fG18ULKNoft5JzIkkK3ngOru5fSOVdO_HS192tDZqmHtk6uISu_nijiNoI-mdHbBpVvbVJKhrhovMA100-PT9dDUU1bHFmDP_Py5HgcbghKpSZd7YWuQjkafDFMrN2M3rQ55qEowVxbNf_fNmWeSvh6ZNjqKr2m2zZ5tog_KVbigfvlT4pzSPU-4tdnoT4XwgtZ1NvnXagDTqLDWu5ebkzG4rfUNIa6-psxLjJ7opt9o-79WJoWKXJDUhrkzRI1045mXtNx388hLXVAt7tfEE3zXJYk5Q7NwX8LgyCSs94PWkHbcpRpWczQJRcrGCmHjSVxhFF8Ev3Vxy_5lAt_l6pdfM8MIEGrxFlVILupXo1SlvLXmhA6RMxzY1geGAMz4xHmCO_NGhHrZOBcENiLPR6fq1XzJM7Y5UC0A87rg4Sw-5R_0LbXBQpUvvaRBEuULASMOUcANK-Uq1Ri3a03MeJrsunk4aBGn_HQI3GuK4v2L0TQRsoXILZ3mgn4GDGJTZGygHtmprIV981F7AjpXEC7wslE2KF1BCU4CwBNSMbRfQVgzsLU_f4RF4k2BANmgTYitwyw8Ykygfx-OVNAhfbMvN7lstqUe9YC40nhT-rgx1d4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر بیشتری از اقدامات تهاجمی آمریکا که از بحرین آغاز شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67842" target="_blank">📅 03:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67841">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/todRNwf-DS5UHXz_c96CJW9PIqmt2jWF68TZxvXF5KfHh7hrvgfTqoOA5P92TW4Y5rtK1zVTCkTXqoWnI2_jQwIs855ot4c-VcexJsf8FrLhJUCq9J45qcHtNsCDAR0TVFC7Mxzgrs-O9giyWpCQ5wN3pAyYR3CuPr58NYuxnGDE7BmCvwEu4bqTiILk0AyOmexsoXEI5JtsKvXleJ28OMAiRDCz5zoXKsUNGPX1yslBg1IunM6wV9Kc5H2u4xZxghgkRPOfWjDW4GPyoXlhMmsoXczgWKNYVE05Jv4NyGnYuxZzPWLYYhe0tgIuTjaFzCQGE9x5eEuuOb6v2zsFoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
منتسب به بندر دیر
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67841" target="_blank">📅 02:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67840">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
چند انفجار شدید در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67840" target="_blank">📅 02:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67839">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
کاتز، وزیر دفاع اسرائیل:   من و نخست وزیر نتانیاهو به ارتش دستور دادیم برای انجام عملیات نظامی مستقل تو خاک ایران آماده بشن.  @News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67839" target="_blank">📅 02:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67838">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
انفجار های شدید در عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67838" target="_blank">📅 02:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67837">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b4e512f5.mp4?token=nh6kyrX3URD03CEzB6VN047txKRcZxUcIF145P1-MYSEDsPPlYjA7qbMejmn61GwbVSyDB48ZFn48er0Dcp70fdTsb4UG-DbBiBUDZyHf8_Q2RZ66tri67kVkl44L91I9AXWTuQC1orqdOYKZfE9XnxkrD89V73f8W3b1nJIkXEr9cd33qRf_Y6QjME7CtfI1zYHvQ0cJ4xwg1UEvZAmeEqpmkPfK1IPj8MsYKok--syM6XMr1uMuE5hT9eyqUV-9KBBfhZnhjTewDHd8fF-wsAsAkI1tf-mzBQN6c0mDBZsQT8WgggBFELsH40SsGzH4nHJNML60PYJnO_heZOeRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b4e512f5.mp4?token=nh6kyrX3URD03CEzB6VN047txKRcZxUcIF145P1-MYSEDsPPlYjA7qbMejmn61GwbVSyDB48ZFn48er0Dcp70fdTsb4UG-DbBiBUDZyHf8_Q2RZ66tri67kVkl44L91I9AXWTuQC1orqdOYKZfE9XnxkrD89V73f8W3b1nJIkXEr9cd33qRf_Y6QjME7CtfI1zYHvQ0cJ4xwg1UEvZAmeEqpmkPfK1IPj8MsYKok--syM6XMr1uMuE5hT9eyqUV-9KBBfhZnhjTewDHd8fF-wsAsAkI1tf-mzBQN6c0mDBZsQT8WgggBFELsH40SsGzH4nHJNML60PYJnO_heZOeRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شلیک موشک از بحرین به سمت اهدافی در جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67837" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67836">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خسته شدیم از این چص‌حملات خدایی، قشنگ بزنید جاکشا
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67836" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67835">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
ارتش آمریکا رسما حملاتش به ایران رو آغاز کرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67835" target="_blank">📅 02:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67834">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از حمله به بندر دیر و بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67834" target="_blank">📅 02:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67833">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67833" target="_blank">📅 02:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67832">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش‌های اولیه مبنی بر شنیده شدن صدای انفجار در منطقه عسلویه منتشر شده است. منتظر تایید این خبر هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67832" target="_blank">📅 02:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67831">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4398edce9.mp4?token=A_v0VtJv0UaNEmftWPC7SfioF9GeSSfBpbchfNh251pQt3TmaiGBSd2asoRoX6u0sztBjcnXBu1Dsv-gZYzGWnbd_rba0lQsfgJg3HceyDBld8rUp5dlXOHJ5Rmh0r0cwLXvX2CANcbmkWXI9hFIHER34eQkGJ1qMsIVOU_R2LF3QFJ968Lt8E04bnl6LHc5FYzvIZXWnW_ruSH6HvDHbxQJxuljPhcJGIxKmKW-z3KOu8p2bEfWmsxdIl8T5wK2KJBM_XKiCtIQaIGgRTOEHSPW0LH0kiqzhFDQUtA_vmo4yfOQZqxBwlZLUI-XfhpLmPEZwHudghoB6GGY24KaHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4398edce9.mp4?token=A_v0VtJv0UaNEmftWPC7SfioF9GeSSfBpbchfNh251pQt3TmaiGBSd2asoRoX6u0sztBjcnXBu1Dsv-gZYzGWnbd_rba0lQsfgJg3HceyDBld8rUp5dlXOHJ5Rmh0r0cwLXvX2CANcbmkWXI9hFIHER34eQkGJ1qMsIVOU_R2LF3QFJ968Lt8E04bnl6LHc5FYzvIZXWnW_ruSH6HvDHbxQJxuljPhcJGIxKmKW-z3KOu8p2bEfWmsxdIl8T5wK2KJBM_XKiCtIQaIGgRTOEHSPW0LH0kiqzhFDQUtA_vmo4yfOQZqxBwlZLUI-XfhpLmPEZwHudghoB6GGY24KaHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
کاتز، وزیر دفاع اسرائیل:
من و نخست وزیر نتانیاهو به ارتش دستور دادیم برای انجام عملیات نظامی مستقل تو خاک ایران آماده بشن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67831" target="_blank">📅 02:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67829">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
تابناک:
گزارشات تایید نشده از حضور تکاوران ویژه دریایی سپاه  "S.N.S.F" به صورت تیم های غواص مین ریز  و قایق های تندرو در تنگه هرمز مخابره میشود.
این تکاوران از یگان های نخبه دریایی ایران مستقر در مناطق دریایی سپاه در خلیج فارس هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67829" target="_blank">📅 02:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67828">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بابا اونایی که نهایی دارن بخوابید توروخدا، تعوووویق نمیفته نمیفتههه
#hjAly‌</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67828" target="_blank">📅 02:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67827">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🇮🇷
سردار عظمایی فرمانده نیروی دریایی سپاه پاسداران کسی که دستور شلیک موشک به سمت کشتی در تنگه هرمز رو داد.  @News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67827" target="_blank">📅 02:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67826">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiSMvl6Lb_REUj6AJRx-VUdyqPEU2fAzLchEEGtuKA4q68o_j5toPhgeNSoI7OcXwLlEDtnN4ZM4F1ghHLCc_EM4gDEIfVbPVdNKYismaL33v8WujAqGSBU3jbjk_Qky37m-_NIwYnl8IdG1y_JP_K34y5d315L1gbHSArWZzGv4pyuudwH9zOGZJrbd2L2kDkbYuW5p7BIH0Lb3jRYzwF6-gzUBD_k96Ro72eYrszynWNShJXR9qMgtdt4zOXUCcz0l-UssYBxD0rInVpbMhx7Iq-JAv_1ZFEZ-9FpEVbDVTRwEjtZ6tLM4Y4mPzUOExl_arXnPcfiwUzk9OEv5dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حدود 35 دقیقه پیش یک موشک کروز ضد کشتی از سیریک به سمت تنگه هرمز پرتاب شد.  @News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67826" target="_blank">📅 02:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67825">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6zZTVbAeWWX843Po0Fnx-KJuARIGtyrs1DZSmRaU4Ylvzwjb58hmHwQ6MW56oJVJuS3seUzyMdriy6ka8eHEy8bHAb4mETc03y0PWGOueRFWh7trEClM_pWrcTHw8KAia4jvA0IXFxX_7ifG4b-9fwzgvkUxYmSL86yUCKkl2HnYWEf6oYsK7dVt6VQOr_oQuc5tGfY_HlPFhl-0dFVPBkaohhJihPlMLF1ylI5fmkKt7I3hsNbXo35FR-UV5PfQfB2eGSPkPDUMyCq8kZ5hf0nssTPfd-iNwRQ91nvRJV7NZa-1j0aMmvhx9LVbA7cyuaCGKSuGnrOk3kVjojlwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هم اکنون زیرنویس شبکه خبر
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67825" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67824">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVYLNASmBO3agld_kBhOKLNX1gsMJJ-P-NYWLY2xFnEpte5VfAwcQ7759hqj1Q_EKfLCGmzLjgaRG9qj1BWkQ5BXKMwzpraA9Sg4iuo3pvuhGw57_KcUGJocyKxgBu9L2n3Cr8XxdD-ZBNs97hCljAoMr0H9_GWRIaS_VD-6Q8WpoqDyBfxY-M3pNaPFvzScYGRvRWye3EzjQOgIgm8m692qDTBU9_p5aUS3h7Sdfal1APvWlJqCFwjYuAzud54BP3Xrg66Ox1F8-Mg_06bpIjJgjYhRbXbAyh108Vo1Tuzba1rK5PsxIG3eQ8roGnMJo9MOAAu9r9KN8NRc64Yb0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سردار عظمایی فرمانده نیروی دریایی سپاه پاسداران کسی که دستور شلیک موشک به سمت کشتی در تنگه هرمز رو داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67824" target="_blank">📅 01:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67823">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
صابرین نیوز :
به دستور مقام معظم رهبری، حضرت آیت‌الله خامنه‌ای، مدظله العالی ورود به تنگه هرمز مسدود شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67823" target="_blank">📅 01:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67822">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
حدود 35 دقیقه پیش یک موشک کروز ضد کشتی از سیریک به سمت تنگه هرمز پرتاب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67822" target="_blank">📅 01:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67821">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🇮🇷
بیانیه سپاه :
همون‌طور که توی بیانیه قبلی گفته بودیم، هرگونه دخالت خارجی و تعیین غیرقانونی مسیر حرکت کشتی‌ها در تنگه هرمز، با واکنش قاطع ما روبه‌رو می‌شه و روند افزایش تردد دریایی در این تنگه رو مختل می‌کنه.
چند ساعت پیش، با وجود این هشدارها، چند کشتی با تحریک طرف‌های خارجی سعی کردن از مسیرهای غیرمجاز عبور کنن و به اخطارها و دستور تغییر مسیر هم توجهی نکردن.
در نتیجه، یکی از این کشتی‌ها که با خاموش کردن سامانه‌های خودش امنیت دریانوردی رو به خطر انداخته بود، هدف تیراندازی هشداردهنده قرار گرفت و متوقف شد.
از این لحظه و با توجه به شرایط امنیتی ایجادشده در پی دخالت‌های غیرقانونی خارجی،
تنگه هرمز تا اطلاع ثانوی بسته می‌شه
و تا زمانی که مداخلات آمریکا در این منطقه ادامه داشته باشه،
هیچ کشتی‌ای اجازه عبور از این تنگه رو نخواهد داشت.
همچنین اگر دشمن متجاوز به بهانه این حادثه، که خودش باعث به وجود اومدنش شده، دوباره دست به حمله بزنه، پاسخ ما قاطع خواهد بود و پایگاه‌های جدید دشمن در منطقه رو هدف قرار میدیم.
کشورهایی هم که اجازه دادن نیروهای آمریکایی و اسرائیلی از خاکشون برای این اقدامات استفاده کنن، مسئول عواقب این دخالت‌ها هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67821" target="_blank">📅 01:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67820">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
#فووووری
؛سپاه پاسداران انقلاب اسلامی از مسدود شدن کامل تنگه هرمز خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67820" target="_blank">📅 01:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67819">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2Zpq_tBUNRZJJEEPhoUdSIlSwpT5Wl0xUyidin2iZorjoF-YIeaeNU7cUln0rp_XNmgjFOHJ_AGtqDXLhsj1Zcfhkgts6svYZUMFP5Ekt989NCDws0a0Ak-suWSn4JyZ-7JW9RN1jCZz3g5WEDdKwouu1o42A5JLrZ7ZOkrS1qWC40am2tZLcQgVP1VSZ6I16lWFaJiWzOxIksvSmU6Vf-rgZdLg90dLt34uVmJ2ebddM-gDb2hAziVuaN8zqZmGhjXjA5Q_RXL0Qxa8VIL_XtXhsgBEv1bammbT2Q1xP9Ei4m0Zwm0H_0yt2-L21aRt1w1OXLISKwrOilux5BCgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67819" target="_blank">📅 01:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67815">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qf9HhcCdoDEQuhb2mrt7Y1COsRAPeZagk8gTIRDD8_VCR0SMldfucPFPmEUw0sG76y9_uxLh5qjgmRkyRDo1yWpY9EhLvMLX6JuJUgTcoyrz7mkN0oby4hV-wO2W8-Tv4rfrFDFw341EqH9dEDCcGbbQtQ5ViT8AV4I9C64qTZlDz0HMEL0SsXEbhSKv3M0_9bgk235QxVL5TL97VTfJ1YMDOlVKkV9F2wfoepJos9ts_Wq0UZ2Bi_AUmVsL-G3eyrhXvIB20KCRB3xQJ6rlS-7c7DzbntqRfta7XiGHo-KM3G4aiTpn7OP1Io3kgofWRzYCc-Wu4tvrQqJEeyXUvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JMxDrRcjEje87vxOot3lhzyiDglZppZLWybInF6258JFHwyqKLA-T_lkBUSP-m5D4uVmTPWc37JcPXCZN5UZqaME95YdxxfzGEfmSKuzemmF0Y0TNoxf4W_WM_La8rlUbIHPucv157Tt1OYxTCM7UVq6IyQrgnikuurpQhWNiylam2DHnS2YhOi1yPXwXYLIjtkjqP_sXGncVX9PTYKFFM2VK3I2L-khacH_A8pL38qK-C5uo3CrA8YKaP6lpjfSgZMZnK7xungVRUVM-J3ffD19UOqh4T8x1lt_Q-7jQwiHbrKzon-7gxtRiVjSVeXzaPhzaTrTod_E9bAheaPxwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FnE3oCroMssxil4ky28bSlbEx_xcuHUmGogqgjPSu4jYRuV0-Ccd5allSo5fzvlsC9RFYbCIpFCYWpiL1p-HJzB0F3sW8C2URIwYB7Y80Ku5eObqGM5AUACovLCrTNcBPZ2qiwHZI6pD7tYucERGnaAtGyvZZBbmHDMYYEZSo5UjfgVMt3k2xeG9BryYDZmTEqv4JVLJ9FJzEXTKgL0EF6a1jKgBTEY5B9lpJw9QoKlcNUh0BnnX99HZNp2LzwQXfEDVuW9hRoFlgfc-rdfJ7W4WTxrsC-0loGZ_TC5xeE44N1MrHJhztxybmvPHMdBMkyzqA9yYlyCAJ8hIPdGmOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nsEc_kdeu2K-fgqqEwnErZcoxvTRgpP0AaKe0bQAH5_d9G2r810mL7wIuvjXpA0FLhSpA1IPLpufxXrlHC2okVJ8HZtdP6fQpbNr5aTt4jSqZrV6p9PPeRZc6Hu802kOou15H5Lh8-QnSdZMP8ZywMtq-UNlxvZ4L7GbsbVF5ce4A_8_djGpbhuqu0TmMN17l_3DM7ptVYwSk7KAWrdsKEazzgv3h3NJdwgHRPLm6ifxWoSYyRG2yy5BV0e1Z2VxMnhLS0g7F9PxAKIzZ-CHG1qPEif1L-jvrKPZL-3kFNXzN3I1f_CupM8s69L4nVyvGXez5CU1EWbGR4EVN67alg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚠️
هواپیماهای باری نظامی آمریکایی از نوع C-17 در سه پایگاه نظامی که توسط ایالات متحده در داخل اردن اداره می‌شوند، فرود آمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67815" target="_blank">📅 00:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67814">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbae51b67.mp4?token=XvYE0tIQwD0gLOlPmOFOigotPXmG00HPaeWHbqujPnLbTkG9ddA2pTteWGXIl6rvUjZnD49NS975dYlX4eoJbbI5ERFL8DfQZoL71Y4umkNtY3PWi-TkkHHVuEHPq2qb4dGNbQ0gjpt6mXLst5sBd0gpLkxrVw22EFNkMhBirBMBT9LQF90P_efSF5rI9LhVnFakaO3bheofigL82b9A6R-L6nfans7rQTyFUFjm2ZrehjeUSx7YGuxwvDSKF-P64A5mQr-J2WZt7uhdjfr6evi0peIZdE8Me8RG-t4z2FlPwK-y2x4rQsTzCS5wHWGcR_wwbjSQqhqvNZChh47jfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbae51b67.mp4?token=XvYE0tIQwD0gLOlPmOFOigotPXmG00HPaeWHbqujPnLbTkG9ddA2pTteWGXIl6rvUjZnD49NS975dYlX4eoJbbI5ERFL8DfQZoL71Y4umkNtY3PWi-TkkHHVuEHPq2qb4dGNbQ0gjpt6mXLst5sBd0gpLkxrVw22EFNkMhBirBMBT9LQF90P_efSF5rI9LhVnFakaO3bheofigL82b9A6R-L6nfans7rQTyFUFjm2ZrehjeUSx7YGuxwvDSKF-P64A5mQr-J2WZt7uhdjfr6evi0peIZdE8Me8RG-t4z2FlPwK-y2x4rQsTzCS5wHWGcR_wwbjSQqhqvNZChh47jfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک پسر هیجده ساله یه رولزرویس رو یک روز بعد از ترخیص شدنش از رو کفی دزدیده
یعنی رولزرویس رو تریلی ماشین‌بر بوده این با هیجده سال سن اومده دزدیدتش.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67814" target="_blank">📅 00:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67813">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzw8LQUSL46ajrpECNUzYP-_68_JB-5zLzCuEXnzMb9UfgWTj-NeO_ORxWajeyyhvcXMTLGSRD-LDs9J3akmca4baqMUkbPnJfNQNNGCwjIcIahjfygiYwKfOXo_cS8a0IIMd2siLsv1XpG4AwY3Ywmbkk7ha8gUwGAoZEC3oTk0_8WyByiEFqVAdPXC3Twpkw2SlgYzT7yaeV5TikF7imc8LaaKY8SXS7zGJKYjQUg5XL1ceFDvWc49TXAabWDezi-87TsphRbsxDBH_JSoCR5nXSqxxRVgXOCcDk2S2dMPHiPjYe0tgYDuIDh_cSuX0FyxpnrNSnZk78yc5jVV1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کانال 14 اسرائیل:
اعلامیهٔ مهلت ۲۴ ساعته دولت ترامپ، که روز جمعه، ۱۰ جولای، صادر شد و از ایران خواسته بود تا حملات در تنگه هرمز را متوقف کند و از آزادی تردد کشتی‌ها در این منطقه اطمینان حاصل کند، در ۳ ساعت آینده به پایان می‌رسد.
این توییت دو ساعت قبل زده شده و تقریبا یک ساعت دیگه مهلت یک روزه ترامپ تموم میشه
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67813" target="_blank">📅 00:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67812">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
🇺🇸
مهلت اعلام‌ شده ترامپ تا پایان روز شنبه به‌وقت شرق آمریکا ادامه داره که میشه حدود ساعت ۷:۳۰ صبح روز یکشنبه به وقت تهران…
تا اون موقع به ایران فرصت داده ترامپ که اعلام بکنه که تنگه هرمز بازه…
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67812" target="_blank">📅 23:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67811">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c50mlv4Mhu24xroWwXfu8sHREDOl55pkKTqAsgqaTOtECz9ctc14DOfthXaJ6vRkcGhluXx1krq6vFxDes4urufpFd4KyDhH6_WBNuHzfEsjPcTGy_suzuXiu7z2UITIvbKPWA_5kJMsaeQuwjcvkYjCbL3_RRvt-lm9sinhgJMqCN6zPDmpgbnr9JLO8vIH--CEiTvtUte1OFV4lToM42oC_tFKTP9RhoYbJGSOxGCVVp6MSmFbconmuzol_O_8BhG8gWkBl2NetbHd8024Dh0g7l13D8WNoMr01L2SUn8AP0D4RXZRMBCucE5C-5ML1p2WikkhNZUv2fN0O1n40Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پویان مختاری گرداننده‌ی سایت های قمار که خودشو مخالف شاهزاده رضا پهلوی جلوه داده بود و معتقد بود عاشق جمهوری اسلامیه؛
امروز صبح ساعت ۶ با هواپیما به فرودگاه امام تهران اومد؛ که توسط وزارت اطلاعات بازداشت و راهی گونی و منتقل به طویله شد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67811" target="_blank">📅 23:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67810">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9S4UUQlbiqiKhtQB5ioD88LoV5R2eLGnxBzINsd61heaPd0owODHznceiVnYnWw4-aoe_u-EKIeVKYQxF6I1XqYEdiocbCDOzQxeL_0XDaxyFJJHZyGNVFs6E9US2YU4yoF5-aa-jw0v-s2j77_L6WrNZ7cesYg0a2O3geqZlTDqBldEhQ4c9-_Rgbl0IS6roR2-eBPPnHuUckj3hfMwKQ1wSvhrsu00dYI1yGHPNMSC8TVaGZmjQ3wAP6FBVmVNxPLth-OxyuvU9WF7PB61uqM_1jy0AhKQEJQaox9jgsbZk4F2j97-cj79Ky9uQ1X3TLwVcmRGxcLCvu_P2BFlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علی قلهکی:
قرار بود سفرِ عراقچی به عمان منجر به صدور بیانیه مشترک درباره مسیرِ شمال و جنوبِ تنگه هرمز گردد و در ادامه نیز «قالیباف» و «ونس» به مذاکره اضافه شوند که با بازگشت عراقچی، گمانه‌زنی‌ها درباره به بُن‌بست رسیدن دیپلماسی در مورد «بند ۵ تفاهم‌نامه»، بیش از همیشه تقویت شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67810" target="_blank">📅 23:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67809">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
اکسیوس:
ایران نتوانست در این جلسه، موافقت عمان با این پیشنهاد را جلب کند و مجبور شد این پیشنهاد را برای بحث و بررسی داخلی در تهران مطرح کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67809" target="_blank">📅 22:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67808">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ttyot08vgxpOzpZyeeUOz2xDbe5AQeE8gbrld-QkB4GFse6J7JEHCX4--tdE-aShQNZlu2iSFsNuBTxDVOGjQlkMZpzS3n2zouqnKMS2BlfPtj-tGC4BmvqNVMPC2-Z4sv8mFvSwrr3-oPQy4Tiklp2uza2Wc6w10DE47tIbMAQger-TEILDgCvyuEOmkb7TQymFO4A0vR7Dkda2eXJRIdKk_c-5Qvgnafukq8LtCz-6rsySMiDpOUD5b-XYPAOfA8YgAy6-AHJ2Bi7h4Z5tlMHzXtAoiZAb6yJ2DFZQebKNkI8AeW_ibDFoalEDLq3nZsqdqbTTkpODWJrFtbkmBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سی‌ان‌ان:عمان پیش نویسی را برای مدیریت کشتیرانی از طریق تنگه هرمز با استفاده از دو کریدور جداگانه کنترل شده تهیه کرده است.
بر اساس این پیشنهاد که هنوز نهایی نشده است، کریدور جنوبی از طریق آب‌های سرزمینی عمان برای کشتیرانی آزاد در شرایط پیش از جنگ باز می‌ماند.
کشتی‌هایی که از کریدور شمالی از طریق آب‌های سرزمینی ایران استفاده می‌کنند، به تایید قبلی تهران نیاز دارند، اگرچه ایران هزینه‌های ترانزیت را تحت ترتیب پیشنهادی اعمال نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67808" target="_blank">📅 22:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67807">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d2e49f67.mp4?token=j3u2s2WqnXCHeQaS5gJzS2g6uuEkenUcFtJwTP9w02wjfoXnQV3nvIlsIoUf1mknWWRSnEAAB2ysw59dwxcYLpI3i_LRYn37La9r9VWh_zp3RNGq6DDYzDti_9TtbPXhKKyhaxjY5rlwy68AhguhBPVVOxxOOCQikgwc7tBlcKLVWVwI7oDGHUIgEo0NY6VB-6CEQf9HuuhV0f7XHbNUdMbagyPRY57Vl3gsRC2DczwAodZ78uTscqC6oA74naVQxrm9_7VfUKWEmCn2WqBVMDXuSvwMgGzm8w8_ogFzw2giONLGykSnyn3S_NBDoOnOdi1LMqw-4717nBr-lYtU8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d2e49f67.mp4?token=j3u2s2WqnXCHeQaS5gJzS2g6uuEkenUcFtJwTP9w02wjfoXnQV3nvIlsIoUf1mknWWRSnEAAB2ysw59dwxcYLpI3i_LRYn37La9r9VWh_zp3RNGq6DDYzDti_9TtbPXhKKyhaxjY5rlwy68AhguhBPVVOxxOOCQikgwc7tBlcKLVWVwI7oDGHUIgEo0NY6VB-6CEQf9HuuhV0f7XHbNUdMbagyPRY57Vl3gsRC2DczwAodZ78uTscqC6oA74naVQxrm9_7VfUKWEmCn2WqBVMDXuSvwMgGzm8w8_ogFzw2giONLGykSnyn3S_NBDoOnOdi1LMqw-4717nBr-lYtU8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سی‌ان‌ان: برای نخستین بار جزئیاتی از حمله موشکی رژیم جمهوری اسلامی به ناو آبراهام لینکلن منتشر شد
.
شبکه سی‌ان‌ان در گزارشی به موضوع شلیک موشک‌های رژیم جمهوری اسلامی به ناو هواپیمابر یو اس اس آبراهام لینکلن پرداخت و جزئیات تازه‌ای از این رخداد را منتشر کرد.
این گزارش در حالی منتشر می‌شود که تنش‌های نظامی میان واشینگتن و تهران همچنان در سطح بالایی قرار دارد و موضوع امنیت ناوگان آمریکا در منطقه بار دیگر مورد توجه رسانه‌های بین‌المللی قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67807" target="_blank">📅 22:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67806">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
کانال 15 اسرائیلی:
ایالات متحده منتظر پاسخ ایران به درخواست‌هایش مبنی بر توقف حملات به کشتی‌ها در تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67806" target="_blank">📅 21:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67804">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08bce6837f.mp4?token=ckLHL7a-PGChTYw7sBZGQpBgNY-rRFQMtMEvMKJG1c7DC5g8g1I_SkIzQbjr3KJt1TNxO-D6EONMtxWdT5AjyAYLs8oy7GET6myuqaLanu-g_ujOdikAfIlbs7zG2Ba3NUUh8-qRQoW4gZSEa9J-jgmqfHL9mE2NOmOX4FstrejIfNj1AYUceyqpeLR2YyFaMukXhgLQsK8tDmJyUd8RKVKoNTfUCSUwXIb6PhfXpNZUGwgSKYrcyWVj96RicElZpdIJG-dkRHmou53ZWVT6281uK9hZJXLScPLzRu686jIXfkyB6jntuMM5nV0Tfef-X2kaHMqAvTVKupzC0GioTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08bce6837f.mp4?token=ckLHL7a-PGChTYw7sBZGQpBgNY-rRFQMtMEvMKJG1c7DC5g8g1I_SkIzQbjr3KJt1TNxO-D6EONMtxWdT5AjyAYLs8oy7GET6myuqaLanu-g_ujOdikAfIlbs7zG2Ba3NUUh8-qRQoW4gZSEa9J-jgmqfHL9mE2NOmOX4FstrejIfNj1AYUceyqpeLR2YyFaMukXhgLQsK8tDmJyUd8RKVKoNTfUCSUwXIb6PhfXpNZUGwgSKYrcyWVj96RicElZpdIJG-dkRHmou53ZWVT6281uK9hZJXLScPLzRu686jIXfkyB6jntuMM5nV0Tfef-X2kaHMqAvTVKupzC0GioTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ارتش دفاعی اسرائیل:تروریست‌های حزب‌الله در حال انتقال موشک‌های ضدتانک در داخل منطقه امنیتی در جنوب لبنان بودند.
این تروریست‌ها موشک‌های ضدتانک را به یک ساختمان در آن منطقه منتقل کردند، که نیروهای دفاعی اسرائیل (IDF) آن را از هوا هدف قرار دادند تا این تهدید را از بین ببرند.
پس از این حمله، انفجارهای ثانویه شناسایی شدند که نشان‌دهنده وجود سلاح در داخل ساختمان بود
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67804" target="_blank">📅 20:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67803">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e14ad8a91f.mp4?token=asB6vIO_J7I2SlGnfvwydRTy71WWoNOrw6Lnju98jrj7gi2SSDdbIxIGMWMzM7mbzFuXWLyFgQ2dZIW8g5rxAw_isT31d2xriy0owBi4Q05DdEMbvCK-h2i1uvpC4HpKu_7PdIs72qJTm-9a2rNuAwVUmHojK25LpUYtki-P0JMCHbrn2p9tXuCzlBQKTRKXGuY_mH5aTqTi68Qjej2d4tJKFKigbDa5lqr46we0cHBIX5-zWnUm_g2MYkW5q-jDgGLPOh5Mo6dzZTq3HuSJ-37Erw-IJTy00OqfNJ6pbNpPSE8xg4sIB5tNo1VvSS5NNjtXW3COPwHmi5TdzAZufA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e14ad8a91f.mp4?token=asB6vIO_J7I2SlGnfvwydRTy71WWoNOrw6Lnju98jrj7gi2SSDdbIxIGMWMzM7mbzFuXWLyFgQ2dZIW8g5rxAw_isT31d2xriy0owBi4Q05DdEMbvCK-h2i1uvpC4HpKu_7PdIs72qJTm-9a2rNuAwVUmHojK25LpUYtki-P0JMCHbrn2p9tXuCzlBQKTRKXGuY_mH5aTqTi68Qjej2d4tJKFKigbDa5lqr46we0cHBIX5-zWnUm_g2MYkW5q-jDgGLPOh5Mo6dzZTq3HuSJ-37Erw-IJTy00OqfNJ6pbNpPSE8xg4sIB5tNo1VvSS5NNjtXW3COPwHmi5TdzAZufA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که رسانه جبهه پایداری از تغییر موضع ممد سامتینگ نسبت به مذاکره با آمریکا منتشر و وایرال کردن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67803" target="_blank">📅 20:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67801">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Byt9gaInCyyA_WbkavoDW3pmG0wkpwV7lL3Igra492M68K-mrLUeRfZQVCQN66qcM4xrFnU9qggNUknDf6C4cJNLT0kSPZskJ0cbUbZzQHrqVaufHU2k1dF1xCQt2BYqcdD6KYKLhKpxShBDl_gfeGgI4X-zUcloai3ILbZJLD3K8I5zwuvuX2ArPxuzlXbDo5YLygl87-tcaTtE4yfWcSkak9yB44C4_3EwfwbaTVfYfNXNnQ8O5azvKmdvb11z67vwF9h45JD4Em30qLCfkJ8wN9XnDobMwm_ED_BZKaFyMGWR63kFRZg6oN4SPKrkPgAAdmMe5czGE4EE3rCRnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S8yFx8cNCwhxc86GHBlM1hUzcrPMhJj4tawP4Oe1ltqhkbK5t9Kj2O-kKPmXyBrOgs7PMIG_7NnelNwY8znq5QfRN94KAESgZuG56eiKidpXBIEI5iigjgdq7w_GAJNmgIiiM7m62pWeQVou1HL7Cy_gl7en3aWQcD9hXEPqu86aJVyQa8EUUGhNN9BLWZyO1zg1G4dLWIsb_986me_kVhdgjpUzrLBFYXNrGqeGfNIIcU7glFdGHAcM1DXnepnF_YEZODwx4TxOOh2m1IXQlExRqqy_XZaAYNSA56DZrib_xpnNzjKUOD9Z_U4Eec_QbWua3WwPRNT4g1XHPXPV7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بسیاری از هواپیماهای تانکر سوخت‌رسان آمریکایی از پایگاه هوایی الامیر سلطان در عربستان سعودی خارج می‌شوند. این هواپیماها معمولاً پایگاه‌های خود را در منطقه ترک می‌کنند، زیرا نگران هدف قرار گرفتن توسط دشمن هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67801" target="_blank">📅 19:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67798">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYNWBL8md5ZXfLq8Xk3KMHeWFoqmANm5T9vYZZMQIH1FpTYWcZxKHim9hI__fXBVx7ayX2BlBpRLMCjHOpEEuMot0DDZKCzuXeO2NLYrmYA990QzRP4SbY300aaUBvRgJ5C155JIYFUO6NNLzwJTosryaEXrWGoTQv_HmHBX9wMX10989LBBGxJBMZWfCN0TDIDMJCF2Jvc0VbbAzJzj9VE5gEN9PZ8MQM8HVhpekfX2Fo-hCGo4wEw7Kad1erSEDsq9ErSPg3guXUOiKDYypvynDAMfOOdK5ef0zTLLzNHwrXPSEb8R1RI_NiKFOkGu-AGdQdG-cPfMFP3gPhjMww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنالیز و پیش‌بینی نتیجه تمام بازی‌های فوتبال جام جهانی 2026
💻
📈
🇫🇷
⚔️
🇲🇦
وین شد
✅
🇪🇸
⚔️
🇧🇪
وین شد
✅
پیش‌بینی نتیجه 2 بازی‌ باقیمانده 1/4 نهایی انجام و در کانال تلگراممون آپلود شده
⏳
🇳🇴
⚔️
‌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
󐁧󐁢󐁥󐁮󐁧󐁿
🇨🇭
⚔️
🇦🇷
لینک رایگان ورود به کانال
👈
بت جی‌جی</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67798" target="_blank">📅 19:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67795">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZkSbsRgh7BqoPqOJ-w4o0CFj6xGh34dinzwey45lzQIEO9PdAOQMBmBAVQ9sQ7u08XKA4Tdzoan1kTMDi-te9o3D5XwjMJ7fnp5g1WnX5PLJHrwuiioSlonwf0_DPz03-g4FwqzDdzD2oeTogVFycGHZsScUtu0XcazETgNHpdqZhHpEeM05Rp-BhoTdmAlJVyOwSmugUZMF6ZWkouCHktkJziogvau3W2D4qSfMjI77cKSJ1oybE-iA7Zpox_JM-alEKL8gc_5Mblty1bDs2IlT6shsHSHvmtu0fa_rjdxL5rTYLuqlqfAB8O5h_TcERsBMpV8vEr-gE1qUyl5og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
به گفته یک دیپلمات مطلع، مقامات قطری در حال مشارکت در مذاکرات میان ایران و عمان در مسقط پیرامون تنگه هرمز
هستند.
یک منبع منطقه‌ای اعلام کرد که طرفین در حال گفتگو درباره بیانیه‌ای احتمالی برای بازگشایی کامل «مسیر میانی» در تنگه هرمز (که در آب‌های بین‌المللی واقع شده است) جهت تردد کامل و آزادانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67795" target="_blank">📅 18:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67794">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00f69c138.mp4?token=UnGs_Y8c2IIcmBV-c2mxifmijnI7mVGwsrrzn9-t-lXlG5yA1iSc8p2nwV2qhPFu3QXiMAGuskYl4TQ750bs_XTVFvrNH1f1XYmuZKvaISR5LoVR5BkzNMQWcZ8U34sviPOx8jfNuqvTnPSJvMbRuC1CfwCnON9W05fRkVnjm6rUN6LOdTWyd58ZlCv6bICdSX0EP586XOB-BAF0Dq6WWLqbYStm7Cf5HClH3eZqG7ysgYytdXAXYEzsrsqgXJivkEsL-9cQUg4NJOPdcqDeBFnQuCrG-MPn7a1tTWBsbSD7DdH5fc5sy8yM2ljW3F5AEbanWtdil90n5YxXZGbU0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00f69c138.mp4?token=UnGs_Y8c2IIcmBV-c2mxifmijnI7mVGwsrrzn9-t-lXlG5yA1iSc8p2nwV2qhPFu3QXiMAGuskYl4TQ750bs_XTVFvrNH1f1XYmuZKvaISR5LoVR5BkzNMQWcZ8U34sviPOx8jfNuqvTnPSJvMbRuC1CfwCnON9W05fRkVnjm6rUN6LOdTWyd58ZlCv6bICdSX0EP586XOB-BAF0Dq6WWLqbYStm7Cf5HClH3eZqG7ysgYytdXAXYEzsrsqgXJivkEsL-9cQUg4NJOPdcqDeBFnQuCrG-MPn7a1tTWBsbSD7DdH5fc5sy8yM2ljW3F5AEbanWtdil90n5YxXZGbU0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریاست‌جمهوری core:
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67794" target="_blank">📅 18:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67793">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3x9_c23n5v3HCyz3OdU4IkjsenXbumF_uWaD_QZB0STA3jMxbuznJXjnQAu-Hax2HOZoZMU1ueg9qz27zUE9fUGf2YDtPEStUCLrhgPbSLxvst7DqUn4sNBwQB3yNh4bOw9E-nGDk91geuBndUlwJ59Ivol02QnzUlIgNx0a3BLKm18C8_G9kcnpxJBwXQj9M1oIwSBkJg2ptWolrUPHiYiM1CDy5HBCWutqwVglw56NfepHf49O5yO5V8dQk2v8qwKBidnlliv4HCsCnHFwiYv1JlYlRRIoAxVSuORUpbImQj0mgHrCUJT8uwG62Ls-kfBSVYEL5rYdlq8UzC7uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری مهر:
یکی از نهادهای امنیتی برای حضور فیروز کریمی در  یکی از شبکه‌های ماهواره‌ای گردش کار قضایی برای برخورد با وی را تهیه کرده و در دست اقدام قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67793" target="_blank">📅 17:32 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
