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
<img src="https://cdn4.telesco.pe/file/A2kF9hvfSXZqGgwrgH2TS0L56pP-y0zKMLjrP3hhl4goqUmxHot539CVnglkH-ym1oTteANtC6OyLXvQ8O3DGW8i6o1rU_LohdKMdEmc4FIgWxEb3KiHQFtVcuUtD5mZ0IcDW-3BHopAUaGqTrCURybNAozAJLwQBVYqEkz4Sy4Fl1wmA8mQ_ermW2C-QNFz66gJZnN5ufHUq6qaWtNzvn_NY8GL_KdtRFT2mnW5G_3mDXMrYJQf2TQ9ZOaWjdgFPKrsAGT-MwRnH81aWP1RzoPXBo1OXdjGlJUy0vVRa7RCUto_M6Z1ZkRHn3XWSZWrN8Hj0jOQzn6WIbZLVMje0Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 150K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 02:24:00</div>
<hr>

<div class="tg-post" id="msg-68968">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=Y637e86oqfy4Zqj_JBkteg6XCvO3Lomls-nOgyrqu2TbGUCYcvhFGkLHEC37Fuxblwu6sq9t8zqWRqY4Vp6TjNdrqaTBKf4yCH_vPJe1c4XwJeu4kIYQjyt1HqeYPvpt7UPPnTbnxwasLZ5I4RnIPLToxWvRQNYTdFSLplStWT9AdGQ1JDyBKWvxBUJgfIKm8dumYw_FggCdviECV0JNRuSY70Lw07J9A-nyTijSw1_BWAKTpoAxIvzS18x9bvIcQfwajSF9_v5yooLpOQEDzYxmlcBO26okmmXVAWJSoudWlo9L1wgsPrL7lMyT05ECCIlE5s3ynH19JpD2jRc4vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=Y637e86oqfy4Zqj_JBkteg6XCvO3Lomls-nOgyrqu2TbGUCYcvhFGkLHEC37Fuxblwu6sq9t8zqWRqY4Vp6TjNdrqaTBKf4yCH_vPJe1c4XwJeu4kIYQjyt1HqeYPvpt7UPPnTbnxwasLZ5I4RnIPLToxWvRQNYTdFSLplStWT9AdGQ1JDyBKWvxBUJgfIKm8dumYw_FggCdviECV0JNRuSY70Lw07J9A-nyTijSw1_BWAKTpoAxIvzS18x9bvIcQfwajSF9_v5yooLpOQEDzYxmlcBO26okmmXVAWJSoudWlo9L1wgsPrL7lMyT05ECCIlE5s3ynH19JpD2jRc4vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پدافند هوایی روسیه یک پهپاد اوکراینی را بر فراز انبار «وایلدبریز» در سن‌پترزبورگ سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/news_hut/68968" target="_blank">📅 02:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68967">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g57WqUUzg8LwHxQH3VGR2fBvYfyJv_R1xsqeLQG1ucOJp-mJPk0CdZhqTxy-4Ek5-A3l5UdLGB-LLedcnfWtCcf-nY-S0QtLypTtZhIG9ip7qMLoe3u6MhtJuG9zuiYGGjGdPQO1FiNmMu9v6S5D0ftMf-1NR18dB_0YtByfeQH3ulvHx-gD3QEzGMGI4wP7199i-aIREfdUGec0DggmSpE9Jhauvmeij8awIQ_1IbPvFU5_tZTK63BxOfLYJu7pMcbbxYWXinIGkwxPrWv9RXfKV9FnbRmSu0EUVFqQYHpfqR2g2ax7LOnFKuzaLBETqsgyuW9kYm7gm_l4Zw7Z4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ارتش‌آمریکا: یک‌کشتی مرتبط با ایران که سعی در نقض محاصره دریایی داشت رو منهدم کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/news_hut/68967" target="_blank">📅 01:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68966">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGpCGD5xQCsEQ4kUQ_77MIELxttBZ7uijsFU5HJ1mBe9aXNJ-Ib-RJo5zXyOAmWCMmjXsjDeEDJCNaxT9LfYriJ3GPRWROTMJk2iRUOhTFpLb75fJrIN70q2cAkzZ0YYC24AGXVTCgpRPr9YOjxmXLxiOpqhXwR7vztxXQrEzod8XA02g1GcDa80mhTqLxIwv596C8Wz1I2sZXDkZ7583uSue8xahXWaGZDZoNgvgkuFzy9zpC0rT9XL91b6uzvYqkKewcMtKLNia2RXk5O5nh6oo0vTLLiU3jqY1-LoQzfHLuI3ELB8vmKjFdHOr2SjelobZSlytsREppL7VHoR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/news_hut/68966" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68965">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JY2iY2032c8-Blgxzx_NC-nPqp6ZXmHRHKnRXryQ6MHMz5fBhEcKXkwx-M8WrtxsS-88dDh7_gzmmLVclC4vbf_J3cFlVH785bMsl7v4J_4l3CDFtBpN3ptvlYZPLmBjllZJYk-kjjYC_9wqk9JL8HFdO-XqbPmRcGp3huTa9H0wWb3Q7HrSCAf1bgDZ1WdZAVKmV2Gv4IE-meXpG0vtGF0V7Hc2pFTToNY_IJULnecsr2DYrv0xcuenYSu1XyVFGsS0B7ye7kUzGSrAMkcQByWOQBCcr6QuUX0DXQsWv3I_gEM1XGVUqoFmKa2xpg5yxUFy5NslM3cccsoC4Xvcog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
رکوردهایی که ترامپ تو این مدت تو مصاحبه‌هاش ثبت کرده؛
«ما ایران رو شکست دادیم.» - 106 بار
«ما ایران رو نابود کردیم.» - 95 بار
«توافق با ایران نزدیکه.» - 88 بار
«تنگه هرمز بازه.» - 75 بار
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/68965" target="_blank">📅 00:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68964">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiTIvqjpeDRmUBybUp-t3ol7m0Xnx9_UTFjFt1H7_vU1LECwMRgN_cks5RgnfTWd2Rg4Fcp3-GHDe2OZn2yzfjqiUbK9wAty2iD8T1njvuchOEOpwPYsYkmrrPXcuqXscZZX2eXcv5TI3dm3J6a2l_hQPTZuinkFSzhVZcVKcoAPODrHmEwmCRKQxatVBG0RBlLB4REwYZCUjOUTwNHVGXZ4feDR2eXPXz2xUKiBniodM_dFVawFmvVqH40_J7yfOI0YKFaZrniVJHaurUaKd6PzWBLJ41y-TRKkpj9Jzu4318DDfCcAu9uN4pWKPjzlh41G3GxE-RbuBquFokD1ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
عربستان دقایقی پیش به بندر حدیده یمن حمله کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/68964" target="_blank">📅 00:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68963">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🎙
خبرنگار:
آیا شما در حال بررسی یک حمله گسترده به ایران هستید؟
🔴
🇺🇸
پرزیدنت ترامپ:
"ما آماده حمله هستیم. ما کاملا مسلح و آماده حمله هستیم. ما با آنها صحبت می‌کنیم. شاید یک نقطه عطف وجود داشته باشد یا نباشد... در حال حاضر، ما به طور جدی با آنها صحبت می‌کنیم. اما به نظر نمی‌رسد که بتوانند به آنجا برسند، شاید اکنون بتوانند."
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/68963" target="_blank">📅 00:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68962">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/68962" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68958">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KlVgYXdiY0BC8c6JDSHPT6dtXYLQQJ9xddJPddzDViIjbbNFWpfRGImDsLnDm2DQuA1USXQdBYX-4rcObjd9mqJ4pYWPxzNBi2TAOK7fvXSB4KQDkefavYF6KW_MZaoWezRwLjYEgfj6W2S8mmx2d6E_ubNJdZCiWmeZUeeLTg0khnS8V4CbTDeuD1K-rRtnRR0nT_2gfCUTPgh7tYh0bixWksP3EOWLQ1JVogjyT7PUk30AivvLMjl_h3fvxwDfe6yb7NB3vCwebDQtsSaXv8UGc6LooBbzUICP5XDTiDTDd_CEqBfAAkH961dWK0FXWhSCXM5hSZq0-AXej4X32w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WFrCKb0XLuf15IazFSe_y7D6vjuZSCFQ0L9yQL10xu-vkAExyH0EhVtLazHie_zhlTpkC3MMcd6NxcZMMd0ZC2dnrf01dMoQyqO9PVvAKFFvqdAKnDaD8jcr8loQIIWWU19XcAtNvTt-BqGyvrlt9EOCsIZzSByxrDLMC7OeKg2SGl2voMNcuunEQ93MXqSl4gx0h-VsiRCutfwqTQ8_m1jH4X2_IrUEQuNpaf7pul3eKNWmfxvA4lHPrcLw74PhlKf1GI1ot0j3qgalx2yRvkUmXdlsWmS1WtaIQTuxEaoj7V7iHZfCslScpp-myn4diKmbT7--OLm0tONDnZLvYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=fWHAgN6jaLCfH6C-91HtrfEsM1zEGOqk573WaKmoGYLyWy0pcWB_31pVNkLLqtbj1JLTwRJUDDfgZZA_TwN1giz0J0ryQNa6Y5Cy3DjQXS7Uxc-a9ekim-cJirCdGnUsVudHnODH2LBKH2CwovSpbTzDd9a1659o-lUDKU2iBtuL_suA9FPr5mb6omHm0q7L41Aik_NEZ_Elv1uWDeFP2brPco2cienQHLN8hVVFhQbg4UVIYA19F0cz4dARuUS6q-1a-J1BoarXIqd6OIflzGNWX3qesBGNQBgOM5NWnOSrnxcDSmWzJVPopVpj-NBt1UdFczE8d30-OIuHJhXYRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=fWHAgN6jaLCfH6C-91HtrfEsM1zEGOqk573WaKmoGYLyWy0pcWB_31pVNkLLqtbj1JLTwRJUDDfgZZA_TwN1giz0J0ryQNa6Y5Cy3DjQXS7Uxc-a9ekim-cJirCdGnUsVudHnODH2LBKH2CwovSpbTzDd9a1659o-lUDKU2iBtuL_suA9FPr5mb6omHm0q7L41Aik_NEZ_Elv1uWDeFP2brPco2cienQHLN8hVVFhQbg4UVIYA19F0cz4dARuUS6q-1a-J1BoarXIqd6OIflzGNWX3qesBGNQBgOM5NWnOSrnxcDSmWzJVPopVpj-NBt1UdFczE8d30-OIuHJhXYRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🚀
❌
🇷🇺
یک حمله دیگر با استفاده از پهپادهای اوکراینی به مرکز لجستیکی ویلبریز (Wildberries) در شهر سن پترزبورگ، روسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/68958" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68957">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=TnHD4MSGCj8UgjcUImrOx4f-AT_aV0yGMflr-X4WGouYrg9G9HSm0FtCxnPbuNhIUUS4chTIGfwiZBDEl_FkqPszvnRhyEWPMnTdKx4t8jSU5J377JtpqNyB4ZYCj5CSc60M4SK55OSZitdPt2kFilKxept7w9Tc3_OIooB1RQtSukQ1LjDHPyhcad4jz1ayhXMi029cNIB62G6Xrhp1U9atzYlN5rin1LBQxSBoo8UPUmPDrLWyc89BVqwKmM6O0W1JiU57UsE8Qrx9-zHst79fAnOsKbzfqQ5FSY6vEOnvSUsl_kH1Df274nksfJ84F-S0nmtqmW2qNfdX6dZ6hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=TnHD4MSGCj8UgjcUImrOx4f-AT_aV0yGMflr-X4WGouYrg9G9HSm0FtCxnPbuNhIUUS4chTIGfwiZBDEl_FkqPszvnRhyEWPMnTdKx4t8jSU5J377JtpqNyB4ZYCj5CSc60M4SK55OSZitdPt2kFilKxept7w9Tc3_OIooB1RQtSukQ1LjDHPyhcad4jz1ayhXMi029cNIB62G6Xrhp1U9atzYlN5rin1LBQxSBoo8UPUmPDrLWyc89BVqwKmM6O0W1JiU57UsE8Qrx9-zHst79fAnOsKbzfqQ5FSY6vEOnvSUsl_kH1Df274nksfJ84F-S0nmtqmW2qNfdX6dZ6hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ :
وقتی توی یه جنگ
داری قاطعانه برنده می‌شی
، باید چیکار کنی؟ دست از جنگ بکشی؟
ما با اختلاف زیادی
داریم این جنگ رو می‌بریم.
همین الان هم در حال مذاکره با ایرانی‌ها هستیم و اونا
آماده انجام کارهایین که قبلاً حتی حاضر نبودن بهش فکر کنن.
🎙
خبرنگار:
شما به آکسیوس گفتید در حال بررسی یک
«حمله گسترده»
به ایران هستید. نقطه‌ای که تصمیم نهایی رو می‌گیرید چیه؟
🇺🇸
ترامپ:
ما در حال مذاکره باهاشون هستیم. شاید اصلاً به اون نقطه نرسیم، شاید هم برسیم.
🎙
خبرنگار:
ایران کی بالاخره کوتاه میاد و پای میز مذاکره می‌شینه؟
🇺🇸
ترامپ:
شاید کوتاه بیان، شاید هم برن توی یه غار و همون‌جا قایم بشن.
اونا غارهای خیلی عمیقی دارن که می‌تونن توش پنهان بشن.
ایران، باورنکردنیه، ولی شروع کرد به شلیک به همه جای خاورمیانه.
اگه سلاح هسته‌ای داشت، حتماً از اون هم استفاده می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/68957" target="_blank">📅 23:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68956">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=P_7xWwNzaw6cz8Ck_92kGJBu1aQfbZ4jKSKy76bO5vQ8-yDXfs6yOM1dRX41nxR1YkTckm0nv-OjgBldH0r0ucaXBq9xZS_1hTG7spwb8SWZJ3aqPLaLMXLAfzaoMYI9hjFVRkGx_QhlnrG8U7GBr_OGiNtx6_OiV-ua_-npgxy1T3EUlpsnCI2n4lG3EUhJtNtJ5H4ACRt4XD-WO-eKEVDh1T-mwmDqlmFAEw37es_BKR5NxDvWTJlrsJhzflIXrIulfHDQ9rSbtaMu-F_Qu29Ufk6OwRlo0eYsxPd_D75sL9Y2ZQwcrQNOlUO0KqSaS01PqRpHyVnFon_MW5A-fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=P_7xWwNzaw6cz8Ck_92kGJBu1aQfbZ4jKSKy76bO5vQ8-yDXfs6yOM1dRX41nxR1YkTckm0nv-OjgBldH0r0ucaXBq9xZS_1hTG7spwb8SWZJ3aqPLaLMXLAfzaoMYI9hjFVRkGx_QhlnrG8U7GBr_OGiNtx6_OiV-ua_-npgxy1T3EUlpsnCI2n4lG3EUhJtNtJ5H4ACRt4XD-WO-eKEVDh1T-mwmDqlmFAEw37es_BKR5NxDvWTJlrsJhzflIXrIulfHDQ9rSbtaMu-F_Qu29Ufk6OwRlo0eYsxPd_D75sL9Y2ZQwcrQNOlUO0KqSaS01PqRpHyVnFon_MW5A-fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
یه انگل هست که باعث اسهال شدید مردم آمریکا میشه. کی دوباره میشه کاهو خورد؟
🇺🇸
ترامپ:
نمیدونم. بهش فکر نکردم. پیتر، زیاد کاهو میخوری؟
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/68956" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68955">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=u2ivBJJaRADSOtJ8oEaTR8UwrwcvVvi0CKzsE7RiU9T_olX-C2PG8FoiwQCuBPJa6ZwZesHgxeIDBql3ErW7RVoBT34FMGZHEns9KeWTfWCGcZqMyFq-7BKOySJ0SNutLSRo2LwGyYNAVbVXBo6Tm1TafKFhBIh-Wtqa7VrGKZb6ALFeUkZ_VuAQtf4PjSCtW5eQkwO3M8yN9tFfP6LwEYbw-NkzlDjRWpuLDps-3PgwkfFlyFVrWxHr-xf7N_Q7B0IIz_55UevTaeK7qCZg9Gf7mkBDTRUi_IRFrIEB0-2jv4U04jfjkj3inQeCS7TqPZcC7nBdzR1aMRrVLhxpWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=u2ivBJJaRADSOtJ8oEaTR8UwrwcvVvi0CKzsE7RiU9T_olX-C2PG8FoiwQCuBPJa6ZwZesHgxeIDBql3ErW7RVoBT34FMGZHEns9KeWTfWCGcZqMyFq-7BKOySJ0SNutLSRo2LwGyYNAVbVXBo6Tm1TafKFhBIh-Wtqa7VrGKZb6ALFeUkZ_VuAQtf4PjSCtW5eQkwO3M8yN9tFfP6LwEYbw-NkzlDjRWpuLDps-3PgwkfFlyFVrWxHr-xf7N_Q7B0IIz_55UevTaeK7qCZg9Gf7mkBDTRUi_IRFrIEB0-2jv4U04jfjkj3inQeCS7TqPZcC7nBdzR1aMRrVLhxpWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
وقتی من وارد ونزوئلا شدم، همه مخالف آن بودند. اما دو روز بعد، آن‌ها گفتند: «وای، این فوق‌العاده است.»
بسیاری از افراد همین حرف را درباره ایران هم می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/68955" target="_blank">📅 23:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68954">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=HSsKfbG6yjTEMlQvpVJ2RLO96VeCQY66FGGnc5BoEl1Yr8ASzjpLRztAHYoR1EeB-Q1wFx_Tso3CTiczZnx7-9gLn-9UF0-9IsVWVmaoVALG1kAQfPTBZsKxh0LtJac_C7psjWQyYaV_HjDYvsqoRYYHI1yEz90Wew2ZYcOrJsreGx0tcEbomtP4Y6uCVnD_Ck4--oLN5DfmUWdtsgsz2HNjJJvyDs92T-zcXoXPxJfwFPbauaZ0cl-KP4ym4RhH4LYCg1NfPdoy06s7CEhl1MsHnSFDt4z19wLT3s__kg8VLslxA-t4PIKkM6jYIY7QDQc8dHKknHgDgR_otck-wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=HSsKfbG6yjTEMlQvpVJ2RLO96VeCQY66FGGnc5BoEl1Yr8ASzjpLRztAHYoR1EeB-Q1wFx_Tso3CTiczZnx7-9gLn-9UF0-9IsVWVmaoVALG1kAQfPTBZsKxh0LtJac_C7psjWQyYaV_HjDYvsqoRYYHI1yEz90Wew2ZYcOrJsreGx0tcEbomtP4Y6uCVnD_Ck4--oLN5DfmUWdtsgsz2HNjJJvyDs92T-zcXoXPxJfwFPbauaZ0cl-KP4ym4RhH4LYCg1NfPdoy06s7CEhl1MsHnSFDt4z19wLT3s__kg8VLslxA-t4PIKkM6jYIY7QDQc8dHKknHgDgR_otck-wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همین الان هم در حال مذاکره باهاشون هستیم. به نظرم هر روز که می‌گذره،
دارن جدی‌تر می‌شن.
من معتقدم
توافق، راه عاقلانه‌تره
؛ اما کاری که الان داریم انجام میدیم،
راه ساده‌تره.
همه‌چیز آماده‌ست و هر لحظه می‌تونیم اقدام کنیم.
وقتی وارد ونزوئلا شدم، همه مخالف بودن. اما فقط دو روز بعد می‌گفتن:
«وای، فوق‌العاده بود!»
الان هم خیلی‌ها دارن همین حرف رو درباره ایران میزنن.
به نظرم،
ایرانی‌ها تا اینجای کار از همیشه جدی‌تر به نظر می‌رسن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68954" target="_blank">📅 23:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68953">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=m2_tYk8N5ab1Ct2tFVffz85uPdj2Qyz-g9Vnwa1eZROXE-AwLAySAG6o9-wSCXCG7vUSbSqFifxKtaEZptZtZnMTafGW3XPsv49iZliZ0YNylUGLZ2VprgX1RJ7xqrFoDvvB7Gq5Jv-EHCwJ__LZdXX6xGO3tw1sAjOIGMqbTwoZujqWU5pOTFoZWM8GuUyyIkprnBOzJ-ZKHcYo9XrpHaVZ_L-qd2Rf01aP66rw8G4TSqmvV3GaKOksaAzFp5LL6qYZUN8g-e54mgGHZO4GFqtoGAS-DNqdnOY_lBTFluIN23uynwtCFBQc5aDX6IUz2KNmXb-o9Ou1VGA8aIR3yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=m2_tYk8N5ab1Ct2tFVffz85uPdj2Qyz-g9Vnwa1eZROXE-AwLAySAG6o9-wSCXCG7vUSbSqFifxKtaEZptZtZnMTafGW3XPsv49iZliZ0YNylUGLZ2VprgX1RJ7xqrFoDvvB7Gq5Jv-EHCwJ__LZdXX6xGO3tw1sAjOIGMqbTwoZujqWU5pOTFoZWM8GuUyyIkprnBOzJ-ZKHcYo9XrpHaVZ_L-qd2Rf01aP66rw8G4TSqmvV3GaKOksaAzFp5LL6qYZUN8g-e54mgGHZO4GFqtoGAS-DNqdnOY_lBTFluIN23uynwtCFBQc5aDX6IUz2KNmXb-o9Ou1VGA8aIR3yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما درباره بمباران نیروگاه‌های برق غیرنظامی و پل‌ها صحبت می‌کنید. بخش بزرگی از جهان این کار رو جنایت جنگی می‌دونه. شما هم همین نظر رو دارید؟
🇺🇸
ترامپ:
به این سؤال جواب نمیدم. شما از کدوم رسانه‌ای هستید؟
🎙
خبرنگار:
نیویورک تایمز.
🇺🇸
ترامپ:
حدسش رو زده بودم؛ نیویورک تایمزِ ورشکسته!
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/68953" target="_blank">📅 23:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68952">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEEgnEewKE4UslcEgzbabMID-mn_5eBMUY5qvQbxJiKS5oqmVotiSIdz6JpeFKdl_WbE8zmZbMt7jZMQdREe5_JVhi4dYqQ0Y9XTBJpEzA2K2hh_zrrnAU7KWiC0DwFWKJSH_7kxBG1454Mi-_NzbiLYKkS4WFmgpIh25536NNAZc9_yQwy0C0V-Vyw8q6GrpmXzYyMuWt6tEiUABIKENM748cVt0Ig7YxPC6eIswl6kq_IndBs6Fg3pJxBBsIVNb3G7AVxW2iMBr-0Ezpv6rbHiBCSzzC4ajGvdqFQXpPux6YE2mEip1o-8uPIUChf4_MXynlHzxmBQdSdSumSqYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
صداوسیما:
دشمن آمریکایی دو موشک شلیک کرد که یک نفتکش (یا تانکر) حامل گاز را هدف قرار دادند؛ شناوری که از دریای عمان می‌آمد و قصد ورود به منطقه را داشت.
نیروهای آمریکایی گمان می‌کردند که این شناور قصد حمل گاز ایران را دارد. اصابت دو موشک به آن منجر به کشته شدن دو تن از خدمه و آسیب دیدن موتور شناور و در نتیجه توقف آن شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/68952" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68951">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">⏺
ثابتی خطاب به شهریاری:
تو دیپلمات وزارت خارجه بودی چجوری شدی استاندار؟
اصلا بچه شمال شرقی، چجوری الان استاندار در شمال غرب شدی.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/68951" target="_blank">📅 22:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68950">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🇺🇸
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا بر این باورند که رهبر عالی جدید ایران، آیت‌الله مجتبی خامنه‌ای، بسیار بیش از پدر و سلف خود به دستیابی به سلاح هسته‌ای تمایل دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68950" target="_blank">📅 22:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68949">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u21hxE6TBKmi5QqsWR6ujBfbVtUfs4cORZt8lx1lNeuQnDNXmHIjfP_5n9QVYFhkOJkk2LH2WvR_heJfr0luf5pB8kJSfem8WJdodX6jMj52J8gw6HI9hWC0kwUms_88phIVVCsSTKl0eFQW1Ad__PvdSmYG6Rhs1wpaGKLFrnLKpicR1MCxmj-mXEebaNxGl-ymc1x0UL2f5wOPLluV1fBGSCjS11kGGRvGGKzqOYXQbJL9cJUDUdmnadm_zEpa_-BYq_WQKyXh-V_bnRhR-0w-IUA5OlsdRGbXAR332nqL4DZsSuEpg-6NaXLQ5qcXtqYWYMDAjwd34J5joFZuaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک‌تایمز:
رئیس‌جمهور ترامپ روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه خود دیدار کرد تا درباره تشدید حمله نظامی علیه ایران تصمیم‌گیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68949" target="_blank">📅 22:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68948">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7Mh_vlyTE37MFQDkyfLJVwubVzlwM9u7uuXzcx9UMU6Ud8ZXyVswaKTI-EM7-z4nTve0I1TGjD3TM3SgZev_e-8-ZzgzrgPTAR04lW3r3WtCAm-bK7sbSssUH9MhnWKNLy09V-GljXz-rL9Gj9GZXr6d_BnaLJCs8Vbakn2qxb451Rtrr2lPEviX_cnN8WrdZfbAmj8jmG5s4dhQp_AvYjgSr5lcbt45PfMfh7JTyHxWQxD5aUs5RQxNpwvTkaYGNMHpQeSUL3xPMRPfMwdw_HSyolO98yAltOJ1ENgDSu4RRzuknaixBuqre_UHE1069xffQiBSK_ijFltSjQwBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
تشکر از نخست وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68948" target="_blank">📅 21:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68947">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78c449631.mp4?token=U9Y_K_e88nQ_ZSiaf2dKFRplKIqPK0jiUvWxuvYeq__mU2XR1I3ID0z36-xzyE9iWMsI_pfZvwrbyyG5kd7iqnUXsCNnu3eREPPLUWQtESOBdVtEwrElCtDSh6XalPqa4sDTnpIDP2Nyw0NUxTbYU2lnQkz3sMCUmVc-Fxw7DkzAXJ0TTKp_bl-SUJp6kenr8agxwXkXCshiOgBXixdl8MuhqT9YfgNh3pDQJ-kaR_fPHT-htJshswuAkuFqynxEHHGUMCQNC4RuUaJ0Xq-B44U2rI5jzDYgQPpkWw_NH4odCQ0X39IWWu-CMPN83n4KuNbKIsi14YcmyNzN0w3ixw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78c449631.mp4?token=U9Y_K_e88nQ_ZSiaf2dKFRplKIqPK0jiUvWxuvYeq__mU2XR1I3ID0z36-xzyE9iWMsI_pfZvwrbyyG5kd7iqnUXsCNnu3eREPPLUWQtESOBdVtEwrElCtDSh6XalPqa4sDTnpIDP2Nyw0NUxTbYU2lnQkz3sMCUmVc-Fxw7DkzAXJ0TTKp_bl-SUJp6kenr8agxwXkXCshiOgBXixdl8MuhqT9YfgNh3pDQJ-kaR_fPHT-htJshswuAkuFqynxEHHGUMCQNC4RuUaJ0Xq-B44U2rI5jzDYgQPpkWw_NH4odCQ0X39IWWu-CMPN83n4KuNbKIsi14YcmyNzN0w3ixw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
آخرین مصاحبه اکبرعبدی با گریه:
ماهی یک میلیون تومن به خانواده ها پول میدن
وقتی روغن یک میلیون و هفتصده ، این یک میلیون روغن برای چی میخوان مردم ؟ برای جق جق در خونشون میخوان که بریزن صدا نده ؟
حالا روغن خرید ؛ باهاش چی بخره که چیزی درست کنه ؟
نمیدونم این خدا هم حرف گوش نمیکنه ، من با کسی حرفی ندارم فقط از خدا میخوام به همه کمک کنه
فرقی نمیکنه فقط به ایرانی کمک کنه
به هممون کمک کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68947" target="_blank">📅 21:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68946">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNpXn-_RhbulEH-gBH3Gukv_StnQjI7WbkhoXfhX_idZkhA_yH39wKZddKz3ZQycBgVHvxi2b9Hqz-rCI9P42yl9I8PlB8fouknuJNgyJeoHJl_bvKSpMu8qQ6Se4OCEOJRpMMXZENhr4WZOoj-GTDFI9bSJDpHuWQZ9KVHRlYW-y8rMfcVILzTFizToBL_mchhv5cCSWDyOB03Em0wi42NOdKGMYgdJeOHvy_st46PW2PRm_AvYVM3ycJnun0LaOoWmMcCIeNuGhO_v6dtJAbVPavLmyZ-OyGYfmJKo_9aaklfHym4XPYitfMVlkcWoW6moMt9T9DvbT_R7xfMxCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون، در سن 66 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68946" target="_blank">📅 21:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68945">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnZTGdNnLP8UfQYOIY5sDGZdSgwsAS8lNLreJeSU890R_7wLAiZiP4Yw-aDd7MKPGIqmets7WzjFxH1Onpp1npsx_K94WffFC8qwY60odu475hxItTx1O5XTIyZ1O2fE5Juvgf_rfeU5tfTMcJSwalzjGp9x5HdZSjJ6-HjRXLMj7ThVfEn0xmD-fj5FiLizvXCLNtdCSy4Q0jmPE9M36O1BYXvOr_KAbqniurxJqine6l8Z07FX1efiY-XXe9sMKTGhXRG2y8XUdQPoLjHEHhXkouhIaQgtwl8ONc1SM0Zz3c4R4i15WR-jebkij0gFB2hrDJuwVM5QLZQFtZA-EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
علی عبدالهی فرمانده قرارگاه خاتم الانبیا:
از این به بعد به ازای هر شهیدی که از ما بگیرید یدونه امریکایی رو به درک واصل میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68945" target="_blank">📅 20:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68944">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2066d70166.mp4?token=d4mYT9k21vLbdJnfHSedmHBQNm27pIxDSgIl-m5e1_YjVnzd_gLx6rzCrunw5xHcACfFWAr8a9dHhfBiK3QXSbadQvrqLf9SlU1V4jUr91XmUhWU8UjgBjLC_Dm5UoyBjgogQIg2qP2BrAjy4fwpW1EDdhk-OomBlh-Gz27-b6q8vgMB5rZDNZYAZfAzrYn3uq4G41mRj8xDVfw9v13T94lJcSNcy6PmXxyZXKtIC3VOrr49Vl6nQGzHSGnCDT7s3KdvLgAIsP4KqqdRwZSO5tIaQGxZonoLdGGkLvwzO00DgTv8DifoprJsoVHESICcbFKDejvsGrWpMyc4klUdTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2066d70166.mp4?token=d4mYT9k21vLbdJnfHSedmHBQNm27pIxDSgIl-m5e1_YjVnzd_gLx6rzCrunw5xHcACfFWAr8a9dHhfBiK3QXSbadQvrqLf9SlU1V4jUr91XmUhWU8UjgBjLC_Dm5UoyBjgogQIg2qP2BrAjy4fwpW1EDdhk-OomBlh-Gz27-b6q8vgMB5rZDNZYAZfAzrYn3uq4G41mRj8xDVfw9v13T94lJcSNcy6PmXxyZXKtIC3VOrr49Vl6nQGzHSGnCDT7s3KdvLgAIsP4KqqdRwZSO5tIaQGxZonoLdGGkLvwzO00DgTv8DifoprJsoVHESICcbFKDejvsGrWpMyc4klUdTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما از یه بازی فکری رونمایی کرده که توش باید
بچه‌های جزیره اپستین
رو نجات بدی و ببری
بیمارستان خاتم‌الانبیا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68944" target="_blank">📅 20:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68943">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2RPDkiriB_WUbRPPJcZQGtUvOsBM0WylXl_BYW8NMCdxgSDZYVfAyhVhSSkrYKAlkJOi9xOGkcOJZtngKaEAGMZqlemrkte6sJeeN518U32hkbNBibc4ipjIZyefjtVztVnET-KpKcbE7H-bcTaTWB5YepXK2jcyYLlkvLDqEGEwpwmD2WI_vZ9BDCCFOWrGBCDt9BvXukF0yON_Yc0qsFZ8MXzVDs2m7TX-ZrR168TciGGDfdA2Oac5EKAl3q9ZhjcxVZSB9aGd5vM38jaJTxj1Tcpiz85K8sIvhZRxucHJdlvdYuqRY91iBoCt369UT80nEilyAPqSgl1PFtEYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ:
رئیس‌جمهور شی در دیدار اخیرمان در پکنِ چین، به من گفت که تحت هیچ شرایطی به جمهوری اسلامی ایران سلاح نخواهد داد یا نخواهد فروخت؛ و این گفته شامل شرکت‌های چینی نیز می‌شد. با توجه به روابطمان، من به حرف او اعتماد دارم؛
ضمن اینکه خودم هم لطف‌های بسیار بزرگی در حق او انجام می‌دهم.
به همین ترتیب، رئیس‌جمهور پوتین نیز با وجود جنگ هولناکی که در اوکراین جریان دارد (و روابط همچنان برقرار است، همان‌طور که با رئیس‌جمهور زلنسکی نیز چنین است)، به من گفت که به ایران سلاح نخواهد فروخت.
او درک می‌کند که من به اوکراین سلاح نمی‌فروشم، بلکه به کشورهای عضو ناتو می‌فروشم. آن‌ها بهای کامل را می‌پردازند و من هیچ اطلاعی ندارم که آن سلاح‌ها چگونه توزیع می‌شوند.
بنابراین، به عقیده من، دو کشور عمده‌ای که اغلب در ارتباط با موضوع ایران از آن‌ها نام برده می‌شود، در این کار مشارکت ندارند. اگر چنین می‌کردند، برایشان بسیار بد تمام می‌شد؛ و قطعاً به نفعشان نبود.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68943" target="_blank">📅 19:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68939">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iINLIwQJOe-e-sTck44oowJ0GlZRX0H_oiga6eqDVqp1wBEh4RtHwdE-_hVODyZxzhOqu2091IRMmIVOGFS8-OBkLHMasdMVo-7enIhbwOJOqw5NGBsm-zFyTIuwz8pmXN6srgbXGTZ770eW4A5NOGDXRMOI7u8lwl8ZoiD-amnjhvTMUZno-k43QS4-JU_5TVhO0Ir9xwV7lF7d1_54g65wdKEYgFYaInSK2eWL2Tg54pe3f3wxYeDe3RpRohpVnSnUlIn33QQY7dg7QlmeiT21EmBllfg5CHke7WMCVWA71yCCju80pYU6-caOF8PZm2IvhaJfweFA7hfHLk7ZgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aYXKLhzNkBrgoZZCKmio6fvj-Y8l70W8Cy5mBW4hujzD7hopl1RyQ8zq_N9Qf28Bwem49Dsj_ZzSxZh2LbzeGad7OahnkoA-oM1IkcDu5Mq6NpS-RRjx-9GeozkUY6RzMqtG_2Gd7X5MSAHPLtT5OrKeIEwY5uJclwv7iMdNnyC8I1exK9glZ4OASidvipoZkRq4U9wqmUqwrYPiCq3LRAnz_hMJoOIybbommhh2A2-3-J6-qI_Uq4-Iu_L0MJoNwz5K4FJ0wYDs2BCIR1q9hzyP0kD78yJ38ujSbZCyTDW1w5hySZsDA3NeP6LmPv_G41H4XCobj7auC334uFnVwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d-e7s_oqzMpRSJx0yNYDL_KOGbYRHJl47Ayu5o135dtT0Ejf1Bl2Hu445h11tKqNR2QaD2N5_Wq4OQTguYnYpszvvxasj0CVCOIylp4U3bN-9-n6PyNREYyL2SOrZywSwFT3pH5Y8tU7OqYIVlsQXeKvteJhG4tmPnIBBzLg6qiadz477Vlm3IqZJEnvHc4qjeDJOIXY8hyoGTjYeBOk-Gtfc-X23ns-cSQhghGIUZtBiI9GasDUgqOTHNDZie_Z7NXC52T-wAgib6MT_Gtn43QMdW0drD69Sv_qmgt-pjn4xM3htVJn_KRbITklBA3WuuH3_px0Hz9YYV2WxLx4lA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=sNIGGzvHjwqF9K8jf4aAY36yBbcXLPCS7UZsGU1rPVPh5u4XbugFTXlSKfmU7e6FvzK4eEZQ2VnUM6800TKtPsF0weR3YcMQ2HeUKhD9hrgl8vARDa3Eu-QVtkBFxc6PiZoyz-lTW3TAhtiL4YsHv6rAWG-y4vBs2SSndJg1AKLuL3s2pzHsoQyCinE4yX1rtsUnJokbU9dvZsss9tppzW0P1Igfjea1m1U2w2bN6XWgkXusVjRaxkIEksDZ0pVzlwQXRg7zrYIKsOKKnE7r5y7MhfT0PlEViJxfwWOz5yyoCk1mDlllOzsl1AR8ZfBvoiMnXbQEftSEujpwJnnIpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=sNIGGzvHjwqF9K8jf4aAY36yBbcXLPCS7UZsGU1rPVPh5u4XbugFTXlSKfmU7e6FvzK4eEZQ2VnUM6800TKtPsF0weR3YcMQ2HeUKhD9hrgl8vARDa3Eu-QVtkBFxc6PiZoyz-lTW3TAhtiL4YsHv6rAWG-y4vBs2SSndJg1AKLuL3s2pzHsoQyCinE4yX1rtsUnJokbU9dvZsss9tppzW0P1Igfjea1m1U2w2bN6XWgkXusVjRaxkIEksDZ0pVzlwQXRg7zrYIKsOKKnE7r5y7MhfT0PlEViJxfwWOz5yyoCk1mDlllOzsl1AR8ZfBvoiMnXbQEftSEujpwJnnIpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ویدیو ای از بمب‌افکن(B-1 Lancer)که گفته میشه در حملات شب های گذشته علیه اهداف نظامی در خاک ایران شرکت داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68939" target="_blank">📅 19:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68938">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=Vnl4TS2pQodfoVkymFX7mqG_fzGX7VHJmMlznV13NI8yNI4Y7TOm3e4f9_fIuDx_VMOcqZGqx4SJqFv1e5k6mXhrE-65B9Cm8sNzEN0eVDyfTxeJSToaT6CgPQZHQPy9cltIPx5BCOnEhwmfmbInQt9zE_skQujoUfHE2bMkeX_F-06rvJTD8iwqid90OLSyALVy7kmmIXoEPIxpCPvss9nwjYZd0vNZFwGw1QFLzprBS4b8U3n5bjuzzdGP-l5cu1pqa0m8Le5DZEHa1R_1-DgvVaJcJ5fEpRlCkTXpsHrZXyKuJacj2HLOYkt5ib2hsaO3iwmS2lf9zPr0rNEc3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=Vnl4TS2pQodfoVkymFX7mqG_fzGX7VHJmMlznV13NI8yNI4Y7TOm3e4f9_fIuDx_VMOcqZGqx4SJqFv1e5k6mXhrE-65B9Cm8sNzEN0eVDyfTxeJSToaT6CgPQZHQPy9cltIPx5BCOnEhwmfmbInQt9zE_skQujoUfHE2bMkeX_F-06rvJTD8iwqid90OLSyALVy7kmmIXoEPIxpCPvss9nwjYZd0vNZFwGw1QFLzprBS4b8U3n5bjuzzdGP-l5cu1pqa0m8Le5DZEHa1R_1-DgvVaJcJ5fEpRlCkTXpsHrZXyKuJacj2HLOYkt5ib2hsaO3iwmS2lf9zPr0rNEc3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
در هفته‌های اخیر، آشیانه خصوصی وابسته به سپاه در جزیره خارک هدف حمله قرار گرفت. در این حمله، چهار فروند بالگرد آگوستا وستلند AW109E که توسط شرکت خصوصی بالگردی خلیج فارس بهره‌برداری می‌شدند، منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68938" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68937">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEZ82PqCAF4RNKh18RXaVEZeGKnZ2U4ccFZX_K-79RwlZ5yKolNZJef3zpqbcS_m1af6TLmAJ8qbkDUYIRcqtBw3Ft50LFGl9YDO7V2TrxrtjaEIKrnknWep3CGEKMyyBRk-Ln3xlxBi0lcyw19_6lf1DWA1v_4Zv-yOEyBPsSHxLvs8LfyaEaBtFQWZOFCvdMXnE63MWeZ2pd2_TGAmhFnoeE7vIozFoZChRywdh1sA0Jr2PPu_S2MiNdxC-WRitQtfnW5VP8A3h9R4gh8kdf6FZrNJ-32JVGHoh3adj4nrdkT-rJCrxD-t_LK4M43IqrBdrEDDJk4kea4xM7d8tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رئیس‌جمهور ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68937" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68936">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887792c366.mp4?token=S6bbXlU28kKB01ZfqIF3sZ3fvkQMv0qUVnhXJVEpGdbsx8Ue6B3VzN8CHW9JiKwkBMnAEvO0ZGfBJ5nxcEM4eRcqyrN62nEs2eTeXwSyvaCbwjy0n2pIDAi9xGvpja60nKD9Ixomv3NDxUjJOYt_nyYizATIU9DfdzjMGesMMITJD3u-6UUPzNlmcJTfzVNRXBe7BwbUo7w99V5yXJZmpxeAjo9_pVm3edmEM9wn_2vTw2F1pbmcP1wEdXnJ6DEOLzr9kFpGqI43jAw56DTFiO_VIj5d8cot4yifYs3P2yiMTZZVcyUsMuqW81PedVLaYufpdmazy44TfJsPaDvQOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887792c366.mp4?token=S6bbXlU28kKB01ZfqIF3sZ3fvkQMv0qUVnhXJVEpGdbsx8Ue6B3VzN8CHW9JiKwkBMnAEvO0ZGfBJ5nxcEM4eRcqyrN62nEs2eTeXwSyvaCbwjy0n2pIDAi9xGvpja60nKD9Ixomv3NDxUjJOYt_nyYizATIU9DfdzjMGesMMITJD3u-6UUPzNlmcJTfzVNRXBe7BwbUo7w99V5yXJZmpxeAjo9_pVm3edmEM9wn_2vTw2F1pbmcP1wEdXnJ6DEOLzr9kFpGqI43jAw56DTFiO_VIj5d8cot4yifYs3P2yiMTZZVcyUsMuqW81PedVLaYufpdmazy44TfJsPaDvQOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
❌
👑
مقایسه تسلط زبان خارجه:
وزیر امور خارجه کنونی دارای دکتری علوم سیاسی از انگلیس
با
نخست وزیر ۵۰ سال قبل ایران دارای مدرک کارشناسی علوم سیاسی از بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68936" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68935">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=gHmHnkLUVG29Q7k8G12m-pFZgzTcBDpZYsw1ctcXjHTRLg6RUNqIIlDJCN5Fz2nvUX4gSEsQCbkG4TZah6az1wrfKsDCK_ZEHVAaAhNL5uJlavkCdkew_KGQP0S4P8vW7U-yJxMycLevOUir8MjpR8z5C8u8Rx5UkyKJtGN7saoWEw5tbIvPekv80wSsfw_hCiCYHFd3ZBOcNSHZUX6LA3e8oDhQuUqes7CLNY1ZodUtEjbXjrKhIOOOkntY6b8-grp56m6vc2B4Ca0YTSqGveHqhkawp1mPS7tLNRLhXGuaCpsBmN6252zxdP1-K8bRGgbkTwle7kd9oJjPkjKzSR-fFPZ7cZT6O7-XW6NnL5aT7mvhilz2gK1C_RqNGMjyeswoxWn3insyxQ9nnFtiOc4aUjm74rYqJD634fHKyEK8no9C8O7joGh-qWoah8ZNgu3G0r2AuGPAf4EIrPMPQskjr9XxoSXS6c_ckccsGjo309InI61SX1qLiPRFMA6QxouYLZmETJGUIoc4H0lWyhw52w5V2eEaMh_DDsSALw6YBmo9uoJ9reet8JDFKCTt77LR6bWyyu2Lb62uFowNaLo9zsdsb5T74gfogTw5L236_xGlko3UmSS0Y_uve1xe60kC1H4fPvyz9HyaerhZXAKOF-i2LT4ibcRLZg1JM_U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=gHmHnkLUVG29Q7k8G12m-pFZgzTcBDpZYsw1ctcXjHTRLg6RUNqIIlDJCN5Fz2nvUX4gSEsQCbkG4TZah6az1wrfKsDCK_ZEHVAaAhNL5uJlavkCdkew_KGQP0S4P8vW7U-yJxMycLevOUir8MjpR8z5C8u8Rx5UkyKJtGN7saoWEw5tbIvPekv80wSsfw_hCiCYHFd3ZBOcNSHZUX6LA3e8oDhQuUqes7CLNY1ZodUtEjbXjrKhIOOOkntY6b8-grp56m6vc2B4Ca0YTSqGveHqhkawp1mPS7tLNRLhXGuaCpsBmN6252zxdP1-K8bRGgbkTwle7kd9oJjPkjKzSR-fFPZ7cZT6O7-XW6NnL5aT7mvhilz2gK1C_RqNGMjyeswoxWn3insyxQ9nnFtiOc4aUjm74rYqJD634fHKyEK8no9C8O7joGh-qWoah8ZNgu3G0r2AuGPAf4EIrPMPQskjr9XxoSXS6c_ckccsGjo309InI61SX1qLiPRFMA6QxouYLZmETJGUIoc4H0lWyhw52w5V2eEaMh_DDsSALw6YBmo9uoJ9reet8JDFKCTt77LR6bWyyu2Lb62uFowNaLo9zsdsb5T74gfogTw5L236_xGlko3UmSS0Y_uve1xe60kC1H4fPvyz9HyaerhZXAKOF-i2LT4ibcRLZg1JM_U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عباس:
چهل روز جنگ و محاصره بود هیچ کالایی کم نیومد
بله قیمت ها یکم افزایش پیدا کرد که طبیعیه
یکی از مهمون های عالی رتبه ما اومد ایران و تهران گفت من وقتی شهر دیدم تعجب کردم
گفتم این همون شهریه که جنگیده و محاصره کشیده ؟ من فک کردم الان بیام تهران شهر مفلوکیه
همه دنیا داره به ما احترام میزاره جز خودمون
من رفتم عراق حرم اونجا استقبالی که عراقی ها ازم کردن عجیب غریب بود اونم ساعت 2 شب
این استقبال از من نبود از وزیر خارجه جمهوری اسلامی اونا به من میگفتن قهرمان
عراقی ها این همه شور و شوق داشتن اونوقت صداسیما یدونشم پخش نکرد
یه نفرم اون وسط تو حرم گفت مرگ بر سازشگر
با مرگ بر عراقچی مگه مشکل حل میشه ؟ من اگه وزیرخارجه نبودم باور کن پشت لانچر بودم الان.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68935" target="_blank">📅 16:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68934">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:
حمله پهپادی به مخازن لجستیکی ارتش آمریکا در صحرای عربستان.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68934" target="_blank">📅 16:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68933">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn5QQnV6zuTFsYpRQPS05KlYZTnBmspQVqUzM04t_aA_N-2Cg56NaNbNOzhPNrPdU2xkvgp0k8wpOuqDDc-J0XwmaknS0s9Nv-6jTUhQxuB2nwwILEDlhywbxPE2DHNfYd3A7v-Va0hMOFs-SsgeKPPrVqL0U_fHu0IZd7PHcRuEZr_xKJL51qMfRMgpqCOGFhD5vP1y_BZ9FanI83dP1-s4ARNVk_o2D_Arw4gpHYV-IAQ9YEGV8INGJd9SK_yP4AsVN8u8s9Rq6Yj3uQph4bSXkV5A9TaL6i9l7XvKjCzNvXt2GO0KEb3_YthVF_1yi6PcWXxbT-oy2SA87BxTqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت حساب وزارت خارجه آمریکا؛ سیاست رئیس جمهور‌ ما:
یک سر در برابر هر چشم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68933" target="_blank">📅 15:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68932">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8y8dSOFhGftEFtB2GkYZJSkSMbSOoffc1yMeKnwrZVB4YC-zx9S6kY4kd48NALGw_ZP4t561nDZeJcBt8kduQ2zt_L5a3DGp8k72cgQ-jjJ_lFLz4-2hpeTXjnONWXxICQiQsdvRLRZrLQ9b9f2w0KHSr6MFfxn5lQb8HeRAIwgZJSAtzAIn--Go-LJjkwOmtCna5gzgt5YDOYx5TW_UfuIeDeHr5TnCPj719EoYmhrCb4wi0sLFngfgSP1Woye5Hz4o7IFjVd1SKStUQLtjQSJ3-pMGHUKQ_YF2qN9gh5U5FOxUVLF_JjKryok0-lukT7uQV9wf-UFaLE-KpHoYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
وزارت امور خارجه آلمان اعلام کرد که این کشور فعالیت‌های سفارت خود در تهران را کاهش داده و بار دیگر از شهروندانش خواسته است که هرچه سریعتر ایران را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68932" target="_blank">📅 15:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68930">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HALS0fGIfVd9PhNCGqVVmTXLUQgF3X62dxWrhnLZMq8hM3nWUjPezmmOm775PCof3EYdgt5YbZCzUnzPlajb5pjzBMGf_OYppsZ81yoBvGgqOagrKgf156ZSi100wLnmfSHHGsHRw23TyVm6rtF9ZauHdCTZnKNI6GirJduOVrXwnwcNgEqkcE3AvtHqnSbghQMHSGjOro2Ina88QjaPTpW4hdvqgBXwLYF81tc08bCZ_mBWKKaB6d-u9ptDYevCv9Lp_fppJf9--wSiIIqBPUiDpWd2_KrdoNhIbG9y-QMPunZX48d51S1ieFFD_I-tKeOvnkfu5UCvkS0iAw-E2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hRJ7TTGs2Ofl8jong2j-sno1zEHUBkmLj_Gl2EPO-WxYj9RrPG9LOR5ewe0cepztxxUHGHwf-QG0Ba6a329KNdVOkcUMnEGYJhNZnktH5usS7NmgMpJRfSJRkJEw5xY0AXkThUCDk4xSQ0sJZmmBLcW0Dmm7SsB9_9C8ABIjXtyyHjWLtEj1lL1TenIaefrqC4juhpTeAT7URNk8ZqsTqjk4zrh8HFcT-yjzDw61Q_GlJmznveAi6GhtC8EtBLOClaVrmaqFCU1A1YXtn4elZSQMv_ravXg3jDCU5u-I2YIGgqDtPpBsQFWiYurVzbSlxhfyHQX-nr5fHW1vTuY7eQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای تانکر سوخت‌رسان آمریکایی به پایگاه هوایی شاهزاده سلطان در عربستان سعودی رسیدند، این هواپیماها از آمریکا به این کشور آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68930" target="_blank">📅 14:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68929">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=PoMfqO5j-3kzg8TyBBSTL2kwQ4e5X-v1Du48cFatYAU5__MJ3zPuixctrQlcbLjo01h9F_4Y2DPnRyFfQa4zEl2-ou8e5XiMjnXIo8vppQObRTXC-C5SJhNDex9dqpETmpKceY1N87UudMUT1iT_IOVePJbzTVS4V3O2CHAnz10y332_9RuMLCuXoT275kWAQGSPEagiZZpnjbyPx8taw2NmO7B7pcsIz_u5S2iFyGVGqd2uCZP3ZA3e7v60vgcxMn8xhFbCRmVzOyOQ5FrgdA8Vcl7baU-BHHijK9icMw2xcIe0_fdcvtUNOX8T97buz_nbPvSV9CervjB1NI18vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=PoMfqO5j-3kzg8TyBBSTL2kwQ4e5X-v1Du48cFatYAU5__MJ3zPuixctrQlcbLjo01h9F_4Y2DPnRyFfQa4zEl2-ou8e5XiMjnXIo8vppQObRTXC-C5SJhNDex9dqpETmpKceY1N87UudMUT1iT_IOVePJbzTVS4V3O2CHAnz10y332_9RuMLCuXoT275kWAQGSPEagiZZpnjbyPx8taw2NmO7B7pcsIz_u5S2iFyGVGqd2uCZP3ZA3e7v60vgcxMn8xhFbCRmVzOyOQ5FrgdA8Vcl7baU-BHHijK9icMw2xcIe0_fdcvtUNOX8T97buz_nbPvSV9CervjB1NI18vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقچی:
کتاب نوشتم، «قدرت مذاکره». نتیجه‌اش هم داریم می‌بینیم.
همین دیشب یکی از وزرای خارجه آفریقایی به من زنگ زد و گفت میخواهیم دیپلمات‌های مان را بفرستیم ایران، برای آموزش!
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68929" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68928">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
«به اطلاع عموم مردم کشورهایی که پرسنل نظامی امریکا در آنجا حضور دارند، می‌رسانیم که برای حفظ امنیت خود، باید فوراً از مناطق واقع در شعاع 500 متری از محل‌های هم اشکار و هم مخفی حضور پرسنل نظامی ایالات متحده، دور شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68928" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68927">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZ-lSjZISAuoodzRKJImzqFgRgwoH6sMusGPeWTlo_2q7HuiGyzO7ejb1sX2wmcuxW9uNC7pPl8Oq2MBEyfhtD2oaGJMfZXxRxKq9Segg34UU5m0YadNBo43k0FuPpFhfugap78ZdeLFKbcVydr2LnLU9hvr4p7QucTi5trJlokWGexnZTOJrz3fB-j6EBU9RJFBWvINTCcA3P0TVbApEA9rYcjbFE0UuFtILScMol94LIyE65mEUF6XkhjyACFVy2NiKzeMzW4w2PdcWiZD2hTrE-w4e7g3g1Gv3_xDM0kWDMAJHSZWm8jhhu_wLP0LMSk303QGwoYqCNxezfRIHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مناطق هدف قرار گرفته در خاک ایران طی حملات شب گذشته امریکا
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68927" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68926">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gu2hOnPx64uZ14BlnG_XdAIq6OuRaiFLMJeGDch5BhSLWaEfOfpfQBbmI1tdOiSCXOYWtmOMymi1gYCIEd040oT_XSlRgAnH35tquTTwk3tE7y4dfxiYo__Ff28b7hCyVNjeb_a8EkeB14sRc1euE73lEOX3Lzw_6wZgoc1HTfsyxChWEN_eX7Tp34h1sI_B8BbB7O7d1J2d3NDiVVaI4o3JNUqiTR0l-w6NZ3_bvWOjZL_SEW9s5r-l-RRlr0pimuvY-vBLMEAAzDQtqV3l6UEyBXViiZDw6mZzQeIpbKaOsLyUBfY3gkt5V8I1TFGGkADN1ztD7mai_sJJA58Fxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
جیک تورکس خبرنگار یهودی کاخ سفید:
نمی‌دانم چطور بگویم، اما من در خودِ «کاخ سفید» کار می‌کنم. از اطلاعاتی آگاهم که افراد زیادی به آن دسترسی ندارند و با اطمینان کامل به شما می‌گویم که آمریکا برنامه‌ای برای شکست دادن رژیم ایران دارد.
آن «کارشناسان» حسابی غافلگیر خواهند شد؛ هرچند بعدش وانمود می‌کنند که از همان اول هم می‌دانستند، پس... بگذریم.
به هر حال، خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68926" target="_blank">📅 12:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68925">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=EaChnUoo6Isd7r73__CLtmWSlrfe6ZEps5DsbMMJVkSL5vZzAAYqXwDQ26EtSlMlwi8toeXw1nhdmLsY_-Qh5znEyl9f9tqNx_z6nc2jMnYmcoh4qjj4faUbU5qTuylgvmjknWcD0Kma9agb9lQcYttxKo6EWRO-ouEK6js2xVjyIecAcUWPlrytsSVP51BFQ1NiJwzpDkBfUXG7LOV2l99bdtzcuXIRQU4LQ8MlP55ZfUqOV9i9N5QNQldUuYirBwLFf_H1r6RPeceFjJlr6XaJKRDZPNTGhAEt0bDGgJGu13mkYAGo1AHyGsm2tDC95d0qI5Z9HW0c7oh_BjP9tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=EaChnUoo6Isd7r73__CLtmWSlrfe6ZEps5DsbMMJVkSL5vZzAAYqXwDQ26EtSlMlwi8toeXw1nhdmLsY_-Qh5znEyl9f9tqNx_z6nc2jMnYmcoh4qjj4faUbU5qTuylgvmjknWcD0Kma9agb9lQcYttxKo6EWRO-ouEK6js2xVjyIecAcUWPlrytsSVP51BFQ1NiJwzpDkBfUXG7LOV2l99bdtzcuXIRQU4LQ8MlP55ZfUqOV9i9N5QNQldUuYirBwLFf_H1r6RPeceFjJlr6XaJKRDZPNTGhAEt0bDGgJGu13mkYAGo1AHyGsm2tDC95d0qI5Z9HW0c7oh_BjP9tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حملات ایالات متحده به ایران برای سیزدهمین شب متوالی ادامه یافت.
در این حملات، محل‌های گزارش‌شده‌ای از موشک‌ها در یزد، انبارهای سلاح در اهواز و چندین نقطه دیگر در مناطق جنوب و غرب ایران مورد هدف قرار گرفتند.
در پاسخ به این حملات، ایران صبح امروز چندین موشک را به سمت اردن، بحرین و منطقه اربیل در کردستان عراق شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68925" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68924">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=gffN4nA4NYQ_geiOs5MfbXwKoquRHt-JsOowBDGKeHMLAALrv414y9BFunBRIrOo0-johMIF4ocut5ydvG2mRRVwjl0zNqn8LkNRbP8k2aikeJXCaEAVPa1_jQ5nmG6Iik0ZRxvQXJE7WCLCutseUXeu0kuoD0Qfz3k2n86bnn9VVglcgrljvr5EuPdWwx1f8SPbn4KaE5KYTPcBx4m6ZSUwSQ8kGuk5mEXwGKRiyvybx7lnxzIVMp1sbcQvbheiqRy54xTyl6BdGRpsPg6X0SKrLsIgkfUNIwIDnLg76TsQrDRTmuXkMM9ALcpiDHKsVK1qoOCh_oOzMJxT1D8lfA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=gffN4nA4NYQ_geiOs5MfbXwKoquRHt-JsOowBDGKeHMLAALrv414y9BFunBRIrOo0-johMIF4ocut5ydvG2mRRVwjl0zNqn8LkNRbP8k2aikeJXCaEAVPa1_jQ5nmG6Iik0ZRxvQXJE7WCLCutseUXeu0kuoD0Qfz3k2n86bnn9VVglcgrljvr5EuPdWwx1f8SPbn4KaE5KYTPcBx4m6ZSUwSQ8kGuk5mEXwGKRiyvybx7lnxzIVMp1sbcQvbheiqRy54xTyl6BdGRpsPg6X0SKrLsIgkfUNIwIDnLg76TsQrDRTmuXkMM9ALcpiDHKsVK1qoOCh_oOzMJxT1D8lfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به اسم ناصر نوری گوشت سگ به مردم می‌فروخته!حالا مردم متوجه شدن و مجبورش کردن خودش بشینه تمام گوشت سگ‌هایی که داشته رو بخوره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68924" target="_blank">📅 11:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68923">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=DtZ7Gq_kjfI6lpY7Suy98XIReDKYVwgf7okSSJ1pL7S3w7RAK8tijDb1_548Xq5_4Yjy_xL0y2k04wVLLyEbbvae3xaiSSoaQAb40fXHQhWESNyc1B5QmlQDR-lYkvtviyH6YbyZMrRIAhjIr-Nc2kaAU2c2_3caLp0Ku2GWfx9JcTWMx3x7NT6LL4TYdkrJ0taYlz3vEU8SeMR6o9rxM7V52M2lBqMlayiD3mYqLrj5mB8x6-ItYhmWrZoKFjIvgL-JJHhl7NTDG3q-196JfDlSnIENkfbhVIOguwDPK7acB2Q0LauzDrES8FYic3TBxQDplO7dNJwxrcAIL0gN6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=DtZ7Gq_kjfI6lpY7Suy98XIReDKYVwgf7okSSJ1pL7S3w7RAK8tijDb1_548Xq5_4Yjy_xL0y2k04wVLLyEbbvae3xaiSSoaQAb40fXHQhWESNyc1B5QmlQDR-lYkvtviyH6YbyZMrRIAhjIr-Nc2kaAU2c2_3caLp0Ku2GWfx9JcTWMx3x7NT6LL4TYdkrJ0taYlz3vEU8SeMR6o9rxM7V52M2lBqMlayiD3mYqLrj5mB8x6-ItYhmWrZoKFjIvgL-JJHhl7NTDG3q-196JfDlSnIENkfbhVIOguwDPK7acB2Q0LauzDrES8FYic3TBxQDplO7dNJwxrcAIL0gN6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش هایی از سخنرانی ترامپ درباره ایران زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68923" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68922">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=MTwqjsuJBa2v_74dPudk5Vq3lEdiKhfgHjOaunIaCDBglrgqX7akucu0TYg3zrU5p3NX1yWA50Wls7bkJ_zDoAr-tsqhffNGS0pHQUutBfMGhmDP-WLq_tlNP6FI3knkJh4NBbF95huhRJrtpvLpgdKYG9jqLjeKCtEpZZVLBsVU1HZizfZr4BidnfZ4s6DeH1WGTljkv7x1PffXT5xbxojNICmXOuUIKuzksTdvT-UmH3MouFmm3p5YxWQX7GBtgrtHD7Do7OSYsQQgDyMeiG2DpmnacjupOGSonx0OCVyyWu9wzl2NLPxuTcE1Q2uMdjnHI4N1igCY7WuET6SWKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=MTwqjsuJBa2v_74dPudk5Vq3lEdiKhfgHjOaunIaCDBglrgqX7akucu0TYg3zrU5p3NX1yWA50Wls7bkJ_zDoAr-tsqhffNGS0pHQUutBfMGhmDP-WLq_tlNP6FI3knkJh4NBbF95huhRJrtpvLpgdKYG9jqLjeKCtEpZZVLBsVU1HZizfZr4BidnfZ4s6DeH1WGTljkv7x1PffXT5xbxojNICmXOuUIKuzksTdvT-UmH3MouFmm3p5YxWQX7GBtgrtHD7Do7OSYsQQgDyMeiG2DpmnacjupOGSonx0OCVyyWu9wzl2NLPxuTcE1Q2uMdjnHI4N1igCY7WuET6SWKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری به ثابتی:
تنگه رو بدیم بررررره؟؟؟ مگه مال ننت بوده که بدیم بره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68922" target="_blank">📅 10:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68921">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=npC3ijrb-V22sedfyNYXDFLicFRqgouxpSsyJXzrEkfd4hSHwq9QLW3MbGMe80a6fVWr1BZbLCBmHPkLbXrYIEWh9-9IvIGjSRu5LaJa-YzpVdGvKmoxHtml0lYwyAMynYO7JCylRLvAL74kLz4eRftaaLk1o5uLBkX7L6MJpqLKGrdFB8GlaKbj2ILewfbMoKLnPWHCHjFOewkGo2lf3559d-_WC7rPgQKXi7I6qo7vkw3ne3BNVrQgji8WpGiJKcD2Jec3atD5ijYvAQt3vrCXtnyif0sm50sLXjkA6a9QkoHPHP2nl0NOgCFq6MzDpYNrCwLDYcIPx1Qeld1lTg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=npC3ijrb-V22sedfyNYXDFLicFRqgouxpSsyJXzrEkfd4hSHwq9QLW3MbGMe80a6fVWr1BZbLCBmHPkLbXrYIEWh9-9IvIGjSRu5LaJa-YzpVdGvKmoxHtml0lYwyAMynYO7JCylRLvAL74kLz4eRftaaLk1o5uLBkX7L6MJpqLKGrdFB8GlaKbj2ILewfbMoKLnPWHCHjFOewkGo2lf3559d-_WC7rPgQKXi7I6qo7vkw3ne3BNVrQgji8WpGiJKcD2Jec3atD5ijYvAQt3vrCXtnyif0sm50sLXjkA6a9QkoHPHP2nl0NOgCFq6MzDpYNrCwLDYcIPx1Qeld1lTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جواد اوجی وزیر نفت دولت رئیسی:
ما ۱۰ خط لوله بزرگ و سراسری گاز داریم. در بهمن سال ۱۴۰۲، یک شب ساعت ۱ بود که موساد روی خط تلفن بنده آمد و گفت امشب می‌خواهیم آتش بازی کنیم‌.
از من پرسید فلانی ۳+۵ چند می‌شود؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز را زدیم. ۵ دقیقه بعد دوستان از دیسپاچینگ گاز به بنده زنگ زدند و همین خبر را تایید کردند.
تا لباس بپوشم، موساد دوباره زنگ زد و از من پرسید ۴+۵ چند می‌شود؟ من گفتم ۹، گفت خط نهم سراسری گاز را هم منفجر کردیم. سومین خط را هم زدند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68921" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68920">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
انفجار شدید در مراغه
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68920" target="_blank">📅 04:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68919">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68919" target="_blank">📅 04:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68918">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=qG6UTyN_M81YHqVPE_NlGQivQtb162sR-nr5HsUSxQhhZ62xI1PRCAjAN6MZSIRSH4pDRggfhriysUf4NqXNlgWfq9YHQBNGkoRAetjdIo5R1O6sFi3deT_JpP56wuLFjg1vGAS5qRtFN0h6Jua1qVzfVXzPkl7ukOrlTRjGG_D5-DfT3jOVEOK-U4nFAp-iv7H7by5JeI9PsGh25ywXhfi44QRvNHxoJMlhX0DWw-ZJEaWIWI-EULkSWGNI6Vg5sMkA8su54D2QSPFdK18S1jxpdDSlgc_CZcuFiDsnsOuWWM54Sv1dheObTMLIDRkQ1g6dF89GxqE-nSdxvqGcpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=qG6UTyN_M81YHqVPE_NlGQivQtb162sR-nr5HsUSxQhhZ62xI1PRCAjAN6MZSIRSH4pDRggfhriysUf4NqXNlgWfq9YHQBNGkoRAetjdIo5R1O6sFi3deT_JpP56wuLFjg1vGAS5qRtFN0h6Jua1qVzfVXzPkl7ukOrlTRjGG_D5-DfT3jOVEOK-U4nFAp-iv7H7by5JeI9PsGh25ywXhfi44QRvNHxoJMlhX0DWw-ZJEaWIWI-EULkSWGNI6Vg5sMkA8su54D2QSPFdK18S1jxpdDSlgc_CZcuFiDsnsOuWWM54Sv1dheObTMLIDRkQ1g6dF89GxqE-nSdxvqGcpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68918" target="_blank">📅 04:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68917">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سرعتی.npvt</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68917" target="_blank">📅 04:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68916">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CA1Ac1AYbaYlS-WlEXOiVNCiGZKoduUSbPo5Lu7h0xVYwreC6PspjyxI-E_An5mWwtyevvzeM9EWIbd6sdBVF3G34rqCexmSubMaDEDPMRQI7jU1fLgheECieyW634iImlsJGPWsd7ZFTDHtaawXVCdFOYT9UFbSyM8CI_tRVBlorZkp3lhWqrQtFS_RtTNS2LlrYCN6oYhuhrw3oY9f3AoX9-cJsy0fxqyzgptTHTnVOaIf4ZegBsPgu4ifWzbESdsR8CU0HQBgPA1NBYUhJpxJbAjo3a7sI1VXVBvepYPJqWgM0OZfzbLaN0ociDKgoPCG_C3B9jyFpKQCHkOxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ پدافند تهران به دلیل حضور پهپاد های شناسایی آمریکایی ها فعال شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68916" target="_blank">📅 04:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68915">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/la8nJkVM-wuCHHT8xB3H19YqjjzhKWTfPaU_lNBciCxArw_9ZC2lIRmslkAcp6ELoiGnDDBc0LNzDAqDix1EW-hu2kABDsx8yquJBe-kUx_HgHeNRywFs382FR8uHsY7lPvWTGkKwJVg0RL5OI4D-0gp8AM9ONGvJHXwZXVTE5zlpPMbQgPPA4UEeep0JK7lNUe7LLcByR_g7db1ZQDqzJdIz-7Fa-BROixPYtC7kkJo8a4bOMdKnLjmaxkg3e7dFgsceC-gn885Y1FGOUoaqR094tRW9XGwSni3xlZFYeDEH6ktFvsbNIQfEG6YjKymCixsWbaZjQnlh8UdEsMBwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68915" target="_blank">📅 03:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68914">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
برق مناطقی از بندرعباس قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68914" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68913">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtWDNwtu31kVZXCIbdCY1mRjbtv_-LCufgd9Uk1fX0FL80gFo9yV4qGkKcUEczs0bykWd13HAUHZOVY9PaOq1Lrj0puMP-r4xAL7WyVXLeZ1mSSJm869pZ_eSDjxwU4YfYwGcfE3YZRt4rZnUXw9h8VZrwNTHlMvPLCYHMLAIUqPyM6X8NB7jiZMXbWPvFrMbzdJ2cvqw_GK4ZXgAuuMxltoGzalwg1-Ber8GMIpYY5jKHHXOrafsdLhNR3ncCn30b5ukatNx_O5cr2_JVgtcF9PuQKpnlhYzCOeidlqr5T0gdHcNJlhJNw5NdQdfeu_KLMh5_bjJ-P1R22DTV8bUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بندرعباس؛ امشب  @News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68913" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68912">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🇺🇸
منابع آمریکایی: ترامپ در حال بررسی امکان بازگشت به سطح حملات مشابه ابتدای جنگ است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68912" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68911">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=tnSkWIVbOVMvzKuKgsHh1E_Ve2tAGxCsTlf6bCplHgXzhOUnwYwivhSVW6gZbI6UxCPe-MK7_p_LrwDe7IdnhjPQknwxDfGLVvz-QGlTsRPhrspzvQ6BbAggj-yKXttekiOmsiSE_aP_N-iOglANzQE_u-S_P_cUeVsK3S1MoN5FFFCMvkngQcgpvtUMtyP9nq50Fu80Xs29ENgbNFi9d4X9Kwo6aNdFyhfBGN9n2MnUKEA4bTD9vihLCHN99M92f1vtkkdtkwu6C6SGqVN1HRVlhU32XKWiOR4oTHN5hwtmFmKInCArmUkO48MD21pV8YXN-ZtKX08GCLRNoJhmhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=tnSkWIVbOVMvzKuKgsHh1E_Ve2tAGxCsTlf6bCplHgXzhOUnwYwivhSVW6gZbI6UxCPe-MK7_p_LrwDe7IdnhjPQknwxDfGLVvz-QGlTsRPhrspzvQ6BbAggj-yKXttekiOmsiSE_aP_N-iOglANzQE_u-S_P_cUeVsK3S1MoN5FFFCMvkngQcgpvtUMtyP9nq50Fu80Xs29ENgbNFi9d4X9Kwo6aNdFyhfBGN9n2MnUKEA4bTD9vihLCHN99M92f1vtkkdtkwu6C6SGqVN1HRVlhU32XKWiOR4oTHN5hwtmFmKInCArmUkO48MD21pV8YXN-ZtKX08GCLRNoJhmhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بندرعباس؛ امشب
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68911" target="_blank">📅 03:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68910">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
دقایقی پیش صدای انفجارهایی در قشم امیدیه و اندیمشک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68910" target="_blank">📅 03:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68909">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=mjkltXe3honxR_yWplcnH6NwFGUzpbWVyyHzQrNHTsbG3SvRangsDA60Wr3F3lx9pnU7p85OFexRKwSrdYIGd84brmkgMMU2ua96RsPiYsc5z4g5ODJ7t2YxMRW22GJ3tvcJEsq5XfnKy9l7TzbRucdhKdYMuY3PSjWXkiLWgWLBIBydxQHDnnArFCGsTFSq0m0yH1dl_IgJYt_Vp-6GHG_UPpZ5XSWVBmcqQxPaw7lugN1-6rx7VH40f9SF64IUQt5_SYZPf8BKaccNT2yumy-LCtWb1QG39-oZTPJKxclOzrYTo-0NU2_T602e-7QKbvOqSpO3cqKEosBGmLM2AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=mjkltXe3honxR_yWplcnH6NwFGUzpbWVyyHzQrNHTsbG3SvRangsDA60Wr3F3lx9pnU7p85OFexRKwSrdYIGd84brmkgMMU2ua96RsPiYsc5z4g5ODJ7t2YxMRW22GJ3tvcJEsq5XfnKy9l7TzbRucdhKdYMuY3PSjWXkiLWgWLBIBydxQHDnnArFCGsTFSq0m0yH1dl_IgJYt_Vp-6GHG_UPpZ5XSWVBmcqQxPaw7lugN1-6rx7VH40f9SF64IUQt5_SYZPf8BKaccNT2yumy-LCtWb1QG39-oZTPJKxclOzrYTo-0NU2_T602e-7QKbvOqSpO3cqKEosBGmLM2AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68909" target="_blank">📅 03:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68908">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=oSgBNrui8FIRjXrG8FJeXezxOH50GzBy5PIIB61dWiMQukjzGE-2RhbWMJRvyJpGEkNA4i520WnIf-CRnwZ-zFSceue440HeicY7cbldr_O7EofH_F0fpbohAJy6xbto_N-YWCOOb3EkrZVvoXfk9ccjU-QBZzPcDI1X21CyWuZFi0xXvfE2rAdAG7KAGNH0sOf6RT-UrZZMuowjmtqvgNcN1QxI3lKl18jjPU4FwyXIG23NdN3Isz1yv0FJWpVNgOXcqTmglzAnA1Z67xkg0zc_5YcIUQ1JfJutrWhPWfYyDd8v8bOPWTn4Hb7YADFg6LqEWpmxW6omMQb9QjXspw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=oSgBNrui8FIRjXrG8FJeXezxOH50GzBy5PIIB61dWiMQukjzGE-2RhbWMJRvyJpGEkNA4i520WnIf-CRnwZ-zFSceue440HeicY7cbldr_O7EofH_F0fpbohAJy6xbto_N-YWCOOb3EkrZVvoXfk9ccjU-QBZzPcDI1X21CyWuZFi0xXvfE2rAdAG7KAGNH0sOf6RT-UrZZMuowjmtqvgNcN1QxI3lKl18jjPU4FwyXIG23NdN3Isz1yv0FJWpVNgOXcqTmglzAnA1Z67xkg0zc_5YcIUQ1JfJutrWhPWfYyDd8v8bOPWTn4Hb7YADFg6LqEWpmxW6omMQb9QjXspw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
لحظه وقوع انفجارها در تپه الله اکبردر بندرعباس، دقایقی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68908" target="_blank">📅 03:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68907">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEXLx7nOdJvt-vuczRfR9C12Oex_6QO9X2emy8RuW8DnqNNx46Qieb4EAe-mKA4fPysKfrofoIWhETeaNPoKACkazSo3-WtmWEp5jpzpC_l3AzZSFRocmVklCCeu_B0y2pfoKhrYwyKgQdKX31-CQ8JwZ0z6t5LAguMsKD9PQ15QcwAECR2AlFoQWO-wnmrdlMMdkuUe00CUemyoEoLykrR-UHM_i7lko78x0e7YwvAok29Ct6I40-8uqu1VfnK0ZUzlMOqSAJEfClk4WkjF-l40lLjlnuBo3hiedMXkTjqiwA__FbjFNCVw1QjcGGG-SOe954GWfCiCec9UvDyXYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68907" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68906">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی  @News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68906" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68905">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=TEC8FLBw43823XrMLr70Y81OCzWQ021AS5kgK5e0I0QNZrK3oERgUAmXA2ZwCHa6_RPwUy10uf9i0USN1fCkxaLGizSqp_8ALaoLPbtS3vhXdaJgQ8s65PS0A40Fm59-Jrn2-P3s6-FWfBX_uyuEOr49XEpvzKeEduZT9kenV_LXBlrTP5fbid-kKeaXFoaEThHslZTumy9ll6Q6Q2Kc52lEp2E9XWN9PVR2e7eBf0c06tTlh0q77N2wLIxoPOwF2czyOSiawgBRW-otD8SH01v4HUKnW-lm0X_gWI9kcmPCEKRg9DvJaPqaAYrfc_MQ6rr-rc-ZbIqEKGQIsWowOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=TEC8FLBw43823XrMLr70Y81OCzWQ021AS5kgK5e0I0QNZrK3oERgUAmXA2ZwCHa6_RPwUy10uf9i0USN1fCkxaLGizSqp_8ALaoLPbtS3vhXdaJgQ8s65PS0A40Fm59-Jrn2-P3s6-FWfBX_uyuEOr49XEpvzKeEduZT9kenV_LXBlrTP5fbid-kKeaXFoaEThHslZTumy9ll6Q6Q2Kc52lEp2E9XWN9PVR2e7eBf0c06tTlh0q77N2wLIxoPOwF2czyOSiawgBRW-otD8SH01v4HUKnW-lm0X_gWI9kcmPCEKRg9DvJaPqaAYrfc_MQ6rr-rc-ZbIqEKGQIsWowOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68905" target="_blank">📅 02:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68903">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=alsbEOQ3x71Z2KJh6BJIBgHBgiGFbZepgx_qNgtkVkL9l5HUTqJsDcoup5odUj4EV397ZlmlCLoDuL7PXn-8H_bFtxBGQrz7mGyzsG61MjyskuFKSYcHr0ua5U_iGLz9qz6kDa4vjYeHCbiJg1DX7tNAjgyFU1gsOAemR8WC6--FMeIogGY1vIJtQ4UhSqaTRxA0jvkCjv81CBPZTtXXWB0xg0iqezzwg-b04ttLkFk1AsB_Zrpm8Mm9EBKMRPXf_Yvs7-nXt9gDhJjPTbkSs6GDFPUKmiY7aip4eNy0vcQqj9xbrpHBLRI6WUfR2wo1i5Z9OHumzVMKBPxvb69H6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=alsbEOQ3x71Z2KJh6BJIBgHBgiGFbZepgx_qNgtkVkL9l5HUTqJsDcoup5odUj4EV397ZlmlCLoDuL7PXn-8H_bFtxBGQrz7mGyzsG61MjyskuFKSYcHr0ua5U_iGLz9qz6kDa4vjYeHCbiJg1DX7tNAjgyFU1gsOAemR8WC6--FMeIogGY1vIJtQ4UhSqaTRxA0jvkCjv81CBPZTtXXWB0xg0iqezzwg-b04ttLkFk1AsB_Zrpm8Mm9EBKMRPXf_Yvs7-nXt9gDhJjPTbkSs6GDFPUKmiY7aip4eNy0vcQqj9xbrpHBLRI6WUfR2wo1i5Z9OHumzVMKBPxvb69H6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68903" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68902">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKxY-AQ8EOPSZ8ckpTxrkZNiIvj3cS_9GCKP8UWnraix8DqUYtBl4fnt41R6K894eUIM54SNjCKc46jAmHksh6iG35CkAR04BRRcIKxBjbOGkNoe3nr_jgLE3okSpk8fzzfcJU1X9nnheRNWeZkD0aCCkJah84GoM6pTOgMmBUBADQZR346llcss7NAauS-e6w7-y9dvgJESRxr0AKfpWkm9756KwqTvTkt16Ni6MfgwEW9j4FiQwzYbH3JWsiSbO-BjQA3mwLyj4P3nCS1A0uE2DJeQY69MSpc75HdHAaKDAh2jVswIWzefUpvAGsH21JrILiwHTnCKQ9um6VqBOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی امروز ساعت ۶:۴۵ بعدازظهر (به وقت شرقی)، دور دیگری از حملات شبانه علیه اهداف نظامی ایران را آغاز کردند. این سیزدهمین شبِ پیاپیِ حملاتی است که با هدف پاسخگو کردن ایران و کاهش تهدیدات سپاه پاسداران انقلاب اسلامی علیه کشتیرانی تجاری انجام می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68902" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68901">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدیدی از حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68901" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68900">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
چندین انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68900" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68898">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=U_z6tgpBNmtdzEWQ7voEIn09JYdYjZ6gmgeyXsSxSC8lkW4X9w-u2Ho6OMX0u2uiwOEOePG0vZ8jg9B7UdOp9QZ_K0Nj9rhNdL08oPjV2ydv1P_iqeFlwoGOeYeP-nphdtqzfld7_ekCsvz_Eb8cqwbvWsXkl0XwxMx8xt1k1yOJEOSWzEO8ZhtAtypH3ufM77tfO4eAXZC7GrTy0iYlKD6L3VXvAkfOxTB4f1AmhC6iHX8Yq09PtceaCbcTS1rexYyLw762j1TEYysJjaQqxxpRKT9jf1knXY52bwVJWonmRTUh48JzCEM4kmYEZxHb2O7U8tSVHnKU-p84l20ruw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=U_z6tgpBNmtdzEWQ7voEIn09JYdYjZ6gmgeyXsSxSC8lkW4X9w-u2Ho6OMX0u2uiwOEOePG0vZ8jg9B7UdOp9QZ_K0Nj9rhNdL08oPjV2ydv1P_iqeFlwoGOeYeP-nphdtqzfld7_ekCsvz_Eb8cqwbvWsXkl0XwxMx8xt1k1yOJEOSWzEO8ZhtAtypH3ufM77tfO4eAXZC7GrTy0iYlKD6L3VXvAkfOxTB4f1AmhC6iHX8Yq09PtceaCbcTS1rexYyLw762j1TEYysJjaQqxxpRKT9jf1knXY52bwVJWonmRTUh48JzCEM4kmYEZxHb2O7U8tSVHnKU-p84l20ruw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران اهداف توسط ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68898" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68897">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=ZHtGK6YZeW9GZ0T7twIZODJfs4nJRO0b_k0m43gzOwZtRbKwufHszipE4icu_HbltQj8T9Y5_ofFIc6tL91tdqo6I2lv-pdImCdyPrtQIvSPz_olXdjg-IQC6VuA137BRqJ86BizD__rqrPKetl3N0O57bi0MkupntD9ivZaXeYhgoDoVRd_OSCPM17MyJtsipef4WWdfCT7ruSidAHPzlnvJfjmbX6muEqOkDiWm2_dhAO8I-xIfZWJH_0ZJKmD_by6Xa2Fbfk02MQvXPO_sEeeP56J5A2clkT5s9QrG2DpSDJS6iaVLvmvxsDYqGnLbUsXVDzpm4aSqqUPb4DK3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=ZHtGK6YZeW9GZ0T7twIZODJfs4nJRO0b_k0m43gzOwZtRbKwufHszipE4icu_HbltQj8T9Y5_ofFIc6tL91tdqo6I2lv-pdImCdyPrtQIvSPz_olXdjg-IQC6VuA137BRqJ86BizD__rqrPKetl3N0O57bi0MkupntD9ivZaXeYhgoDoVRd_OSCPM17MyJtsipef4WWdfCT7ruSidAHPzlnvJfjmbX6muEqOkDiWm2_dhAO8I-xIfZWJH_0ZJKmD_by6Xa2Fbfk02MQvXPO_sEeeP56J5A2clkT5s9QrG2DpSDJS6iaVLvmvxsDYqGnLbUsXVDzpm4aSqqUPb4DK3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین به اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68897" target="_blank">📅 02:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68896">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3266056eac.mp4?token=oViracWiltWCMVGV_K1HtyvobqCqVuZF5TUDtT697nX17xe3G_MsCkeh2bxlHOb1Qu7F0iA6yKrns5Dhdn64xbrM6CO6Qf56dEAjlgJ8MVFmCFibJOzda_9JK09VkiNhLXEhQ_Z0lPDiFkrS8JvrdBclmJzQTilJc3jigRJOyEUax6Iug1hjyzmNJOKtazqrUt15Uc6zNupsGrYL-ZB4DX6zo_sR1de5BbNS7C8vpoDywRbLTJBMZfkNoISlmCq21R0H8kAqn34HXCz0aioQWHzHbBNUw1iDIQUsa-gjxhaDsZc3qA34i0D5D2FdRXDm2RqAnYeond5P2tu9SclNbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3266056eac.mp4?token=oViracWiltWCMVGV_K1HtyvobqCqVuZF5TUDtT697nX17xe3G_MsCkeh2bxlHOb1Qu7F0iA6yKrns5Dhdn64xbrM6CO6Qf56dEAjlgJ8MVFmCFibJOzda_9JK09VkiNhLXEhQ_Z0lPDiFkrS8JvrdBclmJzQTilJc3jigRJOyEUax6Iug1hjyzmNJOKtazqrUt15Uc6zNupsGrYL-ZB4DX6zo_sR1de5BbNS7C8vpoDywRbLTJBMZfkNoISlmCq21R0H8kAqn34HXCz0aioQWHzHbBNUw1iDIQUsa-gjxhaDsZc3qA34i0D5D2FdRXDm2RqAnYeond5P2tu9SclNbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بمباران سنگین اهداف نظامی در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68896" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68895">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از بمباران سنگین در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68895" target="_blank">📅 02:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68894">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
فارس:
گزارش‌های اولیه از سقوط یک هواپیما در آسمان جزیرۀ قشم حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68894" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68893">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68893" target="_blank">📅 01:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68892">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نیویورک تایمز عملاً تبدیل شده به فارس و تسنیم
😐
آخ که چقد این چپ‌ها ولدزنا و حرومی هستن
#hjAly‌</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68892" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68891">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68891" target="_blank">📅 01:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68890">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUf3U6Ty8kML0li2hknS1QwreBx7LyGAqCfQVwtqmLsadCPrBXwzUMb6h-Vi0stnd5Ft0hVkgQVuzUNRU-nkqQ1IFdM25A26M3Om5Nim5GHqp54V70gTUImr6msMXKXzwhCVBNDB9oTWYYIZfNSxeDBrT1f7cN2wXo1_BwKpcfX_aDhVSfea0pEebL_Uc0WQ5q0Lry7JZDoc7YNp0frsmYRD7I7SSIPrpmXloVjnVcj1Dd4Pswtg6inmOnBZzx822eBBkcYtSdxQ_KqOHASwXPjuHyZYL9x9JYuLHPToZB2dfT_I4zEDi1tWwN6Ly4j4NYNPqhYMWdRPcmEms6XKLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:
لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد.
اگرچه ممکن است این خسارات بسیار سنگین باشد، اما با این حال، این اقدامی عادلانه و منصفانه است.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68890" target="_blank">📅 01:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68889">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=u8rrjrIr67vtYvxkWusjArVl_eQU0mRJ645u-zNfxlv9zAANvCTk8wFPcxIv5m1aJY6109FZUxqbXpGujhhPRPeZUCBav8s01yLY9r0evTsLMC_HJGyS641SEtEyII64uzAMrhCV8wqsLhnjYbr8pEIKSN5bZy4Od-0fKjMVn9gDWb89LZ52MgTyTcB--a4xKWKNq0iOMhimKstEnWWPWC41ToiiQ-2VNdWpM8RmjRXLganxOBMwqzeBgSFih7j9yTX4SGfndr5V6sbyKa5k3VEy__3_d1Mc5w8KsN5gG4gEvFNI2SyTQo_nWbz7S8zx7p_2Jfm7omYlHPveovwZGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=u8rrjrIr67vtYvxkWusjArVl_eQU0mRJ645u-zNfxlv9zAANvCTk8wFPcxIv5m1aJY6109FZUxqbXpGujhhPRPeZUCBav8s01yLY9r0evTsLMC_HJGyS641SEtEyII64uzAMrhCV8wqsLhnjYbr8pEIKSN5bZy4Od-0fKjMVn9gDWb89LZ52MgTyTcB--a4xKWKNq0iOMhimKstEnWWPWC41ToiiQ-2VNdWpM8RmjRXLganxOBMwqzeBgSFih7j9yTX4SGfndr5V6sbyKa5k3VEy__3_d1Mc5w8KsN5gG4gEvFNI2SyTQo_nWbz7S8zx7p_2Jfm7omYlHPveovwZGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
مقدار قابل توجهی از هواپیماهای باری نیروی هوایی ایالات متحده (مدل‌های C-17 و سایر هواپیماهای سنگین‌بار) امروز از اروپا به سمت خاورمیانه در حال پرواز هستند.
برای توافق دارن میان
😃
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68889" target="_blank">📅 00:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68888">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
دقایقی قبل دو فروند موشک در جریان حمله  آمریکا به محدوده روستای مسن در جزیره قشم اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68888" target="_blank">📅 00:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68887">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b133a06016.mp4?token=ihfHj9fhtcXAufPg6xbjMqI1hw6NCKEipG5BX2wSzLsio9hrFAecQp3lFl0GHaAR3qXlJZ0UZHHOh4oChy7HuHTgmOOUvpNLbONhtrg1Sb8Dnfvb6EYEWqSMZT_G7nIyF6o6GyWR4KgUv0mxM4AMHVLhK8u01smsUU9pnV9HcVgZKyuDSuLDAK2ps7mFfl6OwpEKRjKzbrtGog0kIR6f77cbiSPUM4orwU_vXx0GL6vzl4nxBlEU0reag7ith2yJDCEYbce0g_-b5I7EKDN1Q-zGG7WjEgUCoThmBJV0ObtXVcvH1eSQGKOfZM4kKztyGtToqaov4VOqhsTuX2bj14i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b133a06016.mp4?token=ihfHj9fhtcXAufPg6xbjMqI1hw6NCKEipG5BX2wSzLsio9hrFAecQp3lFl0GHaAR3qXlJZ0UZHHOh4oChy7HuHTgmOOUvpNLbONhtrg1Sb8Dnfvb6EYEWqSMZT_G7nIyF6o6GyWR4KgUv0mxM4AMHVLhK8u01smsUU9pnV9HcVgZKyuDSuLDAK2ps7mFfl6OwpEKRjKzbrtGog0kIR6f77cbiSPUM4orwU_vXx0GL6vzl4nxBlEU0reag7ith2yJDCEYbce0g_-b5I7EKDN1Q-zGG7WjEgUCoThmBJV0ObtXVcvH1eSQGKOfZM4kKztyGtToqaov4VOqhsTuX2bj14i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امشب تو میدان ازادی تهران
زیردریایی سپاه و سامانه‌ موشکی ذوالفقار بسیج
به نمایش گذاشتن
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68887" target="_blank">📅 23:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68886">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gde_XRbZtueBVyGHRLy_B4Ctc0kaxrjQBLXieDIo5V3wd8L-NPiuUNsZPGbUyYZ1So9ELeUAX4ch5CV5LGsMXgKf5A2xE0iU4ap8m8hbDFRJ20VVgzNWoNYFeGHJZxk81eAKa-fHwwS9KP-iyDDPgBiqeADyGTVmb9rEt3brfpX72e0lDJ4r8DKH2tM-8K4zClLzKw3yzIz9kttV8081GgOhp7YvZOGdn9kGD8LZ7OKVXqvhEj4nkTofuAXKzHS7i6jO_sSkdy1jmgMhG1gzOsc26ShExbZHPsZ8WHqS8jbbQWFRxy2fKJyBVcsTawxJGH-vNeLqmgxGcoED0Mvp_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک دیپلمات آلمانی در گفتگو با شبکه «فایتوکس» (Faytuks) می‌گوید کارکنان سفارت این کشور در ایران خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68886" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68885">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن  @News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68885" target="_blank">📅 22:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68884">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68884" target="_blank">📅 22:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68880">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dnFJoI_l8p5j7Oek2M-YM3BbfHEwwfa3h7EBVSRogD3lBCiaTewLD30SZPGnj-ZgvTESgLr5OcLX7RNQRTB6a4MRIQCHOc73fWukVd6d-u0ZiBaeBw0k4ZM6ni1sLzAYZeHGlFize--uxPeNhreKnnNj5me7axH-2XeNuahbZfR3Vw2jHXPWLDJstPiWzLrGAl06ccsozZFCBdjl626szxUtFf6CqvAIWW7Ogl9miSSMVp6KGQi7LIlB71Id1HPEtHsfjKhjxa_HuAGpJjOC7MDWrXITdqPPpbBtDYk-3R76hkyjlz7h1x9CTq60HaIqjdPBJBk0ssW0r5LEdURxZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e5OV3gdEnnu03ADoy66LAdirfi3SiyFimljLq-EgzA-bu4ijqCvn5-VSbqJO0DUZfrQKW-tT2Ydx20LP4cZlAd6fKks0tQkzPXoQchhiXSlQ8oKXcCQDPkfmmEoWkWSD9iEVx4w4rPz65e4eSCgyy9VFVZz3lY5bLKgfseLuLq1vxtpJslQYnduPqFdgcOHp71DjRWcISGWbciQyKV2Kh34oOfWeyGHANwWrpU1l-EB0nc9JNX_2cOKXCLdRZA0WdxUQrz-RipgDzB0z6cGdIkJOjL5MMjkXxh3al6etiHRUgBCQG7QXYGKYfnjnfycv9XvXGXZ5Ru2LYC4eLIQvAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a671667b4f.mp4?token=qcpz9GepJW-4M2mPXIXVRJncbBYkIoDLxMy-rlJUIjJc062zdh4znp1nSE9szw2rp5FXbMWVcrvbmE1ZaXQNuFikYbNJpUISyhO-kqrd4QzmBkisDHI3YyZqCFju7mwkWARiIuMsrD4c7M2sHvExua9Tug5HPtC6Frk37pYGq5yILWIIYZkferZedjdMYFaaf-GJ5UhGF_vh4FOCyLL1lNB_ZENufw9sh9238-kmQLCzQ69dLYSmdfr5s0fb06e7BvVwqEK1JLGlMitt6aqZA_AejH8hSFIXxk9kjhO3NXbL-0EPccHncA6lC2TVX3iit0w5K_qy2qmDVMIsMHdC6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a671667b4f.mp4?token=qcpz9GepJW-4M2mPXIXVRJncbBYkIoDLxMy-rlJUIjJc062zdh4znp1nSE9szw2rp5FXbMWVcrvbmE1ZaXQNuFikYbNJpUISyhO-kqrd4QzmBkisDHI3YyZqCFju7mwkWARiIuMsrD4c7M2sHvExua9Tug5HPtC6Frk37pYGq5yILWIIYZkferZedjdMYFaaf-GJ5UhGF_vh4FOCyLL1lNB_ZENufw9sh9238-kmQLCzQ69dLYSmdfr5s0fb06e7BvVwqEK1JLGlMitt6aqZA_AejH8hSFIXxk9kjhO3NXbL-0EPccHncA6lC2TVX3iit0w5K_qy2qmDVMIsMHdC6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای تهاجمی اوکراین در یکی از بزرگترین حملات از لحاظ حجم آتش شرکت بزرگ تجارت الکترونیک روسیه، Wildberries، را هدف قرار دادند.
این تأسیسات که در شهر کراسنودار واقع شده، به‌طور کامل در آتش فرو رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68880" target="_blank">📅 22:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68879">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇺🇸
ترامپ:
کیرم
تو هرچی کمونیسته
#hjAly‌</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68879" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68878">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند  @News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68878" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68877">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68877" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68876">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">همین الانم ترامپ داره حرف می‌زنه
#hjAly‌</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68876" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68875">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اگه امروز این قطعنامه رای میاورد، ترامپ مجبور بود جنگ رو تموم کنه، یا اینکه قطعنامه رو وتو کنه! #hjAly‌</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68875" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68874">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.  اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68874" target="_blank">📅 22:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68873">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/351349ff2d.mp4?token=jdZ3Fpu9enufy3eW3ke2LXKc8DIG4cCOOXFfnwdNURCLu1CCa5jsNVM1SO-64oa5nhyhQJDVyE4atDN9qqWgjOybRbIt5YuYuP1K8usSANpyhwgl-Izb5HCperbIDNgNWpA_iR58I5ud6K8tDWvRQoPSfYKtohT_RYOssFQem02_6WiowpCkmTgyuyYtXMssyb-XYK0fQ1PtaQ-sN8wpKGDIelujIYjI_VP6egrw_3TR4RugPJ7UbGgFIH52EpidVr3a5Bz5El2YR02PmuozzXDLseLtKuSpIzNHR3Mzy6bm-dfMSCjWnKtlAJQxsSw5o8L-YsMFULY8qX2H2FXFhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/351349ff2d.mp4?token=jdZ3Fpu9enufy3eW3ke2LXKc8DIG4cCOOXFfnwdNURCLu1CCa5jsNVM1SO-64oa5nhyhQJDVyE4atDN9qqWgjOybRbIt5YuYuP1K8usSANpyhwgl-Izb5HCperbIDNgNWpA_iR58I5ud6K8tDWvRQoPSfYKtohT_RYOssFQem02_6WiowpCkmTgyuyYtXMssyb-XYK0fQ1PtaQ-sN8wpKGDIelujIYjI_VP6egrw_3TR4RugPJ7UbGgFIH52EpidVr3a5Bz5El2YR02PmuozzXDLseLtKuSpIzNHR3Mzy6bm-dfMSCjWnKtlAJQxsSw5o8L-YsMFULY8qX2H2FXFhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.
اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول از کنگره مجوز می‌گرفت. اما با رد شدنش، چنین محدودیتی اعمال نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68873" target="_blank">📅 22:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68871">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0GqQMlFlOGz6l1W56jjRhNK-LIgAsgTM3ntUiZwmAC5683skBwlHjc0DQ7ZK4A6UeRMy4Fje4TgEXGwMjXpWvhid2OOIipGi9yfpbiZEvTAGJScmg5GeQH6E053Vb2C4lu4Q1lMeUn8J1DXhPbqX1c3uQ95IfQB94uNnYiQLb8bByJ6nyRFxkod1o8qvuvOhjEMwwJdUbV0th5YpHfVWDWubTh7sqvUOxllfGJmsipyuLdG5g10ZBaZsZypSBwO-RuVW3aO9xrsqTen9d9WXyn61dFjhFbdQjX1t1_889vuhiKMZ8ozKS-tVCGLncwvaFzxwpliB7G5IdH_7Pp2Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca0071632.mp4?token=nEzuhunejqpYrBApIpimTp6Jl13atjr8J7W7XcMvyMlOUKI6TMfKGHtTYV8x1xRFWUik2ZX4LatP4NISlhwtTWmAVX15g7TPpFQifjQ39EMAxY7xLgh0umFAMTYwhkiozolfZbagl9CzLspTR5WDHeMVQ7v-QqIPxuAq5Bdnd4de_Fz9pwG79Vym_kOkinPMGsxKfxvU_nVsLWHl3jWV_nemFLRic2ohcKN5rZWdd-bphiDuPvU8h2R4uhto3LM1FbpR1vYiY6j3IEdszgVfchnueBeLivF5jTj_jCWUoLEESiB6Jyo4-b1_gRD4G-5yDgWXvKX7F5mYjzAmNv5c0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca0071632.mp4?token=nEzuhunejqpYrBApIpimTp6Jl13atjr8J7W7XcMvyMlOUKI6TMfKGHtTYV8x1xRFWUik2ZX4LatP4NISlhwtTWmAVX15g7TPpFQifjQ39EMAxY7xLgh0umFAMTYwhkiozolfZbagl9CzLspTR5WDHeMVQ7v-QqIPxuAq5Bdnd4de_Fz9pwG79Vym_kOkinPMGsxKfxvU_nVsLWHl3jWV_nemFLRic2ohcKN5rZWdd-bphiDuPvU8h2R4uhto3LM1FbpR1vYiY6j3IEdszgVfchnueBeLivF5jTj_jCWUoLEESiB6Jyo4-b1_gRD4G-5yDgWXvKX7F5mYjzAmNv5c0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ساعاتی قبل سپاه پاسداران یک نیروگاه برق در کویت را هدف حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68871" target="_blank">📅 21:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68870">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=uOZVeg384534zkSDbleNrsqksudcf3_e62sDs43B1EbVNVDcFj7X9O6JxgWeeuhvBsSQvtOsewNSydV9GLfUXbAniX55kc6YPypcXfC7UReqZgwIA_wAcDvXve-GS49pA86kgMgSx9t41mI--XgveLt5Q0Zw-xIC7XXwqClgOyYkKhcpVUkwGGP9ZCHN7st5J1JY6cOU-F8y7WKnalUtIg8M741PcIgZ_rFFI2R0rTVbTB_KgM9wIV5Pf9iGSKbdivKzTasFH1Q_Zci7zub_sfEBjCdKHJJo0jhPKOt-tIq1Aq-7_7qwyDmEL7q2OqrkF3kV6cRbozIg3ft8-Sbm4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=uOZVeg384534zkSDbleNrsqksudcf3_e62sDs43B1EbVNVDcFj7X9O6JxgWeeuhvBsSQvtOsewNSydV9GLfUXbAniX55kc6YPypcXfC7UReqZgwIA_wAcDvXve-GS49pA86kgMgSx9t41mI--XgveLt5Q0Zw-xIC7XXwqClgOyYkKhcpVUkwGGP9ZCHN7st5J1JY6cOU-F8y7WKnalUtIg8M741PcIgZ_rFFI2R0rTVbTB_KgM9wIV5Pf9iGSKbdivKzTasFH1Q_Zci7zub_sfEBjCdKHJJo0jhPKOt-tIq1Aq-7_7qwyDmEL7q2OqrkF3kV6cRbozIg3ft8-Sbm4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب یه دلقکی اینجوری پشت ترامپ اداشو درمیاورد که حسابی وایرال شده
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68870" target="_blank">📅 20:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68869">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=YmQiEMn9nj-X2AOAahnoBRPzCtV6lBVA5xa727PY8N5ghM709Kr6_vFXdsqYyBI9_1h0tJQ5iztdv20-rGhUIOPedX3nNCOBK6Jz5OdL6LofQKXonNzTLRzLEJoVrElsjZTEupKOiuJOVdGpR0M_VSA97t-gPD8e7ICEjbJ0ZiIqOMXPb7ZC_doaNCDw7or-KXMAzH3j9Jch2sPkuuQkQXoVoHX5HnahBn6EJGoOiH6vbRYECPnKpVCMDTy52Ws3e9ZfM9GigsRm0B_hwBjjkGEzkUuLUGp3lvRsiXtdaEBXO8a7MRYWPQ9GqyRnsFiRWQpnp2TwwIRMdkN6Fbs__Fsi6qk6NhSbDNwXguGnsHg0Vt3At4rtivV9HTmHo3aDhduWRoTKv9cgDpkdP2bOixhKu5Q-lOdUj5MpNmpUeI4dUAFrK1NihVndSg5Xfm-IcZog-OaDH9-dGEfJpyMrCvpkqCoIVWZihopmESFtZnPCLgngd4VKCpUw7i1gYSAWo4XgWyOj5ZEvUXEr0PTuos_cH6j9Ok8AHDqTMp5y0gW4WDKwHaRyOwFwiJVv_brAKrSxAl2Uv61TLiJmplht4XzrbAXGuMOtqs58YAtEDd8j79DpHTM114Xx7pye1OpGy7msKYvMH7Uex_XRoD0UP2B4D0NyP4dew_5ybQjIxZk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=YmQiEMn9nj-X2AOAahnoBRPzCtV6lBVA5xa727PY8N5ghM709Kr6_vFXdsqYyBI9_1h0tJQ5iztdv20-rGhUIOPedX3nNCOBK6Jz5OdL6LofQKXonNzTLRzLEJoVrElsjZTEupKOiuJOVdGpR0M_VSA97t-gPD8e7ICEjbJ0ZiIqOMXPb7ZC_doaNCDw7or-KXMAzH3j9Jch2sPkuuQkQXoVoHX5HnahBn6EJGoOiH6vbRYECPnKpVCMDTy52Ws3e9ZfM9GigsRm0B_hwBjjkGEzkUuLUGp3lvRsiXtdaEBXO8a7MRYWPQ9GqyRnsFiRWQpnp2TwwIRMdkN6Fbs__Fsi6qk6NhSbDNwXguGnsHg0Vt3At4rtivV9HTmHo3aDhduWRoTKv9cgDpkdP2bOixhKu5Q-lOdUj5MpNmpUeI4dUAFrK1NihVndSg5Xfm-IcZog-OaDH9-dGEfJpyMrCvpkqCoIVWZihopmESFtZnPCLgngd4VKCpUw7i1gYSAWo4XgWyOj5ZEvUXEr0PTuos_cH6j9Ok8AHDqTMp5y0gW4WDKwHaRyOwFwiJVv_brAKrSxAl2Uv61TLiJmplht4XzrbAXGuMOtqs58YAtEDd8j79DpHTM114Xx7pye1OpGy7msKYvMH7Uex_XRoD0UP2B4D0NyP4dew_5ybQjIxZk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فاکس‌نیوز در حال بررسی فهرستی از اهداف زیرساختی احتمالی در ایران است که ممکن است مورد حمله ایالات متحده قرار گیرند؛ اینکه کدام نیروگاه‌ها ممکن است هدف قرار داده شوند؟
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68869" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68868">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9mCA4YyWX7xix8jqWMQEUU9Kgbe6CqreqfLSJrWFVp5pBLBfTEotcbV9EL9BP_zCUft4iOPLHn6rwdO9QqtZelW1dQdVV2UZcGfELXNsqIq_8Y7KAuwCYAW46tNGqL_tRW4SVo7DYmcS2SClNn9WsH2NSotDKtfpDq-vLDS47X_D9Ogc4RhYIPwj_fC_ClaDUHtRiABYs0VH0Hj7G8CI-zV1qJPPIkyfRb2hAaAVKrfgRfZ-RQ82kvRUg9MAq5yZtSTKExWzfm1IzEeeZ-Kg-Qq3CMX-ROl0SkuuTy7qOvAlgNmeHtHOfYiskkawdBZHWNmhY6vbnKLcsM4RRqjWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68868" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68867">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0jZ4mEQvnu3uURoU-UiSHdnP2QCcCPiZHR81c9DMNJsfCK0BkgncufFNvq6eNBoLVWQnZ2YwjovecOeI6u7YYmrkSf7c6ZckCxve5DoLT6mw7wUC3kunLPId-VgA6RMdVFNwhHbO0PpTXBWPEpn81WvVxPTRnukTMT1pn4XLgzzDxsjO5E0EZffuxKXThrTW6cAqsD6BMMU85VD01Gi25cDgRIP1DmbOMFEY2whD7AWVtEpiVOmtPZ6fVCgNQ8nCuxO6Kr4NLtCALVRzK0ybw75IYOlgAFOzDnO_MVn9fcXmAbCHSbAOtJl9UOVrRzoWVZKQ1M1ZR1mu2Xr92nTsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
آنها می‌خواستند ایران را تنبیه کنند. در عوض، خودشان را با نفت سه رقمی تنبیه کردند.
استراتژی ۱۰/۱۰
👏
👏
👏
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68867" target="_blank">📅 19:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68866">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=rYqjA6YJbv9aqBb9H9ZJ0QHhMKfwkZ5mg8URgGFSUY9MEzOERAz9SJRTmxILLfMC-0Vw6hq_59HfgsKTfOlvoyX9KGE5GYGnUaXSeHm9yLszNVTwSzURRWa9HA_94FyOcYfnRBPHBTk6wM53rtdGu0s7G6UdD3bjQLNxmeaEIqfaRRUKfbrpSjAlWdmJ6GOPU1gdC_pCd3K9-2SL6RiowwzIQGW6yrZxRJloULD6JThs6tC1AQfn39HLFAiGs1EpxRXQa3XCA5ncyhgJ9oIjnkRRjJtrmrB7HtIARQoCFhBbZD3LtxiIlOAospWA7yCp1Wi4DNaq77wSWdDIakIUZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=rYqjA6YJbv9aqBb9H9ZJ0QHhMKfwkZ5mg8URgGFSUY9MEzOERAz9SJRTmxILLfMC-0Vw6hq_59HfgsKTfOlvoyX9KGE5GYGnUaXSeHm9yLszNVTwSzURRWa9HA_94FyOcYfnRBPHBTk6wM53rtdGu0s7G6UdD3bjQLNxmeaEIqfaRRUKfbrpSjAlWdmJ6GOPU1gdC_pCd3K9-2SL6RiowwzIQGW6yrZxRJloULD6JThs6tC1AQfn39HLFAiGs1EpxRXQa3XCA5ncyhgJ9oIjnkRRjJtrmrB7HtIARQoCFhBbZD3LtxiIlOAospWA7yCp1Wi4DNaq77wSWdDIakIUZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العدید هم که تخلیه شده، بنظرم خودمون رو آماده کنیم... #hjAly‌</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68866" target="_blank">📅 19:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68865">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQcxRm0k6tnzhGWKTfDPYs0bHCtJHscOzpG_7KeaVUNz1ND3qeVcAUjTaDDeFgpd8nQHzk-1kCpQtSbjDLQ0pfT97ki0QY8bp3TuAiWyC8876FVIoUIpjsKJSxT77ncPQ-TQ0cUGHjxZzS2fPJgmik1ePNt4QOvSmzNyUdj1dHYtLmDebj31k25fztk08PH0SuWiJ7Jj1vuOpmrNPIYIwH6yNQ6Kx1vL57Pl2NPfl2p6mWf65KwEVB9chtd6L3rbDZUBq5pEqBcko25rxew2Pvn81o9VJK1Byu9tdRm2MxjSdxI99dldlNOqcgFWXucmjE8bFyEkZMI_uEzg2md2XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین نشونه های نزدیک بودن حمله، تخلیه پایگاه هاست</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68865" target="_blank">📅 19:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68864">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ همچنین گفت:  همه چیز برای این حمله آماده است. اگر از اسرائیل بخواهم ظرف دو دقیقه به ما ملحق میشود اما ما به هیچکس نیاز نداریم.  @News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68864" target="_blank">📅 19:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68863">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری؛پرزیدنت ترامپ به کانال 12 اسرائیل:   من در حال بررسی یک حمله گسترده هستم - بزرگتر از هر چیزی که قبلاً اتفاق افتاده است. من به تصمیم گیری نزدیک هستم.   @News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68863" target="_blank">📅 19:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68862">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zqyh8FHdDgjDKrAW_mCgH3XBXByNYZ9a9wovT28douOdowNR-5FZBRG35I0r0ZzZH7-ByMmPqYP6WezkJlzMYCNLqDgbLr_RvKn3jL43LJU40r0xQOxTJIls-O3ndUdLe1aFsnE_scdUJsO_bi8UdGOiipl7jREjsfVkB4nSkFQYz7ueAeLh0_LREBOSWj-kgm-dK1WrQ-gXRLJ7T7IGe0-UVGJjM5UBW3WzqeK6QoftpEnMCciAr7szRCDQMGpd52LrkghSF8yPY1vY4EFn6BxlnOzkAwgitNLZ-sRZcb3E0GsdlGxpj6z0p235ZbMLKSuKyPnMY7UU_Cpm8-3SuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری
؛پرزیدنت ترامپ به کانال 12 اسرائیل:
من در حال بررسی یک حمله گسترده هستم - بزرگتر از هر چیزی که قبلاً اتفاق افتاده است. من به تصمیم گیری نزدیک هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68862" target="_blank">📅 19:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68861">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a86f5d96ba.mp4?token=BJ8MhonxRlsfK9nDhvjbHW6JqGCQT8SoPVT80sVhjVBcXYf1PW7JbPnUcsFDXSXDEMCTbEsPik67RWM2trRpLZWvJmUTaRhLDNHdOhojnjoIeRg3HrSJ_E5OYVP2LtJMOZVcktG8zBmTU7T4OFvpL-Q38Q8jOsneg4bRigNio4NtvU_-k6iii6TVTg6eteqP1iW06FfOQ0GipD5M2yeTqimaeH00RLCMqz_qAo4mxXgst4qwZ4RWmrxs3JhM9j9NUwL4xPPRAZB7Nwk0gCqrU9xUsdx1o4Ec1CFv7FhO4PS0RmbrAwITEoYQyWKe5uQ2NMCKp0EJ4lKj_1JpEOWmVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a86f5d96ba.mp4?token=BJ8MhonxRlsfK9nDhvjbHW6JqGCQT8SoPVT80sVhjVBcXYf1PW7JbPnUcsFDXSXDEMCTbEsPik67RWM2trRpLZWvJmUTaRhLDNHdOhojnjoIeRg3HrSJ_E5OYVP2LtJMOZVcktG8zBmTU7T4OFvpL-Q38Q8jOsneg4bRigNio4NtvU_-k6iii6TVTg6eteqP1iW06FfOQ0GipD5M2yeTqimaeH00RLCMqz_qAo4mxXgst4qwZ4RWmrxs3JhM9j9NUwL4xPPRAZB7Nwk0gCqrU9xUsdx1o4Ec1CFv7FhO4PS0RmbrAwITEoYQyWKe5uQ2NMCKp0EJ4lKj_1JpEOWmVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
من بلافاصله پس از انتخابات به دیدار ترامپ رفتم و با هفت اسلاید بزرگ به آنجا رفتم.
اسلاید اول، اسلاید دوم، اسلاید سوم، اسلاید چهارم. "این کاری است که ما انجام خواهیم داد."
نه اینکه بپرسیم "آیا به ما اجازه می‌دهید یا نه؟" بلکه من به او گفتم: "این کاری است که ما انجام خواهیم داد." و ما به اسلاید آخر رسیدیم و من گفتم: "این پیشنهادی است که به شما ارائه می‌دهم."
شما بمب‌افکن‌های B-2 دارید – این بمب‌افکن‌های بسیار بزرگ. یک مکان به نام فوردو وجود دارد. اگر لازم باشد، ما خودمان نیز علیه آن اقدام خواهیم کرد. اما بسیار موثرتر است اگر شما بیایید و به سادگی بمب‌های سنگین خود را آنجا بیندازید.
او گوش داد و در نهایت موافقت کرد. من بسیار خوشحال بودم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68861" target="_blank">📅 18:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68860">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3008b12665.mp4?token=J5hTbXpBl6JIJzPZ8-Gg8IZIBA_3zfGI57FwUOdeimI3QtQNKR1XlrB70ZXV0--7mTD7iSNQ8ojqx-wqPRpZDmgkoybZ8aiTYdNQBaUU5BDPzWEbm69BKBlXEow5sGuU_JNPUZeHV5-GcgzBjxA7hWzNhHAvQV9UYxNFvFYpjGXj79u9tJmnLCm1OevRQonVQlHwNp-qGubNnynAXoxkgYTCAGVioXp42TrHM3EiM5tS3cmFzlrIMWGH-mUK0aJfFwL65cL9iz7vUkf6KlOVwhxZyCT1JRhQ_V4JYGBPARNxqWIjCdLdu9cUc8abqzokeVtjudW1qEcDfkJFVza72Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3008b12665.mp4?token=J5hTbXpBl6JIJzPZ8-Gg8IZIBA_3zfGI57FwUOdeimI3QtQNKR1XlrB70ZXV0--7mTD7iSNQ8ojqx-wqPRpZDmgkoybZ8aiTYdNQBaUU5BDPzWEbm69BKBlXEow5sGuU_JNPUZeHV5-GcgzBjxA7hWzNhHAvQV9UYxNFvFYpjGXj79u9tJmnLCm1OevRQonVQlHwNp-qGubNnynAXoxkgYTCAGVioXp42TrHM3EiM5tS3cmFzlrIMWGH-mUK0aJfFwL65cL9iz7vUkf6KlOVwhxZyCT1JRhQ_V4JYGBPARNxqWIjCdLdu9cUc8abqzokeVtjudW1qEcDfkJFVza72Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری:
الان تو دنیا کدوم کشور با ما دوسته کدومشون دوسته بجز مردمشون؟
⏺
ثابتی:
اونام دولت هاشون مثل حسن روحانی تفکراتشون امریکاییه
⏺
شهریاری:
توهین نکن حسن روحانی امریکایی نیست بعدم تو در حدی نیستی بخواد بخاطر این حرفت ازت شکایت کنه اگه تفکرات روحانی رو امریکایی میدونی یعنی تفکرات 80 درصد مردم امریکاییه..
⏺
ثابتی:
کی گفته؟
⏺
شهریاری:
کی گفته؟ اگه جرات دارین رفراندوم برگزار کنین تا مردم بگن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68860" target="_blank">📅 18:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68859">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🇮🇷
هشدار سپاه پاسداران به انگلیس: بیش از این پروندهٔ خود را سنگین نکنید!
به رژیم پادشاهی انگلیس که عامل اصلی بدبختی‌های مردم منطقهٔ ما بوده و سوابق سیاه تجزیهٔ کشورهای اسلامی، کشتارهای گسترده در این کشورها، تحمیل دولت‌های استبدادی و بدتر از همه سازماندهی هدایت عملیات اشغال فلسطین و تشکیل نکبت اسرائیل را در پرونده خود دارد و بیشترین مشارکت را در تجاوزات آمریکا و رژیم صهیونیستی علیه ایران داشته، هشدار می‌دهیم که بیش از این پروندهٔ خود را سنگین نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68859" target="_blank">📅 18:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68858">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o04mzUPa2QsWXNGJoU0uALXb0CkeMyJN5T3rscr97c_72YcPxTU8a2mPRmcldCKSWUT3oczXLexSNZE40ayCTzK-9UcOeLZHR4ejoOkNhAU_0veRCKvPoD9lvGgR8ssVbnpioteNVB8nLbIu3SHvxKwQSBuXhEZfQ2yKvZjWbblq_RIm6W82nCfwb9G1K8iLsQQ2zhzc9do-BDi5pOJHnBYhunJOrwIimluJtEXOIWZy1REDZ5lmy1O1_Sdconpnw6kZQqDJzM7O2QCniZNOIdlI77R0LDh0K2idXGAk8d56w09mqmLVfUoIDzdIxtK6UdghQ25ZWcBK8h0KdMoRZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
نفت برنت بعد از تقريبا دو ماه، مجددا 100$ رو رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68858" target="_blank">📅 17:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68857">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STfU_Txn-YOBR_y0-FSR6zjokWQOCBXM7mZ91RxDZuzHTTXve8nHr2i_lxGxPl3-0uNjxjkrMs7sezSoFHXyYflV5zcCQV5FPQPPrwjdCdk--A_FclBqxslbrP8dPl6zfanPRjM-JuSFQWZ9u6CtzrI7oSr4Mzic9zPu6eCdU6gBvrcz8LGHWfM-KgzMIyfo2uA1Ffo4Gi28eANdKFxm45nOQbodCpaB-_mcdM-SaDfsaMpXdPqGpm8_fnzAdvnYYUg1JbMPA2uFsPhJfz_ppjQvuFBAr2-fqXgh-caD-pyCEAGYLcb3PTh50Kk4EATt_5U01adMGYVzgp2PJxSRgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آکسیوس:آمریکا هم‌زمان با تشدید حملات علیه ایران، بمب‌افکن B-1 را مستقر می‌کند.
مقامات آمریکایی اعلام کردند که ارتش ایالات متحده روز سه‌شنبه از یک بمب‌افکن دوربرد «بی-۱» برای حمله به اهداف سپاه پاسداران انقلاب اسلامی در ایران استفاده کرد.این نخستین باری بود که ایالات متحده از زمان ازسرگیری درگیری‌ها با ایران در ۱۲ روز پیش، مأموریتی با استفاده از بمب‌افکن «بی-۱» (B-1) انجام می‌داد.
استفاده از بمب‌افکن‌های «بی-۱» — که قادر به حمل ۲۴ بمب ۲۰۰۰ پوندی یا ده‌ها موشک کروز هستند — نشان‌دهنده تشدید و گسترش قابل‌توجه عملیات نظامی ایالات متحده بود.
هواپیمای «بی-۱» (B-1) می‌تواند در ارتفاع پایین با سرعتی فراتر از سرعت صوت پرواز کند و در عین حال، سنگین‌ترین محموله بمب را در میان انواع هواپیماهای بمب‌افکن حمل نماید.
در بحبوحه تداوم تقویت قوای نظامی آمریکا در منطقه، رئیس‌جمهور ترامپ همچنان بازگشت به عملیات‌های رزمی گسترده علیه ایران را مد نظر دارد. مقامات آمریکایی و اسرائیلی می‌گویند این اتفاق ممکن است ظرف چند روز رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68857" target="_blank">📅 17:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68856">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d380ae3e6f.mp4?token=R7rtbIQ2aC_3OmbjQxxhFw1BH8aValuwdz2-0nmXIugFy5wIDgXH_RyqRrsWg-Zc4-ItfT77JgIpxH-6MHlgU3icVo0zmgfXaJw_TkmtrAq0ICC5tLLf5g7yxzfJ1I7algqTrUYpCHx03rC9eW8Bn7kDC3143L6wL6XYMfl0lI8sWFaM3kxBcTPeM_MAnCK3cI8Nu9jRzzN4hpLNZ4t-YUvGU0WNds0oBqM1INF5V9SYlgBzRAoFEM7MFoGgOZhmVwv1Di-BwiKyjQccUn5ZDUCL-bgP6vo0dY7ZphulOBvZNvcft3UMvlz8EMOm8HvkzGSOsuGJRSNi3y00faD4sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d380ae3e6f.mp4?token=R7rtbIQ2aC_3OmbjQxxhFw1BH8aValuwdz2-0nmXIugFy5wIDgXH_RyqRrsWg-Zc4-ItfT77JgIpxH-6MHlgU3icVo0zmgfXaJw_TkmtrAq0ICC5tLLf5g7yxzfJ1I7algqTrUYpCHx03rC9eW8Bn7kDC3143L6wL6XYMfl0lI8sWFaM3kxBcTPeM_MAnCK3cI8Nu9jRzzN4hpLNZ4t-YUvGU0WNds0oBqM1INF5V9SYlgBzRAoFEM7MFoGgOZhmVwv1Di-BwiKyjQccUn5ZDUCL-bgP6vo0dY7ZphulOBvZNvcft3UMvlz8EMOm8HvkzGSOsuGJRSNi3y00faD4sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پاره کردن امضای ترامپ هنگام شلیک پهپاد به سمت پایگاه های امریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68856" target="_blank">📅 16:31 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
