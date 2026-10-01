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
<img src="https://cdn4.telesco.pe/file/bwaMKbaQ0tl2qFfmCtEE4xRXkzepqC17cHGG7IZcE0Igo-X-PIHVQHuoYlDZBIGLR2iVcUfrcVPouA3H7mFKV6C8jYEFSYKbsxgoqtjzoTo5ASs3lIqMLWJI0wfVmtUhb1bHkYg1nFLrfHi-uDco9vpKaqDyBPYvtMDd0HlxgoT6mcqhcTGEp8-K82RNDgaiDaKy5Ierg0-CestEpn0m7PrJLVW2aIvSwqsKc0lhSalK7YH_ShxkYSdiSK4Q_6wBJPpipnBNw9YIDpZ6LBOVww5qwJt3GEhhrOOH-dteER3b3fgHaNLdOBs9PKMsxA6Pw6ciyDj4cyoQC8xUrMnfRA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 429K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 17:07:54</div>
<hr>

<div class="tg-post" id="msg-30797">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsSBZWckAQoy4bxlAjTuSkQO26U2Iypni2SwK2VaXA1KDTCc76_RBPFUz98JZjLt0LudpiM-fS43ov78Twuqnfmv22f5YKqQ-0ufhm5LpjneWymwhqGk5l8WKR6zP4S42CWrX4BTnex9D-3zWiB8XEVlRqxnHjuH1uYcJvZKtCSU_2UyoJGkO_1hYyfLon29JxtlapjZUTDHsuhQT50FVruQcUIfiGWWy9wF1qdLFwTq19vfbSnwQdBXB6iJ1ey-Htop6SlDqlHqhAmd4bQbhpUYyoRmlJni4tDiTgqer-HJcCE1fLtNMyHfwct-8GVO90WQzb9aP4qQbgzYDpDqNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7281ae07.mp4?token=Ic3JjANhBRxaZH80q_jlISG1CponJAHn7NPKDKKMjHAX0lhMLwR_m-EpiwBLnp9OIG-v-UVBh5bm4uDnRX_AYVHbYJ3p0miP4mDLzIa8t1T3swec_r9aYWCtneaA_7B8gUTD5wHAUSCFjqFPBKSsiUmlxdgztcsCz2qBQ74twC4bGzCy3C3VoGxVEPWQ09WkDKGsiWbm9pg9HfjphSrBWr1R0eV1RL7oupi3ehq1vL1MFzRMEKFAB6JBjLv0WMIC9ZfgDquCqWYIKICTimiZskYM0xq-fpTK8UNXQZNrM9jvuenDx4X3fwAk1kClmMrMt8EZ6x9yLxyJd-DSh96fwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7281ae07.mp4?token=Ic3JjANhBRxaZH80q_jlISG1CponJAHn7NPKDKKMjHAX0lhMLwR_m-EpiwBLnp9OIG-v-UVBh5bm4uDnRX_AYVHbYJ3p0miP4mDLzIa8t1T3swec_r9aYWCtneaA_7B8gUTD5wHAUSCFjqFPBKSsiUmlxdgztcsCz2qBQ74twC4bGzCy3C3VoGxVEPWQ09WkDKGsiWbm9pg9HfjphSrBWr1R0eV1RL7oupi3ehq1vL1MFzRMEKFAB6JBjLv0WMIC9ZfgDquCqWYIKICTimiZskYM0xq-fpTK8UNXQZNrM9jvuenDx4X3fwAk1kClmMrMt8EZ6x9yLxyJd-DSh96fwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
استوری الما خواهر کریس رونالدو: خیانت، غذاییه که بهتره سرد سرو بشه؛ و هر چی انجام بدی به خودت برمیگرده. تنها راه رو به جلو رفتنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/30797" target="_blank">📅 16:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30796">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPF-EGoFLvTtWIha83UapQZudJRhQp-yIu9tsZZXgoQYF15s9jA8dD_6bwK0QsHUj-5PDI1oWQi2_CrrFS2uINbyV5emyKYLDMBhgLBh8wAe1UaF0L9GW3gWp17ye5hDd5N33oTGWj-67qOOhDVe7cp3O-voEbSou2gx4GnaXpTJy1amVGr9_Bh8mg8YhoJSG3gfEnI6GnewmIYGYtNjSFDExFGl3sPO-O8LNE2gkC2KEUykGe07ceS5xTm5uZdDs-xggtYtPsp2MiJvJW8wBdZASNjNgbySHtZugjiaJ-XXqaoTazvy_9W_YTZl0GKSvEsXZjdXULIbgohSr6RWag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
استوری الما خواهر کریس رونالدو: خیانت، غذاییه که بهتره سرد سرو بشه؛ و هر چی انجام بدی به خودت برمیگرده. تنها راه رو به جلو رفتنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/persiana_Soccer/30796" target="_blank">📅 15:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30795">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sss7PkOj1qfNoXMoyEAv4SXXRBi89Tv0F8oftpb07ED1ZKFIo_V_fp5HygyT6huicOyH_Rh2JUr3GUsu5kUCbb8QPgmZAPKo-LhX30E7Qjhr2z5342SpgfD6umPKzA9Du-k3cLtYsxVp9_lnZ5hO1OPDvI8AlPTD6ca7sP_TCN2-lAF49XwoLBFf76drYHwpYmtTS2lkEZ2bMZ-WH0-qENmauTfEQiF2RegtAaEk6TYyR4vpqmGWoSB_TcezQcOlPkTKIXFefQaH56UG3UeJyU6S4_5cSprJJtBQjxEXD8VcK7uN2MKpDC6QTvyMYbSJqzxeEeYRvnQtLsZhk3AJ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استقلال درپست‌وینگر از بین‌ مهدی‌قایدی، یوسف مزرعه و یادگار رستمی سه‌ستاره النصر امارات، فولاد خوزستان و فجرسپاسی دو تارو قطعا جذب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/persiana_Soccer/30795" target="_blank">📅 15:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30794">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUz-10UgH5KO7qlmmWlslmHB6bYyClI4VWaC1Gl9hOAvfI0S67szrAHnZYHHvO4hoejE9ZnybF8H8dFD89EgclWa5yG2BWhzVZTi9IAnHWwtKT5lO9xWPzd3TO-YU7QWDbqsfVfaR0AQWaQBZ5e4V13mRaQgftv35ban404YAwCZzcU770xSzWMzTuvCErZU5WsplIfXJ8f2rySnOhZVXL60cH61EnY3lX51Cw4xXEKLEFuXeGus4BsQZ66pXHxx_XST_zV24cLIg6RBbhoIUIk0OmiF5T_viT7-bdw80IZ6q1Q3msghCOoC-__3Jd8W60kxkDbo57NUoI-vy1_tew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌فدراسیون‌فوتبال‌پرتغال؛ بعد از 20 سال که شماره هفت این تیم برتن کریس رونالدو اسطوره تاریخ‌فوتبال‌بود به رافائل لیائو وینگر این تیم رسید. خیلی خیلی بی معرفتی شد در حق کریس رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/30794" target="_blank">📅 15:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30793">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2f2713791.mp4?token=lXBFG6ihujt69Qwv7ZCKVShdJ2nvHbduui6gvLRrLh6xFYu0zKsiLvfktd_9H60JFyJUsLqHKuAfpMz4-D1BA7snwv_kPeHyLACxFfkqkZOPRMZ1q20EoFzVNSGkcB4VUI2QBmPEZksVLA8g6QBUHuOXzfeO-msVWzLz8nAY-tO0sa2bMY4UD6qOR6r_WM9Q8zL8vUFeRamDqpsoMMU8wBopPop__9rExSu2iz9GUCECq63ruF2H-Tl9sNaM-k_iMpBkfdTT5GRkDP_sMA6oLMVj6-jC277As0p50347YyHgsBl9kYVNQ1ZuZDbHxlbD6w7sojtbX8Mn7rOJitvn5TMjcKIcXkoFeyczaX8d4AE31JQtz2Tp9-f9wXQQIFqqFJ0FAaM0DdII2RxmYrWzyhResoYRRa4fN0rVYB6_B3GxGQy9P4C6K9osm3zpRP6LHY7enrD7cWfmg19Q2efV98EkJu68gmvx4cCn3l3X7I9aQp_tDiAgEOLQURHck4gBUto0mVvPxcMw0p7qNMtzb-SUnsDsIAzk74kA47gsoeOOxPIdvtxJDHqgFfqm86gTXmIsBG3GmqNvpkPQbj211qfPVaXK91S90Eh1yZZXckvCj0FsAgznaO6NpTZaPOBHWmxNdWKNQv7HMDki9m02fOJ1QQfn8l_7SjcWiDNDHp0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2f2713791.mp4?token=lXBFG6ihujt69Qwv7ZCKVShdJ2nvHbduui6gvLRrLh6xFYu0zKsiLvfktd_9H60JFyJUsLqHKuAfpMz4-D1BA7snwv_kPeHyLACxFfkqkZOPRMZ1q20EoFzVNSGkcB4VUI2QBmPEZksVLA8g6QBUHuOXzfeO-msVWzLz8nAY-tO0sa2bMY4UD6qOR6r_WM9Q8zL8vUFeRamDqpsoMMU8wBopPop__9rExSu2iz9GUCECq63ruF2H-Tl9sNaM-k_iMpBkfdTT5GRkDP_sMA6oLMVj6-jC277As0p50347YyHgsBl9kYVNQ1ZuZDbHxlbD6w7sojtbX8Mn7rOJitvn5TMjcKIcXkoFeyczaX8d4AE31JQtz2Tp9-f9wXQQIFqqFJ0FAaM0DdII2RxmYrWzyhResoYRRa4fN0rVYB6_B3GxGQy9P4C6K9osm3zpRP6LHY7enrD7cWfmg19Q2efV98EkJu68gmvx4cCn3l3X7I9aQp_tDiAgEOLQURHck4gBUto0mVvPxcMw0p7qNMtzb-SUnsDsIAzk74kA47gsoeOOxPIdvtxJDHqgFfqm86gTXmIsBG3GmqNvpkPQbj211qfPVaXK91S90Eh1yZZXckvCj0FsAgznaO6NpTZaPOBHWmxNdWKNQv7HMDki9m02fOJ1QQfn8l_7SjcWiDNDHp0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استوری معنادار رضا علیپور اسطوره سنگ نوردی ایران: باخودم بستم که. گفتم رضا: ساطور میکشم اون شکمت رو که اگه بخواد کباب مالیدن بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/persiana_Soccer/30793" target="_blank">📅 15:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30792">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OH3gDiHxm8PnxNGwts_IukvJh-TC7BZ0ZNYFiGkGvzXneInKKfuh3BGpXn5-ee6yfuVlTOeBVNgcBbJuNIGry04nWN91zWHRy9dLx3fMXQmC_fFU_j1ijfr3WQXB0WV_nMZNVA6s_6NySkSTtaGQCKdlf0MCjJ1hAKaXMX8LN-AM_YA3wuubEvvLgH4-t2x20rfEAZB-9CoRob4fJwNsV8jYuFe7OiO0voF3aJkQGfbeLUmlTj12dVw4zjhHzf3KSMqJsZg2JAl_aY7ZZYwfBnAxya7_onRJONPyM3uPaOWEIoBeu2rrZM5FBdKHxWpSP2l7cqYpMkVUP1V7zxpJPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
با خدافظی غریبانه و تلخ کریس رونالدو از تیم ملی پرتغال؛ بلافاصله کادر فنی این تیم شماره 7 پرتغالی هارو به رافائل لیائو ستاره گالاتاسرای دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/30792" target="_blank">📅 14:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30791">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKOlyOksXnznVd5XXbTVRr9v_v7JYHEYAVEU1WvUWo6rRTTwzeof2SdGVufwUs1U-JCXY_sRNVTIEsCckrZbbOHuya04_jnKOi1u1x0DruyQQnN2uk8d2-YOwZnt0c3YJJv6VCFv6Y7dn8qRJcLgFVQ-Bh5HpmMYGVRcP1hFzyc8MeKmTVV7-2-umluw9g2XBVdCHrDQPmiaoiocD4hkhMUKUxdf68RFgqoKb-i0lSmAQd_zXbAA8_U4vvVjz5FmrzfjHP4YPpJ4lPPn9Qu7X9vRjmXdSSnM8qbktVyzRBCVWIbW-fn5eU6A9Y1-HS2bZF2tOOyeYFDxzA9am3GpcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام باشگاه رئال مادرید؛ امباپه تنها دو هفته دور از میادین خواهدبود و بااتمام فیفادی به تمرینات شاگردان مورینیو اضافه خواهد شد. بدین ترتیب این فوق ستاره فرانسوی مشکلی برای دیدار حساس روز سوم آبان با بارسلونا در الکلاسیکو نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/30791" target="_blank">📅 14:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30790">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_JTN9UoyXGWm7Zp_GVg-q5LKz2dv-PeusHqsZQb68ll0SxNK7XhLPqubALeZUinsDArRpwRFRdJlFyQbzk3qN8IIWWyLC7jk6Q3-QRyjzRgBJyNvA-P0VmQWU-GYPae20-ihtZgytDjNbKqB-6W5EazzR_gsz_MyC1YgS2q_IcX1aFJ9NWmCToynI_tK80QluKIeOzAZo1rKlnHSrccoiv_BRiMvSBREWuPM3r9SVVkIDmN9kAR595CILg-ZICxDDK9W7KDM45gfo9r1s6Rjtos0qgTwS_6HJjf7mDKYWXbIYyQMdTCedCssfXHBFSEJBxBRGK8dBn5Llqpuz-Gwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارلوس کی‌روش سرمربی پرتغالی سابق تیم ملی ایران قراردادش رو بافدراسیون فوتبال غنا فسخ کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/30790" target="_blank">📅 13:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30789">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFCpDS2avMvcxOmKPLEm-aHEC28ztrZDKb5lhYDW6GT3CH_oNOWno3o6N65vHrOoDUU6T544_MuPr9nB1UbaembuDyGJt7K6E_eQAJiI4XAQY5mj5UgVutZz27Izag3aCFo724L694R1TOlG05Vi1onJL_nT_x-UhFYyQrDeg_9mnv3mwSlR0qoaCyXP8JmO9hrwlcKn9REiswcMR0glYO99xDZo91KYzbrkxejpgvGmI2uqrFR6U_94CU4rmC2toBJJ3QdEwGtgMgMNKWezzytrZ5MUp61Z-iBx-Dyg3FxIWi6F9gh-Kbol60sc-Tko0u5p8MOOtP81WxL0uzSt3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایرانِ امیر قلعه نویی
🆚
ایران کارلوس کی‌روش در تقابل های خود با تیم ملی ازبکستان رو ببیینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/30789" target="_blank">📅 13:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30788">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAgNKKx7G-fAYUIINrZVJRvcZa2lzI_vcxCZ9Bf71jNuhLxxyAzb9sik2_zSmmWZB-2zrT-p3ZTOGhSwpc6FVU1EpCQavnF82MmW59ncl0Qf8PU4cRCXAcKGTZp14W8ITyLQADaR9h-Gyz9YuKYdwBmtT5_IKTjn0PRb8LOVRFReeayUcaJW6eAjqV9n2zuQbqZVbXTpNYFXecx3W6G8d8D-tRPh4MyjLZcImnBrssne9dC7d55pOSTN7beMbwaGW50dAbHRpJ-2gJW-_814xSPdLQeU7pVPD7HMoKRA5OYDo_nQP4-YKBIXC_JgdAgEcOelnVpMipnETXHjtoAkRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
قصه کریس رونالدو
🆚
پرتغال هم به پایان رسید؛ قصه‌ای‌که‌میتونست خیلی بهتر به پایان برسه و شان اسطوره پرتغال تاریخ فوتبال حفط شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/30788" target="_blank">📅 13:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30787">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXTXG2Tpld3lCleVKeWuzlyW28lye7D-o3QMVV2Hw5ke6YdU4YozXnyBtHqLXtord_IGE4VRTNaq16g9Wa61cqLrVs_i1Uj05d9MqEyKJyMySD8bvz4Uy012FWnKeLghQzC115Zr3SQ42xuhaPRS8CaHuo15-OHAuXWiFnUdl4ogHsvDk1iV1AlJnTSlb9ncUWscit7mEvmjJqyh5jHwSQYJ--u_xV7llIHNQw1FHn45DD9EyhYn88Zrs6MXQy367uBQfWWa5dcBZLjmwaQ09YFF3L9bBzVlqU-Rqb6On0m9_Ca9YeOLPxvxjpPRkGbkaJtOF-f4ONaEE90A1rYNYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه مارکا: خورخه ژسوس و رئیس فدراسیون فوتبال پرتغال بعداینکه فهمیدن کریس رونالدو اردوی تیم ملی رو ترک کرده سریعا خودشون رو به فرودگاه رسوند تا مانع رفتن او به مادرید شود اما رونالدو به درخواست‌اونا توجهی نکرده و راهی مادرید شده. این نشون میده خدافظی او…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/30787" target="_blank">📅 13:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30786">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcI3lDpCgPtDe1nz8nxygtob7KHyG_4FT7iOb007541Pxucpn0Pg_2IZKw31mPddA_MEsh1wdWjTbsEvQDSSEZ7xWlLbvSqmpz14um5eU1vVrl3_AMi99Y4p78VMp20s4251NHm7DVLFXCPchtP1MQg8nO6ulEXZk3q4n7zZJCRaeRzq51OS1ksITmaZcLgxROm7n1FE1GcNNPbl36liAZMEH0oJOfo8x9sgmpG0OoljljXQDdf69A1vXBYpmtHBof2IRJhmvLGr36YkxyUMAJkWpyCTvVpUic3yP7rRLri50I7s8w6WydromyMQRcKus08RZyYkuEwJ2uuwn6USgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده میشود که فدراسیون فوتبال میخواد که یه مسابقه دوستانه دیگه برگزار کنه تو اردوی ترکیه. اگه قطعی بشه دیدارهای هفته هشتم که قرار بود تو بازه زمانی 15 تا 17 ام مهرماه برگزار بشه به تعویق می‌افته. یجوری دنبال‌بازی‌دوستانه میگردن انگار این دو بازی چشم‌نواز…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/30786" target="_blank">📅 12:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30785">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5VDFBB9sdOxJA1GEsRpyFe4FHnUNMVl8favZcSMfI7FZmAfQpelsl_VSPrxMuzk0yBTdxBL_ckhdSVa46QV_tFwhwV_ogpvo7SHu_wcUgOCpTk-SNVpUgb7f0K3vLAO0iRu8yK1m41G7FV7aW1kt3pVkxXLsPndZr0gUYnh5xyK7ncPbxI3mceeifbyQ__yKXxY9Z6TU9IYiV0DkIeRpbIQZByXtgwdGmtUgTm-C26KPR4MfInPETqWxMwgQHfGWJ9oWdlE_EWbMfqU2bPFna3T6mPIOFdNh9qibapLaw5KP_wz-ROhpW7MwfhiGA7ON2PWQeqe71TshJfzzde6uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛ طبق پیگیری‌ های پرشیانا؛ مهاجم‌جوانی که مدنظر کادرفنی باشگاه پرسپولیس قرارگرفته رضا غندی‌پور مهاجم 20 ساله شباب الاهلی است. تارتار قصد داره که در نیم فصل غندی پور را جایگزین ایگور سرگیف 33 ساله کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/30785" target="_blank">📅 12:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30784">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/329904c210.mp4?token=BVuiG9u2_ZeZTm-KVMikLKx7UMtI_O6g0qcMZL_W15PxtB9fsQstqnIqtwt4TYzFYMKEGlAWBkIC28s1MD2C5ocPxn0UewhuqJQjGWWBSQdYSY9oLevFE-mIpE0UUrAmkB5KATKN2k1V6W9mMS-PEu0UfOkmHLzjzcldNAjsjRH-v0jPYuNEMcz3tHu9E51Q3Z7Qa1Woyfjvio7grHtbi7GqRWMhT9D0fH5bca7lJrf-QaOkGBdMvJlI5tPYBCseVkNQi5sFnDNjBDFXMNU_pqwTrm02pTMsGdJjI4CqJ2hgMzBxhh9jj8STJ1hVLl8ZeOJNmQmi8baWxWTJsdWaZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/329904c210.mp4?token=BVuiG9u2_ZeZTm-KVMikLKx7UMtI_O6g0qcMZL_W15PxtB9fsQstqnIqtwt4TYzFYMKEGlAWBkIC28s1MD2C5ocPxn0UewhuqJQjGWWBSQdYSY9oLevFE-mIpE0UUrAmkB5KATKN2k1V6W9mMS-PEu0UfOkmHLzjzcldNAjsjRH-v0jPYuNEMcz3tHu9E51Q3Z7Qa1Woyfjvio7grHtbi7GqRWMhT9D0fH5bca7lJrf-QaOkGBdMvJlI5tPYBCseVkNQi5sFnDNjBDFXMNU_pqwTrm02pTMsGdJjI4CqJ2hgMzBxhh9jj8STJ1hVLl8ZeOJNmQmi8baWxWTJsdWaZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چهره‌کسی‌که تو شش‌ماه‌اخیر فقط گامبیا رو برده که باچهارده‌بازیکن رفته‌بودن با ایران دیداری دوستانه داشته باشن و الان میگه بهم فرصت بدین بهترین تیم رو راهی جام ملت‌های آسیا 2027 خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/30784" target="_blank">📅 12:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30783">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb4088dcab.mp4?token=RNaYTUBRNhD2FX-_s7zE10AkbZt1tLric82A-POgB9SBjQ891ZIXGnG6opufm_D0NgjzS8Cj75IXu6dkzBZHRxai3rHg6BnlOXUaHo8SB4hoP2d0aNfbHdS9iFY8c13ThKFM3UFi1Slm9pJXfacZTW844Lv6dqh6YrgXXkhd8RFIIS4EWTZlbcFCZjfWsU1iaSAv85mgirJD6mfjpY9Dv-Oa3aG9IjlvNx152eCGWtZ5WLT2M_08rarFt-B9b2wMABM82l6eW64tBU8-w2wTT8wvj707_9R8dtDGYLGR9NInRuJ0v4bg9fTZ9tvqTSnw3ypJeXNsckTBIpXI9NC_lXlXHeExxwhy0RWgKfHylf_qwSjt-r2r-2xdyzPMEiQS1CCLOsH6pJpv_t0kLK_b4xl9wYNZcUEQg4vkZ5C6X0zgovswJFYkxnTAWonL1s5EMOimhnFIhi6x22Whr9_2-MUYRs0JwgPG1t8W4h7kZWMWimvOMTqibkTEDkLlsJZP0CsVTT-8diOH-BG9GjsaZIMyn6OonFcLPbzqC9EVO0rJZxezuXVGc7VNQNWV5elg1O7L29cUSSSfby52jB5voh_-ZN8Yx5KjcQe4sHM3FDGHtdwlpO9pbO8aWpszPMYjF7xc55PGD-b7mph8epnTv93rkLt0LDs1LFWwpH_yYyU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb4088dcab.mp4?token=RNaYTUBRNhD2FX-_s7zE10AkbZt1tLric82A-POgB9SBjQ891ZIXGnG6opufm_D0NgjzS8Cj75IXu6dkzBZHRxai3rHg6BnlOXUaHo8SB4hoP2d0aNfbHdS9iFY8c13ThKFM3UFi1Slm9pJXfacZTW844Lv6dqh6YrgXXkhd8RFIIS4EWTZlbcFCZjfWsU1iaSAv85mgirJD6mfjpY9Dv-Oa3aG9IjlvNx152eCGWtZ5WLT2M_08rarFt-B9b2wMABM82l6eW64tBU8-w2wTT8wvj707_9R8dtDGYLGR9NInRuJ0v4bg9fTZ9tvqTSnw3ypJeXNsckTBIpXI9NC_lXlXHeExxwhy0RWgKfHylf_qwSjt-r2r-2xdyzPMEiQS1CCLOsH6pJpv_t0kLK_b4xl9wYNZcUEQg4vkZ5C6X0zgovswJFYkxnTAWonL1s5EMOimhnFIhi6x22Whr9_2-MUYRs0JwgPG1t8W4h7kZWMWimvOMTqibkTEDkLlsJZP0CsVTT-8diOH-BG9GjsaZIMyn6OonFcLPbzqC9EVO0rJZxezuXVGc7VNQNWV5elg1O7L29cUSSSfby52jB5voh_-ZN8Yx5KjcQe4sHM3FDGHtdwlpO9pbO8aWpszPMYjF7xc55PGD-b7mph8epnTv93rkLt0LDs1LFWwpH_yYyU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعدادی‌ازسوپرگل‌های قیچی‌برگردون فوق ستاره های فوتبال در مستطیل سبز؛ کدومش خفن تر بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/30783" target="_blank">📅 11:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30782">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🏅
ویدیو باشگاه پرسپولیس برای یازدهمین سالگرد درگذشت زنده‌یاد هادی‌نوروزی اسطوره سرخپوشان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/30782" target="_blank">📅 11:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30781">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1IyiFIZlrv4tRH4oW670-osSpp2ogBzkhBl2itpI8kW3tDOudc-n3UPjuBuu-H7SVARa4J3Pvd3HanjtUXxhxpU0P2mweXpv_vvw2t13dtXpH4EsnHIxCJSCC4B6RGm6rTd74pPGdXBu69wJLwiDJUg_6by-FbT1jEkUNMijku4auPAaflFpCvf7HVxAI2tcXevTzB0QVJ22QhZpNT0HZHte1BqJnIMj5XMJliDHczEXcr_E4e4Wu1QSt6qOa73OC9mQuTFf5_SNilZDc_hqYKqQa0Etqq1cS3yBhEG-QEmqNVA7pSjAockE-8GnpkcgtayF8L8xQa5l7-mMgd_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
۷۳۰ سال حقوق یک کارگر، پاداش یک ماه آمریکا گردی و حذف شدن در جام‌جهانی ۴۸ تیمی برای امیر قلعه نویی! ۱۴۰ میلیارد تومان معادل ۷۳۰ سال حقوق یک‌کارگر، پاداش امیر خان قلعه‌ نویی برای حذف در مرحله گروهی‌جام‌جهانی ۴۸ تیمی. ژنرال جان باز بیا بگو خدا با من ناسازگاری…</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/30781" target="_blank">📅 11:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30780">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/657e5f9da5.mp4?token=rA96B9Pd2-sDB_Ezz6IWfX41I6FZab-c8DMSyhUSh4KtKcNqhPijGibx6m81mVyRbhLKgntGNROdQr9aTwB5sQetRIzmZYWwBjv4XI-SfKaMmBSe61hTOy7tLoRjtsZJ3w55ZM7vpO8ErNnyXInhknONnnu7DAo6a0EXiiMvTx34MuvYKXLAhQfShKq_Zit1E6KSrSU5LllxoNK1ykazzkE0DJr3Wrd-SD8ZE77ITS4t-1bi_XAogvLCpcBtyc1GNbQbKIuSqtfM0iOjf0W0kpUZmdLcFS1t25H8qHr7eOWAFjBKoaRvPdyO4CrsM0-PRTTcYCU0-GMMcK6m60feQzVLU54o-2LN24xWz7iOdOF8GVYBguIbc1ac8wRQOGTsuqmDvb8LZLkD5_Eh5CLZycxDwWrUuf2NadVa45OKAqZCYGm3vpKX6ajNABsNatMjDU221Iyz83t9YUBzRajhUQ7xZWFvNS2e9nZWwAJfT9QZWjFKdUefyYmxPp2BdBmVUn3ty0Scsco6h8js_FmUwiEZDqILVRkgurRyWKXtDLco6dY0U6_ki4GsdoJcFbEt9CdsQHkFVQ6tdgwUb6fDF_kMAWD4m7Cg03lnj-nfZHY-jWDAXbMmaMoDTO9fB6WiOi2j68p-Gm3aCIyqmjMZwM4b0VW7tvQJX4T_UAvZKXU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/657e5f9da5.mp4?token=rA96B9Pd2-sDB_Ezz6IWfX41I6FZab-c8DMSyhUSh4KtKcNqhPijGibx6m81mVyRbhLKgntGNROdQr9aTwB5sQetRIzmZYWwBjv4XI-SfKaMmBSe61hTOy7tLoRjtsZJ3w55ZM7vpO8ErNnyXInhknONnnu7DAo6a0EXiiMvTx34MuvYKXLAhQfShKq_Zit1E6KSrSU5LllxoNK1ykazzkE0DJr3Wrd-SD8ZE77ITS4t-1bi_XAogvLCpcBtyc1GNbQbKIuSqtfM0iOjf0W0kpUZmdLcFS1t25H8qHr7eOWAFjBKoaRvPdyO4CrsM0-PRTTcYCU0-GMMcK6m60feQzVLU54o-2LN24xWz7iOdOF8GVYBguIbc1ac8wRQOGTsuqmDvb8LZLkD5_Eh5CLZycxDwWrUuf2NadVa45OKAqZCYGm3vpKX6ajNABsNatMjDU221Iyz83t9YUBzRajhUQ7xZWFvNS2e9nZWwAJfT9QZWjFKdUefyYmxPp2BdBmVUn3ty0Scsco6h8js_FmUwiEZDqILVRkgurRyWKXtDLco6dY0U6_ki4GsdoJcFbEt9CdsQHkFVQ6tdgwUb6fDF_kMAWD4m7Cg03lnj-nfZHY-jWDAXbMmaMoDTO9fB6WiOi2j68p-Gm3aCIyqmjMZwM4b0VW7tvQJX4T_UAvZKXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خورخه ژسوس سرمربی تیم ملی پرتغال: در تیم ملی اونیکه حرف آخر رو میزنه و رئیسه من هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/30780" target="_blank">📅 11:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30779">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxQr1K8fqMbqINAD1VLKdxQYTIbdxTh9dJfLTw1fKcBVdenSnyivU7UPBr53lnifO8LIR7f_vmE6CCBVINw7D4u5J2uYP-JnHJGsCQiQGXqAr-R30iorEo__LJ1WMRzK7jL3vJxeFrxFL5wZwXk18ME25i9Zu2PRkGyUMPzX335CtOZ5Uo-BWF8bIbrojjcQav6rYPA3HZxlFwXSbSJxEI2mDycu3AX3Z9sTLg_NvRJ1w8UtQo0LclTqQCTLgS_wG40EcjEzdcjuy0MlHqkxVyjH0VRvIKzgAvSZnYa_nakZbO6D8n4U9lrYtbrUH5U711V6CZ5vNHnyqmXsIk1v9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت‌شده و پلیسFBIبرای‌دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/30779" target="_blank">📅 11:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30778">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdLw2JYtdm6b42ycuydhjBrJEVtgVIWEFsYhGvEHv-oXealPGYIyWRsuepTYKTIVvHHZHkFJVdaQoG4KXk1ox-T3Qe95WmwdkypN7FXmb8GSqnxLv1rXCYCZMqZOHRWNdi8e4-VJeNm11EdMZ2bfIlM2Na13EVQYQFShn0-KOic1XnKpBaN16qBDTo5PLmrz7Jh2J9FyMRDnJMqWeZY-XQ8et9CRi0e7D0U6A9EEH3KMT5j5ZX8zxu6_y3B2UPKc1XCET5A5kNvDv8tuWnopCaHwY-i9C_YKZ-UGt82A1iL51KifItQyXg7fwLpPoeaRDe_laNRrjYFczCUFZvLsMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔴
#تکمیلی؛ طبق‌شنیده‌های‌رسانه پرشیانا؛ دو باشگاه الوحده امارات و پرسپولیس در آستانه توافق برسر رقم رضایت نامه مبین دهقان قرار گرفته اند و احتمال دارد بزودی رضایت نامه دهقات با پرداخت 500 هزار دلار از سوی اماراتی‌ها صادر شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/30778" target="_blank">📅 09:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30777">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0333d815eb.mp4?token=Tv2RGnzPCvOSMXdTX4Z23BR8r6MbeuK3YgOJZ02qN58ZIpHJFpFhonCWh-4qWQ--LmKjDKo0_6kXwJ0niDuYWeCIp2Hy68qd2FncbARV6Zn_4LeEvnUtyNCi4JN3EzDFrgen8irfdT6RJjPfvars4R0C9VjUt3PwgudqOcgEoj0zlYrmZ8tX9RNboMk-cgLN77dzDVktP5TTxRpKqaFrFxj8b5axfGPXNVmCJPj5WGq6Nvr7q-HdM98iBlE1RdST9PO0Ed97_doGwNEdlzCYmEbBDy_YqjHaUNasuKb807c2e7xxfkeAumN3uoyuhK6om1dadlm1UGjVeT3HH-0VQ3F2GjSa4HgJj-HK6GgyEHNqazcuzQ06Pa5EAEs1jiIC3_v568oy9mgXpLZskkxlBSDh7XPjiz1JKr2dDwxHnQKDcyBlFWQmBd94qHtVM3to8d5GuJbjjyg5LAy7GwcVdB7N27mBlaScAINuMpyMGsEIhntUfbxC3_yFUCWWHe--ndwY2eaOU-eq2PwaNXkMjyKKvFRnO4I_5Aq71HLMUzBEbQygHqb2Jud4tBeZLnQ1RPPZyPOmXSP8BSkpNJIsr4i1alCNI5oBDhNG7q1ZEtlY7kRIKOogWuov6liy795tjo0ShiIk3J1jXtVeYqgPX7yaf4YRZAM7vGimjoKcG3I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0333d815eb.mp4?token=Tv2RGnzPCvOSMXdTX4Z23BR8r6MbeuK3YgOJZ02qN58ZIpHJFpFhonCWh-4qWQ--LmKjDKo0_6kXwJ0niDuYWeCIp2Hy68qd2FncbARV6Zn_4LeEvnUtyNCi4JN3EzDFrgen8irfdT6RJjPfvars4R0C9VjUt3PwgudqOcgEoj0zlYrmZ8tX9RNboMk-cgLN77dzDVktP5TTxRpKqaFrFxj8b5axfGPXNVmCJPj5WGq6Nvr7q-HdM98iBlE1RdST9PO0Ed97_doGwNEdlzCYmEbBDy_YqjHaUNasuKb807c2e7xxfkeAumN3uoyuhK6om1dadlm1UGjVeT3HH-0VQ3F2GjSa4HgJj-HK6GgyEHNqazcuzQ06Pa5EAEs1jiIC3_v568oy9mgXpLZskkxlBSDh7XPjiz1JKr2dDwxHnQKDcyBlFWQmBd94qHtVM3to8d5GuJbjjyg5LAy7GwcVdB7N27mBlaScAINuMpyMGsEIhntUfbxC3_yFUCWWHe--ndwY2eaOU-eq2PwaNXkMjyKKvFRnO4I_5Aq71HLMUzBEbQygHqb2Jud4tBeZLnQ1RPPZyPOmXSP8BSkpNJIsr4i1alCNI5oBDhNG7q1ZEtlY7kRIKOogWuov6liy795tjo0ShiIk3J1jXtVeYqgPX7yaf4YRZAM7vGimjoKcG3I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌مناسبت خداحافظی غریبانه کریس رونالدو از تیم‌ملی‌پرتغال؛ یادی کنیم از این هتریک تماشایی و خیره کننده او در یکی از بازی‌های تیم ملی پرتغال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/30777" target="_blank">📅 09:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30776">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJYX0ESXlinnfMWZVXdMdlOXvnUnN3GCNGfMV3MZqrfDi8a1sT6XaoVmIRHhJREwjuT_SMQFB53RwflrRE-bPonxjd0k8mfamXFXwkJsrGwD9zE5e6U4O0IwEXcEAyBv1skZwah097z__jPNVAzRX3l35FAKWkgBrfJFXNYCPmDzFfk3YvT6bdXCAdcaJfHjs8Kj5LLaz4afVjyZ8ufM4tdpxtXKgZuDTuKDhQYrpl1jlwjtuEqDXhZvXW5wGwUMKgcOvRhYt3izolELAwGgTCHkzcu1fOse7MypH2_d3WmH_ebJ6QJjfPS4BEMdHY8BOSPcHavIDU5Ukw8LtJUrJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه مارکا: خورخه ژسوس و رئیس فدراسیون فوتبال پرتغال بعداینکه فهمیدن کریس رونالدو اردوی تیم ملی رو ترک کرده سریعا خودشون رو به فرودگاه رسوند تا مانع رفتن او به مادرید شود اما رونالدو به درخواست‌اونا توجهی نکرده و راهی مادرید شده. این نشون میده خدافظی او…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/30776" target="_blank">📅 08:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30775">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-janbXR8lDz8jnJoDpR59TCV2T-Oh0z-hls2wc2aDm7ngEmSs8leCBu3ZGGDTUWXIyElbxYgC_tJu62kjNVb1YxtkKm5lGoqz3jxwQXrHL52u7PjA35KbgkiqWD6JpwuG_N2NxPcWJrfFARpnWPNVVPasxyOArrOe4v7rr1rbqu8Cq4zesT8yQhfut_uz1G3t-41JQWOoQd_DBdBjefjjNyX8ZtmtdxengrtVKd0pZC5r-lEIk6iHynN-_1DVvH65R36B-z9z6JKOahiAvuYKFeHqdH6KNuymsRQVm9-FtxdkoBbG0ORxct4jnDOZ_ubor7X-kUDe2lVv8lbWk9KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
نشریه مارکا: کریستیانو رونالدو اردو تیم ملی پرتغال را ترک کرد و طی چند ساعت با هواپیمای شخصی خود به مادریدخواهدرفت. این ممکنه آخرین نقطه و پایان راه رونالدو با تیم ملی‌ پرتغال باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30775" target="_blank">📅 01:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30773">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbbdoZrX2YmJ8bZRRc2jZHm21kGRCG8fW-WrlBufRHQMhIf5cMM2ETq4dFOv77kp7wCFDLXke_0SzXW8g5jSdQsaIdrtow1tdmk09TUDU6RotbiZUTW9Ll7u1eR-gOXSROYJ5zVbiI_khHZqH0fb5_tK7LNSDn7tR0Jb2wh0TLuBr1ubyT2V9_5Ae5z5eAeIx8gf27NDwwg4dw60-Z2YaPQWtsvYrVDwc7dtMeHHP35xpB2fp-4EmIYDHNP6TKk2uMs7opiJNOzf6MMZqNra4S05TjA0sfl6Lv8ivu-TQoMCx83YDaWcWUHPEozKZJv60kWWZ6sfMMJfllkkMMSVMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از این به بعد جای این دو اسطوره تاریخ در تمام فیفادی‌ها خالی خواهد بود و بعد از سال‌‌ها دیگه قرار نیست آن‌هارو در مسابقات ملی ببینیم.
🇵🇹
💔
🤩
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30773" target="_blank">📅 01:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30772">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCyyw_-9yQeeGHw5f1m-eHyHLtoSNcaGMu_mWChDCim80qjdMWfTBNjehuXJBElCM9sEAptUs18G_47NkliPZ0HRHm07N6f6v8_V6TbdNQn4ZzjlQhbYmpvDzG1D1wv0H2gKUCwQUXTLG5PoHMayzQVPZ8zqmKbAnUAYZ8uDqA_yrEOhTBxTc4HSruERbPX0pFJO-FWrH1rGagMxsHxn_PXrQ03SMEoCHbUEIB8E_Kl9ffSc7zK1XB_Qa0ojXgTug9PTBZyuYvQ-9Mc2imE5aEuIX3NI1VidJsGeM4CBeTEXNa2sddosVknoC3lTD-QkTAyM6eNpO8JmxyiMYumVlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ مصاف آرژانتین و پرتغال برابر بولیوی و دانمارک در غیاب لیونل مسی و کریس رونالدو دو ابرستاره محبوب تاریخ مستطیل سبز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30772" target="_blank">📅 01:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30771">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3y_P0YRkGPOcuPwyWLwrY6_Jo8k0EszrxD0xsxdYpnBRCsxJGXVSUW6WY0d-efrJiZ3QCnQONJLsAdBE1WQutSyAt2nS92sdL14yQuA-NWjcbJxinBR3qfnaMOgugrUhilt4tqgdQUPnmHzKHIwWpYCnPqqOwv_Lg8R_po59MKSvqLJDsSTBoLa1VWbsVnQvZ9av-4JkjMgIIsPebfgjtAbwfdHoa-i7rDRrdvLBX1CyFdt9Zow_LFBzAsp9TCH-VsThTpz6_Sy-sfSHChidc5jABYCFTsWPNaQn07wAFy8lduK0RBytAnE1y9uNXF5JmX9aOSHwYtS_M2pdyjDXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
برد خانگی یانکی‌ها مقابل شیلی و دومین تساوی مکزیک پس از برکناری آگیره
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30771" target="_blank">📅 01:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30769">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsRpeugVnFCnBFYPcJ9MRlgQi2X4U8keQzxNyq1A08e5YcsVCucMIaRITulo7jTW7MmqjjMnTa4n0RZ_Yd8z-iBeuHIO1o9OssICCwptghJhQ1nMvuKGq7oUJ4JL11N113Dvq0UuhRzld3jenfsYwJggNotEgOmugtRo5qYpeLPbSvqCADWafvo1tSwZ3qdQPnTMoV8oYuyhvBwZ52zx7KyJwzx2TE39YNpRbC0hR4MFIONFsVnIQbWXSMCptumg12pfPKH2p1UTLYoFlHLBEKGkOORvsvQt1Yp84Nh6MeUwavryiriryTNpV98587966-lYBF6glKR3-kOL5TXalQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی بعداز مدت ها خانواده ات رو راضی کردی که باهات بشینن یک مسابقه فوتبال جذاب ببینند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30769" target="_blank">📅 00:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30768">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZfDv4rvDKGLMKvsVIxsuaHBhD0VnjbfeRNq2vf3UkJqTNLZM2FOWCz9CM6AKVsuZXe1DaOrnL8YctkAAuub2261YDncfyTs0cug3C-Zq2z3aIkK2wk0hgvh8czfnDmxyMwddTfOdyfTl94UBmX0M2nkO5hu2yGsVCrCj5i3L5SY_pXR-IFE3EdyZ8dtq__xWXSOn7K6ZkKOTeJCM9C_dd7KOfG4S5I2go0hywe78JI_dg7SHwrzsf0-YXuzLg6G_8cLtchjRLThGwSKcBVou_65npRkIu15Ms6a3pbRqHv1orJedFGy1jAxhGPFn2veRKuNwebPsbR96yEqRpTikw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
روزنامه‌ اوجوگو: کریس رونالدو دیگه قصد برگشت به تیم ملی پرتغال رو نداره و درآینده نزدیک هم بصورت رسمی از تیم ملی خداحافظی می‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30768" target="_blank">📅 00:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30767">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ploTWtDolDS4HyV0DGA8QfcoX4seeT3xQH8dUBsWlV1Mdh5Mwl2oIPZJ8NBM3M8h5-W7rcAnrtLHrhelApoRi23m6oopE4O1GclvVwluy3k23v7OlLneYgx2BbGPN46uEzglRDITxWS2NGKFHFNTmgE-RmrHk79pSTfVDrpBlCOWSdz3f6ctt9r7XycVPnfG8879eQRUvdjhXQMGt5jm4t057bhkZ_lLcDSAYfmd3yHHAeQ2lEbG6HPiclNEqYwED291EwZgpr8JpQILRrawMVq-MRBP3paqLCbU2oinm8TzTXvnxYnIk9yEW68qWu0HSdYIm2AEj5J0_AxELNYCHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
قصه کریس رونالدو
🆚
پرتغال هم به پایان رسید؛ قصه‌ای‌که‌میتونست خیلی بهتر به پایان برسه و شان اسطوره پرتغال تاریخ فوتبال حفط شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30767" target="_blank">📅 00:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30766">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hq9PWfRS50GEK4h3d0Ln_7VnNItWDLP_BxjUkpfNvHmCW2ZsX0OX78_ubxHWNWDWyFYVc4Kt-40pttigIXleusrGyDZv6b04jF11_ZomESmRsJKkbvZnf08zrif2GBvg8TeLw8UjuxvlJ1VjmZE-KpV_P20vjm9O_L59s7xMSu6PUKb_52t1qB77esewhI4j5UClJKg5tV5Su138syTE2KDUfhnC-T3quHLZs66s6xaEA8NiDGHewgakcjgd63FIyiT7klxQE5tMLkx0V15bqBSM0aVbyyW0s0aRHU1pTfn5g_wawj9Prg0CpmxQeDZjHB9GVOIMDWXJ22AT4sTLRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
قصه کریس رونالدو
🆚
پرتغال هم به پایان رسید؛ قصه‌ای‌که‌میتونست خیلی بهتر به پایان برسه و شان اسطوره پرتغال تاریخ فوتبال حفط شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30766" target="_blank">📅 00:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30765">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cebdd683b.mp4?token=ZTel60mz8qgKsqLQ6_LaoXMWcmq4BfNE0Ksjc6Soeql73dmEtOxCN5TXC7E5WNu-2rl5oHbEx4pjwfsN8CyWFUvsvQUD0mJwsYpo7aM1Pafqo5FSC0QqZJedke4U_3prIwRNR3NG2qhlV3XZ6cME4c2qYVXPNOmQu3EbZN-Cl4USL4bAk836MIH2AawUJilV419g7MomVAir78qfDUzF5undEqw5GZQnp9a4DpPsg00cafLRGi9JCWEBqOB99Y_tqipv6kLi6b2uSkRoQ00Saij05WST7dzwR8OmvVoCeDaycWPFUcC4uxtJSuBGAb_gXbNP9AHq41CXcP7oVI0t-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cebdd683b.mp4?token=ZTel60mz8qgKsqLQ6_LaoXMWcmq4BfNE0Ksjc6Soeql73dmEtOxCN5TXC7E5WNu-2rl5oHbEx4pjwfsN8CyWFUvsvQUD0mJwsYpo7aM1Pafqo5FSC0QqZJedke4U_3prIwRNR3NG2qhlV3XZ6cME4c2qYVXPNOmQu3EbZN-Cl4USL4bAk836MIH2AawUJilV419g7MomVAir78qfDUzF5undEqw5GZQnp9a4DpPsg00cafLRGi9JCWEBqOB99Y_tqipv6kLi6b2uSkRoQ00Saij05WST7dzwR8OmvVoCeDaycWPFUcC4uxtJSuBGAb_gXbNP9AHq41CXcP7oVI0t-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خواهر رونالدو: ماپرتغالی‌ها نادان و ناسپاسیم و لایق داشتن بهترین‌ها نیستیم. تیم ملی پرتغال هم به همون چیزی برمیگرده که قبل کریس رونالدو بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30765" target="_blank">📅 23:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30764">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eM70GM93OkeVLHDkkfOBHyjXWDs_WJN6870B6VNbgFPFR4SqB-4X48KTe75FqI4_IuJ6wEuiwDHlDM-MVkV8CIqgfjRzGTBD3q74QgmEgX2e0zyoWe-fdNheC80msuNyxdDwYtKZVWQ0zxiJf-XtC0m8YGZsi_41mzMyeiTW0ygd_GVCJ29hShwLIRVS-1I0X4xtTeFiKOPHMBpBn8icBYv1t14JQAJfnGb_FMDVeQ_pBB7PytVVexLOK9q2WLzKpsZ-9-3sl7qn72rOwFhW6oAy2oJ8J6epPsH4MqETWRoeVcJRyAcibVHa4q0RpQopRoaLp2QmiBmda_OGoMBisQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده میشود که فدراسیون فوتبال میخواد که یه مسابقه دوستانه دیگه برگزار کنه تو اردوی ترکیه. اگه قطعی بشه دیدارهای هفته هشتم که قرار بود تو بازه زمانی 15 تا 17 ام مهرماه برگزار بشه به تعویق می‌افته. یجوری دنبال‌بازی‌دوستانه میگردن انگار این دو بازی چشم‌نواز…</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30764" target="_blank">📅 23:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30763">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c6b3c35f9.mp4?token=dVGhXYMte3qIib2f5QQ7BiRXsoyEOw7N8YhmaREC03Z298yLs6gUbR2yNSHErtJ0m2Nd1Rv0fhTVZNiSZUXmnhMIaVf9L92EcR9W4yYta6Wm1P1rbxq7mzzfENPv77qHw-_xpa1oQNv8B1Kos5yY4ijdHSSp9I_JOo-UuXo3pNpIFRWUhjuF1Xjd0cKvUg7Awx0WFCMvkL1_NTUsyDaIzDTN56ckdp-0AqjeAx9VMsmYhuFHt4X0Q1DugAggTgmo6bOrbYUWKFGagl4mZjheTVEsLRm49_XqeB9TJl6awzvaE-5hQO64pOKJr5DXg2wRG9e7VgNv13mnhV8tgPaoYb1Cf8daxEP0SVTw_2DgGIeW8sB7ugrzweDkeN3EsQjrRo5yFye5lrBVDQtmdqAb9AMianoKz1XRR6p2O1mqBCtdY4G_v0YMtITwh6sjR_II0l2OfV7mb3zBjbZEONoAwViL4v1d34wzxPZtXGjv8WiGN_SUkL43B8P9FQtSEYJ65a-Q3RqTR22fzyM5F1a_1LFAXRxEwJ0jG7fCp8q7SmLTUPN79fZjsWxHZQfYjFJNv1EoNnUdi9q71h8NdN9DS289tOt2yNWCefaRsuy1Px5Etr6k_O9WR0Aqa0cDb67BlUXG74P8quHCdtR3a2ABn2H4NPgWDFDelHAL_ms_9Oc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c6b3c35f9.mp4?token=dVGhXYMte3qIib2f5QQ7BiRXsoyEOw7N8YhmaREC03Z298yLs6gUbR2yNSHErtJ0m2Nd1Rv0fhTVZNiSZUXmnhMIaVf9L92EcR9W4yYta6Wm1P1rbxq7mzzfENPv77qHw-_xpa1oQNv8B1Kos5yY4ijdHSSp9I_JOo-UuXo3pNpIFRWUhjuF1Xjd0cKvUg7Awx0WFCMvkL1_NTUsyDaIzDTN56ckdp-0AqjeAx9VMsmYhuFHt4X0Q1DugAggTgmo6bOrbYUWKFGagl4mZjheTVEsLRm49_XqeB9TJl6awzvaE-5hQO64pOKJr5DXg2wRG9e7VgNv13mnhV8tgPaoYb1Cf8daxEP0SVTw_2DgGIeW8sB7ugrzweDkeN3EsQjrRo5yFye5lrBVDQtmdqAb9AMianoKz1XRR6p2O1mqBCtdY4G_v0YMtITwh6sjR_II0l2OfV7mb3zBjbZEONoAwViL4v1d34wzxPZtXGjv8WiGN_SUkL43B8P9FQtSEYJ65a-Q3RqTR22fzyM5F1a_1LFAXRxEwJ0jG7fCp8q7SmLTUPN79fZjsWxHZQfYjFJNv1EoNnUdi9q71h8NdN9DS289tOt2yNWCefaRsuy1Px5Etr6k_O9WR0Aqa0cDb67BlUXG74P8quHCdtR3a2ABn2H4NPgWDFDelHAL_ms_9Oc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
#تکمیلی؛ یکی از شروطی که فرهاد مجیدی سرمربی سابق استقلال پیش پای فدراسیون فوتبال گذاشته در جام ملت‌های آسیا روی نیمکت تیم ملی بشینه اینه که مشکل سیاسی اللهیار برطرف بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30763" target="_blank">📅 23:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30762">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7FhbIcp3ua9ey-7UMAtiyszSPoJhs7fuXSpkUkNpX8zSCbwGuDHrMERtRq3wqDH1hLeJbYv0znCCFPjRYTOn7hZXMmOgXLFQzUHoQnGTUczY_x6w9R9ymSh3POjxdtyCPAMmM6TxFTZKj7eqmGvEHnFHiOs8SdlE0L5L9gOm-Rkxo8HPaWznlm8dqVvCaQ-I6fFXrcfdI7f1DtOFFnhPy0aol2F4yfaVE6v4AI14gjZ6MWqAghnM0lZuSo69jIZ2d_h2FY1wYJOoTzwEs7rCwecIjxID8JnCefsgUkWe2oZUD9juhVrXCQOFnWhL09ElcvYxt7g4E5hgdcSZghVfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
نگاهی به عملکرد و افتخارات کریس رونالدو در تیم ملی پرتغال؛ بزرگ مردی که یک اسم میوه رو تبدیل به یکی از پر افتخار ترین تیم‌های اروپا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30762" target="_blank">📅 23:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30761">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsoBcbUhQNieYgdocZ3dky9yE5RttyrZnGb7un5ZcOnCuj1MTkQZVO-ZRWWvw5qaAHxiTkoRG5dShJSZgWcncOC8nwxL4QxbqnX3r7ef6HQcuF2G7mb39UeJ0BR2op669Q8KNJSASs7Cc75EnRGwWXrHauMMNPhHn6Pk_D0XR7JdPnGVA49s-Jdmv7IegelNGAXsDy0Q3qvfNrdDPQ8mRMZMjTi5F2TZuXaRLuzRpB4OPShYPd1ei5L72S6r6GvX4N4zIHKAUOL9HB3ohL4xm_EwQuUVlsVDwUR7m1qsSK_EiJ0hlGoWYPf0wIFQUE6SxqYSHUI3SGiT6iPUIKl8SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعدِ پیگیری‌های‌میلی دستور آزادسازی طلاهای میلی از بانک کارگشایی صادر شد. خدمت تسویه و تحویل که بعلت‌مسدودی‌دارایی‌های میلی دربانک کارگشایی مختل شده‌بود فردا عصر پس‌از دریافت طلا از بانک کارگشایی به روال طبیعی بازخواهد گشت. همچنین طبق دستور دادستان، محدودیت‌های اعمال شده بر درگاه میلی رفع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30761" target="_blank">📅 23:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30760">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLM8z05KTbAJ7qfXo11rAz9lMrsaE_T-sqftu0ngwBGyZP0vaTLvn4EkM2nT-HoTjIYEdcx4qa8wNL3zfsAVGMYW8FVWUjf8LTtX-h9L2TAOw9PeyZ4VBAWUP2eCSMIr03XCCXmoLW5Vr8C6CrUJK-7ydhQl8aZUlGgIaOB_ZCTSRnVMWig2jIS7-F02FwACsEnrTpe7m_3e0T3PJsc9Z_jflaKJke1OvP292jQz0OFxCCeQTJbbiOt8l9ssk78Er8H-7DvnjNMQ0Q-EiXFsgOIU0xFBuPdXy3fqmxU-EULXlkiNhirZnEoVqwMsJvk-D478Bb89o6Z7y5tK1uxLbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار دریافتی پرشیانا؛ مهدی تاج رئیس فدراسیون فوتبال علی رغم حمایت‌های خود از قلعه نویی در رسانه‌ ها اما پشت پرده بشدت در تلاشه که فرهادمجیدی روراضی‌کنه‌که هدایت‌تیم‌ملی ایران رو برعهده‌بگیره. اگه سرمربی سابق آبی‌ها اوکی رو بده قطعا سرمربی تیم ملی در…</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30760" target="_blank">📅 22:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30759">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGAaRo8ZgtJN_AT190xwsZnkAUFhYYUOH-zxkcz4OAjTPJTgjfh7yuqT8Fbbeeuwv3XAksFVnDqF3kcmILzj6AIa-N9zOH3XVmcNHgtzYMMCPWk3-Yxt-XV7Vki9xqK0ikQ1VgDjkngrQBqI2lbYOaAZXSAgLdrMml81bJiGqfy_xh0BnyeYTxyTzZFegrJSCFvo82dXDe53XsUnvt_BvAqkkkBp7kLrRhBew752eI0pXlq6bIk_mqQRISQs_ndljKos5KG2J52X-awQ4K8ySTSTsocFXfa4Gbq6gaSuUTn45zBcRO0RUqsIsM-jW_xaYqYxcnIb6VTIuALyZ3kL4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یورگن‌کلوپ‌سرمربی‌آلمان:
توپ طلا؟ اگه تعصبو بذارین کنار و آمار امسال رونگاه کنین متوجه میشین که‌توپ طلا باید به مسی برسه. اون تو 39 سالگی یه تیم رو تا فینال برد و نیازی به حرف زدن نداره دیگه. چون با بازی کردنش همه چیز رو بیان میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30759" target="_blank">📅 22:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30758">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUfD-2wT7PcLrq9i6mLGN_jxufYPWsLgw41Q_bxN7RHLDok5Ed4S_mpb-X9weCKS4UxLq373t8YaAsTdkEalsvwawrRRtvRZdulARpMMkiBhJDL3Q4a2dec0aXPWLtKeWx1OqcGlr-nspDizxEnsK6MH1KKZbArWJ0yn9sJo6nRv4MnQEwjWpLUnhZ_eYnt-McvoVGwuZyeMjqRTjQBmrb3r5-rxXiJmMaHYTfHMX1D6Xk8jYon5IF0JNB4tRnDTDuDipnixHslOFjYynzeHbLAIrhtfxM6DNb1LZMttaKLkULuPCg9zOoz8fi_oBUhilYi0yiXLmeRK9g64TdffVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کریس رونالدو: اگه کادرفنی‌پرتغال نیازی به من نداره خیلی راحت این قضیه رو بیان کنند هیچ گونه مشکلی بااین‌قضیه‌ندارم و خیلی راحت کنار میکشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30758" target="_blank">📅 22:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30757">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0642770280.mp4?token=BGzAuAH3HopiQ4QjyhxAp3-znkGEpst5tZpIoWARhqLoq419G1p_5RsDWr84BZSgx-7T0xbkE_nlsemWZh8gnntzn_UT6yOetRJ0JkLAOxsKk7sOrlWfBBAggRALUJH8vr1rVL5yOjIwAgQ7NvqBeamuIjt0t-3ohSxSjym6TLu-u2rh-1kFnOB-psE4fv9mUfI7oZftLanem0-V_HH2SLOtkJcH1cZ9BxArLFyZS4BCFcNNcIx71bZbD2_VYTYtjzfSsZyrzUCOLAN2yv6qy73v8T_iz9vQOHn-fLGbSC1L6XDTKK17SkwFd6xbarZ_2Fko-2q5kpyur5I9ijpFH259du6z3Fsj7cLyxwF2LswoFt536wqeKc1Na5OqFMJ53GgqcJBMIagq2zZcudUdyh7oixM2D1-uLHeGHMIIljwCGnT9TMutIpQm5FIQGP5ETWZxdW6sd_TMDHoMkSAqu2m9a6_arlaqD4aUp__fHHPWmrl_k_OZvgkfdyJqB_1WzRdK9ah-gA1Ne-tmFTQ9KQJsGi5y3tniYShk7J3pgt6ZqW8UDVtkwHSET1ZNxrO9Ere7DpnR-BKlulFuFUUo-APmeFxsJAvdrw_dNnqsk9tKNgq1dF8-9yVo6GiIkODW8LAL5qUTDN4ZhgphrGPrQY-G03w951-NR84xXS-c4es" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0642770280.mp4?token=BGzAuAH3HopiQ4QjyhxAp3-znkGEpst5tZpIoWARhqLoq419G1p_5RsDWr84BZSgx-7T0xbkE_nlsemWZh8gnntzn_UT6yOetRJ0JkLAOxsKk7sOrlWfBBAggRALUJH8vr1rVL5yOjIwAgQ7NvqBeamuIjt0t-3ohSxSjym6TLu-u2rh-1kFnOB-psE4fv9mUfI7oZftLanem0-V_HH2SLOtkJcH1cZ9BxArLFyZS4BCFcNNcIx71bZbD2_VYTYtjzfSsZyrzUCOLAN2yv6qy73v8T_iz9vQOHn-fLGbSC1L6XDTKK17SkwFd6xbarZ_2Fko-2q5kpyur5I9ijpFH259du6z3Fsj7cLyxwF2LswoFt536wqeKc1Na5OqFMJ53GgqcJBMIagq2zZcudUdyh7oixM2D1-uLHeGHMIIljwCGnT9TMutIpQm5FIQGP5ETWZxdW6sd_TMDHoMkSAqu2m9a6_arlaqD4aUp__fHHPWmrl_k_OZvgkfdyJqB_1WzRdK9ah-gA1Ne-tmFTQ9KQJsGi5y3tniYShk7J3pgt6ZqW8UDVtkwHSET1ZNxrO9Ere7DpnR-BKlulFuFUUo-APmeFxsJAvdrw_dNnqsk9tKNgq1dF8-9yVo6GiIkODW8LAL5qUTDN4ZhgphrGPrQY-G03w951-NR84xXS-c4es" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌وکلفت ابوطالب حسینی به رقم قرارداد امیر قلعه نویی در تیم ملی فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30757" target="_blank">📅 21:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30756">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnzdIiESg4qdsQ-9JL6GF2XMG9ODAeK40TNI8zPmFYwRq_IjyoQ284OSMKRtRWYmHlXSEqu9eh-h0cayp-pIB5kOI-zYXLIT2rjk_dBwNa5EE3zkk5-7x4Hw_6INmhkdF7Gp-gVRu1BtkVR3F0MEyroVGpNAVbVrDZTbyAIfVIPejrr_iftySjmwQ2oBQsUM05V3tA5UPsvoe8ObGQYzZM9DbSd_Y4LujhKIzuUL0DhqUBxMft95pUVvNvwUKajsBrVE2QxatT282WlUFqqnnXKIv0OTsIbO43r2_AbZ2iqNq5MmMfenqh7aSUFHEMY4faa7_sMjshDKhA6JtVvi6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
نشریه مارکا: کریستیانو رونالدو اردو تیم ملی پرتغال را ترک کرد و طی چند ساعت با هواپیمای شخصی خود به مادریدخواهدرفت. این ممکنه آخرین نقطه و پایان راه رونالدو با تیم ملی‌ پرتغال باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30756" target="_blank">📅 21:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30755">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzwzeTbqODUp8UGosLSUsAoNAet6RiNSgWWNS1vdpNGXWaGzECXrk4LWKP7xJhW8mhPi3v9eQBHy-GOSk29Exw3b2eEcFu9YNNDQX9qP9aLQH2v-rDbpa_qffBOPcaYqjcSCu3MU1n-xBtu2CUa0lgoXuoy1u4VPiQDSbCEfD2jREgOCUTje65ZDIpdHg4V_mlCCeBRip8EOnoSxqDKpVkKv0UGHvjh3gdIxjbNTPBYJojwh6TzoU76GgQgeW9peZfIB9Blt3cGF7qFFkNxvzuIlvuZxOzdE_GP0WxPZII4PIkL1YXaK0I5Mzsg6B0abl1xk86rwNrHmvv3wGafSlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌خورخه‌ژسوس‌سرمربی‌تیم‌ملی پرتغال؛ کریس رونالدو فوق ستاره 41 ساله این تیم در بازی فردا شب مقابل دانمارک بازی نخواهد کرد. ژسوس اعلام کرد مشکلی با کریستیانو رونالدو نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30755" target="_blank">📅 20:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30754">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jL20IcZR0qLJcQOYrpLPRf4npUOTF-QZuhydJ5OdZfzY2Ja5qyug81_A0gisyQsHRjbA3jcFh4_RRYg9ZmAMezkfPpTiNS8vdNM4jSHbajZzWss6ggt3HYT7JwRJF0Ixi4lKLfTi3Fh4qntHCnGsEfjCtQ9M2kIPVaDl1KMpD_bSpaH9S62LewLF68TFe7FxqNglpw1xx8uNDYmFa_FncH9IdvxEjrd1UGNcrqoge0MtmI00KaOqxYL-vGd67JFUvCpB91YJbGNU4tu_2ckwRgIAV9gSc9tgK4ZGAOl7H9X9rpMLVWg-ZmNZspVTDSInHt57HoIDcHpB8cXLWBB-qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تالار افتخارات ۴ تیم مدعی لیگ برتر؛
استقلال و پرسپولیس با ۳۹ جام رسمی بر بام فوتبال ایران؛ سپاهان با ۳۰ قهرمانی نزدیکترین تعقیب کننده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30754" target="_blank">📅 20:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30753">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6481f7331e.mp4?token=eTel-wfLa_cTcEJbuMtkLHdt6k15reWMFSfN8ABvGb-qG08jnCRO1pU5A3-6np86qz_bu1Kr2tbbVs7NMNLQ5lqz81JNS-rmwgWBRMwJj9O_VPo5yyCa5EjLRAX1GKbbeuJew0u74ZKXYy2h3-JNdg6KZLTLH6L9k0f4Fr4hJwAWtdH7_LAWJ_0XUcOwxWbCA4ecMH4iRSnMbBhypizb1qVkdSc9qM4mdJ5qzqXa95rp-tDG5YZF4TU4UK-v-2H0bxs8dQPPBbMLJBrJ9nUOueFxNKOHRxUQXCMCP-325cKRML0jZyBij8quccod-bs8RZfsHOdQL72wSjZedBT8k5TFHC982rg1b_ZwRwoqor4SpbY4_SF4SrSwOrtH3ttFRNj_tOr00YdnxggdVHnZPFh_YXvvVTHoryqnirSyBoeZ83QeSw3a4ws71-W654z4E4PsO2RMWpgA6TA_VCQ_Y43W-cydynekH71-fUnfDdfcaHs9uDqQpGcYWHqLbgA72_GN8IqCadPrk59dL5HKEvSo8QF7qfkrk1gLrGOxjZlboVqiNesnvBJ9L3RIu0ao8mAK-zd-5Ke7SY3Q0ZIsc1MV2Vgr9GiTHluUWUGzj3mhFITmqgwmrCHxjJlIUmUAi_wVtBJg7pn2d5mLixtCWNPrNjZTSdKHwW8fFIIY1TM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6481f7331e.mp4?token=eTel-wfLa_cTcEJbuMtkLHdt6k15reWMFSfN8ABvGb-qG08jnCRO1pU5A3-6np86qz_bu1Kr2tbbVs7NMNLQ5lqz81JNS-rmwgWBRMwJj9O_VPo5yyCa5EjLRAX1GKbbeuJew0u74ZKXYy2h3-JNdg6KZLTLH6L9k0f4Fr4hJwAWtdH7_LAWJ_0XUcOwxWbCA4ecMH4iRSnMbBhypizb1qVkdSc9qM4mdJ5qzqXa95rp-tDG5YZF4TU4UK-v-2H0bxs8dQPPBbMLJBrJ9nUOueFxNKOHRxUQXCMCP-325cKRML0jZyBij8quccod-bs8RZfsHOdQL72wSjZedBT8k5TFHC982rg1b_ZwRwoqor4SpbY4_SF4SrSwOrtH3ttFRNj_tOr00YdnxggdVHnZPFh_YXvvVTHoryqnirSyBoeZ83QeSw3a4ws71-W654z4E4PsO2RMWpgA6TA_VCQ_Y43W-cydynekH71-fUnfDdfcaHs9uDqQpGcYWHqLbgA72_GN8IqCadPrk59dL5HKEvSo8QF7qfkrk1gLrGOxjZlboVqiNesnvBJ9L3RIu0ao8mAK-zd-5Ke7SY3Q0ZIsc1MV2Vgr9GiTHluUWUGzj3mhFITmqgwmrCHxjJlIUmUAi_wVtBJg7pn2d5mLixtCWNPrNjZTSdKHwW8fFIIY1TM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
شهریارمغانلو مهاجم‌تراکتور توصفحه‌اش این ری‌پست عجیب رو درباره سربازی بیرانوند گذاشته!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30753" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30752">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jT2_6fK7XGBQSOTWjNefxVTNwVCf6mUT-iSU9TucNnL5pUJXDTItIyTrQhrS4YoW_IJb0Qra1GayFr1lhQF9hfojw1qsudf0ml3hJm-2gW2orZ6x257m65g2t8gMfk1LlqjqoY_gnh5lJ5rNKEqFN1Vpq-CY1MSXOQ5Lyoq8Vo936Cg50M0vl41z1q3qUT8K_B_bATfJPWfz-uBED1TSkPNgjsCydIU-LCyyr2eETIZbqKyyG-uimvbMxedgQOknJKZ2fmo4O2zYn9ft7ExfxZgseKeen0yTt3Jk9Qr7F3oOC-6B8xVYXmsCqSRxynDD3qKBfFbcq-5wa6Do4jZbIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
🔵
آیتک سلامت و یگانه اکبری با عقد قرار دادی یک ساله به تیم‌والیبال‌بانوان‌باشگاه استقلال پیوستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30752" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30751">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df42ded691.mp4?token=BX2qtRzbOVddPCxZLzFaRLc4f5XiPg9AVeFJ9hTbhvJK0TqDmUmlNl6V7sDs_7YRXP8HmQ3f5FAhVf4MsZqJfbX-ZlN7wsf9Ip3vulSKtN9TtCgoMPGwx2ITLMTM7EO2Y3EilsGxx_KlPemCUqbGOcnbB5MObeDC8WZ42St-d7OFZtmfB15YnvAy-ohHnjwesSkcg7kdtn1QHbx18qZLUvJ1UibtAZ0UY_TFUMhX70zr5gB2QrVwOUgZTeome2W0acqBD6IKFsp7OMkkDInuQZVSs_wnnO1PnXTWWSpzOAWAFB0LrGBuhGeI4HPTffr6z8uSRcGdG0k275-zPVIDKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df42ded691.mp4?token=BX2qtRzbOVddPCxZLzFaRLc4f5XiPg9AVeFJ9hTbhvJK0TqDmUmlNl6V7sDs_7YRXP8HmQ3f5FAhVf4MsZqJfbX-ZlN7wsf9Ip3vulSKtN9TtCgoMPGwx2ITLMTM7EO2Y3EilsGxx_KlPemCUqbGOcnbB5MObeDC8WZ42St-d7OFZtmfB15YnvAy-ohHnjwesSkcg7kdtn1QHbx18qZLUvJ1UibtAZ0UY_TFUMhX70zr5gB2QrVwOUgZTeome2W0acqBD6IKFsp7OMkkDInuQZVSs_wnnO1PnXTWWSpzOAWAFB0LrGBuhGeI4HPTffr6z8uSRcGdG0k275-zPVIDKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از ابراهیم‌شکوری درتیم‌امید تا رحمان رضایی در تیم‌ملی؛ درجواب‌ناکامی بگویید: یخورده سرما دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30751" target="_blank">📅 19:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30750">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bw6NcwBxhh4ra7dOlvxYFgqdLSKKoHOwZ3ljsMBy5vl2VoPb1tGvD4au2OskzCIbdLVVFMFsNohpGKQbvaQu2zGKzLxE3KfNJeLNkQxRqMxenykuMeTnJIEslhyouueruc8oryRMhPMsKvZx2oroczBIjaDV4zwjUGIP87fcpwSI37jP_MqYsU1EOMOHUPFemWQr4qTsSGHDsWc6yukCZYGEMkfw7lOHHyPEI4XRg__ZSrNlIFXWwRiwnIWaaTWrd8XVhU9jErrTpOVUM9ub2eNyrnHYaCQtn-HIxiQA3KnI__fHtBmHQVlhEUO4zdq6yqivqbl1BCipXIU568y0ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رسانه‌های‌پرتغالی: کریس‌رونالدو بابت اینکه دربازی بانروژ30دقیقه‌گرم‌کردن و وارد زمین مسابقه نشد دلخوره و درخواست‌جلسه با فدراسیون فوتبال پرتغال داده تا تکلیف او در تیم ملی مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30750" target="_blank">📅 19:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30749">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f9eeb9930.mp4?token=nvQQ0wdJogsepLDKuOubN_07O4Gjmqinc-32yN8qMnUlhM1Io7sAM7TtxTdSHqc8wC0YKMoYR-Usgwaq2TiUht4nXjBNEV0Wus9zehmHTRiQlnTrpxOsTE3CyrN5pGDEEwusVvoIOCEYqiVuR-7rwYgA8bDyc1Xi0XKV8gnUYQOZ4juTmvDq1jWNaketlKTM3SPKaTsCMH8s4T33cLEDtMuycAnyWH5PtuHUvaV8kOiJZe1UncK_rdhTkAAwal6Z0dlJNcQes9YElzI0fofexWN93Y7fz_2U7W9YnktCERX-NrgmFfAgMiQZLHdarKxdv_yy578f4K-4-A3SAkKaRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f9eeb9930.mp4?token=nvQQ0wdJogsepLDKuOubN_07O4Gjmqinc-32yN8qMnUlhM1Io7sAM7TtxTdSHqc8wC0YKMoYR-Usgwaq2TiUht4nXjBNEV0Wus9zehmHTRiQlnTrpxOsTE3CyrN5pGDEEwusVvoIOCEYqiVuR-7rwYgA8bDyc1Xi0XKV8gnUYQOZ4juTmvDq1jWNaketlKTM3SPKaTsCMH8s4T33cLEDtMuycAnyWH5PtuHUvaV8kOiJZe1UncK_rdhTkAAwal6Z0dlJNcQes9YElzI0fofexWN93Y7fz_2U7W9YnktCERX-NrgmFfAgMiQZLHdarKxdv_yy578f4K-4-A3SAkKaRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
به بهانه سرباز بودن دروازه‌بان تیم تراکتور؛ وقتی‌بیرانوند از خیابانی تو خدمت مرخصی میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30749" target="_blank">📅 19:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30747">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_RgFEtPbtJHMgtwy_ICQF8Yncz6eojwl7nfgznVFY8UnIE7WhG47-PG7rQ8z6HGsu84Eepcf-sIbK6nx0HaT7WJOhNSeEf4ODs6MV9XPyktsz9UC72xUhHqk63UU_J0Jiu2fpC7IW98usQgMN1jzlb2DocdwgDRtqzF-kZ7ApY7Q6acaVCgQ8VrHydONtl9f4Zn7FVb_9azJh-vlBFiNy12JLgyqhehU48vU-4cF-cv8Wm8t7kBHdaJ6sLEsKg6QLQiPaS9qZe4iFKhhqnJyzpexg47GneKqI6vwfhcYKeyUQ8EkXDBGxJXPmCnFmUePxOFbD4Jdg1hFBKcB0kZlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده میشود که فدراسیون فوتبال میخواد که یه مسابقه دوستانه دیگه برگزار کنه تو اردوی ترکیه. اگه قطعی بشه دیدارهای هفته هشتم که قرار بود تو بازه زمانی 15 تا 17 ام مهرماه برگزار بشه به تعویق می‌افته. یجوری دنبال‌بازی‌دوستانه میگردن انگار این دو بازی چشم‌نواز…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30747" target="_blank">📅 18:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30746">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-4LuGVw_AAdfygyLtkW5tHLD1R1NWf61SnhGmjfBBDlG2TZnhxaiP7pB0vHb5emsPaP7fpoG9-BhhENf7MhZ953yPLb56qyeyiYODVGpa9q9EdG6m5duGGGWGcAAr_BVTIBHzwYqahUbWTevv8vZx_Sb-uGjmmHvNG9Z383pTe5Jf-PWvxKTdSGsObr-m0CRmGkGm9Ty2TM4WLtp3XaXHfwnTQcv72fboNt3xGqCwOSGhtjJwyAb0cviY1eIxtsY5P9EMDUfflbD_vifVeChN7ftXkAItRCKeEwTTcL63FxEeqaBujOFztY_wdI7TGurNdqiKDvXFJdt5VeHYAqOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیلی‌قلی‌زاده‌جدیدآبی‌ها؛ ابوالفضل نوروزی وینگر 19 ساله سابق تراکتور که در لیگ جوانان آقای گل شده بود با عقد قراردادی سه ساله به استقلال پیوست و امروز در تمرین آبی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30746" target="_blank">📅 18:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30745">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jc_K3590L3jazYgX264_ilgyMHpNXKTzqNYnh1iKRX9nlqr2eeih8-dSpLKHZJwyj1UWx_Ftyq8KtkBEjGPpEcRX0Cs2_NlfModwEpcVwuZ8CnjBaVitCzQhHiiSWuOmcBr3AGkvY9QD130H_WRo7HM-vd1v375vH2RuPvJ1I_BiR0wKJ9u71D13UEcFvJpI_lbOX8sfjJAw_UiBzlULo8TX7tjYX36KQMjHj1I4nJzP8JnGSHTMcfQvZVo5NieG3e9GqRwxwbuOf4Lcm8yk_6Ll_-X_uuWCV-PmjLp8nPXRlsXFc0dqoDCtmu30mZv982x0KRq9F3avjOdr-IfZvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیلی‌قلی‌زاده‌جدیدآبی‌ها؛
ابوالفضل نوروزی وینگر 19 ساله سابق تراکتور که در لیگ جوانان آقای گل شده بود با عقد قراردادی سه ساله به استقلال پیوست و امروز در تمرین آبی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30745" target="_blank">📅 18:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30744">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrM6FFMPdtaqWcgpGc6Rq3xO6HwIKemnTgZZJ2aBTgTthnrE_WD28hHvOznDZiy0ly9UU8dE5UliHiyIwd6KEdVyPwirzw0UC70jRckP219Oee7lvZEQvpKYwOaCzYscSyWIzYHXTl2L8Gw0QLYIuqR5bMldxUWfsvkyc1EdWYhrj1MfD5vCbfSrQYtz_a9FouaK3EMUn7yvIh-Mdg8dp_CjWJ-sht27CW0SBkbs1dUUWYr_V8UwC7fwrr3uGzEa9x_u6MlCJXGiyUKbcpU_6CSsM0mwmmX84IhJVBjRRFadoEe6N-mvbhFSX9P3V5lbiOhmZnLBkoQipNDAhVhmdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انتقاد دوباره پیروزقربانی از کادرفنی تیم ملی: من با تیم آلومینیوم تیم ملی ازبکستان رو میبردم. با احترام به کادر فنی اگه سرمربی تیم عوض نشود در جام‌ملت‌هانهایتا ازمرحله گروهی صعود خواهند کرد و دراولین‌مسابقه مرحله‌حذفی حذف خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30744" target="_blank">📅 17:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30743">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaKda3nPu2e-2K4BPBkcxwQhNhlDpbRMe7avLE6I6iisbRoUh3QnnFotqvihpQA4owFpJivQyAjkLuSth74wsp_Ff8RIW73_ULN3PFuFshoEsRBKVKJDErm0MeYfM1DwMaaEwV116MR9AhIr_vMcMTWL94CndRMNKgHh4TRodbQaTJ2DxSr4lTMzacDRC0h8e05glWQws2PQgMfah4p0uvSdWoSINluly_jkntQKLH54B8eRcGYs-EBVG1-NFHuJYjJ5nffcBjBRiIsG-gb_laDF0ydVBt-HHtYG4n2S_fT6UDbn7wa7XR2nHy6Y3mxRtqpMxpcdVHWatKdTRG5tZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داوید نرس ستاره ناپولی:
وقتی خیلی جوون بودم تو زادگاهم 2 تا دختر بودن مسخره‌ام میکردن. پنج سال بعدش وقتی به چیزی که الان هستم تبدیل شدم برگشتم زادگاهم و هردوتاشون‌روبردم‌یه‌اتاق تو هتل 5 ستاره. بهشون گفتم باید برم دستشویی، بعد کلید ماشینمو برداشتم و بدون اینکه پول اتاق‌ها رو بدم سریعات برگشتم خونه تا کونشون پاره شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30743" target="_blank">📅 17:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30742">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXj9K9kI58e1qDXPYvCVA3j1W8Zi-FCzR02dr1EgvPlrayM2t86GbQbPO20ui8fcAFxgiTRgItIRnQZHKUWRgg3iK-SCQHVTChfwny2rFmx-zHOediCB1yyld6xVVa1OKCShu49Z1yimX94gyCVU-DJrZyyOpcXuEBa-7zlA15j2p298hFbVcZ6QX5UgI6AbDYF6Osc3ADvykCpgkwIXO8xjgBwj-VO83Wq9vlpqra5Rexf4xoHqWeDHqiGc4wC2JZ8m1fUk86yOEQMgYTt61ngO_WgegRVdFRGVN0gmYJvvkNwcGwrHyI381ZWkXXeaKlEXOBpK7v2uqJKp2mv89A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
علاوه بر مهدی‌ترابی؛
مهدی هاشم نژاد ستاره جوان تراکتور نیز به‌دلیل‌مصدومیت دیدار هفته آینده با استقلال در هفته هشتم لیگ برتر رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30742" target="_blank">📅 17:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30741">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfUAhpLP92m1jriFjiQJ1kAYjMUcOvmGgfKYYUCjuD914-Xa-CldOsKLD7ZYJ995D4Geg7OjkHKSc5oXZ6ssjitpYs-uOmvhzIVXYPkGfscPiGTikOcPTDGFX0GJAW5nzjGI22iPMFz3yJLz_SuPTjD6a_wyD-4vnuGoLSI2-FUT4NC7ufyMfNecrP2A-FP5hF7IWGhodtMvGBGoRegt2ylnD7TbWN5i-gQ8gxJU1oQtqIJC7yWvijT2XXt-B0svSGAfnVNa9_GXonfx3Q-NGVRCZ506mZKav-_AJyluEG8xDX-ydptDDvPSGj5HaePc3LPw3c5_RLYTpX2k0qAAfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔵
لیگ‌جزیره هم ازباشگاه‌منچسترسیتی بابت تخلفاتی‌که انجام داده شکایت کرده و احتمال گرفتن جام‌ها از باشگاه منچستر سیتی و سقوط این تیم به دسته‌های پایین تر بشدت قوت گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30741" target="_blank">📅 16:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30739">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3YmxRcF0IVjSz2OeJGqZboew66nFGVjhJ7jBSbks8qINmBnjJfrg-5H5u_v9Yo6d3yisNnXNk84EPOu24sBpqbjB2quP3xHTQBkmentUfG91eF7DCTSOFXl-I8UWhbY8LRtdvUCeU0JKgTeEe4aAcw-Slmf5PAlr10VLnss3p1fri-BIqhO-V8QZKYk-vChEguAEza-W4CakZq0cuqOux0iljC1oVUoR8-DFscg9KXU4-fGA9--LYumsu-zJq6R26OLsEr4j-Yi2_bg6dTg_GKeu6wAZlQsiCuOt8xEBYfqccicVS9IaREb21HygrOCLernnoy7lr7DxgcdZ_pLDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی به ایران بازگشت؛ بیژن مرتضوی، خواننده و آهنگساز ایرانی‌که‌درجام جهانی 2026 نیز اجرا داشت دو روز پیش وارد ایران و روز گذشته در منطقه نیاوران مستقر شده است. مسئولان به شادمهر عقیلی خواننده‌خوش‌صدای‌ایرانی‌پیشنهاد بازگشت به ایران رو داده‌اند که…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30739" target="_blank">📅 16:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30738">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‼️
#تکمیلی؛ طعنه عادل فردوسی پور به بالا رفتن عجیب و غریب قیمت دلار به عدد 245 هزار تومان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30738" target="_blank">📅 16:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30737">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/peGC8H1wQMKiCowwnffaZt-kdJR2xoWl5j2u_JU-g0a4OpMbJA9SdzDDuqWurGeLm9zCVtlZ9fXS2KgYdOOKgqnRB4tR_batQ-KTT4ikS2mGvr8M6u_fvviREpeaghZC2_WzvXBvfEtfotW5c3E5ezmeWFzXk_SohS0kIP2fjGv1lvrz-P1soppJQKWS5kwtByHUl8qbDhUXfTdIMkZPymS2cXz9BSqdOcCBgdZvg0VquQXnQROIZ8Tn_WO1ex4A9WHnprks9HJ1LlJVYjljr4ocdNZQFJ4IbunGh-TXqV4JP4eomRsGfHxtG2rlcZyU6W_gvpx86b-6ymzOccjrlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
نشریه‌مارکا:رائول‌آسنسیو مدافع رئال مادرید ساق پای راست مصدوم خود را به تیغ جراحان سپرد و حدود سه ماه دور از میادین فوتبال خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30737" target="_blank">📅 16:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30736">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‼️
کی فکرش رو میکرد که نکات فنی مهدی طارمی دررختکن تیم‌ملی یه‌روز به مدال قایقرانی ختم بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30736" target="_blank">📅 15:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30734">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oj-C9Uzc3UOb8SAukf--ve3COibyd-KQi0Rmc25jKiN2LYpBmY5rZE7em6L6FL2-dcTCirGN2XuTRcIYvNG5kWnbj7ZPWnQ4zKc493ykFVEHY4WnDbrZ7m2jylzG3jIQCXjisQ6DXlpPY0Ad43m5bI_8yrYpj6-Vmc7qJ_8bIolMG-3msfQTGSUn-yvQCmm5VR8GTs9BFAzJOVjCGZ6L3F5mTS-mD0tIFpLHVdxHsjw0p6psY4xDUYlm4EwYuyp36tWK-pSrDbcTjK-FgvPnWlvh9QZY367HFb9rs-iucRmPIEoQH8mJYHDJ7kFVObam4kVMt5gzPxYDyjQsVs_S6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fdQhqIYc_sY1lKqdzcLv7mNsihI-5NqOfX-IZYK0tEc8srmp6MTlOH-Kq6ZMl8dCaEmspBkkGUSJWel7Bft_AsFKu_JwK0z-0yMCLAjHF3X1M80f-U-RE23nSx9C2-y__Q9LC2_tlBZKkFF77HAoRGz3UK57vmc5AQN7QM_H_1gLC0IGu2IS8Rq5b7nrPPApK-wvjoBLgy9Cr6NFYHJWb2L_0eOmKyjZ5o6hXI-vzecypyLzzi0rWdYaPxugzdvzu9_UpNreujQqlD9XLzdW3u9EeLlNHMEnOTnxuthv-BVrunGpkGt0Vj39clsPjLTIVdh-USwBVoh1qi-lp_ZG_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز ستاره تیم ملی برزیل برای درمان مصدومیت‌اش اردوی تیم‌ملی برزیل رو ترک کرد و به بارسلون برگشت. مصدومیت رافینیا حاد نیست و بعد از فیفادی به تمرینات بارسلونا بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30734" target="_blank">📅 15:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30733">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEFX_ycYeqfvie4MzA6eO2zcrlXUiaWcZjjNvI9lbbE6GJ9uYJfFzHbe82RVg47HuSJLn9PTp8vq0KA3xrUzygvq7k-12BP8EOBsovLgmUPXSWH-RpDbNWxXPKdwfsxDFs4iCkV51bQnPA3SWOXKG7yJwAAv_zF5WEszj-qPz_3ty1CwdSt7OwlUiwByIu6N7MERApRXJ0LgHpPFTqVwbCXkWJfiV-3q51cWZ2-W4NW7qCA7H1UuglpF1n3rlHM7epDI4TXKXw23db7_5Af9-80JpeIpgRge1rupwg6PfZz5RLCIjSQfWSNvD_8pIVlN9Rt4Ag6KvG8vq3CbY-VDWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رکوردزنی‌تاریخی‌حاج‌صفی!احسان حاج‌صفی با حضور مقابل روسیه به ۱۵۰ بازی ملی رسید و با عبور از رکورد نکونام، به رکورددار بازی ملی تبدیل شد.
‼️
جالبه بدونید اصلی‌ ترین دلیل دعوت حاج صفی توسط قلعه نویی؛ این‌بودکه احسان رکورد بیشترین تعداد بازی علی آقا دایی و جواد…</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30733" target="_blank">📅 15:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30732">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRMQbXoM9svClwr6vdTI8kVy7Fv7d4RLAFpEqAiFbWgvy211M6zkyFEKo7a_RE6ahja2kRXAW5cnClgYx68C7XXm28g8nij1Gx7XUzPYO3lXdlyUDl982sc_rOLSBBv-helLgQ4w5Q11yiGmQgD4IGPHj4nnZAjuQ8BXXIX1kLl2qMYyvElCeNxNMDrVnwN1h7OVbF86-4oQKgyFe1VAfC53PNRLNyk9NRVom-F_kHJu_RX4rUzshesQ9ZFtB4gA7Sdci_LY1p1GPV56GBAy6NC6fqdAR2tEmRj51qCYxWJcL8zPyrBDJvzK8qlz9uqZAn75b2rF5Slvlmze3HqKEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هایلایتی‌از دیدارامشب‌ایران
🆚
روسیه؛ فاجعه کامل؛ بی‌برنامه بی‌تاکتیک! گلزنی‌هم فراموش کردیم؛ خوب شد نیازمند آمد! دو باخت، پایانی اسفناک برای فیفادی سپتامبر؛ جور کردن رقیبی درجه چند برای آشتی با برد، از نان شب واجب‌تر برای فدراسیون!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30732" target="_blank">📅 14:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30731">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uK7zq3r49Ib23Y-nBY0ypgQ7mariQgno_ouJRg9aYxhU6LXld54Gk6tQz1j_07Y4bqod7tLr5nN1W8ouFF569yLAW_6BnOwaZsT1EAbEE4XTNT69WLm__9_DcIEMliXQFhqW097wgGts-_aUPotYFt9BigiKiU9NmK7WlXNgatpEuI_OFtLH6DbjoOSeF8v8uy2bHQfyc3bmS8L2F4pwT-e5t9deEwbhErL7VGWXUoQJhrnZffo62opCWbaRcxUtFFHVGTA_J83R81Qzyi27G65gS3CHTrcGRQ7-k0SHohjGFjVuOvttbngY30hQ71SPnLhzYoUJUPKi_m1QzYNryg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال
🆚
کول پالمر ستاره اسپانیایی و انگلیسی بارسا و چلسی در کریرشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30731" target="_blank">📅 14:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30730">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIts-_aI5_yx5KrMCipduFUc8PG5jahjkoIeJ7u3uYETEIoC0Uxji0diSbqK1_gpkVBdyFmoOAxg03ijju_y5kZadolW0PpgejAVXT7fz4qEpxCYW8xncmBMSjzL0Y8O3dIq4RyzBnD1WD6rdQ08E6IBK5S4Ij2YqfVjjYaDfXrs68oHTYBfxhNqcC3UBh1PqKRHZIXejcyWvHLpWzLSE_PyJWfVL_a3vlZiW7h7LKkJERpKjNsRmO3iKxx8wf25kPe6aq8tBc8qsb6kKGz8q95Vprc3AAhDFESPjJ_XCsfdZ4PJ2NMR3-5ZEzfxH_aDmdI1axRlrF7fB9EcLEkrzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔹
معیارهای تعین قهرمان لیگ برتر در صورت لغو فصل جاری بدلیل جنگ از سوی فدراسیون: در صورت برگزاری‌حداقل 75 درصد مسابقات رده بندی براساس جدول موجود. برگزاری کمتر از 75 درصد رده‌بندی بر اساس میانگین امتیاز در هر مسابقه. در صورت اختلاف فاحش تعداد بازی‌ها استفاده…</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30730" target="_blank">📅 13:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30729">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qd4US04YyRlu10yJP8pudA-9rrnu2pzoHBbI5hK0eLrHb4I_goIlMAGZd4nXwdekSNZuvKHw54P-_qnE6YYHleYtV-vTQLcrV6394PqNp8Vm88wo-rhS3MC40bIH3mQ2woCQdfsBVw6UoHn4ZGnJcDix9Ig3qBh2iKzBM_VbhB5XiITDNtjWLTidT3LbZLTwZueJMhGN4ZM2fOTLOx4aXBTV6UM0RBQcvlwzncNGmI_V4Kr8UxYz4ez1fVyPXZ6bqf8VMoyptMftlDp_MnQtWdmYqOiSipNeSrruCgpFLZrTk-RftXQbK37gV-Ls6e_IyjNtN1nb4w01l3StEiyO1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔹
معیارهای تعین قهرمان لیگ برتر در صورت لغو فصل جاری بدلیل جنگ از سوی فدراسیون:
در صورت برگزاری‌حداقل 75 درصد مسابقات رده بندی براساس جدول موجود. برگزاری کمتر از 75 درصد رده‌بندی بر اساس میانگین امتیاز در هر مسابقه. در صورت اختلاف فاحش تعداد بازی‌ها استفاده از میانگین امتیاز به همراه تفاضل گل و نتایج رودررو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30729" target="_blank">📅 13:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30728">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXZRpixKcRb1xP9s7XqzOV0azMZMMxOr2y6AQbkJni0AV_zNQ_0l-50tYgS-yQYSBh4udqFzXobzan9atN-JKCk0pJwjIif30NjR-O9DfpRbLHufhAEkurRdkpAREXcffAraVqhEQGKe0sFYTQisXVoMbAksTo2EZUK6JBye4ARptIZYfla8NqSPnbsJC6kySE4yb9faKnzH_StdaG4G3hl5eSqLctXSbAHivMxR149oGd49iaJGl60D10vKnocZT6HK3smd6sLnDCg1rVN_chn0n3VYubwubBhImjaabuZ5dcsoAIfPF-5YGxxiNsFDsx5gCoreg9T1qrWdqo3zbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌‌های رسانه پرشیانا؛ روز دوشنبه هفته‌آتی‌باشگاه‌استقلال 30 هزار دلار به مسعود جوما پرداخت خواهدکرد و پرونده شکایت او بسته خواهد شد. حالا تسویه حساب با دیدیه اندونگ، داکنز نازون، موسی جنپو و کاریله برزیلی باقی موندهه که حدود 2.5 میلیون دلار برای…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30728" target="_blank">📅 13:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30727">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6wTH-o4tM5Hn0mn03wtsocO-AQTyQN4Y-YwxxiQdzuWMZMr9M6oeYh4WIYMfe7O3W1RlzafhzkzubZupSn1LrZpZPXIvaPwvg_bOjl3y01gVbCg9LyCuZAlzmm0wb-OdAA97SnG_LkPTA7ErC5i7etX5stm-bn4jSgzwQ_Jk9nG0UbVJBLQ2EFpX7aAGmC4_W68ovCypFWWlCIcEUjFuefKGs0cDoTfGLKrMTPvDE4ysrvXBvWszlFLoDHlLSiM5PsdY0TDOQzTH3qta3TwWoHQIhiFMA5cm9VcblRG6MBjJReIlZdnn6GuLybZULK5FxcJK3DX5xhUrE3KM-7iTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لئونورملکه‌آینده‌اسپانیا:امیدوارم یامال برنده توپ طلا شود. او لیاقت این جایزه ارزشمند رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30727" target="_blank">📅 12:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30726">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hnvm3B78tIaD_-osG3-eR5pyZZu49Theroez-kz9hi0xDULMqFcvXgGLNnz9DzyVW1_8TUBxEj1h9oW15EY_KVNk1A7sFC0hL1UyTGguz0ZOmIV0fZVhp0EbB-pMZiCSnTLtG0BCmXRzs4dLK1XXHzGjLN67PspCYqMIajwQqVl7PUtmG6pFarbjq4ojRMT_F_aezNZ0Q1oi9QXjqIfv9uxooUshaqY_Wk8eSeqZq7Ls_CbPa2ZHU4aS8-FiiPBLufcTUC4OjUEUOmEfKuKDeL4RuQTfqUgwF018KK2BeUJLJYjy3iVz57pC6s_egPqJP81iaWdgC_11LRYyfFWVHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رسانه‌های‌پرتغالی: کریس‌رونالدو بابت اینکه دربازی بانروژ30دقیقه‌گرم‌کردن و وارد زمین مسابقه نشد دلخوره و درخواست‌جلسه با فدراسیون فوتبال پرتغال داده تا تکلیف او در تیم ملی مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30726" target="_blank">📅 12:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30725">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb8b65b7df.mp4?token=D_likD26HPIVrOTNk11S2_RsWuWYU9vlMGTi7SNQvATfAGaotiH9Vq-KQzw4PJZ4tMViNf8gJULuNjowcKMhBBXQ889klutXlvQ6DQRTViNseHrtWTULPOvDu3kPDTHxcRLdRm0km1kccf_G7pUfw7W_wOW5Y6b2ozhBANoosoBk_GEkRBZCoIAZrDQJoyqBSGnOuQ6-daYGxOvcfaFbuPGrPkbu2p8brbNQXiPDhqqmusDXcaXZY6K6Lya3Gs_rtl9ZB2hilqQABM_4ErArv3ZxjKGUyjYHpFkB1eC5bfrg6XAhaqKNIYq34JFHcdWVQKOsPBSrx_OHOWlajZ5OlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb8b65b7df.mp4?token=D_likD26HPIVrOTNk11S2_RsWuWYU9vlMGTi7SNQvATfAGaotiH9Vq-KQzw4PJZ4tMViNf8gJULuNjowcKMhBBXQ889klutXlvQ6DQRTViNseHrtWTULPOvDu3kPDTHxcRLdRm0km1kccf_G7pUfw7W_wOW5Y6b2ozhBANoosoBk_GEkRBZCoIAZrDQJoyqBSGnOuQ6-daYGxOvcfaFbuPGrPkbu2p8brbNQXiPDhqqmusDXcaXZY6K6Lya3Gs_rtl9ZB2hilqQABM_4ErArv3ZxjKGUyjYHpFkB1eC5bfrg6XAhaqKNIYq34JFHcdWVQKOsPBSrx_OHOWlajZ5OlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مدیرتولید محتوای شبکه تماشا: درپایان سریال امپراطور دریا؛ باتوجه به‌درخواست‌های مخاطبان بار دیگر سریال پرطرفدار جومونگ پخش خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30725" target="_blank">📅 12:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30724">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0luTDIk3h2Gdg7MNhzG5akLElMOHWIRGFwYEqvKXiCmbX4QFnq1HW89xkNakf8-LWWv1VJkFmhNvUh42KbyXUOpG7CBmytoCXQEfKPODDrg1EfOsW86vduj_eViN0VqzZ9tWxgtQDaGajMdUv4wmV5Wr5HcAtlKQnZs80vNgBW7grUvHhxqESF6X8aQuqAg5GXM6cMI7kBe_WeKN3o22LakpOAZYT8BdQv2gIwxrIOp7o7Ylrhg2oexXDoOKt99X0-tw2O2ohX7wdv014a1zgFBcusqjHhbNae-7vkS1yTZUi7M7OtgpcHH6h5JHtKiq9Ddnr22Pg9kI9saxwd54Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛
محمد حسین کنعانی زادگان کاپیتان 32 ساله پرسپولیس از طریق ایجنتش آمادگی خود را برای تمدید قراردادش باتیم پرسپولیس درنیم فصل به مدت دو فصل اعلام کرده. قرارداد کنعانی در پایان فصل به پایان میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30724" target="_blank">📅 12:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30722">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3853d1925d.mp4?token=CNFQXdOkTP7cpy3SWUkFfYtNQh1iBnlbMKTkkPjSHF2JE1y7995qxPDVaKHT7Rp0f3tAislm5L6PuGjZ_23kwrgbP2gSDJWOoZFEcaIh9pDrocPQiXdZ5jbvbEqZdC_kxtS6obyDfLullluwez9ReHx2iemcrzd1pMKOdSdBIaCVw1k4Lk9AV3_xf1He3DIAkgMCKrLIx5YRMl8ZSh3QgZZzLn2St95L7AeMteIOY7cKbeNFcXGByR8OT6kTNZWVFbuvgyva9b6GyrbSFb4trD7C8Rdbr5w_S9jKbFHeRLVmj1g_-MdWuAnL7kHegJWEgK4YxQpYIf0LROHA7WEjtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3853d1925d.mp4?token=CNFQXdOkTP7cpy3SWUkFfYtNQh1iBnlbMKTkkPjSHF2JE1y7995qxPDVaKHT7Rp0f3tAislm5L6PuGjZ_23kwrgbP2gSDJWOoZFEcaIh9pDrocPQiXdZ5jbvbEqZdC_kxtS6obyDfLullluwez9ReHx2iemcrzd1pMKOdSdBIaCVw1k4Lk9AV3_xf1He3DIAkgMCKrLIx5YRMl8ZSh3QgZZzLn2St95L7AeMteIOY7cKbeNFcXGByR8OT6kTNZWVFbuvgyva9b6GyrbSFb4trD7C8Rdbr5w_S9jKbFHeRLVmj1g_-MdWuAnL7kHegJWEgK4YxQpYIf0LROHA7WEjtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بعداز مدت ها خانواده ات رو راضی کردی که باهات بشینن یک مسابقه فوتبال جذاب ببینند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30722" target="_blank">📅 11:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30721">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpdTDeB4PvnTeblexrE6Bel4D893o9LdtCMP4vejKgFh3VPuEeEE-FYxz_Dut-8VHdUULLFfDNd820TNVeobmmDcYF-SChIga6alp9ZCFViiVradmM0Zo0DJpG_h_NoQ6vJhohnOPjQseKQndupSoVq29W3KY_1VeRRLN8NCEf-LWJOkBwlWmVmNK80vYbg4mVkOniAarMK9DQdyUWTOnXkoXbqM53s-d2R-HhvHFXshIPl83jEq3TcaTMdNe4yqyBlSMoWx4kAZjT27OZnps129srPzsq0W5ITBKIbI_YerAnjkyF1_Fq4ZBT4Jf7fq3E6hyVvqeE2XAr_iA4oDpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باموافقت‌سرمربی پرسپولیس؛ پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن جوان تیم پرسپولیس، به اردوی تیم ملی امید اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30721" target="_blank">📅 11:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30720">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmiKaRZk2SY70-9Gi7iD5Q-GZ0PIBmekECYpGy1uh-k9qMKIAYQtnr0aeOfQJdzeCr8BXwDZtcf8MEj3SxoITWTCXr8o7FOpkFsdsGNv_orUzBcMFtAHGL0CLMOBcPdbipVg-2jNganbXpPUqsiTzkbJtP5QslMduA2CNVyn91V_SZaNvvjoVCmB56t6TTNlD1PIWffDdUwM_ChZixr68i8N4gIzbvlwkqRvdj4xSoPDCjk3AxqB-xrU6XEpVH8GtsUNvbCtTa8f7Y6NNFVhkeYKrcnOnvmprIP6kHJkuXsJyROB-dgZ-xnpoC0f7NgVAQ__ksbXgNa7mhYn1OUQBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
تیم‌ملی‌برزیل امروز ظهر در دیداری دوستانه بمصاف تیم ملی استرالیا رفت که در پایان به تساوی یک‌بریک رسید. رافینیا در واپسین دقایق بازی با یک پاس‌گل دیدنی مانع شکست سلسائو دراین‌بازی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30720" target="_blank">📅 11:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30719">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPO6RxvgqgplAxJCssbZp14GtMqlcVeqx70VNSG_3ut-t9spMR9tqD_7Gi5ognS8woMZG4usKbWlJf0GN1rwdqC3DOtO-ttvE4nzNNQJUjgLcxarX4q5zByTSq07SGrEUEL1Vmo0W2c7hIbNTNIJPv7duan114zqF1Rc_u7m5rbzj2BKGsfHjklzHKgaolK7RvaCuID7QvWoKfqqTWXrh3GDZnYVJxneTMpAN19SeKCFKZBCw_laCB-zeE3YBSpHuI6sr1BNJ4wUuWTHFzeOIdpjTg1nwmFX6cStQoJcyYwzU2H3wPiH6K1wWvlWt7DpZ6dKmgRXYK5WW97zJMOPbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با حکم فیفا؛ باشگاه استقلال محکوم به پرداخت مبلغ 30هزاردلار به مسعود جوما مهاجم کنیایی سابق خود شد. آبی‌ها 40 روز فرصت دارند تا این رقم رو پرداخت کنند و پرونده او در فیفا بسته شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30719" target="_blank">📅 11:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30718">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXSPAHAAvXL-LywPcjBt0YCjB1ZTORkxCh_oDJ2uEj2W0ro4cGSWAcPEzSfKzrH5Nc9l9DibswMiRwS7QnDYa7yX6SgGl1bR8cwnOV6mKoe0yQo6k7AoQ9h9iOWwKL5s6Z3-YpGUK7dqCWNGSjZB2NpCh2Zc6WANpYcRsXYm1_Lx7n8ZxhYPEGkUznManrwQ_-1c8Gb3Cgv5t003yXeAt0_eUDglTWtp-pNZt9oT79377huYd4uj1D7Mu-ilJkhDeKFiewA30hnu1mpAV1rsMG1tg_66ucnvapYYQ22ckztdgILzKEiOFRqhzv8H0SLx6ARxYB59o9NnmhTfAHEjUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد اسفناک تیم قلعه‌نویی مقابل 50 تیم برتر رنکینگ بندی فیفا؛ هفت مسابقه و تنها یک پیروزی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30718" target="_blank">📅 11:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30715">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0zW4ddwnS7dsEHgiSG-pUGuknx9HND7BaxhZfqyUEQhofwsrjD2H-53lRMnQFWjtolYymsTe7cG1WV6qR9c2UuG3xBvYjz2UDd5w42IRlm1jyw7ijpSpMMq0yT4KdMQ-EU_ffR5k5D7EQ8ZshS7khJQv9oGAPMiaBoL3kwg1oYRpJDB5Yo8-G2iPI2__Eo7cRojQrqs6f_dx-9hpNx88zMFRorRN6I7LnXSiXgjDvTKaMeaTy7jx8Xh5Z5B5cq8-8_4FruNlKpQGzDBRtW7F-gFTmDA__4MIuHHJaYwsfAjfpiqfec1SFxKxXgKG4oedC45flidPC0MIdxPS2vdmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ نشریه ESPN: فدراسیون فوتبال پرتغال داره تلاش میکنه که کریستیانو رونالدو راضی شه در یورو 2028 نیز حضور داشته باشه و در پایان این رقابت ها از دنیای بازی‌های ملی خدافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30715" target="_blank">📅 10:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30714">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guUB-dK3os5bcF5vNnPd3T-SWnLk_IiVjFQXra1C4hb7co0GyT59NOUNDaLUqkToWzDQz7-sAWPvRibUVvLzBg_8yMZTZEAHasH5sZ8r5wY0ba_LYfe4DGqk7fBg3gYlTG81DT9vFY4bZfTfveMn6fnmhgqM3bU8hRr3n1QnkwPr1qGtuEQNZ0dyumcfw48vX5FTzTbZKysg46gCObhZ20aVhSlQ0PMZYeTi7Y43bPKi_kbuBS__Vp8rPipZEb-r-_51BSx2xekmuxNe-pqvhsRUCnlZ4zhK6pjzQgjU6X6E95aqt3NkEMaMAdSupNmfnIzgFlMI5C7RO3Gb8-jEAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آخرین شکست تیم اسپانیا در مارس 2024 مقابل کلمبیا بود این طولانی ترین روند شکست ناپذیری یک تیم اروپایی در تاریخ تیم ملیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30714" target="_blank">📅 09:51 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30713">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b22806bf3d.mp4?token=AoycVoOQRrGTTLg31s0TUHd8h6YNDJzv4dlJaZUSOibbfjUWAe23BS5-s0g_y16MWX7QRjSUGC8jOli8FjbMl8VynzpSSDyZOrxbZ6_UMClfYtFK7-3gK2EWli81Yky5hi2k0sI9nHSqUhwtN-0zdOJZEs4r7eKTlgVnrUapRrydAT6zcO7xj8RKSUHj8y0b_GWExSEdqCJBFCKDOph0-Y6o4BfVx84P5gy099XfelPlngO7jt0RwWnUipSLVR7hCa1h9O7z8b25J52MWCARh92xQfRMeZFwKmzbKfNj617ivJF6QXxUbuD5I7ysBxhKkA7Q08tH95auibCWd8Rtjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b22806bf3d.mp4?token=AoycVoOQRrGTTLg31s0TUHd8h6YNDJzv4dlJaZUSOibbfjUWAe23BS5-s0g_y16MWX7QRjSUGC8jOli8FjbMl8VynzpSSDyZOrxbZ6_UMClfYtFK7-3gK2EWli81Yky5hi2k0sI9nHSqUhwtN-0zdOJZEs4r7eKTlgVnrUapRrydAT6zcO7xj8RKSUHj8y0b_GWExSEdqCJBFCKDOph0-Y6o4BfVx84P5gy099XfelPlngO7jt0RwWnUipSLVR7hCa1h9O7z8b25J52MWCARh92xQfRMeZFwKmzbKfNj617ivJF6QXxUbuD5I7ysBxhKkA7Q08tH95auibCWd8Rtjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درفوتبال پایه تهران چه خبره؟! دعوا و درگیری در لیگ‌برتر نوجوانان تهران دیدار استقلال و شاهین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30713" target="_blank">📅 09:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30712">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd646dbb0.mp4?token=V4sQaAoKKMnLqNY86v_Sp54jlm146tKExEo--VLlRAWJceJqAbGB-WfqMo8EtJTHklXdyPROxCweuv4_CaVhirHW3SuEBUYayKVqbzGZAMUr8AHWI4r4YYh9pAnzBWl8hvB4tv3jbr5cP-tC-BKV2i1Q69h6hMjWEM0wuJ36VDre2CyOWZkFX45adrBFlFGHNCLrGCxF1SYa6w9sCPcj5tJUFEb-ly3aOqka4lt2SagSkyJgTe2Cu8YlHc6NoLB-FZk1ohcLEEh6oWdz3wsVQYk2_mJyDWNeUwsiZjqzBe1jDXHwI1wBhWYiEmnuyK6eOrEYmaPTUXBQKBWc8M_U0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd646dbb0.mp4?token=V4sQaAoKKMnLqNY86v_Sp54jlm146tKExEo--VLlRAWJceJqAbGB-WfqMo8EtJTHklXdyPROxCweuv4_CaVhirHW3SuEBUYayKVqbzGZAMUr8AHWI4r4YYh9pAnzBWl8hvB4tv3jbr5cP-tC-BKV2i1Q69h6hMjWEM0wuJ36VDre2CyOWZkFX45adrBFlFGHNCLrGCxF1SYa6w9sCPcj5tJUFEb-ly3aOqka4lt2SagSkyJgTe2Cu8YlHc6NoLB-FZk1ohcLEEh6oWdz3wsVQYk2_mJyDWNeUwsiZjqzBe1jDXHwI1wBhWYiEmnuyK6eOrEYmaPTUXBQKBWc8M_U0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درفوتبال پایه تهران چه خبره؟!
دعوا و درگیری در لیگ‌برتر نوجوانان تهران دیدار استقلال و شاهین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30712" target="_blank">📅 09:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30710">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMHgE9emMJvEzafXIUHBqBQV7ZZwPkVFq3cQ0C3CG4XxhHaE0bTM05JdOaSIAR3wFP7CFe4jSRBOvny6UJ2Jo_HAhv3da1vOeLglN2EUHcvoWLsL-KvcThSRBnx64j2D8slK40jeeWiCb_jE2nNooP8qUY_IwafS42L-DSGnC9U3vo4UJFuTzHhnRL8mmA7a9kUA6m7x5tGhpD1KeD_zB6I2yQ6wjxWCPqs7rEvGcKzVdWKUWczL0KMVmaIkn2HibHzq3wI3RATeyankvlF_RmcQH-gOSnFu_TbNvfeZTA0aYfDiX4m31hOdR5oH1J2vvdM_BP95mSF2rBago8ebQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ مصاف تدارکاتی شاگردان مائوریسیو پوچتینو با تیم ملی شیلی در سن‌دیگو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30710" target="_blank">📅 02:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30709">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNUtgphc_qCaB_o9cZotHHzbWVVU8xI5YXbios_KBvqFYyR5EggW5Ju8CFouqUq5rhY6KC9fQNhpxMM6nIvVr-ONihZgaC8LGDwdNWiLDf0ziByIOvg_OdqVeZGl5PXyRbLCjo-BkBR5jb2T8KHo-pIXM-XFaHCOxwKp8KSSZ4u5LmBU4iHVy2erkIwekJPPt-jpsBj0hIIAs_G-DvHrviNIsfhM49R2bxqfw0YeC1YqhMYZypnE001spLKR3ZFO4r5EsPua1Clvx1Mp6H8V91nYk_rU3Gx-oSgE9-VZDd9w9ngsgc9mxZfxic7JzgJ45h-2Nx18wuGlOdIk3ZrFwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
برد پرگل ماتادور‌ها با درخشش یامال و دومین‌باخت پیاپی تیم قلعه‌نویی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30709" target="_blank">📅 02:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30708">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKvrK-jEKVGJstdNwbloVPIi80OCOubB6ug5_LMFRzMVW75HoKchKxNheCKlrb66CwPKt_hM4OWuMVAKDT0x0mooQQYUWOqeMJwRrxky-lSGLJmWSKqtZWAN4-857Z2EuYWM2v8EgGrvwVHu7rAf3cMbWk0kRO0XUl9L7RoL0GxuRTHNrhrtbJEfhDJ85zyWkX-K0JzPHeH5rhdVHNQvAvXk4EoWlTSFzyzRVApKVuA6HaDPxummgT_-eYcJqTXreivYgbvLatLUwIcODX7dTRCM4Tq4tyvf19RODridYV9mR8a66rO2qEuvrOZjTHd2maL6_nmmqwUIc-SbFQa0Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج مسابقات تیم‌های آسیایی روز اول و دوم فیفادی مهرماه؛ ایران بزرگ‌ترین ناکام این فیفادی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30708" target="_blank">📅 01:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30707">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6w14boOK94n5IS2eboJ3oivaPYzJvZnuX9F8PZJflLCIfz7n3oW0LoFpg6sSq4kufUPJdxsf0WvY524bi0T7wtdAH5HEOYRus4l4vPXHx9EnE-KOdhrV1zvHfymR1TMcmstllZxpypg51RyYZNO7R1w-vgGm0TLgOW92aHsrTCMIiAyXuLwtfSpVAM1xP4N5KGg3hbVXaFibXwSAwu30OKOxKbQvXAk7oO4wCPMwLChe8GM1gcDKEU940LZfFLJfw83hPbrg2P04r591YpC6d33xMVKtweE6MncgN3g9ezTMAjqIA8IUuitNcE753EUti4XQ4_iNczbIPPM7COwMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار دریافتی پرشیانا؛ مهدی تاج رئیس فدراسیون فوتبال علی رغم حمایت‌های خود از قلعه نویی در رسانه‌ ها اما پشت پرده بشدت در تلاشه که فرهادمجیدی روراضی‌کنه‌که هدایت‌تیم‌ملی ایران رو برعهده‌بگیره. اگه سرمربی سابق آبی‌ها اوکی رو بده قطعا سرمربی تیم ملی در…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30707" target="_blank">📅 01:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30706">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twvURjkJy335qJG5cJqC4m8hb0kAX2OnDcPpqilYzrPryQyPMMT9HLIEAVkBgT0-cr1cF6Sm6maD_9VZBX0bDCJ5gwL-swu-XiRjHyChExydNBAracLIV204UTpe9CUqt3ljgicvHbnvMRDzSricuMQ2Yby6KNgdILJQ3tlO8rXdPb8nOnFTu2JXB9u-fc6LV2XveHFFJX_QhOgXJL6M3G7cbkJHn4UO9oJI5DBBIDOodQsatxg1RRnWuH0aYBA05QBPi0lB4w2EsveEJ7bdW0UNQuYtqqhJeeqNzuRylIw3_fCDAvx4qvHS7dx0P14-ig49NNaEDSzXnExXWGPQmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با شکست امشب تیم ملی مقابل روسیه؛ پروژه اخراج امیر قلعه نویی از هدایت تیم ملی آغاز شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30706" target="_blank">📅 01:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30704">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ez7fm2YFZZTAuPjcliQM1dxjsKCEfu_zf4rlLZyM7dZA0ThvLs1kx0sTEMeW7Hlr_i4ihJRkSl6Q_ErTauLJXP82tFxupGmnfXTu9ZmY6RLLYsqXQYRLMRVG8kuw0YTsBXfqghj11v3nwc3nYt_zut-0OiNu4lwyrITDLFADsucs04K-xKuclltEd4ieFW0FzwN2BuAd-nAWkrA-hzGfMRWkSuHp7mRxvFi9aJJsKztW8E69mkaEJ6_-cSNXQwyWfNohvlE5yn6gNnKc_H4e4UEIOpICIfpUhNDMxFyRxl-VWjSdoIkiBXhNfc9Nq2ldpCNF4qrbbC5LBYLV6gFRdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
#تکمیلی؛ طبق شنیده‌ها؛ فرهاد مجیدی اگه اوکی رو به فدراسیون بده حتی ممکنه در جام ملت های آسیا رو نیمکت تیم ملی باشه چون تاج بشدت دنبال اینه اون رو بیاره سرمربی تیم ملی بکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30704" target="_blank">📅 00:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30703">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✅
هفته دوم لیگ ملت‌های اروپا؛ پیروزی ارزشمند سه شیرها مقابل جمهوری چک و آتش بازی تماشایی شاگردان دلافوئینته مقابل یاران لوکا مودریچ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30703" target="_blank">📅 00:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30702">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brVFH0-lWE1NBUk8fdwnkmxZ6fOr197N5jFrvLRHQ7NwGIxZevFRQymMgmQROTynHkdclV1qkTprF5Qr4cJe9tRz9hJoBJPhkihaz0BA9F0BnG60lzOgWG-FatBsQDvqqkJ7vhk8G4VO-U5Y5zMfoaaQyRMkw48X_ZNhZP96YvxWU8qIEkTQtNiPwVewf78uZce4FrKFrCY53VpGQddWN-DMt59vo9aM4hf7p3iPhZFv1OqBzc7rWmI_Je3DMENCdCQ7DiMh2_NoGTSND3TDYCH263G44xVvp9dfwByxnM0l8VDKP6UE6U0Wqvf-9TdxBYgTQb_pv9hrbxeGSrDn_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ ازتقابل یاران یامال و‌ لوکا مودریچ تابازی تدارکاتی شاگردان قلعه‌نویی با روسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30702" target="_blank">📅 00:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30701">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c014a889.mp4?token=M5mkx-C_8LkOW2WCMsc8ykJh9tFn7OBPK1Hqd6LWpMBfr93q_7dJxXtShaYRPOhSaRfInBGpzghC6VvDc_5ZRrNnjHGdRU_RCQW6STdDoKNYtVKutR6_5eBqNBy0ItbaY2Z2XaDftcyp34ruYeAP_evoW3PgH8D12FYIkF5H5PeSMFJtsvBhNL3za00a1oKWBdUAtmKu3hCmCKzKY0udH87uLzyqlPO19g55NV0u6APuuzgeV39IzTYRoY_tciIlnFSArUPS3GijYIj3zWExOjl7Fzbo6i-TdTNivweV3OfE-7FJMRD9F-sI7ihWPZLCa5pWrew7Ozc4TZ-7NY81JDj1Y3cq89H6RLAGgOnv9k4zS_ZtglddyEvcdCm7AIHWvw4I-uPslBPoqeiXrhZ7fQ77VximhasYN67ecRTxf-RUE7UbPy0siUw_349W2UqVy4JJrYx9umJqeQVemrzzOJ0DNG2KRdk4rG566_qji7o2OjbTegkDlF--KGTbNAB-qEqyAFx9geJfO2XDJPocSJgGap6U3_caxq3e4HTpyVgSzA3Z5Y4I9s459t2z1aFwH7Mla-5FN-9mZwBXBcLHvTg2x8vETO0k63RJDSwORdlRkNjTgdMw9iA8Pk2uIcfW5urOVPO3LROqEFTOXEkS28EIHDMOZDTT1R_omkMR370" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c014a889.mp4?token=M5mkx-C_8LkOW2WCMsc8ykJh9tFn7OBPK1Hqd6LWpMBfr93q_7dJxXtShaYRPOhSaRfInBGpzghC6VvDc_5ZRrNnjHGdRU_RCQW6STdDoKNYtVKutR6_5eBqNBy0ItbaY2Z2XaDftcyp34ruYeAP_evoW3PgH8D12FYIkF5H5PeSMFJtsvBhNL3za00a1oKWBdUAtmKu3hCmCKzKY0udH87uLzyqlPO19g55NV0u6APuuzgeV39IzTYRoY_tciIlnFSArUPS3GijYIj3zWExOjl7Fzbo6i-TdTNivweV3OfE-7FJMRD9F-sI7ihWPZLCa5pWrew7Ozc4TZ-7NY81JDj1Y3cq89H6RLAGgOnv9k4zS_ZtglddyEvcdCm7AIHWvw4I-uPslBPoqeiXrhZ7fQ77VximhasYN67ecRTxf-RUE7UbPy0siUw_349W2UqVy4JJrYx9umJqeQVemrzzOJ0DNG2KRdk4rG566_qji7o2OjbTegkDlF--KGTbNAB-qEqyAFx9geJfO2XDJPocSJgGap6U3_caxq3e4HTpyVgSzA3Z5Y4I9s459t2z1aFwH7Mla-5FN-9mZwBXBcLHvTg2x8vETO0k63RJDSwORdlRkNjTgdMw9iA8Pk2uIcfW5urOVPO3LROqEFTOXEkS28EIHDMOZDTT1R_omkMR370" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
عملکرد سه دروازه‌بان تیم ملی ایران در فیفادی مهر ماه؛ دو بازی، پنج گل خورده، صفر کلین شیت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30701" target="_blank">📅 00:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30700">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnnQNggLiJCCtgkIVOvmon-XUOaMzeHEOj195qGS7_--_lliuciOfXuefH_o5H4h83rmGftGnvZ5V5J51bPAakPjh6gXplgBbPDxqSliF7bwr1RQuVgpJ5HYk6a83uEKOB3_oRl7A-cLMQyyMLPzPnlbFQVMvilZ0H-Wp_tPf6cBkzUHf0rgmYoUBMpKYYw9Zgug0xyqmEK4rCqNZKA1I09Gk98hQCG70QsPiQl-xtO9lihhMD2Hl9pF8so5Ct-wYONQmbaERkbmwjHg_H1eRqDE2XAX-nAq2ysODrGgfc0tFj9SZODro4UZ1FGowTNn2ut1vv_i25ESw12kLZpUWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هایلایتی‌از دیدارامشب‌ایران
🆚
روسیه؛ فاجعه کامل؛ بی‌برنامه بی‌تاکتیک! گلزنی‌هم فراموش کردیم؛ خوب شد نیازمند آمد! دو باخت، پایانی اسفناک برای فیفادی سپتامبر؛ جور کردن رقیبی درجه چند برای آشتی با برد، از نان شب واجب‌تر برای فدراسیون!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30700" target="_blank">📅 23:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30699">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAiae3nWJvKlXbQs7r3hTb7XFlhCZIUTDhAezl-FvhcfzyoX1nnMRtyvVyF6Oxl0noJoCUkIYetQ8vnweugLsqebaJY90hsuqvXpsJy9vb0lr_h6B2fpHCVvo7ennVHwGQXPSGwMEGQslJ4ZKo_JDm-D8Dy_TOLPbfzs3zGLAT7TrS4FeFkWNaHqoSe658eNSlIu6cC3n3nL2UJ83uOpr7f3fejJajMTfb2kfUaqI_bv368YQWX3I3_O3m7HHOtyYpNnjQxw8la_eZoHXrKTLLBdLxBjlgKJajgO1W5-roMwL2hw3ZkFsK3xc-9gYQNv9l4EzdLfKWmKOFLBMj9y6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
هانسی فلیک سرمربی آلمانی بارسلونا بعنوان بهترین سرمربی‌ماه‌رقابت‌های‌لالیگا انتخاب شد. چهار مسابقه، چهار پیروزی، صدرنشینی مطلق لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30699" target="_blank">📅 23:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30698">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42de6680af.mp4?token=nSL1_5qHfEd7du9wG5O-n-ACjGrhfGkiyqv1kJEyTDqg0DVRUYz1DHMwktcUx4WoJ1PrTphyfc8CXkW9tV4kvAvgZj9gHG7GMSIE-KmtpUGuCvPd2uoqluy1f8sAPgymgb4NDL_4LWtFV_qVH4l501Mhb9bvY0qIN4dkVxPSquKHM3qku7eYPoSqF9b31BBogkDGizQZ-XhAYlmHlFsl10UNM26xzuFciMWzXFReaA7BRhZC2iLmDe1vXpGMqSKMFASmYA-LBvfpbAL5DuMX0ompKf3x1aFuhvqT4J-rTe7bxDb0i_5lUs6pDba9iALV1gLseNc66K_aAjdw_pzx5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42de6680af.mp4?token=nSL1_5qHfEd7du9wG5O-n-ACjGrhfGkiyqv1kJEyTDqg0DVRUYz1DHMwktcUx4WoJ1PrTphyfc8CXkW9tV4kvAvgZj9gHG7GMSIE-KmtpUGuCvPd2uoqluy1f8sAPgymgb4NDL_4LWtFV_qVH4l501Mhb9bvY0qIN4dkVxPSquKHM3qku7eYPoSqF9b31BBogkDGizQZ-XhAYlmHlFsl10UNM26xzuFciMWzXFReaA7BRhZC2iLmDe1vXpGMqSKMFASmYA-LBvfpbAL5DuMX0ompKf3x1aFuhvqT4J-rTe7bxDb0i_5lUs6pDba9iALV1gLseNc66K_aAjdw_pzx5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هایلایتی‌از دیدارامشب‌ایران
🆚
روسیه؛
فاجعه کامل؛ بی‌برنامه بی‌تاکتیک! گلزنی‌هم فراموش کردیم؛ خوب شد نیازمند آمد! دو باخت، پایانی اسفناک برای فیفادی سپتامبر؛ جور کردن رقیبی درجه چند برای آشتی با برد، از نان شب واجب‌تر برای فدراسیون!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30698" target="_blank">📅 23:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30697">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kI5jDVDzfu1Jl9Q5r_xlyjrX7qUh6LHZPvWe7vFfgvl_OiK1TYFiD-x914xC0fnpsib76oJ27hS6yTmJzas6yZocsKuNJv3Ue8SRRxAhrEDnTHTbWyDT2CO3RuUaevACyhyF7T4moGUxNyIf-50AqL3axoGrFCW2q6-iAzcG1RSmYSsYl9CX3ZZbZcKhMRZLTLalA_OA6ePTQES8ouEt5rMJ5jVNaThlAsOoR0guvHn3fU984GG5iCEQrVjB7w7-bcZDY6eyqsmnk_GpruQpSOBlfEVXOphAzQjuy84wR5jA14Q_B1tkSnpaRdBSXDVvheaTT5hOamCzkr9VsGkqXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توپ طلای امسال یه‌وضعیتیه‌که از بین گزینه‌ها هرکی بگیره هم حقشه هم حقش نیست یه جورایی. کی میبره بالاخره این جایزه رو امسال؟ سایت های شرط بندی میگن شانس یامال از کین بیشتر شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30697" target="_blank">📅 22:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30696">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUMkO57oxP1TSzCvAajRsUE5MConAkYP6LeoNOWTbijXiOdunArpcIg_aPMx1nQtAapB-BDH_wpGLml-3QAReW1gcVOnV1K3D9HvWS6k615HMibVewo9cIXswq-n92MKUW5BjTqHdGRjdD1Jkniooli0V5BAJtDw_xvzHmBVmzzDf0TdX5cXEemmbh15Au9W0K3s_8eR_0WnGa6qkjlWVWQbVCKUVV-sXlUOkhtLGESCKDLA6sW3lm-7X7FfTRLgvRYxPC5KlnTbfMDolWQqpVI8b8H-XYzNjeuFwK_lRF5w6XA4uHM8aQXhaWafJ6YHMCFmfGruogk3hJp7jUnDwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌دوم‌فیفادی؛ شاگردان امیر قلعه نویی در دومین بازی تدارکاتی خود 2 بر 0 به روسیه باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/30696" target="_blank">📅 22:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30695">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TT_8dHKbeVNRg5L1KjisL0LgLAGXNQxH2wLqu_fhfi1OXAbefazrSL5McgmEDHhmMSq10tavAhat3oVdKA9510T-Ffo7z6uC2FUsnpvIlK4hY496GXSrfizYDG31mi9jbuU6Xr4ezqVQxlZjp-XMqWpgFqV8FidZaOi8NcBA-KhYhqtHFccWNPC8En8NWubxqhBGTQvWpCoXTBIDadwxsGgSoItch3N2Bzhcyj1IWY4ga6hQsAoNne7JA4jnOv-EmoCRBe6yHR_F9eOV5E_EGb9dvvnZ_A-kGz3ueWmmOohhFXWd8OQcra14GhVnU5VFjI4_jfRMWZMOvR7SOdCmCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهره ناراحت قلعه‌نویی روی نیمکت تیم ملی؛ حقارت سرمربی‌تیم‌ملی فقط اونجایی که از یکی مثل سعید الهویی که هیچ‌کارنامه و سابقه‌ای نداره مشاوره میگیره. یه استعفا بده هم خودت راحت کن هم ما رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/30695" target="_blank">📅 21:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30694">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/329904c210.mp4?token=EWUYrzkuf_Eui0bdoAdaARzAgCC4JmEIXPIAB3VNwn1LLoa_wTbdrWLwzC_KCHdXnY2tYriZ4qLI_hSLN1x0K1LrFjM_BoEUS5m_XLE1J-a0S2sldEefAH4C5uPCJdsvgv7KCWcpmh7WtsmkVZ4TtWivGkYoGVgGSjJZtctvkokejCCKGhQISYz12-t9OGUdVJ5sdFWtFKmBc4xLa6rs7_T0yqgp9CDjBY6KD1BfYt_kjInAW1IZZQH3kPYT-ovyRE8vkUEG9nuf8wTcVLaATjkLXUJBya72746PgE5HNmGDRn3HuOIX9PBI17hiKO9wD29o79SjVEjPSqj7Pu_7lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/329904c210.mp4?token=EWUYrzkuf_Eui0bdoAdaARzAgCC4JmEIXPIAB3VNwn1LLoa_wTbdrWLwzC_KCHdXnY2tYriZ4qLI_hSLN1x0K1LrFjM_BoEUS5m_XLE1J-a0S2sldEefAH4C5uPCJdsvgv7KCWcpmh7WtsmkVZ4TtWivGkYoGVgGSjJZtctvkokejCCKGhQISYz12-t9OGUdVJ5sdFWtFKmBc4xLa6rs7_T0yqgp9CDjBY6KD1BfYt_kjInAW1IZZQH3kPYT-ovyRE8vkUEG9nuf8wTcVLaATjkLXUJBya72746PgE5HNmGDRn3HuOIX9PBI17hiKO9wD29o79SjVEjPSqj7Pu_7lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمار نیمه‌اول دیدار دوستانه ایران
🆚
روسیه همراه با نمرات بازیکنان تیم ملی در این مسابقه.
‼️
سیدحسین حسینی با نمره 5.3 ضعیف ترین بازیکن نیمه اول این دیدار دوستانه لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/30694" target="_blank">📅 21:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30693">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDPyNKz-UamNEzc28SKYBHzB37yn6Xnqj6v9CAkpNEaF1B-MOlmIX1r8v_yZ5oyRkV-mCrOs6fVeWTkabR5PZr1z492JLkewtyBcokI100RBYjA9ZossyhOrNufV2E_DHMH_g4mnN5F_OaZXaHt4W5qFVab5bzmdfLcScDli4Ijn4VXLWPYLHVGMqjWrC08mFB0562aInb9_f3QuvBTKT3JFgMcZqXLr3P1SlHCJtpHpdFnZcrOUmAHoa81ciB8wShsZxkgXH2FR4-LAPAXJu8ANEHAxPrjN9EHACa3n0eR2ry8TFhYhKQhFgPdM9cL1iGdUJTH83krPeD3YN-yEkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
احسان حاج صفی کاپیتان‌فعلی‌تیم ملی تنها دوبازی برای شکست رکورد بیشترین تعداد بازی در تیم ملی که دست جواد نکونامه فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30693" target="_blank">📅 20:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30692">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUzGqTtHVSyrg6stnhcCp6rBVovh1agVpWlckFY7Y0H4Y-odizeKPluac4MkDFMrRRsPsVJtBU5UVDun7lHjo2_Xq9buSSvH6-IL9hlzMpaLrgG-dUCx18BWVjZ3IaZHUoV0sZ-4h9uK3Fx7ZAaFdtlCXey8pqcWjX51ineY63Ova7vHOxyT9l1RzNz1c3Wxv0Am0-_yeQrhGYU64ES64mP1yya4QGyyEFgH4zNR7Epqjo07XNgLFF9ACJW3qWqEAZjrWcoj-i_8gssngrT2cdPLDIYleWlOctaOQSCKAr3C-5EP105ncu6TkwoVuGC1KPxDLUXXbvfE84dL2_s5BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت مصدومان پر تعداد باشگاه رئال مادرید درفصل‌جدید؛ فده والورده و ابراهیم کوناته به جمع مصدومان پرشمار کهکشانی‌ها اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30692" target="_blank">📅 20:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30691">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b7679a9f.mp4?token=tG-Avl8O8W4-uYe7omKSezWIlV_sgRY3Y-qwhdzrqhS6xzdYZJ-mr1rprFCu33x7fnSeGSE5R88lqFhTcpK64OYsWjkQFVFmNQhQSV_nHQscvT-BB4tdU3jE6wVEu902D6eRrdNTLEGX6WNyrF7E7vJverjN9sWKRW6JIrvClVZb3b3GYxGNJcYz_J7FUNkkyujLSQkj7fqkJDOC4sgnYP2odfQxWleOKMHHqbyFr2jtsleYTxs4bqEZh3sfrQKRQnM_7pvkCwq0Z3NhAclF-3NfduUvJQIqUNyHnxOV8TxT5DmP71JN2DQ4GFle6ry_dv-qNUaezEe2Et7bs2KMew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b7679a9f.mp4?token=tG-Avl8O8W4-uYe7omKSezWIlV_sgRY3Y-qwhdzrqhS6xzdYZJ-mr1rprFCu33x7fnSeGSE5R88lqFhTcpK64OYsWjkQFVFmNQhQSV_nHQscvT-BB4tdU3jE6wVEu902D6eRrdNTLEGX6WNyrF7E7vJverjN9sWKRW6JIrvClVZb3b3GYxGNJcYz_J7FUNkkyujLSQkj7fqkJDOC4sgnYP2odfQxWleOKMHHqbyFr2jtsleYTxs4bqEZh3sfrQKRQnM_7pvkCwq0Z3NhAclF-3NfduUvJQIqUNyHnxOV8TxT5DmP71JN2DQ4GFle6ry_dv-qNUaezEe2Et7bs2KMew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله ژوله به قیاسی و قلعه‌نویی؛
وسط برنامه زنگ زد به قیاسی و ماجرای مهدی قائدی رو پرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30691" target="_blank">📅 20:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30688">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pxFyAtrrN1drh8-xf_Tc8F_9jgI0xWuDzG8KvWmBX5wiDdqK9HrdmKcrzktNCGrKqv4ZKRmQwMbBKrpwX_nssDkQVP0PZkjzrBd2oqTUTpHzaaqzSKWkcleI84IDo4IV7Z-TKj8_kosMCFohepvoZBVcpviuQ5bv_pWJuY6kC8LJ1h6NaF8ALWyQ_3npaNXROF-nFLxuu_zjYzSc47wQ1UGo5QteWNHUWC9iGRBdviOvEYnB2FZA6I5srYlUBw_32SgIYYMOCJbWmpJPTsPFikqnpx3YNwLhC2eyrhUoEhtR8Z_kCsg361KJmXcXxKFdxE--IfEb3ZwxoBi97VKs7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dbcnk-TorFgJzYI4n8xPrxDt5j_Jgi-fge3Bw12AdfbUcXVVEnlVZq4xZ1aj_OnaO_rmvljsTU68wjY5d1A3z6PpDRSSMs5FfyCXqyPYZY5-jJfqqaRqg192mTIF-4_aoXqI_6GXCiTmCqESrkKKnjQYWC7KomY0cSOYPbLJ8_BZ40BycU0TwaszR8wuuB71OC74ksci5g_qDJhOaCNGhuj7TlKTlpPjC8OhzynMQeIP_paWnPT7emnQDOwqWUXXXEZugAnJuGkIg926lZUSau7f6Z55cb7h4gEI7AoV05Wn_Il0yR_dL5aQ289BtkGY6HMDrpwhTD-UPwzu-KWwDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دومی رو به این شکل سوپرگل خوردند؛ گل دوم روسیه‌به‌ایران‌توسط الکساندر گوگووین در دقیقه 36
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30688" target="_blank">📅 20:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30687">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba8d2eb7b.mp4?token=LcKVpJlJaQ1OPg7Ct0VW5W_h31xpdKTrLfzHSYJEW1qRAOyOBszLwyve5BFb5qsIqdwsptdjuKhtj7513hlwJhLNpBH0JmVObJbFPne7S_OgQDOzgbsE_h1m8XqPcEgLoUIxphVf8b9-mzMT41BdyDN66l6mrsb7W7Ge1kFz3VKwN2jsUFU2A75MbPY2oEbuPrlxfSUJYiXQ5wsceK5ZnNJToZ1wd65uc1Ikv9G9aoO6l-03NUfYjtqTIPxV4raJIoRBjLm1Zan-5UqPRdI5bvuJ0C8dacWlUgj8_KoX1FnEoeHMXB41KRAmwNkLckDENiWLe6ESMgLD3p6hWR3aCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba8d2eb7b.mp4?token=LcKVpJlJaQ1OPg7Ct0VW5W_h31xpdKTrLfzHSYJEW1qRAOyOBszLwyve5BFb5qsIqdwsptdjuKhtj7513hlwJhLNpBH0JmVObJbFPne7S_OgQDOzgbsE_h1m8XqPcEgLoUIxphVf8b9-mzMT41BdyDN66l6mrsb7W7Ge1kFz3VKwN2jsUFU2A75MbPY2oEbuPrlxfSUJYiXQ5wsceK5ZnNJToZ1wd65uc1Ikv9G9aoO6l-03NUfYjtqTIPxV4raJIoRBjLm1Zan-5UqPRdI5bvuJ0C8dacWlUgj8_KoX1FnEoeHMXB41KRAmwNkLckDENiWLe6ESMgLD3p6hWR3aCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولی رو تیم قلعه نویی خورد؛ گل اول روسیه به ایران توسط الکساندر گولووین در دقیقه 21
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30687" target="_blank">📅 20:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30686">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2afda25603.mp4?token=PtTl6i2N2S8WRz6mz9AJApfKumng8GZgXEcG6LvR6_J7KTQc-ZtkOrbxd1rGHwk_wlKsvQ-btFGmbXSIRVjzKIhISvTr8I775vkDfl9wrLlxoJtegnqezB7QQ0fq8Nlh9JbK8n8qWgJHzWDCIlCj66c1x3EYgrzqAR4spL7Gw1fl83s2EnNcwFs9supNoeKwyUJQFYwAkiBVHeB79ykOG0IkmGe7B62t4tjAwhTBCEPLqjoHmQ8OZRBKRdAfmOOCOqctqC7e6WdhcAjo284in6PRbXNMvOF1Mc6JBNdLSlrxHO9XLSVu1qVN45USdOzMoBMfDf2HlKUU3LE_UaCh1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2afda25603.mp4?token=PtTl6i2N2S8WRz6mz9AJApfKumng8GZgXEcG6LvR6_J7KTQc-ZtkOrbxd1rGHwk_wlKsvQ-btFGmbXSIRVjzKIhISvTr8I775vkDfl9wrLlxoJtegnqezB7QQ0fq8Nlh9JbK8n8qWgJHzWDCIlCj66c1x3EYgrzqAR4spL7Gw1fl83s2EnNcwFs9supNoeKwyUJQFYwAkiBVHeB79ykOG0IkmGe7B62t4tjAwhTBCEPLqjoHmQ8OZRBKRdAfmOOCOqctqC7e6WdhcAjo284in6PRbXNMvOF1Mc6JBNdLSlrxHO9XLSVu1qVN45USdOzMoBMfDf2HlKUU3LE_UaCh1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باورش‌سخته ولی شماتیک ترکیبی که قلعه نویی جلو روسیه چیده براساس‌پست اصلی بازیکنان اینه‌‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30686" target="_blank">📅 20:10 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
