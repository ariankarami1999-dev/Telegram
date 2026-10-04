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
<img src="https://cdn5.telesco.pe/file/Bu7VwPAiDe0HgWd9MwAf7bpL7nhVuGYh-q5tuMwakQCqlxQP7OhtJJigRAdxLyw5MWa3mpy17CY4oOPmUJwgjfEmmAt9OX8yHEH2uDmqgiP_fNGWPoKs-o7OFlJ3ZfdmuIEW4vZ33QDHrgpThJ5DoCul3BsXERGfDpMSjDDXGzZFS43PTSJ2j3AqK-WzuyNOaRxo97lQyHBwqT_j92G69z0ejbzYMn57_rqWSJWQBExq10GZ-BnzEe3xF6hbYyltbpNixSgrzpXnsl2Yxra_K1C2Z_LeUlC_wDFVw-FedoZ0PLxMtbqbvycGnnXT3ntatXvpPRLRIpikpZAPf-XiAQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 392K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 16:08:11</div>
<hr>

<div class="tg-post" id="msg-107807">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63df69c40a.mp4?token=NOK16TJXzGfz4O4FPRyRib9tjOKWqfxRN_zV4x4wmn-r_DSmKp7raIF7xb4zd45bdAEX-qcrsjSqlm5nZLcH7PFCbLIq2v9xbdsGY8WqwaCJvTlOAI6abbriPFeur5zk6oYo65ayaHuLD7DnxeSJhOknNdslwFMr3nUPINkh_t6f0LdHrSeUmopbhVjj0O4ovQW8EbGIZT4ceuFJDEfO8Zo-NzQ10NwCmUecsdWW67G0hzt0mTwwyq5o0CU0NZwWhONMtSTCN25mfGsVMLUnNeLXyLPWpNI-ND4etf0YvhOiS8Ja5nHZU2M7pa7InwfIDBKR7HOoiadH260cVHektQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63df69c40a.mp4?token=NOK16TJXzGfz4O4FPRyRib9tjOKWqfxRN_zV4x4wmn-r_DSmKp7raIF7xb4zd45bdAEX-qcrsjSqlm5nZLcH7PFCbLIq2v9xbdsGY8WqwaCJvTlOAI6abbriPFeur5zk6oYo65ayaHuLD7DnxeSJhOknNdslwFMr3nUPINkh_t6f0LdHrSeUmopbhVjj0O4ovQW8EbGIZT4ceuFJDEfO8Zo-NzQ10NwCmUecsdWW67G0hzt0mTwwyq5o0CU0NZwWhONMtSTCN25mfGsVMLUnNeLXyLPWpNI-ND4etf0YvhOiS8Ja5nHZU2M7pa7InwfIDBKR7HOoiadH260cVHektQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
رسول‌مهربانی مجری دلقک و گزارشگر صداوسیما که با این الفاظ دیروز جنجالی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/Futball180TV/107807" target="_blank">📅 16:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107806">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dc22c75d3.mp4?token=t1vzCNC4zOQU-m0OM5l6B7UFcfIidNzIUNJIe9BLIUMTIkVFGlV_9zSKOeTEcDuO1h3cVDsPAyvuvCVeqddWDpa9MMbRbgCu6QQjY8X-6gE9ijjpQSsWG7r0YY3TlUFZG5wqrDlhmLZc8E95bewxEJ-defVUyCeU4tZZ8Kr2smFmFOThNKH-INrm43s5jPq_1PBIcEAEZ5-n2wLXCDZ20hrpoE5duSTBQsnOBjW91XHvB4keDkc8_vhjwqr4apWLtZmM3bTN5NRvlBaEeekwGSW7iT6bsgT9KVC4fZcgmJUSK8HFj3OAquJfUX3SkES2Twx1NzsaNdPBmuruQb2rNzM7judrEfDzM9mqfuovjBc_jripEsFxdk5NKwpQhR-KsQx6IZT5TFDuzK81FDotE4JLqmR7vhPKpHbBBZYPmGWsGZT-0FYR81nGZ3invbEh_UUG-3lErmMRAkl664_vQnJCM2S7o0SAkDGNl3QzVWaFIVrrjS-Dig4V6k24MpPoBqnEkACFt2zw8HS7ftW_QMULeNgKkkZ-wk72oF4VPpEiZSct_BJB1yZlEhOaOF5Rp8jq5SClGTxf8e1K4e09b-DajP_FlfFZFM3IflE0dQzA2febRDZ9KuNoIQwpeVkw58OqcEKsnDU_O8eAjb-2_zKp7_bcXcoKdBxoAULWVGE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dc22c75d3.mp4?token=t1vzCNC4zOQU-m0OM5l6B7UFcfIidNzIUNJIe9BLIUMTIkVFGlV_9zSKOeTEcDuO1h3cVDsPAyvuvCVeqddWDpa9MMbRbgCu6QQjY8X-6gE9ijjpQSsWG7r0YY3TlUFZG5wqrDlhmLZc8E95bewxEJ-defVUyCeU4tZZ8Kr2smFmFOThNKH-INrm43s5jPq_1PBIcEAEZ5-n2wLXCDZ20hrpoE5duSTBQsnOBjW91XHvB4keDkc8_vhjwqr4apWLtZmM3bTN5NRvlBaEeekwGSW7iT6bsgT9KVC4fZcgmJUSK8HFj3OAquJfUX3SkES2Twx1NzsaNdPBmuruQb2rNzM7judrEfDzM9mqfuovjBc_jripEsFxdk5NKwpQhR-KsQx6IZT5TFDuzK81FDotE4JLqmR7vhPKpHbBBZYPmGWsGZT-0FYR81nGZ3invbEh_UUG-3lErmMRAkl664_vQnJCM2S7o0SAkDGNl3QzVWaFIVrrjS-Dig4V6k24MpPoBqnEkACFt2zw8HS7ftW_QMULeNgKkkZ-wk72oF4VPpEiZSct_BJB1yZlEhOaOF5Rp8jq5SClGTxf8e1K4e09b-DajP_FlfFZFM3IflE0dQzA2febRDZ9KuNoIQwpeVkw58OqcEKsnDU_O8eAjb-2_zKp7_bcXcoKdBxoAULWVGE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🙂
بازگشت سردار آزمون به تیم ملی بعد از مدت‌ها با کمک متن هوش‌مصنوعی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/Futball180TV/107806" target="_blank">📅 15:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107805">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ab5019276.mp4?token=rF8np1zaqvRnF6HSPcZEWVATiBbeWdmhjEGAiddrbpDyZIFabPTFQLJK4AqxocH4cn44NYT6cce5HpaH8zKcQAH91Rvs9beL3UhKxAOYMOie-rOaj4Y2_HThQjLPTUDzgIN8NwUjplUSlrSnCE-3XKJDGzwqdEHWJCvN29e2azAEKHydOoFqrO-vNy3LpFhFXQJyBDsl0kyVEwc2iwddajE-5uOiiIFwg7Ez_bp9yP2QQFKR07nq5vlEjhFiWrc_f1FdV45-CsnABQHR0KrtcENMYPYYzm2tEIlpUmO1dMKc_231l9HuaAtkXdRWrNGnwI-y-IyDe1EZFK3hv6IwWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ab5019276.mp4?token=rF8np1zaqvRnF6HSPcZEWVATiBbeWdmhjEGAiddrbpDyZIFabPTFQLJK4AqxocH4cn44NYT6cce5HpaH8zKcQAH91Rvs9beL3UhKxAOYMOie-rOaj4Y2_HThQjLPTUDzgIN8NwUjplUSlrSnCE-3XKJDGzwqdEHWJCvN29e2azAEKHydOoFqrO-vNy3LpFhFXQJyBDsl0kyVEwc2iwddajE-5uOiiIFwg7Ez_bp9yP2QQFKR07nq5vlEjhFiWrc_f1FdV45-CsnABQHR0KrtcENMYPYYzm2tEIlpUmO1dMKc_231l9HuaAtkXdRWrNGnwI-y-IyDe1EZFK3hv6IwWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
ویدیو وایرال شده از شادی رتبه ۲ و ۶ کنکور در حین اعلام نتایج کنکور سراسری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/Futball180TV/107805" target="_blank">📅 15:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107804">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49b154fa09.mp4?token=cNTApEH363vNjDIqBoRE15fnTQpGdOn0k7JRlllohOo_PFCE-Z8CMU0VfNb9hKVskT5S6dhVeAhupNm2M4wEhgDJezrGb1OV76JnmCLZ0ZL0Gmpwr7ni7fQf8tvPzBKsAsRBlKgUqcmdtC2BoGkU6zlLUlOGRPIXmQEJ_6Di-8SypSrG5LQXK5ofzGnA1W6smaY7Dn9g-Vj6JJXae17TLrrajUZlaijwSJwkJbRr41AZrYMsInh2yruBfeTVC0lwVXZIsyhfvpiBHJGGq8ARG-rAfdUVK7txe20CTRb717Dco1znAlKHxVihJjbGHxohIH2qYuxP8FquVsA6ZzInDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49b154fa09.mp4?token=cNTApEH363vNjDIqBoRE15fnTQpGdOn0k7JRlllohOo_PFCE-Z8CMU0VfNb9hKVskT5S6dhVeAhupNm2M4wEhgDJezrGb1OV76JnmCLZ0ZL0Gmpwr7ni7fQf8tvPzBKsAsRBlKgUqcmdtC2BoGkU6zlLUlOGRPIXmQEJ_6Di-8SypSrG5LQXK5ofzGnA1W6smaY7Dn9g-Vj6JJXae17TLrrajUZlaijwSJwkJbRr41AZrYMsInh2yruBfeTVC0lwVXZIsyhfvpiBHJGGq8ARG-rAfdUVK7txe20CTRb717Dco1znAlKHxVihJjbGHxohIH2qYuxP8FquVsA6ZzInDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
👤
👤
مشاور قالیباف رئیس مجلس:‌ تا به عادل فردوسی‌پور تذکر دادم، مطلب حمایت از علی کریمی را حذف کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/Futball180TV/107804" target="_blank">📅 14:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107803">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCB6oAviaiNvy4iCQKnCfBjLQKNsGDGud_xF8TZ6Vjb15aPM4pC0LYk7yCHJIcsPTxnys2ey0Jvv_sgocc2LS2eudC8ogzcd3pmkiiY8MkOwtHET1fjiFvO2pSrYp0tdMZHXBIBGPp2fXRCJoDCc_sGp3a_N7AgtkKsRbuikz3Yas1_ceXXDXoGfKe-4mNV4fQsnj-VUKuxlyVTLpUatYAomU-rGS8gbBbjaThRoGfSpuikbcwDQ8AuGyhlB_hTVr5FGJeNIS-od30wIF4muos0b4Ko2fnUWAr5KIimvQrLa1B6KfguJYy097yDBLe8oPQeDjGtHejlFbhlANdByUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇹🇷
وضعیت وخیم ترکیه در لیگ‌ملت‌های اروپا؛ بازی بعدیشون جلو ایتالیا هست که آردا گولر بدلیل دریافت اخطار محرومه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/Futball180TV/107803" target="_blank">📅 14:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107802">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e464e1d963.mp4?token=t9nFgc7_q1XrrGrbJOrseKZZMkqi22Ave4S5MYGVGNC2MXwQDpOZXReqUAS6_vgjiyebKqaRk89U619fOmX4H6yUcZUXExf_MWrOh5JV4kZaFqIq06VhSk-h9X4W9JvzyFnlx24g8jOMATgMuPNLKN4rALj3eSYzi2taG8OR3ZZi6k35dKrRr9d3L1yiJWr7b-MBxRZiWJrqhSEO7DAa6qA8c895syYiBTQbtfe8ovUZLKpPv0qZu3acQ8c8Xom52ihVlevDU3tgesIoNsRJ-1e9XoTsr7_wtjTXp_Nmhf8U1qVrLYIJdV5qsxG6Gjdl2-2ALF3OaYVUPEzYbvmlImmmKHxYtPp1u7jlsOt7Yt81aLTvJj5IcPkCvj0Au8EQKhK8PlvMsITBaxw9Cmd6RSrzfXnmrUD5iAg_c_A2OgaHAFp5dI_icOeiIsUgJOyD3CAHAZSAYuPX88LtNYD3H_Uw7z4_Mhe3HmutyRI6oCOXjYlbzS-ouMpt5_Rg3pivPriw7ymoIWrUH1fXYifwjVavI2o4qjTQxg59nUhKBP_-OTN6uPG8GA7eye6dES58hTrN5bB6R1YnkTbTMSxRpO_7wBP4WV0t1LgBZOMB2P5qLZ13igyhiC7MRzZJsCYC3OM5lERjdQ998vPUcwd3knt2-V9DDb6huNBdHqlIW00" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e464e1d963.mp4?token=t9nFgc7_q1XrrGrbJOrseKZZMkqi22Ave4S5MYGVGNC2MXwQDpOZXReqUAS6_vgjiyebKqaRk89U619fOmX4H6yUcZUXExf_MWrOh5JV4kZaFqIq06VhSk-h9X4W9JvzyFnlx24g8jOMATgMuPNLKN4rALj3eSYzi2taG8OR3ZZi6k35dKrRr9d3L1yiJWr7b-MBxRZiWJrqhSEO7DAa6qA8c895syYiBTQbtfe8ovUZLKpPv0qZu3acQ8c8Xom52ihVlevDU3tgesIoNsRJ-1e9XoTsr7_wtjTXp_Nmhf8U1qVrLYIJdV5qsxG6Gjdl2-2ALF3OaYVUPEzYbvmlImmmKHxYtPp1u7jlsOt7Yt81aLTvJj5IcPkCvj0Au8EQKhK8PlvMsITBaxw9Cmd6RSrzfXnmrUD5iAg_c_A2OgaHAFp5dI_icOeiIsUgJOyD3CAHAZSAYuPX88LtNYD3H_Uw7z4_Mhe3HmutyRI6oCOXjYlbzS-ouMpt5_Rg3pivPriw7ymoIWrUH1fXYifwjVavI2o4qjTQxg59nUhKBP_-OTN6uPG8GA7eye6dES58hTrN5bB6R1YnkTbTMSxRpO_7wBP4WV0t1LgBZOMB2P5qLZ13igyhiC7MRzZJsCYC3OM5lERjdQ998vPUcwd3knt2-V9DDb6huNBdHqlIW00" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حضور بیژن مرتضوی و همسرش در دربند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/107802" target="_blank">📅 14:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107801">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82e592cb76.mp4?token=amGzMs3tnbShRlp_2-3JQ6lf-wUbUxAqBCuzfQ-aZ6nLjR73DjaXMyBikJKLjzQR1GczyWKP-_Cj3ktY25YHgdxzFdEiJZLz8vCTnKS0PAEtkaaI0b73X1dqB8R698M4Iagqz7QgIcDEelAneW3lYsvAn9qf0Z5m61cEXrZScnjiRw8v7nTLUbCp1Ert_9w9kN2smACSLtoLFdp-ITEvGdchOXq25c73MrLytqkcAC_q4LGXiFln4t5sfs-PHjwCBHVm_BTWKokZUSpSMd3p2OSX3Tfp8L50nvMYN0_hBKAVogWk344cRN7LwpaIInV9nK7lNCB34m1InVLplo6Txg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82e592cb76.mp4?token=amGzMs3tnbShRlp_2-3JQ6lf-wUbUxAqBCuzfQ-aZ6nLjR73DjaXMyBikJKLjzQR1GczyWKP-_Cj3ktY25YHgdxzFdEiJZLz8vCTnKS0PAEtkaaI0b73X1dqB8R698M4Iagqz7QgIcDEelAneW3lYsvAn9qf0Z5m61cEXrZScnjiRw8v7nTLUbCp1Ert_9w9kN2smACSLtoLFdp-ITEvGdchOXq25c73MrLytqkcAC_q4LGXiFln4t5sfs-PHjwCBHVm_BTWKokZUSpSMd3p2OSX3Tfp8L50nvMYN0_hBKAVogWk344cRN7LwpaIInV9nK7lNCB34m1InVLplo6Txg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇮🇹
یک‌دقیقه با درخشش دوناروما مقابل فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/Futball180TV/107801" target="_blank">📅 14:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107800">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5581b57d8f.mp4?token=vjGklso303yKsBVZ4lafsOTAnVVCDeNZaPO5CQAMbkMTYpJhJmZm9L1A5saOGUjkFzwruAH5ZBzpFt-sIwf3FOFp-epJOdOgmljPC2sfB_6Je8AhFlQPf1m_b3PzcZI1np0fa13ECtSniuRmM1SwSVZDPGRivsN_KtCoCZC7Bbb4RBeq2hwHESKA1CWowLoe_s0A7_ERPj9OBIDT9ym_wpL4GKZ7irIZmm66OUOlKiPFRiailR_UqJFX1cpv1EVAshZjDYtdwB11BpcOjR4-oHsKS414uYJXuwsmXLoYqJn-4_s2F06BdxUJ4AqcdFLAbQG0orl1pCmRKm_71DWyrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5581b57d8f.mp4?token=vjGklso303yKsBVZ4lafsOTAnVVCDeNZaPO5CQAMbkMTYpJhJmZm9L1A5saOGUjkFzwruAH5ZBzpFt-sIwf3FOFp-epJOdOgmljPC2sfB_6Je8AhFlQPf1m_b3PzcZI1np0fa13ECtSniuRmM1SwSVZDPGRivsN_KtCoCZC7Bbb4RBeq2hwHESKA1CWowLoe_s0A7_ERPj9OBIDT9ym_wpL4GKZ7irIZmm66OUOlKiPFRiailR_UqJFX1cpv1EVAshZjDYtdwB11BpcOjR4-oHsKS414uYJXuwsmXLoYqJn-4_s2F06BdxUJ4AqcdFLAbQG0orl1pCmRKm_71DWyrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
دزدی مسئولین از بانک‌ها سوژه جالب و وایرال شده مهران مدیری در مرد سه‌هزارچهره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/107800" target="_blank">📅 13:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107799">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
‼️
⚠️
درگیری‌شدید و خونین در مسابقه‌ای از لیگ زیر ۱۸ سال کشور که در مشهد برگزار شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/107799" target="_blank">📅 13:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107798">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46755fa2d0.mp4?token=as4jOTPojQ4lANWKB6ZfbBodCAunXUHdXFoLW3Emv79ggI4frjMwtJoXYh129kplqKkSzSYcE5ff3j0Y4hasjuUIBIubzL26Hx2O4LvcivARdUB148HXa-7s3335Nw3TwqwGk7tteioArWUWAnoJNNoVgp-PQQc662NaCNEvFJWrdp7tRrypkMMQWH81Kde1BJIfc5GdS-GkHqBEQkSi7LaUcDNrfrOCIqKdQxwnJoqCGlnWCS7Tt_Nn0UcfWVI-sCpH814yILlTR-MhE0Tm_cBdiSqx-VO2p4g_S_6l-xr1FwGPF9ILaZoS2t52ftBOxufiV3rPG_B4CPu6gscXXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46755fa2d0.mp4?token=as4jOTPojQ4lANWKB6ZfbBodCAunXUHdXFoLW3Emv79ggI4frjMwtJoXYh129kplqKkSzSYcE5ff3j0Y4hasjuUIBIubzL26Hx2O4LvcivARdUB148HXa-7s3335Nw3TwqwGk7tteioArWUWAnoJNNoVgp-PQQc662NaCNEvFJWrdp7tRrypkMMQWH81Kde1BJIfc5GdS-GkHqBEQkSi7LaUcDNrfrOCIqKdQxwnJoqCGlnWCS7Tt_Nn0UcfWVI-sCpH814yILlTR-MhE0Tm_cBdiSqx-VO2p4g_S_6l-xr1FwGPF9ILaZoS2t52ftBOxufiV3rPG_B4CPu6gscXXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🐐
از توماس مولر پرسیدن: «مسی یا رونالدو؛ بهترین فوتبالیست تاریخ کیه؟»
جوابش؟
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/107798" target="_blank">📅 12:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107797">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad1675b1b.mp4?token=U1XoOeIZ_MBlADQmtwTOS4mniKtxmQq1DDt4iHVSocYA9-LjvyGs6_zK0GkqQ5D0SWWy-Ou-bZK7iW6ya2xvNDx3I07CBAXoTTh2wM2RHnFAZX1UUIJZv9VmRsyvzS9DV2sUM_DJoglQmL-x2Qj5fJD4foB66pNzP0uCD1VMMel-oWpV0bWWQuMqahAQHHeZfnfioEOeBnwTf2z_l6LE0duAnH5urMdQTNmLPEcJN4dykTRRV2C2JoVRZXxv_nE-NqXDokEU4g4eemPZtvAsF64oZvAX5AFOJkf-mu681MuyCxeRVKYXI3KcvtaWJ3ZcsquEoXuqgo79-G-Tovweiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad1675b1b.mp4?token=U1XoOeIZ_MBlADQmtwTOS4mniKtxmQq1DDt4iHVSocYA9-LjvyGs6_zK0GkqQ5D0SWWy-Ou-bZK7iW6ya2xvNDx3I07CBAXoTTh2wM2RHnFAZX1UUIJZv9VmRsyvzS9DV2sUM_DJoglQmL-x2Qj5fJD4foB66pNzP0uCD1VMMel-oWpV0bWWQuMqahAQHHeZfnfioEOeBnwTf2z_l6LE0duAnH5urMdQTNmLPEcJN4dykTRRV2C2JoVRZXxv_nE-NqXDokEU4g4eemPZtvAsF64oZvAX5AFOJkf-mu681MuyCxeRVKYXI3KcvtaWJ3ZcsquEoXuqgo79-G-Tovweiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇹
عدم‌پاسخگویی سرمربی پرتغال درباره رونالدو در نشست‌خبری پیش از بازی با نروژ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/107797" target="_blank">📅 12:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107796">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a683578dd.mp4?token=EnrwbBnEJqphOPeywbSTqXlW_kn15AAftuk14Z2_3Wtycqf0FWq-x1lyOoSZIAHA3ZV4eyaPf1cGvhSsbWggB02h7TtYlplpff1_JNHPrLG_GdyFey8O3jQaMH23ZNDMjPCey0ii0RmCDELiov9Las2RfKlOPfP936f-pqCKmTYeKHtqIX1CxFObyZLa3LcdJuL2MzZBfcZqdhqJ1U346tHbPtwplF6LDl2WRxapHrjKI-M0u_uedCLgSn1HdCNZ-bfb5cMTPHbQm6PLaE5x6iO_VYHArAkx87p8jYVQguiJfN7E341PynkGhc3Y8j4O4r-TLLeuZTydTj-pToZlBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a683578dd.mp4?token=EnrwbBnEJqphOPeywbSTqXlW_kn15AAftuk14Z2_3Wtycqf0FWq-x1lyOoSZIAHA3ZV4eyaPf1cGvhSsbWggB02h7TtYlplpff1_JNHPrLG_GdyFey8O3jQaMH23ZNDMjPCey0ii0RmCDELiov9Las2RfKlOPfP936f-pqCKmTYeKHtqIX1CxFObyZLa3LcdJuL2MzZBfcZqdhqJ1U346tHbPtwplF6LDl2WRxapHrjKI-M0u_uedCLgSn1HdCNZ-bfb5cMTPHbQm6PLaE5x6iO_VYHArAkx87p8jYVQguiJfN7E341PynkGhc3Y8j4O4r-TLLeuZTydTj-pToZlBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
دهقانی، مسوول مسابقات بین‌المللی فدراسیون فوتبال: باید ورزشگاه آزادی را همانند نیوکمپ بارسلون مسقف کنیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/107796" target="_blank">📅 12:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107795">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa3096b41.mp4?token=mTvbE5n12Cxxxx56o9DZhaJ2h6umAQpbQSEOcN4Zn-D5BvaLxCzT0F3__QrRv5-X0H_0pI4ej2lxOwOKIUwl_GbaaL1zGneB-bDqtpFPJrMAtW_BdcjNqkc6sgBJVjcJtk1pkuxUnlzvQIJZVobFiWd8PCAvUlJypz2G4L6CovLIiMSkR-FnZTzKtGnR7ONAaT-3g1F8NyxDfLIJpD-45XAGziEvUFM3qvEy3U24Ne1sUWco_TQcmtwDSJceKVuE8bxKvKNZVr83tqDebQxSrVofP0cz8sCpZJGpm_e5ACyDxQA8r4HHUiu01zk8gMrJ5SXjAhYuXbAe1FkvN6IBFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa3096b41.mp4?token=mTvbE5n12Cxxxx56o9DZhaJ2h6umAQpbQSEOcN4Zn-D5BvaLxCzT0F3__QrRv5-X0H_0pI4ej2lxOwOKIUwl_GbaaL1zGneB-bDqtpFPJrMAtW_BdcjNqkc6sgBJVjcJtk1pkuxUnlzvQIJZVobFiWd8PCAvUlJypz2G4L6CovLIiMSkR-FnZTzKtGnR7ONAaT-3g1F8NyxDfLIJpD-45XAGziEvUFM3qvEy3U24Ne1sUWco_TQcmtwDSJceKVuE8bxKvKNZVr83tqDebQxSrVofP0cz8sCpZJGpm_e5ACyDxQA8r4HHUiu01zk8gMrJ5SXjAhYuXbAe1FkvN6IBFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🎙
ترس عجیب پیمان یوسفی مجری تلویزیون هنگام نام بردن از روحانی؛ یه وقت نیاید بالاسرمون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/107795" target="_blank">📅 11:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107794">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6ce37f880.mp4?token=b03T_sinEyDc1vD0FvKL9KPek0HvgQIsuTvhtltlO-rqI9TffBMiFoKS9Yaai6FfITRI_DJ-bDM6lCl5GoT4OiyI2UPdqh1bFYKbnahc8H3O_L0L_MX0nHMeHPsC5rFlABSC_kmJ3s4lM9wvQPpt26HOvIoGHF-xdxZY02TxtT5GuoXeiCmDs_xEfM4LlcAyL3qxBbcoIBC74KMcxwbikZrDZ8gBCeMqpBto3A20KRiXKfjmPIvD0jxjqxWJVyYqiXvSJnsEt4WnyBicSNGizMS-QeS-EImT9ZNNW3A0Jg3TFT2z2J98vZy77KR_7jaj7h-48UZpT5AoQrqGMUxnkpSa_zvGYQNlKtRwfKAkgUJ4SIf8QJFvD3-ZkV3m4TE0KbuHS0HqB43TT-Wj--6NI7CgtG5LG-GEB2Eh814Q-Q-_PaAtvO5iCsK8s3ssiXPV31V7D_IQv2ArU1H2DfxIszlx1zRtqS6Tyuyk28CwXSPwdIO59pJ_yi3UW6rykEUGlTnFf95PPWD2MwrA6Y61fdXa_yxtGpyPdr0auVMtYoGdBn_g6yA5lFx8c_c96HnhD-gVOjpzOq8JFT7wPeYyKPxz6fHKHkYnO059FtXObffIuwBWkMSK00SCMvHAJRW88Q53m-IE9W_QPwvpPsKuuhg5W6ZtNHAFGHXTddlwVI4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6ce37f880.mp4?token=b03T_sinEyDc1vD0FvKL9KPek0HvgQIsuTvhtltlO-rqI9TffBMiFoKS9Yaai6FfITRI_DJ-bDM6lCl5GoT4OiyI2UPdqh1bFYKbnahc8H3O_L0L_MX0nHMeHPsC5rFlABSC_kmJ3s4lM9wvQPpt26HOvIoGHF-xdxZY02TxtT5GuoXeiCmDs_xEfM4LlcAyL3qxBbcoIBC74KMcxwbikZrDZ8gBCeMqpBto3A20KRiXKfjmPIvD0jxjqxWJVyYqiXvSJnsEt4WnyBicSNGizMS-QeS-EImT9ZNNW3A0Jg3TFT2z2J98vZy77KR_7jaj7h-48UZpT5AoQrqGMUxnkpSa_zvGYQNlKtRwfKAkgUJ4SIf8QJFvD3-ZkV3m4TE0KbuHS0HqB43TT-Wj--6NI7CgtG5LG-GEB2Eh814Q-Q-_PaAtvO5iCsK8s3ssiXPV31V7D_IQv2ArU1H2DfxIszlx1zRtqS6Tyuyk28CwXSPwdIO59pJ_yi3UW6rykEUGlTnFf95PPWD2MwrA6Y61fdXa_yxtGpyPdr0auVMtYoGdBn_g6yA5lFx8c_c96HnhD-gVOjpzOq8JFT7wPeYyKPxz6fHKHkYnO059FtXObffIuwBWkMSK00SCMvHAJRW88Q53m-IE9W_QPwvpPsKuuhg5W6ZtNHAFGHXTddlwVI4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
🎙
🇮🇷
بغض محمد عمری ستاره پرسپولیس ترکید: از روستا به تهران آمدم؛ شب‌ها با یک بربری می‌خوابیدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/107794" target="_blank">📅 11:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107793">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9581683260.mp4?token=kih0hAj-fRaTT8kpAlym3TuLdiAFhBB82kdNk1BLfS9lJRQYfwd41ZDRt71Uom77xPO9-veGE4YD53PU4lBxFGPdRUDrK6JrM-UrO9p96QjfiRFpwLT2WTSUfAwtZ8gC7VnuOY72xXgkyeydubF9HeXF4fsCsM1kQXRuLyzQO-s1spikdZy7_zN36DanCnC_aWeTPYBa8kh7lBAXgDq3HXoCGfcE2KvmSmxJL7A8jiJpk33lOr8jzQ0BGJVPK3uUcHhPucjqOgIevlsQ6196UqxpkZ2Y_NIU8hE7kRKJe9xcD3Ldf65oobjWmXaD6nN__0DqUUYPW1imioUEWxlZFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9581683260.mp4?token=kih0hAj-fRaTT8kpAlym3TuLdiAFhBB82kdNk1BLfS9lJRQYfwd41ZDRt71Uom77xPO9-veGE4YD53PU4lBxFGPdRUDrK6JrM-UrO9p96QjfiRFpwLT2WTSUfAwtZ8gC7VnuOY72xXgkyeydubF9HeXF4fsCsM1kQXRuLyzQO-s1spikdZy7_zN36DanCnC_aWeTPYBa8kh7lBAXgDq3HXoCGfcE2KvmSmxJL7A8jiJpk33lOr8jzQ0BGJVPK3uUcHhPucjqOgIevlsQ6196UqxpkZ2Y_NIU8hE7kRKJe9xcD3Ldf65oobjWmXaD6nN__0DqUUYPW1imioUEWxlZFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایش های عجیب وینی مقابل هند هم ادامه داشت!
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/107793" target="_blank">📅 11:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107792">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107792" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/107792" target="_blank">📅 11:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107791">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-OV4SiofXTWkKAS6sBIDs2nqCu-7LBRnYaWS28adFMIcWUWpV-bxb4Q4AiMc2fRokuHkKOWeVVdVZMgEcvn1lhbqomwJI0HZYTrJ83pbldxZTf-N8DpkGuWbTtQ3C6Kp-s-s_9txq1F6L2qcFBo2d7sCjCNCUTynOrrnYc0sblZFi2Mi33X1JZD2eoDX1K5vi6Ti2rLgK4A75y9VRjbjymW-rVAo0vQWtJBw3X3oATAqMmPDr8BYuR1WzyMrLlMyGFK1txVxhzLWZf1kM8M4bouGCgBndYtoGrXdgOaKQ6rJwqznQItFwAksWt8-MGZJBg_Yaqt_y-fkrbLdD8eyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/107791" target="_blank">📅 11:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107790">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6634bc99dd.mp4?token=tYd27yGxghgtFpeH_HU805gIeOQotHzsONar_PfPpedc4Fn20u05ydQubGsGy4DJKUs9sX1qYLtmFm-uftZ664SbR_iNRL0wMvt9rtkWlOEDK7UljXLTB8rvdyTcpFlvrHIomIEloTBeU5ThSL1U1zO1UHULX-j49dC_Ef7ov5_I8NV8VM2fPRokZLGask7q1FHPGq-ButzLewODf0AV_ieMU-Wbymn9ozxKIgV6Q2CzAYEr0JARvFjE-3XaHqHDRkYR_EPBZ_FgvykY_E5AHXr1gtW2qS64909s9Sh2t7K5roNopuCccS42LiI5dTAUTXYOlE9RZYNJpKNQkEk_-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6634bc99dd.mp4?token=tYd27yGxghgtFpeH_HU805gIeOQotHzsONar_PfPpedc4Fn20u05ydQubGsGy4DJKUs9sX1qYLtmFm-uftZ664SbR_iNRL0wMvt9rtkWlOEDK7UljXLTB8rvdyTcpFlvrHIomIEloTBeU5ThSL1U1zO1UHULX-j49dC_Ef7ov5_I8NV8VM2fPRokZLGask7q1FHPGq-ButzLewODf0AV_ieMU-Wbymn9ozxKIgV6Q2CzAYEr0JARvFjE-3XaHqHDRkYR_EPBZ_FgvykY_E5AHXr1gtW2qS64909s9Sh2t7K5roNopuCccS42LiI5dTAUTXYOlE9RZYNJpKNQkEk_-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت‌جالب لامین‌یامال بعد از بازی دیشب
❤️
👌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/107790" target="_blank">📅 11:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107789">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/321c017aa1.mp4?token=Xu6ShQj_BzFKybApmDO4rMP-qUG4BGgec7aqMt9RJ1urq6BR5OjxreSiGDZBYFTf_BYLLodlRdKRKMoIPe3F-p9Fx69lo7pIdqr8cn2r9ctoDXEVVvS2cCQlZqCCzQ7i33PhrvQrGxkpS1mluzwfTv55IG5hoKuZsh3lyS0KBNLGpKps9X0dYQTvPYn49MB4a_HP-AKoS5g8fo1LLQTFDSs9bGNYPTmRh2UusJnFUzmi3_D192GXbv5aP99ylfG7kENV25sTtmKn1ajWKj7M5yyQLsQU8JDqrCtcP8QzSNEBXJ8J956JMfn-y4WG_mGtuh1pEDDqaeOcQUJxDH4vsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/321c017aa1.mp4?token=Xu6ShQj_BzFKybApmDO4rMP-qUG4BGgec7aqMt9RJ1urq6BR5OjxreSiGDZBYFTf_BYLLodlRdKRKMoIPe3F-p9Fx69lo7pIdqr8cn2r9ctoDXEVVvS2cCQlZqCCzQ7i33PhrvQrGxkpS1mluzwfTv55IG5hoKuZsh3lyS0KBNLGpKps9X0dYQTvPYn49MB4a_HP-AKoS5g8fo1LLQTFDSs9bGNYPTmRh2UusJnFUzmi3_D192GXbv5aP99ylfG7kENV25sTtmKn1ajWKj7M5yyQLsQU8JDqrCtcP8QzSNEBXJ8J956JMfn-y4WG_mGtuh1pEDDqaeOcQUJxDH4vsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
▶️
کنایه مهران مدیری به ماجرای نماینده مجلس و مامور راهور در مرد سه‌هزارچهره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/107789" target="_blank">📅 10:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107788">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c7979edd7.mp4?token=tpJgPrYMqOTmx8_Xfe7jOyyE-ylJ6S9w9OW6rhSjmHD9xZIKj4pRgcc7mwf5U4_wgrvnFwL-o3L96h8DOuqdQj-e2ebyJRAFGymPV4Al9RnFZLzCbCK6dK_IAkDmQ_xRMdE3C6AT9WFlLBwr9E3FUhxuQmubmAo1ZCMeoWqGVx5n-cOMUxb2POOZDf-NXJPVD07eLQSu_52wBJD7Zq2yf1qTpyizAxo9EubXwVSrnN5Mhn4vwFlHMVAjXteX58EZdSSs_OZxhK8Wb4n9Nysy_oxAmAUsTxZeBa6Mn52qfGL2bmzypPzZ2uZdzqCY2F_vVwhqLBu7sto-pO1bk8WwYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c7979edd7.mp4?token=tpJgPrYMqOTmx8_Xfe7jOyyE-ylJ6S9w9OW6rhSjmHD9xZIKj4pRgcc7mwf5U4_wgrvnFwL-o3L96h8DOuqdQj-e2ebyJRAFGymPV4Al9RnFZLzCbCK6dK_IAkDmQ_xRMdE3C6AT9WFlLBwr9E3FUhxuQmubmAo1ZCMeoWqGVx5n-cOMUxb2POOZDf-NXJPVD07eLQSu_52wBJD7Zq2yf1qTpyizAxo9EubXwVSrnN5Mhn4vwFlHMVAjXteX58EZdSSs_OZxhK8Wb4n9Nysy_oxAmAUsTxZeBa6Mn52qfGL2bmzypPzZ2uZdzqCY2F_vVwhqLBu7sto-pO1bk8WwYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
🇮🇹
درخششِ دوناروما اجازه ی گرفتن انتقام رو به زیدان در بازی با ایتالیا نداد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/107788" target="_blank">📅 10:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107787">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95502ba1a6.mp4?token=fG0OyRKFclRAx_6Tdg0IChOUZ3Wn8hNoZ_Q02I1kPmEwu9xbTL_2ZwlmIKHihjKwuJeOofhXVbs5pAHtynfgUvEtYMKI2DT6bu1St4fqj_fOv6Cp94VLX0ZFdFxIC35bvyV5AOVdKiZUi6ThY1zN8XyFxwAG4r12IPMR3yz9mCq-Fnlzuai3o-v4vrpu9CTNW43-CkZeCzwp0cQlMgssmoM7MY7G3NUmaiZdqRMbBc5OtUSEhtbvzMqLduImPNToqWzopbuWfbt7QUwVzIBZ6HHHxYy0NOxWTExa8URPN91j8VIynj-xWg9uyxEd24CTRIpg2ZNdqwOTRPpDPujXai0Nn9XSs-0T5qL9mghXizKTulhKbUYbYHuMH5VCR28RcrPC9DVG7kZlP96duMoZQ0Z1LwwQCfFP-rlnfwIWcAIZf1gzKxQyUD3ebzVClzyVmoU6ddIfwQAY8He7FCTLh9mZrdoc6E1WLRzIHxOiKJDGV48sCzbmOGaArGpcHXjrbvP5Jd8bYhrAAii5jL9na8thxO7muNm3i4TJP2X49BFQugRT27eUFZXu8jtBCKWDgyttIdoKxxh89PnzIw-Jj8wLco32EEEUoK2ZikQxZq4NA9yR5evZLiUQVOsR0xLYCTBN_zBrnJjDd7cQ_aiA8gz78iGtl4lUQsrmfx9iSog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95502ba1a6.mp4?token=fG0OyRKFclRAx_6Tdg0IChOUZ3Wn8hNoZ_Q02I1kPmEwu9xbTL_2ZwlmIKHihjKwuJeOofhXVbs5pAHtynfgUvEtYMKI2DT6bu1St4fqj_fOv6Cp94VLX0ZFdFxIC35bvyV5AOVdKiZUi6ThY1zN8XyFxwAG4r12IPMR3yz9mCq-Fnlzuai3o-v4vrpu9CTNW43-CkZeCzwp0cQlMgssmoM7MY7G3NUmaiZdqRMbBc5OtUSEhtbvzMqLduImPNToqWzopbuWfbt7QUwVzIBZ6HHHxYy0NOxWTExa8URPN91j8VIynj-xWg9uyxEd24CTRIpg2ZNdqwOTRPpDPujXai0Nn9XSs-0T5qL9mghXizKTulhKbUYbYHuMH5VCR28RcrPC9DVG7kZlP96duMoZQ0Z1LwwQCfFP-rlnfwIWcAIZf1gzKxQyUD3ebzVClzyVmoU6ddIfwQAY8He7FCTLh9mZrdoc6E1WLRzIHxOiKJDGV48sCzbmOGaArGpcHXjrbvP5Jd8bYhrAAii5jL9na8thxO7muNm3i4TJP2X49BFQugRT27eUFZXu8jtBCKWDgyttIdoKxxh89PnzIw-Jj8wLco32EEEUoK2ZikQxZq4NA9yR5evZLiUQVOsR0xLYCTBN_zBrnJjDd7cQ_aiA8gz78iGtl4lUQsrmfx9iSog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
نمای‌کامل از صحنه‌جنجالی بازی لیگ‌برتر بانوان میان استقلال و گل‌گهر سیرجان؛ فقط جیغ و داد داور و بازیکنان رو ببينيد
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/107787" target="_blank">📅 09:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107786">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363181b8d9.mp4?token=k_p3HzP6axPCildBXNmvc37gFjvLvsCD8K7nTxJO49kxRmkvO7GFdgwWokTIeCgMl7dHFWHjZypgmomd-M1e1x84PUmcW4ku1I8PvVMMe8hFrvJ1xC_DZYf1gFeNHTo26pmtRVoauR2ToFu0AcfXCjBvfyJkl0BpoCWRPltDNNZ6jsdF5SiDxqbP8cp80fu7ppTuCzD8CZHa9pkhrqBblderMtFS-eeCj353Xv-hBsMPzR-rnkdtB1o9gBUTZaqL2e_pfPFuUQzI_mVyyMaY_RQhn5COb8C5G4fR2xpnsN9ksCXb9dskXGd3Oc0E_3W0wGAADQjgNX70jb1MPsnMiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363181b8d9.mp4?token=k_p3HzP6axPCildBXNmvc37gFjvLvsCD8K7nTxJO49kxRmkvO7GFdgwWokTIeCgMl7dHFWHjZypgmomd-M1e1x84PUmcW4ku1I8PvVMMe8hFrvJ1xC_DZYf1gFeNHTo26pmtRVoauR2ToFu0AcfXCjBvfyJkl0BpoCWRPltDNNZ6jsdF5SiDxqbP8cp80fu7ppTuCzD8CZHa9pkhrqBblderMtFS-eeCj353Xv-hBsMPzR-rnkdtB1o9gBUTZaqL2e_pfPFuUQzI_mVyyMaY_RQhn5COb8C5G4fR2xpnsN9ksCXb9dskXGd3Oc0E_3W0wGAADQjgNX70jb1MPsnMiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
▶️
‼️
علی فتح‌الله‌زاده:
🔺
فدراسیون با یه قانون من درآوردی سه جانبه برگزار کرد، میتونست با همون منطق بین ۴ تیم اول بازی بزاره قهرمان مشخص کنه.. به استقلال ظلم شد چون به احتمال ۹۰ درصد تو حذفی قهرمان بود و اون جام رو هم از دست داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/107786" target="_blank">📅 09:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107785">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/708801c3df.mp4?token=ErybHLwqfVuEG_-TEhv57kVV8kD5bPuIuk3A0qOVkLSVccQ6BKxysesnn4__h43-vg1mmeob6bjI3noTfZxtaHLETtNftI6gS6Ca06gzfjmtElPSjwZdwWEvkwSaQDHXL0CzEzOyWZ02FKzOpwCIADb8yTO44Wx9LeEyyuL5e5v0iNcFH9GEHoKvFARqeXDHfQp1A95AnBRn2WFHBTTQKFKrX-rA7x9gjZvuqF3qPNsDBz8b5NiH8k0N89_MZVUNMU0Kwjz3-MUcY9h8iOXeKtul_Ywd9e7i0r-BBorNwrrShqqAGjEJuflDXG1Oa45CfFRxQG7ySwQOSRJJZuoudQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/708801c3df.mp4?token=ErybHLwqfVuEG_-TEhv57kVV8kD5bPuIuk3A0qOVkLSVccQ6BKxysesnn4__h43-vg1mmeob6bjI3noTfZxtaHLETtNftI6gS6Ca06gzfjmtElPSjwZdwWEvkwSaQDHXL0CzEzOyWZ02FKzOpwCIADb8yTO44Wx9LeEyyuL5e5v0iNcFH9GEHoKvFARqeXDHfQp1A95AnBRn2WFHBTTQKFKrX-rA7x9gjZvuqF3qPNsDBz8b5NiH8k0N89_MZVUNMU0Kwjz3-MUcY9h8iOXeKtul_Ywd9e7i0r-BBorNwrrShqqAGjEJuflDXG1Oa45CfFRxQG7ySwQOSRJJZuoudQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🥈
ایشون کیمیا زارعی ورزشکار رشته روئینگ هستن که تو مسابقان ناگویا یه مدال طلا و یه نقره به دست آوردن
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107785" target="_blank">📅 09:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107784">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a540d193c.mp4?token=OOAWzDubXRytsGo7v2mMp8DjmkwwvXia9kZJYLJxriq5aWFzlhejOAC1weCY8Nly6gzVJIXDGGPEYwciOeBajMDaXIEnBXMwItsRNS_NbR7rpnUC6MYHPUJvaGuQ_V2sGxg8jcYKr_2lzJiLj5bPoCvb5plzCDJWDbxvfEKb4VxgcZ5wK3xwdtJlLt999WhhFmFOiR9ORVY2r6JRwOU22MEwjk50ioRtv3Od8RmuvQaDoQ7wNhp1QPyg_wJjZdpaY96xa3zjZC9sAtcW2Tegi7AW_fIypBllIQGPtiuFSSWoJ_c1_dPGTT3qqZEWvl3pXfirmMx1HdXxpwkLow0tcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a540d193c.mp4?token=OOAWzDubXRytsGo7v2mMp8DjmkwwvXia9kZJYLJxriq5aWFzlhejOAC1weCY8Nly6gzVJIXDGGPEYwciOeBajMDaXIEnBXMwItsRNS_NbR7rpnUC6MYHPUJvaGuQ_V2sGxg8jcYKr_2lzJiLj5bPoCvb5plzCDJWDbxvfEKb4VxgcZ5wK3xwdtJlLt999WhhFmFOiR9ORVY2r6JRwOU22MEwjk50ioRtv3Od8RmuvQaDoQ7wNhp1QPyg_wJjZdpaY96xa3zjZC9sAtcW2Tegi7AW_fIypBllIQGPtiuFSSWoJ_c1_dPGTT3qqZEWvl3pXfirmMx1HdXxpwkLow0tcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
🐐
حمایت فیلیپه ملو از کریستیانو رونالدو:
"یه تفاوت خیلی فاحش بین رفتار بازیکنا با کریستیانو رونالدو و رفتار بازیکنای آرژانتینی با مسی وجود داره.‌ من می‌بینم وقتی بازیکنای حریف مقابل کریستیانو رونالدو بازی می‌کنن، خیلی بیشتر بهش احترام می‌ذارن. تو تیم ملی پرتغال، هیچ‌کس حتی به گرد پای کریستیانو رونالدو هم نمیرسه! تو نمی‌تونی بذاری بهترین بازیکن تاریخ همین‌جوری بذاره بره، انگار نه انگار که اتفاقی افتاده؛ اصلاً راه نداره!"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107784" target="_blank">📅 08:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107783">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d08431eb67.mp4?token=u-tSwNQLTBN4lc6kIJOjX1C1LW3xdbvID4hPVh81UHAOmnq02DxF3EMK1euf2Fg2cQyjcpOLdchnpLlf4VKKfA226_ufHHG8lmEZYaKmV9Sz_1zGNj9b9RQ50QElR17lOAqf7kamlt-y45Vi05d-6ZZRP-zDhtjKLkTBsKNxsqgsRDPhkHl-VUWaIKGLzGbk5D0loC0eV6imVS06BCGFnIejJ1xKRC5lZvlk-gLoyIbI3MhD4bhwj8WIzyv-9uHkus7sK5_TK-sjAbPeX5jHkNaH2MTJWd9rWwHXhYazJ50FdBMHHpT2V7lZWVOFTQF6wcayzaTd1HHu4ataQvbwBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d08431eb67.mp4?token=u-tSwNQLTBN4lc6kIJOjX1C1LW3xdbvID4hPVh81UHAOmnq02DxF3EMK1euf2Fg2cQyjcpOLdchnpLlf4VKKfA226_ufHHG8lmEZYaKmV9Sz_1zGNj9b9RQ50QElR17lOAqf7kamlt-y45Vi05d-6ZZRP-zDhtjKLkTBsKNxsqgsRDPhkHl-VUWaIKGLzGbk5D0loC0eV6imVS06BCGFnIejJ1xKRC5lZvlk-gLoyIbI3MhD4bhwj8WIzyv-9uHkus7sK5_TK-sjAbPeX5jHkNaH2MTJWd9rWwHXhYazJ50FdBMHHpT2V7lZWVOFTQF6wcayzaTd1HHu4ataQvbwBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
سوپرگل سکسی یامال در تمرینات اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107783" target="_blank">📅 08:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107782">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107782" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107782" target="_blank">📅 01:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107781">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsfYxixG7GvR3TUho17zXwM3w7C_k77kPJ-s6H02_lLOJi6MNLSvAt4kEO12oYUvOY-sIcQgHrW8l4JBCbYhGjyaA55dcYoevsqTUM8XF19tN0q3GhfqskCKFoKdd2EuMY81ox3911TWX3eC7NgDUBXnrWSzFsJnmrlzfBreP4SJkI0a3cHtZaUBXqIt6xTBVW3WhUzjG40FwUgTMY608yRcRebcuHLBFFuSrEEz6r4uj46edPEeubEWIVvpuxWhCN0oT8PDOUkCuncFSLVuMYwBVsX7AM8DCPg4SFreS5haMFUs4vq-5XebQYHCfUjUwKrUeH6jpH0UALPath7K9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107781" target="_blank">📅 01:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107780">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df11e10418.mp4?token=evcKO7axXHupbPTSVCU6BB-H6jlpIAzGptQcT-u5j1qPfjkcE9HtuA6oXHwrU93T4BI5lw51Zv1qJ5_9BVpNlpz8GnlexQFIxI_v4xbt63l3GVc15ATW7I-1EUkShjvNdtCc6qkmb_I7poJxrXi5xPYIbgGQFq06lpzLZbMygvkrhSLGJ-vL5XvXvGbcOPMAvIekrqkXWn-3seaYWBU6i8apRKc_nO9AuNLiJDt_f1Eom_fOMf0KV-OUj0h8FelHI5FpOeh5EymJZFTtpO4sCMQ-UsIPOc9C4K3p4t_7ptreoNn2z6B_TJeTp3G1tlBNtHqFWDHzjG8Lj_KIO90u7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df11e10418.mp4?token=evcKO7axXHupbPTSVCU6BB-H6jlpIAzGptQcT-u5j1qPfjkcE9HtuA6oXHwrU93T4BI5lw51Zv1qJ5_9BVpNlpz8GnlexQFIxI_v4xbt63l3GVc15ATW7I-1EUkShjvNdtCc6qkmb_I7poJxrXi5xPYIbgGQFq06lpzLZbMygvkrhSLGJ-vL5XvXvGbcOPMAvIekrqkXWn-3seaYWBU6i8apRKc_nO9AuNLiJDt_f1Eom_fOMf0KV-OUj0h8FelHI5FpOeh5EymJZFTtpO4sCMQ-UsIPOc9C4K3p4t_7ptreoNn2z6B_TJeTp3G1tlBNtHqFWDHzjG8Lj_KIO90u7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎁
زلاتان ابراهیموویچ به مناسبت تولد ۴۵ سالگی‌اش، یک خودروی فراری مدل F80 کادو داده. قیمت این فراری، حدود ۳.۶ میلیون یورو تخمین زده می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107780" target="_blank">📅 00:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107779">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f84ad4f46e.mp4?token=UNWg02HeXnT7UhaWp7OzpCYbj-TvkTtNwQWTT7JJtrjLC5BgBLgr3l7pGEKBT8-xzZVE_9d1RU1zfMeajZC4vk6Eci2Tz303xGEQCKS0MQwVzKW9UdKxc1JciBorvIXd5TOzreoS7XH3XTlT6jq5WyJKEJCOGYLtw08dvUGqahZLUMM3TfnlBg-ffKynj72y6ZXGnDxDHJh8Y-6VgDiHn2aKeNVf-_Nh0TfC9uGSRs4FVfO1xIGE4ZbXyjAFvN7bx39NsbUVmt-jSKMd8mjrlKoooqjNWNjflYdMJjcd4Y3auDvFNdO7PhjmEAutNNcFjXM_wEK8gfiG9ypiOXdTrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f84ad4f46e.mp4?token=UNWg02HeXnT7UhaWp7OzpCYbj-TvkTtNwQWTT7JJtrjLC5BgBLgr3l7pGEKBT8-xzZVE_9d1RU1zfMeajZC4vk6Eci2Tz303xGEQCKS0MQwVzKW9UdKxc1JciBorvIXd5TOzreoS7XH3XTlT6jq5WyJKEJCOGYLtw08dvUGqahZLUMM3TfnlBg-ffKynj72y6ZXGnDxDHJh8Y-6VgDiHn2aKeNVf-_Nh0TfC9uGSRs4FVfO1xIGE4ZbXyjAFvN7bx39NsbUVmt-jSKMd8mjrlKoooqjNWNjflYdMJjcd4Y3auDvFNdO7PhjmEAutNNcFjXM_wEK8gfiG9ypiOXdTrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
‏لحظه
اصابت صاعقه به برج میلاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107779" target="_blank">📅 00:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107778">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzzIrk3VOr5iicReytVtmA4lcfY_y_QZnXOqD5rJeR-BHxL1qy0dI_tXZC8ZLliNaO06ye-DeGWtKWgmX-Z_ZZT-vyIsyoT5FwjpOikcVifA2Bce9zCni_gqxrIZXV8xXyu7AhgL75yJVdu_MJIPOkgOXk5izag1DpBopocxbrKY-SotH8EuIL8zAQuzhiR-Al_VqUC0atD5DJX33JSVwpWnV3EZGP4Vfvak2RKzHDJouRUm9RXVoNW5WgHYm4TVZzUX9ADhXqQTiteEj8CBW7lBDPhTxTOjkVP8N-6JNPlbspOWVmrJU1Yx9aSP-OqNwxEvEjGTU8opWP7ciMAFXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
لیگ ملت‌های اروپا| تیم اول و دوم ندارد؛ اسپانیا با هر ترکیبی برنده می‌شود
اسپانیا سه - ‌چک یک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107778" target="_blank">📅 00:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107777">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abea032aaf.mp4?token=Rezygc2-vupeKGZfjNMjrfq0zzSKKWkJjUw5c-Q8Ep2nFYFlh59w_2Fn31kkhPyf2dzAK8UriQ-4Sd1jpyI31EAX_Km4FRMPnfl1MErF6kOXYQNbUlR0w4p5b8SpZl7FsNS5KztgAMBTXZT2VuH_a8tibPeHFoXjGatnpX3FuiyprsY_5pAjYdt8pQ_Naw_O-L30_rvBLptAsi3UTYr1FAdlxDAJBjOOD6edwQvzQQDRmuyYQdGW8enESEr4ezNQ2JXb1yoCEaKwbMD5aCg1Zey-73lmV6pqSzA7WQ_Yaf3JvDlNW7sSbauLdRYSlek_gQGHjWLKdOEJ3uBtygqPcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abea032aaf.mp4?token=Rezygc2-vupeKGZfjNMjrfq0zzSKKWkJjUw5c-Q8Ep2nFYFlh59w_2Fn31kkhPyf2dzAK8UriQ-4Sd1jpyI31EAX_Km4FRMPnfl1MErF6kOXYQNbUlR0w4p5b8SpZl7FsNS5KztgAMBTXZT2VuH_a8tibPeHFoXjGatnpX3FuiyprsY_5pAjYdt8pQ_Naw_O-L30_rvBLptAsi3UTYr1FAdlxDAJBjOOD6edwQvzQQDRmuyYQdGW8enESEr4ezNQ2JXb1yoCEaKwbMD5aCg1Zey-73lmV6pqSzA7WQ_Yaf3JvDlNW7sSbauLdRYSlek_gQGHjWLKdOEJ3uBtygqPcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم اسپانیا به جمهوری چک توسط میکل مرینو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107777" target="_blank">📅 00:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107775">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f7684655.mp4?token=K_nMilXULm7w_LsACBlrEXCJcTcz2-6TjKxdiBDswl-U7DMzLM5i2YXsOlktjoQoZiS5kNe7TdHJke3dmuUGRy2d_6raJgp1j4AlJ13XtfuWQDOLN662h2RgPjGeMbXWYEgy6R-irJVBeaDCXTFZAP-n08rG1XYSei3Le85wgY9T1cnlaiDkCv79ryrU3mp8qKOUj1xQlyS8dmu1WhHG9tfplMi_iKI2f2OWRGxyEx-PTFekyY4jsNLcYraYCTPA3dqRFAog4ub-c5k21Qx9EfkQqpBJeRTofKwR-MegEMn92tCeDnm0TJvk1j6bkV0EoCEhaAGXEq-5pD7KyWd63Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f7684655.mp4?token=K_nMilXULm7w_LsACBlrEXCJcTcz2-6TjKxdiBDswl-U7DMzLM5i2YXsOlktjoQoZiS5kNe7TdHJke3dmuUGRy2d_6raJgp1j4AlJ13XtfuWQDOLN662h2RgPjGeMbXWYEgy6R-irJVBeaDCXTFZAP-n08rG1XYSei3Le85wgY9T1cnlaiDkCv79ryrU3mp8qKOUj1xQlyS8dmu1WhHG9tfplMi_iKI2f2OWRGxyEx-PTFekyY4jsNLcYraYCTPA3dqRFAog4ub-c5k21Qx9EfkQqpBJeRTofKwR-MegEMn92tCeDnm0TJvk1j6bkV0EoCEhaAGXEq-5pD7KyWd63Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول جمهوری چک به اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107775" target="_blank">📅 23:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107774">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdcc4901e9.mp4?token=U6XcSkOaGb9Pl3bRRA7aW5bWqnHbekCNpuewtRfvhP5nHUTADPRBOgm7pYsW1dB4au0LBglcKL6OAP7q2CNWLLLuPCN1MSte73eQQ9yxfluhN5GM1LzEAdIhFFv9KquiiHaOMb4znsTCedR5WM2iG4lGsYRSoxRrb2qsrserLEhKk2EIzAK5rpO8udpIsvWgtdjBsUk8P7v6XcEI5r2GO7UAZUDOlnn80z7K04XX8A8CacnSp94_7rFp90VG18FoSOxXsOvYydNw0UoI14bag30HDSmedGrdp4FDPm5Iqk62ckE3VfdpOLzc0ncuMsW4fomSXzKwYHcHMqHBok8RKqchtHc7ceuYyHyiMF_kWLC6QOQjq4Alr1uP90DRVWQKma6GY65fl4zR73YecSP2MFhVz_u43tj1sWlT2asF3cmtjzel6f9ATztP_EcPxNXQ584wCkSDgZo-HVn_Oxq7rA1VtOewU5JPnpboPLzBuGCU0SvcvJwpicEk-olkrJoQ2SKiP4dfiuNdr86e8a6GuLqvEnBi6pP_uIztj2KtW1GBzvp8DLtdc4FKKh9dn5BT1WTWlxQGaDxlC2Al42r6iZOf_CIayJuST40Dcz6gp4mkDldrM6zZufZS54agc4wljJzCmlkqSWYA7ehdpQs9zOEwQbCOhz_U1OUEpirATjY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdcc4901e9.mp4?token=U6XcSkOaGb9Pl3bRRA7aW5bWqnHbekCNpuewtRfvhP5nHUTADPRBOgm7pYsW1dB4au0LBglcKL6OAP7q2CNWLLLuPCN1MSte73eQQ9yxfluhN5GM1LzEAdIhFFv9KquiiHaOMb4znsTCedR5WM2iG4lGsYRSoxRrb2qsrserLEhKk2EIzAK5rpO8udpIsvWgtdjBsUk8P7v6XcEI5r2GO7UAZUDOlnn80z7K04XX8A8CacnSp94_7rFp90VG18FoSOxXsOvYydNw0UoI14bag30HDSmedGrdp4FDPm5Iqk62ckE3VfdpOLzc0ncuMsW4fomSXzKwYHcHMqHBok8RKqchtHc7ceuYyHyiMF_kWLC6QOQjq4Alr1uP90DRVWQKma6GY65fl4zR73YecSP2MFhVz_u43tj1sWlT2asF3cmtjzel6f9ATztP_EcPxNXQ584wCkSDgZo-HVn_Oxq7rA1VtOewU5JPnpboPLzBuGCU0SvcvJwpicEk-olkrJoQ2SKiP4dfiuNdr86e8a6GuLqvEnBi6pP_uIztj2KtW1GBzvp8DLtdc4FKKh9dn5BT1WTWlxQGaDxlC2Al42r6iZOf_CIayJuST40Dcz6gp4mkDldrM6zZufZS54agc4wljJzCmlkqSWYA7ehdpQs9zOEwQbCOhz_U1OUEpirATjY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
کارشناس صداوسیما: چین دیگه بهمون تصاویر ماهواره‌ای نمیده و بهمون گفته اول برید مشکلتون با آمریکا رو حل کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107774" target="_blank">📅 23:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107773">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‼️
💵
دلار به 271 تومن رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107773" target="_blank">📅 23:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107772">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a91b6171a6.mp4?token=pAq4Gyxb1yZXULGldq6vMyqi2uCNa9abf37RAXHbeLAAevDi6UaGN5rkhAoOwi3MX7Gz5GQ9bt4LAbl7LmaaPK9hUAPYdjnZNu6VE7vdrznmW9eNIIhWuRIeX91uZ-4foilL7Ypei7a8CwYpxU6St2ds0wjX-d81jkMXyHhFheoKKU80WPWvDgMr_cTTS80UeLtX2utjV4gDhb1j1R9ERU0H4gumCmpm_ohxvlKXeXL442MYsVoxWHgCDmzcEY5TQknLKhQOjX4VxxDMxoWJH8TprqzZawBkjz4-Oz5aFhzjd2HwyQOuyCfxToxFvCJmMbMyb1BolodBe4o6LImFfodgwiVNW_slLknCFlBj2ZriWYtQLbtp7dev5oGvLPmJDhgToiLuGNOhniLVt5MvoryVJJxlyW5mfY0z9AE-ffrdtSWEhM6wJ1-iwrg0zk2XQSxgv0enVfDwdfqYXhW5Mr_2YGdz0M7NpYHyQXOhcmq0dUejrXWDsPOEenn2n9VumBfd3e2H5i9pqLuT_mzGzrKvgKXIxdVGAv37yAmzUwBUA4K7db0PlU_tSjMVr86YpYYLOnz-0ck7tjZTrfGhXBtTFffnye62SA5dutxYvO89YV4NWKdTnhzaze6j3fcTZRAciEqPMVw8FN8ltgEPlZH-4g9xAcx69N8LUj7Yevw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a91b6171a6.mp4?token=pAq4Gyxb1yZXULGldq6vMyqi2uCNa9abf37RAXHbeLAAevDi6UaGN5rkhAoOwi3MX7Gz5GQ9bt4LAbl7LmaaPK9hUAPYdjnZNu6VE7vdrznmW9eNIIhWuRIeX91uZ-4foilL7Ypei7a8CwYpxU6St2ds0wjX-d81jkMXyHhFheoKKU80WPWvDgMr_cTTS80UeLtX2utjV4gDhb1j1R9ERU0H4gumCmpm_ohxvlKXeXL442MYsVoxWHgCDmzcEY5TQknLKhQOjX4VxxDMxoWJH8TprqzZawBkjz4-Oz5aFhzjd2HwyQOuyCfxToxFvCJmMbMyb1BolodBe4o6LImFfodgwiVNW_slLknCFlBj2ZriWYtQLbtp7dev5oGvLPmJDhgToiLuGNOhniLVt5MvoryVJJxlyW5mfY0z9AE-ffrdtSWEhM6wJ1-iwrg0zk2XQSxgv0enVfDwdfqYXhW5Mr_2YGdz0M7NpYHyQXOhcmq0dUejrXWDsPOEenn2n9VumBfd3e2H5i9pqLuT_mzGzrKvgKXIxdVGAv37yAmzUwBUA4K7db0PlU_tSjMVr86YpYYLOnz-0ck7tjZTrfGhXBtTFffnye62SA5dutxYvO89YV4NWKdTnhzaze6j3fcTZRAciEqPMVw8FN8ltgEPlZH-4g9xAcx69N8LUj7Yevw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
جواد خیابانی بعد چند ماه نمایش خداحافظی از تلویزیون امشب دوباره به شبکه‌ورزش برگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107772" target="_blank">📅 23:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107771">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd54269d70.mp4?token=g7_vkOirtzBfRd25d5o9OE_ID12Ny5rLnb8B-UPMqifB_XxJHa76Z6yMtffKuUd-CTKnIcbynnoNz4YECOxIbQJaK3qTH9v3Zoa2Uf8LEnrmpYAWNsGbN9Qzxr8CqLZ51-5eMLrG59cT_dQyef3ckOgv7YNfpk8zcesP_5m9bZG2cHD3r7UVMi-S4tesYRp5HzPrrMje3xJNAZ0EnjOFGkBbScTZJg80uijkyCjFFvtDo_kBjJpdrfCuGCPk2DmfLeb_Z-hL4eoZaLaQUE7vXhZZfCgKCLy7aK98Le3kAPZnjLwDQJJ7sJIYW_PqnVszwUMINa5-dbdoAzLPtpQEqh5wntKZjUYNtWwiSyxhmKcFvx1-_k9WXYU7lKjHODZjcttU2zTsSUlHsLjKdxjj3D8oOlqvLmHrpojLEgTqJ0ioAtZPsSMh5l2dZlkGlNyv7o3njGT4roEXG1akuzZGn8-3Ihu-cguXyJSG6YQGEpWG4FH1_QeB7dRoMJY7xMmj3aU4c8cf_B0rr2xVmhfXI-lHguhtR3ZJiuFnEWyL0w-0oLz5-B8WduYBb5UiJZIGklX8PBumbo26M9Xn2Howo9as8GGyev5UN8c4_wzfZGm5RAgx6gSEf2Ws-v6zv845pUVv5sp77nIgGotgj4Jvp7v69yYusogFkMo_q68d1oo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd54269d70.mp4?token=g7_vkOirtzBfRd25d5o9OE_ID12Ny5rLnb8B-UPMqifB_XxJHa76Z6yMtffKuUd-CTKnIcbynnoNz4YECOxIbQJaK3qTH9v3Zoa2Uf8LEnrmpYAWNsGbN9Qzxr8CqLZ51-5eMLrG59cT_dQyef3ckOgv7YNfpk8zcesP_5m9bZG2cHD3r7UVMi-S4tesYRp5HzPrrMje3xJNAZ0EnjOFGkBbScTZJg80uijkyCjFFvtDo_kBjJpdrfCuGCPk2DmfLeb_Z-hL4eoZaLaQUE7vXhZZfCgKCLy7aK98Le3kAPZnjLwDQJJ7sJIYW_PqnVszwUMINa5-dbdoAzLPtpQEqh5wntKZjUYNtWwiSyxhmKcFvx1-_k9WXYU7lKjHODZjcttU2zTsSUlHsLjKdxjj3D8oOlqvLmHrpojLEgTqJ0ioAtZPsSMh5l2dZlkGlNyv7o3njGT4roEXG1akuzZGn8-3Ihu-cguXyJSG6YQGEpWG4FH1_QeB7dRoMJY7xMmj3aU4c8cf_B0rr2xVmhfXI-lHguhtR3ZJiuFnEWyL0w-0oLz5-B8WduYBb5UiJZIGklX8PBumbo26M9Xn2Howo9as8GGyev5UN8c4_wzfZGm5RAgx6gSEf2Ws-v6zv845pUVv5sp77nIgGotgj4Jvp7v69yYusogFkMo_q68d1oo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
هنوز چند روز مونده تا پدیده ال‌نینو وارد کشور بشه بعد وضعیت امروز عظیمیه کرج:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107771" target="_blank">📅 23:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107770">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9943a67dd4.mp4?token=a_fLBHa0AyuKp4K3CKWp2kIeU6gJ8Nosn_-Y3zjt6kSfXwvhOFQ84d5SzC7klaky5FejXDcGGbKjk4NFhP412XEjpTjlXvGPCbRP_4_iCevEqL4ltIUUkcXeO1uhwSOI_DC9-OnLBs5jCgI8AJSiI-LzO7ZNacGEd2AHbpuIx8rocsUSv9JaN5Zr0JzUo2q7EwMMFJb_f4dBgZTGpWe6aXP0ppkXf60YaxQelTqbRWaLkYa5tMDcFrlfWZUP6fli2sygLGl1F4JTGqH6CJDkpayCwpEvGXd8X_ue0IAgzMXW3ajMh0_nxWYRpCxCOwxQSWZV2Go1ulD48YyvGrbNZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9943a67dd4.mp4?token=a_fLBHa0AyuKp4K3CKWp2kIeU6gJ8Nosn_-Y3zjt6kSfXwvhOFQ84d5SzC7klaky5FejXDcGGbKjk4NFhP412XEjpTjlXvGPCbRP_4_iCevEqL4ltIUUkcXeO1uhwSOI_DC9-OnLBs5jCgI8AJSiI-LzO7ZNacGEd2AHbpuIx8rocsUSv9JaN5Zr0JzUo2q7EwMMFJb_f4dBgZTGpWe6aXP0ppkXf60YaxQelTqbRWaLkYa5tMDcFrlfWZUP6fli2sygLGl1F4JTGqH6CJDkpayCwpEvGXd8X_ue0IAgzMXW3ajMh0_nxWYRpCxCOwxQSWZV2Go1ulD48YyvGrbNZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل دوم اسپانیا به جمهوری چک توسط رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107770" target="_blank">📅 22:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107769">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a73573624.mp4?token=ThIEsKep5ehq55GEYuTTahHQ4cvd9pdX_6K71CK8opVOuginY_YvrwplqDgCheGcE7obYuVRTY2VJaGjagqseIE4B-FVVXrrvokMiEuegtg1E8N7cfRL3EqthMrZ3-txwKTBYZW8mZBcZ47w1Wuzn43iqufgK6BiLd_oD4DswMxThRpNbhfST9czBmUjxF1r8mJYNk4CieuUFEyyIrtmTFMCkX7Hz2KYivElxWE8jgIlEc7yD-wby1ttbV8aqZYYsoRXgr_Lt13xgOBKSzmqonB3xHfNfCx8Pxuq6cTImO_O3kIcH3LLcIj0QkQWV8nhPSmK1dO2YGQJeiG2DBPCqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a73573624.mp4?token=ThIEsKep5ehq55GEYuTTahHQ4cvd9pdX_6K71CK8opVOuginY_YvrwplqDgCheGcE7obYuVRTY2VJaGjagqseIE4B-FVVXrrvokMiEuegtg1E8N7cfRL3EqthMrZ3-txwKTBYZW8mZBcZ47w1Wuzn43iqufgK6BiLd_oD4DswMxThRpNbhfST9czBmUjxF1r8mJYNk4CieuUFEyyIrtmTFMCkX7Hz2KYivElxWE8jgIlEc7yD-wby1ttbV8aqZYYsoRXgr_Lt13xgOBKSzmqonB3xHfNfCx8Pxuq6cTImO_O3kIcH3LLcIj0QkQWV8nhPSmK1dO2YGQJeiG2DBPCqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
گل اول اسپانیا به جمهوری چک توسط یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107769" target="_blank">📅 22:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107768">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اشک شوق قهرمانی و معافیت از سربازی
بازیکنان تیم امید کره جنوبی چهارمین قهرمانی متوالی این کشور در بازی‌های آسیایی را رقم زدند و این قهرمانی برای بازیکنان کره به معنای معافیت از خدمت سربازی ۲ ساله بود تا این گونه اشک از چشمانشان جاری شود
البته لازم به ذکر است که همه بازیکنان این تیم همچنان ملزم به گذراندن دوره آموزشی هستند، مسیری که سون هیونگ مین هم قبلا طی کرده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107768" target="_blank">📅 21:52 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107767">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انگلیس هفتا به کرواسی زده
😐
😳</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107767" target="_blank">📅 21:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107766">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3svZS0ooJ2I66H3WhLNCP5FQvLaHkCkNEmtC9qwPgat-zRI8cxubJxyd1Q30pIaQ5ZDhqh_ktszUs14OHor96u1cx9lT5z8Vie5TMDqwzZxHL9dPxAPAhKr1HjWfXlStCy5GOQS43DXGSXmsCJv-62LcUdRd_M42nMesy2uOWJJSuPuj34oFBT9VWPybAWKlrq4PKDKdv4W1gmAvepozmzltnWyV_M1SQxj4F0LYuxG1B1DtjIE-dv2G0wEIyzn9pHBHExKTLJBKkgPQT6nmY-zhq6VEXGJ4J9oJ2Ng4jftequaAZ5vThuDUAM_iyDEwIsNRYgEQR7qjQzILA6bwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترکیب تیم‌ملی اسپانیا مقابل جمهوری چک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107766" target="_blank">📅 20:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107765">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiSkmDGnoA9dhLuV4tDg9FLunm7CgnAtrhP_H_-8KaUZBzF-kHT8pNDq6Vdu-gEiT8MxbGCxV_2KxKP4kb8L-g6En7gQL-LO8PgtEwSgdx6BuI2EY5y20WaCp1xgv6sFiqwnlsgiVeLRkjoRbwtu4vSZKZSG6XUwRMgi3QDiZlZuRcb8aetAZP2GRGFeOAF4H8zN2DsxIMkvC3qU-JN1Zp7JmpetXY7MewBn8QD53IcI22p_Hr1ie4lHLN3AuD168Y_UnAxZIqTp8wg1yuUCqpAHfkGZK9v7MxRLbfs46leYXLRGLiR2yJywbAhTxVi58Xm_Rk3Foogt75XHayLpcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
🇧🇷
در سال ۲۰۲۲ رافینیا از لحاظ تعداد گل های زده شده در مقایسه وینیسیوس بسیار عقب تر بود اما او امروز توانسته دو گل بیشتر از وینیسیوس به ثمر برساند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107765" target="_blank">📅 20:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107764">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4IltgvkgfwZtP624X-YKWY2STuc_aHA5pxBCTHT1P25fdIKr1gInNmFpGjFHCpI6P2j2WYIjX3OGTp0zfnXr9INHXKPhsyPzMAikrerWH5FXI5-OzNIj8uDZw-blvReApwus7bFsC3AwEi05v0kdottScn3jE-TD-hGYyLYiPSW-L41msI-M_gA-uAuS7Hge2r0UpZecMjBmm4JoguKlrZtE2MyOct-gSlb_cBGBXbsbEWH_QOo0dHkm08KFvplRoJqmtGinomf9IgPQHK3D6QxA-qsopwziyN1YJ3VURLA5rb1M-lW_-BfNmqRoyEJ0ynCLtb4jSDNd6IpdlKcmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
ویرجیل فن‌دایک در سال ٢٠٢۶ به اندازه کریستیانو رونالدو گل ملی بثمر رسانده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107764" target="_blank">📅 19:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107763">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cq1FSEnVGK-UiM08JOWtbZY86vO1wPtWi1V7HE2bGc62jvA4Mh2BSTU_WIBXn6NW7RKTiDuvLFq1TCKdNzg49iI0rQnySXkTvQYSqT0MOExAKy-TOIbliodN2J8ndHhV5Tm1A6r3ni5Jh2DD5nNlGwHOj2BXP5JrNJwHEzRCsj32RJLP-A5WQotxqhPPe2GEF6biolOfrzzpVqRCi70A0MofRpycsLAKvKtEa_XLBKoS0A3hzp_i4sro0lwqDl7m6Z7SDoC2hD7MNlUQHZFIerLp2DCO8WWbsUqyXReg5-AqMRwBdBH9e_q0bBO685wN5u7Lte6wAPoPsehCLUk75Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
روبرت لواندوفسکی پس از هت‌تریک برای تیم ملی لهستان در بازی امشب، شادی گل معروف لامین یامال کنار پرچم کرنر را تکرار کرد
🥹
🚩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107763" target="_blank">📅 19:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107762">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f408d58b0b.mp4?token=l4gwq34CIBhhjidsd0EYdiZHY1jiyHKTTLKCbvgK7JYQz8VzZLLbKnbieESU1PUt6wA-fgnHr4wnMFx6hareeiYHDDvbAIxn4CDrJUw2wDSBwL7U-w3wqj37S_ZbEfWD0WU_5bUEDFpFR8BRY2ysYKpAKJ1grUvnAhcP6aJBAIHpttg1ZobXGHyuFZ5dq_dTChpmvBQAqins7skgE8ONmdU1l3lEOzHVri2wktia9aq8vuPu_qFp5GtSDfrQdugMWjXGu5yqe0s-3eDtV47BniBtiZqLegsqazxJAoEsfKve66Xu0Oao0fdNEXfv_KPxCWwlQpD4U7LgXxgKgJRasg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f408d58b0b.mp4?token=l4gwq34CIBhhjidsd0EYdiZHY1jiyHKTTLKCbvgK7JYQz8VzZLLbKnbieESU1PUt6wA-fgnHr4wnMFx6hareeiYHDDvbAIxn4CDrJUw2wDSBwL7U-w3wqj37S_ZbEfWD0WU_5bUEDFpFR8BRY2ysYKpAKJ1grUvnAhcP6aJBAIHpttg1ZobXGHyuFZ5dq_dTChpmvBQAqins7skgE8ONmdU1l3lEOzHVri2wktia9aq8vuPu_qFp5GtSDfrQdugMWjXGu5yqe0s-3eDtV47BniBtiZqLegsqazxJAoEsfKve66Xu0Oao0fdNEXfv_KPxCWwlQpD4U7LgXxgKgJRasg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
ترو خدا هوش مصنوعی رو از ایرانیا جدا کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107762" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107761">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-gZmwVNxB1JR9GNMs34s5uIhd9dlMq1-QCbuF2Mm8PbXPW8cx3v8q3Ob6Bg8saXMMi6_VcZt6LwO4fhmth2Q5zM317k7fjus63eapVajQ5jrUUPb1G8VQq1MYvA01kXInGbji_SQnbj0h6UyCnZELjxQxRW8nJW5gS2uE7RSP1Fvz_o069i-QH2csc51H26knh74GtLuvw-Om5AUavPwvs2YdXK6oq2mUj51OEzso3SHahl2Btifk0tWtWXpv5tjdGIFpzuSblkTu-ix0YQfyS-IRV_SckD1sNECgcqksXRr__6Ld7hKCqQZJmtAkye9X12nG9ChOqa-Y4ROHjMag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇭🇷
ترکیب انگلیس و کرواسی؛ ساعت ۱۹:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107761" target="_blank">📅 18:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107760">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58fe91d1ea.mp4?token=QtxhybJeZNPyZ-8JsjeUvbBQOIkvp_s8s_96KCZwQEMG7-uhQa065RRYgUfMoNvXndfpw_YQHmjUix_GvT8TdQaB_OEWNJRKpXkvSo_7CaF4H_1iV_i8p779CDc9yTgv9Nz5FE40Bl9NeIlUg8Plhl8ySjgO7BiH0hARK5ZIyNpYsh4iNqYYepDqJrfH8RW16kjmPjFspoICU2lZ_M8dgD4ZkhPFMHM--JUZFa-5mn90cx_JlVEjEWGE89TKBrwqJXnP8Quosj1xkw0gKHdvk349lvnNuxDmijADVeiEWAHsRcjLYlPSiiqvxMEtnF4mwnbUQ2EV-3yPXmDp7SNszQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58fe91d1ea.mp4?token=QtxhybJeZNPyZ-8JsjeUvbBQOIkvp_s8s_96KCZwQEMG7-uhQa065RRYgUfMoNvXndfpw_YQHmjUix_GvT8TdQaB_OEWNJRKpXkvSo_7CaF4H_1iV_i8p779CDc9yTgv9Nz5FE40Bl9NeIlUg8Plhl8ySjgO7BiH0hARK5ZIyNpYsh4iNqYYepDqJrfH8RW16kjmPjFspoICU2lZ_M8dgD4ZkhPFMHM--JUZFa-5mn90cx_JlVEjEWGE89TKBrwqJXnP8Quosj1xkw0gKHdvk349lvnNuxDmijADVeiEWAHsRcjLYlPSiiqvxMEtnF4mwnbUQ2EV-3yPXmDp7SNszQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚪️
احسان حاج‌صفی: سعید الهویی، هومن افاضلی و رحمان رضایی جزو بهترین‌ها هستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107760" target="_blank">📅 18:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107759">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
‼️
کنفدراسیون فوتبال آسیا برای فصل آینده مسابقات تنها ورزشگاه‌هایی را قابل استفاده می‌داند که دارای سقف استاندارد باشند و بدین ترتیب تقریبا هیچکدام از ورزشگاه‌های ایرانی شرایط میزبانی از رقابت‌های آسیایی را ندارند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107759" target="_blank">📅 17:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107758">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXtIJICRaKDIXwCKLPMaCgwx-_tlGaykKxvvNJuNDoPWGMp1SaZain6lKQfsca1vdnm_CNDM0Qok15ZosBgIRV87rltiDxYkedRCDUWGIuJpqk30wyCaYQuaojlJgsskHdXzOicii4_blglJLZoBzhYX7OB-y5YTbDcab9cRi_0FZZ_3MZXsQXSAEYF9HLWBkNz3kgBuculUu8Xf8ri6GBxYYdVZcMsvbj4S9wqvF2hzsSeZIZ0bVO-ldz7qu-EltWCEyICf-XGBAlo9wIbLA3p2VOqpz4axanF27KReHWN1s1fZnmhxcTN5jZ2pfeHKzecHVvoH1tt9KdefiokMqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💵
دلار به 271 تومن رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107758" target="_blank">📅 17:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107757">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd85597f0.mp4?token=lF--8Hh6Upa4wTA3q-ezLmK_IstrXhavpQnBn1Yeky792C6DEc9yK0WEjKILxYb1k7auPd0MZ3wng6KLKoq7m9EgeA5PvU_pC_c4mmARe4kPlDIEXldW4jCIZMrxMeq1yo3rRRF_MJ1O9yMDlXGPg7T6B5EgRfE8kfoD08nNosTStE_ZxPFQU4MnBimjpF5ngMyMiYo20t5Mpg6KZaPC2P5zVQonzFaU71SsvTAu226JHCnugkJq8cZdQfmgbnkYwGWiqtw980OCqh6gbC11uQGau3C50rcTBNphYw3c6IAjr5R0K0ZV2-D3U_-xzlalJQHyL8SgmC7tgHcB5kemYWT75Enc4qfZGS9KBHrLNcPvnP7AgVZjMCIuUT0b-uuRXjmFMs0jPnu6fP3FDUGk1mYPXyp0jIqhbawMxS7Ja0UWsvWXJjxxD24KLkAe6igZSdmH0VfYqYKIbd4JGfGB5Gv5We7S552P5qWcJmleaYmcMsbhTw6Aq51r3cBngGyalVubdqUQE-dK_Wze1lx1LPS5I3HYhjkGP4Fh6Y_Lz06MlQxm1-_bYufUa4RCgPKTNdTrdUG2locI3cMZTHfjSmtOFKl993AYX8ltNJ2Z5qs5UgvNaQW5m2DN_p1OOUsvI4PCERM9_5rPAXppHD-pr4_3eiBN03fd4zkaHhQma2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd85597f0.mp4?token=lF--8Hh6Upa4wTA3q-ezLmK_IstrXhavpQnBn1Yeky792C6DEc9yK0WEjKILxYb1k7auPd0MZ3wng6KLKoq7m9EgeA5PvU_pC_c4mmARe4kPlDIEXldW4jCIZMrxMeq1yo3rRRF_MJ1O9yMDlXGPg7T6B5EgRfE8kfoD08nNosTStE_ZxPFQU4MnBimjpF5ngMyMiYo20t5Mpg6KZaPC2P5zVQonzFaU71SsvTAu226JHCnugkJq8cZdQfmgbnkYwGWiqtw980OCqh6gbC11uQGau3C50rcTBNphYw3c6IAjr5R0K0ZV2-D3U_-xzlalJQHyL8SgmC7tgHcB5kemYWT75Enc4qfZGS9KBHrLNcPvnP7AgVZjMCIuUT0b-uuRXjmFMs0jPnu6fP3FDUGk1mYPXyp0jIqhbawMxS7Ja0UWsvWXJjxxD24KLkAe6igZSdmH0VfYqYKIbd4JGfGB5Gv5We7S552P5qWcJmleaYmcMsbhTw6Aq51r3cBngGyalVubdqUQE-dK_Wze1lx1LPS5I3HYhjkGP4Fh6Y_Lz06MlQxm1-_bYufUa4RCgPKTNdTrdUG2locI3cMZTHfjSmtOFKl993AYX8ltNJ2Z5qs5UgvNaQW5m2DN_p1OOUsvI4PCERM9_5rPAXppHD-pr4_3eiBN03fd4zkaHhQma2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
گریه‌های بی پایان بازیکن سابق استقلال در شب دستگیری در کلانتری دماوند!
❌
خاطره بامزه بابک مرادی از دستگیری بازیکنان استقلال در شب سالگرد ازدواج مهدی قائدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107757" target="_blank">📅 17:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107756">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107756" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107756" target="_blank">📅 17:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107755">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JB1rs4J2eS97AqC6cpcRiTtNLc3DN3Rt1T1cRWpnI0SwjNiAKdTw5xPQsWEWsnQc8p2hO7Q2ovAPJ0W-MRW810acjbKz-MzF7yC7hiKjMstVg3BwFc9_2AJqGqauSoMbgKQnKwMtrOUfhte_4lY8hAzYJWzWDQXq-GUMvWYZ5VjvuuAuUqFyUVVmR470PyzZwX8PqiR_sfiyEc49QuoPEhDkfFYAR8ro5P7R6xP9Rjc923Yve7x7Auz3THnKgUfikcuQMpTyQw37oBqTgWwj1hrcvt4gSzLTgqAY3QLR6XejXaj9aiQyvcG0-OR1HQaZ_-wShc4t2wkG9DayyhIkfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107755" target="_blank">📅 17:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107754">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967556808b.mp4?token=A_dFsW01PlcrccyFbdR3sV0n4UG0Sng26AMUC4hbgqZelaw_GRiP0FTpXOyZsRPJqnO-Gon2DT9TKQx289DoYm70ynBCtmE4R8ElkwwBobgxopR-saaKi4moqLQJJd6_BvPgfrDZ7KNqScGCT2jTuCKhFfoUV7fYOCzrvMVG86tflUQ4WOGug6wuTJ9tX6OmDANSqCCw99xO_U1bsTLEoCG14pFHebxF6keit8HKGdf8xztQBhwS5AyxzSse1eNWCR9h3QJjr8fhyw3r0XQ939rCLiesAp8UVahgfnH1oHj2trm4kxnxHYBtrN-7K1XB9mWsbehXEHttpAeSDDBpeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967556808b.mp4?token=A_dFsW01PlcrccyFbdR3sV0n4UG0Sng26AMUC4hbgqZelaw_GRiP0FTpXOyZsRPJqnO-Gon2DT9TKQx289DoYm70ynBCtmE4R8ElkwwBobgxopR-saaKi4moqLQJJd6_BvPgfrDZ7KNqScGCT2jTuCKhFfoUV7fYOCzrvMVG86tflUQ4WOGug6wuTJ9tX6OmDANSqCCw99xO_U1bsTLEoCG14pFHebxF6keit8HKGdf8xztQBhwS5AyxzSse1eNWCR9h3QJjr8fhyw3r0XQ939rCLiesAp8UVahgfnH1oHj2trm4kxnxHYBtrN-7K1XB9mWsbehXEHttpAeSDDBpeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
و بشنوید از مدل ماشین دروازه‌بان اصلی و معروف تیم‌ملی اسپانیا یعنی اونای سیمون
👀
🚘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107754" target="_blank">📅 16:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107753">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b23bb5ad12.mp4?token=vmJI8Ka70TsM0aJ9bjO7rNkLkZ5WRFc8EAnI5EDxFIjfYIY_I1HMYMTEgFy0Gg5dnMZFIGwh2DLqGmrdgH9jm3Z-p-oEYzux6_3OAuzBvYJeD4kCey4i9vvtObeRvBxz6rloDxH21YfJg8Po0vIWHNLhyDXqBBL71aGV5M-nfgUyQWfLpQMOP6zyzDrucqY4V8JSJ1B_A8WQW1W0errzcTP8pImk-qqwpdeok8o3xJyO84m2WpqFlMW-OO9DTinD6URv51nnEIg2JNLKi6sSIe0SP8x19IOS4sxBA4PwdgIrCMwhJjEs4VGH6HhuOrnaqdMJhGcd6WaDiXFi3Gh38Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b23bb5ad12.mp4?token=vmJI8Ka70TsM0aJ9bjO7rNkLkZ5WRFc8EAnI5EDxFIjfYIY_I1HMYMTEgFy0Gg5dnMZFIGwh2DLqGmrdgH9jm3Z-p-oEYzux6_3OAuzBvYJeD4kCey4i9vvtObeRvBxz6rloDxH21YfJg8Po0vIWHNLhyDXqBBL71aGV5M-nfgUyQWfLpQMOP6zyzDrucqY4V8JSJ1B_A8WQW1W0errzcTP8pImk-qqwpdeok8o3xJyO84m2WpqFlMW-OO9DTinD6URv51nnEIg2JNLKi6sSIe0SP8x19IOS4sxBA4PwdgIrCMwhJjEs4VGH6HhuOrnaqdMJhGcd6WaDiXFi3Gh38Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✅
ویدیو کاربردی از نحوه جدید سوخت‌گیری که به تدریج در کل کشور اجرا خواهد شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107753" target="_blank">📅 16:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107752">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b48e9e7f4b.mp4?token=LPh4PGvzRGRbcYKEkZ6p3VfxvzC-Y5Ip2wFzFqe5k992kx__9Yv856ObNhbKnP7-337j4uYwRmM-4VLZKVAgqipDz7LHx5Cj2vWk3X7ifZBjI7tGsFC2l482DYyjKNapemAxIsR71pGLLqXU67IvLBhsrd48terk1z1njbN6X6oKiL0xcJsM8-o4_30OGbRlxvIgTZUQ82twJ7tWRLAwz__0GqXVJ_D655EU5jDtiQrbch4XN3U0l7sqqL2GUjn9ivSvxE9OT4gkBQdJSJdtaGTuY2GLF_TeW4sXN9Y2jQefWih734Z-aUW9y56BSgK52zSK4iEewcX658DmoqXpbY8Fpagadg5umQO9-1FBRaSiyLOzzqYCdsTp_cX40VMfwjw33jb_jpY4ZzRx7-kDlNwhOsJIb_igSuPo1QIx56R1_Ri9JJmlTyl4unp79i1heDiVQ6Z1frHPvCBpJEGQ4mCJJjNLHfFu2F44Hs2ZcGw46S_bOnuVkTL-SfyAR2h_RVIxKZV48fW-Rf_ddKtqaoddv2AjUebKfM4hTq5oGjDaEX65FhJY2jaVwB-ULreeWTSGxaXVriXULP521UIAL0f8XWTh1pr-vIXfy7njftjev_N1V5xewQAA4TnoVffyyQECTEh68Rv8RvBDHKmLJwG4ZTKOSshrlCntiwH8v_0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b48e9e7f4b.mp4?token=LPh4PGvzRGRbcYKEkZ6p3VfxvzC-Y5Ip2wFzFqe5k992kx__9Yv856ObNhbKnP7-337j4uYwRmM-4VLZKVAgqipDz7LHx5Cj2vWk3X7ifZBjI7tGsFC2l482DYyjKNapemAxIsR71pGLLqXU67IvLBhsrd48terk1z1njbN6X6oKiL0xcJsM8-o4_30OGbRlxvIgTZUQ82twJ7tWRLAwz__0GqXVJ_D655EU5jDtiQrbch4XN3U0l7sqqL2GUjn9ivSvxE9OT4gkBQdJSJdtaGTuY2GLF_TeW4sXN9Y2jQefWih734Z-aUW9y56BSgK52zSK4iEewcX658DmoqXpbY8Fpagadg5umQO9-1FBRaSiyLOzzqYCdsTp_cX40VMfwjw33jb_jpY4ZzRx7-kDlNwhOsJIb_igSuPo1QIx56R1_Ri9JJmlTyl4unp79i1heDiVQ6Z1frHPvCBpJEGQ4mCJJjNLHfFu2F44Hs2ZcGw46S_bOnuVkTL-SfyAR2h_RVIxKZV48fW-Rf_ddKtqaoddv2AjUebKfM4hTq5oGjDaEX65FhJY2jaVwB-ULreeWTSGxaXVriXULP521UIAL0f8XWTh1pr-vIXfy7njftjev_N1V5xewQAA4TnoVffyyQECTEh68Rv8RvBDHKmLJwG4ZTKOSshrlCntiwH8v_0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عجب دوران‌کودکی جذابی رو‌ پشت‌سر گذاشتیم...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107752" target="_blank">📅 16:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107751">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9d2f3d6a6.mp4?token=Cxu3laDZMTvYT6zq4pkO-NNs_Df9amyC8jFCGer8sso_n_c0y0x2Z0OcmyiIztghQbB0syti2IC3g9VEvgr1AP0iJt1CkHwVbGh-6Z7Ln8_QtL0i6bl1Dbnw8cedYUkOnKPt25PO1NQCcmHuxYvvrHgba8SzLVPi0VaCdg351HAvdVdZ0kXxWLXzMlyvVr0PDppk5KbCL7JGcUg-XQBeg3lwSD4LO8FfIbeYf-kfpbPQKolVQH6-20Uc8aS4U20boiPOpXlsKtJAtWfP9tyCEPG9P7J9sgA5ZTGLkTkZiA_qPvQODAGFyHd4oCl3n7wA6id_s8GVVxVjS1vU-szwKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9d2f3d6a6.mp4?token=Cxu3laDZMTvYT6zq4pkO-NNs_Df9amyC8jFCGer8sso_n_c0y0x2Z0OcmyiIztghQbB0syti2IC3g9VEvgr1AP0iJt1CkHwVbGh-6Z7Ln8_QtL0i6bl1Dbnw8cedYUkOnKPt25PO1NQCcmHuxYvvrHgba8SzLVPi0VaCdg351HAvdVdZ0kXxWLXzMlyvVr0PDppk5KbCL7JGcUg-XQBeg3lwSD4LO8FfIbeYf-kfpbPQKolVQH6-20Uc8aS4U20boiPOpXlsKtJAtWfP9tyCEPG9P7J9sgA5ZTGLkTkZiA_qPvQODAGFyHd4oCl3n7wA6id_s8GVVxVjS1vU-szwKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⚪️
بازنده‌های پر سروصدا یعنی اعضای تیم‌ملی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107751" target="_blank">📅 15:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107750">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvUgOnqBrD23EP-8yy9vFCGIHosEGn9stT_GSucStl4DwdxnLIuRmNtWx3g6k5FhqZ7F0MDrokLBoMvfW9sYSxSQUz2_4iyqHThF6VFsw74gZeHfw7iHiRWwjBAWdc6fGr1fQ6pzSuT-9nE0_lqJBkrWfunufVk3vhT3my7x4nQ9Kmd9Wm-AU8l5Bi6W5Gv4ZISmRnwDAWPAA9AsU8suvkHC72NSwRmLTCE8Zy_N3PEyxBppt640jL8GSXCASPG3qrqmhd4Ak1GUZ1jymFaXzifopxkHzUZ085rYSZiE4er3-_ftbBa4aooWETWdHS7QWawjnz-ZKUAnPm-p-DhtXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇺
میسا رودریگز "تحت تاثیر" قانون "پنالتی به سبک مارک پوبیل" قرار گرفت که اکنون توسط یوفا اعمال می‌شود.
❌
در بازی پاریس و آرسنال در لیگ قهرمانان زنان، یک حرکت مشابه حرکتی که مدافع اتلتیکو و دروازه‌بان موسو در برابر بارسلونا انجام دادند، به عنوان یک خطا (پنالتی) اعلام شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107750" target="_blank">📅 15:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107749">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🇪🇸
رومانو: بارسلونا پس از فیفادی قرارداد سه بازیکن یعنی رافینیا، برنال و ژاوی اسپارت را تمدید میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107749" target="_blank">📅 15:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107748">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86371ca1ee.mp4?token=GZaAvIiTwYNN-Lmd0Asifwlqf_7Tu2VCMQRN_Nz4ke1LGWebWkNBjT9fkhcYYh8cLDjdkBbxcAz7El-O2H25E9UzdHjtzcLXzLH5tkOhWS7YXPJUzQQkpWjX2Ke7Qq4dA_zYVEqiHL2E1MK5Tq_8_cyzH7DZsoTl4KHT9EGEfgVfsoyor35eFcZlaAHWqgGvZSq_OA2xVcTJFmS-9zM_pk2LaJq56dfA_OntIbOhPPMBbVtRSfmE0UtLAkSq2b0da-uG960v-I8ULzc4srcAGdAhzzulJvEQDQQykDmMXGmwS9jCs18xZta_--lFLvPwEJr6TuCZGy3e2NPVGnM7noi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86371ca1ee.mp4?token=GZaAvIiTwYNN-Lmd0Asifwlqf_7Tu2VCMQRN_Nz4ke1LGWebWkNBjT9fkhcYYh8cLDjdkBbxcAz7El-O2H25E9UzdHjtzcLXzLH5tkOhWS7YXPJUzQQkpWjX2Ke7Qq4dA_zYVEqiHL2E1MK5Tq_8_cyzH7DZsoTl4KHT9EGEfgVfsoyor35eFcZlaAHWqgGvZSq_OA2xVcTJFmS-9zM_pk2LaJq56dfA_OntIbOhPPMBbVtRSfmE0UtLAkSq2b0da-uG960v-I8ULzc4srcAGdAhzzulJvEQDQQykDmMXGmwS9jCs18xZta_--lFLvPwEJr6TuCZGy3e2NPVGnM7noi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مهدوی‌کیا: دوره پرولایسنس در آلمان در یک سال برگزار می‌شود؛ در ایران ٩ روزه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107748" target="_blank">📅 14:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107747">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e10be0d86.mp4?token=lHEKHNWAQH2iD6_3K1S9G4bUM92dd7ZNt-OdV5jqnhPXeX5kj8wBIlSlukvKFHcssekOTucgaMa2IkftIn9p4eYFqeLBAch2fEjXRi3WqdMJlynypfV2xGwSLCVLU-zWBD1dFM3eQquvT8GYyxMf2RaGWKxG1wmLj_NZdu010_iz_lzoywKnhGTrb0jDij2DcOdlTqBLw5Hl6HlUbPkE3FTBQrVFdZX_ncgqpI4IRiuS94kuyyzRuue5m9f4_RJ8eDmZNPuwVM2gA--d7kNGtw3_FlwTTVWxkYFjYtmdQyqbkkdN-ulVQRJ5O6_KMbEMzKPLJqhK0p_f85My8Ovt8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e10be0d86.mp4?token=lHEKHNWAQH2iD6_3K1S9G4bUM92dd7ZNt-OdV5jqnhPXeX5kj8wBIlSlukvKFHcssekOTucgaMa2IkftIn9p4eYFqeLBAch2fEjXRi3WqdMJlynypfV2xGwSLCVLU-zWBD1dFM3eQquvT8GYyxMf2RaGWKxG1wmLj_NZdu010_iz_lzoywKnhGTrb0jDij2DcOdlTqBLw5Hl6HlUbPkE3FTBQrVFdZX_ncgqpI4IRiuS94kuyyzRuue5m9f4_RJ8eDmZNPuwVM2gA--d7kNGtw3_FlwTTVWxkYFjYtmdQyqbkkdN-ulVQRJ5O6_KMbEMzKPLJqhK0p_f85My8Ovt8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
😳
ویدیوی وایرال شده از کلاس تخلیه گریه برای بانوان در تهران! این خانم‌ها برای تخلیه احساسات خود در کلاس‌ها پول پرداخت می‌کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107747" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107746">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd4b89af76.mp4?token=ZKMbNyb8XMoU8fxt_0UbJKcTNzWysFe-yhoiFXP0J3OkR6krgn1ZCttpK7p4UXLhyUt1ceNJE2A483bFD83WKE0jD4331Exyb8sfwLJr4zNeGZmYWh3U_KzgbXCxegDDjOnPLVQ48lnsM3KRGAUUPDhOBRE3xNyfs2dnDv_1qJBmJ5ble5zxKhaRvGDSEQYNeb3zCd0riNY0wQ0A4-nGtvDYIUOU1piGFvzcwnnuK4dTPOz47DQuRihFt-foiFLq6i2jA2oOiU6T3lFhnVj1oo9qLYoH8R7S4Bs8ZnpxHz-ytDuZLvTeA7EwRljIFwAVKxxafR5ZgEy41EoqV1W0r0EIhlsKD3AFCDU5yfgCrZzDCCP0rtU1ox_nfTwJQtsVemNIz08wv0TzLNorA0gTMsAt6IjtbgVAiPgg6PQ80nQFJScFba1647olkwmn_j4lVu4ENvKqU-aWojqUPhkhZ2ITFdZ8dOLT9y9DQoQFKPxIccTxWwJZTR7wBDwrpgmnUPOON5BysCHiLEg0e6zvS9XU1_bXhYTLGt194uSSbfYbQbQYoif8y81t85HMwP-BYYXEnlipZ8i8tyzPoPzf1mK1UU19vQGNeo_8p-8RwTze4ds-Vs49FshKC_sF6rE0toX_bkfursivv_uzcZkie0yexK4Tb4N2sQbUhWmihLU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd4b89af76.mp4?token=ZKMbNyb8XMoU8fxt_0UbJKcTNzWysFe-yhoiFXP0J3OkR6krgn1ZCttpK7p4UXLhyUt1ceNJE2A483bFD83WKE0jD4331Exyb8sfwLJr4zNeGZmYWh3U_KzgbXCxegDDjOnPLVQ48lnsM3KRGAUUPDhOBRE3xNyfs2dnDv_1qJBmJ5ble5zxKhaRvGDSEQYNeb3zCd0riNY0wQ0A4-nGtvDYIUOU1piGFvzcwnnuK4dTPOz47DQuRihFt-foiFLq6i2jA2oOiU6T3lFhnVj1oo9qLYoH8R7S4Bs8ZnpxHz-ytDuZLvTeA7EwRljIFwAVKxxafR5ZgEy41EoqV1W0r0EIhlsKD3AFCDU5yfgCrZzDCCP0rtU1ox_nfTwJQtsVemNIz08wv0TzLNorA0gTMsAt6IjtbgVAiPgg6PQ80nQFJScFba1647olkwmn_j4lVu4ENvKqU-aWojqUPhkhZ2ITFdZ8dOLT9y9DQoQFKPxIccTxWwJZTR7wBDwrpgmnUPOON5BysCHiLEg0e6zvS9XU1_bXhYTLGt194uSSbfYbQbQYoif8y81t85HMwP-BYYXEnlipZ8i8tyzPoPzf1mK1UU19vQGNeo_8p-8RwTze4ds-Vs49FshKC_sF6rE0toX_bkfursivv_uzcZkie0yexK4Tb4N2sQbUhWmihLU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇹
یکسال پیش در چنین روزی برتری پرتغال به رهبری رونالدو مقابل اسپانیا در فینال لیگ‌ملت‌های اروپا و قهرمانی در این مسابقات!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107746" target="_blank">📅 14:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107745">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9decbe8c9.mp4?token=f8PYOMJ0_ww8CW7qyMm0nS4RueQoGLO4aPYbfEwOweWrbof2ULEwBy2oN-S2jJ1wezjYaX1Imp0CG_875HflFHySDkfwOv6uqc3nqLjfYvKYZf-vwEiMGJeZ8W8XVH2aegC62zZEulo2UMNeyX6xJ6oXjG6eQ14E1xPTkkkxNtfwxEZn1hUMvZKuzoLX8mbcEn4TW8dVd0U9vJi3k1bMhzKMg2RFSHCkwa39msfGQSinPJmnmAQlWDJQKk34GsVB6j_C_Yj5h1mwgjj6RCYLtgrrR_YS_HSMoIr3lb0sMftJmbdCHbK2JJDVPBRRdVFXoyyRBw_cMQ8LwYjigjU9vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9decbe8c9.mp4?token=f8PYOMJ0_ww8CW7qyMm0nS4RueQoGLO4aPYbfEwOweWrbof2ULEwBy2oN-S2jJ1wezjYaX1Imp0CG_875HflFHySDkfwOv6uqc3nqLjfYvKYZf-vwEiMGJeZ8W8XVH2aegC62zZEulo2UMNeyX6xJ6oXjG6eQ14E1xPTkkkxNtfwxEZn1hUMvZKuzoLX8mbcEn4TW8dVd0U9vJi3k1bMhzKMg2RFSHCkwa39msfGQSinPJmnmAQlWDJQKk34GsVB6j_C_Yj5h1mwgjj6RCYLtgrrR_YS_HSMoIr3lb0sMftJmbdCHbK2JJDVPBRRdVFXoyyRBw_cMQ8LwYjigjU9vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
یک شرکت فرآورده‌های گوشتی به این شکل کاملا منطقی تبلیغ سوسیس‌هاشو کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107745" target="_blank">📅 13:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107744">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c197e3a2a3.mp4?token=TmfgxD8OGCNlGB4tv4EJMNMOZT6aL26cdpt6QEzYPZZrbe6AkzR-PyIu6vcl57rsyhMocI0pO7hxvxCOJizSjJdux4to0GBitbs1JayLeWv9rXhuWDZD0U24WHMdgTVIcERooq1RZ6XZUxFNZPNhxi2PMlKQnJ4hvPJy866gGN3Eq0BumV41lPRUU-ZYGiUWG4nCPCpKEV50Yowxp4uM4jaggtOSzxBu65R-2rzHgbwPGuWztWaGSk0X03Hir6T3qMwZ0Sx7VDDIL3kQ6FK0fFgsOxaZshEO8SWNNBpSylkCBB0LaNQYnYz2uHpYcfMkJpOqAJxj1uIZtwCVxO8IW6DOHbuxl-LBYNwWPzFKqygjbmE7avxEvSbbMzN48wQzFcGFEQHWUJcahrKXA9ZUL-SjBngEtbu_8u7R6ot2j__LjMF2zwW4Gyxq9nECCbADzenbJuE4AG8S6np4DvIHpOJV-u1jeQ_2i8sWsaSRwKceFhUEwYWhuCuv6gEgQA7ddIMJLv317oJ4p3wFK-3nVt3WuirYqqMu5ZcWD8Y90sOBc84Qenp-Rubh9kdY62hKesxijmWv7gLxgs7Sk5nN2cL5A3a_36Bm3jYBsikqsWyuNmSQ74NR_fkb8RKUK0JjfD6krmv6QBagfJuSGztR-N4DjIXx_J8aF9Ir7eABldo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c197e3a2a3.mp4?token=TmfgxD8OGCNlGB4tv4EJMNMOZT6aL26cdpt6QEzYPZZrbe6AkzR-PyIu6vcl57rsyhMocI0pO7hxvxCOJizSjJdux4to0GBitbs1JayLeWv9rXhuWDZD0U24WHMdgTVIcERooq1RZ6XZUxFNZPNhxi2PMlKQnJ4hvPJy866gGN3Eq0BumV41lPRUU-ZYGiUWG4nCPCpKEV50Yowxp4uM4jaggtOSzxBu65R-2rzHgbwPGuWztWaGSk0X03Hir6T3qMwZ0Sx7VDDIL3kQ6FK0fFgsOxaZshEO8SWNNBpSylkCBB0LaNQYnYz2uHpYcfMkJpOqAJxj1uIZtwCVxO8IW6DOHbuxl-LBYNwWPzFKqygjbmE7avxEvSbbMzN48wQzFcGFEQHWUJcahrKXA9ZUL-SjBngEtbu_8u7R6ot2j__LjMF2zwW4Gyxq9nECCbADzenbJuE4AG8S6np4DvIHpOJV-u1jeQ_2i8sWsaSRwKceFhUEwYWhuCuv6gEgQA7ddIMJLv317oJ4p3wFK-3nVt3WuirYqqMu5ZcWD8Y90sOBc84Qenp-Rubh9kdY62hKesxijmWv7gLxgs7Sk5nN2cL5A3a_36Bm3jYBsikqsWyuNmSQ74NR_fkb8RKUK0JjfD6krmv6QBagfJuSGztR-N4DjIXx_J8aF9Ir7eABldo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🥇
کامبک جانانه یونس امامی در مقابل کشتی گیر ژاپنی و کسب مدال طلا بازی های آسیایی ناگویا با گزارش ابوذر کرمی نیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107744" target="_blank">📅 13:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107743">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vA8ZdFms93GF0nc5hePp0XFwa2J-uXrH6zxgsPM-VSBmQJLE7gT_jFZB3YaGQhtk9FfZCnIQE9kwaGy6uQlKuO-1nTdn7PoEKENChwabQUZOVFjKisS2GbXRwMa4rH3ceGKMi_AV4NYMeOQ-Y-ptEn05AFQfyG-GyRS-dHFHqNYUI2pP6A_1M6ssvhSyU_9LxR6xGB4FUwhw-loFjtq2Wi3nFo9n4vm2RODMgHr-GBVH8C7R56Maq-QH0HojEjsrMIzYn1ylhUTz7RCSRM-0_NufACFawk8I4pQ7Fp7dmCcNDVmpq1yRh699iPiKfP6KFiLnMVKp1JGMGOZM9EQryQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
رافینیا در این‌فصل از مسابقات فوتبال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107743" target="_blank">📅 13:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107742">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/096e7cab86.mp4?token=Crt4-DNR-G1cS20ZOJvwAr189_MKtXcWvZzubXSlXiCuat9g0bMyqvDfNfP0vtlddaKRdu19fwfwPPz18ygdHardavLAPstEjSN7hKAE9CoQ5jYc88orgQXKe73MRpcsEQiiXL_VUDSvtrCZEGO6MbsQB0LPXSLvJRlXubruP9Xqezh3ti0LqV91hzV76EhkJMpqRShYO60BIAtecm28nGA8jjb47igwC_9ZcHphaKkoBfPF16l-ZM3u3PCuVnlk2icmVs3C-z9CkDUr7vYv2FonSghwkK7WPdGa2L3sX_eTBU8-m93_VHviYqKpfZSqWdu1mtIVB_gPbOg_Td1wdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/096e7cab86.mp4?token=Crt4-DNR-G1cS20ZOJvwAr189_MKtXcWvZzubXSlXiCuat9g0bMyqvDfNfP0vtlddaKRdu19fwfwPPz18ygdHardavLAPstEjSN7hKAE9CoQ5jYc88orgQXKe73MRpcsEQiiXL_VUDSvtrCZEGO6MbsQB0LPXSLvJRlXubruP9Xqezh3ti0LqV91hzV76EhkJMpqRShYO60BIAtecm28nGA8jjb47igwC_9ZcHphaKkoBfPF16l-ZM3u3PCuVnlk2icmVs3C-z9CkDUr7vYv2FonSghwkK7WPdGa2L3sX_eTBU8-m93_VHviYqKpfZSqWdu1mtIVB_gPbOg_Td1wdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
میکروفون باز، کار دست گزارشگر داد؛ جمله جنجالی هادی عامل علیه حسن یزدانی!
🔻
در حالی که پیروزی امیرعلی آذرپیرا مقابل آرش یوشیدا یکی از مهم‌ترین اتفاقات صبح کشتی ایران در بازی‌های آسیایی ناگویا بود، صحبت‌های پشت صحنه و خارج از گزارش روی آنتن زنده، یک حاشیه بزرگ برای کشتی ایران ساخت.
🔹
❌
👀
هادی عامل: صبر کنید ببینید اگه (یوشیدا) تو مسابقات جهانی به حسن (یزدانی) بخوره، ببینید با حسن چیکار می‌کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107742" target="_blank">📅 13:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107741">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35b732453.mp4?token=Fk2gw3ohi23RaJ3y-1Vb9VCCeg2GdJpdJHdZo6e4KD_tzGCmZcpQlxS2G0qNPfRAugNVLwyy5Gnz0ZL8DydDb1dqQkWXiWAzbbCick9xHMKRdUKEOra7uMJtqyYDTodlt4te0T2RGJEW-GTVUsNqkQueCsH_C5wWAlu--qDXMxNVw5MWhX6nwVxJKo5EG3yoKKm2AOGTznPN5g28yotRz-6KPEo47ign22JwevRZpyO17SWAU6BViJ-IvB1e4k6qGTJBQh-bcNmo84ASvT94EpzEclZTe8qAahe8dACrJTGsCA1WicMOC7nUyQzro1zlIeSiSDydF5RpAbf-HaxWMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35b732453.mp4?token=Fk2gw3ohi23RaJ3y-1Vb9VCCeg2GdJpdJHdZo6e4KD_tzGCmZcpQlxS2G0qNPfRAugNVLwyy5Gnz0ZL8DydDb1dqQkWXiWAzbbCick9xHMKRdUKEOra7uMJtqyYDTodlt4te0T2RGJEW-GTVUsNqkQueCsH_C5wWAlu--qDXMxNVw5MWhX6nwVxJKo5EG3yoKKm2AOGTznPN5g28yotRz-6KPEo47ign22JwevRZpyO17SWAU6BViJ-IvB1e4k6qGTJBQh-bcNmo84ASvT94EpzEclZTe8qAahe8dACrJTGsCA1WicMOC7nUyQzro1zlIeSiSDydF5RpAbf-HaxWMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
گزارش‌های مستهجن و عجیب گزارشگر تکواندو صداوسیما در بازی‌های آسیایی ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107741" target="_blank">📅 13:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107740">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ls2zEdwtHevg1ORlBvQdTL6ASY0pybiSVT75fYgQu7Vct6xYCB9ZQklAZ_oNA3odTUJifisSDChIeEFLQAYY9_O0abg1eckaULpOVKMMn4cl2osKCJ9ufIrH5Y5sUZOoi1twAhumuWJuRMaccnXLArSkkXcPNM2G15Is5xqmKorjrKfmM_CPuYVtKvwdD8reKFcJatRVlIHgW4NmNdNnIVk3gfWoHXDS85hiSom6alrf1Kz8WHpH3GTdf9a367_369JCKpmx6gGlJ7Wheayka-6l5jMfGlnfWsTdOP1vDmNyQk6IxStyEXaavN23G_kG1mJq70vDxBJrCNNk9G9pWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
📊
برترین گلزنان تاریخ‌بازی‌های ملی؛ حضور اسطوره علی‌دایی از ایران در رده سوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107740" target="_blank">📅 12:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107739">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/888405197c.mp4?token=vzkMqp0G8IQk56-Nq8GwfDNCfgvFVtGTBGwoPEnyImj6XlpEd2TTZcNgWIiCiN_Trjzub3CjvHEF0DLZCjnSaO0kWpSu20XzjhDORP3rZ4qfZaKoys-9ptSXjolSjqRmUWeQUURFMeri7dMkRkw4lqw-d6Bgkc2WB1-HNi7i3Fm1xtKQOX0gjCBqRvyB4Q35fLUl5hYEQa8ReD0Aw_nhgf0wakHBpTIANtAWP227C6hcnOurwKNIlB0cQJhYeFbQzOlY37HnpNsvc47rW8_eJ1CWB_vcbt9mQ5WT2z84YjDxwX3LxbQlW33Isk_6JpWvhNpx-_FgZjDgbHLd5zQ7NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/888405197c.mp4?token=vzkMqp0G8IQk56-Nq8GwfDNCfgvFVtGTBGwoPEnyImj6XlpEd2TTZcNgWIiCiN_Trjzub3CjvHEF0DLZCjnSaO0kWpSu20XzjhDORP3rZ4qfZaKoys-9ptSXjolSjqRmUWeQUURFMeri7dMkRkw4lqw-d6Bgkc2WB1-HNi7i3Fm1xtKQOX0gjCBqRvyB4Q35fLUl5hYEQa8ReD0Aw_nhgf0wakHBpTIANtAWP227C6hcnOurwKNIlB0cQJhYeFbQzOlY37HnpNsvc47rW8_eJ1CWB_vcbt9mQ5WT2z84YjDxwX3LxbQlW33Isk_6JpWvhNpx-_FgZjDgbHLd5zQ7NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
ناراحتی‌ و گریه ناهید‌کیانی بعد حذف شدن از مسابقات آسیایی تکواندو ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107739" target="_blank">📅 12:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107738">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56498866f7.mp4?token=upxLYYBSZZYaHuaZOFAwTuUi35VO3ok2v916IW87dfHf-_XUQusB_m03K-GFKDYwF8IVcJwXp0qi9cK8AX3jS57tSdHXWdAejY4I3tNdiSQRiNsMH107LLuJJPpyGcU_LE3_CmuuYHSeHPp5GRw48d3-mxvOH4tlhir6W6L4zLkKuN3CzJ8BvndDbhaaSd63ueZ2cRlax_MFws3BZJox2xrH5A6-Rl3PEKmfdUKPEMfAs-9aipBprUNL_nPQtvBaqDpK-WDv6q--0DB1jyYAhO9ZLbQq-jtbT32pEWABDEcALtwFcbIYFyTMAX6Cr7WMG0yqOMRF7wIKYMuEsuJSVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56498866f7.mp4?token=upxLYYBSZZYaHuaZOFAwTuUi35VO3ok2v916IW87dfHf-_XUQusB_m03K-GFKDYwF8IVcJwXp0qi9cK8AX3jS57tSdHXWdAejY4I3tNdiSQRiNsMH107LLuJJPpyGcU_LE3_CmuuYHSeHPp5GRw48d3-mxvOH4tlhir6W6L4zLkKuN3CzJ8BvndDbhaaSd63ueZ2cRlax_MFws3BZJox2xrH5A6-Rl3PEKmfdUKPEMfAs-9aipBprUNL_nPQtvBaqDpK-WDv6q--0DB1jyYAhO9ZLbQq-jtbT32pEWABDEcALtwFcbIYFyTMAX6Cr7WMG0yqOMRF7wIKYMuEsuJSVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
👀
گزارشگر تکواندو رو مشاهده میکنید این چنین در اوج در حال گزارش است
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107738" target="_blank">📅 12:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107737">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9OBtuxj7kI23woCCHx2rqxsAA1iBfLDXEFXaBHDrWwfAERQ5D1tfxhHlYvEJN_L3hsR7a9c62qtn3Wkz4bYjL1UTC6DhcflFTUSgkODNzEoXXjsM1kAloQZo-ePzfMkIvb8SH2zwC0IDa7amIo525VM88cxAg-Lw7NGukosXlJTarji4jjha7Zl-NTgM2Ht--bPkavVlkasr4jgwQ-kzyLFXcUiW8h-Tk1j2uQJNY9sVxtmfu4DfjJ8a-pShHec7zNsKic_1k-xnOZS3rWmlpCKC9b2b3RjYdDNTHYBaaaOPXPc9MpdKMKRyi1dkci7DUOvkHft7rrRiYigkcP0YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
مسابقات لیگ‌ملت‌های آسیا به شکل اروپا قرار است از شهریور ۱۴۰۶ آغاز شود. ایران در سطح یک این مسابقات قرار خواهد گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107737" target="_blank">📅 12:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107736">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lg5L_IxHPU97QxGKTOXmmmnXcBOkeTMLeiHbUevutQ-qAiyTlT-ApbVGcj0P1DUW14mmNGKjaXKoEGrWGSDK-N5ez-lVamQCQ5lm9QwK5aMzPnDq7AiyqQvH93TBVWBvClRfpiI3zpVlJEQsaXdLbW0ojYPILo9_S7P7uzT2eYQdMSiO1xuc285uuzXukCevQYdacKy8EoOvbZgMQ0VswrqXDGJjRRiHQnKtvqcH5Vif4-jvEeXb-JI6XjL7j5lheY0v9mRKh3-CA5YJS_ipYExbh6EYblyCkwG4JI_Ex0zQDeL3jWYyM1pfJlCJYntwJioQd87vgFgy7HxnV6AePg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
اسامی نفرات برتر آزمون کنکور ۱۴۰۵؛ نتایج اولیه برای تمامی داوطلبان تا ساعاتی دیگه اعلام میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107736" target="_blank">📅 11:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107735">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6316faf3f3.mp4?token=WYQ8CAMo9lz6ukatctjSF46UNxgxg5LooKkSaGh8z_ni2J_G6XWjTkY-ErkLjMc8ZDF8bfDqpbZ1lQokjGXKL80uZtD7xytZFqj-LgwvdhAp2Rgu26wn63baM76w8Wx3R2hARfVp16BPN4lS-1u7es-s_4hvbhifed_X_f3K2vjd_Xq4dmYFNU0tTM83zUMQZsPmgCgsfV6GJJk4DwKScAoY2NX5MfbEp4Ijuz6RMHonXKBBqgSqiJs7gPQ589Vt5ZqrcErlDPaxFv8B65_Wa_HGhPp7F-Co53Y5DCLU4RUDGQX-moiWJs2NaARbmTr-KqJRgF50SiYsmkNpuKtkJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6316faf3f3.mp4?token=WYQ8CAMo9lz6ukatctjSF46UNxgxg5LooKkSaGh8z_ni2J_G6XWjTkY-ErkLjMc8ZDF8bfDqpbZ1lQokjGXKL80uZtD7xytZFqj-LgwvdhAp2Rgu26wn63baM76w8Wx3R2hARfVp16BPN4lS-1u7es-s_4hvbhifed_X_f3K2vjd_Xq4dmYFNU0tTM83zUMQZsPmgCgsfV6GJJk4DwKScAoY2NX5MfbEp4Ijuz6RMHonXKBBqgSqiJs7gPQ589Vt5ZqrcErlDPaxFv8B65_Wa_HGhPp7F-Co53Y5DCLU4RUDGQX-moiWJs2NaARbmTr-KqJRgF50SiYsmkNpuKtkJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
شبکه سه اومد بازی جودوکار خانم ایران تو مسابقات آسیایی رو پخش کنه که جودکار ایرانی تو ثانیه اول درجا بازیو باخت و حذف شد ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107735" target="_blank">📅 11:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107734">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107734" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107734" target="_blank">📅 11:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107733">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIzrfkpieFPFZGvFlFlpaV9GR8Id0I5vk7hPq5dDZVVH2pTlTQlBDIuqLX5_4oBRWZ7w6g1TFtK0MZAzyCRXUny8UpYOS1OI28OhGGnboKKYX1b91iTt89_dpIOyoA2iRSkexHjYEIGRebffdaTR6pVVDDgP1CFyEr-KOnLCfbrvTHjc7C1-iLxjlKeDDHbesLI9vqsOrh1Oy7Obs5TUG-i4XAviSTPK5Cqw_yv9BwB7YvgLdwlbyuRUCRiHM3bEQBywPJg6XMdVTJ4fUbdEeF-P29FXG1Xq7L-K039otB0GSWS2yD7cTyG7ncpOcUgcEIQsxqBWSad1RkjYsHObqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107733" target="_blank">📅 11:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107732">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68d8475315.mp4?token=BPnzB-JxXSMTpzQJ0C4clwJzLTaJHUYkTQEsr5ARuR_7HdXIglylGHHAkHb0qplaEAMrdsTMHVUY21l4hKwOKXEC1gqJrh-fDJs1kXnyWf2rUNjdHwc_sp5UwHczWT54CmnjSUyUdVG47LFPhw70OT7rhU934S5HHzVqUuFCTucBl0Si5mNSJP4xldB8pirEskCYNtNKS9nnVpNFoqLJTeeMPaP-IHOss9K_NaaQX584h6IsOgRFDwq0LYOQC2b2Xr0q1_LboTBrRvT0GyxZyRSGRthbPE_jP2PRhb5YL7OFWOkbwSfNEIDTHZhB-3tXQgpt2HSJVsWmR-WWomdp6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68d8475315.mp4?token=BPnzB-JxXSMTpzQJ0C4clwJzLTaJHUYkTQEsr5ARuR_7HdXIglylGHHAkHb0qplaEAMrdsTMHVUY21l4hKwOKXEC1gqJrh-fDJs1kXnyWf2rUNjdHwc_sp5UwHczWT54CmnjSUyUdVG47LFPhw70OT7rhU934S5HHzVqUuFCTucBl0Si5mNSJP4xldB8pirEskCYNtNKS9nnVpNFoqLJTeeMPaP-IHOss9K_NaaQX584h6IsOgRFDwq0LYOQC2b2Xr0q1_LboTBrRvT0GyxZyRSGRthbPE_jP2PRhb5YL7OFWOkbwSfNEIDTHZhB-3tXQgpt2HSJVsWmR-WWomdp6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
⚠️
دو قاب از بيژن‌مرتضوی به فاصله ۴ سال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107732" target="_blank">📅 11:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107731">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fbb258d04.mp4?token=chwGspxPDYC13fHvsElbgtMcy743bLLk_klVlsyGlMTGlKaXjMOTXOPem8dFHhDuKtlNQdVoX7G90kxZ6xXkurcbnsMCDXYZy_hy2Z7rnBe_EPI3QzbocaOugBcPoLCvjxYDF5ryUZurxnqZ-a3p7nHEorp2Q9-WPdkTeliec7F1JoVwDukzXq9Jqv3iQZc6o0tkQpjMBcpwjCdn9dQDSjb-BfRdMzRalKfiO5Rz66lS5reaLsDYTrGTwdO5GLs3P1SinW1kLb1V8pxMDlo2N3L076E22Mk7N9-ggKr2wWFwPw2mdtnGLMfsdxdG6RS54YEcPFOl_RObUe58Hzi3cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fbb258d04.mp4?token=chwGspxPDYC13fHvsElbgtMcy743bLLk_klVlsyGlMTGlKaXjMOTXOPem8dFHhDuKtlNQdVoX7G90kxZ6xXkurcbnsMCDXYZy_hy2Z7rnBe_EPI3QzbocaOugBcPoLCvjxYDF5ryUZurxnqZ-a3p7nHEorp2Q9-WPdkTeliec7F1JoVwDukzXq9Jqv3iQZc6o0tkQpjMBcpwjCdn9dQDSjb-BfRdMzRalKfiO5Rz66lS5reaLsDYTrGTwdO5GLs3P1SinW1kLb1V8pxMDlo2N3L076E22Mk7N9-ggKr2wWFwPw2mdtnGLMfsdxdG6RS54YEcPFOl_RObUe58Hzi3cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚪️
نه به تیم‌ملی چیز جدید اضافه کردن و نه تونستن جام خاصی به ارمغان بیارن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107731" target="_blank">📅 11:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107730">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8086af61bd.mp4?token=Uvqc9RJNNt7SEDD52DpWTr8s7xklMdQAnHju_hB2k4K_RtLNpwMih4tN3jSWA67JBaYh5ifAN62spWIXzuL_i_aCWuooYV4pJERjKyrojK5lR6je2l1LHTIAudLgtKioijNMsNXKXPhyJD012QsIKG67UDcq_krvuMB0Ahk148F_cJATWeJ43cvYcorZnK0Ni2LauADVjgkPGkflSViw1PGDSPlQvVPjHBpxzl762Hp5mwit59HqRH7lQZsALkIzOJUsX_JXN46hjo8vqsSbrLmw-FS8b-_eL8PMeW00lUe6a2LpwpNzKbt-jf1shZ1_DyKwD0aklBqTY1Pc2JY5Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8086af61bd.mp4?token=Uvqc9RJNNt7SEDD52DpWTr8s7xklMdQAnHju_hB2k4K_RtLNpwMih4tN3jSWA67JBaYh5ifAN62spWIXzuL_i_aCWuooYV4pJERjKyrojK5lR6je2l1LHTIAudLgtKioijNMsNXKXPhyJD012QsIKG67UDcq_krvuMB0Ahk148F_cJATWeJ43cvYcorZnK0Ni2LauADVjgkPGkflSViw1PGDSPlQvVPjHBpxzl762Hp5mwit59HqRH7lQZsALkIzOJUsX_JXN46hjo8vqsSbrLmw-FS8b-_eL8PMeW00lUe6a2LpwpNzKbt-jf1shZ1_DyKwD0aklBqTY1Pc2JY5Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
▶️
تلخ‌ترین صحبت‌های مالک موبو نیوز در گفتگو با امیرحسین قیاسی...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107730" target="_blank">📅 10:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107729">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdae91c6ba.mp4?token=fZvRWqboZK5TCO0og5uZ8uYp_7FUw5sTv7ddYwpDZX_iP6FJNRiZ1hntTDUuh4HRioWDIC9lvafAOA1P-qz4exmjpwDszk2FfwSd7_I9OpqneRg1eiPkPG4qNPUp4ZR0yy46iipDBAGxLD9GK1g410E6HAyV5S25LlW3F-0rELVQZpTXDAfmbkPGRJt2-azhKgTrV2KQ5sZ8wm63mk3TRGu99-dIrIIfbVx-N1_P3rOcg1_IVSMMlO_U3JJoVmejLAEEARb6tvIEHDXu74606mxNvm_graG9AmemxHf_ZilRWeUAek5xgdSYCamP1dgRdhQdgYIxWdBix5RRfjK2Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdae91c6ba.mp4?token=fZvRWqboZK5TCO0og5uZ8uYp_7FUw5sTv7ddYwpDZX_iP6FJNRiZ1hntTDUuh4HRioWDIC9lvafAOA1P-qz4exmjpwDszk2FfwSd7_I9OpqneRg1eiPkPG4qNPUp4ZR0yy46iipDBAGxLD9GK1g410E6HAyV5S25LlW3F-0rELVQZpTXDAfmbkPGRJt2-azhKgTrV2KQ5sZ8wm63mk3TRGu99-dIrIIfbVx-N1_P3rOcg1_IVSMMlO_U3JJoVmejLAEEARb6tvIEHDXu74606mxNvm_graG9AmemxHf_ZilRWeUAek5xgdSYCamP1dgRdhQdgYIxWdBix5RRfjK2Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
یه راه خوب برای کنترل هزینه‌های اینترنت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107729" target="_blank">📅 10:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107728">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c37b6c6ac.mp4?token=hHQq_Esg7YWv2F4TT3_IJ0H3_eQz70XHg6oPSCRxSJtG4RhhCKtimazusu65EIjWUakie1j3vl0xH74AbUhtZGCM97qJpAYjOBdGksq027j081CKwxaeyW3QpBEKnrpRPdvQr5WJhkCGPGPnClr57aIojhhQdiJKPKOEYyap7bDCZ1JYxGQhJOjr6v8nYSh9i_k0OWMNcnkKSP8CWBHAxfJzHP0EOPULwSIDRtoW95u3LGaw4yM_q2KXjS3PYuI4q75verxk43Wrg2bhH3c_0bEnWtnUvaYR3zswsjpKvu-Sm-JzKhoNodGxFl-_hFvnKzt1zTzGtq4cCSocBCNQVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c37b6c6ac.mp4?token=hHQq_Esg7YWv2F4TT3_IJ0H3_eQz70XHg6oPSCRxSJtG4RhhCKtimazusu65EIjWUakie1j3vl0xH74AbUhtZGCM97qJpAYjOBdGksq027j081CKwxaeyW3QpBEKnrpRPdvQr5WJhkCGPGPnClr57aIojhhQdiJKPKOEYyap7bDCZ1JYxGQhJOjr6v8nYSh9i_k0OWMNcnkKSP8CWBHAxfJzHP0EOPULwSIDRtoW95u3LGaw4yM_q2KXjS3PYuI4q75verxk43Wrg2bhH3c_0bEnWtnUvaYR3zswsjpKvu-Sm-JzKhoNodGxFl-_hFvnKzt1zTzGtq4cCSocBCNQVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بیخیالی بازیکن های پرتغال از رفتن رونالدو دقیقا یاد این سکانس تاریخی میندازه !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107728" target="_blank">📅 09:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107727">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LF-XuZy7xxmPsNt2n3yEns2Z_uodfBOwCpGZW0nG2D-XEnFDec-u3W1HuYtbiGfE1azQwjmaas54MV4uIf_KuEOVouBUOhP9B88ibU4J6SH_cgDKTSbXIxGj0oiWzqljhrnWX9be_3kGvTi6-n92_lBESHa_HxwvB2YgzCqPLFoAqJ0hV2havZXyap6iwG96cX1MkK70AfwJVh1EqIzGzsFGMVIwL__NVmfxsd21_mIIUE1plXBywbBfwE7SW55Me48LBn175UdLivui7hBHRkqkLYRfgokvh1IVAMqOv6pui4C2K0unzyGJkFbpt7Ml1-0tuQLE3ZLM6czM0DxVIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
با اعلام‌رومانو: ریاض‌محرز با عقد قراردادی به الشمال قطر، رقیب استقلال و تراکتور در لیگ‌نخبگان آسیا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107727" target="_blank">📅 09:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107726">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b5c7684c2.mp4?token=YvsLy25w1iZUbZN-rMsk-VXfqpBX_GDf8WAJ3se1K9P7myWgPZnGRt1LGSL-EklwxICAIqbiqYbgmI9OgoEr9aZykMSvErFSgb1WzOzqkWy_JHS77p-uTzhc9DKLAYFrMvnQmfJ8q9IbOJnv4bw8mfOmkibKDGCkkfKdkS08iZvIiDPIvJKEQ3rIhz-_bYoQzKZFgW9xPdslKsP4vKpvvTQBxQ9q3cY7Z9x6DGdNveywaSSUIhb8EgwOqjehobc4m_Kc0zyz9YgDVHeSbt_hdxAd7G5F-Loi_9PeT_6rhZNyVktJW1ol_v90jRWpd8fQGyIUJYwhjl9gJL8WoOmO2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b5c7684c2.mp4?token=YvsLy25w1iZUbZN-rMsk-VXfqpBX_GDf8WAJ3se1K9P7myWgPZnGRt1LGSL-EklwxICAIqbiqYbgmI9OgoEr9aZykMSvErFSgb1WzOzqkWy_JHS77p-uTzhc9DKLAYFrMvnQmfJ8q9IbOJnv4bw8mfOmkibKDGCkkfKdkS08iZvIiDPIvJKEQ3rIhz-_bYoQzKZFgW9xPdslKsP4vKpvvTQBxQ9q3cY7Z9x6DGdNveywaSSUIhb8EgwOqjehobc4m_Kc0zyz9YgDVHeSbt_hdxAd7G5F-Loi_9PeT_6rhZNyVktJW1ol_v90jRWpd8fQGyIUJYwhjl9gJL8WoOmO2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚪️
سقوط تیم‌ملی به روایت اصغر مازیار!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107726" target="_blank">📅 09:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107725">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d02e44cc.mp4?token=qY1w6Uh7RDpXqOUSQflAmyjHwCdrfYvChlCuC-kB-Ocl6iyU1_mEdGFMpw84QBDZJJI3b_pn14RDcHawT82Q5Qp0mf4O1zTnv-vbDoiAsw954DgVnTZ2-gxxsuKe7Y-LfaYVfyCxGsifEjQeGF8v0EHuMVZIB0BXTw5hEnllzYqVttOjz3LkoVzoGzTeNWa-jo9LGrdzdqjf3mdQkzp_HnGfnG1wlIO3HypIdfgj5vNcihrvZq_YuF_5o-hifIJqChQzWpDvMqI0gt6PKXxD1t1ThA3TohORYqeZkHqZGhzFt1u2T6LVjrbLNOp4MqpCtLqcOREeYRddu353gDE-gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d02e44cc.mp4?token=qY1w6Uh7RDpXqOUSQflAmyjHwCdrfYvChlCuC-kB-Ocl6iyU1_mEdGFMpw84QBDZJJI3b_pn14RDcHawT82Q5Qp0mf4O1zTnv-vbDoiAsw954DgVnTZ2-gxxsuKe7Y-LfaYVfyCxGsifEjQeGF8v0EHuMVZIB0BXTw5hEnllzYqVttOjz3LkoVzoGzTeNWa-jo9LGrdzdqjf3mdQkzp_HnGfnG1wlIO3HypIdfgj5vNcihrvZq_YuF_5o-hifIJqChQzWpDvMqI0gt6PKXxD1t1ThA3TohORYqeZkHqZGhzFt1u2T6LVjrbLNOp4MqpCtLqcOREeYRddu353gDE-gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وای این چه سمی بوددددد
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107725" target="_blank">📅 08:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107721">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107721" target="_blank">📅 00:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107720">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIk1_x5LEGyqw1TQINvOrsBsmKivalwuGuMKuUtFVIKioyPk7dZ3oGjouZMhbEJ8tDDXVYV-ys9JsJHy1-nQ5kvk1XajeAclUFpu5LKmHCivFR4NgRoYbb6traSuQYoTMeEgQJ6BWyD7hI_mv-AE64B7mOpJwAP5HTgNEEy9te41CcGeOsGWOoPe-uXzGOMeKVDGSsGTRMZZvCNzSrePly0LIP-ryl0x6asCpeNVVeEio7W8-HeeIC_an8e7oSdNOvzG67j5aSeGTQEjZFjMHeotqVNl_lMMnz9BixLmPmUFUiHG5kh0pL4nhK5S8dSD7FhbgTLRES-R9fMd9SPS2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
بنر هواداران عربستانی برای بازی مقابل قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107720" target="_blank">📅 00:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107719">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇹
🇫🇷
هایلایت بازی فرانسه یک - یک ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107719" target="_blank">📅 00:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107718">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
❌
🇮🇷
علوی، سخنگوی فدراسیون فوتبال: استقلال قهرمان فصل گذشته نشده و بحث جدیدی درمورد اهدای جام به این تیم نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107718" target="_blank">📅 00:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107717">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b540d3428e.mp4?token=dYIXY9CBXS8jYjSszL1TNf_-gu54mwXHe_SmGAxrW33BzI-MDmRNCzOFh1B4yQnezcux_u8W8Wd6dn5HtxT0dsyyL8rZpc5iDuXH9pyyrVfgJLj_cvhjiH-odmeVedZgqOsh3H8Nx7KjtWIGB0bBfDDFTGorB5md2JPO0vGidrwXF8-NfQjiIh6tyq0sz9eZUoHZUUe7O4TO5lKPl_SZrVC3BRaoMCN6B6K-0iUl_f1d3iBsI4X0xGn8Ud49njKSJJGf829uv-xb41xyCE-pz83XSbi9Uz250-8is3VF1bjxq_eEnJrgOpF2TjynEdSDzcvqMcCWvRmx5afYdiX9qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b540d3428e.mp4?token=dYIXY9CBXS8jYjSszL1TNf_-gu54mwXHe_SmGAxrW33BzI-MDmRNCzOFh1B4yQnezcux_u8W8Wd6dn5HtxT0dsyyL8rZpc5iDuXH9pyyrVfgJLj_cvhjiH-odmeVedZgqOsh3H8Nx7KjtWIGB0bBfDDFTGorB5md2JPO0vGidrwXF8-NfQjiIh6tyq0sz9eZUoHZUUe7O4TO5lKPl_SZrVC3BRaoMCN6B6K-0iUl_f1d3iBsI4X0xGn8Ud49njKSJJGf829uv-xb41xyCE-pz83XSbi9Uz250-8is3VF1bjxq_eEnJrgOpF2TjynEdSDzcvqMcCWvRmx5afYdiX9qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇧🇪
گل‌سوم بلژیک به ترکیه توسط لوکاکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107717" target="_blank">📅 23:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107716">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5cfe007c4.mp4?token=SXp22_r6H8FL3-_OY-gwdXLbcwxDwXwkxqluMvXvQzHHBDYfPQwAUnG17sB0Qvv6c97aXjZ53L9NvaoKfel4-kM7DxucyDYhhnJ6rt4WbG1ZlQRotHppW2OlxGxiyWcdFNM5OPsqmFqU5_oyDYbnZrpuF4vypF2bP7mNUgucYkf6a7xqDqwsFBc44p9hLOr1GK0Vp2BDmuzcLzX2kYIK1JRKppCGLbbrNU7si8nB9JLJUwNYe7GeIbI9PL8FbGdeNRN9Fdd5QiEyqrYui69hN8TD3sxm620qTY6pZOttPfv4bSH5vuPesu9ohu7yUK-w7tRNNdHdTv3Fkfdeiq_QfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5cfe007c4.mp4?token=SXp22_r6H8FL3-_OY-gwdXLbcwxDwXwkxqluMvXvQzHHBDYfPQwAUnG17sB0Qvv6c97aXjZ53L9NvaoKfel4-kM7DxucyDYhhnJ6rt4WbG1ZlQRotHppW2OlxGxiyWcdFNM5OPsqmFqU5_oyDYbnZrpuF4vypF2bP7mNUgucYkf6a7xqDqwsFBc44p9hLOr1GK0Vp2BDmuzcLzX2kYIK1JRKppCGLbbrNU7si8nB9JLJUwNYe7GeIbI9PL8FbGdeNRN9Fdd5QiEyqrYui69hN8TD3sxm620qTY6pZOttPfv4bSH5vuPesu9ohu7yUK-w7tRNNdHdTv3Fkfdeiq_QfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇹
گل‌اول ایتالیا به فرانسه توسط باستونی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107716" target="_blank">📅 23:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107715">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f73a4fb35.mp4?token=n2-NKQBi2_ocnkmzmXrcRh_7OBIisvbM-fmfd0VDl2bsYqT-LyR13Vd9mfAfQN0NjstIXe_2qWD0Z7WBpaC8JU0f24Qxcc2hhf-YGFI5wc6GASSNsOPBnMT5AdX3NFqE-MY3L0oxB2UHMYG02dO6jtz2xlADhMaA23MdfrkJosspu28s9eH6BJ63bZE7LwjFjpz3pJ4Fb--0FOJCsBl79cCI60Ck4DjCg6_SwYPOkGJ5eqUenAW4qMSrGfI_fdF_ATCGHKNqE9HoCj6ko_9Y-NZOqffrFWjHrPRQ2XXW4Z-A4UK8yLO6uRJ2z3bSA1VjGw7cWanGo1mATvR0bXe0iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f73a4fb35.mp4?token=n2-NKQBi2_ocnkmzmXrcRh_7OBIisvbM-fmfd0VDl2bsYqT-LyR13Vd9mfAfQN0NjstIXe_2qWD0Z7WBpaC8JU0f24Qxcc2hhf-YGFI5wc6GASSNsOPBnMT5AdX3NFqE-MY3L0oxB2UHMYG02dO6jtz2xlADhMaA23MdfrkJosspu28s9eH6BJ63bZE7LwjFjpz3pJ4Fb--0FOJCsBl79cCI60Ck4DjCg6_SwYPOkGJ5eqUenAW4qMSrGfI_fdF_ATCGHKNqE9HoCj6ko_9Y-NZOqffrFWjHrPRQ2XXW4Z-A4UK8yLO6uRJ2z3bSA1VjGw7cWanGo1mATvR0bXe0iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
✔️
گل‌تماشایی کوین دیبروینه مقابل ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107715" target="_blank">📅 23:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107714">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گلگلگلگلگلگلگ دوم بلژیک به ترکیهههههه دیبروینهههه</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107714" target="_blank">📅 23:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107713">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3dc430d99.mp4?token=fBG7FKKGQ97x-tng5aFvmvylMqtY-QHa5GTNIT5BCmSZXSHhiPfP9DHIpArNl1ckFeJEXQmd0_CmXF54ciXExIldnYVRo1o-8oS4JSFua-jhDYAQGl1tJvoJR9QeTtgelzTqNFPc3D5y-ZT7osNQImyySegIx6FCrJKWLp2qyJefxBJUnDlTLH1BYRmz7SovyF5dUZxSF3VB7bQLYPwbB07LKwlMwg11d9hvk455_m2hJ4BODaWPP4bWoKR-9e_TZzIjA7kG-WRKxdNxfMrspZPnFQcu0UjjdA6eHrltVK3-_MgZiFpvqlKNO6eECgVf83-aii5MNo10t2kqLhtBBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3dc430d99.mp4?token=fBG7FKKGQ97x-tng5aFvmvylMqtY-QHa5GTNIT5BCmSZXSHhiPfP9DHIpArNl1ckFeJEXQmd0_CmXF54ciXExIldnYVRo1o-8oS4JSFua-jhDYAQGl1tJvoJR9QeTtgelzTqNFPc3D5y-ZT7osNQImyySegIx6FCrJKWLp2qyJefxBJUnDlTLH1BYRmz7SovyF5dUZxSF3VB7bQLYPwbB07LKwlMwg11d9hvk455_m2hJ4BODaWPP4bWoKR-9e_TZzIjA7kG-WRKxdNxfMrspZPnFQcu0UjjdA6eHrltVK3-_MgZiFpvqlKNO6eECgVf83-aii5MNo10t2kqLhtBBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🤯
سوپرگل دیدنی اولیسه مقابل ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107713" target="_blank">📅 23:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107712">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سوپرگل اولیسهههههههههه</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107712" target="_blank">📅 23:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107711">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فرانسهههههه زددددددد</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107711" target="_blank">📅 23:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107710">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گلگلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107710" target="_blank">📅 23:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107709">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e970c7c18a.mp4?token=Fcs-yiPg5cPnSyzakKPbPz_ygAzTe-LYI66qOfIE7aAIGz-Jaee437m9AlYBDxCCN0BAvCwjq01jZIQyyextudccb7M_b3eFWczjLS_oUI2-y3KSBxebbvcwx0Pw4KdPX2mj3vmXNEXZZznIypIONl4xysofReMJPSNN2LZsjq5pnBIzqKryI6h0nDoVDZepPt_i1OtChvefOTG6CSKtJCj6XSJZwChBl2Jy7mncx1lBn-6jMJYycVGh2v8Q5bK6leaZ8RVKoxAFj-syiGaWEW1snHal4FOgJXBMGdrtUM6xZmPIbrV9UG-sHeSESkE-xXevK0Caj57JchaBiU96Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e970c7c18a.mp4?token=Fcs-yiPg5cPnSyzakKPbPz_ygAzTe-LYI66qOfIE7aAIGz-Jaee437m9AlYBDxCCN0BAvCwjq01jZIQyyextudccb7M_b3eFWczjLS_oUI2-y3KSBxebbvcwx0Pw4KdPX2mj3vmXNEXZZznIypIONl4xysofReMJPSNN2LZsjq5pnBIzqKryI6h0nDoVDZepPt_i1OtChvefOTG6CSKtJCj6XSJZwChBl2Jy7mncx1lBn-6jMJYycVGh2v8Q5bK6leaZ8RVKoxAFj-syiGaWEW1snHal4FOgJXBMGdrtUM6xZmPIbrV9UG-sHeSESkE-xXevK0Caj57JchaBiU96Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
استقبال بی نظیر و خوش آمدگویی هواداران به زین الدین زیدان سرمربی جدید فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107709" target="_blank">📅 22:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107708">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0312a011f.mp4?token=Ks4gC9noa4jwjtN3rS9rU4YANeAovB5V4SooahG-WuLwPkRVtdbYTgN9YT33zzvIeE5ja1ZcQgdQwwHznl9MIWYfeSFvnLYdTImjziOCvgw2B11-0dakDfLJw3FjkeU12ZvA326TS2t9DlBq1ZOCjt4VpoB-EAa05s8igTqgxw27J8lX0r5p_h-K3CPLS7FdhBuBWFA2WEYotjpBDzspZgxZTJcTrk1-EQxhCydjGgyDaXJtGXDObTi0Hu0wQqN4lHP0t0iayj0EgwGd4q6wG0mTelRVOYVQYKWQ0jxUPKz-e63lmdv3j6NGbTmK-MiAjcGiPQ7BWWIWDMqLe28GyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0312a011f.mp4?token=Ks4gC9noa4jwjtN3rS9rU4YANeAovB5V4SooahG-WuLwPkRVtdbYTgN9YT33zzvIeE5ja1ZcQgdQwwHznl9MIWYfeSFvnLYdTImjziOCvgw2B11-0dakDfLJw3FjkeU12ZvA326TS2t9DlBq1ZOCjt4VpoB-EAa05s8igTqgxw27J8lX0r5p_h-K3CPLS7FdhBuBWFA2WEYotjpBDzspZgxZTJcTrk1-EQxhCydjGgyDaXJtGXDObTi0Hu0wQqN4lHP0t0iayj0EgwGd4q6wG0mTelRVOYVQYKWQ0jxUPKz-e63lmdv3j6NGbTmK-MiAjcGiPQ7BWWIWDMqLe28GyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل‌اول بلژیک به ترکیه توسط کوین دیبروینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107708" target="_blank">📅 22:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107707">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f5c780577.mp4?token=GrVusowH9FFNgVOieeYxRPvS4VASAoo7Z3a9UyTzg3Io98VlmOY2IyQOX2JT8mZWOv83YX0AvNFQEamNFB1I-sCmi6YEyow2RWw1m4GBxMxe1M5yMAmlzcfKLuMpA3NDJJ9pFhLMVkoGoZgAECs6fC-8PA21i_lj8a40IjbmndwITZFLJhFbiRgshaPzY2NTdvU3oUdkX_77bXvzlqtaaKx80dsKclgPD0xjHOfxFxsJY6mp_9Cmrp6WE7ahqoZAKTrSnqpxEn6MEEQ5Xkw_HjX6Vof3KMGVrJyaKqwMRwfDbHH1UAYmnkzYOI8qAnHsKR9RJH24I1eod5b9NIaNTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f5c780577.mp4?token=GrVusowH9FFNgVOieeYxRPvS4VASAoo7Z3a9UyTzg3Io98VlmOY2IyQOX2JT8mZWOv83YX0AvNFQEamNFB1I-sCmi6YEyow2RWw1m4GBxMxe1M5yMAmlzcfKLuMpA3NDJJ9pFhLMVkoGoZgAECs6fC-8PA21i_lj8a40IjbmndwITZFLJhFbiRgshaPzY2NTdvU3oUdkX_77bXvzlqtaaKx80dsKclgPD0xjHOfxFxsJY6mp_9Cmrp6WE7ahqoZAKTrSnqpxEn6MEEQ5Xkw_HjX6Vof3KMGVrJyaKqwMRwfDbHH1UAYmnkzYOI8qAnHsKR9RJH24I1eod5b9NIaNTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
علوی، سخنگوی فدراسیون فوتبال: استقلال قهرمان فصل گذشته نشده و بحث جدیدی درمورد اهدای جام به این تیم نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107707" target="_blank">📅 22:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107706">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3539953949.mp4?token=nAD7vInMmOiTYNWUHNECfclOMxPt7cLlHMaMnbFT4mgz084l8SbcrO5nycvDQARkoptLowY3XA2ZYHJzbTi8bkb0-oaNasPFReU6zg4vIkwELHOH1TJcpRhRIZ7Wr7IMjKjouFrKuJsnUVfh7cU6rYhDLMRW822YzpN3Xh-dWcI656SFUw8hMu19Owv-S_7KSeT_1VRv5lqYTp6tEr5mHDdKFnLmkjh38EP6IOImHS576m-WJEagLVdRGCbiDq3w4YN-aa3fxlXK0U0B--RfUxEz2sxlmMKoVC1z7jDMdYcPAtMmAokCsW5SttyM3ReWQxNee0EdtBPoIhmvnQCQkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3539953949.mp4?token=nAD7vInMmOiTYNWUHNECfclOMxPt7cLlHMaMnbFT4mgz084l8SbcrO5nycvDQARkoptLowY3XA2ZYHJzbTi8bkb0-oaNasPFReU6zg4vIkwELHOH1TJcpRhRIZ7Wr7IMjKjouFrKuJsnUVfh7cU6rYhDLMRW822YzpN3Xh-dWcI656SFUw8hMu19Owv-S_7KSeT_1VRv5lqYTp6tEr5mHDdKFnLmkjh38EP6IOImHS576m-WJEagLVdRGCbiDq3w4YN-aa3fxlXK0U0B--RfUxEz2sxlmMKoVC1z7jDMdYcPAtMmAokCsW5SttyM3ReWQxNee0EdtBPoIhmvnQCQkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حاج صفی: می گویند آقای قلعه نویی با یک نفر(جواد نکونام) مشکل دارد که من را به تیم ملی دعوت کند تا رکورد آن فرد را بزنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107706" target="_blank">📅 21:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107705">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYZSTjQZRrbJn1e262HVoVMlJAwgdiJgrNg9WTuXSrZdjn40XNRgHcSIyAeRklMgcwDPmbX-B6osi6NsXBeBXhkakhvHJm52p3TauMc9Flx0WxxA7wSWy634CBXm0g0T33xyIEzHDJSINeLHdpI7lYg3BaazgvMPZW_yHFqOV_BmkTabKj9xEzULafFKdlyI-IjuBP3VIjdaauVBvGZO2fqsbDUv_g1sHh5SQbDCRwVgM-3ZZawvWPH4ArHVsgI-Av5heTPSfFl44QUxunVHi_g1I6jWXLDPqyFz1DAXmqz97AZf1OWVqHD04xL7C--Ix-QdLenDH09Japq3Q-jiMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب تیم‌ملی فرانسه مقابل ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107705" target="_blank">📅 21:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107704">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPcvY799BiJRLsM0GpQ8Us1_Xic5LCajuYpqPaEkkEHOraKgjaO4ARGSw4U45-hjcc5if29iIjmDq0vG-_zA25mGT_QiO8Pee01Kx0iPH7qvk66KWNrYELOVJsWS45QdJcyZeGoS-MPwR_b0UYgBV3JEIr6AvCR5xJP6vrjdsrMSUbR8p8i7eE-NAn2ZRkxrkFdyxL4fTK20Pd-rSR5oVIr5BaG3QHQJaHnGoragTIEnbw3P0Wm_tQ_pGJxsBJt6YWwlasNL4UmRUAKe2-Oa5Hydg9GjXz5uWLI1fSq279iEeG2f7J4LlO481tKbnhtwRf4JibJ4l-Exzd8F0uG40A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
پیش‌بینی‌های زلاتان از برخی نتایج فصل:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیگ برتر انگلیس؟ منچستر سیتی.
🇪🇸
🇪🇸
لیگ اسپانیا؟ بارسلونا.
🇪🇺
🇪🇸
لیگ قهرمانان اروپا؟ بارسلونا.
🏆
توپ طلایی؟ لامین یامال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107704" target="_blank">📅 20:45 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
