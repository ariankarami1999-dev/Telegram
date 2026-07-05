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
<img src="https://cdn4.telesco.pe/file/oQEi69z3ULo_fds4nRrRbpvuByIXQ9rDRbpu3m2Oe4BKb5g_7rPCjDN6aaql_y2uuOcF_8dJvI-HxezUzicOda-sPsU-C8Il3XbwWDyQ5GszK99uWSSYg_TKr_N5exytDJ85NwISRTNqAqcRIz2CWRcR_GFNSDAfmezR3JP3CHVWUHRtXWyUl5z3uKxFSQ4-LuDcHk0ZG-MfmV5ghglWRyxbFCXgrBrIIiWUCKMZcUkniYYn8-_JyM7qncouf-qj9WVfdi0vhA3blkGu16wgpfXleqi9gNUIm4gycOGL3HCX2N6FtplN0aEtu6HTPxRRDwLOpKWDJy_tip8tycqoaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 206K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 11:56:41</div>
<hr>

<div class="tg-post" id="msg-67323">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/news_hut/67323" target="_blank">📅 11:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67322">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/news_hut/67322" target="_blank">📅 11:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67321">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/news_hut/67321" target="_blank">📅 10:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67320">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/67320" target="_blank">📅 10:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67319">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/67319" target="_blank">📅 09:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67318">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/67318" target="_blank">📅 09:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67317">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7YME2u8bvE2FWFGwBcNjvVV1IfKPlNMALyxhHszxjDBU43HSMuYYyGBPXPbw-MQ1iIEiXiupFn97biaks6DVFAGTJa_IGgZsMmwoM0imeLiJVHyAKmGacSTnq0H_FbXTN6J5py9hh9ZOyXYQDKVwBKYww2DWNgLHL3JJ_5Hz33d7jtMO_kFaSQsQulwoXxq10bLkSBymeI9Gckl9JtYfCQ6lpDJ4FYwuQNzb017HGarwQnf5DUEaYbqqks9CqCcX8oAehppeTJFRjDQ3ofP56bpkpARrb0gzghXSJSagRNo94jCkn2M-_yG9k8LrPTOecQX2mq7RNwt33ik7Pbg8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
8فروند جنگنده A-10 Warthog در پایگاه هوایی موفق سلطی اردن مستقر شده‌اند.
🔴
این جنگنده ها برای پشتیبانی عملیات زمینی استفاده میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/67317" target="_blank">📅 09:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67316">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67316" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67315">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DkXKubrHFJaReOe9Kh1khvnPHZkhuZ6czj7YQ2DyEhdNxh0_GHmNhyEQxZxWkqaPKPoXqXqLmG9cMN7Q7liycma7w1nTsj5nK0IV60pzSE7lvhvSI8oglP1farUeV0vN2rIEgmFNGFZE5RSZWg3FG_J58989gTf3RS6hNpvTojT-_FnaZ-r8OelQmXgNsvMUsyvoehjN9Ua-9UUWLgvyWn_OLprjBzQklpFoJFHWALvPMXf1m5pdupSAjjPq5ZdiqXDTpTWEVC57_vnealmB_onS_ZY2NBFmrKofKM1D7GWZZSbdX4oUi2LTN95dmm946JokUrFj_um9uyjdaU17cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67315" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67314">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cye3988uUL2dfVzqRza6D6X0oHn478y3vtwdpo-sVpEqnKcOjhSWUS5e02yjLZ8ve9He-hfOrWe9gct_Tk-aX7_Z-hTUD9zVDJOJnviPA8Mw30cTIkUEGA8wxOQTZdhuKtHUxgDOuKwsq_VkeSPVi1daK_LT1-29nz_DKL34go3O8pgg0MAcMXPYz4QWFx0XsBuCsrNUGBKJJ3-fUc3nA7ef2HiwZSWJ-OQrHsxnyk08BlPff2UXMdrvOXC4ngzE74_179hY8e0ZJxTtyDTONxJw-4VBQzqKR3HnnTimlQGJhQY5RMLQ4NE9bZQgZpFUIQVwJ9cdE4QEAJ797aI47g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
ولادیمیر پوتین، رئیس‌جمهور روسیه، با دونالد ترامپ تماس گرفت و دویست و پنجاهمین سالگرد استقلال ایالات متحده را به او تبریک گفت. کرملین اعلام کرد که این گفتگو یک ساعت و نیم به طول انجامید. پوتین از ترامپ برای سفر به روسیه دعوت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67314" target="_blank">📅 02:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67313">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67313" target="_blank">📅 01:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67312">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSCRo-pWVyW-vF2zHNSD-pZ5LLY0SfPRkPGIdDoHzd_XLHAWCzcrD56iTxEXrmS6qLucDs5mAv6-1mljJFI-0lc_9dO3ieZKwcYdLjjFqcgyLgbTAR_VymOfBH17tvTLwuGCfAvapbqLwYOhtzwVoBRNg7SfjFQqTMPlX0UFZvF3FHMymBrrQgpQA1JSRO4vSj2clGL2tcol0gabywKlphZV8bLZkxOrvm1f8mUMeEPmTPU93lIrH70pf8V06rFCKT8okPSSDipoH3aenCANn1PmpISV3lVLAQvJKuV7lh5D9-UY69RCaC70MC90qt2PhaQChJrjyyzoaUZQlcn_Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیروهای ارتش اسرائیل در حال عملیات در منطقه حداتا در جنوب لبنان هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67312" target="_blank">📅 00:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67311">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67311" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67310">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67310" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67309">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eRdZ3C2LMcZykC5HWaHNP7aDcCXkyaWK0lcPz24UDW_xuhTRbwwIs6J9XzfQGYvfA328Vnpg1Iv6ZlICWYH9jiMaMhc6MeBP_vzjulLcl9RLTQLkToHEW8BvOM5fWlRZb-akWNn9U7t9FQr7nupK09XchGHrKtUFprJPKB8dj4cuGaO5RvEd07I6hFWJ2FP2Ost35lbUBTzdz1nVzOv6KQ1Ru-BQTk_UKIHQGnjr855yg2Jm1Zj1lk-tP1_qKWnpcCvwfqW0kXCo3FvHCVcuyBNwk8wjuXKCy0lTS43W0Du1u5MEd5a2AZznZkWoIYqj43_boJZmRTQ3f1ktErBNFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67309" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67308">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67308" target="_blank">📅 00:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67306">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67306" target="_blank">📅 23:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67305">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=WQFf7RYG1UZEj-LlfxKA7qahWXULju7ed34A4pF8Nh7Bzj7ouOdtLS0BpfK7bQJ7t5w_Q38YDPzy6UFKaGbuR--peyE-BNvMLVRm-FUH64byqox-8ZM3M1Mb8A3xz9VWaNozJNdwE7C-KOUgefYHK6zpw0oBNSXNEkoPMJbulIBAaOtre_uejOAwNjkPM-_eseRh4UchJQxc79cieFAjV8d57w_lcQ29NJsGnD66m9uB-spumn3a8-iY1DRJ-9IY023SGczR2q9ytFym7umobl-ACrcaGlM6uMd613Qm1IK5ZrsHtQ3XWTt3Gfa2pQezJtzRtqvU9QAa7UCFiKz1nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=WQFf7RYG1UZEj-LlfxKA7qahWXULju7ed34A4pF8Nh7Bzj7ouOdtLS0BpfK7bQJ7t5w_Q38YDPzy6UFKaGbuR--peyE-BNvMLVRm-FUH64byqox-8ZM3M1Mb8A3xz9VWaNozJNdwE7C-KOUgefYHK6zpw0oBNSXNEkoPMJbulIBAaOtre_uejOAwNjkPM-_eseRh4UchJQxc79cieFAjV8d57w_lcQ29NJsGnD66m9uB-spumn3a8-iY1DRJ-9IY023SGczR2q9ytFym7umobl-ACrcaGlM6uMd613Qm1IK5ZrsHtQ3XWTt3Gfa2pQezJtzRtqvU9QAa7UCFiKz1nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم خاکسپاری رضاشاه بزرگ در تهران، زمانی که جمعیت تهران فقط ۹۰۰ هزار نفر بود و بیش از ۲۰۰ هزار نفر در مراسم شرکت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67305" target="_blank">📅 23:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67303">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SDWy4pzi4Ip5XV7vgElrgnwJbFAvfcRovbKXFsMQfktjsbJuyxWNIM0YGwif7vrTGD8XeZ0Lgs1XNBVnzhWoPCqYNe4bhEkCMaSXBCG2egIIuV9Qdu-zzyQtI34Dj0uB7ysJNMUh2WG9F3GqGuKBpUeN4zkhnzeEah0001WFsCCEmhzRB3o4Bl2f4IJP53cIUfdbDWplPPLBh7lFI5Hx78kG_ZmL74E4sYJLgdPkNUlSdj9b9ipL6bP-tqdxQsXmFkIbNThqJMk9qX0B1u0y6OQ6_E7vjFvPgp4ZgeaL5xCinMANTVihO4gWYID1uGY40Pvox5mpHlKyaeHiWZa2lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fm6tcfojvOdGL_83bYjDUh7y0BWt3V52alrsqGSuAkPjNP9PRg55kdIqlJerYybGLl5NlTwljMKzF4EOQqdVPImA_MkBeLJf_XuegOHnA_VUrfn5wHFCqkGpv9_RwY7QflTfGJNQemMhqwMVdcFcilBOfa_m-P3fQ2pQtD9ipD-YU0y5UHpjthTMXGjPNRel19UHSU10RLHiJC9hAXAy1azkF4j3Lp5dUFsi8t46n9iSzKcpqrUQBAI5ctWP1JZTxipjpLKyIn1qdR2e4Lwf4dAD_bDfZHoHdoUwZJ7rg5FZ3FfVdxlSzjUbiC9KKHhneqdI-1eCR0YiHlwKLDsAkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
زمین گرده...
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67303" target="_blank">📅 23:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67302">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-x9-aOaeoV_adeiI6vJbRO5RJJ23JGEbe2axdaJK8uqYooCOtcZfu_YI3nTjT_HCpf8cOn7xYGzfZjLrAiERUYERtJZnhFZgabzbnZm0NWPtIfFiqI9BAWmOaonuOfrc4_p6IpnCrEEGsnlQ2oetS7oRLdEFOPWOltgIlLS8y5u8ZmfTUtqaPo4O5hOZlpf43VeqspUjE8OwLIoUDlM5qy50px87s86x5Gdpbj161rxrXKk-Re0Q76Mq7OMu1h2xno3M4QWo7p-3EQKQhvz_YVC70MlI14_8fI5Jb9-_Iz6Vnr0-b7VvBcZtaBvrx-b7yz5zcgH5oZvO2e3j1B-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
دو مقام آمریکایی به من گفتند که مسیر جنوبی در تنگه هرمز همچنان فعال است.
یک مقام آمریکایی مدعی شد که اکثر کشتی‌ها با سامانه شناسایی الکترونیکی خاموش تردد می‌کنند تا توسط پلتفرم‌های اطلاعاتیِ «منبع‌باز» (Open-source) رصد نشوند.
این مقام تأیید کرد که ایرانی‌ها تلاش می‌کنند از طریق رادیو VHF برای کشتی‌ها ایجاد ارعاب کنند.
مقام دوم آمریکایی اظهار داشت که سرعت تردد در مسیر جنوبی طی روزهای اخیر افزایش یافته است (حدود ۵۰ کشتی عبور کرده‌اند) و این مسیر همچنان باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67302" target="_blank">📅 23:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67301">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=GxHoaPVxkwVCFTpbW6WbZY_jyyEebY4SZX7F4ea_CjjFKuk0FRy0Of6noOy8ms9w0KTXOSzzHFV4k9vzcY5I1AFrD3nF_A5mQN9Brnxna5665Tt3ZX4AYuo-b5unTBxyeCLNvFiduFgGSVYDMkM9z5ahwF3s5KEa0AXQa3fzQeZ8p3w9Mx81ikerernX4BS83i4RsEtKyj4TPEcuyTgo12AOIa05uwhrb2nDblebB-ucFTW9-trUhyUhpEMwmGwDfDCsZA5NiHQl1fQh5jLr-cwCJQKHEHxHTY9B3JAhlWoR_wQ_dGXHv9Fu7kzTtG3qwoOKj100Df1PXhmkO50CiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=GxHoaPVxkwVCFTpbW6WbZY_jyyEebY4SZX7F4ea_CjjFKuk0FRy0Of6noOy8ms9w0KTXOSzzHFV4k9vzcY5I1AFrD3nF_A5mQN9Brnxna5665Tt3ZX4AYuo-b5unTBxyeCLNvFiduFgGSVYDMkM9z5ahwF3s5KEa0AXQa3fzQeZ8p3w9Mx81ikerernX4BS83i4RsEtKyj4TPEcuyTgo12AOIa05uwhrb2nDblebB-ucFTW9-trUhyUhpEMwmGwDfDCsZA5NiHQl1fQh5jLr-cwCJQKHEHxHTY9B3JAhlWoR_wQ_dGXHv9Fu7kzTtG3qwoOKj100Df1PXhmkO50CiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مردم اروپا با دمای نهایت ۳۶ درجه
🆚
مردم خاورمیانه با دمای حداقل ۵۰ درجه
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67301" target="_blank">📅 22:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67300">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=ga-rc1EfDqSjpoccl2L8Zx1Gyw08We7Gnsh5YVf6D87-SrgmS6vgtt3KboPri8hgK5DwcwMM5TsVZ4G6ijoOffiz6MR3yqin20c-0a80s2_qD3QZorB-5s5S1K1mZ1JOhcOoX_O6Q-0MpWJ0no-Mwc2ApNYLKX4O0zA4zMu-lfP72CWq5DQ-xH7ukbcDQrFH315HAGktwOLLXeZ3JVk1jfRnwxtqMdenVWYlEWJC-oHaVs0NsuAppovgGM6XsPEUIkAdqUGjJVA9fUFrmhqTSeGWRKUTmP97pNoUGfGUE8TjiinwZH68-gAdmU93j8ud_eC2A7jXCSQPYFzp5tkC9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=ga-rc1EfDqSjpoccl2L8Zx1Gyw08We7Gnsh5YVf6D87-SrgmS6vgtt3KboPri8hgK5DwcwMM5TsVZ4G6ijoOffiz6MR3yqin20c-0a80s2_qD3QZorB-5s5S1K1mZ1JOhcOoX_O6Q-0MpWJ0no-Mwc2ApNYLKX4O0zA4zMu-lfP72CWq5DQ-xH7ukbcDQrFH315HAGktwOLLXeZ3JVk1jfRnwxtqMdenVWYlEWJC-oHaVs0NsuAppovgGM6XsPEUIkAdqUGjJVA9fUFrmhqTSeGWRKUTmP97pNoUGfGUE8TjiinwZH68-gAdmU93j8ud_eC2A7jXCSQPYFzp5tkC9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیام نتانیاهو به آمریکا به مناسبت دویست و پنجاهمین سالگرد استقلال:
🔴
«۲۵۰ سال آزادی. ۲۵۰ سال دفاع از آزادی.» او این مناسبت را به عملیات «انتبه» در ۵۰ سال پیش (که در آن برادرش «یونی» حین نجات گروگان‌ها جان باخت) پیوند داد و اظهار داشت که آمریکا و اسرائیل در ارزش‌ها، سرنوشت و مبارزه با مستبدانی که شعار «مرگ بر آمریکا» و «مرگ بر اسرائیل» سر می‌دهند، اشتراک دارند. یادآوریِ یک اتحاد مستحکم.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67300" target="_blank">📅 22:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67299">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTMa6fCZ0er853NBrovdyZPzYCBRt8ISKIn7UNnz0Nb0LKvv9r4V1Vo8qkX1ZGhbo8z_JDqLhU5IT9rMuUzkazqYSjNTiA1TZ1MG4Jo0VSikv7VWAinJOpahAtKIIUJadCJSjJjx61x7iNxOVF5PEk0m7ano1PNJsGOz-GJte0sGW1RnFcRKar9Dxy5_1wr2Jn77r92cVBGbgKbJ4cDd0W3zh9pU83UrrzyhqrHH4f3gbNxt_4gp6FffyylJC8p6bLn2OnzHlfC6Kr6dZpikMCgdn1npjmIljrMpzjrK2W5LCjdJDjqul8WMtiabNH470Gd2vrftevlmYQ_yhpnhTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
دور بعدی مذاکرات ایالات متحده آمریکا و ایران در تاریخ 11 ژوئیه (21 تیر) به میزبانی پاکستان در اسلام آباد برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67299" target="_blank">📅 21:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67298">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F69V3NfhRJhqe58PdW7fqUr2HH-NrTJSTD2Iy94jPznJwT4PHRmANatztEViykrREBNzKLw0U6NT8anwUhQ5JXdjUxm8rMj59tvgkii8QWAWYbvtWQIs6dj9GcLWwrfjrVk1xEgVK_WWwOFHQl5VcaCMHbLzHtK_AD6tLphF9053y1xgEdEGr2jRL6c7hInmPaB_Su_V791_kgpGDrAA1K6Q_olP5-jCpkXW7ZWTUG-6fufgknqU2XoLLz6CPBt3QIREC4PpBZ4gRnU7I31tejg1ZAueygSnj_O1BG2IL5Wll-uwptyKRmniy2w51XA9SEfH19HYBeXo_m-TkSwuaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ:
فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67298" target="_blank">📅 21:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67297">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjbXS8dwtkc_yECSqh4RaDJQqkX1LdAhUWIBFwxU1FUQHrxhVXrx8S5LciuFyVXOG9GtmAMjGLLMdeGi6yXvi59--ruzRF5fmSTBUBDN7-d1cAkqgm_gIyPcsNiRhjwiKGGjsO5IsP0doc4OsEs0vsFv1B0IywMYh4NmxBcaQuMiNSWurkIf9e8OUa1gzCUof5t-HMOrox56kRVi0SolyHLbHdWD7E4lwU_JzzWT9vhLhBBOpLlroWFJaYAQHpObWkje9NRI_bHqc5F4be14de9ATnYewq5HX2XfprPiSeXtWV0Xzv3rYSO3Sr6CDY9jMDVjtnEk-Pw6i2cRZqK5Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ به آکسیوس:
نتانیاهو میداند رئیس کیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67297" target="_blank">📅 20:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67296">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
پرزیدنت ترامپ:
نتانیاهو درخواست ملاقات در کاخ سفید کرده است و این ملاقات ممکن است همین هفته آینده رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67296" target="_blank">📅 20:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67295">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به اکسیوس:
از دیدن ایرانی‌هایی که در مراسم خاکسپاری خامنه‌ای گریه می‌کردند، شگفت‌زده شدم. من فکر می‌کردم مردم از او متنفر بودند.فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67295" target="_blank">📅 20:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67294">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
پرزیدنت ترامپ به آکسیوس:
«همه آن‌ها آنجا هستند. یک گلوله [و می‌توانیم همه آن‌ها را از بین ببریم]، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67294" target="_blank">📅 20:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67293">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589cc62912.mp4?token=b_XE2ubHjwrFh8SlAc6LqQVjgmf4ZaVPbR9YgM2LldJa8KxAIu8LNyJ8IFBlWx2zxeDuT5qXR0TceAUojtgd9IJPn5FLJ72QVnJD_x9-yvyK4fNm-2Pa6FiZylWLbExp9YVHSPPuL4oBnrQE_mS8ktp3hUogVx8-GNJXD3IFQ8Sbg-bs5Zl2JA19lHoNk-vYXQpcBTB8aBNJxH9QdwnGS2pNQDovBndthTQycKqhhyx7Rb11iBz_YuB1zL6sM6u37McpvPy8kf0a43nYZQ5jbo5AIEcEq3_RtUcrd115yTO6lcv5E2r-OP8r5mq9fLzqCXyEziqDYwlKKQGK2sH5vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589cc62912.mp4?token=b_XE2ubHjwrFh8SlAc6LqQVjgmf4ZaVPbR9YgM2LldJa8KxAIu8LNyJ8IFBlWx2zxeDuT5qXR0TceAUojtgd9IJPn5FLJ72QVnJD_x9-yvyK4fNm-2Pa6FiZylWLbExp9YVHSPPuL4oBnrQE_mS8ktp3hUogVx8-GNJXD3IFQ8Sbg-bs5Zl2JA19lHoNk-vYXQpcBTB8aBNJxH9QdwnGS2pNQDovBndthTQycKqhhyx7Rb11iBz_YuB1zL6sM6u37McpvPy8kf0a43nYZQ5jbo5AIEcEq3_RtUcrd115yTO6lcv5E2r-OP8r5mq9fLzqCXyEziqDYwlKKQGK2sH5vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
۲۸ دسامبر ۲۰۱۱؛ مراسم تشییع جنازه کیم جونگ ایل، رهبر کره شمالی؛ مراسمی که تصاویرش به یکی از عجیب‌ترین صحنه‌های تاریخ معاصر تبدیل شد.
وقتی این تصاویر را می‌بینیم، شاید اولین واکنشمان تعجب از شدت گریه و شیون مردم باشد. اما واقعیت احتمالاً پیچیده‌تر از چیزی است که در چند ثانیه ویدئو دیده می‌شود. در کره شمالی، مردم دهه‌هاست در یکی از بسته‌ترین نظام‌های جهان زندگی می‌کنند. از کودکی به آن‌ها آموزش داده می‌شود که رهبر، شخصیتی فراتر از یک سیاستمدار است و باید بی‌چون‌وچرا به او وفادار بود.
از سوی دیگر، در چنین حکومت‌هایی، ابراز احساسات در مراسم‌های رسمی همیشه یک انتخاب شخصی نیست. بسیاری از تحلیلگران معتقدند که آنچه در این تصاویر می‌بینیم، ترکیبی از باور واقعی، سال‌ها تبلیغات حکومتی، فشار اجتماعی، ترس از حکومت و گاهی هم منافع شخصی است.
شاید مهم‌ترین درس این تصاویر این باشد که وقتی دسترسی مردم به اطلاعات آزاد محدود شود و فقط یک روایت سال‌ها تکرار شود، همان روایت می‌تواند واقعیت ذهن بسیاری از افراد را شکل دهد.
تاریخ بارها نشان داده که پرستش شخصیت، فقط به یک کشور محدود نیست؛ هر جامعه‌ای که آزادی بیان، نقد و گردش آزاد اطلاعات را از دست بدهد، ممکن است در همان مسیر قدم بگذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67293" target="_blank">📅 20:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67292">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/648e669177.mp4?token=a-0rZKzFgcQ0pdP_oVQgw_Ir4g_XDkC-ThqXAZKGOQ-IlR48_XrU0s3-WXOg1pteNg39T6rjtFGQIabUpINgs_JWb4FPSK89nhG0igRz_wpU8lLdk49gbsQqDNNZYBtJh0R4arA3h9OJAWkaTiKgX8kZwNfOeNWzP1NgzqgKUb4TjaBMGbGD-yB8jRmAOfUwjLCWFO68r1svryXVsiaK_Qv-8pSGOWwQXMN4POi1Z983c6zisrVetdZGoaRxukfVtJ3Uv8ZWHPafw0KagfacKrqYvpb8hvbxngaAD2U6Vn-lCkdEv3zoXDIieGwzxp2BnJHhG8PqCEtAxKVW3h3_yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/648e669177.mp4?token=a-0rZKzFgcQ0pdP_oVQgw_Ir4g_XDkC-ThqXAZKGOQ-IlR48_XrU0s3-WXOg1pteNg39T6rjtFGQIabUpINgs_JWb4FPSK89nhG0igRz_wpU8lLdk49gbsQqDNNZYBtJh0R4arA3h9OJAWkaTiKgX8kZwNfOeNWzP1NgzqgKUb4TjaBMGbGD-yB8jRmAOfUwjLCWFO68r1svryXVsiaK_Qv-8pSGOWwQXMN4POi1Z983c6zisrVetdZGoaRxukfVtJ3Uv8ZWHPafw0KagfacKrqYvpb8hvbxngaAD2U6Vn-lCkdEv3zoXDIieGwzxp2BnJHhG8PqCEtAxKVW3h3_yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
▶️
داده‌های تارنمای ردیابی پرواز «فلایت رادار ۲۴» (Flightradar24) نشان می‌دهد که یک خلبان آمریکایی در آستانه چهارم ژوئیه، روز استقلال ایالات متحده، با طراحی مسیر پرواز خود بر فراز ایالت اوهایو، عبارت «USA 250th» را در کنار نقشه جغرافیایی آمریکا ترسیم کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67292" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67291">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر : مراجع تقلیدی که‌ قراره نمازِ علی خامنه‌ای رو بخونن که همچنان خبری از مجتبی خامنه‌ای نیست!
تهران : سبحانی
قم : عبدالله جوادی آملی
مشهد : نوری همدانی
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67291" target="_blank">📅 19:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67290">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=lT3WsqEalJMlBLv9V64Kw4gI2KI6h-mOvmY7VAADhi-OYPjJc-PL-vdjb0EUIUFjEMUaGTHmF2NfeQymKsqFfjA-3O60XfE9n-9YyS59uz9ciDOQJiV7yWeqVKKCT5EWFbuVOxXDE4LUBkQEolE5Cbyur2nUwNMTUGNSgpGyFCEB9lmIHDvWqGqGRQYRVBl309tdLlQyVhXmi1Ly0b6fA2ZBboiHFzUJR8QphWJczNld8S7mIgaoRxwcwYuoy-8MLjPWuuOldnMeWtYQ-PlHLG418VuJr0y3-zSPW9T_RZ1CcbD6CoQJfJetDNEar2v330wq3NHjMpjR3W2kw5hb1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=lT3WsqEalJMlBLv9V64Kw4gI2KI6h-mOvmY7VAADhi-OYPjJc-PL-vdjb0EUIUFjEMUaGTHmF2NfeQymKsqFfjA-3O60XfE9n-9YyS59uz9ciDOQJiV7yWeqVKKCT5EWFbuVOxXDE4LUBkQEolE5Cbyur2nUwNMTUGNSgpGyFCEB9lmIHDvWqGqGRQYRVBl309tdLlQyVhXmi1Ly0b6fA2ZBboiHFzUJR8QphWJczNld8S7mIgaoRxwcwYuoy-8MLjPWuuOldnMeWtYQ-PlHLG418VuJr0y3-zSPW9T_RZ1CcbD6CoQJfJetDNEar2v330wq3NHjMpjR3W2kw5hb1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
یحیی رحیم صفوی:
بین ایران و اسراییل جنگ موجودیتی است یکی باید بماند
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67290" target="_blank">📅 18:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67289">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIYN2J_ukIjRfT5Jh5O2obmOtO40ap5bGrfOTc4co6ELselckfiMpXbeOsnnDlim5naWu3AM2zp-p_dv1L5K1d_6dbzjc32Ka4ggTp6319yy1oQX3plEj-2paFhtVwOwteralY9OwG7q7Mn5EOPBPtAoEJbvQuCKBK70OQHpjEpxDkjM8CSUr9hsHTVhCw33CI3V2V518wkCKD-W2IVkHt8I3cJg8Tait6lQQwUQCJnqcMcWVinBkKBPJpuXX4EMMgGeeoV5bA0EYyqII893ojVFTUPKeGkgC8YJvyE4Z1OWcYZA5BxOuAdfs7mH38JBC3oS6Tv0iaQrN_6MFLxmmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67289" target="_blank">📅 17:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67288">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=jYf5GfRilneeIpeA0ARnlENbCLUHiyzElTKZQr6r4pL_kaQ_ENC0_n4T3IOcT9YmDG-mnigud0A31H3XPCScAzoJNPjX4Uacw9MeiKusXsfmm5HBQ669dWe42USG1HrJ1PPDtoAAXo_oE51uIfAQLsoh9Xn0Xb7Gh8vm6_AqFC7ys00CPpFhO_0iBn-c8YTbcpbhLaJoB2iFs6WoqHLRlolERH25o0yis5-P_KsIBPlOihckVH3GwdEPNBXRSe8lOl6QgI-ifPOcOFjrdgGWJAl6jpacBgR9M29ipgn6dgltDI7NBR4FBefG2RxSMFLBrWW7Vt5KCPxswHu1oyCzZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=jYf5GfRilneeIpeA0ARnlENbCLUHiyzElTKZQr6r4pL_kaQ_ENC0_n4T3IOcT9YmDG-mnigud0A31H3XPCScAzoJNPjX4Uacw9MeiKusXsfmm5HBQ669dWe42USG1HrJ1PPDtoAAXo_oE51uIfAQLsoh9Xn0Xb7Gh8vm6_AqFC7ys00CPpFhO_0iBn-c8YTbcpbhLaJoB2iFs6WoqHLRlolERH25o0yis5-P_KsIBPlOihckVH3GwdEPNBXRSe8lOl6QgI-ifPOcOFjrdgGWJAl6jpacBgR9M29ipgn6dgltDI7NBR4FBefG2RxSMFLBrWW7Vt5KCPxswHu1oyCzZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
روایتی تصویری از شاهنشاه آریامهر محمدرضا شاه پهلوی:
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67288" target="_blank">📅 17:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67287">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‼️
ادعای نیویورک تایمز به نقل از ۴ مقام ایرانی:
پزشکیان به مجتبی اطلاع داده بود که در صورت عدم توافق، از سمت خود استعفا خواهد داد.
نامه‌ای از رئیس بانک مرکزی ایران باعث شد مجتبی با یادداشت تفاهم موافقت کند.
پزشکیان، قبل از امضای توافق، به مجتبی خامنه‌ای اطلاع داد که محاصره دریایی، ایران را فلج خواهد کرد
.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67287" target="_blank">📅 16:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67286">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=MehdyS29Qn61fAxJUqv8c7zCkSbY7BEaARL4I_hFNcTxLjr5Uf3N1lSzqQVpKAprivWtptU-nRAKB9-jTLJEx9ZNWYHZEaBjcZAbU_PbyZTnZrrP9ARn2UUVvqqBfkeV6Xm3ODr7_emgkNN3QGerfR0x3tzSxemiGf9eWuguAiJHexFAaJH7zXO8Gj9YvWrcYLKDBACLQC3g4ybSU5ulT2u7NX4zgNCHLd3fbXbFUbt9p15R7MkZ8WB2h-UeY2ObCEzUHh5pt6UwWWHC6MiPB1byzavHQK9f_a-fohLh5AedRlz9GTULSD0iC1SiL1TBm0SpqS667HLZ_mg5Zs8D6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=MehdyS29Qn61fAxJUqv8c7zCkSbY7BEaARL4I_hFNcTxLjr5Uf3N1lSzqQVpKAprivWtptU-nRAKB9-jTLJEx9ZNWYHZEaBjcZAbU_PbyZTnZrrP9ARn2UUVvqqBfkeV6Xm3ODr7_emgkNN3QGerfR0x3tzSxemiGf9eWuguAiJHexFAaJH7zXO8Gj9YvWrcYLKDBACLQC3g4ybSU5ulT2u7NX4zgNCHLd3fbXbFUbt9p15R7MkZ8WB2h-UeY2ObCEzUHh5pt6UwWWHC6MiPB1byzavHQK9f_a-fohLh5AedRlz9GTULSD0iC1SiL1TBm0SpqS667HLZ_mg5Zs8D6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارهای عجیب در تجمع شبانه علیه قالیباف و آمریکا
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67286" target="_blank">📅 16:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67285">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=Hdrlj77Xx6COFwo0Whq0kmdqWlimOeQCXITHMGXaVvV7Zhb1vTbRKgrFWZR65AlNEYvaXU9T9raPW0oKRUJa_jil5x7Uh_SAw5dXcLVCE8cG4emK-0p-cwMZ-vU6Zw0BFXCAxTUfIMGfxLqqJk6woHVtv0-5Iaqk49mRwptywnP58XXWCDzZzeVBI_iruM7jo_ubaXnEijfPl1TwQymuP5WpbC5g5Mv8TIxCeF0pOIKQRgBhEnkcz6DEsUgikdM8SpaFsC3MsIvSRgmerCFFQh5311GuFLQI9Erahgt_CbBRJP9ICXrXiW9p_wvLAJte4I9_OpvOKxpp3rMRS6kWZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=Hdrlj77Xx6COFwo0Whq0kmdqWlimOeQCXITHMGXaVvV7Zhb1vTbRKgrFWZR65AlNEYvaXU9T9raPW0oKRUJa_jil5x7Uh_SAw5dXcLVCE8cG4emK-0p-cwMZ-vU6Zw0BFXCAxTUfIMGfxLqqJk6woHVtv0-5Iaqk49mRwptywnP58XXWCDzZzeVBI_iruM7jo_ubaXnEijfPl1TwQymuP5WpbC5g5Mv8TIxCeF0pOIKQRgBhEnkcz6DEsUgikdM8SpaFsC3MsIvSRgmerCFFQh5311GuFLQI9Erahgt_CbBRJP9ICXrXiW9p_wvLAJte4I9_OpvOKxpp3rMRS6kWZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😐
ویدیوی این بسیجی که در مراسم تشییع علی خامنه‌ای وایرال شد!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67285" target="_blank">📅 16:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67284">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67284" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67283">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67283" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67282">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k94B5U4znBNvV3tqDYFx532qipAhgLjaEf7tVFRf8h0CYW5jNz8Ajbk80gayRjPrG1335ZaIs3z7TAh29ryQOFtGpiKlYFZHQBg-7JlNlMEaNGhxHe4ERnSo7sPFpAK_nB4a00Zfmdj3p1_Rn6WoLxRfqo7tCw1QeMw6qxQt_XXUOTL5IoB1M2vxQtNC3YfjgfpGxfiSJ0R9PXZFb5H8zk1lFnaE7ycJgJGEDI3Tl2luNuRd89CzaMMgNCLAouH4CHPodTNue8ca-vEYpV8-RIweUcmrKep_bdYCYoyqtNb09DgmbTbarNaotIPGiBQYy8DN5zDa8jBsPzyz-b68Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علی عظمایی فرمانده جدید نیرو دریایی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67282" target="_blank">📅 16:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67281">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
با تصمیم هیئت دولت، کل کشور فردا تعطیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67281" target="_blank">📅 16:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67280">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOxSyJYm3IlebCmfB1mszF5d2Rvm7SRchLBmHIa4-au47QGYIw87ZjzwJUJLNyc2VLz7F7hp9fNHjPYKXt36fAQU3aWtCVWIJl2KTB_cOMdVAoNkiBZRRSo949LCeakN_KHiHrPcgu-fFqVQmUWYchPCGZXFmZmqianRGZhVHhui1K9lTHPYZf5kEJuQ5ZQ-7QmjSu0B7EX6H7cC-p1ecnI5YfeEXQV3Lm1kIV-3iy74J47Lmqf4kktzsuCwBdy6aPWQ8r0ZOKFuE2Zx2wLcsW46nabSJ7JHFxPeCjWr9M6gwmYtF0XzZxjvoMa-9EEWk9iqyDE7K4lGa02wv_fUNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیویورک تایمز به نقل از منابع آگاه:
🔴
مجتبی خامنه‌ای به مقام‌ها گفته است می‌خواهد در مراسم تدفین پدرش در حرم امام هشتم شیعیان در مشهد، که برای ۱۸ تیر برنامه‌ریزی شده، شرکت کند و نماز میت را بخواند.
🔴
مقام‌های امنیتی تاکنون با حضور مجتبی خامنه‌ای در این مراسم مخالفت کرده‌اند، زیرا نگران هستند اسرائیل از این مراسم برای کشتن او یا ردیابی محل اختفایش استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67280" target="_blank">📅 15:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67277">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/izgIiGJbZd7-_2ie7jUAoGne9zJdvKlmJTg3-1czAPbreuUZJ371WmCeqxbYAjUFJwqCjwr6IONDa0UZ1UWN0PYnqh6rpH1qxo3qAJQV-zN93nt50stDDcFHR0krsHZ2Ln7GEsWkgF7uVHYb-6aCNMdW13aVgV7kgX1hawBoyydM5xnlM_LyRpa1YwMcB8TRgh0ucN1RJp4j06K39DiOAiZIogW9DI9qAj259uC9n8vCZS3gIh16MxEwghty6RyR_hAS-JoXaYcRBPWB-fFUEOiGfnw2PSr21Ga0KCHDrfSTKgLNwtw777xm1fv_Rw9Xzm5VvUdZtIej9g-zwJ2UlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hSsDPXv7dyqJL3fn6Gm_5U7v0GztTw-2IeQgdUQzqpNo9yT6Zie5iBU0Nb0qbTC3bRxwFEkzRjiuBg-VdsDsf95zUpm1OYuAs75-I5Gu0QUeRU-DAw9N012JC2AxPgSrlvQfGZfebWwVGL8ipEXq3c0R3-d4N_FTguFCEPlH5WeL3OS_vv8bT4GBCy42Ei57Y-h32ip0inGqJ87jm4m0lOr9Go7ugvQEOT-DG_Bj_XP3xmCDoa0pqOOq4xewTi54t5ZGl29856eNkSmJAHj6uY0seCCHns771TgmagHkDDlP1Zw-jzim7lJ4nYkjoNCzvTehw8_5tSRnAAdRIYYYOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=mzQQf3RWo9UVPJ1ygecyo0yBxYeyjdNUK8LSCSW3zpUsIsvxQmkBuKVLau0qBnyUIDS66lAkxVtvqv0LMC1p-AVFFZpqYiUTvof3XFV_A_ltqqxdsUR7Mw5cHLA-xlveqhUMEBTh1reYPkzG1GzC0GN3YnVNZE1z0-IDP7gKyVN-NFEejtscxJR2nXdDEM-6IiECnVAzFbhFR2vZ_pSd5faRTm5al1gUr6KBsx21il2tCwZjeWufuFxPHsnTTFMO9HE4xl80CNTWyyWyg7szYUNaQZeeXyB1uWlT868tNTy4-FgupCQ2vfhoiwXJMRL650SDuJlQGXmaFPIhGI4Dxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=mzQQf3RWo9UVPJ1ygecyo0yBxYeyjdNUK8LSCSW3zpUsIsvxQmkBuKVLau0qBnyUIDS66lAkxVtvqv0LMC1p-AVFFZpqYiUTvof3XFV_A_ltqqxdsUR7Mw5cHLA-xlveqhUMEBTh1reYPkzG1GzC0GN3YnVNZE1z0-IDP7gKyVN-NFEejtscxJR2nXdDEM-6IiECnVAzFbhFR2vZ_pSd5faRTm5al1gUr6KBsx21il2tCwZjeWufuFxPHsnTTFMO9HE4xl80CNTWyyWyg7szYUNaQZeeXyB1uWlT868tNTy4-FgupCQ2vfhoiwXJMRL650SDuJlQGXmaFPIhGI4Dxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب، برخورد یک صاعقه با برج وان ورلد ترید سنتر در نیویورک
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67277" target="_blank">📅 15:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67276">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqYNynyI4afM8Dtesw6F39CE81Li5VqgKrcLbmVfZhBw0gtmkjdClUWFu2WelPumWK5qCgHahjeR1ITxX9AXANv4MhhFW_78fJTl7hw7-RtEgkQg4I9aYKF-RziDo1DzoxwBOK7XSk119kDGX0VzMNqU05hQ0IWVZDgY8HFR16eIY0KY5UknLgo9Nt_02Q_xagfzRx_KmW6BGDfKcDwLimq5dMskZUiJ3UQIK6zXUYz7sz-sI-t5O-St7AcG_hF6DcugqnQpCzhYQmsGsLpVmChyM5Tm3qfPg8hcgcsGEVolxGw3bnsgPx6XUMfgo4hI0L0tT5AFFj-O2zU9842sjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67276" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67275">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POxs8h_3Y8zs8wUKtK8liOgHUl3m8WiTv9zrJQ2oljkxrDAv1_8Xm98gEMngbgwUqb8zB4hXBpzudRnpYOR0X7_PllkDWk18Zc6TU2tnxf1csyKXiQKtDiXGzT_S73jZdXC6wAEjmIZrgOTU5tPYKX2zm4mhtgHEW0NUthh4Ruwrb4SCpbrh_tFK_CpVNPobbxfN_olQi4v241Vs3taxKtUn0wW5_UZ6Z3lvT5h_3-mABwR3afsi_bNWx-uKp8KAFQM1-Uzu5-WkykXLgo1cL63yxu3MJRnYL3CScuCjXLS-9aPsp15jjRWYu7WRE9RJguoHVAuOwpa6-e4gxxADBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمال مجازی‌شدن مدارس و دانشگاه‌ها در سال جاری!
🔴
میزان کسری گاز به حدود ۶۳۰ میلیون مترمکعب رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67275" target="_blank">📅 14:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67274">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adF0BIwKZIk5dReh8bkNZTi0p6aTE6a7ZC8_YIgbMptyKcNkDLU-JnUocZkkA_DL3Tb77xqEG_IipLETWR7rQ1uOCUChou7fQOaNhjqGPK7m8lQmFVnQCtblbcI1eeFZ8MG-7AGrtrlRI9qOQmBD1s0w6OK5lbqnSJLPKWZKfPb9QNTgDrGk_pAU9oRIVMHRuVIEGxjwaeunuQblRRqj-C3VMj1nvTAOA6F9ziArFm3A3xw-HNEgT7B-wZH4moW4EjjVZxD515b7_4OhkA7-W-aYTr1G2vdmu4Pjbwy-3EM0YHIlc-nWeDnVFLnqaqt0CdddWisPAJlufWl-GStUJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برافراشتن پرچم «ترامپ را بکشید» در مراسم وداع با جسد علی خامنه‌ای:
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67274" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67273">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=sOimrizgG8mBJSEUxfbLHrIBA4P4wq6-gnjdWh7-rnyz6AV9vzPlweumH54mp15vvdYuZytIcRHbi6npRrceTwm9AcrizIZ5GBpOaNeWuviN9NgGWHWylPakOYjbjV6cSVbhgdUaDo03FPwEVGIPJGMr-QMob2M75SH-jrAMyHUcDkl0KoqTlOp8IsRoZIiz825yzM5Jh9qmwqvcxIDOomV2uBbooz5ibwVKg2YjYuqV64Yc33veIG6g8Z4jjcSG_TD8s5KFthyAlMkv1gIFALTflKexkHYBdyHqml_To0coG4DC0Y7hww7ip31arMafBG9RQ01E9bSor1QbxHOrww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=sOimrizgG8mBJSEUxfbLHrIBA4P4wq6-gnjdWh7-rnyz6AV9vzPlweumH54mp15vvdYuZytIcRHbi6npRrceTwm9AcrizIZ5GBpOaNeWuviN9NgGWHWylPakOYjbjV6cSVbhgdUaDo03FPwEVGIPJGMr-QMob2M75SH-jrAMyHUcDkl0KoqTlOp8IsRoZIiz825yzM5Jh9qmwqvcxIDOomV2uBbooz5ibwVKg2YjYuqV64Yc33veIG6g8Z4jjcSG_TD8s5KFthyAlMkv1gIFALTflKexkHYBdyHqml_To0coG4DC0Y7hww7ip31arMafBG9RQ01E9bSor1QbxHOrww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش نکیر و منکر بعد از ۱۲۰ روز
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67273" target="_blank">📅 13:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67272">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obqSYOeJUWASUKISesudM196NJC23J5lA3U1wUmjWidEWlgTS6ZhVTmS4L4qwyBlsu2cNWJvgDHSLO08S3steB_QGAUFYoPTFEnuxbEIvgRuMMIk-rj_l70mDzo50SmdTzjItnRliU4jV8oyYfBojnqSQld1EaGrZoJToC9mDXyxceYqMtp7SNWRJfoC87_DSuEStcOoNzk6C7POMiSHjHdxb5Ezs2b4-2GqyWQ8nj6ouHD4X7xDoF8Gj7A4ORDMHQ_lKPdVhJSX7ErBbcoTyHGdXZFHlhN-6BYQWV7sOZei9OTOUr398deiwfL9PJApG0VtmEAFNUmi4lf5KRnsCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
التماس رسانه حکومتی در ایتا برای حضور در مراسم ؛ جمعیت کم است...
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67272" target="_blank">📅 12:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67271">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=AGrSsru-UVIBD9nSWqcbFZeDVibMnaWt5JPunUma0BvgN8gZayeOxqF7qNVxzM1mVwxC6oLwIJ4X8Hh0u0YcV9oRfbR8De9sUfTGDpPYy0Gz2Fbvfk65H6fynjA3EC5Za9B7D-_WdpFaSh6qs-PFMV4ze55E_YzNHc6X_SPVz3xcN50DOxXjJPChn7HRvpohMgyUBSoHOUFl-ltJqm_FnpQff2En-LMsjtz6srKYaVbnLmZnxNEWH9pHY_BnC8OVg94-jVlPJpt6eugCXYuWasIh27nrswKwRcd5j57fG4TQ_OGz7-4ut8jQ_W7x27J4BoUSBVWAZgNXlnSu62Qwsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=AGrSsru-UVIBD9nSWqcbFZeDVibMnaWt5JPunUma0BvgN8gZayeOxqF7qNVxzM1mVwxC6oLwIJ4X8Hh0u0YcV9oRfbR8De9sUfTGDpPYy0Gz2Fbvfk65H6fynjA3EC5Za9B7D-_WdpFaSh6qs-PFMV4ze55E_YzNHc6X_SPVz3xcN50DOxXjJPChn7HRvpohMgyUBSoHOUFl-ltJqm_FnpQff2En-LMsjtz6srKYaVbnLmZnxNEWH9pHY_BnC8OVg94-jVlPJpt6eugCXYuWasIh27nrswKwRcd5j57fG4TQ_OGz7-4ut8jQ_W7x27J4BoUSBVWAZgNXlnSu62Qwsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیو ای
از بمباران بیت رهبری9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67271" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67270">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=J39ksw5_zdA1OWkHQ_ZK6fWEXaezj2q5jeLmraEgEdqxmHLP6uhtKw6r1K63gF7E8hcUC1P1jzo29PkgwIQj0URUs9rf0JwiB7Qu9Rz1OHznCDqRd6YFjLfU57KyJJp86TjPyVe-5yecPboSVQO2ZqS_33aQ_JCJDTwna8mNYXw3d1ZyCO9H1D4oqFUrRT6nmTsvby1SZuPFvpd4JrNVmEFVTY3ITBbpLyWj5gMCwMmGZS20Xg3Z4ZtDNxNoSmSM6MMiUc3SZXHF40wdBLnDXpYijVrqviUb6-dJlylxdMr9wdORWQCW7eniMpZxT4tn5yURyZoH6Br6x4gGbUIR_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=J39ksw5_zdA1OWkHQ_ZK6fWEXaezj2q5jeLmraEgEdqxmHLP6uhtKw6r1K63gF7E8hcUC1P1jzo29PkgwIQj0URUs9rf0JwiB7Qu9Rz1OHznCDqRd6YFjLfU57KyJJp86TjPyVe-5yecPboSVQO2ZqS_33aQ_JCJDTwna8mNYXw3d1ZyCO9H1D4oqFUrRT6nmTsvby1SZuPFvpd4JrNVmEFVTY3ITBbpLyWj5gMCwMmGZS20Xg3Z4ZtDNxNoSmSM6MMiUc3SZXHF40wdBLnDXpYijVrqviUb6-dJlylxdMr9wdORWQCW7eniMpZxT4tn5yURyZoH6Br6x4gGbUIR_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار مرگ بر آمریکا در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67270" target="_blank">📅 11:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67268">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=S5YJmKl8dyuBQoBzGaHbil0tEg_PGWa5PJSf5vdSPB7i0vQSX78qgIKRg-4JVw5ZLqtH4ObngaR6opTggMcONMeiF63qir4xZOHOlBLO18koPIcxwZqETABGtcIIDkjRGlVKyJZcC8h2EUCCsKrZPp8zAh8-mWiGHM78arhGmH2ZIfDlhq-dl6p_3fi1NFSGZuGJbxLKmz8ftNofr83sLMZhVJsccJsNs26dEFWfrR5RgqsASG-QjCFsHj1nOv2bgsqZXC6qB6FW1H5KLCi0NWB5Bg1c8pvuhnBm2pBFC8qQS9ktwCY0xX-gfrUY4S68GoiWGSpk-SqWKpWheiQi9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=S5YJmKl8dyuBQoBzGaHbil0tEg_PGWa5PJSf5vdSPB7i0vQSX78qgIKRg-4JVw5ZLqtH4ObngaR6opTggMcONMeiF63qir4xZOHOlBLO18koPIcxwZqETABGtcIIDkjRGlVKyJZcC8h2EUCCsKrZPp8zAh8-mWiGHM78arhGmH2ZIfDlhq-dl6p_3fi1NFSGZuGJbxLKmz8ftNofr83sLMZhVJsccJsNs26dEFWfrR5RgqsASG-QjCFsHj1nOv2bgsqZXC6qB6FW1H5KLCi0NWB5Bg1c8pvuhnBm2pBFC8qQS9ktwCY0xX-gfrUY4S68GoiWGSpk-SqWKpWheiQi9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از پرواز جنگنده‌های اسرائیلی بر فراز بیروت در مراسم تشییع جنازه حسن نصرالله دبیر کل حزب‌الله لبنان بین سالهای1992تا2024!
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67268" target="_blank">📅 11:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67267">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=Xaqnkdhgrk0W2CHa5bYgJ3gE8IrRGRSXhrRHprOTZrgyZQytxEEZlajBp9_8xhlGRVPez4S6t5Vkhv02I1e97W6YMCj_s98mabc-3yTQfEhJ-m9uM9qkwT9VEdb3JYTJAmsk1VMND6vWX4wG2F1Z8JDejvrgM43KShfr_qov9lpJXXDlDAXkjBfpvlxvvbd_AUM7s_DwxcgdycDgZG2AqzaLh31G_9Twb1h_aTKR4SySYNOzgV-_SVmMOOeiU_q8yPEFdYOaMEltf9wxxUIh7OItiQsglh1tsgqKgtmge7QCTHGHyQ5ZBLBBRzygbpW-fdvqXqK83pxS5w9uFqPw1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=Xaqnkdhgrk0W2CHa5bYgJ3gE8IrRGRSXhrRHprOTZrgyZQytxEEZlajBp9_8xhlGRVPez4S6t5Vkhv02I1e97W6YMCj_s98mabc-3yTQfEhJ-m9uM9qkwT9VEdb3JYTJAmsk1VMND6vWX4wG2F1Z8JDejvrgM43KShfr_qov9lpJXXDlDAXkjBfpvlxvvbd_AUM7s_DwxcgdycDgZG2AqzaLh31G_9Twb1h_aTKR4SySYNOzgV-_SVmMOOeiU_q8yPEFdYOaMEltf9wxxUIh7OItiQsglh1tsgqKgtmge7QCTHGHyQ5ZBLBBRzygbpW-fdvqXqK83pxS5w9uFqPw1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مایک والتز نماینده ایالات متحده خطاب به نماینده جمهوری اسلامی در شورای امنیت سازمان ملل :
🔴
اینجا تهران نیست که بخواهید همه را خفه کنید ، اینجا آمریکا است ، اینجا سازمان ملل است. این اسناد حملات شما به مناطق مسکونی بحرین است که دروغ نمی‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67267" target="_blank">📅 10:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67266">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=sD9YVzmY-1R6S9sv_2Zsv_nNhzipIsKvdjlecpWKHelhS5QKRx5RSq8xcm7UA9CGa3NI5O3ZAbkdSzLsbqX37daJmIBJL_sNbb6dptGFWEatQjyN5KWhJ6bta1tWGXh1w1pOg_zK5sjOHuDNlWUjtL8ANsNpXXvSyMDAlwRqcQH3Ybt-brAm7YowYCBlCntlgRsu6KHN_S-h2VICA1MJ_4q4SWE3SUt1l8q1wl3vRTlfmdnwVxYVTXGY7w1FjmxzDgKe7lL2lwEFwrhQJdBt8R6uABJpRAhD-35_xW_Xjka9VIX8Nz_kR4cBYwlEumq2JwkpPh4Vy7pgPwWPNl2RjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=sD9YVzmY-1R6S9sv_2Zsv_nNhzipIsKvdjlecpWKHelhS5QKRx5RSq8xcm7UA9CGa3NI5O3ZAbkdSzLsbqX37daJmIBJL_sNbb6dptGFWEatQjyN5KWhJ6bta1tWGXh1w1pOg_zK5sjOHuDNlWUjtL8ANsNpXXvSyMDAlwRqcQH3Ybt-brAm7YowYCBlCntlgRsu6KHN_S-h2VICA1MJ_4q4SWE3SUt1l8q1wl3vRTlfmdnwVxYVTXGY7w1FjmxzDgKe7lL2lwEFwrhQJdBt8R6uABJpRAhD-35_xW_Xjka9VIX8Nz_kR4cBYwlEumq2JwkpPh4Vy7pgPwWPNl2RjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
وقتی تو ایران میخوای پیشرفت کنی
واکنش آخوندا:
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67266" target="_blank">📅 10:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67265">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=AUdnfPywUPh0oJ8ZaotutBlB6gwBug4Np956txN70-5UYu3Qxab_YHwuBJifE5fjrc_UXewNLDnxplp6h5T-V2GcsBo9ptiEJx_1ngkWd7WqH7av_AQqAHvMmrfb9vWFF-nwgzDIH9g1IfpjJ4XOQkXht42EW9HSHvpkQ486z51OmCPj-gTFm4VoX45oAAY7QYjL6wLd36CbyKmTPpfPg9qyHt8PQEtVJ0HNNpDdWAx9pfMCHMeTy2ZWnDM9E7HGiDlWmbufFP7OX9URzntT67cjR_6YBtZ5ztpI26ywW3_ica_xnR-kLxy6x8pJ6vYPUZZbtTcNlfsqpf5ahpQZVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=AUdnfPywUPh0oJ8ZaotutBlB6gwBug4Np956txN70-5UYu3Qxab_YHwuBJifE5fjrc_UXewNLDnxplp6h5T-V2GcsBo9ptiEJx_1ngkWd7WqH7av_AQqAHvMmrfb9vWFF-nwgzDIH9g1IfpjJ4XOQkXht42EW9HSHvpkQ486z51OmCPj-gTFm4VoX45oAAY7QYjL6wLd36CbyKmTPpfPg9qyHt8PQEtVJ0HNNpDdWAx9pfMCHMeTy2ZWnDM9E7HGiDlWmbufFP7OX9URzntT67cjR_6YBtZ5ztpI26ywW3_ica_xnR-kLxy6x8pJ6vYPUZZbtTcNlfsqpf5ahpQZVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
ما ایران را حسابی درهم کوبیدیم. آن‌ها برای توافق لحظه‌شماری می‌کنند؛ به‌شدت خواهان توافق هستند. ما به خاطر یک مراسم خاکسپاری، یک هفته به آن‌ها مهلت دادیم، چون آدم‌های خوبی هستیم. واقعیت همین است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67265" target="_blank">📅 09:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67264">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=Kv_NOl4egv5VQsK4m0z6_ZeZJFkb0a5F6aSPJVnW2JER0znVKWhcoLHiJHXjtGVEqjfx1_Nn864acYJC6pYVh8mul0AHWpNX-Ntsk9cY1CriNr2R2riICrbG4Cy0F7aBtiKwDtWHkJGUl3GOCh5Yk26K6A4i44FUhdrLgNOKu9lgsJdSMRsUTjz2OiEQuFMDKdnidvDdSwh7c9qrPs4OHlGYAjDTihsAwRV5Lug4-_leEi-RMDrZvuz_oyD5EpFl_wUrOa8quIg2_7cpfOZji4UwiCPCMEccBbngC-dHaeYfHVyiqR_yk9hmX2ydqJ2ePGhk-WOUEv2pUv8PJXptWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=Kv_NOl4egv5VQsK4m0z6_ZeZJFkb0a5F6aSPJVnW2JER0znVKWhcoLHiJHXjtGVEqjfx1_Nn864acYJC6pYVh8mul0AHWpNX-Ntsk9cY1CriNr2R2riICrbG4Cy0F7aBtiKwDtWHkJGUl3GOCh5Yk26K6A4i44FUhdrLgNOKu9lgsJdSMRsUTjz2OiEQuFMDKdnidvDdSwh7c9qrPs4OHlGYAjDTihsAwRV5Lug4-_leEi-RMDrZvuz_oyD5EpFl_wUrOa8quIg2_7cpfOZji4UwiCPCMEccBbngC-dHaeYfHVyiqR_yk9hmX2ydqJ2ePGhk-WOUEv2pUv8PJXptWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
آمریکا یکی از داکترین هاش برای به زانو درآوردن کشور مقابل اینه که هزینه ملیشون رو بالا میبره مانند شوروی که همینجور کمرش رو شکوند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67264" target="_blank">📅 09:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67263">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⏸
مستند کامل و 46دقیقه ای شبکه 14 اسرائیل به نام از «چشمان جاسوسی در تهران»:
این مستند جنجالی دیشب از شبکه 14 اسرائیل پخش شد.این نسخه زیر نویس فارسی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67263" target="_blank">📅 09:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67262">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/iDc5g5XWf24_GS7LzbEEIohllN5bn8mEW5OUAzOPTPselah1bBQ_26agpnc8pzRCFM9je6lRVtVpfc7YWAR8qLNqDUyw22lVVOdu9CG03NpCWtYE1K-Mruv_TEt5wkblqPbneGOMGfBf0frcVWhuUSNtZrs2sakJFjSf9LBLkF7JTcO2jYRZHxr1bZ0NtMUGmSNBLpPeq5pYjjPWL-IEojEoviUToE_cuz__09dUZc29atHmDj0SKCkExi-49dmvOOdCF4t1LiouLC-le5COc9b5lrzLdXntlV3gr4ryhEwX4qxWZm5P0AjlWdLOqCaYIuh7mGi13SINGH74pASAOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67262" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67261">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet @Vision_Bet @Vision_Bet @Vision_Bet</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67261" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67260">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t1aX0VEaj_6vG_XKCB2PtZXwp93cQ2JaViOql31dCAjmhQBc4vEEiGV3Y3w_KXZk-kRmcLTj0xbBzd_Jnmye-W8Dmjza27CDYiaz0w8o_59TmDFwcCns14NprbjBNYJ1dEXItT6mdS0W_EFcu9pe3cvBdzvwxZs7Carb0sVg4PBISMWIzzqYYa8e5sZHHntli8mgi_gqOWicCVPhxyY0EqMaNBxLqNAYsQCi_G0wfycxgfTNT6fqhG8jdlyRVTxjyqwZuQOy77TZy89WFx-mv7ixYsQArBJ25b-1DbkRBT5iNmBaVdaNwsfSdovv5NXC9oyv8wPAnG80sJGF_nwHeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67260" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67259">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل:
اسرائیل آماده است به صورت مستقل با جمهوری اسلامی وارد نبرد تمام عیار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67259" target="_blank">📅 00:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67258">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=W1xRzgUUeBhq4qsYa0lh4Y2YQofFFq9sKxSndD8WlVoe-kExDrnr5JYFJRiaLUN_FuSxEcYN1QIkbZVwpQTGWlccmfEpBi3c7CbArlQ_WxhH3fQ8BzH8x5IBBG1KAbBRyjwVaUE0rH_kgR832EBnAksdJ-Gw9tUBiILfKBArYVwHksa8IK-YwUKFDKZJLA6h423nqjiuyZT-SUvcKGCbyxdEZYe0hFx412VqO6NIsZMOuis3edaFzFPOk3zBSwECK9qj8p4pVmBS59_rYDL947jSo2V25z1xcqdbzhED5xRBjvI_twywXclOxP8T0rn4LrWZ-c-DqqHhatYfOr1hYQVCpWcH5gQZfGFMBQDCChDs-pP8m6MVADT4yQCfX9wFPlu7UpiTHXVhiwNfqf1MXE_YC-j28EUr6SkCSzuXkWeHV4Jgsj_Ciu6uYb93jozJqvCkrgkleOUw7Kuw1vgqo0NNVkLtcsDqkjRhAF4pbZ5uNNMkFn1Jn3ghJZMC43hLUsP_dK7ncOys-GXqdcI2dYwLue6dGyggLz5JDYFa_W4uqJnLPpD-xvJiW2c9IGnyYNv6zmSPVvtPcC2xNxpwgjpJza7OWkg_bkUHvjyNFuk-ovh-rNiJAUwEGLDLQQ3QrVy9gyl5t52cjhotyakkbcg0W1cfiXY5fT4FkAMqHjk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=W1xRzgUUeBhq4qsYa0lh4Y2YQofFFq9sKxSndD8WlVoe-kExDrnr5JYFJRiaLUN_FuSxEcYN1QIkbZVwpQTGWlccmfEpBi3c7CbArlQ_WxhH3fQ8BzH8x5IBBG1KAbBRyjwVaUE0rH_kgR832EBnAksdJ-Gw9tUBiILfKBArYVwHksa8IK-YwUKFDKZJLA6h423nqjiuyZT-SUvcKGCbyxdEZYe0hFx412VqO6NIsZMOuis3edaFzFPOk3zBSwECK9qj8p4pVmBS59_rYDL947jSo2V25z1xcqdbzhED5xRBjvI_twywXclOxP8T0rn4LrWZ-c-DqqHhatYfOr1hYQVCpWcH5gQZfGFMBQDCChDs-pP8m6MVADT4yQCfX9wFPlu7UpiTHXVhiwNfqf1MXE_YC-j28EUr6SkCSzuXkWeHV4Jgsj_Ciu6uYb93jozJqvCkrgkleOUw7Kuw1vgqo0NNVkLtcsDqkjRhAF4pbZ5uNNMkFn1Jn3ghJZMC43hLUsP_dK7ncOys-GXqdcI2dYwLue6dGyggLz5JDYFa_W4uqJnLPpD-xvJiW2c9IGnyYNv6zmSPVvtPcC2xNxpwgjpJza7OWkg_bkUHvjyNFuk-ovh-rNiJAUwEGLDLQQ3QrVy9gyl5t52cjhotyakkbcg0W1cfiXY5fT4FkAMqHjk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
هواپیماهای اف-۵ و بمب‌افکن‌های بی-۲ بر فراز نمایشگاه بزرگ ایالتی آمریکا در حال پرواز هستند و جمعیت از پایین نظاره‌گر آنها هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67258" target="_blank">📅 00:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67257">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=Z-q0h7QNNPZv9vsauvXADz7dfTyscVpvr87yUOMpjObDl46zLfKr4YE0hFZybbZ0krp2wcGiwA97kW2foyE3jDn21L3k10RUWvz07xU7jZJ88RtF2Ov6YM62-Q1cqJtxVXM4KGTfM1EQKZpn5UYLxNMUDevssNT8fqm88ArNuzIFMf_T7UJOGnLlD7buRtTmLlRQ-MDDk4tYz6b3a9P8mwuvzBqbBfiKyogqF-qeuTTsjfAPfw8M0jEPcY7rVJzf8spga2BswY5910QzPYbTQKQlvP_C6-ihQh_oq-kg_n8cWvisCEqrVI-OeHEvl8saO-MCLUO9gKyxZN3BXjDXSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=Z-q0h7QNNPZv9vsauvXADz7dfTyscVpvr87yUOMpjObDl46zLfKr4YE0hFZybbZ0krp2wcGiwA97kW2foyE3jDn21L3k10RUWvz07xU7jZJ88RtF2Ov6YM62-Q1cqJtxVXM4KGTfM1EQKZpn5UYLxNMUDevssNT8fqm88ArNuzIFMf_T7UJOGnLlD7buRtTmLlRQ-MDDk4tYz6b3a9P8mwuvzBqbBfiKyogqF-qeuTTsjfAPfw8M0jEPcY7rVJzf8spga2BswY5910QzPYbTQKQlvP_C6-ihQh_oq-kg_n8cWvisCEqrVI-OeHEvl8saO-MCLUO9gKyxZN3BXjDXSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با هر ثانیه این ویدیو سوپرایز میشید
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/67257" target="_blank">📅 23:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67256">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=GsmsU_9ZfJB4JouQjnz9t39ti1MYbWrp20y3Fj3U5qB-58_OZNm7cdPYTH9kVGm8Cqb3DCz3zxBUGv0Ru0cRNmtqJ83cowCRvHtQF4zlag5sUsubYU6EFzGKvfhpO1dUmlVZmHYTnPcPfsLn6G3vl3DTQR2wTvKMA3S89SOzqlH-5ium4OSK5qMhqOKrITpu7jHiix_BFhm5tDsNY7IsH3iuP14UBbeyDrbXO3PIegMm-OZDpcecpoMqqPjZPnEaXQTCH8D5FpMW-FX_oLKjf2EmfzUQ0LRHLTLqgOx5-vVs5t4b9VI2zGU48skXJu0J8FrlAiejvf0Dx2SZSXwO-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=GsmsU_9ZfJB4JouQjnz9t39ti1MYbWrp20y3Fj3U5qB-58_OZNm7cdPYTH9kVGm8Cqb3DCz3zxBUGv0Ru0cRNmtqJ83cowCRvHtQF4zlag5sUsubYU6EFzGKvfhpO1dUmlVZmHYTnPcPfsLn6G3vl3DTQR2wTvKMA3S89SOzqlH-5ium4OSK5qMhqOKrITpu7jHiix_BFhm5tDsNY7IsH3iuP14UBbeyDrbXO3PIegMm-OZDpcecpoMqqPjZPnEaXQTCH8D5FpMW-FX_oLKjf2EmfzUQ0LRHLTLqgOx5-vVs5t4b9VI2zGU48skXJu0J8FrlAiejvf0Dx2SZSXwO-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عزاداری مجری آیت‌الله بی‌بی‌سی از سران حاضر تو مراسم تشییع خامنه‌ای بهتر بود
😂
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67256" target="_blank">📅 23:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67255">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=uF4l6_Oxl8gYa_q63VZb7VSCUrnBsevTJJqGgQTmrloM3uelng7gZ9fAC8MO6bln48Crkf83hB5gbmxsFHafkPtZtxLv14Pxv0LfxHy8cPh9lU77X3ShJ3va2yORDt0XM4NfFvENNSq_SQBo2MgOVDTBM-kkynqbUOr88n0mXksvML5FJrDj0823NhtVhI8AWZRn-KMTvI84ILceSxPTzp-wfpYkqWx8LY4lQcF9ErimDsHorn3ElMRynVHORqqzaqo_KPkVhwkPjkJF6gogpAHIu_Iqg_nXiuQSO6HkfJhfMc4axGyydRp-T1-vkq_76runCAZjUc8VwxyN__ZJUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=uF4l6_Oxl8gYa_q63VZb7VSCUrnBsevTJJqGgQTmrloM3uelng7gZ9fAC8MO6bln48Crkf83hB5gbmxsFHafkPtZtxLv14Pxv0LfxHy8cPh9lU77X3ShJ3va2yORDt0XM4NfFvENNSq_SQBo2MgOVDTBM-kkynqbUOr88n0mXksvML5FJrDj0823NhtVhI8AWZRn-KMTvI84ILceSxPTzp-wfpYkqWx8LY4lQcF9ErimDsHorn3ElMRynVHORqqzaqo_KPkVhwkPjkJF6gogpAHIu_Iqg_nXiuQSO6HkfJhfMc4axGyydRp-T1-vkq_76runCAZjUc8VwxyN__ZJUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر شلیک موشک‌های بالستیک آمریکا از کویت به سوی مواضع رژیم جمهوری
اسلامی
منتشر شد
ویدئوهای منتشرشده نشان می‌دهد نیروهای آمریکایی مستقر در کویت، موشک‌های دقیق ATACMS و PrSM را از سامانه‌های پرتابگر M142 HIMARS به سمت اهدافی در خاک تحت کنترل رژیم جمهوری اسلامی شلیک می‌کنند
.
بر اساس توضیحات منتشرشده، این تصاویر مربوط به ۲۸ فوریه ۲۰۲۶ است و بخشی از عملیات نظامی آمریکا علیه زیرساخت‌ها و مواضع رژیم جمهوری اسلامی را به نمایش می‌گذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67255" target="_blank">📅 22:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67254">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3720a35424.mp4?token=ui-nCyCzKZiDJ1pSi4bHZDcfScY9X07WpRPuvhvPifQNioshVTP5BMmgwccHEGCyK9qqaxuFtAEP9aN5LbxxB4gvSw1D0CasIuYOoihpT6NU4VkEyKam_f2tcvommX_6ttl3-lRbUl1nagK-14jeTZIwhKo7SfLXRALjKQxFWh7mMhKomTdCeRq2a4nfIncowMP3JuwS8vnl76oacLDpqOGBsDP0kruXBkdjVsa9_WguqFSyEIRXBKrPGjM4PQ57G1Ri8F9PLYM4lKUTLk_trGtioAhSBfT3IMUBnRHtVnPQwbudtWDvl6Z-9E6QYQUtaodB3MEvodcMsXmUUjVF0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3720a35424.mp4?token=ui-nCyCzKZiDJ1pSi4bHZDcfScY9X07WpRPuvhvPifQNioshVTP5BMmgwccHEGCyK9qqaxuFtAEP9aN5LbxxB4gvSw1D0CasIuYOoihpT6NU4VkEyKam_f2tcvommX_6ttl3-lRbUl1nagK-14jeTZIwhKo7SfLXRALjKQxFWh7mMhKomTdCeRq2a4nfIncowMP3JuwS8vnl76oacLDpqOGBsDP0kruXBkdjVsa9_WguqFSyEIRXBKrPGjM4PQ57G1Ri8F9PLYM4lKUTLk_trGtioAhSBfT3IMUBnRHtVnPQwbudtWDvl6Z-9E6QYQUtaodB3MEvodcMsXmUUjVF0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ورود خودروی حامل‌ جنازه علی خامنه‌ای به‌مصلی تهران
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67254" target="_blank">📅 22:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67253">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEY4gkDS3tXC1opPZioNSHpYf-n1U-ZRqAxdlNsGb3g-Cyn4Uc1HHSDMct4soQoHheTaU73uM251VlAK5iK_uVSTisR717W1a0WPoNpCYm442cjCNZ7N7J29b3Fnzlxy8T2TlwAeD4DLg8z4jLU5WNZR2NC7eVDiP_O98JfqSxKHVsz_Qf9EE58kFEtGUPuO2IlM50g9BZonVnLfVMrNw_X9XapcZv8Jga38C5eGX6Bjz0gF7x3R5FWVxUDNsC2QPNdYwcW44X4mhicYWobkkcMmjE2i_gBrreDvKmE86dNnn2GZtOCLbUUu9EkW_tEPTzOQ7bA7axJCHpXkCVKkig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سید مجید نقطه زن فرمانده هوافضای سپاه هم بالاخره از سوراخ اومد بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67253" target="_blank">📅 21:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67252">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rveQDZSS1e4B6JSgq2y2b7y-rOEbugHY6uz9sprp5lFwJG7EBrV22lY2aeHjBEUYf2ENpsTGS9GmnS45N8m_7kius3c3nra9JlzMr3FrXafVP6DV5WrqIAaPoVioOr4tCWxQHpJB5wbDwQ5rVmCrQY47tcuqO4fUd_QbVoKfIzDEun0DPlmKY8Yf_3hMePyTDiPGBjswSmX8DiLd8RD4kujzetDvI5DNMOXG_9wjBYvjEpCK28k03EED6oa_BFobbaAHOEAN3TUkAQ-APPyujVpxn8PMk_WKN782KW83phkqjOidc6SesjXdmkH4QvnieeiH2Iaz7g2u86ppwTX8Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ: ۵۸ میلیون بشکه نفت و میعانات رژیم روی آب مانده است.
حدود ۵۸ میلیون بشکه نفت و میعانات متعلق به رژیم تروریستی جمهوری اسلامی روی آب انباشته شده و نزدیک به ۹۰ درصد این محموله‌ها هنوز مشتری یا مقصد نهایی مشخصی ندارند.
بر اساس این گزارش، با وجود تعلیق ۶۰ روزه بخشی از تحریم‌های آمریکا، خریداران بزرگ همچنان با احتیاط عمل می‌کنند و خرید نفت از رژیم جمهوری اسلامی محدود مانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67252" target="_blank">📅 21:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67251">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuZzGJeZKogIns1GftUCl2H83UOTeEfGQsJqIZ6uHhWmW5wdrdQQbeFb0tP7b6Nhum36rm480wqXF-7RdEau3zFnKmdCpm3yDBBzumq71VnzJowkuIWnH552aaN4ZbeiO0N_wga0Kh5-5HsgXM7UIslq9MSnfmWtqW32tHttfVyrbvCjE3cQhnTVq-0lstwyA_aIO4gJFDM0UKJkxl9SWjAlU1Uo8xkNAstjOqNex1IPmN05gT6wjViSne7j8jeIek0kN27Go21IoCpyWNbriOkZJtW_AXlJq08pssirXePVNjv5Q2JSDw8XneYXGQs4QaNgcf1oQKjNv3Kc3vwPlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
نگاه معنادار عراقچی به قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67251" target="_blank">📅 20:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67250">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxX1DCrd_Jgf1lD_9tfXyCI9CbsD29D3mOEkQa3H-hdVUwyMZQ8Kt4K2_CbU_xu3RRrIczDqBaZ-uJsWLLMiY53t6_EBelETmAXFvKyE-4gLcfWAnu_6ULtRuRmCTKGHJ3kNs9oAReaHhQwpkphzinw0JgK2cw6nUAySCC4AbUkmFvk6rCRzYHJa2XpHbZe2nzoCzRB5mGHeX5O3KvdqFQiXzQ6Y2ztTd0PGLwcnPYJEZEzoQvhqEebVk1H-6ogn_HHmO53wydhg3-t_ZCnoQ17WdnPO8bi17m1Y89VgNul7knsFtT3fyGBh-ribvTf7geRSaqZ4sMVpDZOWQ0IJ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید (آکسیوس):
رئیس‌جمهور ترامپ امروز با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، گفتگو کرد. دفتر نخست‌وزیر اسرائیل اعلام کرد که آن‌ها توافق کردند به‌زودی در ایالات متحده با یکدیگر دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67250" target="_blank">📅 20:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67249">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SF5_Y9DTKqmRZry1mamu5aa5h0lczav-F5n_VxF_42_0SDcWFBkNi9q1OTLuoo6_tnt_j_8OtDunN0O43PTFiPPmECwz0Gp7CIRID1FHa6bymPoYu3kEVRVF5G3PC0Fb1I6hc5H0G-9KOgo0XJURmn4yrbvb5yp0Hhw1JfzQ1N71H82iqxY9rcdU8THsSNgu_VdHXq8NkBDAkPDmHVeW1DBDE3xXIDBXcKNoToUSQMN163o1kLI1fYhxgRxmZ486aor5KjgLLTXrTIj1dQflzzV23dvddnHz0nsfey2TrBiyFwe3_dm2WhZT2CCFQFdYa_M6s4MHBnRYub5Inj4tjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
😆
‏سی تی اسکن از دندون عقلم:
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67249" target="_blank">📅 19:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67248">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCroJQgV3BHNTxJb-_7XT9OJY7oP6Ovxg1rbzm_eZVHZTTeHK_6KBtQ0DYx1oVbA49xrqGeTmR4HoCsxkccqpVUyrFDQxTINTO1u6RA__fnjNmT3jgJewPnmbonW9O9_ZbR6-ZxszzBaJYiHgo4O-EdhVXgndwe0pErAin3d1IJju6kaD5mjaIbIj3WFtzzxPvlq2cWj6AY3e-yy7QLjwOaw6n63URjXUMwq_ZuaKLIdCu7ieP_1dopV0ZCf2cDNHbjfw85ulfy7d4xxgjkuHSbNN8xi8Bg72cSCv_SABYtB4_XmjPwRHSR40PGUfxfleHYC9zis6U0wiSJ4-ayocg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دفتر نخست‌وزیر اسرائیل؛
گزارش نیویورک تایمز را که حاکی از آن بود مقامات آمریکایی معتقد بودند اسرائیل در حال توطئه‌ای برای ترور مذاکره‌کنندگان ایرانی در جریان مذاکرات با آمریکایی‌ها در بهار امسال بوده‌اند، رد کرد و آن را «یک تحریف کامل از واقعیت» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67248" target="_blank">📅 19:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67247">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=s-tH-zM9L1-khQLHRpyJSJcV602VVqDk6-L-zl6iJJAts7CHLwz_TlKbLC7I8NY8mYwu1OaHsa_WRWwdmRkAgQIm-0DmmS9uil2f6aHw8IeZuhxrtOUAdlLo43O6W5Q9yXOo_iryRKH_mfRH2ajQodaFWvUD_EfsentNDy17mCM0wwTjdHQUVQAkjjaDRBdF6bz93Jn5eXXveAcUmmGBM4VTXeETtwacny_9H4HAkTbj5oHRLlKQG82ykR7dAil93TGw4ZP5bTgLmszRgRG6-aNIIFj0Q9pVRdGOz4a70hO2SZrqKeVDADwtwI4OLWjIMePD2zgo7XvSsYBXq--ZFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=s-tH-zM9L1-khQLHRpyJSJcV602VVqDk6-L-zl6iJJAts7CHLwz_TlKbLC7I8NY8mYwu1OaHsa_WRWwdmRkAgQIm-0DmmS9uil2f6aHw8IeZuhxrtOUAdlLo43O6W5Q9yXOo_iryRKH_mfRH2ajQodaFWvUD_EfsentNDy17mCM0wwTjdHQUVQAkjjaDRBdF6bz93Jn5eXXveAcUmmGBM4VTXeETtwacny_9H4HAkTbj5oHRLlKQG82ykR7dAil93TGw4ZP5bTgLmszRgRG6-aNIIFj0Q9pVRdGOz4a70hO2SZrqKeVDADwtwI4OLWjIMePD2zgo7XvSsYBXq--ZFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه بمباران بیت رهبری 9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67247" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67246">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/X_xy_moRtWmV5fryZQeAV5z2qhjcDPit41lnHDxivEndZ8AtmpJgjJ7dkQ0WC2Tdh8WQXAva-g2T47dGpuqf8LbLmXcY3RCCMfI4GYA_A4Stjc3U76AFYW0uW7W8C5xF41Y6k4x1WTvBoy5QmLUtTPSwyZBK0KKg-wusXVBCDNlPlehN5x6Z4Jema-itOad4nAkiXLgcd_zgHPVjJKpVERmfS67kz1CQLoTlHaquCHPKtF8ooLrT4E3IK8WgZ5hJNyzab2WXhqmddp-aALhL51W4WvTVUGNLM87Xib2seQRPcYBxNMhqvoE9DKYpQjSJo-mloUIYCYdzzu_t9t_j1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67246" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67245">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=BiO_4WCpKBy9ElbWwyI7i6CZtrUKuY06JzG3Zo8Y7XHahD6zPrDMthSB51gaeR7JgKfEuPCqq42A5JbPOMJoPRXzp03SY4mwPFaMOwHPn8wFg-swaF4N1thXkdol2js3MJ_HbBCQuCuS0bwtft8iqUqex2tAxKPu0ZDRV0jSqXypnM0flYwgL8yh3Oy0zsGI0g2homn8CGVbV2guHATiqNPAvKKXAOATFtKtcuGQU5SYATofQ7KnR9nQQVYHFxqkBJkBWOdDVtSLGkcPJuTTr5Oh_o9KxhPVHnNV_Jwk9Zmn8RkimsIxMrg2U_oHh5HbtU7bnJjzpabhk8ofuPZU5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=BiO_4WCpKBy9ElbWwyI7i6CZtrUKuY06JzG3Zo8Y7XHahD6zPrDMthSB51gaeR7JgKfEuPCqq42A5JbPOMJoPRXzp03SY4mwPFaMOwHPn8wFg-swaF4N1thXkdol2js3MJ_HbBCQuCuS0bwtft8iqUqex2tAxKPu0ZDRV0jSqXypnM0flYwgL8yh3Oy0zsGI0g2homn8CGVbV2guHATiqNPAvKKXAOATFtKtcuGQU5SYATofQ7KnR9nQQVYHFxqkBJkBWOdDVtSLGkcPJuTTr5Oh_o9KxhPVHnNV_Jwk9Zmn8RkimsIxMrg2U_oHh5HbtU7bnJjzpabhk8ofuPZU5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بغض و گریه های تمام نشدنی قالیباف در مراسم وداع با علی خامنه ای:
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67245" target="_blank">📅 19:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67244">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=vKL-DIKRIVVur4MyODRkq6xQf9yFrQO5xBbvA-b7oQx-gRhy4_tvNcG7hfNJ2dEO-fsrF0nWknwDTL4OzKL6oX1NurHIJGvwWct06iGhjW4Pkpa4AtC_IhyGBpFnUr9N868ZUcFhaZsoSy12C_LUVMRbhrwMJ5rnMbY2HCVSO4QeIDe6nEjK6PWdTLN1jMMOCjOGGpG3pM4Zubzub4QAkikn2ojK6QFjnu-AnEcNJ_jWOMu5RFErpros37gqbGBu_rsGVQnPc5Ae-kRjfrf8ez1h14isz1tk0qd7VlNsL2138XbeYT0KFoIUvduyoKUnCgtzViDuJabln6vzA4zuuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=vKL-DIKRIVVur4MyODRkq6xQf9yFrQO5xBbvA-b7oQx-gRhy4_tvNcG7hfNJ2dEO-fsrF0nWknwDTL4OzKL6oX1NurHIJGvwWct06iGhjW4Pkpa4AtC_IhyGBpFnUr9N868ZUcFhaZsoSy12C_LUVMRbhrwMJ5rnMbY2HCVSO4QeIDe6nEjK6PWdTLN1jMMOCjOGGpG3pM4Zubzub4QAkikn2ojK6QFjnu-AnEcNJ_jWOMu5RFErpros37gqbGBu_rsGVQnPc5Ae-kRjfrf8ez1h14isz1tk0qd7VlNsL2138XbeYT0KFoIUvduyoKUnCgtzViDuJabln6vzA4zuuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد سردِ حدادعادل ( پدرزن مجتبی خامنه‌ای ) با عراقچی و قالیباف
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67244" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67243">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=MEGg4NcR7oBeD3r6UqbzlBtk5BP2FbukjO5jXVQb_oeupWPLUKktPy21CRvycg3zI93IZNQfwSyqA9symuHQnths9nGOuLmX0Pl6HvCWPj3d16X2eDRi_tsveNbc5PNBe2q97DhPp27k-NfCax_Is09rSvCOheB7cyqy5a9nJSA4C1AfvXgMxrLliJFfU_FgqSbg6n_EsssOujtwxzB3M25Dd0azsQSn_SR1jRwpST2iuTjXIdBgxBc-zHo_6sm5lyxj281i3Efv9jOiF-JLKyuh0NgpXvuU86LyZon6AebxOwY71AWsk-dwYuDzOztDImUwqlYj7cXC1hvhhCbJ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=MEGg4NcR7oBeD3r6UqbzlBtk5BP2FbukjO5jXVQb_oeupWPLUKktPy21CRvycg3zI93IZNQfwSyqA9symuHQnths9nGOuLmX0Pl6HvCWPj3d16X2eDRi_tsveNbc5PNBe2q97DhPp27k-NfCax_Is09rSvCOheB7cyqy5a9nJSA4C1AfvXgMxrLliJFfU_FgqSbg6n_EsssOujtwxzB3M25Dd0azsQSn_SR1jRwpST2iuTjXIdBgxBc-zHo_6sm5lyxj281i3Efv9jOiF-JLKyuh0NgpXvuU86LyZon6AebxOwY71AWsk-dwYuDzOztDImUwqlYj7cXC1hvhhCbJ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپی قدیمی مربوط به انتخابات ۸۴
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67243" target="_blank">📅 18:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67242">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKSl1efFutzsrFA5mbeXG_j9xSYrUKYmiUvFv90fOt_2qkIWB1HYefXzv7p6SsnrebIViaWB6P3GB5JCt2wQ0hxNPkERJmmKN9M1tW4yF3AR3r9Ku5xl49amSq2W_gOwv10-T_LLN-9dGowPN9FEYYfEGIjW0ids33r04fkYUqI70wz7cc8yxkM32xx2yDrU6edObIdmTrdYz-XJVcgmR8PxMBn5dTN_o0pPqlOVhrMF4-O9vJkB0qL3pDRHUqUOV_R56LJgxmaFfKxJNPtaGJL2a13pD6SL7Wr3TRqsIzaBH-ZB-nLiJ1UQC6TvSHNH-r9wBMGQAJGtT4zObQKmng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهره خوشحال پزشکیان در استقبال از مقامات کشورها
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67242" target="_blank">📅 17:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67241">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=n1Vy_qYGFeDo0ZHpV2G4KmsqSbBJv4iD7U5N7mOMkcYD26zUHmrxkzJkCIB0OBmtVwJrEZSr78dgykED-iANKA3ueHpvNed-iGhobj71L0gMrVOGSA05EqCeVmLo2SxWEFoTafzFCuGbENRz8qwAtj0vw6V5ePl0DIrAxpzUvX6iZq9FxGXrndkCd59N_Z5Z8axRqxPCudO0_EIa3NMqDsQmOlDwjsEhIocjbHVRIcholRM4xASfnDyWuAF5Hm49iWwhC_EAkYDp3tyyz-CtkuzCzfHvw-rEk92VfuZOMcCg_rbuUdM4t1FigF9Zeyso9pOQxGYNfqjosUyUp6J-wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=n1Vy_qYGFeDo0ZHpV2G4KmsqSbBJv4iD7U5N7mOMkcYD26zUHmrxkzJkCIB0OBmtVwJrEZSr78dgykED-iANKA3ueHpvNed-iGhobj71L0gMrVOGSA05EqCeVmLo2SxWEFoTafzFCuGbENRz8qwAtj0vw6V5ePl0DIrAxpzUvX6iZq9FxGXrndkCd59N_Z5Z8axRqxPCudO0_EIa3NMqDsQmOlDwjsEhIocjbHVRIcholRM4xASfnDyWuAF5Hm49iWwhC_EAkYDp3tyyz-CtkuzCzfHvw-rEk92VfuZOMcCg_rbuUdM4t1FigF9Zeyso9pOQxGYNfqjosUyUp6J-wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان در تلاش برای جاری شدن قطره ای اشک از چشمانش
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67241" target="_blank">📅 17:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67240">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=p_q6d_rCKhtAE_Pz_Eq34A3Xh6C_BDkwolIvUsnRcISoFnRlXbOupOlOoLV-nbJqLyEXlk_TBy4X3IN-eAnzn8BdAFEWCn4iRgEXil6wrvBmMHQtocwPTue9wmHEg0m9A20Ttp65ShGOh65Pvox8K7HIK1ECsDL-Niw3xJiL_caYDxEr-p5rJutV3Z-cNCys727Rq1GJYzoGyho7Y94DKKh2q8o0k7wvJdJU3gFoeM1JUlqu1vnFOq8raVAhMsHvCbSjBN_8YCan5wb_aGNHLYGfhAUzggJr5ezrov0FykLC36dchOzqZ_VXN-I3XmTpfXp8-RnXQ1UaMh_sdJxSZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=p_q6d_rCKhtAE_Pz_Eq34A3Xh6C_BDkwolIvUsnRcISoFnRlXbOupOlOoLV-nbJqLyEXlk_TBy4X3IN-eAnzn8BdAFEWCn4iRgEXil6wrvBmMHQtocwPTue9wmHEg0m9A20Ttp65ShGOh65Pvox8K7HIK1ECsDL-Niw3xJiL_caYDxEr-p5rJutV3Z-cNCys727Rq1GJYzoGyho7Y94DKKh2q8o0k7wvJdJU3gFoeM1JUlqu1vnFOq8raVAhMsHvCbSjBN_8YCan5wb_aGNHLYGfhAUzggJr5ezrov0FykLC36dchOzqZ_VXN-I3XmTpfXp8-RnXQ1UaMh_sdJxSZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در یک سو مردمی که در زباله‌‌ها باید دنبال غذا بگردند و در سوی دیگر «تامین ۱۲ هزار تن کالای اساسی برای تشییع قاتل فرزندان ایران زمین و عامل شماره یک تمامی مصیبتهای مردم ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67240" target="_blank">📅 16:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67238">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=d6ZUDeqp53P3PcJaAXC_idYMxn2R7KRjvlTb2ajX69KKb9AVniByj62omz2t99W_eJKVsWnyEQ8PQ2PHvk_lsiXX4awZ0eGnA8_bSg8Jk_2ywVynjGG69fnvlObYI150KFzxXGhyu47kAWRqo1aayZEP0891ZFnPbo64uYDDs3ClduTf5FepDA17FWLDof-mlVM1IvC1j8aXuLdti_f7_tkJZVWJnhUJwcxzwGrumNej7CLKULEWQ2zYQMm7DDic9Q4QbJ_PI9vXeVQw_SuWOJYmAtH4m3dGaE46HKZ5QK5Mf5Jow_ZI3YsB5RF9h6abHgGvpUSznw51TUxBCOwXpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=d6ZUDeqp53P3PcJaAXC_idYMxn2R7KRjvlTb2ajX69KKb9AVniByj62omz2t99W_eJKVsWnyEQ8PQ2PHvk_lsiXX4awZ0eGnA8_bSg8Jk_2ywVynjGG69fnvlObYI150KFzxXGhyu47kAWRqo1aayZEP0891ZFnPbo64uYDDs3ClduTf5FepDA17FWLDof-mlVM1IvC1j8aXuLdti_f7_tkJZVWJnhUJwcxzwGrumNej7CLKULEWQ2zYQMm7DDic9Q4QbJ_PI9vXeVQw_SuWOJYmAtH4m3dGaE46HKZ5QK5Mf5Jow_ZI3YsB5RF9h6abHgGvpUSznw51TUxBCOwXpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67238" target="_blank">📅 16:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67237">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyOdg-DJjYBCPnmLJjnRTexmL8liZEiTf4VZUf30gDJz4zldc83_D6eyNfNtJKa0Bjs2fZC46NVNsR4P9VSkyAeUhu5h1aG7MZJJqSnscE-2DgxhXrvA1ihVB4yKVNblATJt0RqgQ84IpL8gGsFPGqF0RbjUoopOsA2aBZlCarS-1i4gEAZzIg2yg-QSDUSqc6r17KXZE8iMesGzU7NHneenIn0aCYuSgCFmTUURanlfQ3j-QojvhZR08Hqji31IPycF-5xlqPLL9z8VbLkUZOKckB7bhLo_OyXHekdlmmIs25l6_EdJXoZ_X60d5Q6TcHFomhjd1lM1y7Gim1lJEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
پنج فروند بوئینگ ۷۷۷ سعودی سابق علیرغم تحریم‌ها به ماهان ایر تحویل داده شد:
پنج فروند هواپیمای پهن‌پیکر بوئینگ ۷۷۷-۲۶۸ER دست دوم از خطوط هوایی عربستان سعودی به ماهان ایر ایران تحویل داده شده است که دو فروند از آنها در فرودگاه مهرآباد تهران تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67237" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67235">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhvmE57R7YdhyiYbI6m1QXROF73_v0OZ9cAJLRLmo65L8RZX32fV9t2PMGtTwdZNZIQTXYUrRpuNMJJP8pgMICFZjxXrYjU-TqVZeNZ-XLdQMzzEgp4GpdAXwJefWBBWnBpmhZ_vW3PiWXJ7qXRyo7Dlw45yXTJ_vsVNoE6ioTt8KoXfcniOSuZjul1JXbsgKJQnDqeDW7Tv25kZ_AKZDBxac8-i0VgDu-K_BMQ-F878JGx2kW8FTMIKXqDB1wcMgNjZNBtFP40oNuGW-UC2yqEqdXSi1znTbv6QqX8286sipDSkcUWvsmMftWEFAqBESGNMBe5jxRNKtamiC5N3kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=C783x_QOLwvW8D5q0qQCeO8vpLguKM1S6vYne0xDJbpXki598xVWTbwg3VKDWhwr0NfbjJULFPY6_2kbXKnyElEDV-nW-mGV24c1rwn0VOeq2rxYMWNvTlU8PtuaXi-TA-9hz1l2ZE6TxTv4IvTB-r9tEJ7Pprzzg1RlGoxarKdS4lluA7siiHEwPPDRt5p7Y2_jAtFhIJGlQEUHX3jm0LpvnoqzZXj4TQSvuoXwdvvR04fulJabQ7jPquRlEdpZpePSRaRpwBU3m8x2B-4Gpm_oetu4Ht7euTEv3EXbEyq4QMRE2tKKQBaL0bQxB0y6ngcUX1yRCI94GVoEaS-HbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=C783x_QOLwvW8D5q0qQCeO8vpLguKM1S6vYne0xDJbpXki598xVWTbwg3VKDWhwr0NfbjJULFPY6_2kbXKnyElEDV-nW-mGV24c1rwn0VOeq2rxYMWNvTlU8PtuaXi-TA-9hz1l2ZE6TxTv4IvTB-r9tEJ7Pprzzg1RlGoxarKdS4lluA7siiHEwPPDRt5p7Y2_jAtFhIJGlQEUHX3jm0LpvnoqzZXj4TQSvuoXwdvvR04fulJabQ7jPquRlEdpZpePSRaRpwBU3m8x2B-4Gpm_oetu4Ht7euTEv3EXbEyq4QMRE2tKKQBaL0bQxB0y6ngcUX1yRCI94GVoEaS-HbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بر اساس گزارش‌های اولیه، جنگنده های عربستان بر فراز صنعا، پایتخت تحت کنترل حوثی ها، به پرواز درآمده و مواضع این گروه در نقاطی از یمن هدف بمباران قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67235" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67234">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s6xnACf3h5hGjXE4dwdzIo6IXZxcQTj9Tx8MCMSq_KkiWte6z8Xssm_IhdQ70AWH8GcM6UhbMAkEV-V-XmT5g0Ff1tDmKeAAizwozNa4F6einqZ5jBHonn4TZ7hsfaJgxGhcUo5tLUogrnlZ3G1FiW_0tveYUFoTIfGKBnh2frHKLaI4sVcnrYWWIgWwBClicrrPw666u1BM2YNlc2iFguFLXwkBU0jAL5FdsgXagkZNoBdnAg1wKz4BcrwbwNFwq68Uk7gTaajr2hkC17fIg-sScHWMJUSqRsVjp5KafyVv75AZIYscD5MS-hMDZNipZoayRKMMPQmcBZVEMBgUcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این عکس از تفاوت تابوت محمدرضا شاه پهلوی و علی‌ خامنه‌ای وایرال شده، تابوت شاه کاملا ایرانی و تابوت خامنه‌ای شکل و ظاهر عربی داره.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67234" target="_blank">📅 14:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67233">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=TY1qjsVEVAAVuzWRaYPXt15GbFXkdoP4T9_DkABpIVES_YkV0qtVPIvoQ6_N_9JPu5ghsEGutBBeru33j7ngpO6tfB9_CmqdcLHhraKm8OxBz9xb9rTUL6WpZBMyWnx8lPk0NoBwsCF8g3qdIVT4tJB6c8oSMlB-jiVU7vSJBanCWaVCk6siMQbqCVeIMo0ymGFaLNA_AxLw16AM7vN6KcIQFJcClDRqxNT7bfanWjvADiNQfrLwejXRhIbclHllKffGlQl8i29k9dAYQDqYMMhCa0grpEMgAPQ49ovdRnlhrF-nBjO2ExmEfka8oZlCsfx5a9uNUbtHf1PTBOojjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=TY1qjsVEVAAVuzWRaYPXt15GbFXkdoP4T9_DkABpIVES_YkV0qtVPIvoQ6_N_9JPu5ghsEGutBBeru33j7ngpO6tfB9_CmqdcLHhraKm8OxBz9xb9rTUL6WpZBMyWnx8lPk0NoBwsCF8g3qdIVT4tJB6c8oSMlB-jiVU7vSJBanCWaVCk6siMQbqCVeIMo0ymGFaLNA_AxLw16AM7vN6KcIQFJcClDRqxNT7bfanWjvADiNQfrLwejXRhIbclHllKffGlQl8i29k9dAYQDqYMMhCa0grpEMgAPQ49ovdRnlhrF-nBjO2ExmEfka8oZlCsfx5a9uNUbtHf1PTBOojjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حضور فرماندهان ارشد نیروهای مسلح جمهوری اسلامی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67233" target="_blank">📅 14:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67231">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzV6-f75bq93diohrBFwUVij0vK_B_vFVhmiXUasAc3cgVvMruLEcGHUwaRUBfsZLozUSpEwBwWNfE6ZASG6FcL_at2U08GGV1w8gnD46pbLzubqUE3dAzA_jUvH9lkImLeVv1MbZoI9HWn5Mz6WeNlR2jsEsekFiqpjgai4-KL-QRfwYyPRJYuDSk5n1NZH38ZqbUecEbCE17k-iOsA5qZHOcUW_xBcCZonpzhDHtTpfC7Gbi_xWR90bD4RHRof9JM3r_0hXBI4GiiW68SHvbU948HUgX6bwpykzOlHP4P--DKq3QmfIFcdLwl-ZrRWRiXHBleEK6mxHM7M72YNTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=QV31q7HQVcuQK7fE07adIuHu8x3rkGE1XXrfvBtxE8In2TN3vvItAkH1gZ8bkBWgK0ZaqNboJuDLUHF6Ob8hGTQvzTTUlgzuKgdbgbF4L6fHbOKo5_PO0Gp32zxtL6U5zS1P00AVnTnahnXYV3V5KVeTIoycDm1nL8zr8CSLl76Xgy1Avo81A5o96kx3CnaWSkSrRZkbSqvIBsRs_l1Eex2IZAwh8trL3jXadWN-Drplhxq8ze_8XJU6D_pxuym365e3KhWCi2VPis5Fv77SBe01n4Q5eoBbtAAgJopwJBA-S_NhKNRDW-gveFP2QlqBoWMOukA7iqpR5u_J3jS44Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=QV31q7HQVcuQK7fE07adIuHu8x3rkGE1XXrfvBtxE8In2TN3vvItAkH1gZ8bkBWgK0ZaqNboJuDLUHF6Ob8hGTQvzTTUlgzuKgdbgbF4L6fHbOKo5_PO0Gp32zxtL6U5zS1P00AVnTnahnXYV3V5KVeTIoycDm1nL8zr8CSLl76Xgy1Avo81A5o96kx3CnaWSkSrRZkbSqvIBsRs_l1Eex2IZAwh8trL3jXadWN-Drplhxq8ze_8XJU6D_pxuym365e3KhWCi2VPis5Fv77SBe01n4Q5eoBbtAAgJopwJBA-S_NhKNRDW-gveFP2QlqBoWMOukA7iqpR5u_J3jS44Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس حوزه انرژی: تنگه هرمز از مسیر عمانی، اتوبان شد!
این فیلم از موسسه کپلر را ببینید،
چقدر تلخ است، کشتی‌ها و نفتکش‌ها در تعداد بالا از مسیر عمانی از تنگه هرمز عبور کرده و همچنان می‌کنند.
با این روند، به زودی ترامپ بابت تامین امنیت کشتی‌ها از مسیر عمانی، عوارض هم می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67231" target="_blank">📅 13:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67229">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fa301248.mp4?token=VB-ei6Y5yozIHl1XQQoXOY0yiYLRj1NseoHaFbhp--SiycpexNjHXGsposHXm-n1e5Sm6Gg3pNq26Rvv1lrg2M34p4GkohJ9xYNtVBaFSIz4Fj8dVno0DL1oGGXiWoCVAYkc98vL5kqSX541c49SJApUb5ZvyIpo3IGxCIl0ahEb_touIpD1C1NbA5h0H7ZsLW6PmgblKb8J55wVhnGnqDMQoyFLelCjO7W3_j6TZW_T6CCWiTDosgE8SZGcFtJ_K5cBk8HP_qZcctwCAxUb83bV_nNGW02ZG1W-Zr_ZrLyNviip_sjXY8OhpY1fcNcbx1kk3TlpkQxz7MnX7qDaQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fa301248.mp4?token=VB-ei6Y5yozIHl1XQQoXOY0yiYLRj1NseoHaFbhp--SiycpexNjHXGsposHXm-n1e5Sm6Gg3pNq26Rvv1lrg2M34p4GkohJ9xYNtVBaFSIz4Fj8dVno0DL1oGGXiWoCVAYkc98vL5kqSX541c49SJApUb5ZvyIpo3IGxCIl0ahEb_touIpD1C1NbA5h0H7ZsLW6PmgblKb8J55wVhnGnqDMQoyFLelCjO7W3_j6TZW_T6CCWiTDosgE8SZGcFtJ_K5cBk8HP_qZcctwCAxUb83bV_nNGW02ZG1W-Zr_ZrLyNviip_sjXY8OhpY1fcNcbx1kk3TlpkQxz7MnX7qDaQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پالایشگاه کلیدی لوک‌اویل در روسیه هدف حمله اوکراین قرار گرفت!
این تاسیسات سالانه حدود ۱۷ میلیون تن نفت خام را فرآوری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67229" target="_blank">📅 12:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67228">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKtc0uMXvvQ4JT4fKeUNKkkxq6-SsDsw4TVrTr_LNQ6joBbNKfikLrkHSVuvo-g1zy5nNFhsnU4_oMuT_Xwq9mf5Py8aUmqdd6a4uhEl2DBvJ1t88ZbdwFF5nkgTB9lt2SjPKUP6OcmIak6bmeQo9KKrqSfr39CwDX2YgTUlTXXtJuQdLGIeXT-2CNj0DyHfet4QBaz9xHhH9BHxtCYNae6WFchsXDZgGB15prKPuojL0cFyuQWEtnJc0MESzXUd7lG5E-iu-I6Exf_vVPi37ouWkO5SsfNdQXz9uBxSZMpqq_zI_9pqcts1-Lu5Uqoo1VhTMkNVI7eodYO-CO7cmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
همان‌طور که ترامپ درباره درخواست ایرانی‌ها برای برگزاری جلسه در دوحه دروغ گفت، دیشب نیز دوباره دروغ گفت؛ این بار درباره حمله به تأسیسات راداری ایران. نه جلسه‌ای در دوحه برگزار شد و نه حمله‌ای به ایران صورت گرفت. هرگونه حمله‌ای از این دست، با پاسخی کوبنده مواجه می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67228" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67227">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uz-bHbWEwYdQO-Yj7RgmqF6ELKbmIXRHdn1_IynvqyEFqa8QiipA89OdjnJLoX_wJMGzXvF9SHhYMpO2HDVew1UYqGTktcFbdKGm37ewcvoxyINoQpV8dCF9JhxCQNDS5AusAU4owQsmrIBxk24pCmbWytAmzBi7FhqBUTyOzSv1bSauQ7pjCu216ts7M5B73Neh3J5zucPB1B3zunqggXCPud2Ro_3ycOACepNNee9Z95P0ygo6DgtAAgjUo284lQ0jiNnr3O8qlBgewl2enS_yvCI6gXJiMbXVtkD5LczEYef_zIJjjTQryaMHhuP1x3KSCdjCmKrafV9Ui1bq1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی طلات رو روی ۱۶,۹۰۰ فروختی و توی یک روز،
قیمت طلا
۵۰۰ تومن بالاتر رفته!
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67227" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67226">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmM4K_cgBWpt_qdXMdKtETW8WoVywWIY8M7-8Vca60MY70Px-AdxiDGTPWZM_cohXpegs7iiFH3Bau8_93CQBe2QtCATl6RCSaCiBiy5lmkJ6t-H-TYOxgol2rdCX3-PxhfhJ1x6zS-diE1q1PBgFHdXOBpS5oPGREcI9wlc_DqHY2LUJKy1-LpQ283GqS6pSuCXKGW4jOo2JUj3dnEMGjpUOPjQ2VQxQWSM0S2a7-fx9x1sAKqhBiel9KKm41I3YtAePEr-sc57sxQHvSMIZQsAYHVslsqOwp4NByaFCRoBBPPpkgeHeDD5EwuxOpKEMnr9MCpe-DneRbBSNx4YDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید محمدجواد ظریف:
ایران، پس از دو قرن تجربه تلخ ناامنی و آسیب‌پذیری، با هدایت رهبر شهید به مرحله‌ای رسید که در گزاره «دوران بزن در رو تمام شده است
🤣
🤣
» متبلور است. این تغییر پس از دو سده، احساس خودباوری و اعتماد به توان داخلی را برای ایران و ایرانی به ارمغان آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67226" target="_blank">📅 12:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67225">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10282a802.mp4?token=ckoCH6HFDPPNFnK0injJFPzWXGIT7qGzriZHzC8mAS6FRTeuLo-RpgEMH-byE_VnWV3DdvHbO5TArKGBqg_rBCpmy5cQnEhh8AE98ixlnDPvj-BpNvoY69jSvJHQJQ0cdec-OLlEF9GEYb-Db8taTMdSpnt6mQBA205l-oFvCB8boDs3W-FnpY0vHY_wldB89pvaiVCNBr5IPIcvLfLaKDWoBoNKF4VjV09nbku4QWmsxRp__d4tp5qCZBTtn5dJFTf8RKXC_2HA8wn0C0li7JRM0Qn2ThcZxjJDj85dnMXopY4RBevt_kgmHhCfAWMEwxCSTl_Vukg-QsIh4Z45qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10282a802.mp4?token=ckoCH6HFDPPNFnK0injJFPzWXGIT7qGzriZHzC8mAS6FRTeuLo-RpgEMH-byE_VnWV3DdvHbO5TArKGBqg_rBCpmy5cQnEhh8AE98ixlnDPvj-BpNvoY69jSvJHQJQ0cdec-OLlEF9GEYb-Db8taTMdSpnt6mQBA205l-oFvCB8boDs3W-FnpY0vHY_wldB89pvaiVCNBr5IPIcvLfLaKDWoBoNKF4VjV09nbku4QWmsxRp__d4tp5qCZBTtn5dJFTf8RKXC_2HA8wn0C0li7JRM0Qn2ThcZxjJDj85dnMXopY4RBevt_kgmHhCfAWMEwxCSTl_Vukg-QsIh4Z45qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226825be38.mp4?token=QT9S7pamSUMI1HDYhK3IW6hMLnWj5xP3Kpmq5MDf-oOk3iAxiJv6vJ9T25_s1dgFd09M-fI6P2-JxP46uiWZoctEorYAK_LhmjFv8YVSY7S_5LKNoBCmZ-UWas2tCuZsqN0r4C8GMwov1yfSLsmhmpjgHNROG07SjjwnFHtrLbAVCeKT3unK0NiuwTuIqB8fCRR6Y3RNBVHVlz3HWNPkTwd4BUeKVRtojKGIEmNX3pYgp5caESwIoQA2mYOV0j5XUZ6Ks2sU_Tv_hkuV5xnnEBxjp22w4f1KId6G3TEqxwn5l1i_idlm4cETMsyR7DzK6t_1-14VXt8DLUhSC75_DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226825be38.mp4?token=QT9S7pamSUMI1HDYhK3IW6hMLnWj5xP3Kpmq5MDf-oOk3iAxiJv6vJ9T25_s1dgFd09M-fI6P2-JxP46uiWZoctEorYAK_LhmjFv8YVSY7S_5LKNoBCmZ-UWas2tCuZsqN0r4C8GMwov1yfSLsmhmpjgHNROG07SjjwnFHtrLbAVCeKT3unK0NiuwTuIqB8fCRR6Y3RNBVHVlz3HWNPkTwd4BUeKVRtojKGIEmNX3pYgp5caESwIoQA2mYOV0j5XUZ6Ks2sU_Tv_hkuV5xnnEBxjp22w4f1KId6G3TEqxwn5l1i_idlm4cETMsyR7DzK6t_1-14VXt8DLUhSC75_DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نریمانی مداح حکومتی:
منطقه شیعه نشین جنوب لبنان ۱۱هزار خونه صاف شده، آقایان چرا نمی زنید زیر میز مذاکره!
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67224" target="_blank">📅 10:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67223">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VABuWFuAN2SrUhXl-nESSp1TqJwE6Ag4YQbSvZX4IwUVHX0SCP-EVKkx4hN9_H1vog-2n5LRe8KCxI5vy2khlewfZJLPAwUexuS3NojS9P24LN3pR8bx6EHLCy3Jg93f5rmx9zGhIBfeXH9uw6_g0R7J1Juf0faz08ZFSw98siSPD0IF_jF2T-YzCXwsF4DfVI2SqtWLVSRwhhvk20z7OCljkKeafHEPWGoQVRmAKTz1c-Tss9Phf9FogKfFZRsU2g-b_VVyNF_LJ1X-dn-QyvBXmQ9hDPiyGQJ3UkZwGFcer-g8D_kUtiDMztuES4GoyCvewHsXUHUrJP2_biCSAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه بانو الکسیس پورن استار معروف اعلام کرده با مردای همه کشورا غیر 2 کشور رابطه جنسی داشته، ایران و غنا
برای اینکه کلکسیون خودشو کامل کنه، گفته فرم پر کنین و درخواست بدین تا یه نفرو انتخاب کنم.
از غنا 2700 نفر و از ایران بیش از 1 میلیون نفر درخواست دادن! جوون ترین ایرانی یه دهه نودی 10 ساله و پیرترین یه پیرمرد 78 ساله بوده
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67223" target="_blank">📅 10:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67222">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55805ed771.mp4?token=XvTiHIWXxSeO_91CCchQ-aAXzETFsBwFVh2vnzMS4h0teC3FK6c4kf1ZkYq_P409UF7pEq_Dqlm6Kwv-e-QA-1_11WJZO_OW0_Ngazp1hTQOesKDe_Z0dmmsunQc-Fheb8BA3ZHjW17D8XCRv2gJOtx2ZHp9E0-fJR9982j-lWA41BuYFsE2cr3bgOjd8a3QwH4y_RBYQxHOPU-bxs_jbatVnNr2g6So4PLqbPpC0C5ku4rfFjx8DV5JGRs88J2dwIKc1IMmgoXCL1UThgaKW66Qrw6qb2fYrEsYHCE6_JG1Rv7_xtg05twR5r_GMOybHWXPn4JTQ8bz4TiMu6H3IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55805ed771.mp4?token=XvTiHIWXxSeO_91CCchQ-aAXzETFsBwFVh2vnzMS4h0teC3FK6c4kf1ZkYq_P409UF7pEq_Dqlm6Kwv-e-QA-1_11WJZO_OW0_Ngazp1hTQOesKDe_Z0dmmsunQc-Fheb8BA3ZHjW17D8XCRv2gJOtx2ZHp9E0-fJR9982j-lWA41BuYFsE2cr3bgOjd8a3QwH4y_RBYQxHOPU-bxs_jbatVnNr2g6So4PLqbPpC0C5ku4rfFjx8DV5JGRs88J2dwIKc1IMmgoXCL1UThgaKW66Qrw6qb2fYrEsYHCE6_JG1Rv7_xtg05twR5r_GMOybHWXPn4JTQ8bz4TiMu6H3IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پروفسور جیانگ:
آمریکا احتمالاً بین آذر تا اسفند یا حتی زودتر حمله زمینی به ایران را آغاز خواهد کرد و امضای تفاهم‌نامه فعلی تنها برای خرید زمان است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67222" target="_blank">📅 10:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67221">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kild0dGIAxk-U-H0KUZQKWhQXsSPdZx5wBCOtPGv8XlEUSa4TkmSHrIMKxrE65Vakdq0FtU4Gs9pVmlS2tjeKd3zhBJ1ttA6mSvSvgY30U6xtT-B7GD5N6Xb86Rqg7uhHTYW9LMMmPNvAvsoClEEwQJMZ98VRiKyJQqsB8i7y3x7HC_QiiG-UcabQUpE8FOwtHgtPvgOB3gL7FJFwnYPl7FhbxACqTv3gisZ6SXkfiDZsVv5QlZCHhwNqV-RXVpJkKJ_fYwZoXNoBelQlE1Mb_o61tcsq1ZLZDnjpg3PeTuBdQh7qdAccdtFcu3TIyT_WKcRfD69plpMMPPuIZjKZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین فاصله زمان مرگ تا زمان دفن رهبران جهان، مربوط به الیزابت دوم بود با ۱۱ روز فاصله که سیدعلی خامنه‌ای با ۱۳۲ روز فاصله با قدرت این رکورد رو شکست و نام خودش رو در تاریخ جاودانه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67221" target="_blank">📅 09:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67220">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=epxx4mpa2ipCLizp3CtTyPbLoA6cqcoWr7lIcTpD5-IVU4qk_KBv_FQaTt9myqSis0TPAmHL3XnX6qDHBVsjO8bVQKcIr4YGhPO_SJjRRdoXzhyUBYflAemzjFwKK4udmn-prJYOnovjpvh8ilnP3gyG1VH70UVXn3ckKsekqzjlghy_u8a2093uK8K8IKETmByh7uIuG141XTRyebXZ85BhRQ3-sB2QqiC9jPec3YWlva40b385MFoNSc8IBnFsPyXHvjtttHFeboO7yHeLwydaHm7f_YFr-h2im5wLSw_RvE2YxnQpQ6LBrng8nqWnnCTr4P6dssqkRu67jbebmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=epxx4mpa2ipCLizp3CtTyPbLoA6cqcoWr7lIcTpD5-IVU4qk_KBv_FQaTt9myqSis0TPAmHL3XnX6qDHBVsjO8bVQKcIr4YGhPO_SJjRRdoXzhyUBYflAemzjFwKK4udmn-prJYOnovjpvh8ilnP3gyG1VH70UVXn3ckKsekqzjlghy_u8a2093uK8K8IKETmByh7uIuG141XTRyebXZ85BhRQ3-sB2QqiC9jPec3YWlva40b385MFoNSc8IBnFsPyXHvjtttHFeboO7yHeLwydaHm7f_YFr-h2im5wLSw_RvE2YxnQpQ6LBrng8nqWnnCTr4P6dssqkRu67jbebmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان
:
من به عنوان مسئول دولت نمی توانم ببینم مردم مشکل دارند و بگویم همه چیز خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67220" target="_blank">📅 09:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67219">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67219" target="_blank">📅 02:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67218">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFuck Bet(cheGuevara)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbjBIycHz-b8BOmvXeUdVbCf5yeQHhkBRo4nvjQHw8RP32lOVG8kcdAY2u9B5DTU6BeD0V-Bclm6JoTUPOsoJKPR3OFPtIdMCDOKlYrndjFasPgvxSUJCRcmVILGcHicwF4wYcYdxRESSnvvL8mNORKtzypxQeH3J1dU0JLHLRGxFRZZna8oihu6Q1CYp2CBxEXjDykJuqvdTuAr32Kl6QLdHZ0YiVUitEjsg-KIjcbf0mnUvWryKdbASP-bdk2chkcbLbi7M6T1femsm98SyPjTm2idy0HA1Ay2eyrC0L3t8VmvgnB2DAxW2tm-fBZaZutuuMklA1eowrtU-i-Sqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67218" target="_blank">📅 02:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67217">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=Q6QaDM_F6rwyolVrVMxx-GyfVfBvNhK3dFRQ6YAhWdqNdFH70W7lwM7lFlnUkTFC-9avmU3IVBfidfw4Ppv0UEd9osTbgF3rPMUBaaP0IoeR9i7C_YY21YM60qFTyiXjcpctzvNUqC2CYhcikzVoISL1Rpwrohv28ZtapwA4kELicxjgH0WPBC-_xlClfuwyp8vN00wTp26ZCvQC17rDHnf12Zqb5t1HSCmpiCUg9gDx83rIHDfGolH_sQeHMurm3YVIt-HbU0V3vpx67yRXLz8SFEjOYbGidV4_oKIlV4_wYQqEoL4HCwrVw9JDatMWyNLKAjPjKJXIKCiy7eB3uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=Q6QaDM_F6rwyolVrVMxx-GyfVfBvNhK3dFRQ6YAhWdqNdFH70W7lwM7lFlnUkTFC-9avmU3IVBfidfw4Ppv0UEd9osTbgF3rPMUBaaP0IoeR9i7C_YY21YM60qFTyiXjcpctzvNUqC2CYhcikzVoISL1Rpwrohv28ZtapwA4kELicxjgH0WPBC-_xlClfuwyp8vN00wTp26ZCvQC17rDHnf12Zqb5t1HSCmpiCUg9gDx83rIHDfGolH_sQeHMurm3YVIt-HbU0V3vpx67yRXLz8SFEjOYbGidV4_oKIlV4_wYQqEoL4HCwrVw9JDatMWyNLKAjPjKJXIKCiy7eB3uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«آن‌ها تورم ۳۰۰ درصدی دارند. هیچ درآمدی ندارند؛ بنابراین ما بخشی از آن پول را برمی‌داریم... و اگر به آن جایگاهی که باید برسیم، دست یابیم، تأمین [مواد غذایی] را منحصراً به کشاورزان آمریکایی می‌سپاریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67217" target="_blank">📅 01:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67216">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=qecE2XbF2SPd6WflaBoIRepLjWS_Q-H61bTaFYVXwCeV-0p4T0MYq4xGCIhjfAs5FTxR4bBofLyeIdQbt-eVd8YIE6RgLOmNdEUUJ7bg1cQV0tLmt5i343L8pDYHaSu6gZ6sX1t-uf8Q1ZL7oM_7s0eWa2Dbnlh7vYiM2Mk3fF30kTlQ8AVtAYpZm2Jmg3TZqvYgEGRJWyEyK7k-0pu-33AufNmZRv59nn78pS8KTwlG0C_A-2zi1TSKCdi2qIoqF6-jPef0BFGLYIGnPlrkKO3imR7B5N6g2Epnlk_c2WuqwsfZjN7sKdRTMB4DWuVPEqZ6MiyJweDIfRAkYypr8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=qecE2XbF2SPd6WflaBoIRepLjWS_Q-H61bTaFYVXwCeV-0p4T0MYq4xGCIhjfAs5FTxR4bBofLyeIdQbt-eVd8YIE6RgLOmNdEUUJ7bg1cQV0tLmt5i343L8pDYHaSu6gZ6sX1t-uf8Q1ZL7oM_7s0eWa2Dbnlh7vYiM2Mk3fF30kTlQ8AVtAYpZm2Jmg3TZqvYgEGRJWyEyK7k-0pu-33AufNmZRv59nn78pS8KTwlG0C_A-2zi1TSKCdi2qIoqF6-jPef0BFGLYIGnPlrkKO3imR7B5N6g2Epnlk_c2WuqwsfZjN7sKdRTMB4DWuVPEqZ6MiyJweDIfRAkYypr8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما رادار ایران را منهدم کردیم. آن‌ها هیچ راداری نداشتند؛ هنوز هم ندارند. همین چند شب پیش دوباره آن را منهدم کردیم. آن‌ها یک سیستم راداری جدید و خوب داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67216" target="_blank">📅 01:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67215">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82798a9488.mp4?token=Bynsb-aHZ_BFZpOOq4FaaTmB_yeaSQh8QRPjFkSzeQXnLgx3J91dDzi3wlliBfZaSYznssn49ug6UuqvcwLy1nlXzdZ6eWMVLk_KPxHk5LeN5RcKk0TLOFG8Y9UM5Vg2m-ikNw4xem2t12ZW7SeafMLf5o4iRQDds4B3LhnDsSGwQb2c_wAM_PUIDqP1pVtDtDoJR30fhg1PwA3GY9MVOWHYxxjnhNIhjEJpAPVckSPz1z3F7Dej8sy-kOtOMkBemJu32AGxzjMnu5ZDQB363rg-2ygvb3xRAqDvnGDgkxdZueS0Lj8arFX1DNHLfuFt8rPHd5xp0rqNomP6KuyDvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82798a9488.mp4?token=Bynsb-aHZ_BFZpOOq4FaaTmB_yeaSQh8QRPjFkSzeQXnLgx3J91dDzi3wlliBfZaSYznssn49ug6UuqvcwLy1nlXzdZ6eWMVLk_KPxHk5LeN5RcKk0TLOFG8Y9UM5Vg2m-ikNw4xem2t12ZW7SeafMLf5o4iRQDds4B3LhnDsSGwQb2c_wAM_PUIDqP1pVtDtDoJR30fhg1PwA3GY9MVOWHYxxjnhNIhjEJpAPVckSPz1z3F7Dej8sy-kOtOMkBemJu32AGxzjMnu5ZDQB363rg-2ygvb3xRAqDvnGDgkxdZueS0Lj8arFX1DNHLfuFt8rPHd5xp0rqNomP6KuyDvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما آن‌ها را به طور کامل از نظر نظامی شکست دادیم. آن‌ها هنوز تعدادی موشک دارند. ما می‌توانیم آن‌ها را نیز نابود کنیم.
به نظر من، آن‌ها تقریباً به تمام خواسته‌های ما تن داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67215" target="_blank">📅 01:26 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
