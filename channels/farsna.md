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
<img src="https://cdn4.telesco.pe/file/C6txvn9JkJnSBQm7zw2oyDdriv7RnqhI4NJJF7OctIE5w0hLwzjNSnM4-vGp-g2_cn-K5YX2cG-pSb_3H6g6BUx0jjtAM904zGX_V9b2zljUqEnkvbriRP8lPd3-oHja_iGeS_FUX51j1UYSbTLUjV5_lIvIs08DfcAej4btwslyj6QiJv8JYnIZmc-WPAN2quJ78aFwo2dLFof2cM9aLE8A0EPIxnPNAJGHzLAqk9cM5NIJgqO3GJM340h86q1f4jc_L0vzJ9-6Z5WRj3krroZ8wBYOaeB5k7qYZPmfaVva224aGUNbkbNcIFF26ZMVQ5S59wG7NouV33HGZGzxAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 23:49:58</div>
<hr>

<div class="tg-post" id="msg-447705">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/907de65e2e.mp4?token=NNpEsqe-p5dBhh86cWQ5TakMISP_0Z43fJj-x3q5N5xhMrUmLaeNz6fmclIUe2uQfMZ67hSUFtY2ITqtnubic6Lrv3LrwFcHtrhet6WKS5dCpsP4msH0tGLJB8ZE4dW-gr9g8BWEYWs0W8xooRfnw3HIBoYz7OGYSBPCIfvs9jRqruJ_-uXLgKVOFjqKaWzBaKfKLZsLbK8G4lOJmw3eVoYIjLqgJASq-srTqV5Un5qUaj_ebSmd7OSFNbOqWT_ufn9yKquXup3TyX-ENvNjc0M-HPuXpmlaRcVTmApdBrS8OtuojijQ1gGVkS0xGCuLU0moesMWoPxJIBAoMqkc_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/907de65e2e.mp4?token=NNpEsqe-p5dBhh86cWQ5TakMISP_0Z43fJj-x3q5N5xhMrUmLaeNz6fmclIUe2uQfMZ67hSUFtY2ITqtnubic6Lrv3LrwFcHtrhet6WKS5dCpsP4msH0tGLJB8ZE4dW-gr9g8BWEYWs0W8xooRfnw3HIBoYz7OGYSBPCIfvs9jRqruJ_-uXLgKVOFjqKaWzBaKfKLZsLbK8G4lOJmw3eVoYIjLqgJASq-srTqV5Un5qUaj_ebSmd7OSFNbOqWT_ufn9yKquXup3TyX-ENvNjc0M-HPuXpmlaRcVTmApdBrS8OtuojijQ1gGVkS0xGCuLU0moesMWoPxJIBAoMqkc_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیگر در امان نیستی؛ حتی در خواب‌هایت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/farsna/447705" target="_blank">📅 23:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447704">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b07596c0a.mp4?token=MyyDIJ50uQVRzDY5ZcOL8ws2EGQNdhQUgdeBfw2FNwRvFnlU3Vx38QXhh-KDfiL_3XQZyTCora2URVcJ5p1qA-8-xZQ-gqOKpkqzQcNmDr8M8VycBWa4JhjxRq8a4jVbD4toxq0E9o325E0gPpIMY0Lows8jtHcTTbVU3PFzVqzixB2hX4C5gG3yM1_UG51vSceJci1BkZWZa-umSfQZOVj06pHEfjQ2rITT7yVYZtky7REcVAn-NaXPPgJsRiAO0SfgVHiWvSycmOIDGM72LVynB8iCC0lkEYRN0zRVnEWZWxXVKa1JcWjWmDSXw1j5Iemr0txO2JJUhNz668sGkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b07596c0a.mp4?token=MyyDIJ50uQVRzDY5ZcOL8ws2EGQNdhQUgdeBfw2FNwRvFnlU3Vx38QXhh-KDfiL_3XQZyTCora2URVcJ5p1qA-8-xZQ-gqOKpkqzQcNmDr8M8VycBWa4JhjxRq8a4jVbD4toxq0E9o325E0gPpIMY0Lows8jtHcTTbVU3PFzVqzixB2hX4C5gG3yM1_UG51vSceJci1BkZWZa-umSfQZOVj06pHEfjQ2rITT7yVYZtky7REcVAn-NaXPPgJsRiAO0SfgVHiWvSycmOIDGM72LVynB8iCC0lkEYRN0zRVnEWZWxXVKa1JcWjWmDSXw1j5Iemr0txO2JJUhNz668sGkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
به این میگن فراخوان
🔹
شعار جالب کودک انقلابی در مراسم تشییع رهبر شهید در تهران.
@Farsna</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/farsna/447704" target="_blank">📅 23:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447703">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDgzB6oD3F7xxDGsXRToVg-zlKdm5jBi8YCgSac0Jp3LQBndOwD1QQ5ysW4pLjHO2DuK4x-PQt_ILzHtiOsSazBBYnOZBSmytCu2KFb2L6gAfAF2kl5TEH7gOSCGaMibb8p86dVLaUBM9Ov3mT-67cwS4t43_kIeJ67CZpSkv3EwcScnIxMQYr4cYiIynaXKoyCP-4QDK5c4adrsZT6Gvh__T1s2hLctIf9SfARI2lGi5iH0WD0akpLbrg-C3-Oi9D1W4dbBH5p-llqBmxgHvD7lHrY0QGZwMeLKGeAn0dnF_1ZUbmAs119oviMMC75mt1a4Cjrg4j-_B-wsIlzhmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکای‌نیوز: تشییع امروز خارق‌العاده بود
🔹
سردبیر بین‌الملل اسکای نیوز که برای پوشش مراسم بدرقه پیکر رهبر شهید ایران، به تهران آمده بود این مراسم را با عبارت «خارق‌العاده» توصیف کرده.
🔹
او دراین‌باره گفته: مراسم تشییع امروز نشان می‌دهد جنگ ترامپ علیه ایران بی‌فایده بوده و ترور او نتیجه معکوس داشته و حمایت عمومی را تقویت کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/farsna/447703" target="_blank">📅 23:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447702">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daf5179a07.mp4?token=JajdW5AX1JtAd1nFuOKi7lBit2g5X0GRgFeHvSLzRN-g89El5Snp2l2DQCbdxFPG5TW8PloyoifMRv2ajtwaelZXzBi2NQ7iI6o01cRzEezaDMvQzI21Xi3Ik1RaCOpuYO0DdFfFIFU_3XjAFRdr8s97alfruZQXmCfI36j32Rb7DGbw_4nat1vI63vydEk5DoHodNP5xp2RgxZwLFXoavmCGSSIXynz_UuT2von6D8QUWen6BgiTQV5srGxI0H-gv_Ch55QDB8JTPkUjvVBBnwjndJKNEfTQljW5SvgKZ2vBrj1csDMMbwpGm27VK6YfBacizpxsx4ROTQda_qbaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daf5179a07.mp4?token=JajdW5AX1JtAd1nFuOKi7lBit2g5X0GRgFeHvSLzRN-g89El5Snp2l2DQCbdxFPG5TW8PloyoifMRv2ajtwaelZXzBi2NQ7iI6o01cRzEezaDMvQzI21Xi3Ik1RaCOpuYO0DdFfFIFU_3XjAFRdr8s97alfruZQXmCfI36j32Rb7DGbw_4nat1vI63vydEk5DoHodNP5xp2RgxZwLFXoavmCGSSIXynz_UuT2von6D8QUWen6BgiTQV5srGxI0H-gv_Ch55QDB8JTPkUjvVBBnwjndJKNEfTQljW5SvgKZ2vBrj1csDMMbwpGm27VK6YfBacizpxsx4ROTQda_qbaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال و هوای جمکران چند ساعت قبل از شروع تشییع رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/447702" target="_blank">📅 23:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447701">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0be5112c1c.mp4?token=Lmeg696LZ5ejBt1CYb-jZF5VI0wtdL4cWtolIsKdv1f11tEV81cydnrgVAqfEPpavpMiI9WI_-ZTSdGAQVLyWmUq2AxxZT6IP328c0t8yT7JbXK1s-RRG-s0G7aCNw8nQvbHRRTlwuSg5i6t0y4-Hcl8EeF_ue_58rfbIIuTkhPNgOzT5n3Jtwka-eRqhZ9CfZGpY4qIXtSPFmwQGs3U-Peb3fg8FC6TqWfdMZPTN2l0xhJeU1lfAVO6ql_mHaTHgLb4szUCLa8v3XjEl9MjCt0sqi0tAZw001a6agavujZOWp1Ic-1TxOLz711zwoXXf04RlInW4CpgcnZb8Enr3F8dlpe70qA6uhA2WY3hZ2t8fXa2tjfinpKwhL_su13AQpQQ7OLVxX6EWCGh8Q_iEGLCYP0iessSZ10GiFkVDLS30xZVxkRgjCi3C32DEdek3qNsmqtUPgjH9Zs8qaVirXO7jxz3WSnxag8oZU5zkv8HIPUlESxjmQSnDmja_XQ_q6bRhqFnsEkS9i4wVsU93ebiRXOs-K2256lFUosOFg44GNM8z65_9BYDgAWZE8dnVPVeHSP1EStL4aezn54dBgiSLoTV8CabBCdWO8yV1FAlEOCkOSVxVnQ-BrOLMAJDVLCOpMgZBLIVUod_VD0nlP3Rw0nFNllLvGh3ieZel3I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0be5112c1c.mp4?token=Lmeg696LZ5ejBt1CYb-jZF5VI0wtdL4cWtolIsKdv1f11tEV81cydnrgVAqfEPpavpMiI9WI_-ZTSdGAQVLyWmUq2AxxZT6IP328c0t8yT7JbXK1s-RRG-s0G7aCNw8nQvbHRRTlwuSg5i6t0y4-Hcl8EeF_ue_58rfbIIuTkhPNgOzT5n3Jtwka-eRqhZ9CfZGpY4qIXtSPFmwQGs3U-Peb3fg8FC6TqWfdMZPTN2l0xhJeU1lfAVO6ql_mHaTHgLb4szUCLa8v3XjEl9MjCt0sqi0tAZw001a6agavujZOWp1Ic-1TxOLz711zwoXXf04RlInW4CpgcnZb8Enr3F8dlpe70qA6uhA2WY3hZ2t8fXa2tjfinpKwhL_su13AQpQQ7OLVxX6EWCGh8Q_iEGLCYP0iessSZ10GiFkVDLS30xZVxkRgjCi3C32DEdek3qNsmqtUPgjH9Zs8qaVirXO7jxz3WSnxag8oZU5zkv8HIPUlESxjmQSnDmja_XQ_q6bRhqFnsEkS9i4wVsU93ebiRXOs-K2256lFUosOFg44GNM8z65_9BYDgAWZE8dnVPVeHSP1EStL4aezn54dBgiSLoTV8CabBCdWO8yV1FAlEOCkOSVxVnQ-BrOLMAJDVLCOpMgZBLIVUod_VD0nlP3Rw0nFNllLvGh3ieZel3I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد خون‌خواهی گرگانی‌ها در شب ۱۲۸  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/447701" target="_blank">📅 23:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447700">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0073f2bda.mp4?token=niTUoOLR90U6NeagL0K0ag0DH49QrHo1EQIupcFuebjsm4NRyZ6LsxS1sf6iCRCAvbxtYFawLVrq7yipXm9Kq3gWhqPlis1R1VpLi63mMTiQJwjHtefrCoE7Ue8I_nf261hml_BET6TeujbJkoYEc5bDH5WGLFuROCxr14D21cKFZHq82xBA_waSzUwo_qMBeE5GI15KZleW32cRQys29e0rz4EZpm1eQ89uLmCVWkBwyZUXMwfG9VUFptJwuMA_9-qdlQ3u3ChfITfBSzzL3X1x5gEkCqHwUVP9M0KshBWONcSvzKCmsKr-Ll__pdwHHsW14iHWZ_hE19Ci0O2qPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0073f2bda.mp4?token=niTUoOLR90U6NeagL0K0ag0DH49QrHo1EQIupcFuebjsm4NRyZ6LsxS1sf6iCRCAvbxtYFawLVrq7yipXm9Kq3gWhqPlis1R1VpLi63mMTiQJwjHtefrCoE7Ue8I_nf261hml_BET6TeujbJkoYEc5bDH5WGLFuROCxr14D21cKFZHq82xBA_waSzUwo_qMBeE5GI15KZleW32cRQys29e0rz4EZpm1eQ89uLmCVWkBwyZUXMwfG9VUFptJwuMA_9-qdlQ3u3ChfITfBSzzL3X1x5gEkCqHwUVP9M0KshBWONcSvzKCmsKr-Ll__pdwHHsW14iHWZ_hE19Ci0O2qPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عاشقان امام شهید در جمکران منتظر آخرین دیدار
@Farsna</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/447700" target="_blank">📅 23:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447699">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fd89a66e7.mp4?token=g0G60xMtDfrp4tpHJU7vfaS-UMzL_uG8vWD5wOxUOMhMKDpE4wZsKuTkrLeF7XyYGmFR3iE6Mtn9L_eJRFJY_MgjjEzpCmMNfNNkNsmf6UpTBq7AEPzKT6CdcdiNWzNcPK34qEmEP6cHi313wt9USzrKUKWhi74w63kf5vZNkEIHY_Oq4pILxL64Z87NJyO4NcoADrrW9Zk8gKZCWthEtLPGbiLuGBSmw1yoXpAnCV_dtq8jPGLbqHMNSG58LAHtsHIYrdVUY1IOGazhRKace8HDeqYWSKnR2hdPIa2AlQrdubcxrcKkqtAE5aub3WBHPENHNYb-JHfMhZK0orkmOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fd89a66e7.mp4?token=g0G60xMtDfrp4tpHJU7vfaS-UMzL_uG8vWD5wOxUOMhMKDpE4wZsKuTkrLeF7XyYGmFR3iE6Mtn9L_eJRFJY_MgjjEzpCmMNfNNkNsmf6UpTBq7AEPzKT6CdcdiNWzNcPK34qEmEP6cHi313wt9USzrKUKWhi74w63kf5vZNkEIHY_Oq4pILxL64Z87NJyO4NcoADrrW9Zk8gKZCWthEtLPGbiLuGBSmw1yoXpAnCV_dtq8jPGLbqHMNSG58LAHtsHIYrdVUY1IOGazhRKace8HDeqYWSKnR2hdPIa2AlQrdubcxrcKkqtAE5aub3WBHPENHNYb-JHfMhZK0orkmOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد خون‌خواهی گرگانی‌ها در شب ۱۲۸
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farsna/447699" target="_blank">📅 22:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447697">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oa2cdpJbCE20sVeQec7PRqnICK0kEF1Jwz0JfndU8Zsc265-Y9jQPamtnZrLPb3dQOpzphECi6VY0m91z20YnW-tJWcwC7DQngzONcosF8U0tVm24wXjXItEw438y_INO9LhygMPM4mrr9Rcd2xKlL3aglNThkvmnJePOh6CVe0OCbD7Vs7bR0Xcn8carXD5iQmwSlTxfNxOnnaBzU7ZgFr8d2xm1EN8gLP4eHuE87LSG6csQAWLdivVOBc1B3j371SqQPUMOxj4R-Gv-m4ZCGv8DhELt2UGhIRQB1iRS1ka2UjU6KLB-W6HUhszfcVD25aDHmIFN_ygCCV2rhxntw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دبیر شورای‌عالی امنیت ملی در پاسخ به ترامپ: با مردم ایران با احترام صحبت کن، وگرنه با زبان دیگری پاسخ می‌دهیم
🔹
ذوالقدر: به رئیس‌جمهور متوهم امریکا که امروز ۹۱ میلیون ایرانی را تهدید کرده است می‌گویم:
🔹
پیش از این تو به‌عنوان رئیس یک کشور بی‌ریشه با تاریخ ۲۵۰ ساله با ادبیات مشابه از محو تمدن چند هزار ساله ایران سخن گفته بودی و نتیجه برایتان جز شکست و استیصال و درخواست مذاکره و آتش‌بس نبود! ایرانی با زبان تهدید بیگانه است.
🔹
پس با مردم ایران با احترام صحبت کن، وگرنه با زبان دیگری به شما پاسخ خواهیم داد.
@Farsna</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/447697" target="_blank">📅 22:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447696">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار تهران - خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd48407210.mp4?token=JVNkxWBweSG_NLbqG-OQUzU8EiETIpPvt5gsidY9qSHC39XQX5FUNn_bhNE-9dEIASGRHCYmxYTtb4eYCzxmJMy9FT-84Y5Df4BSYbmRjsYC8pvaxplZB6cVDqFL0ihRwDWw51RBgd0_mq1rEhy6T39VbIq9csNq9kyBUVpjblMvRuZ4I3F8zrR3pgYAE43bzCV_st8dCo9I3v4lWC-HxHm8Bj1_rwtdhj5qp_IS4suKsRuDpytcIHejvPdbWXCfrUHJrqqx2sXq-YuzIKE43lIi4kyhey-Oax-ua4rLGHZMROwv9sVKUsm_D_eZ5R2iy2a9FJo4a5JEnB9RFrEXGX7HRmufIUk95UBcsPWyHv0rpYxSLgOLXk05LnmGYdGka_PugtoGVmJE5u1USv74G9UeE-PSv-9IbDMrUl3YzNpOfId_pg0m7QNErUGbXDcMbRypwM8uQ3JYJrRd9TWM38ck1nTCuAQVBszttQEzqm7XmoFLy3tDRzZuj2jo9hlOesz2J6ir-gcNkrsXCmoRKkTbfTBYQm56-yqFN_Re3gzxJP3sx4dpIdE_oumInxPPRmDssuCdwsYPWwtTJhM9wIwMozT6ttjDjKGHFZNEQUnWaV6KQK_boovaLdrR1wgSIstnKUrx1n2_1ncG0vM364A3ikcSaOLVNiiHj3rXd2M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd48407210.mp4?token=JVNkxWBweSG_NLbqG-OQUzU8EiETIpPvt5gsidY9qSHC39XQX5FUNn_bhNE-9dEIASGRHCYmxYTtb4eYCzxmJMy9FT-84Y5Df4BSYbmRjsYC8pvaxplZB6cVDqFL0ihRwDWw51RBgd0_mq1rEhy6T39VbIq9csNq9kyBUVpjblMvRuZ4I3F8zrR3pgYAE43bzCV_st8dCo9I3v4lWC-HxHm8Bj1_rwtdhj5qp_IS4suKsRuDpytcIHejvPdbWXCfrUHJrqqx2sXq-YuzIKE43lIi4kyhey-Oax-ua4rLGHZMROwv9sVKUsm_D_eZ5R2iy2a9FJo4a5JEnB9RFrEXGX7HRmufIUk95UBcsPWyHv0rpYxSLgOLXk05LnmGYdGka_PugtoGVmJE5u1USv74G9UeE-PSv-9IbDMrUl3YzNpOfId_pg0m7QNErUGbXDcMbRypwM8uQ3JYJrRd9TWM38ck1nTCuAQVBszttQEzqm7XmoFLy3tDRzZuj2jo9hlOesz2J6ir-gcNkrsXCmoRKkTbfTBYQm56-yqFN_Re3gzxJP3sx4dpIdE_oumInxPPRmDssuCdwsYPWwtTJhM9wIwMozT6ttjDjKGHFZNEQUnWaV6KQK_boovaLdrR1wgSIstnKUrx1n2_1ncG0vM364A3ikcSaOLVNiiHj3rXd2M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودروی حمل پیکرهای مطهر شهدا در مسیر آزادراه تهران - قم
@TehranFarsnews</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/447696" target="_blank">📅 22:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447694">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">لرستان هم فردا تعطیل شد
🔹
استانداری لرستان: تمامی ادارات باهدف تسهیل در تردد زائران آیین وداع با قائد شهید امت فردا تعطیل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/447694" target="_blank">📅 22:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447693">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUhqflrPWks6sOnpJ8kqiW_4p7ToAPN1TX7ab7YscLSEHYvG6XUHypZfngjOC9vgBjvq13ok-Iw9vvbQCeMt7ockPxeD9YAUsEgKRSY5c0Xm5YeGD_lQ0yPtYOqHlDzqcMzMHZtUmPlrIxgdHybtcVJCPX99xMlUFZV_4Wr7rhIjcG9biKekV4bi0w5JcAicIn60nwHV-c3mXXFU3gNy0M8v3R3U8N83Mdyl3EGYYpMnaw-cHDkBhWugopoL36LAyjJqVZRhony5cCgx_6MnsbVX6wBZAEfHkHVn-C0AuvgeYIblrD88DbV6grK43a0SsizqwSIFWmFH4YnOzWzeJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
محسن رضایی: ‏ملت بزرگ ایران، پس از ۵ دهه، امروز نیز با همان صلابت و ایمان روزهای آغازین انقلاب، شعارهای کوبنده‌ی خود را علیه آمریکای جنایتکار و اسرائیل غاصب سر می‌دهند.
🔹
این شعارها که با خونخواهی رهبر شهید توأم شده، به خشمی مقدس و اتحادی پولادین علیه دشمنان این مرز و بوم تبدیل شده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farsna/447693" target="_blank">📅 22:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447692">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سخنگوی ستاد تشییع رهبر شهید: نماز بر پیکر قائد شهید در جمکران، بعد از نماز صبح و به امامت آیت‌الله جوادی‌آملی اقامه خواهد شد
🔹
بعد اقامه نماز، پیکر رهبر شهید انقلاب در بلوار پیامبر اعظم به سمت حرم حضرت معصومه(س) تشییع می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/447692" target="_blank">📅 22:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447691">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🎥
تهران، آخرین سلام را گفت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/farsna/447691" target="_blank">📅 22:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447690">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a509ce5c59.mp4?token=qBoo-YpS8gASO9_CWGzmUAzszXHi8wD24Oo2GflQK6bpICYVV0RNH3HB0BovFMSxhC0d-iQNqYOod1oGeSaP5XSYAHYS-YEMncDcq3OPjtxL4orEyN24kO--fZqmT-g4w9MKf3vaS5MyGCapBLvyqYvYpgbKr-Vj-PRHjM2gjM-TkfsFOOMVlIv9uVE7mA7BMEgzh3MV9B5eEqTW7-H3-w6AHbPRA4HUzSQtel7sufefIKAwwz7QUppFw1ZgQPTgxOwPCulgrJczPPoMD3dI38fyU5-Y0tGFiK7SJvnkgTNLXkJ0HIIOPKKBFitbM9oWW_oVqEl4KkGlQPeYtYnZKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a509ce5c59.mp4?token=qBoo-YpS8gASO9_CWGzmUAzszXHi8wD24Oo2GflQK6bpICYVV0RNH3HB0BovFMSxhC0d-iQNqYOod1oGeSaP5XSYAHYS-YEMncDcq3OPjtxL4orEyN24kO--fZqmT-g4w9MKf3vaS5MyGCapBLvyqYvYpgbKr-Vj-PRHjM2gjM-TkfsFOOMVlIv9uVE7mA7BMEgzh3MV9B5eEqTW7-H3-w6AHbPRA4HUzSQtel7sufefIKAwwz7QUppFw1ZgQPTgxOwPCulgrJczPPoMD3dI38fyU5-Y0tGFiK7SJvnkgTNLXkJ0HIIOPKKBFitbM9oWW_oVqEl4KkGlQPeYtYnZKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایانی بر انتظار ۱۶ سالۀ مردم قم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/447690" target="_blank">📅 22:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447689">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LN8k-VOg-TTeVzJXMpxjn5qtuqna23w--CdoyLdDn3LGReCFWr4NwkGGvljNy6fn5jtgM4ns1NrMwSDe7v2lN3IeuvKXMIN8iNFIzBuLH1dTJfWx8PxeTFySL8SsfGVuHquJ33FKicA2ochi2AkSaiRQb1lTjFr5N6x_3619nfPCHZgDhPfGkjLRYS-kPq9KOuvXPaHXn7oGj8pfzLk6TBvS1YWtArf1dG1INW1ORjPlhAst5eekkqQ4mWidjmoENK0ig_OY9AFJFSXBONTOQXMhQjCLEmEawoG-DQWplxsxDJAmiyAEHSMTTIBp9kj6xJ347pYVYtIxRgnia0X6ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای حضورنداشتن سیدحسن خمینی در نماز رهبر شهید
🔹
انصاری، سرپرست آستان امام خمینی: سیدحسن خمینی بدون تشریفات متعارف در مصلی برای وداع با رهبر شهید حاضر شده بود.
🔹
اما دربارۀ نماز بر پیکر رهبر شهید، ایشان به سمت مصلی حرکت کرده بودند اما به دلیل توقف خودروها در مسیر، امکان حضور در صف ویژه نماز فراهم نشد.
🔹
او همچنین امروز به همراه خانواده در مراسم تشییع حضور داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/447689" target="_blank">📅 22:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447688">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phBmj4cm48LYGsW7heJNgPL6jh11MY3PiD8IkL3-NoJA8WPVmDPMUD_wypIKwHbACgsBUe6L6LUYoGreebWTgh9jouL0Ei8hLF7WJ88gvCh__9LdsNNXFCl27HErhdjwEP6rc0atGbtLzfodGW8eoerWsNDIS1yOq2UuMZRPy2Hb77ahQ3IGkzAOqsuFQB303hzGoJqtme5-4yxgGJ_gsNX4h9HTBWXalHe4LqoVAnMbXA0gckd5bt2k17-D4tt_Tu7uJb2cppBzThyAgTd9qXhv5G-zLdws_JVM2GrU26lz9p2qVsFdywVUz1xQh62m1uLVa5EZB08KsombzUDTRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: قاتلان قائد شهید امت به سزای عمل‌شان خواهند رسید
🔹
رئیس مجلس در پیامی به‌مناسبت تشییع تاریخی رهبر شهید انقلاب نوشت:
بسم‌الله‌الرحمن‌الرحیم
ملت شریف و قدرشناس ایران!
🔹
داغ جانکاه فقدان رهبر شهیدمان و آخرین روز حضور جسم مبارک و مجروح او در پایتخت ام‌القرای جهان اسلام با تجلی وجه دیگری از بعثت شما در این مقطع حساس و سرنوشت‌ساز به حماسه و شعور تبدیل  شد و حرکت به‌سمت پیروزی قطعی ایران اسلامی و جهان اسلام را شتابی دوچندان بخشید.
🔹
مردمی که ۴۷ سال پیشران و پشتیبان انقلاب شان بوده‌اند، در ۴ ماه گذشته هرشب با ندای مرگ بر امریکا و مرگ بر اسرائیل نفرت و انزجار خود را از قاتلان امام شهیدمان فریاد زدند و «انتقام» را خواستار شدند.
🔹
تحقق وعده الهی قطعی است و متجاوزان به خاک ایران اسلامی و قاتلان شهدای این سرزمین به ویژه قائد امت، به سزای اعمال شان خواهند رسید و گام نهایی انتقام از مستکبران با آزادی قدس شریف عینیت می‌یابد.
🔹
ملت مبعوث شده، رهبرشان را بدرقه کردند و همچون ۴ ماه گذشته دست بیعت به سمت ولی فقیه حکیم مان حضرت آیت الله سید مجتبی حسینی خامنه‌ای دراز کردند.
🔹
باید قدردان این مردم بود که در مسیر نورانی امام و شهدا ذره ای عقب نشینی نکردند.
🔹
دنیا امروز فهمید انقلاب اسلامی و جمهوری اسلامی ایران، پاینده و جاودان است و با پشتوانه‌ی این مردم، بن‌بست و شکستی وجود ندارد.
🔹
این ملت، از مکتب حسین علیه‌السلام و تربیت‌یافتۀ امامین انقلاب اند که در ۳۷ سال دوران زعامت رهبر شهید انقلاب، نه تنها روحیه جهاد و مبارزه را حفظ کرده اند؛ بلکه ساختارمند و محکم در برابر زورگویان دنیا ایستاده‌اند.
🔹
قدر شما را باید دانست و از هیچ تلاشی برای احقاق حقوق تان کوتاهی نکرد. چه در پای لانچر و دفاع از کشور، چه در عرصه دیپلماسی و مذاکره به عنوان بخشی از مبارزه‌ی تمدنی و اصولی با سلطه‌گران و چه در عرصه خدمت به شما برای گشایش امور معیشتی و اقتصادی.
🔹
امید است توجه به توصیه های اکید رهبر شهید و رهبر معظم انقلاب در کار بی‌وقفه و موثر برای مردم، با همت مسئولین محقق شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/447688" target="_blank">📅 21:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447687">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تمامی ادارات یزد برای تسهیل حضور مردم در مراسم تشییع پیکر رهبر شهید تعطیل شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/447687" target="_blank">📅 21:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447686">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ادارات بوشهر فردا تعطیل شد
🔹
استاندار بوشهر: به منظور تسهیل در تردد و بازگشت زائرین رهبر شهید، ادارات استان بوشهر به‌جز دستگاه‌های خدمات‌رسان و امدادی و بانک‌ها روز سه‌شنبه ۱۶ تیرماه تعطیل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/447686" target="_blank">📅 21:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447676">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZmF04z4AA__fdCuLzj-0Y1GE75Bp6GCABMf4cSMOTbKsddznhh8OpV3HYSt4TV6tbV_Htb2LdW6P9r0fSZ0LDnvEXCRWLFvAHXgFJQx1HLvSiHwDd5XyGb8jyYJ-8m0fYVhhG9Gaea25qNfCDRGD2NJKbzNbZ3OSydUW2bgfrecFUneETKERalmvonekgoUOtRIQbeO23ssdj70skNvqVsUkm3AcgJ54tKSXs10eMt1pL8mkgwMMxViUvUU5-dYw2NFizdMM4o6sm0Gcbuh1kiNL8dEHFq4aSosW5kk43vRA-E5jRXocU7nLogzg_SM9TP4oAQerfIDJZyFVyrKkZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXo70wkP9Xopxig8JXkl-_H2PGZqqXnrH18wfqEIBXSb3aE9srwxAMI9udZOkU93-TKZb-u0h_nyR_K7kX6oE4hf0wbvfITvf1fkafKUthI921qnDUEFzb4zzGbTV-0IWoudHaLlQqTyOp_Bgmhw4ulfyQI20I_ms9hjjAaPEobisILDXluNJGZ72jSKcOzgu8POdvuuQFDUzjOc5m7ceiwyROHVR0WF9X9eWDzYlvlF8856GCx1mKE6Bed9L4JlgG4YkWH41_bW-tgYD4jbHzvtgTKlSjA7OtEAK_PMJmL8OiARmxjiYyR19Jgrei_ijwbISSQrGPJ5k8ww8GgkyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LJVftn60MazDwRVjDb3IgNvHVgObeoYbTE71amZihbE77931VCM8kTTEHHCoA3hSP1N8-7nyd0kszXKatEOJc1-BdBdH4crBGldY7AL5xoJAj63mGSdIO_HgbfCvvtiIv2QqIuv5wcJ6IfXWoYaGCh1LfPG3h7s9vKzIw86L0xap1MZ-kkPtdPxJ66J1wFRrNUEUWkW0OK-K7L8nKSmcq-34tAKJBQhkpDYYYIRG7OC04WsgHSX3pkp2TQacMegSsFjEpHaVqd9uliLLaBx4LRVs1SqIkn3f4El045DiQl9rpvpn91f3QppLoB2-vXlxezKpiFNp7FNAy_FA_BjLjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hS_ga9BjnPPjoXDiRrVLNzsVDAjMqhGtcaKS4mNdPwcvIwVVW98wFYE6i1hrGZGYASK8NDVqttXEC6ILrseqge7NlWm84b5n8K4WE4OA3Yt0ul889hicLrNz8WxPthdZhoFS6cbAdNj3SRS3ycxI_1gCfumoGTjpb65PBYl9G_KA1E2zD7pwvsOBjz_jPxXVfPk7SgXckCNq5VpAY6FzzcQrfMLR4Pa1MgBNls7R7cj6j25NoNIwWVJQCP8IgICkVuiIzr0B029YJXZOd7-TzGaOIyKXGnUJuT7lo140rwE759Xvz1OSyottwRZmK6a6NoiZQMurAP3XwJ3jnXgU_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dDR6hhsZMMAZEIU_8xqLnlWpf7QwaN3geWI0FZtAdq12uaX5aoBR38byyyUqBM06WLQ4Rcn8yOwUDmQf3kfWDTE9vXS69eP_m8f4HHGKNyjt3e941z48186TbHhqvexL1WixpX6QoiYIpSoeGmg4OL_G71cDFTzk7cjqcRztRLWiWU0LL4Vb1ju8s2DyMzSS4u5aLHq3wZL8o0fy0msElC5pz52ppC7jWLs1ApqDGBcs37NuQHT9DEMHB31VgKKEdDg16cMttefyWdD3l3SAI98Q9k0nnH-ioX1W-RQvZDlUEcfZ1gMOz0dvp1VUgOcABx0ABgTijJaFHQexni4vIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EbyN9Q7JiZ0CgUpHgSL3MizJSG6YRJztBYriWgACuMVLlbVhALQdsfjhj96zIIPgJCN5Whawcvqp_UhoG6OBSIuCaQGxm71TBvINP30yLF3x4VRo75wjf4PaiVvFUIJJjyVZAupNbirotsOd-9wqEhp00ejZ-lJSRfe6FQibXlAuNPMfGKYmWCQ2Sc-mFvllv7sjpczeZcF4zG2Kz8VfUJDShE4N9l9N5dhkwyN6Vdvx1Jlw6HVdNkfQBsAieChp-PY_glWiBR-Qp3i93xIEhYmx3oQA42S5y0PQ9L74kXNhJDN8822v9ZHgdYEjG823Jd5Lvx3J57IceyvWwfQQOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/unT1TV_ilEIYGaYIA1-RhBVgRQceGA9yOsdtLQIKLUS7EQkVE5KkbFZXD5OSMeuSOSaojcb4fiijm7yoJwX76iITQU-2NdH-1W9pGCKReLVQF5sFpLdBrMTb7DPR04Gc_jl_vkDU9HUUj5Za7U4AYvUHwJ9Dg-lbsjWXYwLI9-M3RAqUcOoqsO--zKc0iPK8GmnMyn49Aw8t-xZv6mESt-IqlaaFYfelLRs3xWTda_16wdLtLNDUPRLQF6fDNzBidIXB1gQvI2RODF0l0Sz3pBBs-Rl-Ji785BH_qcY33a_zzjPivzzVCbffvc_ApRzmmidSjjh-2EuswIOPDQBBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IOkxUFk_MrjEvpulassqKRK_IN5fhwQJcsKrOI4YSYL--YrkdnCv_p05ejpTs_4BkzwuVWwROFhfJXyCq8EN26QuB6btfr-TrzvTOWew_12ibcbqAjFejsQgbUn8TJXxEbhaE_CIhjsCB4E15Za1HAjk60pY0C8UtGBYMI219mH3VPa0wEDnbU3OXqZo8IcAxT31Ts-2TfCJOrwScZn8N4MeAUqTT7Zz4nsXFFwY_Tl-3KoXVWQY8jVT9_BT0jOssZccODmqpiXKB0iirv02emJoPFMs6pqNYq37ZyV8rLkcSNDp5uWxZGpgDtY6pYQdX-lmrYiMfw4DajCig9fMmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0MM-F9mA3sUyhZSnm2_o-IIOQSfdtHhSq_txz73K5budy1Uqf0Qo4mNJcF_HBMZT0NYhZ6W5RCWJfZ7MDyi99nQoLJVNSemDtrP6X_8J1GOCRvmW7wBIsH1T_1YgPacMasLf_sBAB1hD6Kdc1hC1qrdEuh5oolsZg61QjxwCTWw_kVpPLLUfpxLrh0FsVwOJgHk3M1yyoTWlxXLGJPzazwIFMsdMil-F0h6KTAh_vJIeVDBQCYSz2SKsnIv4nZh_9koHMM3qJc9bWlMgSuVIWWxlIro3hwCCpiehkP16WCDIZvd98IgaQF-MQyZ-0nsrKz72RKQuY-U67RWI8lC9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L6z3wOmt1bn10BPPvYApjZ1idQ-NliVcl3S6swCSMmURwKNinl6aWdu0Q_d2gLi5y435OsHV9jJkD7wk3A8BJrkjrDzme2xxve2ZCKT_QY3qiJfRSUFdZefMN928FA-m28Ldr_tPfnnk5OU1Y8KsQgzplBUChDRL5F7maSzY2-hwMbjdfVjmHdWdvmC0_Ik6j9WyxjBkkSG3A0TQuIiBzwpebJi-SDzfH6VWchAfvDFNhKKB3yhN7uYCR-BtOTwKcFXOlq6UwT8oA6lMflxPCB8oq3c0Z1dU8_GpddKgt1fP4DNycvalj_aidSrt6mBFkliflAudYBcPiOzDU9vcqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚫️
حضور مدیر عامل محترم بانک شهر در موکب خدمت رسانی بانک در مسیر تشییع پیکر رهبر شهید انقلاب اسلامی</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/447676" target="_blank">📅 21:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447675">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/447675" target="_blank">📅 21:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447674">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TroIitsnThZVh0rzE-e99MG-g_BOYBg2qc5bl36d8YJsYX2QBU_VJdjyujlVzsQiw-3-DJI5WoSj9d2xeT2L7Ra3P0sfyUQEteRcYfkadY3w4d1QYQFojeEgJ3GKHmuYwseG1ADmkpDhPwS4Hj32cTILpKruk_C4LLs7vpOIYLutdbcGpo3MyF9WJEtq6vE5et8HjQaagq8Rec4BYXb1-ik55ProNL9mEsz02ZlKSV5KnWVXbeO7WXKvYZVJLl2V9YDy10sRaJtFCrc8kQN0Fs26QtIg20tI6m02abToHK0nyGm4tL4kKrgVTJBPYvFd0zMtV6fun7e2Kas9l41dsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس فیفا: ترامپ دربارۀ کارت قرمز بازیکن آمریکا با من تماس گرفته بود
🔸
فیفا روز گذشته اعلام کرد محرومیت ناشی از کارت قرمز فلورین بالوگان، ستارۀ تیم ملی فوتبال آمریکا را بخشیده تا این بازیکن مشکلی برای دیدار یانکی‌ها مقابل بلژیک نداشته باشد.
🔸
بخشیده‌شدن این کارت قرمز با شکایت فدراسیون فوتبال بلژیک و اعتراض افرادی چون توخل، سرمربی انگلیس و یورگن کلوپ مواجه شد.
🔹
ترامپ امروز تصحیح کرد که دربارۀ این موضوع با فیفا تماس گرفته زیرا بالوگان را ستارۀ مهمی برای تیمش می‌دانسته است.
🔹
در ادامه اینفانتینو هم تایید کرد که ترامپ دربارۀ این موضوع با او تماس گرفته اما مدعی شد این تصمیم را مطابق با آئین‌نامۀ فیفا اتخاذ کرده.
@Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/447674" target="_blank">📅 21:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447673">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv5thzjrrqW4Cdy55TLrmy92seALbROJi-1FdapXzFTDKgENRBq5nFY8FW21uxZXv1jkDQt-FMvZ0CrvaeLY_MW1kwNP8HDgKZr-T34A7Y0t6e-gBiPgHHbocowzJWKZufiR7VwF7LG_AkE_4Ni2GTZPelY3DmEGxT6NIVodc091n9jL_UFxMJKWjycrOe9kYrykzEp_3ynS9VvbONTX4umklqmRxNaaXHmSi35P4Ipiy-gTEFwHChVsla9H6ZrHiiG5mK3Kqe9OKut4FLzK_VIAlFGRFUtch0xriMSmchkzkrylPzKS3ksp1VwfGFOm1TWYrzcqOE_zqI9FOWpkng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بدان امید به تشییع آمدیم که صبح روز ظهور برگردید
@Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/447673" target="_blank">📅 21:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447672">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_Gcaj6fsie9wTVrZG3fZRWjZjwL2BDKN8D0ITJQ7zrazvfczhOexKCuHhKPioou0jKTbLhu9lGQvJdv62_gYorUAu5vzYMl3R78uipSEG-pNAqnUw87uqNvdfR2MQyNJdMw4wtWA3hq06lpBxZP9oXVm78ijJHQb7HkcyyzNxWy8bvu3ugo1ObE8ozfxz64CMoVfhmipWFiLyqUdJ2Vw8hFqHIeepuzsPM5SkWisL3yJqObcfa_sdZ-Dw5oLwrfm9tHk4F-jZn_WVggcJqmDJDatpLq-G9UhmhfDJh2pTudsaeCq3Df_1sjMuaogHsEOI7fks2dSxNjeIGSKuc6OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
رسانه‌های جهان مات عشق و علاقۀ ایرانی‌ها به رهبر شهید خود
@Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/447672" target="_blank">📅 21:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447671">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a9851feaf.mp4?token=pmP6abOl9d1_qSwXk-Lw2zc-bm0ggLmc6yEeXtFmrVtmzZsGzPQT9SaL7SomFQZZW2Gf7FYBpRA40AkjAklGJ1iV8iehPbJzs6IygiVcPWbICHx7elfpPYg5JxLPzbEWoPEWZ5NLOhaFzNVe0hd1Bi7DKaxWoe3FIF35fwBs9VR6cddaUGUFe-ZeMXdz48TsPFqgWLWp1meZ-OLrdFeeh-y3FKtM2n1brL-A-tbS9KtNwWHo1XCMkZ0_e_EGBys7y7570cGm-llbxDJ2BbbIzJmo9KE4ABO8O91uVsWQ7U1wAn9CNTxCRlSGsjnT3zOq--26SIRrE-jjMCCLvUJ7UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a9851feaf.mp4?token=pmP6abOl9d1_qSwXk-Lw2zc-bm0ggLmc6yEeXtFmrVtmzZsGzPQT9SaL7SomFQZZW2Gf7FYBpRA40AkjAklGJ1iV8iehPbJzs6IygiVcPWbICHx7elfpPYg5JxLPzbEWoPEWZ5NLOhaFzNVe0hd1Bi7DKaxWoe3FIF35fwBs9VR6cddaUGUFe-ZeMXdz48TsPFqgWLWp1meZ-OLrdFeeh-y3FKtM2n1brL-A-tbS9KtNwWHo1XCMkZ0_e_EGBys7y7570cGm-llbxDJ2BbbIzJmo9KE4ABO8O91uVsWQ7U1wAn9CNTxCRlSGsjnT3zOq--26SIRrE-jjMCCLvUJ7UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قم آمادهٔ آخرین وداع با آقای شهید
@Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/447671" target="_blank">📅 21:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447670">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c6a70224.mp4?token=SRdsv0xB1Xxh1uyn5quflZVLUo4ullJ3sVNUZGfteghwXUqJqvkToNYkmLaDOg-iqKimJXwtaONwacw29I-qORHMfAs_eGQPtCusj9JCG_bkxOGQa3QXH7U4m1o3dlNYPQBTklsu-pMDuI1Lh-v43dOFZwh7R3DFvgFaIVCe2xJSC-_yhEojMxWk8MG6_QovGimdczmeO4fE9FxMdZkIFjaBntIkPn2JgrP0bF3372-RKZL0ah93szbs7iGsuWpw6JH2pwzCuOcI81j_N14KravIVb7sgnfta7hY_cvni5JwpRxGx1k8iHXhCkyHnxNsdBvcEb5wakt4c_3rzNqdRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c6a70224.mp4?token=SRdsv0xB1Xxh1uyn5quflZVLUo4ullJ3sVNUZGfteghwXUqJqvkToNYkmLaDOg-iqKimJXwtaONwacw29I-qORHMfAs_eGQPtCusj9JCG_bkxOGQa3QXH7U4m1o3dlNYPQBTklsu-pMDuI1Lh-v43dOFZwh7R3DFvgFaIVCe2xJSC-_yhEojMxWk8MG6_QovGimdczmeO4fE9FxMdZkIFjaBntIkPn2JgrP0bF3372-RKZL0ah93szbs7iGsuWpw6JH2pwzCuOcI81j_N14KravIVb7sgnfta7hY_cvni5JwpRxGx1k8iHXhCkyHnxNsdBvcEb5wakt4c_3rzNqdRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خشم و آشفتگی دشمنان پس از تشییع امام شهید
@Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/447670" target="_blank">📅 21:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447669">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d743ee26f.mp4?token=pRlAY7VLbHDUhAbAmB8D4RoYFC5Oq7g_sGfrfWrtk0AtT4OrrOeDD1DFBER_obfgbyKavdTkwchU0w5rq4KJQrdDN4s1bTWa7YZoZWyaEaTdUZtYqXXDM358RcGo85iWavamowjumw3Mz_2ClD7JIL2dKq5TiTVxa-c6qtqxqp4MWQrRM6ZT_-y8nKRDaQCRHBKGrMio2LA8CSwtM2w0BaLuBB2CmrIP6KEUMPJq-0BE7QITboIUOfQruBXJbkCGXHUQDMWhqBlXmplunbdijAu5ujkeXuKKXoBrHmn_kDQ71GHcCmilWJoopSxH6UroyChkEotD0bCW6PyELJv3Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d743ee26f.mp4?token=pRlAY7VLbHDUhAbAmB8D4RoYFC5Oq7g_sGfrfWrtk0AtT4OrrOeDD1DFBER_obfgbyKavdTkwchU0w5rq4KJQrdDN4s1bTWa7YZoZWyaEaTdUZtYqXXDM358RcGo85iWavamowjumw3Mz_2ClD7JIL2dKq5TiTVxa-c6qtqxqp4MWQrRM6ZT_-y8nKRDaQCRHBKGrMio2LA8CSwtM2w0BaLuBB2CmrIP6KEUMPJq-0BE7QITboIUOfQruBXJbkCGXHUQDMWhqBlXmplunbdijAu5ujkeXuKKXoBrHmn_kDQ71GHcCmilWJoopSxH6UroyChkEotD0bCW6PyELJv3Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسهٔ امروز از قاب نوجوانان و جوانان باغیرت ایران
@Farsna</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/447669" target="_blank">📅 21:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447668">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f5cc9d0aa.mp4?token=Ay6buQYAJTY4b0vgeMkXFI4Vyd_biRspP7tkcAXF3zySXmurq1gw0MvRl9NfMgZeqOJqSSQLpC8GV9kt-HexWPDlGvKTEWjgN_AarJYPZ25irF8EC0juW8Y5BR-Mf9K1bIYFcllr15Hn2g1VQXnkyJj2vSEr-IDhn86dO37F9wFHGE8cERxmaCwxbuz9uDyBd5G_3dWYUHVbT4SWMcj32HLQ5nJBY55GuFouCKxeyXg82wt5RuJzgK2TCvg3gDxYbeP4tHGNxEtLMXo9uf9rk1ivOqHHTgaBQPnG5SICvaFEPAG6BRvEiqEGcgrvzomPW_bu61R-MWXTz6-aem6DkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f5cc9d0aa.mp4?token=Ay6buQYAJTY4b0vgeMkXFI4Vyd_biRspP7tkcAXF3zySXmurq1gw0MvRl9NfMgZeqOJqSSQLpC8GV9kt-HexWPDlGvKTEWjgN_AarJYPZ25irF8EC0juW8Y5BR-Mf9K1bIYFcllr15Hn2g1VQXnkyJj2vSEr-IDhn86dO37F9wFHGE8cERxmaCwxbuz9uDyBd5G_3dWYUHVbT4SWMcj32HLQ5nJBY55GuFouCKxeyXg82wt5RuJzgK2TCvg3gDxYbeP4tHGNxEtLMXo9uf9rk1ivOqHHTgaBQPnG5SICvaFEPAG6BRvEiqEGcgrvzomPW_bu61R-MWXTz6-aem6DkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازتاب حماسهٔ تشییع قائد امت در رسانه‌های جهان
@Farsna</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/447668" target="_blank">📅 21:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447667">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e22d09f3a5.mp4?token=KYYzLCUuB2amqYkStwDmCPaUgG3WObaftcF_ld9YsizIiQeR0YexFQS48Y5l3YGhjla0RMZNG3sDhDsaP4-6WtEn9Kc2q-CTlR42EwJ011Qex8Ov5Kw-B029UIQ-uvjkI2yDxODzcwg-qFfGGqeW7rEMkmsFOkn7chqjA3wPqZQEj_LmnCrkYtCxjl_CC4UGypBRv6W-qbMPoQM0iP7tdc-S74B5vEOTzjPvGOXrtwvPvEr3ExXiAjunTfTFIMcz4xe6z_9pb33w2z6Oo9W6TqlljprEz2LMuWRjGlhWweAozVABbgWVdz_2ENSOeegwD73MVxwzdkEdpfZlE1_ZWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e22d09f3a5.mp4?token=KYYzLCUuB2amqYkStwDmCPaUgG3WObaftcF_ld9YsizIiQeR0YexFQS48Y5l3YGhjla0RMZNG3sDhDsaP4-6WtEn9Kc2q-CTlR42EwJ011Qex8Ov5Kw-B029UIQ-uvjkI2yDxODzcwg-qFfGGqeW7rEMkmsFOkn7chqjA3wPqZQEj_LmnCrkYtCxjl_CC4UGypBRv6W-qbMPoQM0iP7tdc-S74B5vEOTzjPvGOXrtwvPvEr3ExXiAjunTfTFIMcz4xe6z_9pb33w2z6Oo9W6TqlljprEz2LMuWRjGlhWweAozVABbgWVdz_2ENSOeegwD73MVxwzdkEdpfZlE1_ZWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور مسئولان در بدرقهٔ تاریخی رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/447667" target="_blank">📅 21:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447666">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🎥
پیمان امروز، ادامهٔ راه فردا
@Farsna</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/447666" target="_blank">📅 20:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447665">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7cdff38f0.mp4?token=XQ7dyimHUsZaw19Odf94LLv5VaaIqOpUKq57YcNaPp7fx9FpHDSLj1aJqj8fZ44ro-Vlq1mqhkjBzDg-fm2vaJqZBYqcYVejRw5aHXLzx0DQzYFSL4VtlVeFbcdHVxzdw3hNaYjN3e2e6E0xI_SYPEdaYGjQrg1zGUxZglmMGYMqmEdLRf6RQDF_OzjkpT54ey285vP5WbAhe7dCvgxNMrS-VfwkWUnGZx8cMLcGe2_NMrCFlRaOshchFIuDxMmFNLsv6IwzstIX7eCnDikxLKXrRC0Ww-yR76PALC2ZM1l2QblVbH74EihpSSvKKOj3jBFoGwRC5SLFMIZYKAP9Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7cdff38f0.mp4?token=XQ7dyimHUsZaw19Odf94LLv5VaaIqOpUKq57YcNaPp7fx9FpHDSLj1aJqj8fZ44ro-Vlq1mqhkjBzDg-fm2vaJqZBYqcYVejRw5aHXLzx0DQzYFSL4VtlVeFbcdHVxzdw3hNaYjN3e2e6E0xI_SYPEdaYGjQrg1zGUxZglmMGYMqmEdLRf6RQDF_OzjkpT54ey285vP5WbAhe7dCvgxNMrS-VfwkWUnGZx8cMLcGe2_NMrCFlRaOshchFIuDxMmFNLsv6IwzstIX7eCnDikxLKXrRC0Ww-yR76PALC2ZM1l2QblVbH74EihpSSvKKOj3jBFoGwRC5SLFMIZYKAP9Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از زوایای متفاوت از غوغای مردم تهران تشییع رهبر شهید در تهران
@Farsna</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/447665" target="_blank">📅 20:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447664">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc7a08a3b8.mp4?token=ac8Ywtr9aw0FfFmjDMwB3mh50ysP6V2LH6IX8lix6JKRQWORb_JcBFG6RhPobiL09HONenmW_y_6pTd7XBmxGepVx-82dxnrfDkgS6BskJoyvqZ-UfzKb5gWejjtRzxzFGEREDFiqWaaNZc3qnUATs_4xuqryMCTW2Ul8Z8K_KjQqwp7vXxqznsfM5bQygYhl0Nb7XxNPx2bBIBheaGP31FIOIwde83ltxqRk6CkJSG3NUYsVokjGY_h0E5zVJfn4QnoH16I-FoQv70UBCGiv6lcn7RINIoBRTm8Vu_LwFuKS8VQJeOA1vmRpggLPzyqdJBgQvm79FDqJiOMMenqFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc7a08a3b8.mp4?token=ac8Ywtr9aw0FfFmjDMwB3mh50ysP6V2LH6IX8lix6JKRQWORb_JcBFG6RhPobiL09HONenmW_y_6pTd7XBmxGepVx-82dxnrfDkgS6BskJoyvqZ-UfzKb5gWejjtRzxzFGEREDFiqWaaNZc3qnUATs_4xuqryMCTW2Ul8Z8K_KjQqwp7vXxqznsfM5bQygYhl0Nb7XxNPx2bBIBheaGP31FIOIwde83ltxqRk6CkJSG3NUYsVokjGY_h0E5zVJfn4QnoH16I-FoQv70UBCGiv6lcn7RINIoBRTm8Vu_LwFuKS8VQJeOA1vmRpggLPzyqdJBgQvm79FDqJiOMMenqFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ملت بیدار، هم‌قدم تا آخرین وداع
@Farsna</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/447664" target="_blank">📅 20:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447663">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ig5mMZ_yddDFDUU2Lc-tyyIAYliuzg0wkuKtZGZSsJoCsEHyecoxSxqJgjnbvfrEs1-kRgfU0ktZFnW0VZW9buxLa60B4z2IqshWqag8qXhlRFVA1JCaZDIxKRemtT3PlZ_acEdud7lxSJ2mwOkgmirWniZQ18Hgj5pmazKxLU-P6DaaJ-bYQqhlHw0_nk_v02gkm2bF9J4EINIRPtkpYlsbn4vKSZYjLeMaygrabe7lH4FMWVlie8dz67YpcucNP4h6JVwBuH-C89hUihkp8-I3XaNo1amsm_ebUmmpv7P2VMzuDfPKTMfvu8AYUniwx55QUEP3AeiskkmZR-PfEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از حضور معاون دبیر شورای‌عالی امنیت ملی در تشییع رهبر شهید با تصویری از بردار شهیدش مصباح‌الهدی باقری‌کنی
@Farsna</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/447663" target="_blank">📅 20:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447662">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHk4qT-DNYSHzYYQuRSQOcv_qZHxNxY_M65rGf4pSZ0zKjcdbhuZAqPjjwTPw0NEOSVZaX-E3w5DR_nLH00hw2-tham29dKLOUJqzVAPcg4Q_4KPJucfApAGEZGUUpJhJwcw2ZAckJnj3koFHT0QmByJQzQyYmAUSDG2y4md3U5lVnk_Lgkdm1XeatPP7KFNqAhE4L0n9uDC7VtOWxyYCgBFdzq3KJYuXcTvXOAZ--a-Et_2l2JYOQ0slw-4mnL07ZQAvVDpOzlvMiROXuCJcJZj07TZ7EfXswLCXJ773GPh8dEIrfQ2d6DsoCQI72MlCHd651-_QPF6XILap5RTeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
برنامۀ
بدرقه و تشییع آقای شهید ایران در قم
◾️
مراسم وداع: سه‌شنبه از اذان صبح در مسجد مقدس جمکران
◾️
اقامه نماز بر پیکرهای مطهر شهدا: حوالی ۶ صبح
◾️
تشییع از مسجد مقدس جمکران به سمت حرم مطهر حضرت معصومه سلام‌الله‌علیها
@Farsna</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/447662" target="_blank">📅 20:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447661">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28240ed893.mp4?token=LVLs6QTabwFR0PTIqPqDMtZeSFwPU5ySIeOiXXH5XpBi-qzTjN7rQQ6hkB7fJNRHcDA1NNxx1wDRyMOzB03UxFbPpES1k5qu1l67dkGs62gPgv5DlVARm4qoVtfEvlpa1nCjPtEBkcBJohCUFXQj3DfQdndxNZGl8le9wDt8UxpQgxw94K5PG-RnN_jsnv4YYShrMGaUNe9-z-hLpAaLbbsfNCEiOjkRh1zEQwvNuZueMWrtCiWbTvSDDNMDqd5fQLtuwsH1rErskNsGGL7RW9s-JG95QdUdFERLodmbdUtj6lzNycnay5sjcheUgoC-BmFZAr0n9vWwWAQxu5vDHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28240ed893.mp4?token=LVLs6QTabwFR0PTIqPqDMtZeSFwPU5ySIeOiXXH5XpBi-qzTjN7rQQ6hkB7fJNRHcDA1NNxx1wDRyMOzB03UxFbPpES1k5qu1l67dkGs62gPgv5DlVARm4qoVtfEvlpa1nCjPtEBkcBJohCUFXQj3DfQdndxNZGl8le9wDt8UxpQgxw94K5PG-RnN_jsnv4YYShrMGaUNe9-z-hLpAaLbbsfNCEiOjkRh1zEQwvNuZueMWrtCiWbTvSDDNMDqd5fQLtuwsH1rErskNsGGL7RW9s-JG95QdUdFERLodmbdUtj6lzNycnay5sjcheUgoC-BmFZAr0n9vWwWAQxu5vDHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید انقلاب به قم رسید
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/447661" target="_blank">📅 20:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447660">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/234f9e8b93.mp4?token=TY_zOluxhmfdNqOQGFc1SDHe02hPAi7CZkNDREQj_bFSLfTXWlly7kGMukiu-TkohiIjoK-VnnTrKqSwesbmEUCNAFiKSmjev4TFpNfF0XvDlwKLSRcc4K1ikykJnyxsJEUtTT5VMXUUrSEkQ6ZF8UOLze_PCLJcdUEg6mEAGHaC-YU-1Nf7ygXFQ6Kq8j26GfJTUBX73W1Rkq3Va9wJ7O5xvYZVXhv-WH4C8N3gxL6WsyjbeARRuYgBW3B6EyVm3l5feZr3pFVl3om0xqfua9VbjoW9647Y97D_yd3nHuhEitJgKDO-RcunrL9hHG2ewrOcesSQUmOatZq-e1IcSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/234f9e8b93.mp4?token=TY_zOluxhmfdNqOQGFc1SDHe02hPAi7CZkNDREQj_bFSLfTXWlly7kGMukiu-TkohiIjoK-VnnTrKqSwesbmEUCNAFiKSmjev4TFpNfF0XvDlwKLSRcc4K1ikykJnyxsJEUtTT5VMXUUrSEkQ6ZF8UOLze_PCLJcdUEg6mEAGHaC-YU-1Nf7ygXFQ6Kq8j26GfJTUBX73W1Rkq3Va9wJ7O5xvYZVXhv-WH4C8N3gxL6WsyjbeARRuYgBW3B6EyVm3l5feZr3pFVl3om0xqfua9VbjoW9647Y97D_yd3nHuhEitJgKDO-RcunrL9hHG2ewrOcesSQUmOatZq-e1IcSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور جاماندگان اندیمشک هم‌پای تشییع رهبر شهید در تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/447660" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447652">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58de79d79e.mp4?token=aNWUmHvZCiof8S7h6JRXvfYqjaoO8-4OA41fH7LbNbA3stZ0GeZyvO2iq6T0RZP6GXd_QnL6t4655QBbUlS9kMZMnMedKM6QPZcXfTzs6c5V-_qWEYPcNEBm7NxqpAD4moG-M0CupvDxsLXdqwEAfP1UxaBQ2IuOB4F8oWszfn25NAQf7E_727d1du_PU8pxE0djc9kNI5sOLpKS6LLiLoZYub6HF0pAgdISUqaCNL9hdsR_ILhae9nuRcnRJhn7AiX5gBMT8JB086W6ksNx_AG_PKoiGGUjH0TkYWfMApsiE-XNL9crPLeYbOFypRwbyVmA4yv2FHodbckHaBpbSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58de79d79e.mp4?token=aNWUmHvZCiof8S7h6JRXvfYqjaoO8-4OA41fH7LbNbA3stZ0GeZyvO2iq6T0RZP6GXd_QnL6t4655QBbUlS9kMZMnMedKM6QPZcXfTzs6c5V-_qWEYPcNEBm7NxqpAD4moG-M0CupvDxsLXdqwEAfP1UxaBQ2IuOB4F8oWszfn25NAQf7E_727d1du_PU8pxE0djc9kNI5sOLpKS6LLiLoZYub6HF0pAgdISUqaCNL9hdsR_ILhae9nuRcnRJhn7AiX5gBMT8JB086W6ksNx_AG_PKoiGGUjH0TkYWfMApsiE-XNL9crPLeYbOFypRwbyVmA4yv2FHodbckHaBpbSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایی متفاوت از حال‌وهوای عاشقان رهبر شهید در آخرین روز حضور «آقای شهید ایران» در تهران
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/447652" target="_blank">📅 20:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447651">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe680719c9.mp4?token=G2ZIDqRYljxYCvTNpzWtkA5T6p2BUoobRua0MiDVJTaet-FQMnwRXNu9qrROLdxJV_AH7UUW5lhR8m-22wPBigmMGTSVsrfXG1sjv44Gs8NGEhUXENK2lTQ1n8yxeAN8qbzFQ0JgygrjN3DMHgs8l5mQNWjJoyoi7dY5CQ8Is3givxu-RtcD8x4Xwfe5rLMYdpEt-93hiJRDe2Zxt2hnie_4qnuNAGCJi3Wc4DQhA6mkRRv3ZacqrjYhNKF_kmt8meEw_H--4ur-d-4sHtCLWQp7jcHqGPQ7LSEpOv--pFOe3xj4FuTe0cSf8P0XX5QYv5FtlPkCcFV_owRymbJtZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe680719c9.mp4?token=G2ZIDqRYljxYCvTNpzWtkA5T6p2BUoobRua0MiDVJTaet-FQMnwRXNu9qrROLdxJV_AH7UUW5lhR8m-22wPBigmMGTSVsrfXG1sjv44Gs8NGEhUXENK2lTQ1n8yxeAN8qbzFQ0JgygrjN3DMHgs8l5mQNWjJoyoi7dY5CQ8Is3givxu-RtcD8x4Xwfe5rLMYdpEt-93hiJRDe2Zxt2hnie_4qnuNAGCJi3Wc4DQhA6mkRRv3ZacqrjYhNKF_kmt8meEw_H--4ur-d-4sHtCLWQp7jcHqGPQ7LSEpOv--pFOe3xj4FuTe0cSf8P0XX5QYv5FtlPkCcFV_owRymbJtZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیندگان آقای شهید را با چه لقبی خواهند شناخت؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/447651" target="_blank">📅 19:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447650">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0065bbda57.mp4?token=Jlr3LHawkuYpP0W1zbQtxLmJOiVeKt-CyUmMysIX_PeHJZKIIxXKVw0lQLgdJ7TPlXiAstAjVoY4SXvITuEvVzBGk-0tNyPs6B72k4nqMU5rUjNdCqdCxUqPBWy7PFPMzUwxFLl5OmmgEQLteGSSUl05EM7R65bYOP7xG4pGhR9Ti-RISGCWTAekQtj9XHfSbHaEaxVocdSHyIx_7O7NJzTIcTdlFg8Vb1uMd7WIpbhjAECZ-DltLjxPQd5-C_ZXJdU4YKH0lDaqnhgm75rswgNY_nNwuadMncVKf4fbOorEF35GbIaoYjP7PGKHy8X2Lk1B546cLcH_NQ790GCovw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0065bbda57.mp4?token=Jlr3LHawkuYpP0W1zbQtxLmJOiVeKt-CyUmMysIX_PeHJZKIIxXKVw0lQLgdJ7TPlXiAstAjVoY4SXvITuEvVzBGk-0tNyPs6B72k4nqMU5rUjNdCqdCxUqPBWy7PFPMzUwxFLl5OmmgEQLteGSSUl05EM7R65bYOP7xG4pGhR9Ti-RISGCWTAekQtj9XHfSbHaEaxVocdSHyIx_7O7NJzTIcTdlFg8Vb1uMd7WIpbhjAECZ-DltLjxPQd5-C_ZXJdU4YKH0lDaqnhgm75rswgNY_nNwuadMncVKf4fbOorEF35GbIaoYjP7PGKHy8X2Lk1B546cLcH_NQ790GCovw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر ستاد آیین وداع رهبر شهید: از مردم معذرت می‌خواهیم؛ برای سلامت و ایمنی مردم ناچار شدیم پیکرها را از میانهٔ خیابان آزادی وارد مراسم کنیم
.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/447650" target="_blank">📅 19:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447649">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXFujhFooi15CniFRTsxmnOJzS7IlDs0FN8RyOjQIja-A0Qh253DZusfcJHlUtXprvXahoG0uW9ZH0UBU4iBCvr6msHMhfbq8V__5QHgKfBXsjH4HWj2feptEDuJO82uWZzSztqhI4OKYlj2wfPab3RBiqvOwfYbJ8t5yXm8AlsN1KhZXdTKhib626QqMOrGs6Fys9_oRiZt_sPZKQQqxc0wXh3DIUL49J_qn7Lsz4Q7xlgsiXEjOpYGZQ7cFQ-ipyXx_5u-K5_WzuSf-nBKgpNWroFHHUH0lIQ4TS9RGqxe6qLaOWOKZhFGHJxvFAQ3PxjQgJ9TBsyWXJ00DXWl5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: دریای عزاداران در تهران به آمریکا و اسرائیل نشان داد که تلاش آن‌ها برای درهم شکستن ایران شکست خورده است
🔹
رسانه انگلیسی رویترز: مراسم تشییع پیکر آیت‌الله خامنه‌ای، رهبر فقید ایران «فراتر از یک وداع ملی» بود؛ ایران به جای آنکه پس از جنگ ضعیف‌تر به‌نظر برسد، خود را «مقاوم، متحد و مصمم برای شکل‌دهی به آینده» نشان داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/447649" target="_blank">📅 19:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447648">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🎥
حماسهٔ مردم مبعوث شده در تاریخی‌ترین تشییع
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/447648" target="_blank">📅 19:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447645">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سمنان تعطیل شد
🔹
استانداری سمنان: به‌منظور تسهیل حضور مردم در آیین بدرقهٔ آقای شهید ایران، سه‌شنبه و چهارشنبه ادارات و بانک‌های استان سمنان تعطیل است.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/447645" target="_blank">📅 19:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447638">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WzzOq59KVkt1lExnD3LYUm625rgbYv2n1FIlkYdUUKtn25lzn_DkmINrZLf0_lkcCvqcWIqE0btFUnknGOSuipIJ6kHIG9sQIAQd4JI0EXYCP7Q1I8_r-UW_Wb38ElkMNQbmhDskg-gHhNip_jEUZUgNonmqP8ChI9-Vcd1WYBwo-guShcSnNCMNQR1RD_Ck-Uf5NlBREI9Vf56DrA_RyOSHzCGtSm3JW14dRPC4_kiE_KN5v0VMeaWQfRL56XoH3LAsWrvoQSFJSrcTObnm7BmWCTgNp1IbMaIgou-PiuFok88ZLUgaOxgFT645naxKHnVAyKo2j35403JLWxA-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZuyxOomXF71csvyrOpYgHMKM_TI8axA0qpvsv3kvDzZXH-Ntokgo0atpzcBrYOwRyzlasPuhwoIK8ncM2j0akwt50Th17uuZZxiiYWht6YwWUGqd583eN1j1mPueUOtsTlAzESD0-WE5htOiKWumkwqcgVvn7sJUZnNU16X0ZA8YGsnqjfr2uEkQPkefGTW_rUFQDhQdgNje2T04XZcR0Jxh6efQyGBkPp1apBr2aapjluZVDslDIyUhj2eSYGdfxpJ-zD6KekJTDxdFQdL_pJNpG0lapbFZztXgQV_ptbWKx03GjmyZlotuByiEA0b7UWoMuPi2kKBUy6yHdKNJrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m4IPsQEHw9jLYAMq2SJT2nG0yKg9_jVVmLhlS3vzjzGQyBoYUFus5RLWHBXBDkCpvMzX7RN6oi7UfkVdgKbQypH7NsFjdC0coQnt3A-msPvzIbvQjTXCe54Uweio2O9Kp8lNHppaO5T19qUrYbwff7DiWPO0QrgQIBRa5KxS5I6kazFZyx_1WVDdvRzklI4gUNYa_lMYpaAqm7tB2Yoau0bWyqO8kIb1on9oBGgI8TUYtRfvnCizmhA7h6hYwyIMDQwveS3mnUT-2IbeCZSeKI35jhH8TlbtZ_TZEyxrSHQ_m3d1jUhxvI2k-zSt_e-NXmL-0x0bvOgnlwIhQ5Zrdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CkB_Jqi3vNujLYLS_HWv93E1MddvpE9cuCmf43pSrM-iC_5XhCZMOdw8cU8AYos2_X9lK43yDWOxFMYsz_x9jvSGwawlFXaiojAJXRa5RZLJ4egYz0_7r_YvGHp9Jeuk7ER8AUbrHOikOOKpw2r5UWZlKJb70EpZgavGaa7PCxbEpk1fZkeSX4vEltM1JjGBgsKKbhtnkOyzcwFVSEV0srNX539un4tzIqpTBicwv7xUSqOEQ4iDVNt41tpAqsglu0dxD7Cyy1JDihSN5S0KvK4qN7w6SbKs3BUrRJWbNorysVS3N8mHpgPWhwYrtTz8AohXNUtlPLPQ009GEnmaHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RzGbIbRK4pL2eWYMdY4O7CIB1sXNCUiNo765wDGX8cfGb656bWod6pXNTqBGu3BHxA6pIDovtkab6iWlILdhm6_7fsuWrq81vNbVSu-hxi7CepDsEp7C5F7TQLIx7-Au1WskdBBduVuU99_fzNAfZCLlKja6hmOUizZhs86OVsSwuSJaErZEdYg9CDKREkqmXalnQRmAvSNOWRGrL9zU-MTg_n3L-CdQSSXf6ojJp0EkOFYkP7vfRKh75f9CsViIH8JkNAkS072LQtQZ4tF7IaeTeRzCyLiEt5wuf7CsrmehMQpNhtsPc8EjzNat3Jpyre0ULyWNVXURizKB8KY8kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QW0NBw8hmX1pT9Cmbxa_iLTmdM4YP32aaHlIJq87AQc88UDDiDuyigtkXlVVk7BBW3FUGYl_k8KWo8t0PvB3OqAM0AcyNUKcMVxmv1NyZq75-s5KBVTE6dS1IOeuXTXpsqHYqen6oGIVPjml0CerqHZZfzsy5bY_li_Xbowqzxh3lPG3QoigbA89WD1bgEJdilUu5KJuSInmom_yDuZkvTuBr7C6GD7XJrqDyrgKC6D-NHg9A0THRirVy6uDkgByL3gkNdsR9pMYOxnHNFi2psY7xnFaT9ZJ2m4BgHl5Czbtfr7MXhWTDJgC1kTbaiUq8LVCOH8MDNLfdSWmfT1e9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CffmTnrcYkVV6E2yNtgC2nLxlaVQe1pZY1mi2OE0Yq1UmEFlvC8dsu8rVtruZVcaB_vReveXgDW7Cdwx66A6JlF6yRmaYCSPhSgbYqK-ksZ1iqgpIZAvEtZOOhyPmuCGbv0y3hGumIX9EEdd1wZUZrXzfNBwWx1A4hWAK2q8QEgqvHejQBP7-wrS30x2z3XvqY6VD2vBWDYmioKcsxIGIUG2IkCfschpY_YNvuC_vTpmPReh5L_1-SEBqMp8i5KPrW7Ul2FO3Vbrthyr-RCNuaaW26F__tijczDseBO7C8-pi9qfcLz_0kvjD-GfquXU2bk4yMdPtuKKNwxCJl9h8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آخرین حضور رهبر شهید در تهران
عکس :
احمد بلباسی
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/447638" target="_blank">📅 19:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447637">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ادارات مازندران به‌منظور تسهیل بازگشت زائران رهبر شهید فردا تعطیل شد
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/447637" target="_blank">📅 19:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447636">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نقض دوبارهٔ آتش‌بس در لبنان
🔹
منابع لبنانی از حملهٔ توپخانه‌ای ارتش اشغالگر اسرائیل به شهرک «قبریخا» در منطقهٔ مرجعیون واقع در جنوب لبنان خبر دادند.
🔹
در این میان به‌گفتهٔ وزارت بهداشت لبنان تعداد شهدای حملهٔ هوایی ظهر امروز رژیم صهیونیستی به شهرک «النبطیه الفوقا» در جنوب لبنان به ۴ نفر افزایش یافته است.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/447636" target="_blank">📅 19:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447635">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c18cb1906.mp4?token=MSbv3wHDiMxjggq4_C7guknNfrFKnho0f1z3DeqgO4vhlaeekm8INDsTRk6myhjP9B3dQLCIuaEC0sqaAhx1FwghAnZ8jihvbW0vj3iBhesQmgMfCIFS74IT0DvvnOa1u-eM0oXG8BQJD-jBGY-pj4wXJL5bBYqtRQ4avjWA59kN7rOin5AKEKHd6AiwqclbqnWo6udIlYU_ldBt87vumQrHGcnO1cNCKSVFI2bwJux_Cjaq5FpmvL1hxNzRJGknS6edTifz4g6YI1IGDW9Mqt5SQsIfH0AqhjOrXbzfqLIqZgvn6vWd8pJFMtCNbyQiRlQf1yf2kSDA1URb4nlbgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c18cb1906.mp4?token=MSbv3wHDiMxjggq4_C7guknNfrFKnho0f1z3DeqgO4vhlaeekm8INDsTRk6myhjP9B3dQLCIuaEC0sqaAhx1FwghAnZ8jihvbW0vj3iBhesQmgMfCIFS74IT0DvvnOa1u-eM0oXG8BQJD-jBGY-pj4wXJL5bBYqtRQ4avjWA59kN7rOin5AKEKHd6AiwqclbqnWo6udIlYU_ldBt87vumQrHGcnO1cNCKSVFI2bwJux_Cjaq5FpmvL1hxNzRJGknS6edTifz4g6YI1IGDW9Mqt5SQsIfH0AqhjOrXbzfqLIqZgvn6vWd8pJFMtCNbyQiRlQf1yf2kSDA1URb4nlbgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
به‌یاد ماندنی‌ترین جملهٔ حضرت آقای شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/447635" target="_blank">📅 19:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447634">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8W7YmCa3Oi1BLoarZO0MQF-WuOe2j_9av8jIcpGZaexwOUwHOP5YSDNrjvV3uxMCeR0Wc4_AWszisvmlFzSnuSO4sDh-xQRbp6JcYLN58PzlqPP65LtMs02D-v4jxTGe8oUsFXRpML7PFSYpZQrR_AbSzd8vhY_NPGX1Lw40qzblXGu8Gfw-7ryP3PXR3Xt5qt85t4yEGmNMdZ0vAkjKhKWcZqrW9LycDe2c2tJrDGH70szTilKGEapcmKCXFzJWtIOwo4CDsAOkZDGI_Rc90Xsr0CSy-HXgyX_lRjMRRWMNAJKZzTqqnVcLhpBO8_-P_KZhnJ7aG4OKv2VRUE4Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
استوری درستکار، سرمربی تیم ملی کشتی آزاد، برای بدرقۀ رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/447634" target="_blank">📅 19:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447633">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd45e1cdc6.mp4?token=HbdW5z4KKt1x-r-bHdAlpeUBah48ijbTxe45qqxCCqWPdkgJA7AXqbJvTy85-7lhUTGVErDjHNcuSUn0paeJ_0A11v3JmimHg99pmUIYN9UWsa3OTA62IsyacMGa9j0-QdZOXSR3ofZk5xL6kYWXK0H-DWKjp3YgPK1CbZVAMX7CwuRwrrugOVoCAg_qRPxVSsnuS9rquyY4PGKiYltzNauZj0ei0JmEwfGD7kpk_l6Hyl-GhyEPu6KpMSxXaEtsTj1KstcYE839gsy25cLOUYM4j6ucpcVBGBhoy8BdQ9kkR2DL-8rUt42rkgwC8sTIz6Pic_qztc_KpdGN164O5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd45e1cdc6.mp4?token=HbdW5z4KKt1x-r-bHdAlpeUBah48ijbTxe45qqxCCqWPdkgJA7AXqbJvTy85-7lhUTGVErDjHNcuSUn0paeJ_0A11v3JmimHg99pmUIYN9UWsa3OTA62IsyacMGa9j0-QdZOXSR3ofZk5xL6kYWXK0H-DWKjp3YgPK1CbZVAMX7CwuRwrrugOVoCAg_qRPxVSsnuS9rquyY4PGKiYltzNauZj0ei0JmEwfGD7kpk_l6Hyl-GhyEPu6KpMSxXaEtsTj1KstcYE839gsy25cLOUYM4j6ucpcVBGBhoy8BdQ9kkR2DL-8rUt42rkgwC8sTIz6Pic_qztc_KpdGN164O5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حالا دیگر این شهر تو را ندارد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/447633" target="_blank">📅 19:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447631">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTDDrMNYrJ8W82kFMK0ZzmuE-AFsaL3EPzMWIsbx99ELAgSXJ8I9H3DLgslJqBFSAFqOiphLKzXhVH7YPWXrxmRpX6ec-uW1sKtfYfpbQRbNgG3PxSkak4lrZOdGKTEpunEByu58JkmDcHyQUdsFfSIS-faYC6frFcN5_GByHThTZ9BluZf_OPl4gG8S16mT-fdBWyiPuMiJawtqV9Fhg6nbf7cFTdysrKWNMAJH6nOQ2iDA8FL5IzRozUr1P-VJq68ch9G0TlJB--Saj58Pv7BQa46RMZ3sTm361St91al_yuEuJic9rnk4KqB80OjMlB_TUrVlq7b8cjqNporteg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
رفتید سوی بزم شهادت به‌سادگی؛ خوش باد بر شما سفر خانوادگی
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/447631" target="_blank">📅 18:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447630">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f5e3fe8a3.mp4?token=XwUNPqD7mNiUioMrkNejsUQdKnTofLeYh2vSNcRR07AF-6eRiL4SATWXw_S8CqBPb1pDk-E5nUxN707wGnXu5r2I9J4dysxGvqUtxFWQclYNaZuofVIrt_TbnPZ4zSCcd7ZLupcWuc11FHbcnWfBKxJolvqxNZWNmKhLt2YLy5KoKJZNh48z75VAN2sMyb6WmX8PTSlGok3-hUO1-jxPel3hkSdFBCvQXBzRouZp0fv4Q_BVFt1m_l2rI_N21Q7k4h9NH5BkY927Ag4MVyMZIWjS7O7UAqTwLg35pcpJxXOkIcKLLrRZ-xp1hbNXZ9Y7H2d_pBn16M18O07oz5INig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f5e3fe8a3.mp4?token=XwUNPqD7mNiUioMrkNejsUQdKnTofLeYh2vSNcRR07AF-6eRiL4SATWXw_S8CqBPb1pDk-E5nUxN707wGnXu5r2I9J4dysxGvqUtxFWQclYNaZuofVIrt_TbnPZ4zSCcd7ZLupcWuc11FHbcnWfBKxJolvqxNZWNmKhLt2YLy5KoKJZNh48z75VAN2sMyb6WmX8PTSlGok3-hUO1-jxPel3hkSdFBCvQXBzRouZp0fv4Q_BVFt1m_l2rI_N21Q7k4h9NH5BkY927Ag4MVyMZIWjS7O7UAqTwLg35pcpJxXOkIcKLLrRZ-xp1hbNXZ9Y7H2d_pBn16M18O07oz5INig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نصب کتیبۀ مراسم تشییع رهبر شهید در حرم امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/447630" target="_blank">📅 18:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447629">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پیام مهم فرزند ارشد آیت‌الله سیستانی به دفتر رهبر معظم انقلاب
🔹
آیت‌الله سید محمدرضا سیستانی، فرزند ارشد حضرت آیت‌الله العظمی سیستانی خطاب به دفتر رهبر معظم انقلاب نوشت: درست این بود که پدرم، آیت‌الله سیدعلی سیستانی، بر پیکر رهبر شهید انقلاب نماز گزارد، اما وضعیت جسمانی و سلامت ایشان اجازهٔ این امر را نمی‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/447629" target="_blank">📅 18:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447628">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hr2Vh690KK-upwtvZx0ZAwWw7S3n9ZJGur_Y3NMsgkgXDxnAl_M0B2W84eUxErdYpgHWBIhJmbQy1oWBfLKXMXrnAa58lJJbzJrqNvkeXNuugMdA_2kIdg6u1vDC9qYU0vciXyCRMaqjRnezHUr4Pl2l8rhELh9ghPpCx1QCmyjfKkZqdJyqYTAW8Z5JOs8sLcVwt3Z1wMUw_CgruZyxUqDqC2KiizbA7JenVAZxA1UKzwkC--NWrg56d-CsBX1UCd6tR4Z_EBHNZ4lzXb_8Whl2pSQdTlFieE2cEkbKT_vuvcX0F_b8ZUwTo1YIPjUdO64EO8l3_r9uRWlW8wigJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حماس کمیته اداره امور دولتی غزه را منحل کرد
🔹
دفتر اطلاع‌رسانی دولت حماس در نوار غزه امروز از انحلال کمیته اداره غزه خبر داد تا اداره امور را به یک کمیته تکنوکرات منتقل کند.
🔹
دولت حماس با اشاره به اینکه اقدام مذکور در راستای بهبود وضعیت داخلی و در راستای منافع عالی فلسطین است، تصریح کرد، هدف از این کار، کاهش مشکلات ساکنان غزه و گرفتن بهانه از دست رژیم صهیونیستی است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/447628" target="_blank">📅 18:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447627">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gb-4d8E4NX9Zbx4e24XooIUspBS8PuhHw-fdVEnSNmXlkdLL8SDbaEOZ97t5QqrkUlvm6Qu6fYufON3X1jMHanOx9--0wawenbU0EdtdDCv2Z1vOf8z6ayZxYacoDbL8Lz7ktRVifP6ItvjioDHgU-S7vPeo4eS0INbsMJVeOtFYcgLuFlJUGStVPYP3HmcOz4SgUk66YLBwmvG4ZhsDVjZgtN6J_6UI-vZH0ieDRRKH6mabi-XFRjzKo5QCW2IAJaYwMzprNebKaV54rZemLOHnatF6jJB9YHcyB-zVJIakbFGmuf_fO3EazhcDgEF_zNM0o3UC9KUbMqk93VSWgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
استوری مهدی ترابی، بازیکن تیم‌ ملی فوتبال به‌مناسبت تشییع رهبر شهید انقلاب
🔹
ننگا به ما اگر که ز خونت گذر کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/447627" target="_blank">📅 18:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447626">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/309edf5817.mp4?token=CUrpwcvTgyw8uGlPY2slMooHIuVBHSzhZAIsL64Znq3BHre3VSQcXQkb8QRixyJ8GeUyMZLUGh_RMcLz1ZOtP97sqyBNZoG_QPQd1i7CkOJPlAW1UXjnWyx0ZvLsdXwW3s6vTfXQ_FeTUd1r8i22U_vD37sbfBTJ0ImmaSi9LTwj8l9zJLrp3ZyfU-U6i2iuvHFx_RVuYSCZPqwhu_C3m1TQAHv-LEhfeeBLsQu4F1W86uaqTnw41XfbD8a7pRcQ00kjFN_ZYDccUgy2_XIo16sL6qL0cnunjMLCkW5PTcPtHbfXo3aL5Np47sxffqSrIykuGBzCwDTW8_VH_MIKZTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/309edf5817.mp4?token=CUrpwcvTgyw8uGlPY2slMooHIuVBHSzhZAIsL64Znq3BHre3VSQcXQkb8QRixyJ8GeUyMZLUGh_RMcLz1ZOtP97sqyBNZoG_QPQd1i7CkOJPlAW1UXjnWyx0ZvLsdXwW3s6vTfXQ_FeTUd1r8i22U_vD37sbfBTJ0ImmaSi9LTwj8l9zJLrp3ZyfU-U6i2iuvHFx_RVuYSCZPqwhu_C3m1TQAHv-LEhfeeBLsQu4F1W86uaqTnw41XfbD8a7pRcQ00kjFN_ZYDccUgy2_XIo16sL6qL0cnunjMLCkW5PTcPtHbfXo3aL5Np47sxffqSrIykuGBzCwDTW8_VH_MIKZTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: تنگهٔ هرمز یک ماشین پول‌سازی بزرگ است
🔹
ما امتیازاتی گرفته‌ایم. اکنون ایرانی‌ها باید به این امتیازات پایبند بمانند، اما سلاح هسته‌ای در کار نخواهد بود. ما قرار است مواد غنی‌شده را تحویل بگیریم. من به آن غبار هسته‌ای می‌گویم. من دنبال تغییر رژیم نیستم.
🔹
نیروی دریایی ما بزرگ‌ترین محاصرهٔ دریایی تاریخ را رقم زد، باعث شد در طول ۲ ماه حتی یک کشتی هم نتواند از تنگه عبور کند. و سپس ما محاصره را لغو کردیم چون به توافق نزدیک شده‌ بودیم.
🔹
ما در هر صورت پیروز خواهیم شد. یا توافق می‌کنیم یا کار را تمام خواهیم کرد. ترجیح می‌دهم توافق کنیم چون نمی‌خواهم زندگی ۹۱ میلیون نفر تحت تأثیر قرار بگیرد.
🔹
ما می‌توانیم پل‌ها، نیروگاه‌های برق و تولید انرژی آن‌ها را در مدت کوتاهی از کار بیندازیم.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/447626" target="_blank">📅 18:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447625">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/559e520b6f.mp4?token=RXiyArXHK3icTOaaEpfT24Ug9-bY2ERFpSdw1C9r9h4AIJaCdDkli8B3Fil1QplM7qcCxBo1KJo2ou4r1JQ3AMLJuZGD4_ZNlXuFuoDl1x_TBp9_FTPdEu26XoWhoGDdvUvCFtlwoAE4KDjzOmsKO0CgusDZfyLtJSdiY6Zy7uR7WTphELtURhVckkEZ2Ez3FiorR4VILnOfTm2ZObrAf8H0LGtC8ewGLr6TTXu13sMs5WKPV-EsG_H7dUDNBYIvk9gcKb4LNSTfA4WZD9iTlCzw84PjTxIXMEHwVsRlqvKK8lAKXxq7vfRPUzy4lLlSW4LBoL8A8Rx0e8zs6Z6_mj82gTFMWK1NV30emx1Pd2R4_mmvrMIXXJn3VdM2Bg8F1F0Yd7OZJHYhmqUVRZj5HIdTKZ1hOJ0M8B-Du9bzff0ZME-GT_9dh1ceFgJN0w83CjSMe_lrqQKm5ImcOIqaKjVzCaVx6CeOgl4P-DpAdvGH0pN1UArxm1J2R4QPweFgktSvFCqZMYfPFzsmPjBbnKBXKckvkXaWWXskQtEvzWJhJTxKOpjaQPeMEThPNXfpXhY4Apt7io4uaNR11IJcUpELk1ecdXDeuVmmyjnmNuaY6M_9SnO9H_eaZ_bDpFkmmjWPJHY3Cu_n7R1TEFgw3PMadNh9E6VLGqW-k5YkadI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/559e520b6f.mp4?token=RXiyArXHK3icTOaaEpfT24Ug9-bY2ERFpSdw1C9r9h4AIJaCdDkli8B3Fil1QplM7qcCxBo1KJo2ou4r1JQ3AMLJuZGD4_ZNlXuFuoDl1x_TBp9_FTPdEu26XoWhoGDdvUvCFtlwoAE4KDjzOmsKO0CgusDZfyLtJSdiY6Zy7uR7WTphELtURhVckkEZ2Ez3FiorR4VILnOfTm2ZObrAf8H0LGtC8ewGLr6TTXu13sMs5WKPV-EsG_H7dUDNBYIvk9gcKb4LNSTfA4WZD9iTlCzw84PjTxIXMEHwVsRlqvKK8lAKXxq7vfRPUzy4lLlSW4LBoL8A8Rx0e8zs6Z6_mj82gTFMWK1NV30emx1Pd2R4_mmvrMIXXJn3VdM2Bg8F1F0Yd7OZJHYhmqUVRZj5HIdTKZ1hOJ0M8B-Du9bzff0ZME-GT_9dh1ceFgJN0w83CjSMe_lrqQKm5ImcOIqaKjVzCaVx6CeOgl4P-DpAdvGH0pN1UArxm1J2R4QPweFgktSvFCqZMYfPFzsmPjBbnKBXKckvkXaWWXskQtEvzWJhJTxKOpjaQPeMEThPNXfpXhY4Apt7io4uaNR11IJcUpELk1ecdXDeuVmmyjnmNuaY6M_9SnO9H_eaZ_bDpFkmmjWPJHY3Cu_n7R1TEFgw3PMadNh9E6VLGqW-k5YkadI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خون‌خواهی؛ بلندترین فریاد مردم در تشییع رهبر انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/447625" target="_blank">📅 18:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447624">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59aaacce4f.mp4?token=fr3zgN9zckXKG7TXPWMNf95ZooFXQhy9a5mApao7yJwGBm7_Xd7_1hRHSBYvJE19hEXfqB3H3A5fqoEmnywJ9hC6LXeivpBOWAv9khKHFmEFtNT582ebEUntE7pb88dbMTHlFMhke8JOPs2GXPTEbjaIznxREIkvwUBOGbBC6hj8bNcdHfUkJQtJBewGKU119mzn8PaJKRxbh9eJoiRKn6WlmJj4t-jasKrF83tK-XVN1DZgaG5MU6AmydzDNxMvYuUV6nIib1tBGmCXGSqc_f8lI71pWJ3AJ6tzzylLBDL32AImyKVPEBpqpNhMoyxN_qKtCV6n8D-uZ7Dzzgn-yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59aaacce4f.mp4?token=fr3zgN9zckXKG7TXPWMNf95ZooFXQhy9a5mApao7yJwGBm7_Xd7_1hRHSBYvJE19hEXfqB3H3A5fqoEmnywJ9hC6LXeivpBOWAv9khKHFmEFtNT582ebEUntE7pb88dbMTHlFMhke8JOPs2GXPTEbjaIznxREIkvwUBOGbBC6hj8bNcdHfUkJQtJBewGKU119mzn8PaJKRxbh9eJoiRKn6WlmJj4t-jasKrF83tK-XVN1DZgaG5MU6AmydzDNxMvYuUV6nIib1tBGmCXGSqc_f8lI71pWJ3AJ6tzzylLBDL32AImyKVPEBpqpNhMoyxN_qKtCV6n8D-uZ7Dzzgn-yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم! آقا از تهران رفتند...
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/447624" target="_blank">📅 18:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447619">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmiA_Qct5vTniXJAJaqLtGqo1mVdxwdO5hMapaa_NPcyoL69yKg8WCF5r2NrH0g-JIiJzCsvCubQnCUykNK8qMTJZwTYGWtVJ7U-OmPnG53YLL-JubjDeikOqkFlrJr_GmJBms4LfkLLwPDmbxiLcf4IOxbHTYzRr52EEfYHuuEXtAYXFtVMY11KyZRieAY4wcwksHVVaMTIJ62AhEc0665KgfSNcX7T6o87ctFGbtBXeTmlCaH63JLtHocjKzaheNcdeAuKeZHkSI0ZlZqr8LStWNaDHHSeKpBhFFk5nTQ52Ipo5m_sS0ZDRNKM8FqFJQuEmbVYdzYwMPDH8ThSZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ffaGgtGg4-Y8E-f8RavQsBeEutBe26db3OWOe8_lxKLjO7m6n9Uy8J1ME8qIbBlgQjdqxazk6Pk5xzmSO29XhyI9lPgDUuzyKcWLuxuez106Fb0vf27MvVwQ9cm-89VC_Zjr5W-DGOU0fXtrYy3aL5pNMY3G6Rwq3Po4QCr9Mgf0fYxjoBP5q_x6pPHUnPcbOsTXur43Jh3yRBhgKt8UeSLr4CoKoj1xdn3QH_DawxTjmSdq_6hQn1_5olmQ3Mr57GBlslB7ih9P64ULYDiboamlOEnKOo5noGoNwuW3yQUv24gR0f66kziwdD9JLHTW8oM7sQo6TsoJIABPXMmiHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uN-t2kjf6wg-tSfuV3NWDtXxL_VJUCmgcW3lsooouj998jNSMIwkatXcWlRTSg4XwlZc4zYQ4W9J_qbJ0FGimEH89ticurMXz03jSu94lyY_d6yxA_u1JBAZOHcRs6D5Pc3Mswol_phtEF5rv4w0GQZ33z55sbHM7kFxKGyIZdQj3cS_gQDbGDKN1CqrmvbS53I_acXDdhYM3RJB6MDr3FL98mcStO37Jp5d2CZ0EAbDBtUA_HKgzyFt2JgaqF0Ne3CZeWZNagiSWOTXrKKloQK71b6-ooy8IKxrDQvR1zhqrng6AiXIpg8KODbjuo_XytUvR12-Jwp9583fOKr9EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jOSIohxyuPDxoPOeLk_NFbWzhTb6NaO41UR6N4rZg76jwt4VICVaLuzSsPo-iU1eZa22O8HUhhxo5tYplKg5oJhbUX_0x4O2uQs0eEaKra9Q0Lzz50DKosHwox-yivn0R8xoM5HxilsQqOq_AKfU4EiCD-Ocha4KRl0hfRoP5n9S8D9yVsSFzfGtJ4V5Jb-x_AVoNONtTtcfi7HVOppX-s-vpatJDKJHWTEvUX6Zk5GlBumq4Jk5IgaIbIyvcmCyBEKOtIuts9bVj16LtlG5Pfk6GTTxc-Q2sI04g3OlyQ2EGSqqiNBYr8zHHwGfgLIm5D378dQIIl_3SAjEFD3PUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bY68LBftc8MF7B01vy6enWl-r2qIh0DeY8Yw_7cjXfa8h7Czzz2Zcx4y8U5m-Hd5kZy5zAfCXC8P1MyxhMkIzYLiS5KNdxNRCwOJ0qhoA14YJzTywUU0HA45XITH7Xve20C346BWryiNaLbzbGfKR4U1Oc-bMpopRNFlJYGTUnm5a4Nb_us2kelw_VUvxidYn-yqv6JCOl56uk0FtcVYVL-e-9xFlb24Gc9HZbihKiPgNOS5Bn0IEAe3SleivB_Bj3xHK5v9syxd4R1iF0IUquz4_76GuXeT7HPdS7q5ZEShOp1IT7j6qWzpluBKZtXYK469qqDULpJPoDN__8rC4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وداع یک ملت؛ تهران میزبان باشکوه‌ترین بدرقهٔ رهبر شهید انقلاب
عکاس:
عادل عزیزی
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/447619" target="_blank">📅 18:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447618">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5e4aae075.mp4?token=vU90c7Q5vN2LkGJ2JioHSsx31mhln-Y4pq7QhCYdzjR9KdCZuptt9BqBURRxhcpi9TIb9LNFrLFZj1E8sEa_iQSdCnax8fbcRz2OKatiWYTCRRMTnGUM6i2mrh2_U7dyFja16jTugr9EIOOQ8QAgHYDjq5vtlD0fzeqpxnRHuPIcTQEBGLBRbvAGo1UQR8PDnJ1ECHmn43CgE1OViyt9NN7MSJz0ndOh5tIHTYbSvyRbWBKmsz409InDrh4l6BfrPnS51LRFcULhdvJ_XTyE1Jp8lCOH3yHAZAaonB7Mc1EqMYMes_VkGhdiNBujTdY20Sp8nLTHfHczgf_NyKqqiiyE_m-xOpuofEhy50q201IY8vKLVUDeGYSQ8i5v0Qy7ptYya3vl1-Koy9e9tGJC6Bq4AuOyKjIiDSGlfZoT0zvO4KhMSg5KmgZHbkCq2heksI8B3DdXpksj4qJz9DEVdW0Q3AUIk21d1NTV3bdL5DSMEt7pt4JwpfcUL-2TipWLu-mxY-3I0TFVSPL0bga-VG6l78XNiG8fz10w3J8lhOXX0dU-sBBq5EcQ1aY63Nc6rXVQfMxamchGbQhIMCFmP1RO1OxQj_A3Hkh4E2_x0KnO7-xQUo5kKW0ktUpat9TuhIjvtDkJu15AwfQqRDEJkviu_EfCTI5N3FT8uwcJQdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5e4aae075.mp4?token=vU90c7Q5vN2LkGJ2JioHSsx31mhln-Y4pq7QhCYdzjR9KdCZuptt9BqBURRxhcpi9TIb9LNFrLFZj1E8sEa_iQSdCnax8fbcRz2OKatiWYTCRRMTnGUM6i2mrh2_U7dyFja16jTugr9EIOOQ8QAgHYDjq5vtlD0fzeqpxnRHuPIcTQEBGLBRbvAGo1UQR8PDnJ1ECHmn43CgE1OViyt9NN7MSJz0ndOh5tIHTYbSvyRbWBKmsz409InDrh4l6BfrPnS51LRFcULhdvJ_XTyE1Jp8lCOH3yHAZAaonB7Mc1EqMYMes_VkGhdiNBujTdY20Sp8nLTHfHczgf_NyKqqiiyE_m-xOpuofEhy50q201IY8vKLVUDeGYSQ8i5v0Qy7ptYya3vl1-Koy9e9tGJC6Bq4AuOyKjIiDSGlfZoT0zvO4KhMSg5KmgZHbkCq2heksI8B3DdXpksj4qJz9DEVdW0Q3AUIk21d1NTV3bdL5DSMEt7pt4JwpfcUL-2TipWLu-mxY-3I0TFVSPL0bga-VG6l78XNiG8fz10w3J8lhOXX0dU-sBBq5EcQ1aY63Nc6rXVQfMxamchGbQhIMCFmP1RO1OxQj_A3Hkh4E2_x0KnO7-xQUo5kKW0ktUpat9TuhIjvtDkJu15AwfQqRDEJkviu_EfCTI5N3FT8uwcJQdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت جذاب از حال‌وهوای مردم کربلا برای بدرقهٔ آقای شهید
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/447618" target="_blank">📅 17:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447617">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa6db0b54b.mp4?token=WXeAB9MucN8GgO1yL9l9Gz35VdYQj-QcNiSxy7Z_vWH3G48gbXZ9GiQZU4zo9kmATczJVyfsdZi-H2j2qs4sqVvwneKZVP1kQ1pkt6FwDzZWS72GgnBTtEm-LQVo1R0WBN208lUT2lHQdL8Jvhzq_bo2-x0g8I5I35eWfqtbNfyH3ESANWJTNg2twJXVkc_BZqysg8l_mMcSIMbEtRuRNwQBszktwR7ms5wk_N-ggeq6oPRnE_5CZrZJca2X1m7cRkT2XzRbdLaBhHeGLDjueeq4J9oGOAbpj_HBPTbVNbizks9u0zt2cE7E4A1mgKAuLPnIkPpOOhL0nBTwy1rWOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa6db0b54b.mp4?token=WXeAB9MucN8GgO1yL9l9Gz35VdYQj-QcNiSxy7Z_vWH3G48gbXZ9GiQZU4zo9kmATczJVyfsdZi-H2j2qs4sqVvwneKZVP1kQ1pkt6FwDzZWS72GgnBTtEm-LQVo1R0WBN208lUT2lHQdL8Jvhzq_bo2-x0g8I5I35eWfqtbNfyH3ESANWJTNg2twJXVkc_BZqysg8l_mMcSIMbEtRuRNwQBszktwR7ms5wk_N-ggeq6oPRnE_5CZrZJca2X1m7cRkT2XzRbdLaBhHeGLDjueeq4J9oGOAbpj_HBPTbVNbizks9u0zt2cE7E4A1mgKAuLPnIkPpOOhL0nBTwy1rWOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تارا اوگرادی قهرمان ایرلندی
ناوگان صمود در برنامه پرچمدار: مشت گره کرده آیت‌الله خامنه‌ای در هنگام شهادت برای من نماد ایستادگی و مقاومت است
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/447617" target="_blank">📅 17:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447616">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2xaHFna-re32QI_MF7dFPD29e8_wBtTSzinR1GtpYFrErQuoNi1aqOqNprwmK2u-FLyFWh0OxwkUa9tbn8Yn_SaYBDTdKrWT0zCuNDfo0SKXfXJqueL8Zk0Hp20HxwodruKx5GnwxHAmfwYqnDMw0T7Eve16OiZFvqB2YL8pUlZ23eyyLp92K6kYyeO02heSkFiesXcKRDcdaksgslzE97TlLRi8Kv2-eZmG2SE7TlVA6wz-dMZUH2L4eJaEAaXMHsqLXAbUEVWKaC1A5ewUMoEnd2FKP4DJ3nUeTOVGbOTMJmYIZWD9LXbAt1Ls1yzSCD5aNOIL_s9irk1RsbOvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پردیس احمدیه: ای رهبر شهیدم راهت ادامه دارد
🔹
پردیس احمدیه، بازیگر سینما با انتشار تصویری از تشییع پیکر رهبر  شهید انقلاب نوشت: ای رهبر شهیدم راهت ادامه دارد
@Farsnart</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/447616" target="_blank">📅 17:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447615">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9065214fb.mp4?token=W6efHQDSs6QiQSY9OsYC-UYo-pOx1XICR1Wa1WMD0RhtKdZE54tRgLIi8ymEf6khlunjZRAcQBTkKScpbgmtcQYaVK3d6XPD5tZBYuXigzFivl0uipBv7aBqm5qAqHmdF9ixuQ-n1Vf04Rcmx1xFZ7gh-PbkCS-TJtgbK7aPDPAoRVXJq7QDCNCtkyVt5M7ZOgiv9bTm14YUaoES-_kl5gtNmj_t0aBe5SNGBhTNtfCfNbzQVLbCHHvpZta37Sh-fKLL-Ty7iC_Idx_Pdh8rT10AAvejirGPlXLLcpo5pO1WRgUOFKCbEzkiTMR7NWIIDWs9XADVr9YYH07h6CV1nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9065214fb.mp4?token=W6efHQDSs6QiQSY9OsYC-UYo-pOx1XICR1Wa1WMD0RhtKdZE54tRgLIi8ymEf6khlunjZRAcQBTkKScpbgmtcQYaVK3d6XPD5tZBYuXigzFivl0uipBv7aBqm5qAqHmdF9ixuQ-n1Vf04Rcmx1xFZ7gh-PbkCS-TJtgbK7aPDPAoRVXJq7QDCNCtkyVt5M7ZOgiv9bTm14YUaoES-_kl5gtNmj_t0aBe5SNGBhTNtfCfNbzQVLbCHHvpZta37Sh-fKLL-Ty7iC_Idx_Pdh8rT10AAvejirGPlXLLcpo5pO1WRgUOFKCbEzkiTMR7NWIIDWs9XADVr9YYH07h6CV1nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زائر لبنانی: تا نابودی اسرائیل دست از خون‌خواهی نمی‌کشیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/447615" target="_blank">📅 17:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447614">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13492af301.mp4?token=sVRX0cQHqBG9yOSDvjX5jxZcZ9EXkBEZOV-cdz-x5moOwYiTCYWgfRfh0zWFGK-9zyji92BXK0lcHw34EoPPvoa4L50Q7KlgWWkG8OyKO5PAaiu6i9l7PCA6ikHTiAO1GVDMr9lJc4KoYVl0mEaE9_9yOLFQTVRhaUoDtlPYGfdsk7MLzU3c23l_kEVJTtjV41qqTmEoNz1r--jegKqjToO9gW0I4K6Ndgo2GY36CT2Yg6_dkcFShoKOhonAGLRKyrMM6s6pl4YSfYX9c89fvFRF2rhPzh1HNUF1IalrvoGMO9CZf3fElLCjzoQ2o-Fw4gn4yChrPkjaEFo2VDmzkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13492af301.mp4?token=sVRX0cQHqBG9yOSDvjX5jxZcZ9EXkBEZOV-cdz-x5moOwYiTCYWgfRfh0zWFGK-9zyji92BXK0lcHw34EoPPvoa4L50Q7KlgWWkG8OyKO5PAaiu6i9l7PCA6ikHTiAO1GVDMr9lJc4KoYVl0mEaE9_9yOLFQTVRhaUoDtlPYGfdsk7MLzU3c23l_kEVJTtjV41qqTmEoNz1r--jegKqjToO9gW0I4K6Ndgo2GY36CT2Yg6_dkcFShoKOhonAGLRKyrMM6s6pl4YSfYX9c89fvFRF2rhPzh1HNUF1IalrvoGMO9CZf3fElLCjzoQ2o-Fw4gn4yChrPkjaEFo2VDmzkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام
پناهیان در برنامه پرچمدار: در تاریخ اسلام شخصیت جهانی مانند رهبر شهید انقلاب نداشته‌ایم
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/447614" target="_blank">📅 17:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447613">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آزمون کارشناسی ارشد در روزهای پنجشنبه و جمعه ۲۵ و ۲۶ تیر برگزار خواهد شد.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/447613" target="_blank">📅 17:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447612">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55393f65b4.mp4?token=WFjplgX0GYrVRLaC-sstpz50JfL0I2PSfPJtshLC3LCr5C2hjJonA77AlC4jae1ZxJmM0dMbSLqqp1LT6rPDPMuuCY5dBazok9099P6DQkmL4PsumoUXvviXYI3Vc8Czfn_PlW4Qwg9OUTW45H6S6mIf4JuDTAWlMYe-V0FZ2rfZekHSdSaBW_anE927-KiENJLhvzpHG5r8WNFs9yLO6vU5pqSpnW0bfnowj3krlKvLEVMMgJOU4t2gbiuVkLknS2yFsQb9L3epjEL21DsbNS9J8B4s_yw3JtXMWp6kFTYG1xIS2WLasvFNfrvdYo_lOe5nzfCd7rQhVJ9iK_WlPV-vzDXNJC5d1oms6ECQxXa3CGc2ngiL45PG8W6SeAmyq3MsFGASUMCJYFLVoEkw0YexuUd3TIA-Cx60nenSWQfOadKpJ8rb7LUOZe0LE1K-xIBhih8BPSGcrkUY3v7eMjlkyG9AfH3buceraEhYNK4ZX2KTwUQIfs-BPY0s-crgK2ioKOEKyzzNcL8yjaJaA5Ra3CG25pgYCjpXTOpSPsDDCK91FvANq6_mP8mMJIygVstJvfOUuVBaOO6_HLStevzFk7Sn4eHncYwldWQ_ihiU5SaR0Fv2txQ5CgaZlIjOuSQoaNtutj1E5eRNrVHP2_9sLvK8Ce0-1JVpUgnsjMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55393f65b4.mp4?token=WFjplgX0GYrVRLaC-sstpz50JfL0I2PSfPJtshLC3LCr5C2hjJonA77AlC4jae1ZxJmM0dMbSLqqp1LT6rPDPMuuCY5dBazok9099P6DQkmL4PsumoUXvviXYI3Vc8Czfn_PlW4Qwg9OUTW45H6S6mIf4JuDTAWlMYe-V0FZ2rfZekHSdSaBW_anE927-KiENJLhvzpHG5r8WNFs9yLO6vU5pqSpnW0bfnowj3krlKvLEVMMgJOU4t2gbiuVkLknS2yFsQb9L3epjEL21DsbNS9J8B4s_yw3JtXMWp6kFTYG1xIS2WLasvFNfrvdYo_lOe5nzfCd7rQhVJ9iK_WlPV-vzDXNJC5d1oms6ECQxXa3CGc2ngiL45PG8W6SeAmyq3MsFGASUMCJYFLVoEkw0YexuUd3TIA-Cx60nenSWQfOadKpJ8rb7LUOZe0LE1K-xIBhih8BPSGcrkUY3v7eMjlkyG9AfH3buceraEhYNK4ZX2KTwUQIfs-BPY0s-crgK2ioKOEKyzzNcL8yjaJaA5Ra3CG25pgYCjpXTOpSPsDDCK91FvANq6_mP8mMJIygVstJvfOUuVBaOO6_HLStevzFk7Sn4eHncYwldWQ_ihiU5SaR0Fv2txQ5CgaZlIjOuSQoaNtutj1E5eRNrVHP2_9sLvK8Ce0-1JVpUgnsjMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آماده‌سازی جایگاه پیکر مطهر رهبر شهید انقلاب در مسجد جمکران
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/447612" target="_blank">📅 17:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447611">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4adf4cb623.mp4?token=LnubIs8PfUTga4FY0IoXuIFZZxGR4ICbb-VEbax-4Z0YMsB8-4OS77Ddd2_itysVFMXDd7-uJ3Xr01PFgXMI88wiZ-99i6AkHjNdCctTKidMmeLYMz67EIOAP4pM90yTLb7jTv0OyJ3wDyrSU1-GRfNfeahN0_2vB2vbvPnsD5C3CsUKI0VUmE1KCJvpthsZu6WvL0ZrdCKwJduOzTVbB4Paji3MsVAHXuqK7NhWsfu7hbU5Dx-vd_b0fISpFgqGDMRoqrrlUuvdM42Fs_8iLKS7mJEylVCS6xF-wEm16yCMHMomWYfQL-p7x6yD3T_nktrxp9hXjbjiByfRHA2qXRL9ZaeN3J6hwdPchKb5GbRuXvhtSnYdnrmCZmL02flaHa1EW52APnkrQZpKi_toRqvQCEMaBT85z2qN2wxdCyuiqCA08Rx_Nif1yxXMc2vaqh4jv25lV1Gnp2UUv_TZDqlCC456Yj12QL2yFvCW79kKwGHfBCX4PC_fsuGqszrFidBuCJtxssNRWUImgj7akrV-HsCHPma9StmZf2QZ1Qi8uL540D1W3HrMjFJys4UdezPHCQuG0rTSXZJnotnTHawYvV2d5iY9Nkbrg6GXBMVgELzdG6MTJBZLDoohI1c-A25PEg6_3w2OpHvSTaGeZ0cIGa8F6tLjlfdc2vrQ4js" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4adf4cb623.mp4?token=LnubIs8PfUTga4FY0IoXuIFZZxGR4ICbb-VEbax-4Z0YMsB8-4OS77Ddd2_itysVFMXDd7-uJ3Xr01PFgXMI88wiZ-99i6AkHjNdCctTKidMmeLYMz67EIOAP4pM90yTLb7jTv0OyJ3wDyrSU1-GRfNfeahN0_2vB2vbvPnsD5C3CsUKI0VUmE1KCJvpthsZu6WvL0ZrdCKwJduOzTVbB4Paji3MsVAHXuqK7NhWsfu7hbU5Dx-vd_b0fISpFgqGDMRoqrrlUuvdM42Fs_8iLKS7mJEylVCS6xF-wEm16yCMHMomWYfQL-p7x6yD3T_nktrxp9hXjbjiByfRHA2qXRL9ZaeN3J6hwdPchKb5GbRuXvhtSnYdnrmCZmL02flaHa1EW52APnkrQZpKi_toRqvQCEMaBT85z2qN2wxdCyuiqCA08Rx_Nif1yxXMc2vaqh4jv25lV1Gnp2UUv_TZDqlCC456Yj12QL2yFvCW79kKwGHfBCX4PC_fsuGqszrFidBuCJtxssNRWUImgj7akrV-HsCHPma9StmZf2QZ1Qi8uL540D1W3HrMjFJys4UdezPHCQuG0rTSXZJnotnTHawYvV2d5iY9Nkbrg6GXBMVgELzdG6MTJBZLDoohI1c-A25PEg6_3w2OpHvSTaGeZ0cIGa8F6tLjlfdc2vrQ4js" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفت‌وگو با  اهالی بازار کربلا در آستانه بدرقه آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/447611" target="_blank">📅 17:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447604">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JuAlyq3N9lHWqH8xPV1cT_KXzlQOrCo_M8oSpchY7kFJJx-_7MS7a3ltInIM_M0vD2SE8tB38qKXxrEkrNjc_nNbfpKefnlhuGlccJ5TmaU_XShAMFjYTuUxrkP4h2fMpUmDFXH_Y6qBZIYXpJwtmKd8RquetGngu9YYjZ62hTLGEIqppqaNtKAE3OLR6DSt2dwgYQwdh1pvVgp4jfPMYzzPQdBHXx7TUF_wYP0GG7onb8Lbgfnunx0qfZN01qtITpIzMKHvS-6RIDQJ50JDTkbTo6X9Baq3deI7ehO_KhVUu9yTr3GDV0iNJjFdQyxQgxQwwIyQ_OtUsU5TK1P2Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQib_V58LoIcPpW4aarDBYnia5bHKwMYGSsnlBEaNfxSZpifEej9Tw_lRPdoPClA8Pvz_ec5o2xEBNvYVl3tBw05GLxD2Ysx3pfV5O3DyinrYOiom-EMVMgzg6Ld8St7sLHerPZb9o5IMbC-FOfJVJk_-ajGiKcQrXrI-fNayYXao6Dil015dkNPmOIyfN6BrptIMxvqyWsG4ZPenAiAzYpzsR8lCA1fHMIZz8jqiZWljTHAX_-u9Ld-toX46nbx6lTULvZOH0U_DNoPHoJXgKqWkyjgFtEvEDlrPkpTjms8yS7T6HV4ApETithJbFupLkZS9Ebe_wxzHp02SJ09xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AzJDh9LpfCAPvnpEqg3ogT9OedvQNuO29a0UidajgVlnRh_nhFOawX4jrlwkB5spS1LT7DP251kUZ9pnMPkjW5E2pOotuxSDmguaW9X6aQFMoKjhufO3qBnvduQhZbGSg2fjPOQHdfr7boi8apCpHf1ujSCFGTtKKEDb8XBY1IpmPCxi7oaitUROvksYzuFqvqEw4stF7oPkY_EZOdqvMJzLyokWthxC3PjrTWh0w8PV8Su80HxEdL3nqaDANhL6mQuuvlow1UTF6RoutV6os1ANpVpAAcYIX7UUkpU09quc4FGdzVav5sF4mB0DnI8ovY24coBh2FwR4NqzvGLtxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eTaNXl7YNbtNagGCtosddvZbHiU6TQ3sIymhq43TAN_QcHGUJXNaKFo2pneeqLg92VoHgmCP_fSqSq6ao58Jy6oePxkQhSANNk94ENX_UHR0QBkiOZT-mO17uovVlyhU2RIOWtxvbu4LMDss27__0scIXrgH2SQxoCusjrKW-n-5XNvuecv3QKFpw_v3Ot_vWr02QuK2KB9hhVRYGHScJ2MQ5e9LlNGqJa3m3MoDMB_62LJyZsw3_MMJYAFlcSgJff0qzx11N8O10PGLCx_LE1cb3mPPSor3sVmVla5Wuiucc6m6n2V9dCcMFyES-N0cyGnF2fosoG8yyxs1mEoC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTlEzfxkPuGDNNeVchqw8x4lmVpxo8CRryLmtZW7kSU0KS4fS5chV1Z_E6FoK4Q6YkSK-qnSU-SHDIqjQ-rSr0uutWj4RoV8zCIkF9llv4MpekAvl9bkh7v5mdpKa5ewUPQh8EjBFHzhBSLL-HmgKitlev4CYI4TlH74Bys_jvH1yAHRXpuRzrdPAn1Bk8uKxIQOvNwp6A0VdSUuEU7OWlyIHaYN24puq58oKGTZfVvtNiG1HBnrSQLhPG1CoCVGF-GSHd6RnAGRht62VBoySDD9QzZg43XbHYGJPll3Pj0OmfBxSGS48S5ll1_imPRh5S9G8FN08pn5QreOSavehg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T9M99hCwRuXgGM2faZDO7vWeiya2lSN1Ta1TLhF5rMEQCVSKJ50nVO7hnVOpqaZpSQlfzTO_OH25QPNBLrOloDWr1KTKJ4tWaMA3ycAQBWthUqBmdg3ArqAeHi4s32T_OaZ8pqQW6P0ohyTFDAL5LrIt1bEmv8LPFqd7g15xVTgil3cJt67E3xH_6D2QpV75Pn9XpXBOOFenO75XBJ2sOVHtrUHnKaQnxGOBB4aOV1wAX3AB29Mz505alE7mchVuiMAZnMNBD03-NrdkFfVbpeT0kiWis-vXC3jF2sMwE4FlVa8U7GlB3R_K2CFvo0emjgaBmHfyb9U4QvGgQRFARw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ciC4hLUrJsEIIpXE3IliOs248prcTLCgcWEqrEi4hCZmu83ZTuGsdmCk-edZqsk3wgKsIQd4m-WwdVLDSWOSMadlq75HxsREx3vPi-bQqN95ibUAW2XA4fiJ_m6klF7RERybH7gk8Boz5AWnO5Zeo3eTRSFVEQLWDfmWsjXOc9NsKGuqhgIbE9TMozRn91dSiLQ3bKffp97eGsE7YqGMaCBp1bkWvt9HbEJwv5r8QOJR4UNV5-PHdr4JeFs7hQt1Ka3DrRyR9d6G1h5uZMTae-I2Iw_7TuUcX1wZaOKH7EDEoptDkSZ6BBwrbtE9c29iz5EHujou6KJQCRgqfwnnSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خرم‌آباد در سوگ رهبر شهید
عکس:
نگار ده دهی
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/447604" target="_blank">📅 17:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447603">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24be751d00.mp4?token=ME1L9-X1cilY5DwhW9Jpm9hk40rIQG2isbxg1ehJZ0AinSCQ5Behq2bhpN21LZBESsIapADzPcR7nGTDrWb8P-F_rDry-BFB6rT9EeJ65WScZT_E4xUCiToD0BtBRzZwR_eLOig0TNlrBVFL8TGvEIYTv58Rbk-a2regi-W7wNaU-XkqszogWktCZGOdKjpTRaWARDGo47bWifmcExGBjihpkrcNuQqCmHeQKFJ2GtLxnh5xxaAJJvfZADn-tKdjjxOCkC4A55T7wGd38JLPQAxQ-lgwUoV73VqkV7Mx3wRPQcXbQAriW4PPm5tGMhuSipSCf79hS_QYD9yYfe8MVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24be751d00.mp4?token=ME1L9-X1cilY5DwhW9Jpm9hk40rIQG2isbxg1ehJZ0AinSCQ5Behq2bhpN21LZBESsIapADzPcR7nGTDrWb8P-F_rDry-BFB6rT9EeJ65WScZT_E4xUCiToD0BtBRzZwR_eLOig0TNlrBVFL8TGvEIYTv58Rbk-a2regi-W7wNaU-XkqszogWktCZGOdKjpTRaWARDGo47bWifmcExGBjihpkrcNuQqCmHeQKFJ2GtLxnh5xxaAJJvfZADn-tKdjjxOCkC4A55T7wGd38JLPQAxQ-lgwUoV73VqkV7Mx3wRPQcXbQAriW4PPm5tGMhuSipSCf79hS_QYD9yYfe8MVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر آموزش‌وپرورش: در راه رسیدن به استقلال و آزادی نباید هیچ‌گونه ترس و هراسی از دشمنان به دل راه دهیم
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/447603" target="_blank">📅 17:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447602">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAGix_A9JJtL_hI4DB2kZlQfuGFc5YjTV0ZqnLpqVDZohB3xRAZtf3yPVQAlYDDbJM5woojvnhmp62h5LGDyhIq0egfSVJZT-5k1PWs4cLdocFZIDrv2Em8vRTu5eSlfgd_GXY6yXF-mteERq4fRYj-Hbj6ISc5Q8_2tI5xzLfwX6RuRxqOposAfhkJepKiWBK8YNTjK21D-SquEmWwWvJCRwz-dmr7a0vGd539_SMsAgX-QAAgOwc31JGANatzZ1L4zH-Noc5A1PZkcBPuVUQ4XMCGwP1Piy5vbaDzId-o7GEBupcltwMxI5R7NTOJVqz450VZrDFwFCjsyaialow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درخواست نتانیاهو از ترامپ: ترکیه نباید به اف-۳۵ دست پیدا کند
🔹
نتانیاهو در گفت‌وگو با شبکهٔ فاکس نیوز، ترکیه را «رژیمی آلوده به اخوان‌المسلمین» خواند و گفت به‌نظر من نباید اف‑۳۵ یا موتور برای جنگنده‌هایشان در اختیار آن‌ها گذاشت.
🔹
ترامپ ماه پیش تلویحا موافقت خود را با فروش موتورهای جنگندهٔ اف۱۱۰ به ترکیه و بازگرداندن این کشور به برنامهٔ جنگنده‌های اف‑۳۵ اعلام کرده بود.
🔹
نتانیاهو مدعی شد که چنین اقدامی موازنه قدرت در خاورمیانه را بر هم می‌زند؛ توازنی که به ادعای او، با برتری هوایی اسرائیل و همچنین موقعیت آمریکا در خاورمیانه تضمین می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/447602" target="_blank">📅 17:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447601">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ee2d813eb.mp4?token=ved1ib29lWWhMA5ALQhU0C07ZQiFfZnIp75Uq1i_rUUuwMaLxuHRRiRAKQgDdWz7K1eaOC10KUJAnbRIYSfVUgqG-4Ognfa_LFUooUwwSky8BmgPDq92j2YCBqti3kEd9hocN0ZnGbBg0igTv4R4_CRFcbfPTQcKNzAprUjhPSlbQnZfYB9HYklFadQbnEioqi22-hODbLJTjDj3QbesOMN-r2GLSwA8Q7FVpjjnM9f8ZiIa8pA33yB_9NCSB16BESjmjqApYSnK69cawIyor9eUm58GWT4VbXl25GAosWvb66KXiRGRqmSVCQhTSEFI1oIeZ9ZmnNbjJHkFJmn1DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ee2d813eb.mp4?token=ved1ib29lWWhMA5ALQhU0C07ZQiFfZnIp75Uq1i_rUUuwMaLxuHRRiRAKQgDdWz7K1eaOC10KUJAnbRIYSfVUgqG-4Ognfa_LFUooUwwSky8BmgPDq92j2YCBqti3kEd9hocN0ZnGbBg0igTv4R4_CRFcbfPTQcKNzAprUjhPSlbQnZfYB9HYklFadQbnEioqi22-hODbLJTjDj3QbesOMN-r2GLSwA8Q7FVpjjnM9f8ZiIa8pA33yB_9NCSB16BESjmjqApYSnK69cawIyor9eUm58GWT4VbXl25GAosWvb66KXiRGRqmSVCQhTSEFI1oIeZ9ZmnNbjJHkFJmn1DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دکتر باقری لنکرانی، مشاور پزشکی رهبر شهید: تنها کسی که در سال ۱۳۵۸، در شرایطی که دانشگاه‌ها جولانگاه گروه‌های ضدانقلاب بود، شهامت حضور و گفت‌وگو با دانشجویان را داشت، رهبر شهید بود.
@Farsna</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/447601" target="_blank">📅 17:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447600">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvJSobr74M4u6gzMsYs_yIgAlONTyV8StazF4EBHiGwvlSaZAEajFk-6n2Se_KCKTTxqaRpp4Iql-raZ49co1KngPPCoATjgF4bj1j1cJPxQqAn4aQpD5RP1cP_ZzmihsDV1D8-Fh1lXLtWxXlPDfVr_yKLHanAcrovcfYeppE1vxz0uhA6tFrWV5GhfBuynCj-akBSmj8G6z0BFbFp9cNfPCRiD2f1nCJA8Ded-grjIFaYHq9Pw07RB-ylmf3cVPty3DCcF5QooLxAS1Y3E_DBQ-2yLpyUAc-KcwVjaywY99-Bb0i793aS3sW39yAGCpzDqZN2OEa0cdUwaYY0EsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام دفاعی پیشین انگلیس: ایران قدرتمندتر شده است
🔹
توبیاس الوود: ترامپ هیچ استراتژی نداشت؛ صرفاً یک نمایش قدرت نظامی در مقیاس عظیم بود اما در نهایت، امروز می‌بینیم که ایران، به‌نوعی، قدرتمندتر از قبل از ورود آمریکا شده است.
🔹
ترامپ هیچ جنگی را با ایران نبرده است. حکومت همچنان سر جایش است، موشک‌های دوربرد همچنان عملیاتی هستند، پهپادهای شاهد و مابقی تجهیزات هم همین‌طور. و همان‌طور که می‌دانیم، ایران کنترل کامل بر تنگهٔ هرمز را در اختیار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/447600" target="_blank">📅 17:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447599">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPFfv-Ga0o39n5czJNfTV60jjOPrMGJVR__gcwn4yoPq5Kdf93Ihrp1H7eweOmb4GavM1pNsGfGvPXlHQYw2U4Cgo97qeGy7sgn3l6cWW2m22gM12sfzZwn4PnVMHwjU2OoWq8Prkgs3LKblilpmnO5qnZXImn0jpKL8oxRD-JBNbAnK-5eh5JPCeq_FGThtBW8YZ5n7PyWDhHLauJC8gX_9Jvp4pOPdXCq97bjhSvwLGTTMeTTo5sW82rNILSy_VYLNR2hi-t9gs_EhIjTEKjuGPiwYQNnZPkyMxy9vi8ikuV2wjQYAhKa24x50cb9WbQNNXJEXNNMVHYEnU3aRQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
#تحلیل
| محمدرضا جلایی‌پور:
تشییع رهبر شهید انقلاب در تاریخ ایران و جهان بی‌سابقه و شاید بی‌تکرار باشد
جامعه‌شناس و فعال سیاسی:
🔸
باشکوه‌ترین
#تشییع
که نه فقط در تاریخ ایران و جهان بی‌سابقه، شاید بی‌تکرار هم باشد، به پایان رسید، بدون هیچ تلفات انسانی. پیامی قدرتمند به متجاوزانی که چند ماه پیش از نابود و تسلیم و عصر حجری کردن ایران حرف زدند.
🔹
دست‌مریزاد به همهٔ سازمان‌دهندگان دولت و شهرداری و سپاه و فراجا و ده‌ها هزار داوطلب بسیج‌گر و خدمت‌رسان و میلیون‌ها شرکت‌کننده که چنین
#قدرت_بازدارنده
و اهرمی برای ایران ساختند.
@rahbari_plus</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/447599" target="_blank">📅 17:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447598">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be74ae9eeb.mp4?token=FU19b5t8G-YHxwChKjyaimVk4NdJsIc0izmAq2Z0mqrFUQzK83xP43fmqmKu60JrPs0uiS2ZSrQ9r-3mt4PiO7vw-Wsqeq-ngGRHpNrhbBEcDOcoqwOOVxCIaHGqlVngalRlTWmMUOlbnmH2lul4pTOywl9RG0MyBA9zch7bIps7mKgGGb9MNgb8HPfJeo40umW44_Bf0RG7sIGCY4yKK2Wdu-bu49-Yb6qgxTJPukv9-qaO--yZtds0O2kC3l_a-sizYP1toDIPFeEREy-rlRmPS-zbsA9KKbQqn3u9gVVhLT3PoWdtx8iytswUajy_b3JlHjqff3phxKkXFY0Bw1fOBKdroVJqkWhN-qs2jgtDwV1-vCN7Xjbt2S-eX8zG3fNhLiq3-KUUTcs-x5sd4TO1zFzE82Dss02ngBd7df_WR1UguAM0sRajP3pDMv6JYlMSuG70l2-Ed86f9_Mo1l9ndpnKA2FhZ_BCmNow746iTDto21ug0zsfzR2fLSf12P2tu4N0IEZetzqvCo8CYYgC7R0-weHWWnUpijAcMp6OgXa2jil4aR9ZCyIMZDJHWtJkbumvBziU10sIFDL5VTjSLtY73so8B430_7fLBjHMqD13TaU7kYItIUvOLea66d_fqY0NapFkQNqTtWRgNsYSTegrRXerL0Z4dpkze9E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be74ae9eeb.mp4?token=FU19b5t8G-YHxwChKjyaimVk4NdJsIc0izmAq2Z0mqrFUQzK83xP43fmqmKu60JrPs0uiS2ZSrQ9r-3mt4PiO7vw-Wsqeq-ngGRHpNrhbBEcDOcoqwOOVxCIaHGqlVngalRlTWmMUOlbnmH2lul4pTOywl9RG0MyBA9zch7bIps7mKgGGb9MNgb8HPfJeo40umW44_Bf0RG7sIGCY4yKK2Wdu-bu49-Yb6qgxTJPukv9-qaO--yZtds0O2kC3l_a-sizYP1toDIPFeEREy-rlRmPS-zbsA9KKbQqn3u9gVVhLT3PoWdtx8iytswUajy_b3JlHjqff3phxKkXFY0Bw1fOBKdroVJqkWhN-qs2jgtDwV1-vCN7Xjbt2S-eX8zG3fNhLiq3-KUUTcs-x5sd4TO1zFzE82Dss02ngBd7df_WR1UguAM0sRajP3pDMv6JYlMSuG70l2-Ed86f9_Mo1l9ndpnKA2FhZ_BCmNow746iTDto21ug0zsfzR2fLSf12P2tu4N0IEZetzqvCo8CYYgC7R0-weHWWnUpijAcMp6OgXa2jil4aR9ZCyIMZDJHWtJkbumvBziU10sIFDL5VTjSLtY73so8B430_7fLBjHMqD13TaU7kYItIUvOLea66d_fqY0NapFkQNqTtWRgNsYSTegrRXerL0Z4dpkze9E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمیشه باورم که وقت رفتنه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/447598" target="_blank">📅 17:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447597">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae71663822.mp4?token=e2FGZUjrIaH2QoAfWTSJ-mmIr_1qM6zesoP9m_OmWewveJFZki-13Q5tZ6L4bfB0A0mX1dZ9GJiSEawNO7iva5HyeScjV6y-sDX0Qq5rCmQsJYpjNs6zVK5XXcwBEWQC6z8EzsJlkLWtojoBzB5Kc3UIdlZIzvKoJ0TAsk9VHopqwpjJzsAPL8SmlBO9twu07zRX6usz1XOSjyqhCDFkWaJSgO1-bytCOjao58JoOXWrCaMFMUYGQTIXHIL3htZK2KIGgFVa1FHovd5Zwlnd5gM2CRjoWRRuqXcDBzw2qEwYMlepRirZ9ftxuNHvEozVGZiv2BqyU5Q-9Ym_jq110w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae71663822.mp4?token=e2FGZUjrIaH2QoAfWTSJ-mmIr_1qM6zesoP9m_OmWewveJFZki-13Q5tZ6L4bfB0A0mX1dZ9GJiSEawNO7iva5HyeScjV6y-sDX0Qq5rCmQsJYpjNs6zVK5XXcwBEWQC6z8EzsJlkLWtojoBzB5Kc3UIdlZIzvKoJ0TAsk9VHopqwpjJzsAPL8SmlBO9twu07zRX6usz1XOSjyqhCDFkWaJSgO1-bytCOjao58JoOXWrCaMFMUYGQTIXHIL3htZK2KIGgFVa1FHovd5Zwlnd5gM2CRjoWRRuqXcDBzw2qEwYMlepRirZ9ftxuNHvEozVGZiv2BqyU5Q-9Ym_jq110w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاد دانشگاه یمنی: امام خامنه‌ای در راه دفاع از مستضعفان و مبارزه با مستکبران شهید شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/447597" target="_blank">📅 17:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447596">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPFsaUx9LFxIKj49Sr_JMIsejRTTy-o-ZKSf-DDk3UAPqlnTlolEZ-BjZCVY6QviKB5g31IpRptDSr1Sz77ZlS6KXmDXwVivoVo11HzgYYZYKcyqfnxbBcdkJGkvkjJnjKWhp1x2uoFCqo-3G9bbXY0MnIfysarSfcyctFWyTRRcYHRn_IDl5SmWL7O0GP0dOXXKizOksGKCd7CfilSdRLETuKl06pb0_hk32VwBFB_tNfueEVwCLtGKR8duL_JqJeOBVcY23wv0-02LkWc95zbq04_zkyYDkPCZSPDkMLTNYAGQSoAFJrdktHUm56A8EpydTE5Cpm907HMrXbZbSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محدودیت ترافیکی معابر مشهد در ایام تشییع رهبر شهید
اعلام شد
🔹
مسیر اول: خیابان امام رضا(ع)؛ از پایانه مسافربری امام رضا(ع) تا حرم مطهر
🔹
مسیر دوم: بلوار قرنی و خیابان شهید رئیسی؛ از میدان فردوسی تا حرم مطهر
🔹
مسیر سوم: بلوار طبرسی جنوبی؛ از تقاطع فجر تا حرم مطهر
🔹
مسیر چهارم: بلوار مصلی و خیابان نواب صفوی؛ از تقاطع غیرهمسطح مصلی تا حرم مطهر
🔹
مسیر پنجم: بلوار جمهوری اسلامی؛ از میدان پرواز تا میدان پانزده خرداد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/447596" target="_blank">📅 17:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447595">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93e4ca20bd.mp4?token=tmuJ9vsJ7mXiT54gZXRss33rep72nQ_aqps-Prwc1BgLmUug2IcP8tAzhWSJHp79OhAXxkNwF-fMd9VVBHW-AduNAjSsaBlIPnjfiEcAKU-m2yQsjalQ12Uoq9l6mlZCTHyc-dWgFaiYpKrcp4RfXZKpjHa00hOxgFeLIgq29kaY9Z2y_-93upotaLWGvWR8eQXc9gyt4fs77Nxhoy1miNb2gFlH_3c5hujhJzdlmd2UTzr1tQpdMt1zhASAbKg91FwKX2k7skK1hqgBvMa6C67IlCuvtaNuyLwcJLGYT2rar43MHKf8S3nXs5Erts7f1k_u2DmMeqF_2q44qjQIIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93e4ca20bd.mp4?token=tmuJ9vsJ7mXiT54gZXRss33rep72nQ_aqps-Prwc1BgLmUug2IcP8tAzhWSJHp79OhAXxkNwF-fMd9VVBHW-AduNAjSsaBlIPnjfiEcAKU-m2yQsjalQ12Uoq9l6mlZCTHyc-dWgFaiYpKrcp4RfXZKpjHa00hOxgFeLIgq29kaY9Z2y_-93upotaLWGvWR8eQXc9gyt4fs77Nxhoy1miNb2gFlH_3c5hujhJzdlmd2UTzr1tQpdMt1zhASAbKg91FwKX2k7skK1hqgBvMa6C67IlCuvtaNuyLwcJLGYT2rar43MHKf8S3nXs5Erts7f1k_u2DmMeqF_2q44qjQIIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امروز حسرت تهران جاودانه شد
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/447595" target="_blank">📅 16:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447594">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5fb616c1.mp4?token=fmBoCBqcBNnEY0Ebp7DBo9OTFvw-XhI63QngQm8b7qtFgmOtjd6I7iRjTqlPYMTSkw8DFALrbGq7b3J-HuxaOecTFjqnaPpOBGiAuyZZjJbODt4UW9SeRj7R0ihZKrlleG31Ue4Zxwg9SoiQr5Wa0J4VPwHJMbM8Kjd4rL2i2Y9w-J_XNZR937tjk1-zvhy59PO4L7hpEnDxWzZLV4b-CF6R4TwH5PZ4sYVGyVdkv4ZYR00TDVcrzTsapd9zdw1ZNGXoQvmkOQvySwAGwfHdrECsyMcHN9wxWGjn2txyaBHDmpXAgRVUHliNQ2mYTaLbsDHa7bFGamrcbYicGktlyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5fb616c1.mp4?token=fmBoCBqcBNnEY0Ebp7DBo9OTFvw-XhI63QngQm8b7qtFgmOtjd6I7iRjTqlPYMTSkw8DFALrbGq7b3J-HuxaOecTFjqnaPpOBGiAuyZZjJbODt4UW9SeRj7R0ihZKrlleG31Ue4Zxwg9SoiQr5Wa0J4VPwHJMbM8Kjd4rL2i2Y9w-J_XNZR937tjk1-zvhy59PO4L7hpEnDxWzZLV4b-CF6R4TwH5PZ4sYVGyVdkv4ZYR00TDVcrzTsapd9zdw1ZNGXoQvmkOQvySwAGwfHdrECsyMcHN9wxWGjn2txyaBHDmpXAgRVUHliNQ2mYTaLbsDHa7bFGamrcbYicGktlyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دوری و بی‌تو بی‌قرارم...
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/447594" target="_blank">📅 16:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447593">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYzGCqcaV7vt1IQo9bQAfuViEtzXvODf-wf8DHGAAU0zz8XkeqIyQxazGgQCLg7vmrn59dAN-kd1SogUkk73Acj8i2O-0gOMF8ayEa_tJ8Gv9_COzezIP2CosPaC52C7LKCDyo4YvX2_99airw-oEKNVYv-CTe3nkXTF1GZMTpTCK0InymX0VSgJCriqGMYc6TVwenXTNdrcDg9_XaabA3sDXR8IOqirOYHqtYV7LZ3IQkyUXjm1kh8Pf5TfyYPpWNEd6R4TBzLWvo6fXBvKwsuxTXiHHOh4oRFmD8VvKyE_gdUeCQCkNRcgB8LrMK9z7rfuUuZvjoZS0gr0ph22KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
اژه‌ای: مردم انتقام می‌خواهند تا هیچ مجرمی به خود اجازه ندهد جنایات دیگری انجام دهد.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/447593" target="_blank">📅 16:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447592">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/838f9d1885.mp4?token=XAsSnqD7vRqTu83aOq0H007pCSPtgy-r9wuAJgmyctaPR02F-XBx6U75ElPGiwaC7RrR-S2wOB5XYRj0-b9_44rbmnpUm4vRwdYbrENc0rS4zx6zoPVg-GKaJ70-LmYEGbfP7uXjVaskpNSMCZkrVdeC8zPH6ZSNE3TxR2NJgIobfv1kJBNvrp0zi-scquzOZ-pBbcEwvb03JdIJjwutHzbMf-F42xxiuub9QtA221ZIvh0JS19NwvghT0Ay-7Xu8of5aldWANCx19k5m13h7Vwkak3dEFH-f6wWkY0Q4oGUBpOwZAXfRgpMuDjc85vClK-Kk3sEh4fpaON9DRTDAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/838f9d1885.mp4?token=XAsSnqD7vRqTu83aOq0H007pCSPtgy-r9wuAJgmyctaPR02F-XBx6U75ElPGiwaC7RrR-S2wOB5XYRj0-b9_44rbmnpUm4vRwdYbrENc0rS4zx6zoPVg-GKaJ70-LmYEGbfP7uXjVaskpNSMCZkrVdeC8zPH6ZSNE3TxR2NJgIobfv1kJBNvrp0zi-scquzOZ-pBbcEwvb03JdIJjwutHzbMf-F42xxiuub9QtA221ZIvh0JS19NwvghT0Ay-7Xu8of5aldWANCx19k5m13h7Vwkak3dEFH-f6wWkY0Q4oGUBpOwZAXfRgpMuDjc85vClK-Kk3sEh4fpaON9DRTDAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اشک‌ها و دلدادگی عاشقان در مراسم وداع با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/447592" target="_blank">📅 16:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447591">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa32f53b4a.mp4?token=SpMaQLtKN9-ULFzXRlvIH9E9irVj0-rU7xlGCJicqwMaVvFEzzxKO0JV6MszwkBJgj8Q92GaYTWsBUwSQj8bz1ROkltLkqf8swq9Na_bK7QYiZpBgqApI_5qx0jrl1Z_7WUBj-grrE8qdQQ_MhrH3dQN4ks7xVtt_ONw4_LDB2QO_uiDB9NOpmaxhG-7T9c8p7nHvtiIFkIp7iADR6s82DA_5lwsOeLc4fVHnkHpaNOiMIrQ-dh4JgbAZkQ8UfBBKAeJq30RQQLO3Ovv8z7NBs4lEkT2HCgfylyILZg7W2CYTrDbGrQwX4Vu0EqR4EJiKU9A4cYL9mZh0_FQvc8hIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa32f53b4a.mp4?token=SpMaQLtKN9-ULFzXRlvIH9E9irVj0-rU7xlGCJicqwMaVvFEzzxKO0JV6MszwkBJgj8Q92GaYTWsBUwSQj8bz1ROkltLkqf8swq9Na_bK7QYiZpBgqApI_5qx0jrl1Z_7WUBj-grrE8qdQQ_MhrH3dQN4ks7xVtt_ONw4_LDB2QO_uiDB9NOpmaxhG-7T9c8p7nHvtiIFkIp7iADR6s82DA_5lwsOeLc4fVHnkHpaNOiMIrQ-dh4JgbAZkQ8UfBBKAeJq30RQQLO3Ovv8z7NBs4lEkT2HCgfylyILZg7W2CYTrDbGrQwX4Vu0EqR4EJiKU9A4cYL9mZh0_FQvc8hIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطرهٔ کوثری، عضو کمیسیون امنیت ملی مجلس، از حضور رهبر معظم انقلاب در دفاع مقدس
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/447591" target="_blank">📅 16:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447584">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUetiES3puH53deaHvISqcBVoUtYw5pIC2gP6BElEg3todAPtHEMaWGaNdcHlLa5QrL6NV0CLoRAej07-F5EtOnqmckjzyaEt6mU9l3LOq_sYNCHUYwFikSAI27cVaMayDtKoGXHPT9OcIVze1k4HcCLtT2aseovujx4Mv_kd52VqX5Y6a9oTu-p3QJJtkuFY7mUkIn1Z4I3m3_T4RVS1sK0ZygokrnWUTwoQ5nfdVRcz0rVWax9N3PfHaijiGmNKJWJ1lsO4DnFy46HOLlSaQLBsOwRTcELC5rpvn5nXitjlbUuulkV-q3z_Sr_l9FQ7xd3lvNAwE9ssvrzUAAkiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aSbvh2sKCH38eCBkqboJ1PhmXUkXyJqpr8R3i5ddbM9qyTDd_jL0aKangFVaExJZP2iP0TSfxvevsZwP405kXcvcqZJOJRvwWNDTDBIpchuFnqgc3twfA0z3V1s0SUqBs5ZkehuSdz1cVsbGS2QsEn4FLYXhFxnczzxtsaTElM6FqcOiJMpN_q6yXJ4wV2tULutc29qq4A-O2s_CKHKIcyXAcopd27Ss7B95ftOBlF5kaVrUbYoJPyT3vImeBbacjy6nLeWe1RP_kfAnUOwhQOOQBd9BK_4RVZ6r1ZIUiOXISjmYMJAO0kpTowbq0bbooJ7eO8hLZ2TR3EVkQntjNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tHo6Ef3A5dkGBJAOPXM4NHO9UBKf18nqlGgfIxskmkz5BqEK1ncWcD8ZrrnbYvVhy4vDYeqMCO7cVJ47BbMib1LYRQGUv3CDgbXlbsfUeS-x6BRIjVP_-DZZGPtHgBc9Z1GDkZKQq5NrXjHgBvLyEY_C61sYJ5ayoYlX8rsVDz2SIXS34JpREUVocYhwCBcVuyzjcgAHEgocEZvinnrjv5LMQuXGniAckPCfbXIc4QCRZyDXnQFgdoPy0awMR-J_aH3qRTEEL35shECkhpGpJ48CG_dKYcxZ1uDt_qw0szOIqJODAY00t0DtCUmGOfgEFigWfsGACAPOwlayxpOc4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DH6h36dKRVVMpFIvmkzwcEyzhC8ChoObXSSmWXIwzGbb8BbQ5THGmDJ0Su8cP_YR6ugfqykGh0jrMMT8CRM8hTVOytJjByH2hDqt08NDNA1rjhuzZwjQdfbtfIAXSoxnCbWsjATcAP1lytqoobGrBou9vYCC-MrR1g6UsHM6Q60xC_r_QdIxw3Ne6CMx3EpePG3f6h9ItEUgMaBp1-p4Uu3-LzEqdt8DeMnqO1TciBoLbPwyQ7TvWUA9-9ajiJS-fYMVtLHYbafjN82Kns-1x5srPLHSBY6AU7n6lyHvBbF9OywGao-ApBJ8VBWgAZqQ91CHFxBpRM8DlBTPJCEIjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B07sInmhyktaChqhiqhXcEeQTx8Ko8qAk4_gLUY-vf6Rs2CPdDCqXYkmTMm2-SThVketXODfBVUtHfofB6P0vay1ijZHHhopxo0bk36CxwmC2af0fbBSXReh0BcERcZrUeMxQNPl3OHwEfxSZsOPjQ2CBMhwDPvjbfQv3PE5YCcuETL8KEtu8LD-HvCGtO8qCbsStlnf5IZf3bx-yRB1FOjW2yAvadwzk6nppbL2nMNtpLKU-_4TufL4mIY2sbV0dNs3_aCg8Hm5DRwnOWkvVS1XCR0dj24BrthqPOUEo9GJGWT6FFRwvJd0jrEdOLM0P9o0UmNctaINll2fIflWRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mlTa4ZNhen4au0SIBI-SGzr9U_cBRk75JE34gYfHH-nCsX8k5XNHKPKoM-0z8Yam5GINjgukpQpL-ifCCE8KCdj3nrO0FxV52F88BOOJ8Et9Z2OioGvy8spU23Psxjkowg23sGzjoPC6xLc_EfMkEyZzFM75NSJ_JwL86ZY7R0_Rq6ZulouuGDpfWN9BWpolsTDO-BVrQyN8yvScvauG05DdFqtXrHA_ZWr3B_vHyzZqgGBKXWLFi0KnwBTr1ZPhspiHhLcrm0WvMbAz6GDaGdAPm38ExlkGoFfFS27ugHE3sHT8cNjLyexCtaWGENo8_Bkt9PWI2mHs-Q8PhfSFKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c2dYGb102oQCt7rEshJOXaOjQB-6PISyaWethLu-cw0CExDrJ7empYpOzpvW83rdFwtEVBQiIvlOjPXULALo4fFZPam68C7h8PnXe_b_mJOYew33xJp2KD08BaBzMjRbfaYyZ9NJGKt77_9i03QctZeOLw0LT18T-U9S9Na3-jBUfvLWykviGWfcRIfYMbb1RMjevhGdCUcRDXUj9YRMDOP-llf8ZXANdn9tfJPFmsSK7lhutzcuLtWZVHM6NotJsRY42AxzV1rVyOp9DbKjNs6F6fzb1nKGCWRSUvE4k1bXjX3aTGEtczMg_9idMsOxpKBfp1s-K1QdRnAkbKVITw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
وداع مردم ارومیه با رهبر شهید انقلاب اسلامی
🔸
مردم ارومیه هم‌زمان با مراسم تشییع پیکر مطهر رهبر شهید انقلاب اسلامی در تهران با برگزاری مراسم جاماندگان در این شهر با قائد امت اسلامی وداع کردند.
عکاس:
قاسم رحیم‌زاده
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/447584" target="_blank">📅 16:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447583">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128e2c6ef7.mp4?token=toZ5zvlVPKvJrnpeZAo2sDTbvicT7LA159c808yhtAWLXbrPDGUuB_65GNUQdXThtWwy9uw6C0AQgwn9960wrEmbxOJEn47KMAO8u__4fTau7ckU-XR-QPJQuOK7wXOtVW_pU17PSZNnkTMDpJoJDqdR2gLKv3FIhV8n6T2CWIozhA5IqbPvuWunO-a8qQt67GKwwA5SbVgTNdApYarcnVwhtvW29TxNx3Ula-wmpEei3Mcp1gSndisrSIxEuhab0AYOQzrQNq4vRiDuRv50ftEj6w5c7BKnS23LLPNrVoYfIy9e2KtMGChLqG2Tct13rxg4cF11ATxM8tgUNYLt3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128e2c6ef7.mp4?token=toZ5zvlVPKvJrnpeZAo2sDTbvicT7LA159c808yhtAWLXbrPDGUuB_65GNUQdXThtWwy9uw6C0AQgwn9960wrEmbxOJEn47KMAO8u__4fTau7ckU-XR-QPJQuOK7wXOtVW_pU17PSZNnkTMDpJoJDqdR2gLKv3FIhV8n6T2CWIozhA5IqbPvuWunO-a8qQt67GKwwA5SbVgTNdApYarcnVwhtvW29TxNx3Ula-wmpEei3Mcp1gSndisrSIxEuhab0AYOQzrQNq4vRiDuRv50ftEj6w5c7BKnS23LLPNrVoYfIy9e2KtMGChLqG2Tct13rxg4cF11ATxM8tgUNYLt3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوگ‌نامه‌ای در فراق پدرشهید امت
‌
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/447583" target="_blank">📅 16:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447582">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aec563c796.mp4?token=BwOB-44sFDsV4iVnuBcd23W5IZtmIvBridrn0lqVVfEnkBoai4dsqlExf_SnwUNTt6EyfeIoPf1IYIWwYK3rKxbLXcNUYHVH2sy8MD_GAJRcBUh123rBCxILyD-gREYzo8pSPhb-rmkoIQdxzXdqnFCI0Q50EvWTBY-fl_aiHOx10isxQYYKF_HfGsAZoyEDm98XFy9QKZHtqo5S1qY6yG5Ib8BM7KzrNznUNyobonT1RUkO5e3s08aJyNhro4Meypj-cNoRSoDqgENq81tYw-XUNoJ91JDbCUs0hrYvKOdWU5PfzDplZgkoR2aWkOXAKOXq26WMpaAI-8SKrNUlkS55KVuJaIJU5A9nUyCV0-S81e1b4RRVqN8yJrF31XISY-RyEiD3WZJ4ei1mPdVMaowv-C3IocMt_Xyzzi3YYJf7l5Duhvp5uhFjk7TYEMGNfAf-GC42DVWtVrwu7EXnje-3Mr2Am4u09-iHFzphIAnAjFQFSj5NnQr5uORKRpF-GXZ22_WHq_RwMx8WcPUVxRQdkYmP1LpDuwNOqU5I-98mwmcFvJdyPeN9HAU8H73U9CsKcVy59ownpwXFTWde0jBupuHeX5GKL0Dpayl3rMNF2qfuHz0HxACmIJ2EWr6aVwtM3RuQ1jjRGzgEug0yQUOvEgkBZuEGQCcVHxmw79w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aec563c796.mp4?token=BwOB-44sFDsV4iVnuBcd23W5IZtmIvBridrn0lqVVfEnkBoai4dsqlExf_SnwUNTt6EyfeIoPf1IYIWwYK3rKxbLXcNUYHVH2sy8MD_GAJRcBUh123rBCxILyD-gREYzo8pSPhb-rmkoIQdxzXdqnFCI0Q50EvWTBY-fl_aiHOx10isxQYYKF_HfGsAZoyEDm98XFy9QKZHtqo5S1qY6yG5Ib8BM7KzrNznUNyobonT1RUkO5e3s08aJyNhro4Meypj-cNoRSoDqgENq81tYw-XUNoJ91JDbCUs0hrYvKOdWU5PfzDplZgkoR2aWkOXAKOXq26WMpaAI-8SKrNUlkS55KVuJaIJU5A9nUyCV0-S81e1b4RRVqN8yJrF31XISY-RyEiD3WZJ4ei1mPdVMaowv-C3IocMt_Xyzzi3YYJf7l5Duhvp5uhFjk7TYEMGNfAf-GC42DVWtVrwu7EXnje-3Mr2Am4u09-iHFzphIAnAjFQFSj5NnQr5uORKRpF-GXZ22_WHq_RwMx8WcPUVxRQdkYmP1LpDuwNOqU5I-98mwmcFvJdyPeN9HAU8H73U9CsKcVy59ownpwXFTWde0jBupuHeX5GKL0Dpayl3rMNF2qfuHz0HxACmIJ2EWr6aVwtM3RuQ1jjRGzgEug0yQUOvEgkBZuEGQCcVHxmw79w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک عمر ارادت رهبر شهید به امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/447582" target="_blank">📅 16:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447575">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/laePOFPSYykMCTmE36tKbMzUGm6w1JqvUugGfawqzOA4lAXFjMivm8hblliHDKfEH88D878hqX_KaWIOi6G-sF_fv74VPOtUxeuzgtG9ukREMVCCP9SmRozGVoDrE3QG_R5Zqrr0NPlw0AWomuSeLYpoDNFqldrNKqlpEJuKsDVbnAOX0lZvT1px7xJuoik1yhrETCpqoDAaZPDRpZuhrAAsAJsP4nGGUiqUqL-2WMCbk5qMGuvtYMLkCnPF_RAnWsEvRdR55vVJf0z1maGma7GnDNnjjVFFARkuBvvy-1QuHhXFxfZt4tXvT7Ve1j0UmgJ0_YS0BJXMFz0Z1Ez9Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUZpgMQxFT6mWrMM2_MMxi91cvxZgi6tPyLPLTxUCTYdOxpAceuj1iptyhlGOXiwZNyYxA1GvtSAyzuQec3VhJaf9bw9BjQQfJ3uLyYpUDdSAJZ-BkxBeIwupDWfi4l_rD3nrvfVDRIb_KFo_-cNWE8QGVhXtvwFf-uYuv3JykOP8NUK4-HU3hXus_nseQrP5-t-Wyi9HX3j19knbwiIwftI-7VuYtPR3I-VuI30QuBns3OBwwuaoR5RCvqPM9zn9gUKAkF6G_91qCl886Qhjr64ZMOsRO9CPbDvwlaFWMX-KBerPzysZy0qPFpxPzpwgnau9BmDevTeX_3v0rk7cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vfPq6oaMkbUjRNbvroUsUaP-2nPVNi87q1RYEdyR9fjTMfJwpBVAApPDNfUsCCX9iw2A5oWFjSS3IiYCv9fHIDoDZ4ZjQRK32YyozspCJ1atG8sqH38je8fmGpF_v6YYWoFVNvMUw3AY0TQKalWyu7KhrYhu-hNQobWrxOfuDNbgVUri39hQDsJx6zsGN2TJk4YY2aAWjoUKNnA4Ei6YwwDgth_9xegUgUkghKbxXsIIp0B_3fXTakZiPKSFN3AeaqKIQ3rE4Ei2G_XjbMHieFVo_z_YxuBWvnaVzY-pFZZZd4U12Hvg1Beqv2O8qa1lAQTZ1AdUql6D5Ncq8AFL6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eNaZ9nV90ka_Gc8ajPgWnt5-CCLnT19km5dXUnV4lEHu7RcedyfGB4reWaRB9CVsfE1RU_KtaiMtYMTNJg1XZJ-6YnK1jQszrKJhnrWSuGIi0PPAd07dvtkvYGCcWZS7Ln155I6twZ7GGiNLA2h1KRF8eCCkZEBr4wbNQd5Itg0uPeXNAy6y4yfy5L5vbEFha3FXoQJNk6K5mxw4vO1XgK4eysDVghizfKrOgiDxPj68OoKERSWCuh6QY3BGmskDCZwWOGfFQJ11LSUOJ9UFAfTpE3uycY0BzuzrHWr9bGkzxbMCWDEPI4PKBTTp1Dj8smTi7yT4ZEGF0Nv9aavO9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rPPeB9zoqpRVcLHYOsnUEu3FSrjkEUqjpdx4rZbzdtOsRHvTJPbawBF5qIVbOLiLFUd6kAWrgPJe3KeUZRqTaPRi5-N8oJe5_Ny5C5RMTfXPU-z3dJEy7f9gT7CIKtt3rqR58latSjOp8S1uot81D1qTIMWihO67Faxd5eqAOQr8jcSAtDmHuJgNrxRE3F_R2OpzH0RP0fV3NrCwSs7YxuXiaBO2VWjUFRroE3qDEzTgSKCPCMSfJefdwVFIfLqXiv0xb3OSUrz97ZotRfE2vecNI3tEL3UHITvcugBdSps1_SZ0h36jm8vluC7x6OCGfR8FVPFKKM1Ps69g5D5iJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FmvAImLbI1wklcO9ubTuvpdmsedDbLL0HOZAeHJ5ZS3-KQCCB_bQQgkdcQKYB8xGlSVIGMgjCN_A4gSpgQ5evCMs967XpAeOLVZWEMbT8gjqzsuoni9zSseVyV2rZpYkJcD-vp_aPJ_TC4X_9orGn7CDyXghpI1Q1O4rAR43oZ4y-hqgyDCNAPwD3aJfpUDQOq9fV9tfFo9R5947ppNPO155Lr_1d5Uo-fsZOyecnQEiLJSWxAmukecAnKIEaQ_oX4_rhpvrrr89vjAo7OmAkTDry8o1BpEih7MUOtdVG0pe-8noxrML_i1ipgN6bljaNyCwqkdx-ZPEw1EZAAWnVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qoQPtrFAhGYoSkO-55YBBDU-2b45v9SxjILvmSUHiTBVsDPfDqq0qgkGAAtAwQlrvk8UDjEYbop33pRNhsKaraPoXVlLAYqSnyw3lxxT88H9BbnLnmdeEzgkHCjsCBokEZ5bPabRcW5iDLxRzI2KkazMlIoZzXpQZLNPwFPaZ22F0M9E_xcx7CI-6HreV2sRrSQXItKNXXMM_J7yqMMvfpW57u1M7_cXtUEu-okxL7zaw--oxNd-GN_wA7Az7T8anqMIeQTRYtUtjGAMMoO5-TgmgR2GQn_nBwKE8ktoLXA-PSlOmDS-iy_5fl9UFm6qDITE_FSSB5S6hQhFH07LSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جمکران در انتظار بدرقهٔ رهبر شهید ایران
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/447575" target="_blank">📅 16:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447572">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZV_sy6ki2JZqJdV7PMiXHnueaQh4MYLLALp-yCMfXSBmezz4lmdiRlemkaLjJo3PBU6hLVxkQSHRMdo3ruPJn9OF4dhmQUUawS6eFsidU79W408f-vDjXQ8gDr4TeOKFQ194eYKCCsBC7g3gSH4B54X3lAs0wKeO2yXpMrQVkGDCmUIAX5pcgWSmp_fe4YCXOfNdVy6CdPCLmvuH6m70XYDTvxU7XI1dPezOmgiEP2ZFBL7_cINHYPpy9rsUhELOjHjQHZtAqT0rgj_xDcwQaGeqkcJATvsOtCvQ6b53iF4ZDMS_y70Y8vtLEJT1NOA1Ft98MhTu75AiitgOhOsqeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
وداع محسن چاوشی با رهبر شهید انقلاب اسلامی
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/447572" target="_blank">📅 16:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447571">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مدیر فرودگاه مهرآباد: از صبح سه‌شنبه پروازها با اولویت مسیر تهران-مشهد از سر گرفته خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/447571" target="_blank">📅 16:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447570">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/883edc8dcc.mp4?token=JGjGCqgJBmv19U7i5p2nAHwgdI0wf69b_1sVKL34Eyw7TRxBMPU8FJ07583UA9SHg-72wAA7OBu4uTWFC5kxopyg0Y5bOyPABF0fkrZ7uk9bWNSeWYfvWITpbRePfV4VJ0ZOEsGxRqz5_QMM3RaPwyV1aUc7TIYDBlUBrMQHDD7Bm3H657KPhLaqSZ3JViEU4qe3vZ5x2Z8NLCCDljbZDtFb7hBsDtfHD8Rf_nTfsA-KucEadA4YGGVgjXpee_mOwm1aOuYY4i5Cu5OgIGjnxxZXbsrNT8K3susef9JZJoFODwNAZdoGB1A57KrGflIwGnjOz4aNmHqOcepLNv5_UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/883edc8dcc.mp4?token=JGjGCqgJBmv19U7i5p2nAHwgdI0wf69b_1sVKL34Eyw7TRxBMPU8FJ07583UA9SHg-72wAA7OBu4uTWFC5kxopyg0Y5bOyPABF0fkrZ7uk9bWNSeWYfvWITpbRePfV4VJ0ZOEsGxRqz5_QMM3RaPwyV1aUc7TIYDBlUBrMQHDD7Bm3H657KPhLaqSZ3JViEU4qe3vZ5x2Z8NLCCDljbZDtFb7hBsDtfHD8Rf_nTfsA-KucEadA4YGGVgjXpee_mOwm1aOuYY4i5Cu5OgIGjnxxZXbsrNT8K3susef9JZJoFODwNAZdoGB1A57KrGflIwGnjOz4aNmHqOcepLNv5_UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما اومدیم دیدن تو، این آخریشه...
🔹
مداحی مهدی رسولی در بدرقهٔ آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/447570" target="_blank">📅 15:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447569">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc3592dd4f.mp4?token=JTG6WrpjK41ejzbvfI5kc4VH-wmdFkFEEgOJhNMNphaBnhxjPkoR-Z2Wn7fyGybxQ2s9SaG_NPR0EOA9YYpQE3Gr62CGeZoCGMoUM1a9ahgYSd9V7AwwzmECdOETyGsuJHXz1-RcLgsontHz0dIoynTR7X20b9esRMqJQ0Nt0aL1aX3kwbH1UaMG08g7lmmvYRNG0yEZKMSAfBatmpAAI1rwGD_dznGOLLjOiz-H5IPWOa_T1wS_6G7Up0GXeLmkGVEH41DequBgX_Z8Mf2NAQQOp8fcATgwUdIV_DuYoY7ws-1mGB9ieNLlXMRNGckJamB_hdDsl79ztwyHM27AuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc3592dd4f.mp4?token=JTG6WrpjK41ejzbvfI5kc4VH-wmdFkFEEgOJhNMNphaBnhxjPkoR-Z2Wn7fyGybxQ2s9SaG_NPR0EOA9YYpQE3Gr62CGeZoCGMoUM1a9ahgYSd9V7AwwzmECdOETyGsuJHXz1-RcLgsontHz0dIoynTR7X20b9esRMqJQ0Nt0aL1aX3kwbH1UaMG08g7lmmvYRNG0yEZKMSAfBatmpAAI1rwGD_dznGOLLjOiz-H5IPWOa_T1wS_6G7Up0GXeLmkGVEH41DequBgX_Z8Mf2NAQQOp8fcATgwUdIV_DuYoY7ws-1mGB9ieNLlXMRNGckJamB_hdDsl79ztwyHM27AuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای عاشقان رهبر شهید انقلاب در مراسم تشییع
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/447569" target="_blank">📅 15:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447568">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72987d517.mp4?token=pbgHNXGmkvbcU9SoQey-CpV2K_QejH515PH9zpPPDIjTTqoe2P9fouQsP3hoj6j5k4KAJV3MEXh24u82Pn6zX86WMKjtBNaYR6ofA4gQ3pV_6f2fkC71utZanC1DMir0Gt3RuFvNVdabKSb6ESvVNver8bTI84ht8Ui9IGXvOkiBmX9i31wgEBa0bid_XlLMcq2G_8DMDW3Px-qOwKyyiei67K1s6VVR-earttk4okNNSEvqvzy_8t_EjRucG8-uJWZgJ2WpxZmt3SS-cK9kN0vxHFqc8hEvhSLneMrwBHQ3KeyVonXyRJF8gE1zTbKBCDYXBZsUIOhbpiFj_9kvzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72987d517.mp4?token=pbgHNXGmkvbcU9SoQey-CpV2K_QejH515PH9zpPPDIjTTqoe2P9fouQsP3hoj6j5k4KAJV3MEXh24u82Pn6zX86WMKjtBNaYR6ofA4gQ3pV_6f2fkC71utZanC1DMir0Gt3RuFvNVdabKSb6ESvVNver8bTI84ht8Ui9IGXvOkiBmX9i31wgEBa0bid_XlLMcq2G_8DMDW3Px-qOwKyyiei67K1s6VVR-earttk4okNNSEvqvzy_8t_EjRucG8-uJWZgJ2WpxZmt3SS-cK9kN0vxHFqc8hEvhSLneMrwBHQ3KeyVonXyRJF8gE1zTbKBCDYXBZsUIOhbpiFj_9kvzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از تشییع پیکر مطهر رهبر شهید انقلاب در میان مردم عزادار تهران
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/447568" target="_blank">📅 15:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447567">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3b5032ec3.mp4?token=mojt3pBznKgJXIqZAD7WZRPvXKsgxwL74jOL6LwwsaqRGpTe81-efGDnvcehfJ_ubIAqYr_gNj8RoZL0xZbkelEOnieIsPbg-eO0Vhu9iQbGTOSckbvQ429kyLwVsR8487Qhfw3x77JtffFjzqUlLHCkAcAE6Mq-IEGTOzOcdl22MWxy43qUoLbtla5Hw8RoH3DE5WoiAeAuFIAUurgNNbZVQV2cmj6wNqXgmFI0DEmmt_4ajCxJVFq14KFzwOFkUB9sPMP6omZJcOUtuvH0mWhlTFMC0uc40ArWgmQ9cVSaEBVll_E6aIwGKkPNpPs4_QzAU4qhPKiWX8_MnOvHig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3b5032ec3.mp4?token=mojt3pBznKgJXIqZAD7WZRPvXKsgxwL74jOL6LwwsaqRGpTe81-efGDnvcehfJ_ubIAqYr_gNj8RoZL0xZbkelEOnieIsPbg-eO0Vhu9iQbGTOSckbvQ429kyLwVsR8487Qhfw3x77JtffFjzqUlLHCkAcAE6Mq-IEGTOzOcdl22MWxy43qUoLbtla5Hw8RoH3DE5WoiAeAuFIAUurgNNbZVQV2cmj6wNqXgmFI0DEmmt_4ajCxJVFq14KFzwOFkUB9sPMP6omZJcOUtuvH0mWhlTFMC0uc40ArWgmQ9cVSaEBVll_E6aIwGKkPNpPs4_QzAU4qhPKiWX8_MnOvHig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک سوال از حاضران در تشییع امروز: شغل‌تان چیست؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/447567" target="_blank">📅 15:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447566">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rb_fIa5RhQ8eRMN_navnzjXBvw-bxy31zohRdKceVyJzxTZHeRR-aPETZVKDcizKApYf3bNnGWVhO0uKqLAxv2kHT-vL-U44IUk2K5iwnlRw9hQc1MBOByYUu73i_lMuSXBOJGX5s79sZtHOKCCEqtaadAzceuoUZRdQAkTW27KTlo-1EUenvuMG37AVYEgJKB0KpO8nQJVttPIODWjmOY-FGM4VoXiFjhrt_sXBNfbZti2vEgNpIphf4j02tJYonDFBGqN-9K41yGjRjL8SmBYCiuPWfO7Mo_3QjJ5yB3IoTh2tRj6OzZIxt6VSnHoTTCGdBQV8FzAjGHe2p7d-nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور عراقچی در تشییع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/447566" target="_blank">📅 15:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447565">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eff642341.mp4?token=ppDHVtoatzA0jhCQ9I9BVrPOpcoboBgIyPZwiNJAa3axb1ysvdXnRTF3Z3ZIzF0GbjmS-N05FcbkpHYQX6fYAaNsZllarqI3mjYVNslrfi3uDI6WmUYZHDu1YK2j_9kIKw1L2Fsjo7IagtrHaXG5uh7IwPuieGxErZbl_eREnW-7snx6d1VqAJtyCbDTy4blt5zej6GYlAZuVXWbF5gM1UfNwpHHyrw9BgiDD4ColnA9l78l0L34_SvTOedGnYOqxJrl1_njwWw5Lqrxtaj6oflxhtJiQqPxVjm7cDIcwUdX1YlBBbItxYnuxRup86O0HDr7OEdOgsKfiFmw7jBWCAE2Lwm2ycWXD61PxX4RYVf76AH56EqjGEEW4B8dFMRlTeQVpftF1hG0xX4DCUuPCI2uJ17spJa0wPkp2fDdoiClTba4aPxHz3d0tq3J46s3k1lNphqFZ4nE7lsymIJmSKEc-BClPedlwLhTASDsHgvM0JCSL2qqGi-Ib4_8sAJNKBTm0F9hG64kiHbdjH25FXTgbjzoSxiWz-Y-NdUlhvgo8cIPHHL61nV5neKKAUJWj9q_owdTORPnittMZ2dqaxrNdvTNoCKz_vo7g_1qO5avKV6FY-5gF09htMlmUiWx6zSREhU7OSeKkSuZIctYHgmT1qbgMyqnL6vi6GCBlWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eff642341.mp4?token=ppDHVtoatzA0jhCQ9I9BVrPOpcoboBgIyPZwiNJAa3axb1ysvdXnRTF3Z3ZIzF0GbjmS-N05FcbkpHYQX6fYAaNsZllarqI3mjYVNslrfi3uDI6WmUYZHDu1YK2j_9kIKw1L2Fsjo7IagtrHaXG5uh7IwPuieGxErZbl_eREnW-7snx6d1VqAJtyCbDTy4blt5zej6GYlAZuVXWbF5gM1UfNwpHHyrw9BgiDD4ColnA9l78l0L34_SvTOedGnYOqxJrl1_njwWw5Lqrxtaj6oflxhtJiQqPxVjm7cDIcwUdX1YlBBbItxYnuxRup86O0HDr7OEdOgsKfiFmw7jBWCAE2Lwm2ycWXD61PxX4RYVf76AH56EqjGEEW4B8dFMRlTeQVpftF1hG0xX4DCUuPCI2uJ17spJa0wPkp2fDdoiClTba4aPxHz3d0tq3J46s3k1lNphqFZ4nE7lsymIJmSKEc-BClPedlwLhTASDsHgvM0JCSL2qqGi-Ib4_8sAJNKBTm0F9hG64kiHbdjH25FXTgbjzoSxiWz-Y-NdUlhvgo8cIPHHL61nV5neKKAUJWj9q_owdTORPnittMZ2dqaxrNdvTNoCKz_vo7g_1qO5avKV6FY-5gF09htMlmUiWx6zSREhU7OSeKkSuZIctYHgmT1qbgMyqnL6vi6GCBlWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نجف برخاست!
🔹
اهالی نجف برای آیین بدرقهٔ آقای شهید «جهان اسلام» آماده می‌شوند
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/447565" target="_blank">📅 15:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447564">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a86330faad.mp4?token=Hhp6M_FVZHpGs-AyIMTeRW6C39irI6KjlQtpQjQ880RVSt7xhqUml26tm1q4nlzTKJqy7PMhZc54V7jfKFd05KbpgRHVgt4y_9jd_c4wqEazdIG9fKDKoiYvNbD7rumzNGi0APKP-pvCZcCxZmzqDyL04VmvTnmwQMhNC2FARLB5OECNdX1cTry1WTXqGz5ym0xI4lum882D9yWrv_9wfc44eWiIs8MLUgMS2THYNW05n2tQDH-No4DuS8Ppg0w6FWKl-kNpdaU6dmWDBHtxXhAVFKUYJQGZ-CvgTiXHosmbu-0H60pkGaqASt6rd88XyqhsChKzXyau6PLnHLeOKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a86330faad.mp4?token=Hhp6M_FVZHpGs-AyIMTeRW6C39irI6KjlQtpQjQ880RVSt7xhqUml26tm1q4nlzTKJqy7PMhZc54V7jfKFd05KbpgRHVgt4y_9jd_c4wqEazdIG9fKDKoiYvNbD7rumzNGi0APKP-pvCZcCxZmzqDyL04VmvTnmwQMhNC2FARLB5OECNdX1cTry1WTXqGz5ym0xI4lum882D9yWrv_9wfc44eWiIs8MLUgMS2THYNW05n2tQDH-No4DuS8Ppg0w6FWKl-kNpdaU6dmWDBHtxXhAVFKUYJQGZ-CvgTiXHosmbu-0H60pkGaqASt6rd88XyqhsChKzXyau6PLnHLeOKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری مردم بافت کرمان برای رهبر شهید انقلاب
@Fsana
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/447564" target="_blank">📅 15:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447559">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TPjRcfyHwi3rHWMHOhu935kIX9VUtpxUXvMqCnwF8CisI8HuofBp685JmQSSWvar_3X5dKaYDrmALXyj4DXUxbyD0l2Bl72GrPimt4Ko-UvcXANqW_zS0Kj5RQYiBq1i1rj-FCXwbh-1pnDswvKaT04Cie4zw5ie4lREyn3FpNYdjjpqOEvYWEOaFpDRHBCfM1uMvJily-mPT1BDqg8RmR2iu_bmVXm1HT2w3VntAqkLRBwtkQLcUh_Vcumqt1hpotErq5HanccACi5oWEKjxkKCvk9z4BxZFZloh_1oO-WqumNyeEbz6pXFEERdNbakCTwylkHw8NpAUaIfxKLSJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/axj43F6rN-Uaovv0hxl5Q68Kv-gximpAwqnH151jZk7_SK74DEZqpP-SfIRKBwIX9wFRsvIMEy_1KdMjc6IdaFqL3PdyUYmEHDPtNJcxLEwNqPq5RMesTJsb9mN6dYQWWs8KbnU4cjtO1a8v1hKcSZ3MFzG7oXzOcswsx05EhT1-7E-GomdSBnO1hDL58nSFowxevdhuqgAdYXDj0ozbj1UwpbbHop0tCzSVRKCnEQ8gZgnLFYVQw-9hYf-Hg3lmA-ND3kxZyf1qpWv-LJk_UeS7jZJAL0oy7FS_LE09atsju5pj6ZtjEROpULsnjtRN50nFjlcakk1ZCHIXDXbe_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h8JCESbCn_i0SCnNFGh7jyzAfmlnU1nofOv1POjixg1-HLyPvnwLulMYaXmcPYM4ERixtU8yV-gkn8I7Yw7D1LzurUkS8fqiT8HUuGdLQ9C-EE42UYhs5YCQ8Ddbzn6_wK4iatY67DoLwwqCmtnoImhlcYWmM0BUYqYWs3aJ1XAGqlPc-CDvKAMTeWt0GZnzqQMK8MLOyD7trWevgV-8TzQLhJafHq-VyVR7ic9jg6iaGhYAr6AbhA2u9cuAfQL7LOubFzlYOYgfpgF9yJJvfoau04PKIsUhpaAY6YGyk4prN3xWVofKxl5GFaHtEVgMNg6RxjfB6aZpp4PTPsDS3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MFUMPJrH43C2PZfaDluBLsDINs-6a0TFf4tTZeox9Tx9eCQcuLGQU6nRZ8p2ti_QdoYZBVhBRfMh9vQN3WGnlPy3kkkq0lkxJnoZ-fW2rc1RAfm7cE8eRhgPGCFb9McxIiFhMT8x2heIguv6rXMthRDAOmiOIA_QiA7kvwvTPjcVH6_HxjBNDtGDb2UEZwohqszB00B992aieqRi1q554ycEcTtY7lToQICA2O8dwSWicVYiQf5eyseUn9gaBdElBejZQe4PDbf6-TXWYDmYP4Idw06931w_bOhvTe8Cv9cJmdCfWG_qroe3Eb52Cok0OwtA8QJhpuBK7II2plQWjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fPxV6NP4TXYl6tgtOMn1b_ESXLHlhh_eYql7bHNGZNiSIg80G7Jjye3s-pNXIYdinVtXKkoMF6sNNn-VJqceYk0ypkj6dnugwCDvUuK0wVr5bKV7vLhZbzc6ShauhSrtiCxIi5KSb2ZBUIh1Xhn2TpVK0W0SzsFYXfH16RzInBFEkXtGZDe-57MJJ0eVVivWmSpZmsZ96XP1GhdNJ0rDyBd3ZhJ3IPWmi05kAGN9e7XaeIbJj-wTgACyHa1BXU2DGp-OpXaIWZJH5qwiPgphZoTS6tffzeIcCYKgbs7gMZ0FwefrVf2TKWwfd_lAOYmqGkJ204ZJpqiSk4r9CXbaAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پیکر رهبر شهید در میان سیل انسان‌هایی که برای وداع آمده بودند
عکس: محمدمهدی دهقان
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/447559" target="_blank">📅 15:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447558">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8be8b66395.mp4?token=vaqDLJefvmfzj8FpFOy7fLS3dMLxTpg2i2hhmjlXSTo_6wGCLRDc9_LMiu1GXsG2v_Mi0WC3q2W_5LqpYEFPJ7QQWLE-05-KVrpDn1YJOyRG2CgRJt9kUlU5OLzBTupEA3AGU_loCVdQh0Usy30FJzvCJnkWXlLpR1wFNuk4NF3dM6wtw3InWNCI3lk9P2rDwcZGNTP-rYi-WW1vwdT0kaK0U-gzHTw56BJ_GlLnwBDTLIEuwq_wxa0GDq2VqRc-ubXl8FE4YsRKx9lrSFHLeNyPDoArIaYQJ0wMEGVWxVErxNOWVUoFZWi4dRshZY7PfbjuglwPlZJZnRjWbx860A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8be8b66395.mp4?token=vaqDLJefvmfzj8FpFOy7fLS3dMLxTpg2i2hhmjlXSTo_6wGCLRDc9_LMiu1GXsG2v_Mi0WC3q2W_5LqpYEFPJ7QQWLE-05-KVrpDn1YJOyRG2CgRJt9kUlU5OLzBTupEA3AGU_loCVdQh0Usy30FJzvCJnkWXlLpR1wFNuk4NF3dM6wtw3InWNCI3lk9P2rDwcZGNTP-rYi-WW1vwdT0kaK0U-gzHTw56BJ_GlLnwBDTLIEuwq_wxa0GDq2VqRc-ubXl8FE4YsRKx9lrSFHLeNyPDoArIaYQJ0wMEGVWxVErxNOWVUoFZWi4dRshZY7PfbjuglwPlZJZnRjWbx860A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از رهبر شهیدم معذرت می‌خوام که به خاطر قضاوت دیگران از او دفاع نکردم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/447558" target="_blank">📅 15:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447556">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Usbl27O78G3TX4evmz3QE_oHXC0PbMVarRYO8og5r53b8JNjwAKEuWZZISoeo7vJEh1D02jsN3Bnyfpnf0g9NgVePo5W3WcJEEJK8QZ53fYTTAKKcwRerQnfzivIoXyxJ9HEyj7l1A79R5o9lecO316WwAX3SD_OrbJkGkjWDXqhWDdt28tSCkeKhyQZx1MNcXqJNgYmoT9Gx-VSJ5QKmlw8xeH-sazZrhzGsEHZZSZzLUY5musgXYn3_ZUPt5ikCRBrtuxHSiB8_eXHbIGMP4vgxIdlUQyYbKO4ScayWMSe1WDAqbbpCEYQ5mcBhQ7FfOzNQrdzxb4D3cILoz4i9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bVDEFzVwBAHCc7eqhclwd870ES4Dy8UsdxWUg4u8LuxpxBdRDqc1xkzpeK7JaDvKRM6rAJIiqphbOJVdNZbt5Uovpy5Vd3DrbBFjr73cVE0n9_29QghI0UEhcEc076CO_1xzcj3uvvYi_6MZgXtnTSh0w3Go-RSi96xC1eXnzU0Ge-AJ7afq2pCh2YB__r7KeH0EsQ-dJiEV6HhNAJjT5Z04vXw1ijbx7y948Pzc_eTO_S8jcgJcUIST2OpK2q1bjo385zhHMF8Y4bknAqSZDQgcQLjVUKM2RcThEmG9QhsbXmZWNRIyMeEk5_G6A1xvJkW2Dt_vVN8Xk-zXk9DUGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور دبیر شورای‌عالی امنیت ملی و وزیر ورزش در تشییع پیکر رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/447556" target="_blank">📅 15:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447555">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9930dc6d55.mp4?token=FQEWzcJkYR1v-N1GhZb-pcUUytqARUlsk8LOVV5IGSy46vcVbvvZl9ay7AfLR4287M7UrrbMjReBU5pOZ5HXMpRzWsz2OuJRluwpotM79Q0H8SpWD519HHUOssDgHZzFAXTi3rBzgpbA-nBaSNASEFEhstaaBRnniBC6glh9mqXKHzz7PvpVQGAHdYLrwhh9PHtenmX1l_R9A_Tv5UfN6fTuFLOuIT6NaDTRlEOgiFYXUA1hdf5NyYN3c4JGDFUP6wgULAhT4rqdcEYZasq2Di2p4TvkTxm_rsMlJu7vJYb90eibeOTBDVzFdYlcVAzXnohpcKceOctbu5TnjGWEeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9930dc6d55.mp4?token=FQEWzcJkYR1v-N1GhZb-pcUUytqARUlsk8LOVV5IGSy46vcVbvvZl9ay7AfLR4287M7UrrbMjReBU5pOZ5HXMpRzWsz2OuJRluwpotM79Q0H8SpWD519HHUOssDgHZzFAXTi3rBzgpbA-nBaSNASEFEhstaaBRnniBC6glh9mqXKHzz7PvpVQGAHdYLrwhh9PHtenmX1l_R9A_Tv5UfN6fTuFLOuIT6NaDTRlEOgiFYXUA1hdf5NyYN3c4JGDFUP6wgULAhT4rqdcEYZasq2Di2p4TvkTxm_rsMlJu7vJYb90eibeOTBDVzFdYlcVAzXnohpcKceOctbu5TnjGWEeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیژن عبدالکریمی: باید به این مردم و فرهنگ عظیم افتخار کرد و بدا به‌حال روشن‌فکرانی که از این مردم جدا هستند!
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/447555" target="_blank">📅 15:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447554">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wdb7B__alOP5nsY0IbW5uxHxReUe5mMoG7iZMzco-8RtbId1_0RnHBsVbHMBPajGtbTggUn8lmgMo6Xu6vFU-hkBjg0KX2FKo4rBGwYQrV1ueEHEUMf2-sr3BwZ3wNOH8-0hp_FomeP3EQKXfHkJ_UAovC-ySjY6s06jhCQy0vb-oRFZGG-cBL2Ca2ws3771uQAAV_7WqX5z3sfl5tJOzkPbgvZqukdhXewgHnXFUCithNe0B7DfXshMZclKfxy3qu3GFbwI4EGJi8gfCStH2yqZMBxHG1LxIbzGYSsLFuy70JK_z4KEtlFqbGD0jDaT-yP9jFxZg2EFBjhGr3lhSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس اورژانس تهران: تا این لحظه هیچ موردی از فوت عزاداران گزارش نشده است
🔹
تا کنون ۲ مورد مصدومیت حاد ثبت شده که یکی از این موارد مربوط به بیماری با سابقهٔ زمینه‌ای قلبی بود و مورد دوم هم یک مادر باردار بود که عملیات انتقال او با بالگرد امدادی در حال انجام است.
🔹
تا کنون به ۷ هزار نفر از شرکت‌کنندگان مراسم تشییع خدمت‌رسانی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/447554" target="_blank">📅 15:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447553">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f42a6017e.mp4?token=kzwSS3Zz-O3kD1kwb685s4boy-So9aydQQyMSKPobnYoDdlN1JlQgBqzkWok03g_PZen-UxhMINSBN9FGo7QCvI1sm-igCyucAYjInX9rBY5fcJ5B0fyhR4FgV7v02rg9CzFjofHpubtf-a4NF1EGLgwHkxKeXdMf1PKNbW4T2Tt4wxRF3K_hfPmYdm3fyRzygLJF6WhNaSY9VN0sC1m8qRL78IpVLxNiNkQxjOKV82BzFJXujDbsZd66e1IDX-Fd1kfrh3e3_Z2nKAqaiUH-EgQhwZ0SjojCufBbdCTRPL8BEJsy4ULDmwH_wMq8djmkLbp-yD7RfKt3iVGWYFFSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f42a6017e.mp4?token=kzwSS3Zz-O3kD1kwb685s4boy-So9aydQQyMSKPobnYoDdlN1JlQgBqzkWok03g_PZen-UxhMINSBN9FGo7QCvI1sm-igCyucAYjInX9rBY5fcJ5B0fyhR4FgV7v02rg9CzFjofHpubtf-a4NF1EGLgwHkxKeXdMf1PKNbW4T2Tt4wxRF3K_hfPmYdm3fyRzygLJF6WhNaSY9VN0sC1m8qRL78IpVLxNiNkQxjOKV82BzFJXujDbsZd66e1IDX-Fd1kfrh3e3_Z2nKAqaiUH-EgQhwZ0SjojCufBbdCTRPL8BEJsy4ULDmwH_wMq8djmkLbp-yD7RfKt3iVGWYFFSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار «فرمانده کل قوا، لبیک سید مجتبی» در تشییع رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/447553" target="_blank">📅 15:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447552">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLE9XIfYQe4Hy57mTm2caf-1V1FYQag-jq5oqNTQj2rM8U0r5okwy4ZNc5Lf4VPxJFzhWFn4G_pRJcRpSwP0TmOAfHNd0SwYsplnKH-9BjfeYvTqGEqkDp00TTR5yz88x7OMmwZY8lTiE2hgjAveqNqM7xLGaa7Q-ZbJuKWRSogdGbH8FSxGqbiQ04qwdqQb7akluzoaAJFkWWJp2oQ0AkOa10Rh2Yba09Oz2vDgFivrEHMBQjgzqGvyd5EP3ArbKD6cd-vpymO6hYXtCke3rsgsPnGT24IE1Pw14kZbGf0DA8tZjymNBjgYQTAKrtcq5f9YoB1-Rj-V_H9dZciotw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه شماره ۲ آستان قدس رضوی ویژهٔ مراسم تشییع و تدفین رهبر شهید انقلاب
🔹
آستان قدس رضوی با اولویت قطعی تداوم جریان زیارت و خدمت‌رسانی شایسته و ایمن به زائران عزیز، تمهیدات لازم را برای برگزاری شایسته مراسم تشییع و تدفین رهبر شهید انقلاب اسلامی و دیگر شهدای…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/447552" target="_blank">📅 15:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447551">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e0e772f65.mp4?token=GBwwzc9Gf0tzUPkikmAVV7AyQbz_IyUJJfNBkAJgAaMM3T5genT04XB1aUDAno47W_UY96p4XVetUx7OP7NDdzSBSRa5uv6UdWLHzMWbXsqL0U0QqmqfUXdjm3qyYbOA4Icew7EcOX9IFYAFaVSLxWKh16TxWsg4jfuIbkbRowXWFpvtp1E5DnHXdZ9pL9oKA5r3KOkxZVCUSgvqq3LzUmS47UPEALo4Vq8B-cm6Ynryn-jDfZrlvvBDLmOz3-zms_FTVD4rzmETX2wgLjCcqwCZH2wnO0nF2ODgCJ4zhC1KxVAmDHVVVqOpRy78CMPqkLajqmRoFMWrJdezgnmLTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e0e772f65.mp4?token=GBwwzc9Gf0tzUPkikmAVV7AyQbz_IyUJJfNBkAJgAaMM3T5genT04XB1aUDAno47W_UY96p4XVetUx7OP7NDdzSBSRa5uv6UdWLHzMWbXsqL0U0QqmqfUXdjm3qyYbOA4Icew7EcOX9IFYAFaVSLxWKh16TxWsg4jfuIbkbRowXWFpvtp1E5DnHXdZ9pL9oKA5r3KOkxZVCUSgvqq3LzUmS47UPEALo4Vq8B-cm6Ynryn-jDfZrlvvBDLmOz3-zms_FTVD4rzmETX2wgLjCcqwCZH2wnO0nF2ODgCJ4zhC1KxVAmDHVVVqOpRy78CMPqkLajqmRoFMWrJdezgnmLTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نامزد ریاست جمهوری فرانسه: تمام دستاورد حملۀ غیرقانونی به ایران، تقویت نظام بود که اکنون از پرستیژ و اعتباری کاملاً بی‌سابقه در جهان برخوردار شده است چرا که ایران موفق شد نتانیاهو و ترامپ را به‌طور هم‌زمان شکست دهد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/447551" target="_blank">📅 14:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447550">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmtooxl7mCS9SDP8dAyOJTiH5jlWOVD58yNOggiMob4J_PgXVGHJeCOIz69Xppzb1EJN2PVIos0tM-YkuqXi4tkliEVE3ioedHCDbPqXY_Vf6aqnEsBjq0AnDClEJM49XsYYmZM52ndd3rqdAc888C8i8M_MnSfegFmGQWU3YB8DYzNfc3D5RPXSeOj7M_YMtH8etW56oskmxoOQbXP-45C7Alv9rX52SLqgR_Ft9w1b7KxHboij52Kop8D4cN_VYPw9YGuOGap7W7T7iwFMrV8QdGIEuO0k9-TdtGVqQgCwJQLEVm8zFFQiTXyiI2WT_Lcc9GUqY6bj3YcpUx8K5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
۲ میلیون سفر با مترو در کمتر از ۲ ساعت
🔹
همزمان با آغاز مراسم تشییع رهبر شهید انقلاب، در کمتر از ۲ ساعت، یک میلیون و ۹۷۲ هزار و ۳۲۸ سفر با متروی تهران انجام شد.
🔸
به‌دلیل ازدحام جمعیت، ایستگاه‌های میدان انقلاب اسلامی، تئاتر شهر، دروازه دولت، فردوسی، امام…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/447550" target="_blank">📅 14:58 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
