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
<img src="https://cdn4.telesco.pe/file/Mc9KBt3uUFjBj7OblSlHJSBVtcsquzDO8NIehmIP4XNSfYSW74sB4OQQ9vFFm7d39C1oaeixtLiUBpH7mxBNk704wbzbZNje2ajnO_xekYLdCA2G2qwcb2pgw8gQ9NNkeD1tQwE-9CZLnHzu18qeogCzc8C9TyFbMrbxsBBR83RtrJtDxDCxZwtgPkTVJR-PUB05B3Yh26FlwqVMMMqfOuzESJ_cfmJVqQDJbxZ4gtYbpkOjPCI-Zpz2PJvigT9mXPLO8VtJm_Dv6xy2oWP7e36OJ_Mg1UN5WFE0PX0TosUYLqRQLeiHJ_d5H1MM_RAVpsysoM1wvh0g7phFiegx7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 205K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 14:06:16</div>
<hr>

<div class="tg-post" id="msg-67328">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=kdzTbY9D2BdJPZObPGwo_Zl6To6pCxvAx0M2QizX7SPFDO0qBB2-lMirO6kUScLDnmzD-Jn4BfAdGBNeUkSByp8ebSSjiitFxS1COfVRapepxwZzP8aW01Xdb5wt58KmdXrUdnV1TQrEj1bhOuwpzZcTwoL0LlZ-7fgFDKmG3sv78Lsid-xyXM9nrsgrghyeKPDGZqPfAk43ufKzTgqgETkSFCku0OGm7g5OJHKULsllXz1bHyTYNC29_ra6e9nVDRvLMHzKGsLcgXLFOy4E42Ljt8bbX1OsHYXxvcUsPtF73GLU4s7v_fwO2gtIzo4Oxki1A4G2JfbfAD5xvaxk3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=kdzTbY9D2BdJPZObPGwo_Zl6To6pCxvAx0M2QizX7SPFDO0qBB2-lMirO6kUScLDnmzD-Jn4BfAdGBNeUkSByp8ebSSjiitFxS1COfVRapepxwZzP8aW01Xdb5wt58KmdXrUdnV1TQrEj1bhOuwpzZcTwoL0LlZ-7fgFDKmG3sv78Lsid-xyXM9nrsgrghyeKPDGZqPfAk43ufKzTgqgETkSFCku0OGm7g5OJHKULsllXz1bHyTYNC29_ra6e9nVDRvLMHzKGsLcgXLFOy4E42Ljt8bbX1OsHYXxvcUsPtF73GLU4s7v_fwO2gtIzo4Oxki1A4G2JfbfAD5xvaxk3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این بزرگوار که قبلا گفته بود بخاطر یه تیکه نون به سگ دادم اومده داره ترامپو تهدید میکنه میگه بیا کوت عبدالله ببین چیکارت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/news_hut/67328" target="_blank">📅 13:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67327">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/news_hut/67327" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67326">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=rfcz84OVHs4SoZYKu8flPj6t0Q9tPJgn87Zyw_wH7xohP_IlK197XECIZtZ_5pqxSZ_FinwkWGV-RsOev_PlA_CMxm1OuIfrvnKsbwhpD6NGDt5Nxx7cFn5GqkWufksL9sJ4LU8_dcb1nnMrf0TB9uQXdxNoTREpo3_ECc7vT_BUAC6j6saacrdyNlW3Zw2NykVEB7dqCX3LTKS_v8cTYyhtppM5ufJDYqz8MK2bg2kRiHRrrwa8vhr8DZUbSuadoPLGnkcyoWz4-_691XYkq0TqMwCIzYAPpkKVmOKuTkIm_r37-D-4t7BJlPVcUq2khZ0jHA3-noFqRm2aYAmjag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=rfcz84OVHs4SoZYKu8flPj6t0Q9tPJgn87Zyw_wH7xohP_IlK197XECIZtZ_5pqxSZ_FinwkWGV-RsOev_PlA_CMxm1OuIfrvnKsbwhpD6NGDt5Nxx7cFn5GqkWufksL9sJ4LU8_dcb1nnMrf0TB9uQXdxNoTREpo3_ECc7vT_BUAC6j6saacrdyNlW3Zw2NykVEB7dqCX3LTKS_v8cTYyhtppM5ufJDYqz8MK2bg2kRiHRrrwa8vhr8DZUbSuadoPLGnkcyoWz4-_691XYkq0TqMwCIzYAPpkKVmOKuTkIm_r37-D-4t7BJlPVcUq2khZ0jHA3-noFqRm2aYAmjag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جمهوری اسلامی پس از ۴۷ سال در مهم‌ترین رژه‌ی خود حتی به‌اندازه‌ی بند پوتین‌های ارتش شاهنشاهی هم نظم نداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/67326" target="_blank">📅 12:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67325">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ac4BNJdKFqVIJe_cfPKqTKvb_EVAOEg66WXMcbywQo9D5t05-Mmx_p2g-ODN1agpc9qk3-E7xBq7rMkF9dFerR13KLGullf06zN2_iJD35ANN7mQQvMbxK8iXpu2eG952_SipvwMhUIyWfr_6AWX0TvMfxieCU6qz8TXf_FFa24tIuzt7atsz87ois5SZ9RCQNaLJFOorJPD58A6w9RD5aBMWosRENSXpT3B-jrPFtwA7tusnklUEG2EEUl9byazNkeIxfyv8_jxx_FcW7kRnzoSiML_T4XA3v-MUQVRCBAqa0VkZHUaWqJwy7Et5anU43ECpU2ykIjWKCb4j7ngTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هرمزلتر:
🔴
نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده
🔴
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/67325" target="_blank">📅 12:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67323">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaB0osKUzDmp6z3ij2h6F5IuJc_2UnA_E4GzGrpS17rA478rtwXPUFHwDSAXWxaliA5OoE0KWo3ob2b4wtndC1O8w6KgBVcOVb9FQI7V1LCAu6WD0bX1J_6h5v4YOyVLHc254w9_r3XQJOOIirdcW81ZkELLtNd-KG4UbbhY0Fqnbu78oov8ZcDTUckpx1yZn-i6CTWBVEtnqh3DVS5bZwGrx94r-3G7ln9ok4Vl0t6H0z9CQmjs_yHNBGoLSsUnfXOx37FraI4V1LYG4aGlWwgu3eLPyOS4s1FeP5roMc4okXDGfrnsLe2BWB2WJFL0Ilfjq1MaEyd1cYYmS7GB0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=PnlSlFQR-48f5XCqZvlHzS3KnmZ60LBSAFYh96fq5xkDKbDNoNLTY3SNw6zq8um0ThL8IUcDJ6I0XUHPqBbhhGCL8X5tqgxEk3_fVIft59owZYph7y77zY-qvAlhnhoBBTbVHYCbnz9zH5fSIQNqjXZtGtJOMcQR_ohTW-IYvcqGzKcSuYAeTgUrbExhgHuw5l2OIK5EgcJmq9rAii-RikJbOlWDUjd4O2dcVj9EyhPmlVDLATQg_JRGYKmNqz-WBXBQRbhx1Du2ffik7Lox5WcjgI1r2oJx8OrehCX-8nT9ZMk6ch_9o-7jvT2BuGmjWuB2mctN2WglTX1hJiGQHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=PnlSlFQR-48f5XCqZvlHzS3KnmZ60LBSAFYh96fq5xkDKbDNoNLTY3SNw6zq8um0ThL8IUcDJ6I0XUHPqBbhhGCL8X5tqgxEk3_fVIft59owZYph7y77zY-qvAlhnhoBBTbVHYCbnz9zH5fSIQNqjXZtGtJOMcQR_ohTW-IYvcqGzKcSuYAeTgUrbExhgHuw5l2OIK5EgcJmq9rAii-RikJbOlWDUjd4O2dcVj9EyhPmlVDLATQg_JRGYKmNqz-WBXBQRbhx1Du2ffik7Lox5WcjgI1r2oJx8OrehCX-8nT9ZMk6ch_9o-7jvT2BuGmjWuB2mctN2WglTX1hJiGQHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بعد از چهار ماه همچنان عامل این جنایت و قاتل فرزندان ایران چال نشده و اجازه چال کردنش رو از قاتلش گرفتن!
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/67323" target="_blank">📅 11:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67322">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=LjpxoXQpGdrLbuPc76Q-bVVz3NX4mh04wj6NDO33-UF_gvL_A6OXxJKuhOLt4E_UfbjCtg3WdSIeMywzIzG12jBc0f-ff9GlkXYCf4zS6fWbuXK6QI-3nqIwYSA-cU3AlygIs6tKFlIkktSnPpA-k-kSxCzBYwJ7Z5TwVROGwwzE8ojqM6mSlnSYnpKQtRJBI3u_2Fuf5UnLKfwcZNGClehxN7U8Jf3FBwcKt2XVZuMNUPddEunTLX4ncN92K0ZJOBhZpA3ysJ_wlsIzB9MzAlBNc2vgG-oguNGlDImk4OVyWgAyicK8l1CXc9RmDL_zJgEjPlJFWW7Lgfzo83eGAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=LjpxoXQpGdrLbuPc76Q-bVVz3NX4mh04wj6NDO33-UF_gvL_A6OXxJKuhOLt4E_UfbjCtg3WdSIeMywzIzG12jBc0f-ff9GlkXYCf4zS6fWbuXK6QI-3nqIwYSA-cU3AlygIs6tKFlIkktSnPpA-k-kSxCzBYwJ7Z5TwVROGwwzE8ojqM6mSlnSYnpKQtRJBI3u_2Fuf5UnLKfwcZNGClehxN7U8Jf3FBwcKt2XVZuMNUPddEunTLX4ncN92K0ZJOBhZpA3ysJ_wlsIzB9MzAlBNc2vgG-oguNGlDImk4OVyWgAyicK8l1CXc9RmDL_zJgEjPlJFWW7Lgfzo83eGAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی رسولی  مداح بیت رهبری میگه برای خون‌خواهی اومدیم؛
شما هنوز خونخواهی سلیمانی و... رو نگرفتید بعد میخواید اینو بگیرید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/67322" target="_blank">📅 11:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67321">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=qzjfrR74N8kUHThDdwDs3mutU0HLll60A-iRTQpeoNtEQFopPnYWr7DoEXtyJbgu-mN2xvsG0__G4_7zTHHOUqQ-6xMgg3KQ7__LZ85o3qJnh4zF5hdNx0VZGF1XPgmkCrgifT7F0btsN4JYRJad3N8F36aY8g6xvSBelKvOscRLaQKTTr_W4qhyulMhAR8bnpb6bmtyQjK0s_mXGPbcpM7ee_97nf2JqU_TXuJTw9HW_f_SdxUt0wmMInAu3SRGWpnGkrtw2pDrX6xSsvza_3Wmp4_I_t_TLdCbRTeO_wCarWy8i6sVfPssqhPpj0Dwgve4D2Qi8jdwSdnD86n4wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=qzjfrR74N8kUHThDdwDs3mutU0HLll60A-iRTQpeoNtEQFopPnYWr7DoEXtyJbgu-mN2xvsG0__G4_7zTHHOUqQ-6xMgg3KQ7__LZ85o3qJnh4zF5hdNx0VZGF1XPgmkCrgifT7F0btsN4JYRJad3N8F36aY8g6xvSBelKvOscRLaQKTTr_W4qhyulMhAR8bnpb6bmtyQjK0s_mXGPbcpM7ee_97nf2JqU_TXuJTw9HW_f_SdxUt0wmMInAu3SRGWpnGkrtw2pDrX6xSsvza_3Wmp4_I_t_TLdCbRTeO_wCarWy8i6sVfPssqhPpj0Dwgve4D2Qi8jdwSdnD86n4wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف یه 20-30 سالی هست درحال گریه کردنه
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/67321" target="_blank">📅 10:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67320">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=l386xyC_fozaBtfIp6X07mxH80rnFVF545fmzsICpGJEmhAbH81XloOi-mVg5VTZWlyO6ONIjqkyWul_awtaSQTdEwKeuFSQyiYlpdPsX9vt5TIVExlbcaOjoq8ptPlUTyGOElhwSFBL5DCONWf_JcNQph1O1WgHrH2fhugGt8vNUifrNFwREhA-LClySY3Cxqx_miQZb2ZtVKD9bHgs-HJbH7i8FgT-LxkAWPExcoO0RsM9uCbvReMe21kZ40nZelWq_yP7hFI-9PtK08wHBk9f4UcLaiSvPysgMDC2Vnmde8cAJbRDO6Y4qQvYg6dAaxHEi1xvt7yK2V0XMgdh4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=l386xyC_fozaBtfIp6X07mxH80rnFVF545fmzsICpGJEmhAbH81XloOi-mVg5VTZWlyO6ONIjqkyWul_awtaSQTdEwKeuFSQyiYlpdPsX9vt5TIVExlbcaOjoq8ptPlUTyGOElhwSFBL5DCONWf_JcNQph1O1WgHrH2fhugGt8vNUifrNFwREhA-LClySY3Cxqx_miQZb2ZtVKD9bHgs-HJbH7i8FgT-LxkAWPExcoO0RsM9uCbvReMe21kZ40nZelWq_yP7hFI-9PtK08wHBk9f4UcLaiSvPysgMDC2Vnmde8cAJbRDO6Y4qQvYg6dAaxHEi1xvt7yK2V0XMgdh4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان مراسم افتتاحیه مسابقات «فولسوم پرو رودئو» در ایالت کالیفرنیای آمریکا، یک چترباز پس از آنکه پرچم همراهش به درختی گیر کرد، تعادل خود را از دست داد و به شکل خطرناکی روی یک چادر سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/67320" target="_blank">📅 10:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67319">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=ZU8HtOswhTN1IPsrpVpH3ea0Pf41sm85uoSJacmJApIPN47h2iJwqXjEOImor0MDbvOmxFrTlrl73wcGFND0lm9AU9EWRDahrFXKuppV0jmpZKDjZs1f_6Ch5WZcJLXgvdfhy0e0QcjHpCbr3Yt3IJS6q8V9K3bfV9KYSNWGJMrp2x2UvqEMYQUELr7wL_Fz8pO6F2CLsNkFafmK3losLGDCNZpMe3JkPuRotFnXAefciPq2d4pcI9e-jBmY18P4HNxUHBDNuQ7-0WTCSjm_uJOvC37lupp26aMvettLfDW87TBryUAHCazuVXgeZX_0OJHnLF-3ZZDe2wjSCelMqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=ZU8HtOswhTN1IPsrpVpH3ea0Pf41sm85uoSJacmJApIPN47h2iJwqXjEOImor0MDbvOmxFrTlrl73wcGFND0lm9AU9EWRDahrFXKuppV0jmpZKDjZs1f_6Ch5WZcJLXgvdfhy0e0QcjHpCbr3Yt3IJS6q8V9K3bfV9KYSNWGJMrp2x2UvqEMYQUELr7wL_Fz8pO6F2CLsNkFafmK3losLGDCNZpMe3JkPuRotFnXAefciPq2d4pcI9e-jBmY18P4HNxUHBDNuQ7-0WTCSjm_uJOvC37lupp26aMvettLfDW87TBryUAHCazuVXgeZX_0OJHnLF-3ZZDe2wjSCelMqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین حضور عمومی مصطفی، میثم و مسعود، سه پسر علی خامنه‌ای، در مراسم تشییع او در مصلای تهران.
مجتبی خامنه‌ای، جانشین علی خامنه‌ای، اما همچنان در انظار عمومی ظاهر نشده و در این مراسم غایب بود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/67319" target="_blank">📅 09:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67318">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=hN1Hqon8DbV9eofxzEtAiPV6Cs3agA8dNv6IMRuNRZDf_nSru7jm8R4_FlY24n0jA6p1Gu5vc5G6cXCwwnTt6C06YiCO6uJRnbyjRJiKizIsH2NA-0cuXt17b06GVrCi1_r0gxrbjeKhXRexiFyBVepHfVlWwnzO0PBx0wH5itr3XsgUqkXlqSZe1mrC6mSqIFSHsnn0cim6ZYOP_oQBlzL6_qgg-0BiJIjEk8tmN1rmkMjTeDn7oNXduWq85SPz9AHOBBbF6HX_dP7QIDufl4xUJorhGJABE83cuKJBuLvajELwAfnNR6qps6Tfs2KOICUO9m6Gnxmet7D_KTgPwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=hN1Hqon8DbV9eofxzEtAiPV6Cs3agA8dNv6IMRuNRZDf_nSru7jm8R4_FlY24n0jA6p1Gu5vc5G6cXCwwnTt6C06YiCO6uJRnbyjRJiKizIsH2NA-0cuXt17b06GVrCi1_r0gxrbjeKhXRexiFyBVepHfVlWwnzO0PBx0wH5itr3XsgUqkXlqSZe1mrC6mSqIFSHsnn0cim6ZYOP_oQBlzL6_qgg-0BiJIjEk8tmN1rmkMjTeDn7oNXduWq85SPz9AHOBBbF6HX_dP7QIDufl4xUJorhGJABE83cuKJBuLvajELwAfnNR6qps6Tfs2KOICUO9m6Gnxmet7D_KTgPwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زاکانی و برخی از مسئولین تو حاشیه مراسم رفتن چلوکباب خوردن، عرزشیا هم اون بیرون زیر آفتاب، صف وایسادن تا تخم مرغ آب پز بخورن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67318" target="_blank">📅 09:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67317">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7YME2u8bvE2FWFGwBcNjvVV1IfKPlNMALyxhHszxjDBU43HSMuYYyGBPXPbw-MQ1iIEiXiupFn97biaks6DVFAGTJa_IGgZsMmwoM0imeLiJVHyAKmGacSTnq0H_FbXTN6J5py9hh9ZOyXYQDKVwBKYww2DWNgLHL3JJ_5Hz33d7jtMO_kFaSQsQulwoXxq10bLkSBymeI9Gckl9JtYfCQ6lpDJ4FYwuQNzb017HGarwQnf5DUEaYbqqks9CqCcX8oAehppeTJFRjDQ3ofP56bpkpARrb0gzghXSJSagRNo94jCkn2M-_yG9k8LrPTOecQX2mq7RNwt33ik7Pbg8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
8فروند جنگنده A-10 Warthog در پایگاه هوایی موفق سلطی اردن مستقر شده‌اند.
🔴
این جنگنده ها برای پشتیبانی عملیات زمینی استفاده میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67317" target="_blank">📅 09:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67316">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67316" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67315">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DkXKubrHFJaReOe9Kh1khvnPHZkhuZ6czj7YQ2DyEhdNxh0_GHmNhyEQxZxWkqaPKPoXqXqLmG9cMN7Q7liycma7w1nTsj5nK0IV60pzSE7lvhvSI8oglP1farUeV0vN2rIEgmFNGFZE5RSZWg3FG_J58989gTf3RS6hNpvTojT-_FnaZ-r8OelQmXgNsvMUsyvoehjN9Ua-9UUWLgvyWn_OLprjBzQklpFoJFHWALvPMXf1m5pdupSAjjPq5ZdiqXDTpTWEVC57_vnealmB_onS_ZY2NBFmrKofKM1D7GWZZSbdX4oUi2LTN95dmm946JokUrFj_um9uyjdaU17cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67315" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67314">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cye3988uUL2dfVzqRza6D6X0oHn478y3vtwdpo-sVpEqnKcOjhSWUS5e02yjLZ8ve9He-hfOrWe9gct_Tk-aX7_Z-hTUD9zVDJOJnviPA8Mw30cTIkUEGA8wxOQTZdhuKtHUxgDOuKwsq_VkeSPVi1daK_LT1-29nz_DKL34go3O8pgg0MAcMXPYz4QWFx0XsBuCsrNUGBKJJ3-fUc3nA7ef2HiwZSWJ-OQrHsxnyk08BlPff2UXMdrvOXC4ngzE74_179hY8e0ZJxTtyDTONxJw-4VBQzqKR3HnnTimlQGJhQY5RMLQ4NE9bZQgZpFUIQVwJ9cdE4QEAJ797aI47g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
ولادیمیر پوتین، رئیس‌جمهور روسیه، با دونالد ترامپ تماس گرفت و دویست و پنجاهمین سالگرد استقلال ایالات متحده را به او تبریک گفت. کرملین اعلام کرد که این گفتگو یک ساعت و نیم به طول انجامید. پوتین از ترامپ برای سفر به روسیه دعوت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67314" target="_blank">📅 02:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67313">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=OqE4wxyC_nI-_a_PxU6GULNmA8wiRz3NAaAj31iylIW7WYnmeKZmva7UuO9CHxvmTSe5TiVmmLhXCQ9h00FtSdGf5CmnXuwdMqFjXr38qsukHTCK2HfpXaAj8pG1X6tuRHwqIyaJWAI7Qc7MVUto_NJOFxya4QFZC6Dj3SRQD4YKkAZlYuHioJ3Ns5VJesX2gnIEY_Q_aV5s-sE2rlxeTfG10I5s4C5mlrO8h9X61BePuLMCq54BG7n8ZNpaOBORSMJ9wqLsdvoBIC_o4Ep2BS7HmwNjoPlK_DNLIxYuHHTSsK4VqSwWKM5LEUHGOVVvyLX98XwWqQ6vnR07xYnkUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=OqE4wxyC_nI-_a_PxU6GULNmA8wiRz3NAaAj31iylIW7WYnmeKZmva7UuO9CHxvmTSe5TiVmmLhXCQ9h00FtSdGf5CmnXuwdMqFjXr38qsukHTCK2HfpXaAj8pG1X6tuRHwqIyaJWAI7Qc7MVUto_NJOFxya4QFZC6Dj3SRQD4YKkAZlYuHioJ3Ns5VJesX2gnIEY_Q_aV5s-sE2rlxeTfG10I5s4C5mlrO8h9X61BePuLMCq54BG7n8ZNpaOBORSMJ9wqLsdvoBIC_o4Ep2BS7HmwNjoPlK_DNLIxYuHHTSsK4VqSwWKM5LEUHGOVVvyLX98XwWqQ6vnR07xYnkUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جمعیت هموطنانمون در تجمع چند ماه پیش تورنتو رو ببینید و با جمعیتی که در مراسم تشییع جنازه علی خامنه‌ای اومدن مقایسه کنید
🔴
فرقش میدونید چیه؟ ۸۰ درصد جمعیت در مراسم خامنه ای اصلا ایرانی نیستند. کلی لبنانی عراقی یمنی و فاطمیون افغانی گرسنه رو با پول و... آوردن بازهم نتونستن مصلی رو پر کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67313" target="_blank">📅 01:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67312">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSCRo-pWVyW-vF2zHNSD-pZ5LLY0SfPRkPGIdDoHzd_XLHAWCzcrD56iTxEXrmS6qLucDs5mAv6-1mljJFI-0lc_9dO3ieZKwcYdLjjFqcgyLgbTAR_VymOfBH17tvTLwuGCfAvapbqLwYOhtzwVoBRNg7SfjFQqTMPlX0UFZvF3FHMymBrrQgpQA1JSRO4vSj2clGL2tcol0gabywKlphZV8bLZkxOrvm1f8mUMeEPmTPU93lIrH70pf8V06rFCKT8okPSSDipoH3aenCANn1PmpISV3lVLAQvJKuV7lh5D9-UY69RCaC70MC90qt2PhaQChJrjyyzoaUZQlcn_Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیروهای ارتش اسرائیل در حال عملیات در منطقه حداتا در جنوب لبنان هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67312" target="_blank">📅 00:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67311">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=bZvjCMaFjaIVPgv2yw-AfE25sDwRLuB3Qi89heHHV-mQqw4VmFg5PUAoMfbHgsPmON4qldfniZ20bIwCbD-MpNX2nY3KGvx67-UulUB2ZrpF-W62A0OVFr9fCbuL2aTpFHoHl-M6I-okjzb9HEs-hrQ70H2jgLX6nPkPbVqWTEy4zSGXBZ0OcBFp-p6GMuUeiaWawz1fBkV3Kkv0-dUJjYay_itlBalYWTQzeNx7bXchbYM_tvWLh4x6-VQUbXxH5FdZN-Be0Qf9eUFbtk_ASkKrvK943nFesd0MsI8_AQ6XObkSbl55ay0I9F4AZgaKUpL2wtp-ktLpbsrgWhqixg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=bZvjCMaFjaIVPgv2yw-AfE25sDwRLuB3Qi89heHHV-mQqw4VmFg5PUAoMfbHgsPmON4qldfniZ20bIwCbD-MpNX2nY3KGvx67-UulUB2ZrpF-W62A0OVFr9fCbuL2aTpFHoHl-M6I-okjzb9HEs-hrQ70H2jgLX6nPkPbVqWTEy4zSGXBZ0OcBFp-p6GMuUeiaWawz1fBkV3Kkv0-dUJjYay_itlBalYWTQzeNx7bXchbYM_tvWLh4x6-VQUbXxH5FdZN-Be0Qf9eUFbtk_ASkKrvK943nFesd0MsI8_AQ6XObkSbl55ay0I9F4AZgaKUpL2wtp-ktLpbsrgWhqixg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه‌ای،‌ 3 بهمن 1403:
ده‌ها متوهم به درک واصل شده‌اند. من به شما عرض می‌کنم به فضل الهی این تجربه تکرار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67311" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67310">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67310" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67309">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eRdZ3C2LMcZykC5HWaHNP7aDcCXkyaWK0lcPz24UDW_xuhTRbwwIs6J9XzfQGYvfA328Vnpg1Iv6ZlICWYH9jiMaMhc6MeBP_vzjulLcl9RLTQLkToHEW8BvOM5fWlRZb-akWNn9U7t9FQr7nupK09XchGHrKtUFprJPKB8dj4cuGaO5RvEd07I6hFWJ2FP2Ost35lbUBTzdz1nVzOv6KQ1Ru-BQTk_UKIHQGnjr855yg2Jm1Zj1lk-tP1_qKWnpcCvwfqW0kXCo3FvHCVcuyBNwk8wjuXKCy0lTS43W0Du1u5MEd5a2AZznZkWoIYqj43_boJZmRTQ3f1ktErBNFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67309" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67308">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=OVciMYBgRxDV4ZRMbgPJjUaLS-NewrrXbHjoKl34U_qk7dZjLOSRwQnVpHy_3Pqwk2E8V3tQdvteGtTXIF3qXDPlEKh9sEhjWPhlfGtP1hoyZopiYimW4SQX6nOr9md_mMW8nmPibYny0DZ6qq1hE0jySg7RYW8VSVYpDNUAhv29f_8CPfPfFHiqPQ-mIIMjc3lKfzbMiafsw5Gxq0ugCa5sYK0AGFWXGgxP85NKEQbbw3sX4e6BTzF6eTa1LkzL7C6A1yUFArABgNg6ecqet8pw0hMACGX75NLScjR8Kv9AmZrZepeuleUxuyHbVT7qxTe0CPWs9Wuoa0PzjumgNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=OVciMYBgRxDV4ZRMbgPJjUaLS-NewrrXbHjoKl34U_qk7dZjLOSRwQnVpHy_3Pqwk2E8V3tQdvteGtTXIF3qXDPlEKh9sEhjWPhlfGtP1hoyZopiYimW4SQX6nOr9md_mMW8nmPibYny0DZ6qq1hE0jySg7RYW8VSVYpDNUAhv29f_8CPfPfFHiqPQ-mIIMjc3lKfzbMiafsw5Gxq0ugCa5sYK0AGFWXGgxP85NKEQbbw3sX4e6BTzF6eTa1LkzL7C6A1yUFArABgNg6ecqet8pw0hMACGX75NLScjR8Kv9AmZrZepeuleUxuyHbVT7qxTe0CPWs9Wuoa0PzjumgNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس‌هایی لو رفته از ابویسانی، معاون وزیر اموزش پرورش حین گفت‌وگو با دانش‌اموزان معترض ؛
دانش آموز:
نه اجازه میدین تشییع رهبرمون شرکت کنیم ، نه اجازه می‌دین پیاده‌روی اربعین شرکت کنیم، چه کار مهمی الان دارین؟
+ ابویسانی :
اربعین بخوره کمرتون!
دانش آموز:
ما می‌خوایم تشییع آقا رو شرکت کنیم.
ابویسانی:
برو بابا تشییع تشییع..
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67308" target="_blank">📅 00:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67306">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUgp3gUXf-7xI5PTHhARzhLiTKZX5FNvRh4SKM8mLsW_6g4cTgFhdu15KX9cDaj7j0Rx8_aTgbZ6Lbych-TMBOmCwusy8jtx4MZnm8JOEho1ysUh6ntewxR7XRi1n-ZZW8QPGxpCIHI7qMUUV1UGJFpEWM_WQYm462GLNcFZid4ww9xNBwEmjF3gdnOQaQ6222w32sQvl2AUpaYac6lbdOw-vd-SzxL8sgTnCBfcecMVZvwa8QNHEmUGnPA0qX11g4kM2vNnHLVyYZIIptys4vLSZ4oKotYogsiK8pBv6UWe8WXwCkiMwPXzrPfjM_RLhjF4rKTfhTNcoRh2RQ4Syw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=NH_m0iuoBroQiYX9G1HJ1tC24zwK7U11M4wb0J6-6hLSD1ODEH2OAdC2_dCvbiT9wZn0byB7hY8WRCpjzvZ3cIdQeazV-Se7wGE0Z-F3hlz3i5TU6h64UYIc-SAh1bERfrPBWIaPTX08ueibW6LRaax8-cM1UUb3idrNQ2akuwTeJ2cB_QxAKVWoI-OF70x82lDcUjRw2UeXo9Upcv2RBg6VyQirQAtSnq7XRJ1a6zo3FU7Pm_5tzZlg-DXcGd1t4EzXNtMWSB6AGSO41Fc7Krq5ukOLenUtIuYL67dl7sRPm8mfZrTdFqIY1pImDvJfzpmBJr6PPdIXVWNFJftEzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=NH_m0iuoBroQiYX9G1HJ1tC24zwK7U11M4wb0J6-6hLSD1ODEH2OAdC2_dCvbiT9wZn0byB7hY8WRCpjzvZ3cIdQeazV-Se7wGE0Z-F3hlz3i5TU6h64UYIc-SAh1bERfrPBWIaPTX08ueibW6LRaax8-cM1UUb3idrNQ2akuwTeJ2cB_QxAKVWoI-OF70x82lDcUjRw2UeXo9Upcv2RBg6VyQirQAtSnq7XRJ1a6zo3FU7Pm_5tzZlg-DXcGd1t4EzXNtMWSB6AGSO41Fc7Krq5ukOLenUtIuYL67dl7sRPm8mfZrTdFqIY1pImDvJfzpmBJr6PPdIXVWNFJftEzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از مزدوران نیجریه‌ای حالا یک فاطی کماندو از بوسنی و هرزگوین ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67306" target="_blank">📅 23:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67305">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=OHZNHf2rqPRuI6kfCZSFkt1-vyU339T9exZIOKyBOqAYVEjzzYGC_ftC1Nd0CK9NAM-1AIyQNkzpc1kp_iO_xkJRUBR3iPKtaY66dVvgFkG5oUdWUHD4TZrd84RreG8VMETIHaBSyo7BqQlGMpeWnwQ6mJR4XJP1YZkMdlfe9HltAcQhwP1IH3Vks1IiDtFTHI6J_L7ma66g5Xp6Bwn5HFhGAViR7MVZYS1Brt1k_OQgEm4C2uSNeECmQemv3cVgGaEhHNIw-yTPLTGrLwT6RRkS27GVtScFU9Tc2d2g-JAYNhuMiLupO5PY1MIklog5Xf0IfZ6sZOQ9psLn2XIwmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=OHZNHf2rqPRuI6kfCZSFkt1-vyU339T9exZIOKyBOqAYVEjzzYGC_ftC1Nd0CK9NAM-1AIyQNkzpc1kp_iO_xkJRUBR3iPKtaY66dVvgFkG5oUdWUHD4TZrd84RreG8VMETIHaBSyo7BqQlGMpeWnwQ6mJR4XJP1YZkMdlfe9HltAcQhwP1IH3Vks1IiDtFTHI6J_L7ma66g5Xp6Bwn5HFhGAViR7MVZYS1Brt1k_OQgEm4C2uSNeECmQemv3cVgGaEhHNIw-yTPLTGrLwT6RRkS27GVtScFU9Tc2d2g-JAYNhuMiLupO5PY1MIklog5Xf0IfZ6sZOQ9psLn2XIwmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم خاکسپاری رضاشاه بزرگ در تهران، زمانی که جمعیت تهران فقط ۹۰۰ هزار نفر بود و بیش از ۲۰۰ هزار نفر در مراسم شرکت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67305" target="_blank">📅 23:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67303">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RTIBRuSrhS4zvV5tGiYURCo4FXMIwKr7jECzng5hLch5L13OajUSKxDhTflsgRb5pqq4JlFEjCCyzdafiO81_CUTzqEu1ubVbjTiKH3EsO5iOT8FKvhahQ_0aKzyKYoAUR4Z5ZQkws04Ih-FioS8RRgDNWG_OELuu-M_Vn3KMc6tWET4t7tFdXwupUB8YtSTMyhdHD0tcSKHp4-rvgGIDQh1Zy3kSFWE3HvFBdM-Utcs3e0zSW6ikSN9hAHn9xvqFrWNALsrFEw1_ehXs742k4O1JXopJPzSuf9UvisU3SJ0Gao0QycC-1GerMqx6DOWv2-FvHH_yo9NnD78d0jP3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6k0bvx1Kpms6ekw7KZI7fGANpqo8S2U2Lq7JkpNqZz5OyFF-w0W4_DRbLlAVrEQ-x_L4ionETtWlNy72d3u46bE5mZ6XI5oIgRK10Oq-SZSDl9jwUflMXutemyQpItNYugaA6e7cYCPendoaB_ngL9a9Ohw5er5fQCpoRpR1a68YHB6BA07Q1MmiaTfFfmSXenkWlsSamcolTc8qIqgU-0ybGksBN0RbjTYmJTb00WvgtAGK0Rx_D-0Z3905_vUK6PIXmE0xIiN9B2bvAY7WA6nq87BJmqs1zfOJ0q78MZHwMDjdWveGswltVl7pOEK1i547iXBTNrU8NSLeymjog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
زمین گرده...
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67303" target="_blank">📅 23:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67302">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOgxgE9SaHQZ_s1tvJBCbU5x3AYM6ELpLVLu2tXHKfjCvn9TAtgNycZZDlUp6tG0d5jphT9lfT9rV4wZvWvhW1l2eY--Nmdrjnh4AW-Ew9d4Sq1ixsDBhx1ICrprLxQBsILrq0jahboKQtadF4p91FKxGcU87pnXWcPgP3LE1JVlhg2REwFQfDCap84RvOohYPZlw90DK2UDCdU3tS5UBdSp5RERIGDSDUmmXshYc7h8oiXc37grs73gj2mrKNRMIFLlDkU2VW09Ys2VnBm4D1vnybjkGrVmgxHL_wB6IQzYB1zpszc-Dc7xka3GHLGkO4SAqSz7iUOPS13icNgnKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
دو مقام آمریکایی به من گفتند که مسیر جنوبی در تنگه هرمز همچنان فعال است.
یک مقام آمریکایی مدعی شد که اکثر کشتی‌ها با سامانه شناسایی الکترونیکی خاموش تردد می‌کنند تا توسط پلتفرم‌های اطلاعاتیِ «منبع‌باز» (Open-source) رصد نشوند.
این مقام تأیید کرد که ایرانی‌ها تلاش می‌کنند از طریق رادیو VHF برای کشتی‌ها ایجاد ارعاب کنند.
مقام دوم آمریکایی اظهار داشت که سرعت تردد در مسیر جنوبی طی روزهای اخیر افزایش یافته است (حدود ۵۰ کشتی عبور کرده‌اند) و این مسیر همچنان باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67302" target="_blank">📅 23:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67301">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=KvxktnvV6Vn5X9C0sYoJfy95-F-AgKTfdpUjpKB0TKB5ChnjqG0OdDGitRdGxNCcChw5DJNX1vuZyl_ZWwytU_MRJk8GC83Sg6MWsxr9Vajpjtt66XEH6zu0gBytUXhToXjdSSd8dHO726g7dQUSY-CBVE9m5FQ3QsqgNpNYR4IuFI_Ec_nTOu5yekUQa0cFvbvEC0dW4htS-Nf0FO4pB26OMlLBKPmZ3L4KcQM8CXl6lNuwAZwzO6kNj6C9GoHwGNx_0uy8ujHsToYJqeNdUXnGD4Q7q-VoXa9emS-MX9Qj9I1gih8HvnKydyZeThEiWbX1fTV6F6ScuqJ58ohXZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=KvxktnvV6Vn5X9C0sYoJfy95-F-AgKTfdpUjpKB0TKB5ChnjqG0OdDGitRdGxNCcChw5DJNX1vuZyl_ZWwytU_MRJk8GC83Sg6MWsxr9Vajpjtt66XEH6zu0gBytUXhToXjdSSd8dHO726g7dQUSY-CBVE9m5FQ3QsqgNpNYR4IuFI_Ec_nTOu5yekUQa0cFvbvEC0dW4htS-Nf0FO4pB26OMlLBKPmZ3L4KcQM8CXl6lNuwAZwzO6kNj6C9GoHwGNx_0uy8ujHsToYJqeNdUXnGD4Q7q-VoXa9emS-MX9Qj9I1gih8HvnKydyZeThEiWbX1fTV6F6ScuqJ58ohXZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مردم اروپا با دمای نهایت ۳۶ درجه
🆚
مردم خاورمیانه با دمای حداقل ۵۰ درجه
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67301" target="_blank">📅 22:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67300">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=S_kqbvkO9Mm0iH-NCb1aGky8gdOQ6kDwajoTYvO5nidovJHN5XoiA_bwkVE6QVs8yw1hWZC4KOA5mG8Hfh66hs5HXRI3PXussPzIU0XZgi1hAIXemzZVudgNKpylG1WHzGQcL_am9zBLW6cVn-f6ciYR6kt3YqZ2hI5iwQyIrG49N3djk0VjdLEpyT6bR_W-3J6JHFJ9GXLEuM8cGnZiJc2DAHOLuaqcjp5xZyRBoNHhhSlYQoWr0D88TpJRm4tJZfSk4U92ICbmNXZY5Cs97Iph62XA9wcISEqMtZ5zXp_Slrt2khS_0-Pv1IClbzIFWN-U-Zi-Gniaxr92bHUfLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=S_kqbvkO9Mm0iH-NCb1aGky8gdOQ6kDwajoTYvO5nidovJHN5XoiA_bwkVE6QVs8yw1hWZC4KOA5mG8Hfh66hs5HXRI3PXussPzIU0XZgi1hAIXemzZVudgNKpylG1WHzGQcL_am9zBLW6cVn-f6ciYR6kt3YqZ2hI5iwQyIrG49N3djk0VjdLEpyT6bR_W-3J6JHFJ9GXLEuM8cGnZiJc2DAHOLuaqcjp5xZyRBoNHhhSlYQoWr0D88TpJRm4tJZfSk4U92ICbmNXZY5Cs97Iph62XA9wcISEqMtZ5zXp_Slrt2khS_0-Pv1IClbzIFWN-U-Zi-Gniaxr92bHUfLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیام نتانیاهو به آمریکا به مناسبت دویست و پنجاهمین سالگرد استقلال:
🔴
«۲۵۰ سال آزادی. ۲۵۰ سال دفاع از آزادی.» او این مناسبت را به عملیات «انتبه» در ۵۰ سال پیش (که در آن برادرش «یونی» حین نجات گروگان‌ها جان باخت) پیوند داد و اظهار داشت که آمریکا و اسرائیل در ارزش‌ها، سرنوشت و مبارزه با مستبدانی که شعار «مرگ بر آمریکا» و «مرگ بر اسرائیل» سر می‌دهند، اشتراک دارند. یادآوریِ یک اتحاد مستحکم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67300" target="_blank">📅 22:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67299">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VP8WvcYFguFd90OVi5EDgHqDzl8hfpOfF4DOF9cVLr_fCvrVamycbLvhM4eFU_kbnTNTv3nDziSD7GOdJowpnMEjZanOw9PeFH3zhBu3Y30HzH7eP2gwqTRCbYBQrEAf04Bdfs7l5xlF6GUYb4yC0tVOFtS4tG8ii_oOTLHZ7oUdjGL4Hg9dmRwf8gNFQm5AmC2wwNRZb_zY-fa57bdDdl7CUCESYukPq6Vk2X1RWh0A6Z1ncc6Nh5Xb8tbY_DUAN9L2f2Q_ayx9JC0Ca62oFnt5j6vwVvstVMzsDzWQdc1vTabnC1in9RtvbqNXGVzEH9E24mk0OjrJ2Bk0VafvTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
دور بعدی مذاکرات ایالات متحده آمریکا و ایران در تاریخ 11 ژوئیه (21 تیر) به میزبانی پاکستان در اسلام آباد برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67299" target="_blank">📅 21:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67298">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePw9ElbEq-aszTm66v3WudnQ-3xD4i1-ORnFHRABwKd5fOpwq9wLsTgBLPurfvzGuFx8xZAT5syei7rHppsTEWD270YihxYWJyHMhNUtD1moFH-4ORWeCKc9BXTk0R1xURtFQJ9PCuIruKk6I7oCul0HLea1a8mHFMULzAMd78fLO06z-Lvkl64plu3P_C0czAB9upYT2P5DPywid5iTru7XjsbQry0ihUPYoip2uc_e3CZQ-BDdt1n1Gey6kFcYTb-uvBqMQ5Ckr4mr3L36XqgYFj2WqRuMLaAiN-LUiv0ymrQCuPEYMmA_eQF3EcT0qB2nNBuWeBJRsjQWMdhZZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ:
فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67298" target="_blank">📅 21:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67297">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTkg2o3w-kXVKbdJpjkFbC3RTbB5VkiRdJ1O3U83MStL7SMFR4SNoO6ivPy9cV0U-Dm6zcmnf3UwfUuoN-TDay_6xjYLMxfaIZpPYOyO848_DvOQfMIdBEVbSSoGLwqC4zVtSrgmlRnvecsk2x987l8ez07oiFuh285kVEwaq0PxtGcnHMKJWYzqp2ImBmxZS4LsVx3ZpwRdGj5GHJV5-_q9w2vWmezsK2HrRlGnmz8JAHG5CxZrcuoMGW8jjWCCcOJHogxhOrd9LLRRQ9IwABYSfAuxBQVJacx0tahaXGgR_IZlIuWadTCjZItj-xjnM4R4pt3Mmfj--YhEtgW2cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ به آکسیوس:
نتانیاهو میداند رئیس کیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67297" target="_blank">📅 20:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67296">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
پرزیدنت ترامپ:
نتانیاهو درخواست ملاقات در کاخ سفید کرده است و این ملاقات ممکن است همین هفته آینده رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67296" target="_blank">📅 20:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67295">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به اکسیوس:
از دیدن ایرانی‌هایی که در مراسم خاکسپاری خامنه‌ای گریه می‌کردند، شگفت‌زده شدم. من فکر می‌کردم مردم از او متنفر بودند.فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67295" target="_blank">📅 20:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67294">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
پرزیدنت ترامپ به آکسیوس:
«همه آن‌ها آنجا هستند. یک گلوله [و می‌توانیم همه آن‌ها را از بین ببریم]، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67294" target="_blank">📅 20:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67293">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589cc62912.mp4?token=SElD6Zpcd3UNiNtR7NiU_q0lateLV4smHYOLK9SMlmKcPsRanxfmiz0rhZOXeUATdIA3smoeyHJlKhfzG50Wwvr1_3prOvESVhBhOPFn25s4hYT-ZLHwfkQB1BNM9cNf5Dz49GiFBODdBNUTiRG82JTA-m0SvbwQkHxtqC63WN6sKye94JXMR7Dxc9njs1u8JLJx0Pl7bvnaxmOBo3GmaEftNoY1AtnFgOIk9cMBre-lsGwOfEbP-f97EcSJuULa97mxidH5pAdFTTtjssnq8a0Nr_luYc7wkP5_YSOBYW3EAYUmT0sSsjRUxLSoR9LFrAlwY7-zI7QplZIjaLvOXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589cc62912.mp4?token=SElD6Zpcd3UNiNtR7NiU_q0lateLV4smHYOLK9SMlmKcPsRanxfmiz0rhZOXeUATdIA3smoeyHJlKhfzG50Wwvr1_3prOvESVhBhOPFn25s4hYT-ZLHwfkQB1BNM9cNf5Dz49GiFBODdBNUTiRG82JTA-m0SvbwQkHxtqC63WN6sKye94JXMR7Dxc9njs1u8JLJx0Pl7bvnaxmOBo3GmaEftNoY1AtnFgOIk9cMBre-lsGwOfEbP-f97EcSJuULa97mxidH5pAdFTTtjssnq8a0Nr_luYc7wkP5_YSOBYW3EAYUmT0sSsjRUxLSoR9LFrAlwY7-zI7QplZIjaLvOXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
۲۸ دسامبر ۲۰۱۱؛ مراسم تشییع جنازه کیم جونگ ایل، رهبر کره شمالی؛ مراسمی که تصاویرش به یکی از عجیب‌ترین صحنه‌های تاریخ معاصر تبدیل شد.
وقتی این تصاویر را می‌بینیم، شاید اولین واکنشمان تعجب از شدت گریه و شیون مردم باشد. اما واقعیت احتمالاً پیچیده‌تر از چیزی است که در چند ثانیه ویدئو دیده می‌شود. در کره شمالی، مردم دهه‌هاست در یکی از بسته‌ترین نظام‌های جهان زندگی می‌کنند. از کودکی به آن‌ها آموزش داده می‌شود که رهبر، شخصیتی فراتر از یک سیاستمدار است و باید بی‌چون‌وچرا به او وفادار بود.
از سوی دیگر، در چنین حکومت‌هایی، ابراز احساسات در مراسم‌های رسمی همیشه یک انتخاب شخصی نیست. بسیاری از تحلیلگران معتقدند که آنچه در این تصاویر می‌بینیم، ترکیبی از باور واقعی، سال‌ها تبلیغات حکومتی، فشار اجتماعی، ترس از حکومت و گاهی هم منافع شخصی است.
شاید مهم‌ترین درس این تصاویر این باشد که وقتی دسترسی مردم به اطلاعات آزاد محدود شود و فقط یک روایت سال‌ها تکرار شود، همان روایت می‌تواند واقعیت ذهن بسیاری از افراد را شکل دهد.
تاریخ بارها نشان داده که پرستش شخصیت، فقط به یک کشور محدود نیست؛ هر جامعه‌ای که آزادی بیان، نقد و گردش آزاد اطلاعات را از دست بدهد، ممکن است در همان مسیر قدم بگذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67293" target="_blank">📅 20:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67292">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/648e669177.mp4?token=p_BzKUpeKdDJGLqLEvIjqPNqsb0ZvPY2VDJro_237umTBoF6AdbPx1V77A9eizEHQWG-Qj-J6U0lB44YE7PIQMpO80mBa3kA5o1ONpQ511lGwoo0WcKYdLjDA1KOdT9kW1Ttz3eO5Wg4vrMHnoC4-1gRieWLWwx72ududtR121SM00xC-Jgq4pNCgPVD0NUZEw6kdCnR8YbNrri40JkbPh2sAxVonkOpUJk0MwOcaezOCa-vpBGHEFQkxfOA0h6tTwijx1W5mEZUd-D3717UNzBF5Q_sk8ndiypoxub3NmSa02WIrsMQBN3dOuAN0CTZGHP_R8ykQkc-jNglqUdv2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/648e669177.mp4?token=p_BzKUpeKdDJGLqLEvIjqPNqsb0ZvPY2VDJro_237umTBoF6AdbPx1V77A9eizEHQWG-Qj-J6U0lB44YE7PIQMpO80mBa3kA5o1ONpQ511lGwoo0WcKYdLjDA1KOdT9kW1Ttz3eO5Wg4vrMHnoC4-1gRieWLWwx72ududtR121SM00xC-Jgq4pNCgPVD0NUZEw6kdCnR8YbNrri40JkbPh2sAxVonkOpUJk0MwOcaezOCa-vpBGHEFQkxfOA0h6tTwijx1W5mEZUd-D3717UNzBF5Q_sk8ndiypoxub3NmSa02WIrsMQBN3dOuAN0CTZGHP_R8ykQkc-jNglqUdv2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
▶️
داده‌های تارنمای ردیابی پرواز «فلایت رادار ۲۴» (Flightradar24) نشان می‌دهد که یک خلبان آمریکایی در آستانه چهارم ژوئیه، روز استقلال ایالات متحده، با طراحی مسیر پرواز خود بر فراز ایالت اوهایو، عبارت «USA 250th» را در کنار نقشه جغرافیایی آمریکا ترسیم کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67292" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67291">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر : مراجع تقلیدی که‌ قراره نمازِ علی خامنه‌ای رو بخونن که همچنان خبری از مجتبی خامنه‌ای نیست!
تهران : سبحانی
قم : عبدالله جوادی آملی
مشهد : نوری همدانی
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67291" target="_blank">📅 19:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67290">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=NOBvua5cYOQntHDGs-g_USWEz0bz9uGe4IXJrNbcuV7FpLKG8A3opbeFzP7bnDUNBETfb38Mcgikmlr907uruTUBfKcHBzt_4erFVbf4g5ubeykhUdUaL5NuiTY9Dq5LD_WuosXC6Zz1M8JTmctsUGvfh_3-xtLHxa4RocBsuZxVyd2LUWEJhjmWWzjz8jQDQq65s9zqI5iyp-q_Kjdx9ZY5NbIuPKKGc0x4_nkcvFqqdgTYJBfyAEY9OUMyVaw0CGA1zL9CxFl1Cln4T_iif5-E8mumAr65w00_oGqLJHD6Dn70cYdWbcdZpC4o1En9WIGFS-miGjsjyQI-KLz5EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=NOBvua5cYOQntHDGs-g_USWEz0bz9uGe4IXJrNbcuV7FpLKG8A3opbeFzP7bnDUNBETfb38Mcgikmlr907uruTUBfKcHBzt_4erFVbf4g5ubeykhUdUaL5NuiTY9Dq5LD_WuosXC6Zz1M8JTmctsUGvfh_3-xtLHxa4RocBsuZxVyd2LUWEJhjmWWzjz8jQDQq65s9zqI5iyp-q_Kjdx9ZY5NbIuPKKGc0x4_nkcvFqqdgTYJBfyAEY9OUMyVaw0CGA1zL9CxFl1Cln4T_iif5-E8mumAr65w00_oGqLJHD6Dn70cYdWbcdZpC4o1En9WIGFS-miGjsjyQI-KLz5EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
یحیی رحیم صفوی:
بین ایران و اسراییل جنگ موجودیتی است یکی باید بماند
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67290" target="_blank">📅 18:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67289">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKW6Q9fHcqla9H3urRwPymZ1X-oksZqWtI9i296HVI7V_A0YEZy-AJocsoUKukg5GC7oUafsSBVBPutSos9Uz4X9VC3mhJjooJjthXnPA_R2lVUQALblYQacSXnzTPVf1BTDCB7ACghPcxtO9BXw3CVzXh3g4AKCh9UwAgxFhpkJXxVmEdcByAMxIRnVkZTEIBc3civ1CDGHf0b_MWLo5Ba1OcnXJDnU02SZ5qVCbxD1xwh2awY82PvTew7CvsIGKQK1CJwsLbjiNXEP46ZHnUgdPicvLF9Xw_nuEDT6AEbR81iGtaLTN4v21YRXcjPwcMuIAvBKyFenq7BxskggWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
🔴
خطاب به نمایندگان خارجی حاضر در تهران برای سوگواری علی خامنه‌ای، دیکتاتور فقید ایران: ایران در سوگ او نیست.
🔴
ایران سوگوار بیش از ۴۰ هزار فرزند خود است که در روزهای ۸ و ۹ ژانویه به دست خامنه‌ای، قالیباف و ماشین سرکوب آن‌ها به خاک و خون کشیده شدند.
🔴
رژیم مبالغ هنگفتی از ثروت مردم ایران را صرف برپایی این نمایش تبلیغاتی می‌کند، حال آنکه حتی یک رهبر دموکراتیک نیز در آن حضور نیافت.
🔴
آنچه امروز می‌بینید، ملتی نیست که در سوگ حاکم خود نشسته باشد؛
🔴
بلکه ملتی است سرشار از خشم برحق، و همین خشم و دلیریِ قهرمانانه، بساطِ باقی‌مانده‌ی این رژیم جنایتکار را درهم خواهد پیچید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67289" target="_blank">📅 17:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67288">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=W1_BGLjI0SzLxq0i3-sRfYMVZ90eRzxIRKYnCLm1fSjmbApEudbNSVDfUFGXchf2UWsd3VCR3kUw7sZbYVg7W338vu8Zxy2ClV6RRjqOeSrjZSVVMpjmNTh6ckMPASBZYtuoc6yVddeDZPimYS_KtI-vinGywUBiJV1iX5Ox2MxKL6fun0z5_q90wpd_bGC-ytcG3aJOGmzkOeTj1p2ZCfaDZCT7xwIw7vtBJKp7l2U6BMw6QNrWmjdKYFgbxpVJ23tf6Pe74sWl9VGM4jEi6IJYXK02oH9oNXQdsE67cSlLgMglHHmvbwrtzMbhzD1klPfNcPsbe1F8oueIvlKevA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=W1_BGLjI0SzLxq0i3-sRfYMVZ90eRzxIRKYnCLm1fSjmbApEudbNSVDfUFGXchf2UWsd3VCR3kUw7sZbYVg7W338vu8Zxy2ClV6RRjqOeSrjZSVVMpjmNTh6ckMPASBZYtuoc6yVddeDZPimYS_KtI-vinGywUBiJV1iX5Ox2MxKL6fun0z5_q90wpd_bGC-ytcG3aJOGmzkOeTj1p2ZCfaDZCT7xwIw7vtBJKp7l2U6BMw6QNrWmjdKYFgbxpVJ23tf6Pe74sWl9VGM4jEi6IJYXK02oH9oNXQdsE67cSlLgMglHHmvbwrtzMbhzD1klPfNcPsbe1F8oueIvlKevA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
روایتی تصویری از شاهنشاه آریامهر محمدرضا شاه پهلوی:
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67288" target="_blank">📅 17:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67287">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‼️
ادعای نیویورک تایمز به نقل از ۴ مقام ایرانی:
پزشکیان به مجتبی اطلاع داده بود که در صورت عدم توافق، از سمت خود استعفا خواهد داد.
نامه‌ای از رئیس بانک مرکزی ایران باعث شد مجتبی با یادداشت تفاهم موافقت کند.
پزشکیان، قبل از امضای توافق، به مجتبی خامنه‌ای اطلاع داد که محاصره دریایی، ایران را فلج خواهد کرد
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67287" target="_blank">📅 16:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67286">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=p-6aimUcKY_9aWpXQgXUP_rWu3KZ_bRo4CBzJb2rJ9plId-YRfXCheZe9s8G98dR0jSPR7byHygEP1BML4eZkggx5K1VvYsNPeHcFFZeWYFjPn8ZJS0OVHF6nFBL4FZIxAJHEVpelWjoZlgU2kWfh2pZueqkJ2SPGc16_OZWFNTTlBbGCcPogUzDYKwoHaRfCRFHMrr6o8Jsc_yxSw1bhv0VgHf70lwC4QkUYIfGbFoVEfkx6joKeC2njIfs4l8IEpfdtV2YoczTRoyFZBkb3ZhhPz4WRVzhXDgqGnUVarYJvsv4d6eyDczNItb8hrkuNdoVPcKHWL-z54beb5IrVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=p-6aimUcKY_9aWpXQgXUP_rWu3KZ_bRo4CBzJb2rJ9plId-YRfXCheZe9s8G98dR0jSPR7byHygEP1BML4eZkggx5K1VvYsNPeHcFFZeWYFjPn8ZJS0OVHF6nFBL4FZIxAJHEVpelWjoZlgU2kWfh2pZueqkJ2SPGc16_OZWFNTTlBbGCcPogUzDYKwoHaRfCRFHMrr6o8Jsc_yxSw1bhv0VgHf70lwC4QkUYIfGbFoVEfkx6joKeC2njIfs4l8IEpfdtV2YoczTRoyFZBkb3ZhhPz4WRVzhXDgqGnUVarYJvsv4d6eyDczNItb8hrkuNdoVPcKHWL-z54beb5IrVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارهای عجیب در تجمع شبانه علیه قالیباف و آمریکا
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67286" target="_blank">📅 16:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67285">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=mRiLek9pwf0xQvweTjRnRZ2AUcLnMWLw3luHw0roWTN6Qp6g923MBpcgJfnbmCb8AOeR9n2fraYVfrHbpBeO2bBe6Yn9Tf7oVUlHwiKdf-Mn4QhleoMUj8j3Al2THNbiyZTCv8IR0TCbcEp7uF75E-bip_YB7bTHIUj6CfiAKCyXRZ-EVvw-F9CKw3xKvbyZH-1lZfso0-8B49MMwtXfIJqp2cONoxPrTLBQQoLIk4Y0pfNGJcvV6_6YPIaSqAiY8w5x78VB7eFwmQUZPPHg1nadwVFOlGQyKv4m2ZIvo_5xOeSnIjYCYkK2pVUesnuGkCmN59qv8ym3D0TgQUtl-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=mRiLek9pwf0xQvweTjRnRZ2AUcLnMWLw3luHw0roWTN6Qp6g923MBpcgJfnbmCb8AOeR9n2fraYVfrHbpBeO2bBe6Yn9Tf7oVUlHwiKdf-Mn4QhleoMUj8j3Al2THNbiyZTCv8IR0TCbcEp7uF75E-bip_YB7bTHIUj6CfiAKCyXRZ-EVvw-F9CKw3xKvbyZH-1lZfso0-8B49MMwtXfIJqp2cONoxPrTLBQQoLIk4Y0pfNGJcvV6_6YPIaSqAiY8w5x78VB7eFwmQUZPPHg1nadwVFOlGQyKv4m2ZIvo_5xOeSnIjYCYkK2pVUesnuGkCmN59qv8ym3D0TgQUtl-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😐
ویدیوی این بسیجی که در مراسم تشییع علی خامنه‌ای وایرال شد!
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67285" target="_blank">📅 16:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67284">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67284" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67284" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67283">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67283" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67282">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/An8B1e1Uri3OH9B7Ht8RBxWDd0f2hYRbvBMM8jv0j5yIkJ83SZAdqqrIlk6DO-ur6rCdPjIcQRz9wS4Wj5zwVXzNh_IL7QN1KfnMB17ts6fghTmetHFhjn4eLCJoPUK6yP0Hc-0TexSMh-Px-fcJWjIFKyE2axzaYKtZQM63GuWAPvmO06xMnmczINDA_lj7VnByVw6Uj7oJupcgjYXGCWOnbXr0gG6gzA3J9DsNPvWs_3b4gQeJz1dRf3pAhf5ECPsqqboWKuki0ZwKh2FUXaL0j5mz9gQiP7JunSf9AlO-19pBa-IYLq2TjldOPWKT0F6k1QH7YeqALj1qWJhsBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علی عظمایی فرمانده جدید نیرو دریایی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67282" target="_blank">📅 16:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67281">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
با تصمیم هیئت دولت، کل کشور فردا تعطیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67281" target="_blank">📅 16:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67280">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oL_LpEWusptBnQXYHSXGHYxDVMyeey5L5u5U5606bguamFS6w2jnrj0zj1v02WT8ly_S9aLz4InZXhKq5NmioggcLtIOcSxt9OoRL7ZEPXMb8GqAczhBK7JDLIylB5ZChROvfXxJC0k5mupRdOgUH0fYnoDoEPDrDUWdOv7VZdqngNgoNinz1eL8n-LQ7kRb2sgcGi7fsC5BVSuC8Fk8j7bOdwtpXzSiyN0Tb0-oZAy9iMq5bhEFPrLDwl6ocK75mb426qj76_9ps0kT4kFtpqadfG4gRIVzRycl39y3e3t8kaPc53KHNr55oITl6CfoWmiKUWCuVbTFdmzTy_VDwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیویورک تایمز به نقل از منابع آگاه:
🔴
مجتبی خامنه‌ای به مقام‌ها گفته است می‌خواهد در مراسم تدفین پدرش در حرم امام هشتم شیعیان در مشهد، که برای ۱۸ تیر برنامه‌ریزی شده، شرکت کند و نماز میت را بخواند.
🔴
مقام‌های امنیتی تاکنون با حضور مجتبی خامنه‌ای در این مراسم مخالفت کرده‌اند، زیرا نگران هستند اسرائیل از این مراسم برای کشتن او یا ردیابی محل اختفایش استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67280" target="_blank">📅 15:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67277">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SRGHehm9dp0W5wZR7B0kD4nHZ1FXfQfoW1KJTzTbjy6eya6Uju41mfO9c0HK5CJqje1qHnBFGErTYARprnmJchlRJK0LPKvjSqBefaVtpuoNCuWcm4o7C8NsPZDhu2UnGodu1msEIkp5_AJkPlJYZYn46_pFWEuQ72nrYUgEYaejbqfp9KRZROxR7Tar62IWc90i3NFJwGiHFHyLIaBwaIgBdcCaTJrmAUeKC8axQKEmxF0MNTzt0exuL61XKwFHwRKvZrvA78o6EdI4JEFDHExzknVgNNnSg478X0WXAcKfD3Xcv-GmAfs3MuzjxCAZNpTUGt2zD3MSsWON6n0H3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TgqRk2b4z76Bdpo42SsstlrkOMNOSzwvEyN6BeM_oHRnInT0069yAsRZJNxdcq-t2HgY78akXOUeubdAp8YAIkMkRnKXYx1YvXp-dZ2bmyI0Chppc8yQSYtUmGCNpsKpLcKPEBhzdM2FM-528l1228HTfRLiEKDUIVBo_2i50rVB0LDhtAIbFH-J5ZYEJJm2_vxNqkwxxiacP4IRvw-qbwadJ4ebsJPe2bGsGF0_dJP--vgcObhX2yCdxCgcSt7nBw48IRe8TIlq3xkzfEFUkhaIquYH1dULa4zAPxD6fdqkB6ZUbh0P1CXgpKFWzjF61TImzUEu57h33BaWdqX6wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=I4HBYh8HVuA6JjMm7yDnmeRoPUmZw4opx5xdAxTBj541aPFf_v6fmo4wsUTzXx0Drvl2myLSlYksBK5lILRHpndvSQkDtmGSUngYEcMMD2WIRFIR7_dCbeecTRxbPuapC7JajODsnyXiw1oIAspfLW9VLKQvHWFgP3PXmUwH_jSz2fvDwtKFAzuWStTIlWhrAjEtbwxpKwTWpRHeIf9Lk565Vz6grUS7ASrEmi8OplYEAk-R-c_8GEactRle_OvZWDZ1uQny8US9SOd1h3zhoVnmfUNRMauHlZhRAyyEZFkpZJNbL-VmJ6RkWK-Z7N-ZeKCRE7wnTIuwWjo-DMHQ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=I4HBYh8HVuA6JjMm7yDnmeRoPUmZw4opx5xdAxTBj541aPFf_v6fmo4wsUTzXx0Drvl2myLSlYksBK5lILRHpndvSQkDtmGSUngYEcMMD2WIRFIR7_dCbeecTRxbPuapC7JajODsnyXiw1oIAspfLW9VLKQvHWFgP3PXmUwH_jSz2fvDwtKFAzuWStTIlWhrAjEtbwxpKwTWpRHeIf9Lk565Vz6grUS7ASrEmi8OplYEAk-R-c_8GEactRle_OvZWDZ1uQny8US9SOd1h3zhoVnmfUNRMauHlZhRAyyEZFkpZJNbL-VmJ6RkWK-Z7N-ZeKCRE7wnTIuwWjo-DMHQ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب، برخورد یک صاعقه با برج وان ورلد ترید سنتر در نیویورک
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67277" target="_blank">📅 15:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67276">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzpfw_fsuQZUb-XmbN5cEE3NscBeEMu5bnGcrV5faSyTTcR9v7O0AAOr9KYEpUCQ2JfjngjUPguG7E3kmdgce-KDrJl3ST4hROUAM-3BhxqvStFFdd0u3SeK25mCsf5qvyY6zKpAR53OD9gzawKwAFK6BsrFYLwecvcL8oDPNoVtc2tWMCTynSHHipEhocC_4nUFt-rfg02YEe8-WSK-FCu0f2PQZ6PsQ0ydx8evWE7b3Znez_i9Q1RmSBvW7f_I6_fNY3DOtjr1aKKimLp8GUfJzdhzPS3W9XNFJsOnHsPOgLws7yoKaJoaj6s4gyi59BRoSud8zdHmEmoxKJf0lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدودوف معاون رئیس شورای امنیت روسیه:
🔴
ج ا به‌جای سلاح هسته‌ای، به سلاح دیگری دست یافته که دست‌کمی از سلاح هسته‌ای ندارد: تنگه هرمز.
🔴
بحث‌ها اکنون بر سر این است که در آینده، درباره نحوه کارکرد و وضعیت این تنگه چه توافق‌هایی حاصل خواهد شد.
🔴
مقام‌های ایرانی همچنین یک «سلاح ترمونوکلئار» دیگر هم در اختیار دارند: تنگه باب‌المندب.
🔴
اگر این گذرگاه بسته شود، همه محموله‌های نفتی و سایر مسیرهای حمل‌ونقل عملاً قفل خواهند شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67276" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67275">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIoPghaMuOs54fWotZX7ONFtTR1tayumcAovyzNRIpAXqr1qN_kTo4GONuxKHsDKnAY-f0In9Q-w-chWnZ5sizMKhzOzTdIVhC7JL4mJhCUbTeUgkV2DUXETjseL6QWZJv8FvDPCP48WhkLo5h64VlOA5WlYYdvXr3emIHSP7RVhKfXzbyCA_cpD0e49yVy6zHUpyjU9nnJKsApCaqUQOcEuMmkxT6uZiffqChZ7CVScqpvfMV1x7unXgh-EV1QywC7gQ5a450UTcjBLgTCCNK-IxZoUiLErLPUxTX-rUogt8cB27rRJNkz8I_cZRpWErHS3ZsoAsy6_4xmrtB-fUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمال مجازی‌شدن مدارس و دانشگاه‌ها در سال جاری!
🔴
میزان کسری گاز به حدود ۶۳۰ میلیون مترمکعب رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67275" target="_blank">📅 14:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67274">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0SoRqzH3xAVMsUhrrRd0TRb-0BhS5XQXYmhe61QEe8-CrIpoADoQfAmW-AX9C8gD_3UUBBJ2Mk8AAzu8i8VxzJfddJqy-ZiI_b4ycQSq3Mlqc00AKkZ6mxU3kKYtDoiHktVgzch3O10CLuLpurUz6sNZ13KvDjEDDCxw1QaNVg1t14qHXRd9fg5-UPqWvUnBci0hbkFyoOKOodTlAQxPmeTlUOSSTBXdfu5e0Hva0iSeyxNvl4lT3Lip1G14Ut9_YJYtDRK9zMggZ3SfxyPYfWVCQPPLtXVFYX_Pax_p08hQVXZZHGltQZXaUM5CGWdfY0tBoJpknIdsS4bvaDZjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برافراشتن پرچم «ترامپ را بکشید» در مراسم وداع با جسد علی خامنه‌ای:
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67274" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67273">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=vaETACYnf6S1Z4Nj08DAZHrKq0VuTWe57lpZRb06VAbvBtu_kvezdF636JRqPo29rNnHXP6uX1l_z4uY4d4NwbJeENnOX6juOdaENCiFwrc1oMsLhbuC6xmM3S9cJs6SkrPegJfzTw0-Y8NPGrXEC5QgGP6Qk0M2RTBHc3mXQHLN2sE52LcNnyH2UzYG8hhwTCwywbjMAmrLBpRYu6y186II21GfVCuYLrw5A5a32kxTgF0dk3rrh7r1Stg9AijAzXEYYkZesC7mTf_io2diUcIC_NvviRBPE_tXsLloDXrQJ84i-VUSvb23vaYHGNzluvJvFqd1J3rtCubbHCZx4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=vaETACYnf6S1Z4Nj08DAZHrKq0VuTWe57lpZRb06VAbvBtu_kvezdF636JRqPo29rNnHXP6uX1l_z4uY4d4NwbJeENnOX6juOdaENCiFwrc1oMsLhbuC6xmM3S9cJs6SkrPegJfzTw0-Y8NPGrXEC5QgGP6Qk0M2RTBHc3mXQHLN2sE52LcNnyH2UzYG8hhwTCwywbjMAmrLBpRYu6y186II21GfVCuYLrw5A5a32kxTgF0dk3rrh7r1Stg9AijAzXEYYkZesC7mTf_io2diUcIC_NvviRBPE_tXsLloDXrQJ84i-VUSvb23vaYHGNzluvJvFqd1J3rtCubbHCZx4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش نکیر و منکر بعد از ۱۲۰ روز
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67273" target="_blank">📅 13:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67272">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKskgLFhgHRWpj7A-T2I099UkwRN1PwLmQTyalQM0Ym3oOBRKf18c8y-vVwlaxTvmfNTnmYuheBvzvlPGqk__oO2Onc00GbVblkDiHgpIYKeQFVsAhDTKLef5-NrdsUCPPW7IH0XoYIK0jLMb1BnhEutKmnpReY2IHd_96NNgKgfr79kBhFTNnmgw_3cUkQUHe8_SsTsEIMnJZvEtxJ90z-xJU1hWjiQhLF04mZbtLZRuUnK_XAOhuhLlwPas-607bMUMcUbq9LSttB6eVWTfmbQEBzT5LQrZ_Qyq8OjsAs-6SsLGl9ZFa_ejKaEEILLWdwWHQSLmIMdnIEWZu8ixA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
التماس رسانه حکومتی در ایتا برای حضور در مراسم ؛ جمعیت کم است...
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67272" target="_blank">📅 12:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67271">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=Fp-KITDhy256LDMT_4uQLUAow0n1UuOitsA_e5-F1RWlL0tAp4ujH9er3ljTyFctONXAxehM5chDJtCrQHNne7BXlhBTZzmtCCFg4mxzMNXsNx5OSSwxVne2LucL-BcNWdkrvdI9byv3PbY9-8NWanlAjZwUcMip5RVFzQ7smjJoDAeI5yXGQRGNn_5_Y6fdHeRbfwsbS6MKKu5RZWcbzChOh-7cxToXlvcWjQzUY-R-2p1KX9zQz8pR9ssdzVvA2nj2rzX4yDoZeJEtA68YV5iNoB-iu1b1e3m3uPX04vZazc-bMqfFtsuL0_zcfcIbLFzCkPQK1T9c0CI1p3Ofhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=Fp-KITDhy256LDMT_4uQLUAow0n1UuOitsA_e5-F1RWlL0tAp4ujH9er3ljTyFctONXAxehM5chDJtCrQHNne7BXlhBTZzmtCCFg4mxzMNXsNx5OSSwxVne2LucL-BcNWdkrvdI9byv3PbY9-8NWanlAjZwUcMip5RVFzQ7smjJoDAeI5yXGQRGNn_5_Y6fdHeRbfwsbS6MKKu5RZWcbzChOh-7cxToXlvcWjQzUY-R-2p1KX9zQz8pR9ssdzVvA2nj2rzX4yDoZeJEtA68YV5iNoB-iu1b1e3m3uPX04vZazc-bMqfFtsuL0_zcfcIbLFzCkPQK1T9c0CI1p3Ofhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیو ای
از بمباران بیت رهبری9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67271" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67270">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=cpOjx8zXgF8n6wdEBSEjfaf1dE77KSvUMVN54F582IBX51oDY66pC8JRrbPSUc7vaxPn7Qp7K8-2DcmG-7tv81dQpknWkAfatDIwC-n7TkoucaryY4RY8jADzYrFMBt-AEe6DlC3klwyZe-uiU5lZH5ZKx55mtq9y49UiRux5302zcxkKANHM5jWW6NN4-IyAKCA3TtMHwJEICN6WooriPtcuqoT-F_z6eH8t231KPf5GatT9tLJIbYiLMY-U1c79jGZUAIRhOhgseN6b1TMKQbDhL6_2a-EvOpo7TlxdCUYFy6-XkPt5rwG9vEUJPWl1ioKdLno2QtbTsAzt1HTGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=cpOjx8zXgF8n6wdEBSEjfaf1dE77KSvUMVN54F582IBX51oDY66pC8JRrbPSUc7vaxPn7Qp7K8-2DcmG-7tv81dQpknWkAfatDIwC-n7TkoucaryY4RY8jADzYrFMBt-AEe6DlC3klwyZe-uiU5lZH5ZKx55mtq9y49UiRux5302zcxkKANHM5jWW6NN4-IyAKCA3TtMHwJEICN6WooriPtcuqoT-F_z6eH8t231KPf5GatT9tLJIbYiLMY-U1c79jGZUAIRhOhgseN6b1TMKQbDhL6_2a-EvOpo7TlxdCUYFy6-XkPt5rwG9vEUJPWl1ioKdLno2QtbTsAzt1HTGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار مرگ بر آمریکا در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67270" target="_blank">📅 11:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67268">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=gMkKdvcKysC_y_O0raeGUrgRHfQEAeex1yHo7GLI_uaTF-K9b8siECWfGkmDA2XiXeV7IeGu-3DdFXyExSeZ4Q0ucgJpFesETvGKcfg_glxx78bLkToAWOMb9by9WO5uFlrG98o6ycWHrIM_-QXfoBLhfIUi-fhrPNlltbb7firw8FrXea8uXkTZ3lSLzS8viS4HF4_VnSFcFMxTdG54-a_7nihnjZSstFA4949yRJ-Jqh6cT50Jfz09IUKCG8n4VBM7UDotK9l5lgcbCTpeX_YL25vjUtzTUfZoUUo0J82UBqpTkCMfh171SyH1OLlMuu8jnDjnQmdM9WzwTZ3VFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=gMkKdvcKysC_y_O0raeGUrgRHfQEAeex1yHo7GLI_uaTF-K9b8siECWfGkmDA2XiXeV7IeGu-3DdFXyExSeZ4Q0ucgJpFesETvGKcfg_glxx78bLkToAWOMb9by9WO5uFlrG98o6ycWHrIM_-QXfoBLhfIUi-fhrPNlltbb7firw8FrXea8uXkTZ3lSLzS8viS4HF4_VnSFcFMxTdG54-a_7nihnjZSstFA4949yRJ-Jqh6cT50Jfz09IUKCG8n4VBM7UDotK9l5lgcbCTpeX_YL25vjUtzTUfZoUUo0J82UBqpTkCMfh171SyH1OLlMuu8jnDjnQmdM9WzwTZ3VFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از پرواز جنگنده‌های اسرائیلی بر فراز بیروت در مراسم تشییع جنازه حسن نصرالله دبیر کل حزب‌الله لبنان بین سالهای1992تا2024!
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67268" target="_blank">📅 11:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67267">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=MIyTsvAO63bT6SSrLooeKbfyeF0eazJPp8x5JvJTRlK_uTNDaXFxIzmnoY7xFP5jZxMrOXFmEGwAICe6kdZ5PonYvi5POBbMDmEnRTvLhA67M6tGymwtLdmiaQhEWh8j-sz3sV2DIKqgvuyz8M2_d-E66iV8cDqGDykaXVZln_-v3Um83K8OXqjtSYNiiU9Kd6XSYZ6booyI9m_atrmp2FsbAffAY4i5ReqDM4b2ge8qBvgc6G0WX-zPsWP5cXCSAOr3hhKVj9WxBJAKCIBpxYqM6kVgKvKwiiUfkHxTmL9x_C9lFvK6pADpd5zAwbrCiAhHr1ZO2d0OYaomPeB_Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=MIyTsvAO63bT6SSrLooeKbfyeF0eazJPp8x5JvJTRlK_uTNDaXFxIzmnoY7xFP5jZxMrOXFmEGwAICe6kdZ5PonYvi5POBbMDmEnRTvLhA67M6tGymwtLdmiaQhEWh8j-sz3sV2DIKqgvuyz8M2_d-E66iV8cDqGDykaXVZln_-v3Um83K8OXqjtSYNiiU9Kd6XSYZ6booyI9m_atrmp2FsbAffAY4i5ReqDM4b2ge8qBvgc6G0WX-zPsWP5cXCSAOr3hhKVj9WxBJAKCIBpxYqM6kVgKvKwiiUfkHxTmL9x_C9lFvK6pADpd5zAwbrCiAhHr1ZO2d0OYaomPeB_Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مایک والتز نماینده ایالات متحده خطاب به نماینده جمهوری اسلامی در شورای امنیت سازمان ملل :
🔴
اینجا تهران نیست که بخواهید همه را خفه کنید ، اینجا آمریکا است ، اینجا سازمان ملل است. این اسناد حملات شما به مناطق مسکونی بحرین است که دروغ نمی‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67267" target="_blank">📅 10:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67266">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=HRPfGNnTcNp-n7r29UyEBqkHJz0Uj2lgKKyNhdEk-xUJWFFDGNoUG9avjQDJtwU_kpTfa1h-r_SH-laguNZHnGdgBZoNFqZ3ofhe_mko-lMy52DfzJhj-3NxQmA-zHgaNYBFLgG1kA0ci5_CYv1hCDyjWEo5XK5J-Jh0ov5XDGG9YdMvWqyrnXkwVji88irhkVq76T9BnZBvqhxR4aFcfe30siIMNTg5MTL8J1r50b0YuAWQbkt4FytbrLLPfQsJaanYIzAtqOz6TXr5oqGdRKnIrDKUUpd_zMau5BY2CWOy1RK54GUUVhWwl6IuGHVLJH25sVCZpWWeBW_x27zNfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=HRPfGNnTcNp-n7r29UyEBqkHJz0Uj2lgKKyNhdEk-xUJWFFDGNoUG9avjQDJtwU_kpTfa1h-r_SH-laguNZHnGdgBZoNFqZ3ofhe_mko-lMy52DfzJhj-3NxQmA-zHgaNYBFLgG1kA0ci5_CYv1hCDyjWEo5XK5J-Jh0ov5XDGG9YdMvWqyrnXkwVji88irhkVq76T9BnZBvqhxR4aFcfe30siIMNTg5MTL8J1r50b0YuAWQbkt4FytbrLLPfQsJaanYIzAtqOz6TXr5oqGdRKnIrDKUUpd_zMau5BY2CWOy1RK54GUUVhWwl6IuGHVLJH25sVCZpWWeBW_x27zNfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
وقتی تو ایران میخوای پیشرفت کنی
واکنش آخوندا:
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67266" target="_blank">📅 10:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67265">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=ZYVdPIy84XCxNX2QdrLGGHChyTfqmPeXqCMdQcOrvPRpJTK2tXnLNHtOL7TtmUCwV8DjKnOKVfqr-lqWXkoar_I-35E03shg4-NF8aSeeUaGA5tSadSUNcxMWDjjxyN98ACmTKQ12-U5xjKpyDw046chD3MhyszUY77gTtDvWNVkn3Hcmm-4X4k3INq5JtRntzcZNuGAI6vIepQ3TALiZvFRVry7FEm0EDqDwfIsLEy0pQ-lG0W6MynxikHTPQ4g10AeRLZHhPMX86zFszgKdyDrPUI4eQyYVPiWVlTpoFrH_HHJKh0T6I8NnVDDVF4E5d8mxHUEuriBqmnp_WBJlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=ZYVdPIy84XCxNX2QdrLGGHChyTfqmPeXqCMdQcOrvPRpJTK2tXnLNHtOL7TtmUCwV8DjKnOKVfqr-lqWXkoar_I-35E03shg4-NF8aSeeUaGA5tSadSUNcxMWDjjxyN98ACmTKQ12-U5xjKpyDw046chD3MhyszUY77gTtDvWNVkn3Hcmm-4X4k3INq5JtRntzcZNuGAI6vIepQ3TALiZvFRVry7FEm0EDqDwfIsLEy0pQ-lG0W6MynxikHTPQ4g10AeRLZHhPMX86zFszgKdyDrPUI4eQyYVPiWVlTpoFrH_HHJKh0T6I8NnVDDVF4E5d8mxHUEuriBqmnp_WBJlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
ما ایران را حسابی درهم کوبیدیم. آن‌ها برای توافق لحظه‌شماری می‌کنند؛ به‌شدت خواهان توافق هستند. ما به خاطر یک مراسم خاکسپاری، یک هفته به آن‌ها مهلت دادیم، چون آدم‌های خوبی هستیم. واقعیت همین است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67265" target="_blank">📅 09:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67264">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=GoV7QjiVh6hjmhy6ujWEyiuWqecZFHxNw99CuFzaKrgG7LfcIZ45s16Kbui8arDl2x0Yq1wHC9_yepUKLQgERaZ7MlYxM19daXyvYacLvtYPRLhF3XJngbF9WAjyWrlfLAOoIiMbkWc-rP3pqiO4OuXdx_cejUnzTq86j5tEBvxKgfRVHKwDbPRDEhiDi0MtpDiqi2g0ougkcXl4TzqgVyRSzKqAG8sjJpKLY-XgdN5cFOZNMFE9-NEGx-9IIvDXrREKGKHG8-n4HcwKJqgwGl41SN4pt9ctgntU4eDmBaKoZcsC4x8gIdEVOVf2vee0FzeCepLdgzUoquetUzD9aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=GoV7QjiVh6hjmhy6ujWEyiuWqecZFHxNw99CuFzaKrgG7LfcIZ45s16Kbui8arDl2x0Yq1wHC9_yepUKLQgERaZ7MlYxM19daXyvYacLvtYPRLhF3XJngbF9WAjyWrlfLAOoIiMbkWc-rP3pqiO4OuXdx_cejUnzTq86j5tEBvxKgfRVHKwDbPRDEhiDi0MtpDiqi2g0ougkcXl4TzqgVyRSzKqAG8sjJpKLY-XgdN5cFOZNMFE9-NEGx-9IIvDXrREKGKHG8-n4HcwKJqgwGl41SN4pt9ctgntU4eDmBaKoZcsC4x8gIdEVOVf2vee0FzeCepLdgzUoquetUzD9aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
آمریکا یکی از داکترین هاش برای به زانو درآوردن کشور مقابل اینه که هزینه ملیشون رو بالا میبره مانند شوروی که همینجور کمرش رو شکوند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67264" target="_blank">📅 09:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67263">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⏸
مستند کامل و 46دقیقه ای شبکه 14 اسرائیل به نام از «چشمان جاسوسی در تهران»:
این مستند جنجالی دیشب از شبکه 14 اسرائیل پخش شد.این نسخه زیر نویس فارسی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67263" target="_blank">📅 09:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67262">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/iDJVpzBVe632mjMSS2oU_QxrzaxToUzRcMnLpzy6xsSjBlK5yoO_P5HhvhKLpZoX8o2HuOoaJaKW871wtRf8Q8HUKbX5wCVYkfNNotbYCxIhz6HjVRNV9ozNpVZUHHHjwYeWNeZ6XVW9PdyPb1f69S3hvqp6dAU2uFbRs1qSTbWvlVKpv1lUDFJKxrcz5XNm_Q13LxtEebLjgozSH1rfTgH0COsRM3nSLavjgSrt4dcGCMXHUiIlWs4vl9Saii7h7pFmHDOn1NzCfvawCCzF8-iS5u-OTqilYP1u_NkDuWrffXk-NnJzOEE4uSG0OM3ZB4EwyfVTmwH-8ObGqjlc2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
انقلابی در صنعت هوش مصنوعی
🔥
🔥
🔥
🔴
میدونی هوش مصنوعی ترند دنیاست و اینده ی اقتصاده ولی بلد نیستی ازش استفاده کنی و درامدزایی کنی؟
هوش مصنوعی TimeTrade این مشکلو حل کرده
✅
هرکسی با هرمقدار علمو دانشی میتونه ازین هوش مصنوعی استفاده کنه و با سیستم auto trade به صورت لایو و روزانه درامد داشته باشه
🔥
👇
https://t.me/+hcwmoHXpF6k5Y2Q0</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67262" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67261">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet @Vision_Bet @Vision_Bet @Vision_Bet</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67261" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67260">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ss2-ztcMxaUw95MqgSGfSNwaLGO5z0lh6_SqPWudguIH-Gv1iyNqJUj56jiZMugopD8KKgAEPwmVOOcpXATh7Z6Gw0dqfUAX45ROSjF8L6K_HHqDTrkWZyTEuHD8YEDYwoE8Qx7hvOcA6NLZTJHESPiDStwIMaCXtWeIpvbNo6xfUSZ6e6cfvaFdKtmhq6aGJHGYqvH7h4_5Mkrs97zwBxSl4ql6k0EzqvMzkqxFzMXCYqolBIzWzhcwvviAGSJF1tCXWgoNCrXEHmrmBuzTKiC8rw3qdJ1T0tFjTHpf_87cDvLyyCiH63f0Dk_Bj3ngF3J2efPE85ZnnHan7DL3Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67260" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67259">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل:
اسرائیل آماده است به صورت مستقل با جمهوری اسلامی وارد نبرد تمام عیار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67259" target="_blank">📅 00:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67258">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=VDAhd6Qr5WNFDlYMW_wKANHRnKxEk1eMDWr3useXlevX2UYfS-Fx18CIiAWcivUflLR-Qw-ksu9x-EIQOHEqoy13ac_4owLFTloGrE6weFj0lu9P13PL8s98l0jhhuBCriXyqSMuhiiB-wwPyUlvUBvSik5-981Wme--TfD1OI6Osa_FMTbHVmMwy4MAV87RboEmeu836oKZNvfShgoans3_qUBD7pyistt03MP39LLMda4sPz8uw8ODN4quz_BA9PM4ppkPw9YvJS4eo0L88g2HB04yZLu3mKmQfGTr33sPGX8sZZxfyk_WBLJv14xDimpU7VF1CYym4fQiexJLbZNmrf6uVOrjDdNJr5au8ep_T3mF0QvArmI004yjQMvhLwkF9KFlNR8ESu2UJ2gNm0YPVzpDhShdBCjgM1h34O4Iq4rap29jpy796EaocRVgmro33dF0Q0qUn_igETqlfy0W57uesVUacpm9kHe7fyO_SomKxTtFKbUpRSVF_WuExhFTkHmLZFTus_YQXrmaU5FuVCDHUK3p1wPMslIAglUHpHZopTRQuPcmZ9yB7oCpcPiRxzHoOk2RaGPLAeSbkedjER2x-ZiZ0T0eve05HjV13-gZhXXaMQhlnBloAoZa5RSJ4eQ_62TDaDbZ1Ad6h5n-iYeOOhfqzaXUslJLQFo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=VDAhd6Qr5WNFDlYMW_wKANHRnKxEk1eMDWr3useXlevX2UYfS-Fx18CIiAWcivUflLR-Qw-ksu9x-EIQOHEqoy13ac_4owLFTloGrE6weFj0lu9P13PL8s98l0jhhuBCriXyqSMuhiiB-wwPyUlvUBvSik5-981Wme--TfD1OI6Osa_FMTbHVmMwy4MAV87RboEmeu836oKZNvfShgoans3_qUBD7pyistt03MP39LLMda4sPz8uw8ODN4quz_BA9PM4ppkPw9YvJS4eo0L88g2HB04yZLu3mKmQfGTr33sPGX8sZZxfyk_WBLJv14xDimpU7VF1CYym4fQiexJLbZNmrf6uVOrjDdNJr5au8ep_T3mF0QvArmI004yjQMvhLwkF9KFlNR8ESu2UJ2gNm0YPVzpDhShdBCjgM1h34O4Iq4rap29jpy796EaocRVgmro33dF0Q0qUn_igETqlfy0W57uesVUacpm9kHe7fyO_SomKxTtFKbUpRSVF_WuExhFTkHmLZFTus_YQXrmaU5FuVCDHUK3p1wPMslIAglUHpHZopTRQuPcmZ9yB7oCpcPiRxzHoOk2RaGPLAeSbkedjER2x-ZiZ0T0eve05HjV13-gZhXXaMQhlnBloAoZa5RSJ4eQ_62TDaDbZ1Ad6h5n-iYeOOhfqzaXUslJLQFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
هواپیماهای اف-۵ و بمب‌افکن‌های بی-۲ بر فراز نمایشگاه بزرگ ایالتی آمریکا در حال پرواز هستند و جمعیت از پایین نظاره‌گر آنها هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67258" target="_blank">📅 00:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67257">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=RCDVtjqwimhsi5tcZiZxzzIuVrwaxYnZwikOObqh38kj-Qp8RoieHC-v-nNAPw52KystOnP28_e3PMpC8Qve2W_m9N-sx8PwDu8sqmB_m0-P4dFAY8ThkvVC-c5UmgH8n_Al3TVbbGz1YEqLDu8gcBp_kv2EZnSCgDFgaSPxKriqskAy5xaC4rgpDXmV7lRX5h_NvstAgRItM5m2gC_izp1JxUKgSUL5_s7rRZoVg_W1Aw4QOq19IvCQI1Tb4KApLNRazE4GZNIVA0v2ssNo4I6ZQ4HqTECJCzSQYWjCBL9mQJQblyDg5na0xUhqWWwXY4QYcTaKTZwEP8YUPuz3nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=RCDVtjqwimhsi5tcZiZxzzIuVrwaxYnZwikOObqh38kj-Qp8RoieHC-v-nNAPw52KystOnP28_e3PMpC8Qve2W_m9N-sx8PwDu8sqmB_m0-P4dFAY8ThkvVC-c5UmgH8n_Al3TVbbGz1YEqLDu8gcBp_kv2EZnSCgDFgaSPxKriqskAy5xaC4rgpDXmV7lRX5h_NvstAgRItM5m2gC_izp1JxUKgSUL5_s7rRZoVg_W1Aw4QOq19IvCQI1Tb4KApLNRazE4GZNIVA0v2ssNo4I6ZQ4HqTECJCzSQYWjCBL9mQJQblyDg5na0xUhqWWwXY4QYcTaKTZwEP8YUPuz3nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با هر ثانیه این ویدیو سوپرایز میشید
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/67257" target="_blank">📅 23:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67256">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=c-LU7L_Ktrcko-mTZq5nMPAtF8kWZK8spy112-zPck6XC0mN8wOAYafFcy_WWzVdErEKWWvfGwGNF7DU8rnWLHoOGvHuOsyNkuS7KT8EPBagOnM-VySXWugco0PaNbrzcRdTN-hhxMvR0Np8FqBEYpZZiZSXR1zvQLLak5vqWbZjVMdXcal7dHAtJK2jTbqxTO5HuNtDR7OGdkBIMssRQhJxh2MqR-erMO9ZyF0yj7Nm8QDVl_9hK83-Lk_f0rk6hp209HaF65aLM10iytHdMJ0c03irFKyQzws7y9CSYtCR09YjrY7oweeSYxTkMmBTVlr5AoTwsBteG4lCXcnJAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=c-LU7L_Ktrcko-mTZq5nMPAtF8kWZK8spy112-zPck6XC0mN8wOAYafFcy_WWzVdErEKWWvfGwGNF7DU8rnWLHoOGvHuOsyNkuS7KT8EPBagOnM-VySXWugco0PaNbrzcRdTN-hhxMvR0Np8FqBEYpZZiZSXR1zvQLLak5vqWbZjVMdXcal7dHAtJK2jTbqxTO5HuNtDR7OGdkBIMssRQhJxh2MqR-erMO9ZyF0yj7Nm8QDVl_9hK83-Lk_f0rk6hp209HaF65aLM10iytHdMJ0c03irFKyQzws7y9CSYtCR09YjrY7oweeSYxTkMmBTVlr5AoTwsBteG4lCXcnJAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عزاداری مجری آیت‌الله بی‌بی‌سی از سران حاضر تو مراسم تشییع خامنه‌ای بهتر بود
😂
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67256" target="_blank">📅 23:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67255">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=TPEIG7gPRCHOrvTKQyAYLghtFMQR7BbRjap7IoJ7wN0knaelQlp7P35tquh8VtTQ2JLTEQXkqnP7Pk7TrQp0LGMInuy9cLVtXk0ZFixqgNNfotwIYO04OqYeULDxiq5B0iRq7npS0Of5JHD7-KILLdmxbHOMphMShwQ2WAm-H-34AGfjS0Tk1mAjT4IdI6SXn2AZeDitoJxnafauisPAj3byYbX6t4s3pvqy-dFnhjGNsQs5IX84zFQYQ5HK_H5efFCxu1d0ZV7aNFCV9NMcNA0Q5byT4q2FEyOUC2RI1Pa3w5ifZVkxJtG-BoZY_om7GNWRtG05NQfOelNAQT1Asg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=TPEIG7gPRCHOrvTKQyAYLghtFMQR7BbRjap7IoJ7wN0knaelQlp7P35tquh8VtTQ2JLTEQXkqnP7Pk7TrQp0LGMInuy9cLVtXk0ZFixqgNNfotwIYO04OqYeULDxiq5B0iRq7npS0Of5JHD7-KILLdmxbHOMphMShwQ2WAm-H-34AGfjS0Tk1mAjT4IdI6SXn2AZeDitoJxnafauisPAj3byYbX6t4s3pvqy-dFnhjGNsQs5IX84zFQYQ5HK_H5efFCxu1d0ZV7aNFCV9NMcNA0Q5byT4q2FEyOUC2RI1Pa3w5ifZVkxJtG-BoZY_om7GNWRtG05NQfOelNAQT1Asg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر شلیک موشک‌های بالستیک آمریکا از کویت به سوی مواضع رژیم جمهوری
اسلامی
منتشر شد
ویدئوهای منتشرشده نشان می‌دهد نیروهای آمریکایی مستقر در کویت، موشک‌های دقیق ATACMS و PrSM را از سامانه‌های پرتابگر M142 HIMARS به سمت اهدافی در خاک تحت کنترل رژیم جمهوری اسلامی شلیک می‌کنند
.
بر اساس توضیحات منتشرشده، این تصاویر مربوط به ۲۸ فوریه ۲۰۲۶ است و بخشی از عملیات نظامی آمریکا علیه زیرساخت‌ها و مواضع رژیم جمهوری اسلامی را به نمایش می‌گذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67255" target="_blank">📅 22:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67254">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3720a35424.mp4?token=EZagwnbMuBK_Zc-kIFb7PAgxW9-ZgvIyVwhhscY7YxD_bsolySjB5TskSUHXSjLjU1CB6OCNCoz3WMhuZcZQOBiOt4OKikvJFsKq0brbIeq-vdXfUxmGeWDJVEa7joqcx4chD7gqbreFsbzPPag7jlqDhZtGsmZqImgX0W-aZE_ZXa41VFFCdjDFwMiZRPIUwzgxogGDMm-kE1nWvvsNulHawff1E8J_LjHQiRke25S-phiv1ynicHLk-bpzbkNBdIE1AUxV1RVSMpDAmFuNwZJPVgJjG29KU4vtV6828OaQjpkLhfpoQh2OfnVXTyGNqDI2MacRBWDDcrsas92bIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3720a35424.mp4?token=EZagwnbMuBK_Zc-kIFb7PAgxW9-ZgvIyVwhhscY7YxD_bsolySjB5TskSUHXSjLjU1CB6OCNCoz3WMhuZcZQOBiOt4OKikvJFsKq0brbIeq-vdXfUxmGeWDJVEa7joqcx4chD7gqbreFsbzPPag7jlqDhZtGsmZqImgX0W-aZE_ZXa41VFFCdjDFwMiZRPIUwzgxogGDMm-kE1nWvvsNulHawff1E8J_LjHQiRke25S-phiv1ynicHLk-bpzbkNBdIE1AUxV1RVSMpDAmFuNwZJPVgJjG29KU4vtV6828OaQjpkLhfpoQh2OfnVXTyGNqDI2MacRBWDDcrsas92bIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ورود خودروی حامل‌ جنازه علی خامنه‌ای به‌مصلی تهران
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67254" target="_blank">📅 22:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67253">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1HqFv30g6ae0R-6hp49F3CpuYEZSA1Ef46302wNeRfwQoYuAA7VCyTAx5N6dPpc5yI4iDSxPVtCJZzh5dPIYDeNihO3yWE_d0dHql-3f75xxzya3U5EE6nAaXm70ZfqDYQMMnl56w3dMTbU83gvyPjPkpNZx8j8gCFbKMqTjetOjKpmrciwTyyUzPBYxZmqD9SmBsq4d-_XtajIY2x9uQw5dK4-7uPyRiP0zUNtzqGS1_HZqt4KNXFn3UViBsj5JZxXNfth_Gx2arSNBbug846StbCR9TWCwCLkzpGbwIp_VxBPEqC3IXYMLubRM-PPaZugNQR4ivLBIiseBkkxDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سید مجید نقطه زن فرمانده هوافضای سپاه هم بالاخره از سوراخ اومد بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67253" target="_blank">📅 21:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67252">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jiyZL_D7vxZM-inRrSdtwZjMLWurxSktDzYZZf3aq2gMfxD6nfJnLtQudZWDxepBUh1B0-bk02ehllMmf5T2rp0FvmudmBMTx6uCdZmnXSfRqzNFyYZAgRimkHimtKP3Ckef4Pn47n45e28f5_n2Ra92zW7Tik7Fy7VQggX7JQ2aPxBVLfYXhhOnFJS_Ue42oVeKyMD-SF3qFGIdgxwNefI3SNagPBJGP0elc-zmYRr_wvPn7uVCZBk4ghaMMjXARgrDHRpjKbr8Lk7H0o0GxRJgzql2n68q4aK-B0AwpfVI0zhILyphiFtWdVY-2qH4kuSirWSuP3uwY6DgUhfJRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ: ۵۸ میلیون بشکه نفت و میعانات رژیم روی آب مانده است.
حدود ۵۸ میلیون بشکه نفت و میعانات متعلق به رژیم تروریستی جمهوری اسلامی روی آب انباشته شده و نزدیک به ۹۰ درصد این محموله‌ها هنوز مشتری یا مقصد نهایی مشخصی ندارند.
بر اساس این گزارش، با وجود تعلیق ۶۰ روزه بخشی از تحریم‌های آمریکا، خریداران بزرگ همچنان با احتیاط عمل می‌کنند و خرید نفت از رژیم جمهوری اسلامی محدود مانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67252" target="_blank">📅 21:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67251">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR8pfhgN_wGxZCA_1zJBhoA0GPFa63kp3QKXOlZzzy3keVX4rUK6sJ0VnhfCBRYXNEVMr-dTMJY3GPNkPsdsO48nJOpyoxskCHfYWSpAVx6Hp0_BdLHwgs-EMwKfoo9_GxVIU06foXtAIEJvV2HqvDf2dhXZu986nFL4RgrIKInL_A1vY-_qgcxixSyEue7mpeY5shMf9DVk8p-_HRd4zWMA8i7bGSlBrapjDN7hFokwF01OgUhe1VeprBIsRfOtlLCkia3VE_JwkSp1wpOtaq4UN_ngSQn5_l1xoCTqqEiAnJyaxuBn4N_PZI5PC7EslD_qg82gWaNODBr42I5TYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
نگاه معنادار عراقچی به قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67251" target="_blank">📅 20:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67250">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9ajuIKuWRrrdV_u5Y6DXQFSgdVvG_QUVeoJ8Hqvisupa_MhYmBhjcItjm1gc2YZyimfkQ9JhwyGl2DZ3ezhr-LUeGLP_uHdFB6fk9WHTmJB3lwVOss-bi3hRhsHKyxppz8L0BgKEQoKhSQ5F-EVPWWD-c7bgny730c5HZl-_KDreqvc6mO1nRe6HllPoARB3fvXSwz6XKVTqZ7_jw7OXKdOEF5sEAPm-DXKZLYUKqjuodJizc7VOBeAX2L7-IqC1SMWLhZlB93iFcYYEc-dlCQz0FRrmw0MFGG-MSyYvqLY9amUX5QuhRZ-KeRpe9C9f09uwpehVopDHzNkyYPlQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید (آکسیوس):
رئیس‌جمهور ترامپ امروز با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، گفتگو کرد. دفتر نخست‌وزیر اسرائیل اعلام کرد که آن‌ها توافق کردند به‌زودی در ایالات متحده با یکدیگر دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67250" target="_blank">📅 20:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67249">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwUvT-MZ3fK1xFp9zP695EFmnY-kTS26-Cb2BAebcrAn8bTu3xJAFg4PQ6O8oh2trm9YrJEWLFeLUsSEK5_ay7GTBryvfH_cAH7G3E2BIgoUbpqHxnflo3ewJEjtzPUQ6rGIsQKjHSG_6Alb5tfbNnLV-bneBLSWWCV1qhPACMy3XYHMKis84Ku80YY_DYF339szho3zlTDIj_PLv5YnqJF618CDSd0VvVTKVtJ7_R8C6vyS5xrVq8G1eKh9bT3qCkF-DsYFF04UeTvR4Tr7uaO0zBrVDj4meqA7aPCRpBBp5XJ_9TGydtaylisXT54xA1pOjrK1XTxqNxGNpGTF8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
😆
‏سی تی اسکن از دندون عقلم:
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67249" target="_blank">📅 19:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67248">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kl7m8kylU8U45EpS0P7Bs-PDyHIOVVRwTKz2Nb3eVBDZDHxYrFySI3SPMwKA9oy3ErhgXYAVotZHzMFaCnUQWsqQLqFIgyXQcsVNHcxkxPZACIDMMCpGtrcDY2w4GaDhW3UHXKtbs5VR-ZZfm4eODI3QfG0XWW7PAI2hih0BovE5b_fUp9fftSHzO3JRnDBklDYSg86iZpl-M9H-g7zoYcIBiXozlJozX3k-HNyEucp2U7fmOubKv99bXIu94G9W6kjU7eFkPHAxeIE0RQN0hOZIqqJzrWkuM2vX2-rhrQFeqVVrmJWY2vUeVmPmSRTcZN-eX4-BGrCzbXh7fBTM4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دفتر نخست‌وزیر اسرائیل؛
گزارش نیویورک تایمز را که حاکی از آن بود مقامات آمریکایی معتقد بودند اسرائیل در حال توطئه‌ای برای ترور مذاکره‌کنندگان ایرانی در جریان مذاکرات با آمریکایی‌ها در بهار امسال بوده‌اند، رد کرد و آن را «یک تحریف کامل از واقعیت» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67248" target="_blank">📅 19:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67247">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=emRuE4T_87qCfE5arnmbGU6uTpOzPhi_xOLgHwh87ygpH9uB2GDy1AvjahRw97K9by1gqtf4-IFBDAyTITjorXCgcn8O8qIN-5r2Dr9KuRV4JQVvSDl9GMNZ4hztEdAl11-4s3NsshWSjAEvwH3q9USZvDY06zutzdz3BEjxb6rAFzOIzcYP5pHS9jC8v-dQGendtetFfj_l16kvbZeSctjiWdhkgCx9p_wBB4KwN853nk3vS445fBtxW83ca-O-4dC6DYk545BnswVuHSHMXO4i8nJn7qoHZ5jsmiQJ8mEleqmoEKuSLaboLLWkVAUC7xY8LmPi7bPwJoOUXMXKUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=emRuE4T_87qCfE5arnmbGU6uTpOzPhi_xOLgHwh87ygpH9uB2GDy1AvjahRw97K9by1gqtf4-IFBDAyTITjorXCgcn8O8qIN-5r2Dr9KuRV4JQVvSDl9GMNZ4hztEdAl11-4s3NsshWSjAEvwH3q9USZvDY06zutzdz3BEjxb6rAFzOIzcYP5pHS9jC8v-dQGendtetFfj_l16kvbZeSctjiWdhkgCx9p_wBB4KwN853nk3vS445fBtxW83ca-O-4dC6DYk545BnswVuHSHMXO4i8nJn7qoHZ5jsmiQJ8mEleqmoEKuSLaboLLWkVAUC7xY8LmPi7bPwJoOUXMXKUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه بمباران بیت رهبری 9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67247" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67246">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/H7SkNK9KvMU1ZsOq252DH0YHPQJ6dLpEvhEz8RrjOVV86767Ficf7GXtY1sX-bPi0CkoskBiXsIZcz7-Qn9oUKNLjX0ZmNUCu88JMCf3cH3f954NOdN6cDtg92fBcTN8ucTzHYxGqgUTLCeFKYnQRbBTUpo9kCHobKvCUJN0hU-gXaX_mb9KfYKsZM1U4PizLFv2s9Cmlxf4cHn5WGxaRLdXtN01XdCPObJbaL1Ep9rjCUAuwOuWdura5GbAo4Ydp-bXELIYIcjgSxFvgz3433wRexiz6rYNb-QpcSS1wJG4GgZNEGzUUXcpvVIF1pAYVrWIncqTuaEO22MvsBs7oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67246" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67245">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=kgdzKxTRF4vRWWqTAIXAuGf-QlBTZBjvDezMCWmk2eY7RHSVuB6_pS0qn_IY4UNp5wxiSwDuCjcI4hF1-VnWxZBcXtnI6iaR-Z__nl53z_ylpI-M8xVyWVrhNyBAY33rYzLTnK9C_CVFRkH7Lhy3xdDGSmq3b1CeNYVuvK153E0rrjORH9rZV5SLSkxd1QnqU--SidL0CZ2vdkmYYQy3J8_8jvCB0TEMRu8dXroVSHnqotto_Wp-Iku4NxfmmyemriAVmTdEmbsM_eWhluYEVlTsmtllHPn19th1fL90tLBrTkCbV0wTAYLeXu4AtUB7_xoyjZO80wkNQ6jiBDHLkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=kgdzKxTRF4vRWWqTAIXAuGf-QlBTZBjvDezMCWmk2eY7RHSVuB6_pS0qn_IY4UNp5wxiSwDuCjcI4hF1-VnWxZBcXtnI6iaR-Z__nl53z_ylpI-M8xVyWVrhNyBAY33rYzLTnK9C_CVFRkH7Lhy3xdDGSmq3b1CeNYVuvK153E0rrjORH9rZV5SLSkxd1QnqU--SidL0CZ2vdkmYYQy3J8_8jvCB0TEMRu8dXroVSHnqotto_Wp-Iku4NxfmmyemriAVmTdEmbsM_eWhluYEVlTsmtllHPn19th1fL90tLBrTkCbV0wTAYLeXu4AtUB7_xoyjZO80wkNQ6jiBDHLkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بغض و گریه های تمام نشدنی قالیباف در مراسم وداع با علی خامنه ای:
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67245" target="_blank">📅 19:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67244">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=tf049Hj-Ic4_4XCMNKvs6wpyyMtC_gWcw6x-gKSRfRDD1ZgP6v51rhnwTBQJwlchPNceFReTjOP2RJyB6yLR_4eD6HL2UxvMmR4ddEdx8Wm0iel7kbOtCH5hZdtkijjKAX5w4F2TG6f6gl71f_oSwmaKAsF1Ghk8u4OsOFLUHM5O8kWbvRxQQQ_5iFYnu6_nGtPhf2ZXU-4bw3nv0oesNust73EhR5vR8Ver4T1P6Q_t99O_7AZzmEapmUovz2T63-yY_bCC1UgdbzTYxU4q8EMPUcSn2PI4F0zLWGyLPxYzWwDqwKADxhD0YHoV-SndHz_18qB9EGzG5YVJT9EPZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=tf049Hj-Ic4_4XCMNKvs6wpyyMtC_gWcw6x-gKSRfRDD1ZgP6v51rhnwTBQJwlchPNceFReTjOP2RJyB6yLR_4eD6HL2UxvMmR4ddEdx8Wm0iel7kbOtCH5hZdtkijjKAX5w4F2TG6f6gl71f_oSwmaKAsF1Ghk8u4OsOFLUHM5O8kWbvRxQQQ_5iFYnu6_nGtPhf2ZXU-4bw3nv0oesNust73EhR5vR8Ver4T1P6Q_t99O_7AZzmEapmUovz2T63-yY_bCC1UgdbzTYxU4q8EMPUcSn2PI4F0zLWGyLPxYzWwDqwKADxhD0YHoV-SndHz_18qB9EGzG5YVJT9EPZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد سردِ حدادعادل ( پدرزن مجتبی خامنه‌ای ) با عراقچی و قالیباف
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67244" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67243">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=UFVTu2XzrC6qKa8CewDC3EZQudUvMiHeTqlWGr9AqFqVJCogKC8gVQvroGIZQCjQxjNTm0j44DtjsqH-rQBvkwkJR9aKzewSELsFn3MIOrfUx_CE3bZ2IcDuH_pheUqULqCOMhYkee_kgJlsuWz2ADaVuxejakZr5GmvrK7Fxta7mqp_RSYDFZ8NyKUkZwjy5d9uMtc-SO6_iV44xBfirQNNyvexEq_G_V-Ig1qCLNFR7nV6PbNXFvjm7Y0Z2tarq8pQc94-QZuvVzbVvmLkXi4CeSsBg9XEylnMCSgLtnx_nJSe6tsw6RG737e-7l4-0Ov8BeSFnVzvd3oewMXgWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=UFVTu2XzrC6qKa8CewDC3EZQudUvMiHeTqlWGr9AqFqVJCogKC8gVQvroGIZQCjQxjNTm0j44DtjsqH-rQBvkwkJR9aKzewSELsFn3MIOrfUx_CE3bZ2IcDuH_pheUqULqCOMhYkee_kgJlsuWz2ADaVuxejakZr5GmvrK7Fxta7mqp_RSYDFZ8NyKUkZwjy5d9uMtc-SO6_iV44xBfirQNNyvexEq_G_V-Ig1qCLNFR7nV6PbNXFvjm7Y0Z2tarq8pQc94-QZuvVzbVvmLkXi4CeSsBg9XEylnMCSgLtnx_nJSe6tsw6RG737e-7l4-0Ov8BeSFnVzvd3oewMXgWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپی قدیمی مربوط به انتخابات ۸۴
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67243" target="_blank">📅 18:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67242">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBzWpwMn2_TS85vIG3dlIPk591fgtCH_DtBOw8kAODyHJ3zWYyl297gWRosrE0pJh-_ctrXK_417IUAbQpnMBs-qn4fTD4CQrTAPOeMzfzoPKQ4mg84RMStW6s2TCEI-iUcgz9At0aUtUDRzUrwJ6b80VJnE9-g7ORqC7hjzQI0oVHzSP3hAA0-4zw7PjAGQi4jQvtqatfsL9IVkKeaYHPx3NVN6fKuun3dO9OKQe3G6CsJlQa0Fgs0CwP5rUMcBcCwP-LvaqwMANpT1y8Y2UPjIjDI4U1rRgaOdkb6v-2OPbKHZzPCSypsA07v14kdWpyQdEN1GRY-MLavE5YQVDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهره خوشحال پزشکیان در استقبال از مقامات کشورها
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67242" target="_blank">📅 17:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67241">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=p-SeMh3j1_XMFtW-gVpqBgeRZUXMQ5T1KE3Iep8qBKUPcEwGef1SML50euokoKeaeCKaD6GDQHAAVZ6Q9vRRpLtc5IEPA73odSZfUzIaqJ6eQkiDvVaRKAMQwy238H437pNADL7rOUzSh7yri74OCtu_EeGVJBHSmHVsvARN24iAVzUpUxGRymnelPqFhWc8fMNGvPCSNjhuup5bIAY-BqY-ahjNJSA4emNRtNzmf_hMhyET-bfMGq3V22ypeJtmEb5-HSkvZ6fLS5VrqdzSGLRrMPrraM3jKxKWaf2mpWrBQDVEjmgKTreB4wls5NzUXYtwWNsd5MleG3bGBvuzQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=p-SeMh3j1_XMFtW-gVpqBgeRZUXMQ5T1KE3Iep8qBKUPcEwGef1SML50euokoKeaeCKaD6GDQHAAVZ6Q9vRRpLtc5IEPA73odSZfUzIaqJ6eQkiDvVaRKAMQwy238H437pNADL7rOUzSh7yri74OCtu_EeGVJBHSmHVsvARN24iAVzUpUxGRymnelPqFhWc8fMNGvPCSNjhuup5bIAY-BqY-ahjNJSA4emNRtNzmf_hMhyET-bfMGq3V22ypeJtmEb5-HSkvZ6fLS5VrqdzSGLRrMPrraM3jKxKWaf2mpWrBQDVEjmgKTreB4wls5NzUXYtwWNsd5MleG3bGBvuzQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان در تلاش برای جاری شدن قطره ای اشک از چشمانش
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67241" target="_blank">📅 17:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67240">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=QBX5sonnnK7fLJ8q0OD5XJGyV1nc8dcJ2GtJh1tjiohZ2N8MJXlchuf2i7d1x-xIBf-RjzIEgHg3F5uuBL0ZjsR_V2hVcVsVpqMhc2kZTHWHtvdrt4WcO72olOjqlEwWTI--agwC2mwCO-huBw8qHyT-UZs6kIlfV_MteIqMHpt4v6y05PzvLbLSxffr2C8zUIJ20KwxMAgzEXQ3gudGstGSbcunr6_wJK7Ojucm0kXjVX98uZMCbbe8L8Vz_hnEIt74P9lCszJsA_-Vv6LV2paFJsoG3nLtsqQvBoRGjoKxnSQ1Q34ogX1LaSxN2OuwS737wmRKSaxawEvJ-UCw3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=QBX5sonnnK7fLJ8q0OD5XJGyV1nc8dcJ2GtJh1tjiohZ2N8MJXlchuf2i7d1x-xIBf-RjzIEgHg3F5uuBL0ZjsR_V2hVcVsVpqMhc2kZTHWHtvdrt4WcO72olOjqlEwWTI--agwC2mwCO-huBw8qHyT-UZs6kIlfV_MteIqMHpt4v6y05PzvLbLSxffr2C8zUIJ20KwxMAgzEXQ3gudGstGSbcunr6_wJK7Ojucm0kXjVX98uZMCbbe8L8Vz_hnEIt74P9lCszJsA_-Vv6LV2paFJsoG3nLtsqQvBoRGjoKxnSQ1Q34ogX1LaSxN2OuwS737wmRKSaxawEvJ-UCw3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در یک سو مردمی که در زباله‌‌ها باید دنبال غذا بگردند و در سوی دیگر «تامین ۱۲ هزار تن کالای اساسی برای تشییع قاتل فرزندان ایران زمین و عامل شماره یک تمامی مصیبتهای مردم ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67240" target="_blank">📅 16:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67238">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=td2o8BhNl4PE9OvL-kMv8Q2-wRWpWEB5G7ugmvLFXM3dPNe_ToaQgrj9tHmym2lYclk_f-A_xRPT7bvpmIpd5RSZVtJ-q7TPbsAeQXCV_6W6CudBytVjnomEj1tlVgd7Yp1BjXynv6iLN5L6KRlhGO8shYq7Pf1K-tjIBSFziJ2m2Uz2P3k3cj2UBq8r9Mn5QASxHwqPDYlgPuAmqKObWgjHaZpTvoDUoVIskTtw_FX6PZ7V_cd0dtOL8T4c6VMVxZeN3QiPDqGdEZAj5yy3I4GxxqiMhFI40oCrphof1zoMjWIii0xPMhwEq_Ga4H2mvFwqd7Ow0LOHe-wQDNh8Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=td2o8BhNl4PE9OvL-kMv8Q2-wRWpWEB5G7ugmvLFXM3dPNe_ToaQgrj9tHmym2lYclk_f-A_xRPT7bvpmIpd5RSZVtJ-q7TPbsAeQXCV_6W6CudBytVjnomEj1tlVgd7Yp1BjXynv6iLN5L6KRlhGO8shYq7Pf1K-tjIBSFziJ2m2Uz2P3k3cj2UBq8r9Mn5QASxHwqPDYlgPuAmqKObWgjHaZpTvoDUoVIskTtw_FX6PZ7V_cd0dtOL8T4c6VMVxZeN3QiPDqGdEZAj5yy3I4GxxqiMhFI40oCrphof1zoMjWIii0xPMhwEq_Ga4H2mvFwqd7Ow0LOHe-wQDNh8Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ارتش دفاعی اسرائیل:‏در واکنش به آسیب واردشده به نیروهای ارتش اسرائیل و در پی نقض توافق آتش بس: حدود ۱۰ زیرساخت سازمان تروریستی حزب‌الله در جنوب لبنان هدف حمله قرار گرفت
🔴
در حمله‌ای دیگر برای رفع تهدید: نیروهای لشکر ۹۱ یک کامیون مورد استفاده حزب‌الله برای انتقال تسلیحات را هدف قرار دادند
🔴
در حملات دقیق نیروی هوایی با هدایت لشکر ۹۱، روز گذشته (پنج‌شنبه) حدود ۱۰ زیرساخت متعلق به سازمان تروریستی حزب‌الله در مناطق بنت جبیل، بیت یاحون، کونین و براشیت در جنوب لبنان هدف حمله قرار گرفت. زیرساخت‌های هدف قرارگرفته توسط این سازمان برای پیشبرد طرح‌های تروریستی علیه نیروهای ارتش اسرائیل که در منطقه امنیتی فعالیت می‌کنند، مورد استفاده قرار می‌گرفتند.
🔴
این حملات در واکنش به آسیب واردشده به نیروهای ما در منطقه امنیتی توسط سازمان تروریستی حزب‌الله و در پی نقض مجدد توافق آتش بس انجام شد.
🔴
همچنین بامداد امروز (جمعه)، نیروهای لشکر ۹۱ یک گروه از تروریست‌های وابسته به سازمان تروریستی حزب‌الله را که در نزدیکی منطقه امنیتی در جنوب لبنان، در حال انتقال تسلیحات با استفاده از یک کامیون بودند، شناسایی کردند. بلافاصله پس از شناسایی، نیروی هوایی برای رفع تهدید علیه نیروهای ما، این کامیون را هدف حمله قرار داد.
🔴
در پی این حمله، انفجارهای ثانویه شناسایی شد که نشان‌دهنده وجود تسلیحات در داخل کامیون بود.
🔴
ارتش اسرائیل به فعالیت برای رفع هرگونه تهدید علیه نیروهای خود و شهروندان اسرائیل ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67238" target="_blank">📅 16:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67237">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYMpGCRuIIIAjoanrmU1RlAehRxsMKT9tlw40Inwa3pwkmC_UhqjDRTBqWAgw8h5rVSHR3o2fUd26XZGQgAbPVmE3268mbfhL98PxyYAdWiKaz2mmSocmz5ShQVh91u0qcfMZZ5FEcM0Wdkizo7_hqKUhGtQbkIGpmYVQTBIfJMFFaxlmazc7P_-sP1vsfUqA2WmsgvuI7ZTmw0uKF_XptryyEVK98lxSxCiLSZbgPkJVSDBVp5ZjB23Tvh3lglUlw86C1EXX9H5L9UTDl05P_Sd_a4rtG3mqfbfrChprPKG07glnjNeqpVW7vSkwyjJJmVeZAiBS805d7gNyROzUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
پنج فروند بوئینگ ۷۷۷ سعودی سابق علیرغم تحریم‌ها به ماهان ایر تحویل داده شد:
پنج فروند هواپیمای پهن‌پیکر بوئینگ ۷۷۷-۲۶۸ER دست دوم از خطوط هوایی عربستان سعودی به ماهان ایر ایران تحویل داده شده است که دو فروند از آنها در فرودگاه مهرآباد تهران تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67237" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67235">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXVuqJiewdXm4G8egwobNfQLJ6sedUukIDNTgdzI_rkUfuzpJ_xCf57Sk3jAXSRRvv1N999IAw05jeJDcWrE3Yw-9avjdvY4ooynoQ_ijxf8hGL-6jzZSXHjSR1gO4IYDNNH7TGYI655plTtJ6x54yoBCEdg67iUvg0PWsqoErzDXlf_aMTBXXFboUkPnuGB58lGuqL3nD5igN9QstxV7-E6nK1YZkqv-ME7VJZx_rMGXvdDu5vn6KOvuw078zXFl-AikU9ExvdFyX9t4Kh6faQKE4ZKRUKtweGY_h1bRi02x6dqgfN-w4JMUUC3Q7GcoovtPiPpMxSIiMHr1Hqv-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=dtYs03T_bCPaUpcpU-1oTsNtHYLJ3KGC3LvkGJCxCRscS5WSZGRbvGwT1DZfH8r9zO4NRTERr_DCB85v1OXnCYa3zVTZni3cwWthqE6flH79-ivQXFLWJ4CtVOSBddCFbX2poZ_gsKj8huyXT9U5RSYOWOPOyxEkDyRMN0Hg-Q0iZbslu4mMXv1azZEJ4_r9lz2_mTFOIKTyC4F2PTwU5Kl1jBL7CstpDzoPocjGLRfh5p9q4pgOKOM4Jx3_01n4GzQ6ZEox7rQwE8RDPOic1mMJJGB6dFgQGtxMeRFdQ45oaPKTxu6ZBJAL_Nq7APD9KwyABbt-X8LiBbmFsNj8bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=dtYs03T_bCPaUpcpU-1oTsNtHYLJ3KGC3LvkGJCxCRscS5WSZGRbvGwT1DZfH8r9zO4NRTERr_DCB85v1OXnCYa3zVTZni3cwWthqE6flH79-ivQXFLWJ4CtVOSBddCFbX2poZ_gsKj8huyXT9U5RSYOWOPOyxEkDyRMN0Hg-Q0iZbslu4mMXv1azZEJ4_r9lz2_mTFOIKTyC4F2PTwU5Kl1jBL7CstpDzoPocjGLRfh5p9q4pgOKOM4Jx3_01n4GzQ6ZEox7rQwE8RDPOic1mMJJGB6dFgQGtxMeRFdQ45oaPKTxu6ZBJAL_Nq7APD9KwyABbt-X8LiBbmFsNj8bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بر اساس گزارش‌های اولیه، جنگنده های عربستان بر فراز صنعا، پایتخت تحت کنترل حوثی ها، به پرواز درآمده و مواضع این گروه در نقاطی از یمن هدف بمباران قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67235" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67234">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RSGgt6wLXUzH-wlta4Ja0NnSGNdI21o-tnFOO-bccShRyZZGi0rPhKLar9JpZ6qa5L7nhzW60bm5hszh4im9X6PMf75dhTarZHY1_-Tg2c5B1FsKbFHfdzn8QbLJP-tksXI_KH_9Ft67xRBJ4TKLHSugyjERYwdBWniboNZRacvVpsinZf4zWH5339MjXz227X1L0ATIOQIT8ePmkeV2qKqYNkJ7qX52ZvfgKl8qBSoy3OGxzz4hEOEpH4C9TGUYVuOR0w5nPi95B5P3ypub35DL1tUnS42Ni93ujkqXzBb0RY23-BSduX8kWfKd5Dn0WCNgC7VIKUDnMm547NmhWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این عکس از تفاوت تابوت محمدرضا شاه پهلوی و علی‌ خامنه‌ای وایرال شده، تابوت شاه کاملا ایرانی و تابوت خامنه‌ای شکل و ظاهر عربی داره.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67234" target="_blank">📅 14:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67233">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=YbhjTIdltbdg0k4k9sDaoe1ECaRg2s7Kocy08zo8Eq4W1A9uRzdi2JrWV9J93O_uy4g1M1Q3GKhUVSdRXrCnS5orHUf2LA5Rk9CSdfccC6CYaJVlPsktd2WdZjF9Ch6ImP178wO87RUYR0Kk2QkGD14my4U5HTAwPBhqDUPRPZuFT39_WeWps7KocetPVrp_CM0-UUUtf1QbOjihwBX2iN_PnIeciyl-pkOohegMndTW5gGuu3mZv8G03TH2Rhbyfi85dXvPCxGJERcQZJ3P8MkgCmNfIVhS8D8ePTlU3yFuXlvmoCqfO74mC58-CpdF4jmjg1RYLdF4JLb-DUGlag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=YbhjTIdltbdg0k4k9sDaoe1ECaRg2s7Kocy08zo8Eq4W1A9uRzdi2JrWV9J93O_uy4g1M1Q3GKhUVSdRXrCnS5orHUf2LA5Rk9CSdfccC6CYaJVlPsktd2WdZjF9Ch6ImP178wO87RUYR0Kk2QkGD14my4U5HTAwPBhqDUPRPZuFT39_WeWps7KocetPVrp_CM0-UUUtf1QbOjihwBX2iN_PnIeciyl-pkOohegMndTW5gGuu3mZv8G03TH2Rhbyfi85dXvPCxGJERcQZJ3P8MkgCmNfIVhS8D8ePTlU3yFuXlvmoCqfO74mC58-CpdF4jmjg1RYLdF4JLb-DUGlag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حضور فرماندهان ارشد نیروهای مسلح جمهوری اسلامی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67233" target="_blank">📅 14:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67231">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CX2edDPH575B4I3gwsy74QDwvNBw_9WMlvZ5m2PYA4bPcDDLz2kIthZrQrXcwXqfyApS84lLIat-3iSzD8TskUA_12v-oBawdHXUUn1jcCMaFs5OFLQ1x2vKTsSvYA3W1D7diYMJHuAA4M5w9iUQkd6h9ZZgWhiWgMahR3ysgyjSSXNYEpdSoaAk5ccTzw9KP-r6v_2qc9Juw3oOjYLDvSCZrGWNUvgmX29O7Kd9VGrn3BZIgZmgsnHuCJqkqr39thykWPTbBPTkEpiK4RQ9Hq2Ryo77de84D-wFetFAdI2uSMWUjYTjIdaBzz8QYl7D6eNsbKmnRUCKyrJ0DgVDnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=rkuos7QQCr6F_euJfFi2gBSSe0_VTf9MgC-cEfTIsJZniADAU4sPpQHe_egrcQjbjqxMfzVqKPcGnU3HpwbGb2yng8lVI-oWlM61jWTz9do6FtyoLwGjLGv9YLXbuGbTmgdOEGsWAiLF_F-2gBPgG0F28NIZauEcN0N9sBpxbQ2j-FeR7iQ7w3EZpI0qn_GbkpxYBfON-uqAZPvTW9oDZgwh0MfsZmCe55JPCp3l9gcygwVWfB-p-ztDtPuTKGpQRBeoJbYuUQVaVWrl_5rZlb_z7dm0XB6x-1qbMoVGbBa43TZHjdfzPI8wmcvmT09OR0jCuL-Rx7I-z8DNhFiluw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=rkuos7QQCr6F_euJfFi2gBSSe0_VTf9MgC-cEfTIsJZniADAU4sPpQHe_egrcQjbjqxMfzVqKPcGnU3HpwbGb2yng8lVI-oWlM61jWTz9do6FtyoLwGjLGv9YLXbuGbTmgdOEGsWAiLF_F-2gBPgG0F28NIZauEcN0N9sBpxbQ2j-FeR7iQ7w3EZpI0qn_GbkpxYBfON-uqAZPvTW9oDZgwh0MfsZmCe55JPCp3l9gcygwVWfB-p-ztDtPuTKGpQRBeoJbYuUQVaVWrl_5rZlb_z7dm0XB6x-1qbMoVGbBa43TZHjdfzPI8wmcvmT09OR0jCuL-Rx7I-z8DNhFiluw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس حوزه انرژی: تنگه هرمز از مسیر عمانی، اتوبان شد!
این فیلم از موسسه کپلر را ببینید،
چقدر تلخ است، کشتی‌ها و نفتکش‌ها در تعداد بالا از مسیر عمانی از تنگه هرمز عبور کرده و همچنان می‌کنند.
با این روند، به زودی ترامپ بابت تامین امنیت کشتی‌ها از مسیر عمانی، عوارض هم می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67231" target="_blank">📅 13:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67229">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fa301248.mp4?token=pNWaL3UURjEGvZKOAQGltBt6dSB_-cITcbeX3SEyF6KWF0-647toLUSsX2qTDdR7Iiekj-4XmPa3etgyX_plTRNPihn8_nCStR2DZo3-VcCX-EP9MlETig3o22NJfaxtQ_A_35NVwgfosvxnNEqp57dGIZCqkRXztDAhCiYCbShJ4psCGwfjcNDyvJmbgMtF8iLrfekVau3uvkMWUCYbRa5yQg9W0TxKSHNcKcsLWu3ZLEmAjuYcTSGslM2-5GUutRanc1-3N5-ns7p3OtusSyXA4VebAqcDh-Q3CJ0IO1DjXNKrnot3e6EjC-lzx65tyVBGCqB9qMHZtH_Y59r7Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fa301248.mp4?token=pNWaL3UURjEGvZKOAQGltBt6dSB_-cITcbeX3SEyF6KWF0-647toLUSsX2qTDdR7Iiekj-4XmPa3etgyX_plTRNPihn8_nCStR2DZo3-VcCX-EP9MlETig3o22NJfaxtQ_A_35NVwgfosvxnNEqp57dGIZCqkRXztDAhCiYCbShJ4psCGwfjcNDyvJmbgMtF8iLrfekVau3uvkMWUCYbRa5yQg9W0TxKSHNcKcsLWu3ZLEmAjuYcTSGslM2-5GUutRanc1-3N5-ns7p3OtusSyXA4VebAqcDh-Q3CJ0IO1DjXNKrnot3e6EjC-lzx65tyVBGCqB9qMHZtH_Y59r7Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پالایشگاه کلیدی لوک‌اویل در روسیه هدف حمله اوکراین قرار گرفت!
این تاسیسات سالانه حدود ۱۷ میلیون تن نفت خام را فرآوری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67229" target="_blank">📅 12:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67228">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7iOb1ENKbyIOCDfSga7HQ2i3OTlRspsu4Dr27-nQyLuxDQKsFJzw67IaYRZzFHkbwnAfZ4wfWhgll1TC5-2KYfTXp_-KtQWeD5RenLHyJ8LsHFRXOLhhIhrs6PxT2CJbHKDS7SsjDFnmW8nlI86BYDzEo5xf7m2rRsya2INMBONpTcD-kXA3G-6643hOehawFdChJVXEc7e3RBUxoYP69RtgzGWp_IEKamMnsr8jtzxdhYzTCT7NfifMk78gAybU58rZGyCjsE-DXrSOx6TEUPSvDNCqagNIvKtBopIL0DflhWVt25kGNoBa2vAAqAVWLt93e_y9qmYAcSmg6fcOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
همان‌طور که ترامپ درباره درخواست ایرانی‌ها برای برگزاری جلسه در دوحه دروغ گفت، دیشب نیز دوباره دروغ گفت؛ این بار درباره حمله به تأسیسات راداری ایران. نه جلسه‌ای در دوحه برگزار شد و نه حمله‌ای به ایران صورت گرفت. هرگونه حمله‌ای از این دست، با پاسخی کوبنده مواجه می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67228" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67227">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gh4JrVhUt0XgvEMazpH1jt3MJw3gG8Oc-EmSrysNEObLa4czV3DjsAsCckCYCKvdj0qkbWILms8SbrxDgSaN1_G7l431vAddF06vAZUikVAOxwgB40PYpD1E6wfP3w7tlOiaUNHrbglmEBpBJtzHufCKWF3HKrQ8PK4Vi8dAdTaQAxO7c0YJz_V4vk72W0hroc_WQbqaWUS1Zh9LSfuffmRYdcJOCLLKz9ZtSlDb5-oMwfv5sVO3UAQZRFo4HdBbU2sMJu1B26-TwlCev_XQSoFC3B2aHg33e6XT5PFmQw31rUKnBOPgrV0Gq8ImxafNKgEETlgeJMnnwhTOF6VMOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی طلات رو روی ۱۶,۹۰۰ فروختی و توی یک روز،
قیمت طلا
۵۰۰ تومن بالاتر رفته!
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67227" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67226">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4V555Jph9fLN56YKzA0KYR-sf9BesPHO7YNxWQaNkBZFcH4zHQqrASBJFf08hEgHKFDLxqar2bDDft0WfOfKj-hC7BHqa0fwm6-P54AVUVY6_-R28vh2g0OSW8jpc7_LKTygiSoXj416hUQMia6LEzUd6iCd3AVxzZcVEKgIvKyWXDBpfmeYcR8CbdZ9GGGmIykobJv9nXmrXZtX2gv1CFZQa-foUl1BkBru_kY9ZR3Jm3MMoczuN84XOFuGpTDaT5mYCD9RBt0jPmUqASH0nFoICGJ_PZH5MDa76-FedhOZ2cdhJX3xRF_OEDEAkX9VMQSn3hi0jxu3sYQagF_YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید محمدجواد ظریف:
ایران، پس از دو قرن تجربه تلخ ناامنی و آسیب‌پذیری، با هدایت رهبر شهید به مرحله‌ای رسید که در گزاره «دوران بزن در رو تمام شده است
🤣
🤣
» متبلور است. این تغییر پس از دو سده، احساس خودباوری و اعتماد به توان داخلی را برای ایران و ایرانی به ارمغان آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67226" target="_blank">📅 12:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67225">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10282a802.mp4?token=RBQ_NDpoPqgKy5EW9uXPkLv5DLdd7whAU-A_Nn-XWFmrFcEYicipPcAWIscoC20tf7sM0OmU5S-t8rgvOohTt9VzpYcE-50fXfTftd1OtfyzuqOY8170gcmMdF0m5i394P9u2aHWykToYbjnMcaJjROs1DiWjdt-fmESr5tkY41WGMQF79tkN6JvFDd6YopeoDLfFT2DI8Vfx9AcS7gHINNTh6JzIWAR5dYHM2sDBLaMJWcU7sSAKy7m0h58QyzoBQ5u7FUXK0YgchyzHEA6U7KvRfPU2I6q6gauQDMij8eNskT_1v96Irdgw19LiU-WgBtbqqodg9NwAt_cp2tXcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10282a802.mp4?token=RBQ_NDpoPqgKy5EW9uXPkLv5DLdd7whAU-A_Nn-XWFmrFcEYicipPcAWIscoC20tf7sM0OmU5S-t8rgvOohTt9VzpYcE-50fXfTftd1OtfyzuqOY8170gcmMdF0m5i394P9u2aHWykToYbjnMcaJjROs1DiWjdt-fmESr5tkY41WGMQF79tkN6JvFDd6YopeoDLfFT2DI8Vfx9AcS7gHINNTh6JzIWAR5dYHM2sDBLaMJWcU7sSAKy7m0h58QyzoBQ5u7FUXK0YgchyzHEA6U7KvRfPU2I6q6gauQDMij8eNskT_1v96Irdgw19LiU-WgBtbqqodg9NwAt_cp2tXcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده‌ رضا پهلوی درباره اسلام:
🔴
من نه با اسلام دشمنی دارم و نه با هیچ باور دینی دیگری. ایمان، امری شخصی و محترم است و هر ایرانی باید آزاد باشد که دین خود را انتخاب کند، تغییر دهد یا هیچ دینی نداشته باشد.
🔴
مشکل ایران، اسلام به‌عنوان یک باور مذهبی نیست؛ مشکل، حکومتی است که دین را به ابزار قدرت، سرکوب و فساد تبدیل کرده است.
🔴
همان‌گونه که هیچ دینی نباید بر حکومت مسلط باشد، حکومت نیز نباید در باورهای مردم دخالت کند.
🔴
ایران آینده، کشوری خواهد بود که در آن مسلمان، مسیحی، یهودی، بهایی، زرتشتی و افراد بی‌دین، همگی از حقوق برابر برخوردار باشند.
🔴
معیار شهروندی، اعتقاد مذهبی افراد نخواهد بود، بلکه پایبندی به قانون، آزادی و کرامت انسانی خواهد بود.
🔴
اصل جدایی دین از حکومت، آزادی عقیده و برابری شهروندان.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67225" target="_blank">📅 11:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67224">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226825be38.mp4?token=gQBfASUJz3rTUAWh2HtqpN4rhaIKkb9vhSVTYbP529lkd4nneRyTO58zu87oWNwfvTeAWJtN674OewjDTp5N64-hE7EUKldMuIMhniaE-okLVkwthQVPaIxfu9lQatwgvzURVFDnQSnAdNjifiSSjf8Tm1nH-M1ou1Kj8WO4vkprUW9VF89kgP-73L293CJ9q2kfDGdCY4HEuBERIF5EB7kFY_mCf80gU8U65YKWwRNei3ijYM3CTsNV45dHdhkkFeuDVZn5yux2ddUac8ddE80rHABb-EBeLsEOlunKUBogNg1P3-hFueIH1pl_ek_woIbbzUEFDGKpIOvUnDs3wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226825be38.mp4?token=gQBfASUJz3rTUAWh2HtqpN4rhaIKkb9vhSVTYbP529lkd4nneRyTO58zu87oWNwfvTeAWJtN674OewjDTp5N64-hE7EUKldMuIMhniaE-okLVkwthQVPaIxfu9lQatwgvzURVFDnQSnAdNjifiSSjf8Tm1nH-M1ou1Kj8WO4vkprUW9VF89kgP-73L293CJ9q2kfDGdCY4HEuBERIF5EB7kFY_mCf80gU8U65YKWwRNei3ijYM3CTsNV45dHdhkkFeuDVZn5yux2ddUac8ddE80rHABb-EBeLsEOlunKUBogNg1P3-hFueIH1pl_ek_woIbbzUEFDGKpIOvUnDs3wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نریمانی مداح حکومتی:
منطقه شیعه نشین جنوب لبنان ۱۱هزار خونه صاف شده، آقایان چرا نمی زنید زیر میز مذاکره!
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67224" target="_blank">📅 10:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67223">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRFsoaH2h5ZDUn1eVp8oi5F_pVNiwPekTP4SWx5I2b34ileHr_HWBeIyYNSKQSlHcI6ieYpQUjauhCbRUqj1QDcfHCaUzeQ2Ffdh0_6uplPF-MsV8CmtZ1vs5xzUe6YG-UZ5pcbID-kizT-kAQTk2Uyb5oGxNY7Yzn7fqgtxBXH2rE6k3ahQY3DCTHyw-kCqx-9rY7-6bClAR1keBM0P1wqx3LHayvB2uVKyK3F9qRUB7pPlo75bOD5kw-V46O6hHTl5hgctYS36_tJbbN-2V5z762rL8uL5RqExywrOnMTvHQkxhvUW8Is-9XYt1o8kd7uqQhN3dgJGkGEoRLDsNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه بانو الکسیس پورن استار معروف اعلام کرده با مردای همه کشورا غیر 2 کشور رابطه جنسی داشته، ایران و غنا
برای اینکه کلکسیون خودشو کامل کنه، گفته فرم پر کنین و درخواست بدین تا یه نفرو انتخاب کنم.
از غنا 2700 نفر و از ایران بیش از 1 میلیون نفر درخواست دادن! جوون ترین ایرانی یه دهه نودی 10 ساله و پیرترین یه پیرمرد 78 ساله بوده
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67223" target="_blank">📅 10:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67222">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55805ed771.mp4?token=Vm7k1qwdftHN2KL808XT8Fp2WdAxaeo2duq64kgNdHf-sx25f0jBUDTZVRt5uTjJFfKNBWTpdbqUHYK11R6ZBhZcB9a65szJdlD_jPXj-hDjNVTAt4FLMz2KNYx06VIILVG5Z9Ta-O2KnPquCf8knyj3MsxHSRGOgUdjBBnOSxOm2D1eqQVLP_BDtq09LS_gKrw3Tarfks7ux9l4kMvQR41OWaE3sFUXEZjtRYdJsMq2QMH2zwU_VRSyZwMrQIACHjMztGSwZDexVK7gwoOSxJsyKcIvEsrjFDJcmck9UoNJYJCnTsZMm-C7q3eQCLUgSTQcBrVS5xiGcHHo_trbCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55805ed771.mp4?token=Vm7k1qwdftHN2KL808XT8Fp2WdAxaeo2duq64kgNdHf-sx25f0jBUDTZVRt5uTjJFfKNBWTpdbqUHYK11R6ZBhZcB9a65szJdlD_jPXj-hDjNVTAt4FLMz2KNYx06VIILVG5Z9Ta-O2KnPquCf8knyj3MsxHSRGOgUdjBBnOSxOm2D1eqQVLP_BDtq09LS_gKrw3Tarfks7ux9l4kMvQR41OWaE3sFUXEZjtRYdJsMq2QMH2zwU_VRSyZwMrQIACHjMztGSwZDexVK7gwoOSxJsyKcIvEsrjFDJcmck9UoNJYJCnTsZMm-C7q3eQCLUgSTQcBrVS5xiGcHHo_trbCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پروفسور جیانگ:
آمریکا احتمالاً بین آذر تا اسفند یا حتی زودتر حمله زمینی به ایران را آغاز خواهد کرد و امضای تفاهم‌نامه فعلی تنها برای خرید زمان است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67222" target="_blank">📅 10:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67221">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4TnomvJMGIenuZG5a5TURCFknKeYCvLSJT0T9KY-737ms3jkjwCAKmu88MzV2xASfWAcYI8tABR6cUzBozq4dLBY7o3cC4PnoawhZv5RNBuOJVBQUieYrwqzBRN4XB_-wQYr0XTsVEZHRIyKYH84UuNocICT1Ok3wN2P5Q-B_8DM95jsri7G_F4WMTzSQ0oASqMYpG_gWofpULeG2QKzpPstfLxqG--2q_kBRvdQXLH2-NzhuwXdHYXgoO0OAiMOnan77gFdz8KPU4TkKm9fhKRZfS0onlQlnu9iWlFsNfD3z4Zf8EKOL-nkHczTIvCXcJST1gJTWl9JP2eZcF1kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین فاصله زمان مرگ تا زمان دفن رهبران جهان، مربوط به الیزابت دوم بود با ۱۱ روز فاصله که سیدعلی خامنه‌ای با ۱۳۲ روز فاصله با قدرت این رکورد رو شکست و نام خودش رو در تاریخ جاودانه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67221" target="_blank">📅 09:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67220">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=C5m4Gk8yPS9EojDLrXs8R3z2t6OyR6TbYInxG5KOb60bZjPoXK3J4-BT45kXIva8mJ6_raSnoDq8ZFaHV21RO2kfm9wE68g8I32oqFehQv-3rIiprUosWCq6iJ_x7huHchGXGSfxkN6CO8GNlFMGQ6jfA0cgzEIk_ExjX_QMVeNXu5QvCjYk1T7aNke_i2VROIq_QLRkSXJ7IXDviuuaez0Rji31lqp9JgDYUtj2eqQIPVA8HgjtAS1p2JKSSWqZyHe5JaKXQaE_wMD4RZ4X_5ubm6omNMgkyYlWCGk6IAg42b6oS9G1pNrz5hgLNTD4FTtVrTIW_dKjcGByGsYbAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=C5m4Gk8yPS9EojDLrXs8R3z2t6OyR6TbYInxG5KOb60bZjPoXK3J4-BT45kXIva8mJ6_raSnoDq8ZFaHV21RO2kfm9wE68g8I32oqFehQv-3rIiprUosWCq6iJ_x7huHchGXGSfxkN6CO8GNlFMGQ6jfA0cgzEIk_ExjX_QMVeNXu5QvCjYk1T7aNke_i2VROIq_QLRkSXJ7IXDviuuaez0Rji31lqp9JgDYUtj2eqQIPVA8HgjtAS1p2JKSSWqZyHe5JaKXQaE_wMD4RZ4X_5ubm6omNMgkyYlWCGk6IAg42b6oS9G1pNrz5hgLNTD4FTtVrTIW_dKjcGByGsYbAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان
:
من به عنوان مسئول دولت نمی توانم ببینم مردم مشکل دارند و بگویم همه چیز خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67220" target="_blank">📅 09:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67219">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67219" target="_blank">📅 02:25 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
